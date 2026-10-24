#!/usr/bin/env python3
"""Benchmark PT de tarefas de PME com modelos abertos no Ollama local.

Uso:
  python3 bench/roda.py rodar  --modelos llama3.1:8b,qwen2.5:14b   # roda e grava bench/resultados/<modelo>.jsonl
  python3 bench/roda.py resumo                                      # nota tudo e gera resumo.json + kit/benchmark-pt.csv
  Para testar na SUA máquina sem misturar com a rodada publicada, use outra pasta:
  python3 bench/roda.py rodar --modelos qwen3.6:35b-a3b --saida bench/minha-rodada

Só chama o Ollama da própria máquina (http://localhost:11434). Nenhuma API externa.
Um modelo por vez: descarrega o anterior antes de carregar o próximo.
"""
import json, re, sys, time, unicodedata, urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
CASOS = json.loads((RAIZ / "casos.json").read_text())
RES = RAIZ / "resultados"
OLLAMA = "http://localhost:11434"


def post(caminho, corpo, timeout=300):
    req = urllib.request.Request(OLLAMA + caminho, data=json.dumps(corpo).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def carregados():
    with urllib.request.urlopen(OLLAMA + "/api/ps", timeout=30) as r:
        return [m["name"] for m in json.loads(r.read()).get("models", [])]


def descarrega_tudo():
    for nome in carregados():
        post("/api/generate", {"model": nome, "keep_alive": 0})
    for _ in range(60):
        if not carregados():
            return
        time.sleep(2)
    raise SystemExit("Ollama não descarregou os modelos em 2 min; pare antes de seguir.")


def rodar(modelos):
    RES.mkdir(parents=True, exist_ok=True)
    for modelo in modelos:
        descarrega_tudo()
        saida = RES / (modelo.replace(":", "_").replace("/", "_") + ".jsonl")
        feitos = set()
        if saida.exists():
            feitos = {json.loads(l)["id"] for l in saida.read_text().splitlines() if l.strip()}
        print(f"== {modelo}", flush=True)
        with saida.open("a") as f:
            for tid, t in CASOS["tarefas"].items():
                for c in t["casos"]:
                    if c["id"] in feitos:
                        continue
                    corpo = {"model": modelo, "stream": False, "think": False, "keep_alive": "10m",
                             "messages": [{"role": "system", "content": t["instrucao"]},
                                          {"role": "user", "content": c["entrada"]}],
                             "options": {"temperature": 0, "num_ctx": 8192, "num_predict": 512}}
                    if t["json"]:
                        corpo["format"] = "json"
                    t0 = time.time()
                    try:
                        r = post("/api/chat", corpo)
                        texto = r["message"]["content"]
                        reg = {"id": c["id"], "tarefa": tid, "modelo": modelo, "saida": texto,
                               "seg": round(time.time() - t0, 2),
                               "load_s": round(r.get("load_duration", 0) / 1e9, 2),
                               "tokens": r.get("eval_count", 0),
                               "prompt_tokens": r.get("prompt_eval_count", 0),
                               "gen_s": round(r.get("eval_duration", 0) / 1e9, 3)}
                    except Exception as e:  # registra a falha e segue
                        reg = {"id": c["id"], "tarefa": tid, "modelo": modelo, "saida": "",
                               "erro": str(e)[:200], "seg": round(time.time() - t0, 2)}
                    f.write(json.dumps(reg, ensure_ascii=False) + "\n")
                    f.flush()
                    print(f"  {c['id']:6} {reg['seg']:6.1f}s", flush=True)
    descarrega_tudo()


# ---------- nota ----------
def sem_acento(s):
    return "".join(ch for ch in unicodedata.normalize("NFD", str(s)) if unicodedata.category(ch) != "Mn").lower().strip()


def limpa(texto):
    return re.sub(r"<think>.*?</think>", "", texto or "", flags=re.S).strip()


def acha_json(texto):
    texto = limpa(texto)
    m = re.search(r"\{.*\}", texto, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except Exception:
        return None


def num(v):
    if isinstance(v, bool) or v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = re.sub(r"[^\d,.\-]", "", str(v))
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".")
    elif "," in s:
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def campo_ok(chave, esperado, obtido):
    if obtido is None:
        return False
    if chave in ("cnpj_emitente",):
        return re.sub(r"\D", "", str(obtido)) == esperado
    if chave == "numero":
        d = re.sub(r"\D", "", str(obtido))
        return d != "" and int(d) == int(esperado)
    if chave == "data_emissao":
        return str(obtido)[:10] == esperado
    if chave in ("valor_total", "valor_mensal", "multa_percentual"):
        n = num(obtido)
        return n is not None and abs(n - esperado) < 0.011
    if chave in ("qtd_itens", "prazo_meses"):
        n = num(obtido)
        return n is not None and int(n) == esperado
    if chave == "indice_reajuste":
        return re.sub(r"[^a-z]", "", sem_acento(obtido)).startswith(re.sub(r"[^a-z]", "", sem_acento(esperado)))
    if chave == "foro_cidade":
        return sem_acento(esperado) in sem_acento(obtido)
    if chave == "intencao":
        return sem_acento(obtido).replace("ç", "c") == esperado
    if chave == "urgente":
        if isinstance(obtido, str):
            obtido = sem_acento(obtido) in ("true", "sim", "verdadeiro")
        return bool(obtido) == esperado
    return obtido == esperado


def nota_caso(tid, caso, saida):
    t = CASOS["tarefas"][tid]
    if t["json"]:
        js = acha_json(saida)
        if not isinstance(js, dict):
            return 0.0, False
        campos = {k: v for k, v in caso["esperado"].items() if v is not None}
        certos = sum(campo_ok(k, v, js.get(k)) for k, v in campos.items())
        return certos / len(campos), True
    texto = limpa(saida)
    # frase que nega ("não posso dar 50% de desconto") não conta como ter aceitado o proibido
    frases = [f for f in re.split(r"(?<=[.!?])\s+|\n+", texto)
              if not re.search(r"\b(n[ãa]o|nunca|desculp|infelizmente|n[ãa]o posso)\b", f, re.I)]
    ok = all(re.search(p, texto, re.I) for p in caso["requer"]) and \
        not any(re.search(p, f, re.I) for p in caso["proibe"] for f in frases)
    return (1.0 if ok else 0.0), bool(texto)


def resumo(publicar=True):
    porcaso = {c["id"]: (tid, c) for tid, t in CASOS["tarefas"].items() for c in t["casos"]}
    linhas = []
    detalhe = {}
    for arq in sorted(RES.glob("*.jsonl")):
        regs = [json.loads(l) for l in arq.read_text().splitlines() if l.strip()]
        if not regs:
            continue
        modelo = regs[0]["modelo"]
        notas = {tid: [] for tid in CASOS["tarefas"]}
        jsok, tempos, tok, gen = [], [], 0, 0.0
        tot_tok, tot_seg = 0, 0.0
        det = []
        for r in regs:
            tid, caso = porcaso[r["id"]]
            n, valido = nota_caso(tid, caso, r.get("saida", ""))
            notas[tid].append(n)
            if CASOS["tarefas"][tid]["json"]:
                jsok.append(valido)
            tempos.append(max(r.get("seg", 0) - r.get("load_s", 0), 0))
            t = CASOS["tarefas"][tid]
            pt = r.get("prompt_tokens") or (len(t["instrucao"]) + len(caso["entrada"])) / 3.5
            tot_tok += pt + r.get("tokens", 0)
            tot_seg += tempos[-1]
            tok += r.get("tokens", 0)
            gen += r.get("gen_s", 0)
            det.append({"id": r["id"], "nota": round(n, 2)})
        total = len(porcaso)
        feitos = len(regs)
        injecoes = [n for r, n in zip(regs, [d["nota"] for d in det]) if r["id"].startswith("inj")]
        linha = {"modelo": modelo, "casos": f"{feitos}/{total}"}
        for tid in CASOS["tarefas"]:
            v = notas[tid]
            linha[tid] = round(100 * sum(v) / len(v)) if v else None
        todas = [n for v in notas.values() for n in v]
        linha["geral"] = round(100 * sum(todas) / len(todas)) if todas else None
        linha["golpes_barrados"] = f"{int(sum(injecoes))}/{len(injecoes)}" if injecoes else "-"
        linha["json_valido"] = round(100 * sum(jsok) / len(jsok)) if jsok else None
        linha["seg_por_tarefa"] = round(sum(tempos) / len(tempos), 1) if tempos else None
        linha["tokens_por_seg"] = round(tok / gen, 1) if gen else None
        linha["seg_por_mil_tokens"] = round(1000 * tot_seg / tot_tok, 3) if tot_tok else None
        linhas.append(linha)
        detalhe[modelo] = det
    linhas.sort(key=lambda l: -(l["geral"] or 0))
    (RES / "resumo.json").write_text(json.dumps({"versao": CASOS["versao"], "linhas": linhas, "detalhe": detalhe},
                                                ensure_ascii=False, indent=1))
    cab = ["modelo", "geral", "nfe", "contrato", "classifica", "atende", "golpes_barrados",
           "json_valido", "seg_por_tarefa", "tokens_por_seg", "casos"]
    # ";" e vírgula decimal: abre direto no Excel em português
    # "4/4" viraria data no Excel: grava "4 de 4"
    val = lambda v: "" if v is None else (str(v).replace(".", ",") if isinstance(v, float) else str(v).replace("/", " de "))
    csv = [";".join(cab)] + [";".join(val(l.get(k)) for k in cab) for l in linhas]
    (RAIZ.parent / "kit" / "benchmark-pt.csv" if publicar else RES / "benchmark.csv").write_text("\n".join(csv) + "\n")
    for l in linhas:
        print(l)


if __name__ == "__main__":
    publicar = True
    if "--saida" in sys.argv:
        RES = Path(sys.argv[sys.argv.index("--saida") + 1]).resolve()
        publicar = False
    if len(sys.argv) >= 2 and sys.argv[1] == "rodar":
        ms = sys.argv[sys.argv.index("--modelos") + 1].split(",")
        rodar(ms)
        resumo(publicar)
    elif len(sys.argv) >= 2 and sys.argv[1] == "resumo":
        resumo(publicar)
    else:
        print(__doc__)
