#!/usr/bin/env python3
"""Põe o resultado do teste (bench/resultados/resumo.json) dentro dos 3 guias (PT, EN, ES).

Uso: python3 bench/injeta.py   (rode depois de `roda.py resumo`)
O tamanho de cada modelo vem do `ollama list` desta máquina.
"""
import json, re, subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
REPO = RAIZ.parent
res = json.loads((RAIZ / "resultados" / "resumo.json").read_text())
casos = json.loads((RAIZ / "casos.json").read_text())

tam = {}
for linha in subprocess.run(["ollama", "list"], capture_output=True, text=True).stdout.splitlines()[1:]:
    p = linha.split()
    if len(p) >= 4:
        tam[p[0]] = p[2]  # ex.: "17" (GB)

linhas = []
for l in res["linhas"]:
    if not l["casos"].startswith(str(sum(len(t["casos"]) for t in casos["tarefas"].values()))):
        continue  # só modelo com todos os casos
    l = dict(l)
    l["gb"] = tam.get(l["modelo"], "?")
    linhas.append(l)

bench = {"maquina": "NVIDIA GB10 · 128 GB · Ollama 0.33",
         "casos": sum(len(t["casos"]) for t in casos["tarefas"].values()),
         "data": "24/10/2026", "linhas": linhas}
js = json.dumps(bench, ensure_ascii=False, separators=(",", ":"))
for arq in ["guia/index.html", "guia/en/index.html", "guia/es/index.html"]:
    p = REPO / arq
    if not p.exists():
        continue
    s = p.read_text()
    novo, n = re.subn(r"/\*BENCH\*/.*?/\*FIM\*/", lambda m: "/*BENCH*/" + js + "/*FIM*/", s, flags=re.S)
    if n:
        p.write_text(novo)
        print(f"{arq}: {len(linhas)} modelos")
