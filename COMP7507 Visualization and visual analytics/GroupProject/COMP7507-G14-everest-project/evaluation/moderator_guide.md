# Moderator guide — 25 minutes, 6 participants

> Read the consent line, run the six tasks, close with five statements. Keep help to a minimum.
> The point is to find misunderstandings, not to make the tool look good.

---

## 0. Consent and setup (3 min)

> “Thanks for helping. This is a course project: we are testing an Everest planning interface, not you.
> The session takes about 25 minutes. I will ask you to think aloud — say what you are looking for,
> what you notice, what confuses you. There are no wrong answers. We record only an anonymous
> participant ID, and you can stop at any time. May I take notes and start?”

Record: participant ID, date, role (student / climber / other), familiarity with Everest (1–5).

---

## 1. Warm-up (2 min)

1. “Have you ever looked at Everest expedition data or a route map?” (open, no judgement)
2. “If you were planning an Everest attempt, what would you want to know first?”

Do **not** explain the interface yet.

---

## 2. Tasks

Rules for all tasks:
- Read the task aloud once, hand over the sheet, start the timer.
- If the participant is stuck for **60 seconds**, give **one** neutral prompt: *“What are you looking
  for on this screen?”* Count it as a prompt.
- Do not point at controls, do not name the answer.
- Stop at the time limit; record **N** and move on.

### T1 · Historical change (2 min)

> “Stay in **History**. Find one thing that changed between the 1980s and the 2020s. Point at it and
> tell me what it means.”

**Answer key** (any one, with a number): expedition success 29% → 89%;
median days base camp → summit 44 → 28; expeditions per year 14 → 40+.
Success = a change + a rough number. Watch for: reading a single bar as a trend; ignoring n.

### T2 · Compare two sides (3 min)

> “Go to **Routes**. Keep spring and the 2020–2024 period. Compare the south and north sides: which
> has the higher success rate, what are the two sample sizes, and would you trust that comparison?”

**Answer key**: south **157 / 173 = 90.8%**, north **11 / 13 = 84.6%**.
The point is the tiny north sample — a good answer says “north has only 13, so the comparison is weak”.
Success = both rates **and** both n. Watch for: quoting 91% vs 85% without n; treating the difference
as real.

### T3 · Inspect the route panel (2 min)

> “Scroll to the camp altitude profile. On the south side, which camp is listed by the smallest share
> of expeditions? And read me the note under the chart — what does it say this panel is?”

**Answer key**: the **summit** has the smallest share on the south side (69%);
the note says it is a **schematic cross-section built from the campsite field, with no georeferencing**
(not a map).
Success = correct camp + correctly identifies it as schematic. Watch for: assuming it is a real map;
believing the summit is “reached by 69% of expeditions” rather than “listed in the schedule field”.

### T4 · Enter a profile (4 min)

> “Go to **Your plan** and enter this plan: **age 40–49, male, spring, south side, standard route,
> 20 members, 30 hired staff, oxygen yes**. Then tell me: the estimate, the comparable sample size,
> and what the comparable group actually did.”

**Answer key**: model **≈ 69%** (69.2%), comparable members **626**, observed **402 / 626 = 64.2%**;
expedition-level **≈ 97%**, comparable expeditions 191, observed 189 (98.9%).
Success = reads the big number + the cohort n/rate without help. Watch for: reading 95% interval as
“range of individual outcomes”; confusing member and expedition rows.

### T5 · Interpretation under change (3 min)

> “Now switch **oxygen to No**. What happens to the number, and what would you tell a friend about how
> much to trust it?”

**Answer key**: the estimate collapses to about **3%**; the status shows few comparable records; a
cautious answer mentions that oxygen-free cases are rare and self-selected, and that the model smooths
an extreme group.
Success = notices the drop **and** gives a reason to distrust the precision. Watch for: treating 3%
as a precise personal prediction.

### T6 · Find a limitation (2 min)

> “Open **Data & methods** and read me one limitation of the model.”

**Answer key** (any one): 2020–2024 runs higher than the model average (under-prediction in calibration);
oxygen is a near-perfect separator; associations not causal; sparse cells return insufficient evidence.
Success = one concrete limitation in their own words.

---

## 3. Closing (5 min)

Ask, then show the **five statements** on the sheet (1 = strongly disagree, 5 = strongly agree):

1. I could find what I needed without help.
2. The charts made the comparison clear.
3. I understood what the estimate means.
4. I understood what the tool cannot tell me.
5. I would use this if I were planning a trip.

Then open questions:

- “What was the most confusing moment?”
- “Was there anything you expected to find that was not there?”
- “If you could change one thing, what would it be?”
- “Did anything feel misleading or too confident?”

---

## 4. Answer key summary (for the note-taker)

| Task | Expected | Success signal |
|---|---|---|
| T1 | success 29% → 89%; days 44 → 28 | change + number |
| T2 | south 90.8% (n=173), north 84.6% (n=13) | both rates + both n, warns about n |
| T3 | summit 69%; “schematic, no georeferencing” | camp + caveat |
| T4 | 69%, n=626, observed 64.2%; expedition 97% | number + cohort |
| T5 | ~3%, few comparable records | drop + reason |
| T6 | era drift / oxygen separability / associations | one concrete limitation |

## 5. Moderator's own checklist after each session

- [ ] record sheet filled (all six tasks, times, prompts)
- [ ] confidence ratings and five closing statements entered
- [ ] 2–3 verbatim quotes captured
- [ ] one-line “biggest misunderstanding” written while it is fresh
- [ ] any bug reproduced once and noted with the exact steps
