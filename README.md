# Sua empresa de IA

[![Sua empresa de IA](guia/assets/banner.jpg)](https://inematds.github.io/empresa-de-ia/guia/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## O que é

Este é um kit gratuito para o dono de pequena ou média empresa sair do uso solto do ChatGPT e colocar um agente de IA para trabalhar num processo de verdade. São ferramentas que funcionam no navegador, sem cadastro: o Raio-X de Processos aponta por onde começar, a calculadora mostra quanto custa e quanto devolve, o checklist diz se o agente está seguro para ligar e o comparador da fábrica mostra se vale mais a ferramenta pronta, a API ou uma máquina própria, com um teste de modelos abertos em português. Quem faz consultoria tem o modelo para aplicar tudo isso num cliente. Depois, a trilha leva aos cursos e kits do INEMA para montar cada agente. Você só precisa do navegador; nada sai do seu computador.

## 📖 Guia de uso

Guia completo com as ferramentas interativas: **https://inematds.github.io/empresa-de-ia/guia/**

## De onde vem

Em Berlim (GTC, 21/10/2026), Jensen Huang disse que toda empresa vai virar empresa de IA e que é preciso produzir IA, não só consumir. Ele explicou com um bolo de cinco camadas: energia, computadores, fábrica de IA, modelos e aplicações. Este kit traduz o bolo para a pequena empresa. Vídeo: https://www.youtube.com/watch?v=t-mBC3kuhLM

| Camada | Na sua empresa | Peça |
|---|---|---|
| Aplicações | os processos do negócio | Raio-X de Processos |
| Modelos | qual IA faz cada tarefa e quanto custa | Calculadora de custo |
| Fábrica de IA | ferramenta pronta, API ou máquina própria | Comparador da fábrica + teste em português |
| Computadores | agente isolado, acesso mínimo | Checklist do agente seguro |
| Energia | pessoas, dados, contexto | trilha INEMA |

## O que tem no repositório

```
guia/index.html                 # página com as ferramentas (PT) + guia/en/ e guia/es/
kit/raio-x-processos.csv        # Raio-X em planilha (com fórmulas)
kit/calculadora-custo.csv       # calculadora de custo por tarefa em planilha
# os CSV usam ";" e vírgula decimal: abrem direto no Excel em português; no Google Planilhas, Arquivo > Importar > separador ponto e vírgula
kit/checklist-agente-seguro.md  # checklist de 10 itens em texto
kit/modelo-consultor.md         # modelo do consultor: 6 etapas, roteiro de 12 perguntas, proposta e relatório
kit/benchmark-pt.csv            # resultado do teste de modelos abertos em português
bench/casos.json                # casos inventados das 4 tarefas (nota fiscal, contrato, classificar, atender)
bench/roda.py                   # roda o teste no Ollama local e dá a nota por regra fixa
bench/injeta.py                 # põe o resultado nos 3 guias
bench/resultados/               # respostas de cada modelo e resumo.json
```

## O processo, do início ao fim

1. 🧠 **Raio-X**: o dono lista as tarefas que se repetem e recebe a fila dos 3 primeiros processos (guia, passo 1).
2. 🧠 **Custo**: calcula custo hoje × custo com agente e o custo por tarefa concluída (guia, passo 2).
3. 🧠 **Segurança**: marca o checklist; abaixo de 6 itens não liga (guia, passo 3).
4. 🧠 **Piloto de 30 dias** com o kit INEMA indicado, anotando toda semana tarefas, retornos para pessoa, custo da IA e reclamações.
5. 🧠 **Medir**: refaz a calculadora com os números reais; deu certo, passa para o próximo da fila.
6. 🧠 **Fábrica**: o comparador mostra o custo por mês da ferramenta pronta, da API e da máquina própria, e quantas tarefas a máquina dá conta (guia, seção Fábrica).
7. 🧠 **Consultoria**: quem atende clientes segue as 6 etapas de `kit/modelo-consultor.md`; o botão "Montar o resumo para o cliente" gera a proposta com os números das ferramentas.

Tudo isso roda no navegador (⚙️ JavaScript da página); não há servidor nem agente automático.

**Teste de modelos (mantenedor):**

1. ⚙️ `python3 bench/roda.py rodar --modelos <m1,m2>` roda os casos no Ollama local, um modelo por vez (descarrega o anterior), e grava `bench/resultados/<modelo>.jsonl`. Caso já feito é pulado.
2. ⚙️ `python3 bench/roda.py resumo` dá a nota e gera `bench/resultados/resumo.json` e `kit/benchmark-pt.csv`.
3. ⚙️ `python3 bench/injeta.py` põe o resultado na tabela dos 3 guias.
4. 🧠 Revisar as lições da rodada no bloco `TF.licoes` dos guias e publicar (commit + push).

## Fontes dos números do guia

- Cetic.br, TIC Empresas 2025 (17% das empresas usam IA; 80% compram pronto, 26% fazem própria).
- Serasa Experian, pesquisa com PMEs 2026 (41,3% citam falta de conhecimento; 31,2% custo).
- Gartner, previsão de jun/2025 (mais de 40% dos projetos de agentes cancelados até 2027).
- OWASP Top 10 for Agentic Applications 2026.
- Keynote de Jensen Huang, GTC Berlim 2026.

---
Parte do [INEMA.CLUB](https://inema.club) — conteúdo aberto e gratuito.
