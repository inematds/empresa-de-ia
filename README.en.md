# Your AI company

[![Your AI company](guia/assets/banner-en.jpg)](https://inematds.github.io/empresa-de-ia/guia/en/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## What it is

This is a free kit for owners of small and medium-sized businesses who want to move beyond casual ChatGPT use and put an AI agent to work on a real process. The tools run in the browser, with no sign-up: the Process X-ray shows where to start, the calculator shows what it costs and what it returns, the checklist tells you whether the agent is safe to switch on, and the factory comparator shows whether a ready-made tool, an API, or your own machine is the better fit, along with a test of open models in Portuguese. Consultants get a template to apply all of this to a client. After that, the path leads to INEMA's courses and kits for building each agent. All you need is a browser; nothing leaves your computer.

## 📖 Usage guide

Complete guide with the interactive tools: **https://inematds.github.io/empresa-de-ia/guia/en/**

## Where it comes from

In Berlin (GTC, 10/21/2026), Jensen Huang said that every company will become an AI company and that you need to produce AI, not just consume it. He explained it with a five-layer cake: energy, computers, AI factory, models, and applications. This kit translates the cake to the small business. Video: https://www.youtube.com/watch?v=t-mBC3kuhLM

| Layer | In your company | Piece |
|---|---|---|
| Applications | the business processes | Process X-ray |
| Models | which AI does each task and what it costs | Cost calculator |
| AI factory | ready-made tool, API, or your own machine | Factory comparator + Portuguese test |
| Computers | isolated agent, minimum access | Safe agent checklist |
| Energy | people, data, context | INEMA path |

## What's in the repository

```
guia/index.html                 # page with the tools (PT) + guia/en/ and guia/es/
kit/raio-x-processos.csv        # Process X-ray as a spreadsheet (with formulas)
kit/calculadora-custo.csv       # cost-per-task calculator as a spreadsheet
# the CSVs use ";" and a decimal comma: they open directly in Excel in Portuguese; in Google Sheets, File > Import > semicolon separator
kit/checklist-agente-seguro.md  # 10-item checklist in text
kit/modelo-consultor.en.md        # consultant template: 6 steps, 12-question script, proposal and report
kit/benchmark-pt.csv            # result of the open-model test in Portuguese
bench/casos.json                # made-up cases for the 4 tasks (invoice, contract, classify, support)
bench/roda.py                   # runs the test on local Ollama and scores it by fixed rule
bench/injeta.py                 # injects the result into the 3 guides
bench/resultados/               # each model's answers and resumo.json
```

## The process, from start to finish

1. 🧠 **X-ray**: the owner lists the tasks that repeat and gets the queue of the top 3 processes (guide, step 1).
2. 🧠 **Cost**: calculates cost today × cost with an agent and the cost per completed task (guide, step 2).
3. 🧠 **Security**: ticks the checklist; below 6 items, don't switch it on (guide, step 3).
4. 🧠 **30-day pilot** with the recommended INEMA kit, noting every week the tasks, hand-backs to a person, AI cost, and complaints.
5. 🧠 **Measure**: redo the calculator with the real numbers; if it worked, move on to the next in the queue.
6. 🧠 **Factory**: the comparator shows the monthly cost of the ready-made tool, the API, and your own machine, and how many tasks the machine can handle (guide, Factory section).
7. 🧠 **Consulting**: anyone serving clients follows the 6 steps in `kit/modelo-consultor.en.md`; the "Build the summary" button generates the proposal with the numbers from the tools.

All of this runs in the browser (⚙️ the page's JavaScript); there is no server or automatic agent.

**Model test (maintainer):**

1. ⚙️ `python3 bench/roda.py rodar --modelos <m1,m2>` runs the cases on local Ollama, one model at a time (unloading the previous one), and writes `bench/resultados/<model>.jsonl`. Cases already done are skipped.
2. ⚙️ `python3 bench/roda.py resumo` scores the results and generates `bench/resultados/resumo.json` and `kit/benchmark-pt.csv`.
3. ⚙️ `python3 bench/injeta.py` puts the result into the table of the 3 guides.
4. 🧠 Review the round's lessons in the `TF.licoes` block of the guides and publish (commit + push).

## Testing your task

1. Open `bench/casos.json` and copy a case similar to yours (for example, one from `atende`).
2. Change the `id` to a new name and the `entrada` to your customer's real message (with no personal data).
3. In `requer`, put what the answer must contain (e.g., the correct price); in `proibe`, what it must not say.
4. For document-reading tasks, use the `nfe` or `contrato` tasks and fill in `esperado` with the correct values.
5. Run `python3 bench/roda.py rodar --modelos llama3.2:latest --saida bench/minha-rodada` and open `bench/minha-rodada/benchmark.csv`.

## Sources for the guide's numbers

- Cetic.br, TIC Empresas 2025 (17% of companies use AI; 80% buy ready-made, 26% build their own).
- Serasa Experian, SME survey 2026 (41.3% cite lack of knowledge; 31.2% cost).
- Gartner, June 2025 forecast (more than 40% of agent projects canceled by 2027).
- OWASP Top 10 for Agentic Applications 2026.
- Jensen Huang keynote, GTC Berlin 2026.

---
Part of [INEMA.CLUB](https://inema.club) — open and free content.
