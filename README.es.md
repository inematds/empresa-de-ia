# Tu empresa de IA

[![Tu empresa de IA](guia/assets/banner-es.jpg)](https://inematds.github.io/empresa-de-ia/guia/es/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## Qué es

Este es un kit gratuito para que el dueño de una pequeña o mediana empresa deje atrás el uso suelto de ChatGPT y ponga a trabajar a un agente de IA en un proceso real. Son herramientas que funcionan en el navegador, sin registro: la Radiografía de procesos señala por dónde empezar, la calculadora muestra cuánto cuesta y cuánto devuelve, el checklist dice si el agente es seguro para encenderlo y el comparador de la fábrica muestra si conviene más la herramienta lista, la API o una máquina propia, con una prueba de modelos abiertos en portugués. Quien hace consultoría tiene el modelo para aplicar todo esto en un cliente. Después, la ruta lleva a los cursos y kits de INEMA para montar cada agente. Solo necesitas el navegador; nada sale de tu computadora.

## 📖 Guía de uso

Guía completa con las herramientas interactivas: **https://inematds.github.io/empresa-de-ia/guia/es/**

## De dónde viene

En Berlín (GTC, 21/10/2026), Jensen Huang dijo que toda empresa se convertirá en una empresa de IA y que hay que producir IA, no solo consumirla. Lo explicó con un pastel de cinco capas: energía, computadores, fábrica de IA, modelos y aplicaciones. Este kit traduce el pastel a la pequeña empresa. Video: https://www.youtube.com/watch?v=t-mBC3kuhLM

| Capa | En tu empresa | Pieza |
|---|---|---|
| Aplicaciones | los procesos del negocio | Radiografía de procesos |
| Modelos | qué IA hace cada tarea y cuánto cuesta | Calculadora de costo |
| Fábrica de IA | herramienta lista, API o máquina propia | Comparador de la fábrica + prueba en portugués |
| Computadores | agente aislado, acceso mínimo | Checklist del agente seguro |
| Energía | personas, datos, contexto | ruta INEMA |

## Qué hay en el repositorio

```
guia/index.html                 # página con las herramientas (PT) + guia/en/ y guia/es/
kit/raio-x-processos.csv        # Radiografía en hoja de cálculo (con fórmulas)
kit/calculadora-custo.csv       # calculadora de costo por tarea en hoja de cálculo
# los CSV usan ";" y coma decimal: abren directo en Excel en portugués; en Google Sheets, Archivo > Importar > separador punto y coma
kit/checklist-agente-seguro.md  # checklist de 10 ítems en texto
kit/modelo-consultor.es.md        # modelo del consultor: 6 etapas, guion de 12 preguntas, propuesta e informe
kit/benchmark-pt.csv            # resultado de la prueba de modelos abiertos en portugués
bench/casos.json                # casos inventados de las 4 tareas (factura, contrato, clasificar, atender)
bench/roda.py                   # ejecuta la prueba en Ollama local y da la nota con regla fija
bench/injeta.py                 # inserta el resultado en las 3 guías
bench/resultados/               # respuestas de cada modelo y resumen.json
```

## El proceso, del inicio al fin

1. 🧠 **Radiografía**: el dueño lista las tareas que se repiten y recibe la fila de los 3 primeros procesos (guía, paso 1).
2. 🧠 **Costo**: calcula costo hoy × costo con agente y el costo por tarea concluida (guía, paso 2).
3. 🧠 **Seguridad**: marca el checklist; por debajo de 6 ítems no se enciende (guía, paso 3).
4. 🧠 **Piloto de 30 días** con el kit INEMA indicado, anotando cada semana tareas, devoluciones a una persona, costo de la IA y quejas.
5. 🧠 **Medir**: rehace la calculadora con los números reales; si funcionó, pasa al siguiente de la fila.
6. 🧠 **Fábrica**: el comparador muestra el costo por mes de la herramienta lista, de la API y de la máquina propia, y cuántas tareas aguanta la máquina (guía, sección Fábrica).
7. 🧠 **Consultoría**: quien atiende clientes sigue las 6 etapas de `kit/modelo-consultor.es.md`; el botón "Montar el resumen para el cliente" genera la propuesta con los números de las herramientas.

Todo esto corre en el navegador (⚙️ JavaScript de la página); no hay servidor ni agente automático.

**Prueba de modelos (mantenedor):**

1. ⚙️ `python3 bench/roda.py rodar --modelos <m1,m2>` ejecuta los casos en Ollama local, un modelo a la vez (descarga el anterior), y graba `bench/resultados/<modelo>.jsonl`. Un caso ya hecho se salta.
2. ⚙️ `python3 bench/roda.py resumo` da la nota y genera `bench/resultados/resumo.json` y `kit/benchmark-pt.csv`.
3. ⚙️ `python3 bench/injeta.py` inserta el resultado en la tabla de las 3 guías.
4. 🧠 Revisar las lecciones de la ronda en el bloque `TF.licoes` de las guías y publicar (commit + push).

## Fuentes de los números de la guía

- Cetic.br, TIC Empresas 2025 (17% de las empresas usan IA; 80% compran lo listo, 26% hacen la propia).
- Serasa Experian, encuesta con PYMEs 2026 (41,3% citan falta de conocimiento; 31,2% costo).
- Gartner, previsión de jun/2025 (más del 40% de los proyectos de agentes cancelados hasta 2027).
- OWASP Top 10 for Agentic Applications 2026.
- Keynote de Jensen Huang, GTC Berlín 2026.

---
Parte de [INEMA.CLUB](https://inema.club) — contenido abierto y gratuito.
