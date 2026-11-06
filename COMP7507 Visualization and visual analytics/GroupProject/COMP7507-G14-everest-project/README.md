# COMP7507 · Group 14 — project folder

Everest climbing decision support: history, routes, and profile-based summit-success estimation.

## What is here

| Path | What it is |
|---|---|
| `Proposal(1).docx` / `Proposal.pdf` | the submitted proposal (Part A–D) |
| `Himalayan+Expeditions/` | the untouched CSV snapshot (Maven Analytics / The Himalayan Database) |
| `proposal_check/` | 28-check data audit: `proposal_data_check_report.md`, `claim_checks.csv`, 4 figures, scripts |
| `everest-app/` | the offline application (`index.html`) + pipeline + README + screenshots |
| `evaluation/` | 6-participant task test: moderator guide, participant sheet PDF, record sheet, analysis plan |
| `discussion_1_prep.md` | 3–5 minute walkthrough script and questions for Discussion 1 |
| `discussion_1_onepager.pdf` | A4 handout for Discussion 1 |

## Status against the proposal

Legend: ✅ done · 🟡 partial / needs a decision · ⬜ not started

| Proposal item (Part B / C) | Status | Where / note |
|---|---|---|
| Historical view: annual & decade trends, seasons, duration, team/support, oxygen, success, deaths | ✅ | app module 01 |
| Season × decade heatmap, linked interval charts, counts vs rates, sample sizes | ✅ / 🟡 | heatmap, decade highlighting, year zoom; no brush-select of a year range |
| Route explorer: filter side / route group / season / period | ✅ | app module 02 |
| Compare duration, team size, support, oxygen, success, risk | ✅ | six-metric like-for-like panel |
| 2D map and 3D terrain with camps / waypoints | ✅ | SRTM 30 m terrain (Mapzen/AWS tiles) + camp chain mapped in OpenStreetMap (ODbL); 2D hillshade map and 3D WebGL terrain in app module 02. The expedition CSV itself still has no coordinates — documented. |
| Current 2025–2026 aggregate indicators, kept separate | 🟡 | 2026 spring only (the cited sources cover 2026); clearly separated layer |
| Profile inputs (age band, sex, season, side, route group, team, support, oxygen) | ✅ | app module 03 |
| Rank comparable historical plans | ✅ | cohort ladder + “closest historical expeditions” table |
| Regularised logistic vs constant and side×season baselines | ✅ | Brier / log loss / AUC on a held-out period |
| Only pre-expedition variables; exclude post-expedition fields | 🟡 | no summit date / reached altitude / deaths as predictors. “Oxygen used” and “hired above BC” are recorded during the expedition; documented as a limitation. |
| Comparable sample size, uncertainty intervals, calibration, explanatory variables | ✅ | result card + calibration chart + drivers |
| Sparse profiles return insufficient evidence | ✅ | exact cell < 10 → no number |
| Data checks: keys, filters, missingness, denominators, empty states | ✅ | 28-check audit + 23-check in-browser self-test (`?selftest=1`) |
| Browser-versus-Python results | ✅ | same self-test compares 8 model predictions and 6 cohort counts |
| Train / validation / test = 1990–2014 / 2015–2019 / 2020–2024 | ✅ | evaluation; deployed coefficients refit on 2005–2024 and documented |
| Compare Brier, log loss, AUC, calibration curves | ✅ | model card + Data & methods |
| Visual analysis: do seasonal / route differences survive similar groups? | 🟡 | supported by the charts and the model, but not yet written up as a report section |
| About six external users, completion / time / misunderstandings | ⬜ | kit is ready in `evaluation/`; session not yet run |
| Offline application via `index.html` | ✅ | no build, no server, no network requests |
| Report (30 Nov) | ⬜ | outline in `report/outline.md` |
| Demo (21/28 Nov) and peer evaluation | ⬜ | — |
| MapLibre / 3D terrain | ✅ / 🟡 | 3D WebGL terrain shipped (three.js + SRTM); a MapLibre tile-style variant remains optional |

Roughly **95% of Part B is implemented**; what remains is the user-test session and the written report.

## Remaining work, in order

1. **Consultation** — settle the map/3D weight and the member-vs-expedition estimate (see
   `discussion_1_prep.md`). Everything else can proceed regardless.
2. **Run the 6-user test** — `evaluation/README.md` has the full kit; about half a day plus analysis.
3. **Report** — `report/outline.md` maps every proposal section to existing figures, tables and numbers.
4. **Demo** — 8-minute script built from the three views plus the self-test panel.
5. **Optional polish** — MapLibre style variant, per-expedition drill-down from the map, exporting a
   scenario as an image.
