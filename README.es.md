# Tu empresa de IA

[![Tu empresa de IA](guia/assets/banner-es.jpg)](https://inematds.github.io/empresa-de-ia/guia/es/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## Qué es

Este es un kit gratuito para que el dueño de una pequeña o mediana empresa deje de usar ChatGPT a la suerte y ponga un agente de IA a trabajar en un proceso real. Son tres herramientas que funcionan en el navegador, sin registro: la Radiografía de procesos señala por dónde empezar, la calculadora muestra cuánto cuesta y cuánto devuelve, y el checklist dice si el agente es seguro para encenderlo. Después, la ruta lleva a los cursos y kits de INEMA (en portugués) para armar cada agente. Solo necesitas el navegador; nada sale de tu computadora.

## 📖 Guía de uso

Guía completa con las herramientas interactivas: **https://inematds.github.io/empresa-de-ia/guia/es/**

## De dónde viene

En Berlín (GTC, 21/10/2026), Jensen Huang dijo que toda empresa se va a convertir en empresa de IA y que hay que producir IA, no solo consumirla. Lo explicó con un pastel de cinco capas: energía, computadoras, fábrica de IA, modelos y aplicaciones. Este kit traduce el pastel para la pequeña empresa. Video (en portugués): https://www.youtube.com/watch?v=t-mBC3kuhLM

| Capa | En tu empresa | Pieza |
|---|---|---|
| Aplicaciones | los procesos del negocio | Radiografía de procesos |
| Modelos | qué IA hace cada tarea y cuánto cuesta | Calculadora de costo |
| Fábrica de IA | nube, API o máquina propia | guía de la fábrica (próxima pieza) |
| Computadoras | agente aislado, mínimo privilegio | Checklist del agente seguro |
| Energía | personas, datos, contexto | ruta INEMA |

## Qué hay en el repositorio

```
guia/index.html                 # página con las 3 herramientas (PT) + guia/en/ y guia/es/
kit/raio-x-processos.csv        # Radiografía en hoja de cálculo, con fórmulas (en portugués)
kit/calculadora-custo.csv       # calculadora de costo por tarea en hoja de cálculo (en portugués)
kit/checklist-agente-seguro.md  # checklist de 10 ítems en texto (en portugués)
```

## El proceso, de principio a fin

1. 🧠 **Radiografía**: el dueño anota las tareas que se repiten y recibe la fila de los 3 primeros procesos (guía, paso 1).
2. 🧠 **Costo**: calcula el costo de hoy × el costo con el agente y el costo por tarea terminada (guía, paso 2).
3. 🧠 **Seguridad**: marca el checklist; con menos de 6 ítems no se enciende (guía, paso 3).
4. 🧠 **Piloto de 30 días** con el kit INEMA indicado, anotando cada semana tareas, casos devueltos a una persona, costo de la IA y quejas.
5. 🧠 **Medir**: rehace la calculadora con los números reales; si funcionó, pasa al siguiente de la fila.

Todo corre en el navegador (⚙️ JavaScript de la página); no hay servidor ni agente automático en este repositorio.

## Fuentes de los números de la guía

- Cetic.br, TIC Empresas 2025, Brasil (el 17% de las empresas usa IA; el 80% compra software listo y el 26% crea uno propio).
- Serasa Experian, encuesta con pymes en Brasil 2026 (el 41,3% cita falta de conocimiento; el 31,2%, el costo).
- Gartner, previsión de junio de 2025 (más del 40% de los proyectos de agentes cancelados hasta 2027).
- OWASP Top 10 for Agentic Applications 2026.
- Keynote de Jensen Huang, GTC Berlín 2026.

---
Parte de [INEMA.CLUB](https://inema.club) — contenido abierto y gratuito.
