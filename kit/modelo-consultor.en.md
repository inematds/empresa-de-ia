# Consultant's model: applying the "Your AI company" kit to a client

For people who do AI consulting for small and medium-sized businesses. There are 6 steps, from the first coffee to the 30-day pilot report, using the tools in the guide (https://inematds.github.io/empresa-de-ia/guia/en/).
The underlying rule: **one process at a time, measured before and after**. You don't sell "AI"; you sell a task that starts costing less and a number that proves it.

## The 6 steps

| # | Step | Time | Tool | What you deliver |
|---|---|---|---|---|
| 1 | Diagnostic conversation | 1 h | Script below | List of the tasks that repeat |
| 2 | Process X-ray with the owner | 30 min | Process X-ray | The queue of the first 3 processes |
| 3 | Baseline and calculation | 30 min + 1 week of measuring | Cost-per-task calculator | Today's cost and the cost with the agent, in your currency |
| 4 | Where it runs and whether it can go live | 1 h | Factory comparison + checklist | Chosen path (ready-made, API or own machine) and the checklist verdict |
| 5 | 30-day pilot | 4 weeks | Weekly measurement spreadsheet | 4 measurements: tasks, handbacks to a person, cost, complaints |
| 6 | Report and next in the queue | 1 h | Calculator with the real numbers | Before × after and the decision: continue, adjust or stop |

In step 4, the checklist needs to give at least **pilot with supervision**. Without the mandatory items 2, 4 and 10, the pilot only runs with a person approving each response.

## 1. Diagnostic conversation script (1 hour)

Talk with the owner and with the people who do the day-to-day work. Write down the answers as tasks: verb + object + frequency.

1. What does the team do every week that is always the same?
2. Which customer questions come in repeatedly (price, hours, deadline, status)?
3. Where do these messages arrive: WhatsApp, email, phone, Instagram?
4. What paperwork passes through someone's hands: invoices, payment slips, contracts, spreadsheets?
5. About how long does each one take? How many times per week?
6. Is there a written rule for it, or does each person do it their own way?
7. Is the information in a system or spreadsheet, or only in someone's head?
8. What happens if this task goes wrong? (loses a customer, loses money, legal problem)
9. Which task does the team hate doing the most?
10. What do customers complain about most regarding delays?
11. Which systems does the company already pay for (calendar, ERP, online store, accounting)?
12. Is there sensitive customer data (health, financial, documents)? Where is it stored today?

Output: 8 to 15 tasks for the X-ray. Ask the team to log three days if the owner doesn't know the numbers.

## 2. X-ray with the owner (30 minutes)

Fill in the X-ray together with the owner, on their screen. The queue comes out of the calculation of hours per month × clear rule × digital data ÷ risk. Explain the queue in one sentence per item. If the first in the queue is high-risk, agree that a person approves each reply during the pilot.

## 3. Baseline and calculation (30 minutes + 1 week)

Before changing anything, measure the chosen process for one week: how many tasks, how long each takes, how much the hourly cost of the person doing it is. Without a baseline there is no "after." Fill in the calculator with those numbers and with an honest estimate of what the agent resolves on its own (start at 50% to 70%).

## 4. Where it runs and whether it can go live (1 hour)

- Use the factory comparison: ready-made tool, cloud API or own machine.
- Sensitive data calls for a conversation with the client's lawyer about the LGPD (Brazil's data protection law; in other countries, the local equivalent) before choosing; the guide does not replace that analysis.
- Run the safe-agent checklist with whoever will look after the agent. Record the verdict in the summary.

## 5. 30-day pilot

Ready-to-fill spreadsheet: `kit/piloto-semanal.en.csv`.

A simple spreadsheet, one row per week:

| Week | Tasks done by the agent | Handed back to a person | AI cost ($) | Complaints | Notes |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

Set up a short meeting every week (15 minutes) to look at the spreadsheet and the agent's log.

## 6. Report and next in the queue (1 hour)

Redo the calculator with the real numbers from the pilot and decide together with the owner:

- **Continue:** positive difference, green checklist, few complaints. Move on to the second in the queue.
- **Adjust:** many handbacks to a person or cost above forecast. Fix the rule or the model and measure for 2 more weeks.
- **Stop:** negative difference or a risk that doesn't close. That is also a result; record why.

## One-page proposal (template)

> **Proposal — first AI agent for [COMPANY]**
>
> **The problem:** [FIRST TASK IN THE QUEUE] takes [X] hours per month of the team's time and currently costs about [$ TODAY] per month.
>
> **What we will do:** an AI agent that does [TASK], with a person reviewing whatever it doesn't know. It runs on [PATH: ready-made tool / cloud API / own machine].
>
> **How we measure:** one week of baseline, 30 days of pilot with weekly measurement, and a before × after report.
>
> **Expected calculation:** cost with the agent of [$ AGENT] per month; expected difference of [$ DIFFERENCE] per month. The numbers will be redone with the real pilot data.
>
> **Safety:** safe-agent checklist with verdict [VERDICT]; irreversible actions (paying, deleting, mass sending) only with a person's approval.
>
> **Timeline:** [START DATE] to [END DATE]. **Investment:** [VALUE OF THE WORK].
>
> **Out of scope:** other processes in the queue, integrations not listed above.

The guide has the **Build the summary** button, which fills in this text with the numbers from the three tools.

## Pilot report (template)

> **Pilot report — [COMPANY] — [TASK]**
>
> - Before: [N] tasks/month, [MIN] min each, [$ TODAY] per month.
> - After (30 days): [N] tasks, [%] resolved by the agent, [N] handed back to a person, AI bill [$], [N] complaints.
> - Real difference per month: [$]. Hours freed: [H].
> - Checklist at the end of the pilot: [VERDICT].
> - Decision: [continue / adjust / stop] — because [REASON].
> - Next in the queue: [TASK 2].

## Go deeper (open INEMA courses and kits)

- Professional 2030 · AI Consultant (diagnosis, pilot and value measurement) (in Portuguese): https://inematds.github.io/prof2030-consultor/
- AI Consultant · From label to result (in Portuguese): https://inematds.github.io/consultoria2k/
- Sales with AI · Consulting playbook (in Portuguese): https://inematds.github.io/formacao-vendas-ia-consultoria-v72/
- DICA 1 · Client Map (diagnosis) (in Portuguese): https://inematds.github.io/formacao-dica-diagnostico-v72/
- AI Consulting area (courses and kits): https://eventos.inema.pro/consultoria-ia/en/
