# Task-based evaluation kit

Proposal commitment: *“Approximately six external users will complete tasks that follow the product
path: identify a historical change, compare two routes, inspect the terrain view, enter a profile, and
interpret the estimate and its limitations. Completion, time, and misunderstandings will guide
revisions.”*

This folder contains everything needed to run that session and turn it into a revision list.

| File | Use |
|---|---|
| `moderator_guide.md` | Script, task wording, answer key, prompts policy, closing interview |
| `participant_sheet.pdf` | One page to print per participant (tasks + ratings, no answers) |
| `participant_sheet.html` | Source of the PDF if you need to edit it |
| `record_sheet.csv` | One row per participant × task; open in Excel / Numbers. **The P01 rows already in it are format examples; delete them before the first real session.** |
| `analysis_plan.md` | How to turn the rows into completion rate, time, error themes and a revision log |

## Before the session

- 6 participants **outside the group** (classmates are fine; ideally 2 with outdoor/climbing interest).
- 30-minute slots. One moderator, one note-taker if possible.
- Laptop with `../everest-app/index.html` open (offline; no server needed), browser at 100% zoom.
- Print one `participant_sheet.pdf` per person and one `record_sheet.csv` (or a copy per participant).
- Tell participants: anonymous ID only, no personal data, they can stop at any time, we test the
  interface not them.

## What to record

- Completion: **Y** (unaided), **P** (with one prompt), **N** (failed / gave up).
- Time: start when the participant starts reading the task, end when they state an answer.
- Prompts: count them; note the wording.
- Confidence 1–5 after each task.
- Verbatim quotes for misunderstandings (“I thought the bar was a map…”, “so it is guaranteed?”).

## What to do with the result

`analysis_plan.md` turns 6 × 8 rows into a one-page table plus a ranked revision list. Changes go into
the app and into the report's evaluation section; the proposal's fallback order (reduce decorative
detail before removing denominators or uncertainty) decides what gets cut if a revision is expensive.
