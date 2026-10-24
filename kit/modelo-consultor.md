# Modelo do consultor: aplicar o kit "Sua empresa de IA" num cliente

Para quem faz consultoria de IA em pequena e média empresa. São 6 etapas, do primeiro café ao relatório do piloto de 30 dias, usando as ferramentas do guia (https://inematds.github.io/empresa-de-ia/guia/).
A regra de fundo: **um processo de cada vez, medido antes e depois**. Você não vende "IA"; vende uma tarefa que passa a custar menos e um número que prova isso.

## As 6 etapas

| # | Etapa | Tempo | Ferramenta | O que você entrega |
|---|---|---|---|---|
| 1 | Conversa de diagnóstico | 1 h | Roteiro abaixo | Lista das tarefas que se repetem |
| 2 | Raio-X com o dono | 30 min | Raio-X de Processos | A fila dos 3 primeiros processos |
| 3 | Linha de base e conta | 30 min + 1 semana medindo | Calculadora de custo por tarefa | Custo de hoje e custo com o agente, em R$ |
| 4 | Onde roda e se pode ligar | 1 h | Comparador da fábrica + checklist | Caminho escolhido (pronta, API ou máquina) e veredito do checklist |
| 5 | Piloto de 30 dias | 4 semanas | Planilha de medição semanal | 4 medições: tarefas, voltas para pessoa, custo, reclamações |
| 6 | Relatório e próximo da fila | 1 h | Calculadora com os números reais | Antes × depois e a decisão: segue, ajusta ou para |

Na etapa 4, o checklist precisa dar pelo menos **piloto com supervisão** e ter os itens obrigatórios 2, 4 e 10. Sem isso, o piloto não começa.

## 1. Roteiro da conversa de diagnóstico (1 hora)

Converse com o dono e com quem faz o trabalho do dia a dia. Anote as respostas em forma de tarefa: verbo + objeto + frequência.

1. O que a equipe faz toda semana que é sempre igual?
2. Quais perguntas de cliente chegam repetidas (preço, horário, prazo, status)?
3. Onde chegam essas mensagens: WhatsApp, e-mail, telefone, Instagram?
4. Que papelada passa pela mão de alguém: notas fiscais, boletos, contratos, planilhas?
5. Quanto tempo leva cada uma, mais ou menos? Quantas vezes por semana?
6. Existe regra escrita para isso, ou cada pessoa faz do seu jeito?
7. A informação está em sistema ou planilha, ou só na cabeça de alguém?
8. O que acontece se essa tarefa sair errada? (perde cliente, perde dinheiro, problema legal)
9. Qual tarefa a equipe mais detesta fazer?
10. O que o cliente mais reclama de demora?
11. Quais sistemas a empresa já paga (agenda, ERP, loja virtual, contabilidade)?
12. Tem dado de cliente sensível (saúde, financeiro, documento)? Onde fica guardado hoje?

Saída: de 8 a 15 tarefas para o Raio-X. Peça para a equipe anotar três dias se o dono não souber os números.

## 2. Raio-X com o dono (30 minutos)

Preencha o Raio-X junto com o dono, na tela dele. A fila sai pela conta de horas por mês × regra clara × dado digital ÷ risco. Explique a fila em uma frase por item. Se o primeiro da fila for de risco grave, combine que uma pessoa aprova cada resposta no piloto.

## 3. Linha de base e conta (30 minutos + 1 semana)

Antes de mexer em nada, meça uma semana do processo escolhido: quantas tarefas, quanto tempo cada uma, quanto custa a hora de quem faz. Sem linha de base não existe "depois". Preencha a calculadora com esses números e com uma estimativa honesta do que o agente resolve sozinho (comece em 50% a 70%).

## 4. Onde roda e se pode ligar (1 hora)

- Use o comparador da fábrica: ferramenta pronta, API na nuvem ou máquina própria.
- Dados sensíveis pedem conversa com o advogado do cliente sobre a LGPD antes de escolher; o guia não substitui essa análise.
- Passe o checklist do agente seguro com quem vai cuidar do agente. Registre o veredito no resumo.

## 5. Piloto de 30 dias

Planilha pronta para preencher: `kit/piloto-semanal.csv`.

Uma planilha simples, uma linha por semana:

| Semana | Tarefas feitas pelo agente | Voltaram para uma pessoa | Custo da IA (R$) | Reclamações | Observação |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

Combine uma reunião curta toda semana (15 minutos) para olhar a planilha e o registro do agente.

## 6. Relatório e próximo da fila (1 hora)

Refaça a calculadora com os números reais do piloto e decida junto com o dono:

- **Segue:** diferença positiva, checklist verde, poucas reclamações. Passe para o segundo da fila.
- **Ajusta:** muitas voltas para uma pessoa ou custo acima do previsto. Corrija a regra ou o modelo e meça mais 2 semanas.
- **Para:** diferença negativa ou risco que não fecha. Isso também é resultado; registre o porquê.

## Proposta de uma página (modelo)

> **Proposta — primeiro agente de IA da [EMPRESA]**
>
> **O problema:** [TAREFA 1º DA FILA] toma [X] horas por mês da equipe e custa hoje cerca de [R$ HOJE] por mês.
>
> **O que vamos fazer:** um agente de IA que faz [TAREFA], com uma pessoa revisando o que ele não souber. Roda em [CAMINHO: ferramenta pronta / API na nuvem / máquina própria].
>
> **Como medimos:** uma semana de linha de base, 30 dias de piloto com medição semanal e um relatório de antes × depois.
>
> **Conta prevista:** custo com o agente de [R$ AGENTE] por mês; diferença prevista de [R$ DIFERENÇA] por mês. Os números serão refeitos com os dados reais do piloto.
>
> **Segurança:** checklist do agente seguro com veredito [VEREDITO]; ação sem volta (pagar, apagar, enviar em massa) só com aprovação de uma pessoa.
>
> **Prazo:** [DATA INÍCIO] a [DATA FIM]. **Investimento:** [VALOR DO TRABALHO].
>
> **Fora do escopo:** outros processos da fila, integrações não listadas acima.

O guia tem o botão **Montar o resumo para o cliente**, que preenche este texto com os números das três ferramentas.

## Relatório do piloto (modelo)

> **Relatório do piloto — [EMPRESA] — [TAREFA]**
>
> - Antes: [N] tarefas/mês, [MIN] min cada, [R$ HOJE] por mês.
> - Depois (30 dias): [N] tarefas, [%] resolvidas pelo agente, [N] voltaram para uma pessoa, conta da IA [R$], [N] reclamações.
> - Diferença real por mês: [R$]. Horas liberadas: [H].
> - Checklist ao fim do piloto: [VEREDITO].
> - Decisão: [segue / ajusta / para] — porque [MOTIVO].
> - Próximo da fila: [TAREFA 2].

## Para aprofundar (cursos e kits abertos do INEMA)

- Profissional 2030 · Consultor de IA (diagnóstico, piloto e medição de valor): https://inematds.github.io/prof2030-consultor/
- Consultor de IA · Do rótulo ao resultado: https://inematds.github.io/consultoria2k/
- Vendas com IA · Playbook de consultoria: https://inematds.github.io/formacao-vendas-ia-consultoria-v72/
- DICA 1 · Mapa do Cliente (diagnóstico): https://inematds.github.io/formacao-dica-diagnostico-v72/
- Área Consultoria de IA (cursos e kits): https://eventos.inema.pro/consultoria-ia/
