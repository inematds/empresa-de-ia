# Modelo del consultor: aplicar el kit "Tu empresa de IA" en un cliente

Para quien hace consultoría de IA en pequeñas y medianas empresas. Son 6 etapas, desde el primer café hasta el informe del piloto de 30 días, usando las herramientas de la guía (https://inematds.github.io/empresa-de-ia/guia/es/).
La regla de fondo: **un proceso a la vez, medido antes y después**. No vendes "IA"; vendes una tarea que pasa a costar menos y un número que lo prueba.

## Las 6 etapas

| # | Etapa | Tiempo | Herramienta | Qué entregas |
|---|---|---|---|---|
| 1 | Conversación de diagnóstico | 1 h | Guion de abajo | Lista de las tareas que se repiten |
| 2 | Radiografía con el dueño | 30 min | Radiografía de procesos | La fila de los 3 primeros procesos |
| 3 | Línea base y cuenta | 30 min + 1 semana midiendo | Calculadora de costo por tarea | Costo de hoy y costo con el agente, en [$ ...] (en tu moneda) |
| 4 | Dónde corre y si se puede encender | 1 h | Comparador de la fábrica + checklist | Camino elegido (lista, API o máquina) y veredicto del checklist |
| 5 | Piloto de 30 días | 4 semanas | Planilla de medición semanal | 4 mediciones: tareas, vueltas a una persona, costo, reclamos |
| 6 | Informe y siguiente de la fila | 1 h | Calculadora con los números reales | Antes × después y la decisión: sigue, ajusta o se detiene |

En la etapa 4, el checklist debe dar al menos **piloto con supervisión** y tener los ítems obligatorios 2, 4 y 10. Sin eso, el piloto no empieza.

## 1. Guion de la conversación de diagnóstico (1 hora)

Conversa con el dueño y con quienes hacen el trabajo del día a día. Anota las respuestas en forma de tarea: verbo + objeto + frecuencia.

1. ¿Qué hace el equipo cada semana que es siempre igual?
2. ¿Qué preguntas de clientes llegan repetidas (precio, horario, plazo, estado)?
3. ¿Dónde llegan esos mensajes: WhatsApp, correo, teléfono, Instagram?
4. ¿Qué papeleo pasa por las manos de alguien: facturas, boletas, contratos, planillas?
5. ¿Cuánto tiempo lleva cada una, más o menos? ¿Cuántas veces por semana?
6. ¿Existe una regla escrita para eso, o cada persona lo hace a su manera?
7. ¿La información está en un sistema o planilla, o solo en la cabeza de alguien?
8. ¿Qué pasa si esa tarea sale mal? (pierde un cliente, pierde dinero, problema legal)
9. ¿Qué tarea es la que más detesta hacer el equipo?
10. ¿De qué se queja más el cliente por la demora?
11. ¿Qué sistemas ya paga la empresa (agenda, ERP, tienda virtual, contabilidad)?
12. ¿Hay datos sensibles de clientes (salud, finanzas, documentos)? ¿Dónde se guardan hoy?

Salida: de 8 a 15 tareas para la Radiografía. Pide al equipo que anote tres días si el dueño no sabe los números.

## 2. Radiografía con el dueño (30 minutos)

Completa la Radiografía junto con el dueño, en su pantalla. La fila sale de la cuenta de horas por mes × regla clara × dato digital ÷ riesgo. Explica la fila en una frase por ítem. Si el primero de la fila es de riesgo grave, acuerda que una persona apruebe cada respuesta en el piloto.

## 3. Línea base y cuenta (30 minutos + 1 semana)

Antes de tocar nada, mide una semana del proceso elegido: cuántas tareas, cuánto tiempo cada una, cuánto cuesta la hora de quien la hace. Sin línea base no existe el "después". Completa la calculadora con esos números y con una estimación honesta de lo que el agente resuelve solo (empieza en 50% a 70%).

## 4. Dónde corre y si se puede encender (1 hora)

- Usa el comparador de la fábrica: herramienta lista, API en la nube o máquina propia.
- Los datos sensibles piden una conversación con el abogado del cliente sobre la LGPD (ley de protección de datos de Brasil; en otros países, la ley local equivalente) antes de elegir; la guía no sustituye ese análisis.
- Pasa el checklist del agente seguro con quien va a cuidar el agente. Registra el veredicto en el resumen.

## 5. Piloto de 30 días

Una planilla simple, una fila por semana:

| Semana | Tareas hechas por el agente | Volvieron a una persona | Costo de la IA ([$ ...], en tu moneda) | Reclamos | Observación |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

Acuerda una reunión corta cada semana (15 minutos) para revisar la planilla y el registro del agente.

## 6. Informe y siguiente de la fila (1 hora)

Rehaz la calculadora con los números reales del piloto y decide junto con el dueño:

- **Sigue:** diferencia positiva, checklist verde, pocos reclamos. Pasa al segundo de la fila.
- **Ajusta:** muchas vueltas a una persona o costo por encima de lo previsto. Corrige la regla o el modelo y mide 2 semanas más.
- **Se detiene:** diferencia negativa o riesgo que no cierra. Eso también es un resultado; registra el porqué.

## Propuesta de una página (modelo)

> **Propuesta — primer agente de IA de [EMPRESA]**
>
> **El problema:** [TAREA 1.º DE LA FILA] toma [X] horas por mes del equipo y hoy cuesta cerca de [$ HOY] por mes.
>
> **Qué vamos a hacer:** un agente de IA que hace [TAREA], con una persona revisando lo que él no sepa. Corre en [CAMINO: herramienta lista / API en la nube / máquina propia].
>
> **Cómo medimos:** una semana de línea base, 30 días de piloto con medición semanal y un informe de antes × después.
>
> **Cuenta prevista:** costo con el agente de [$ AGENTE] por mes; diferencia prevista de [$ DIFERENCIA] por mes. Los números se rehacen con los datos reales del piloto.
>
> **Seguridad:** checklist del agente seguro con veredicto [VEREDICTO]; acción sin vuelta atrás (pagar, borrar, enviar en masa) solo con aprobación de una persona.
>
> **Plazo:** [FECHA INICIO] a [FECHA FIN]. **Inversión:** [VALOR DEL TRABAJO].
>
> **Fuera del alcance:** otros procesos de la fila, integraciones no listadas arriba.

La guía tiene el botón **Armar el resumen**, que completa este texto con los números de las tres herramientas.

## Informe del piloto (modelo)

> **Informe del piloto — [EMPRESA] — [TAREA]**
>
> - Antes: [N] tareas/mes, [MIN] min cada una, [$ HOY] por mes.
> - Después (30 días): [N] tareas, [%] resueltas por el agente, [N] volvieron a una persona, cuenta de la IA [$], [N] reclamos.
> - Diferencia real por mes: [$]. Horas liberadas: [H].
> - Checklist al final del piloto: [VEREDICTO].
> - Decisión: [sigue / ajusta / se detiene] — porque [MOTIVO].
> - Siguiente de la fila: [TAREA 2].

## Para profundizar (cursos y kits abiertos de INEMA)

- Profesional 2030 · Consultor de IA (diagnóstico, piloto y medición de valor) (en portugués): https://inematds.github.io/prof2030-consultor/
- Consultor de IA · Del rótulo al resultado (en portugués): https://inematds.github.io/consultoria2k/
- Ventas con IA · Playbook de consultoría (en portugués): https://inematds.github.io/formacao-vendas-ia-consultoria-v72/
- DICA 1 · Mapa del Cliente (diagnóstico) (en portugués): https://inematds.github.io/formacao-dica-diagnostico-v72/
- Área Consultoría de IA (cursos y kits): https://eventos.inema.pro/consultoria-ia/es/
