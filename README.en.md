# Your AI company

[![Your AI company](guia/assets/banner-en.jpg)](https://inematds.github.io/empresa-de-ia/guia/en/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## What it is

This is a free kit for the owner of a small or mid-sized business to move past casual ChatGPT use and put an AI agent to work on a real process. There are three tools that run in the browser, no sign-up: the Process X-ray shows where to start, the calculator shows what it costs and what it pays back, and the checklist tells you whether the agent is safe to switch on. Then the track leads to INEMA courses and kits (in Portuguese) to build each agent. All you need is a browser; nothing leaves your computer.

## 📖 User guide

Full guide with the interactive tools: **https://inematds.github.io/empresa-de-ia/guia/en/**

## Where it comes from

In Berlin (GTC, 10/21/2026), Jensen Huang said every company will become an AI company and that you have to produce AI, not just consume it. He explained it with a five-layer cake: energy, computers, AI factory, models and applications. This kit translates the cake for small businesses. Video: https://www.youtube.com/watch?v=t-mBC3kuhLM

| Layer | In your business | Piece |
|---|---|---|
| Applications | the business processes | Process X-ray |
| Models | which AI does each task and what it costs | Cost calculator |
| AI factory | cloud, API or your own machine | AI factory guide (next piece) |
| Computers | isolated agent, least privilege | Safe agent checklist |
| Energy | people, data, context | INEMA track |

## What's in the repository

```
guia/index.html                 # page with the 3 tools (PT) + guia/en/ and guia/es/
kit/raio-x-processos.csv        # Process X-ray as a spreadsheet (with formulas, in Portuguese)
kit/calculadora-custo.csv       # cost-per-task calculator as a spreadsheet (in Portuguese)
kit/checklist-agente-seguro.md  # 10-item safe agent checklist as text (in Portuguese)
```

## The process, start to finish

1. 🧠 **X-ray**: the owner lists the recurring tasks and gets the queue of the first 3 processes (guide, step 1).
2. 🧠 **Cost**: calculates today's cost × cost with the agent and the cost per completed task (guide, step 2).
3. 🧠 **Safety**: ticks the checklist; below 6 items, don't switch it on (guide, step 3).
4. 🧠 **30-day pilot** with the recommended INEMA kit, writing down every week the tasks, hand-backs to a person, AI cost and complaints.
5. 🧠 **Measure**: redoes the calculator with the real numbers; if it worked, moves on to the next in line.

Everything runs in the browser (⚙️ the page's JavaScript); there is no server or automated agent in this repository.

## Sources for the guide's numbers

- Cetic.br, TIC Empresas 2025 (17% of companies use AI; 80% buy off the shelf, 26% build their own).
- Serasa Experian, survey of SMEs, 2026 (41.3% cite lack of knowledge; 31.2% cost).
- Gartner, forecast of June 2025 (over 40% of agent projects canceled by 2027).
- OWASP Top 10 for Agentic Applications 2026.
- Jensen Huang's keynote, GTC Berlin 2026.

---
Part of [INEMA.CLUB](https://inema.club) — open and free content.
