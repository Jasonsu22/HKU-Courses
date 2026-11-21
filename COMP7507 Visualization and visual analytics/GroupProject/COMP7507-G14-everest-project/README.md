# COMP7507 · Group 14 — project folder

Everest climbing decision support: history, routes, and profile-based summit-success estimation.

## What is here

| Path | What it is |
|---|---|
| `index.html` | starting page for the submission: links to the app, kit and documents |
| `DEMO_AND_STORY_GUIDE.md` | how to tell the story and run the demo, with exact clicks and links |
| `VISUALIZATION_UPGRADE_PLAN.md` | the reviewed plan for this upgrade |
| `version_comparison/` | before and after versions side by side, with differences highlighted |
| `Himalayan+Expeditions/` | the untouched CSV snapshot (Maven Analytics / The Himalayan Database) |
| `proposal_check/` | 28-check data audit: `proposal_data_check_report.md`, `claim_checks.csv`, 4 figures, scripts |
| `everest-app/` | the offline application (`index.html`) + pipeline + README + screenshots |
| `evaluation/` | 6-participant task test: moderator guide, participant sheet PDF, record sheet, analysis plan |
| `discussion_1_prep.md` | Discussion 1 walkthrough, kept as a record of that session |
| `docs/05-记录/模块1-3改动清单_2026-11-14_v1.md` | layout, interaction and terminology change log |
| `report/outline.md` | outline of the final report |

The submitted proposal is `../Proposal.pdf`.

## Status against the proposal

Legend: ✅ done · 🟡 partial · ⬜ not started

| Proposal item | Status | Where / note |
|---|---|---|
| Historical view: trends, seasons, duration, support, oxygen, success, deaths | ✅ | page 1, linked by a timeline brush |
| Season × decade heatmap, linked interval charts, counts vs rates, sample sizes | ✅ | page 1 |
| Route explorer: side, route group, season, period | ✅ | page 2 |
| Compare duration, team size, support, oxygen, success, risk | ✅ | dumbbell small multiples with intervals |
| Charts connected to 2D map and 3D terrain | ✅ | filters drive route width and camp shares; altitude hover links funnel, profile, map, 3D |
| Current 2025–2026 indicators, kept separate | 🟡 | 2026 spring only (sources cover 2026) |
| Profile inputs and ranked comparable plans | ✅ | page 3 form, parallel coordinates, closest expeditions |
| Regularised logistic vs baselines | ✅ | Brier, log loss, AUC on held-out 2020–2024 |
| Only pre-expedition variables | 🟡 | no post-expedition outcomes used; oxygen and hired staff are recorded during the expedition, stated openly |
| Sample size, intervals, calibration, explanations | ✅ | page 3 Estimate and Trust |
| Sparse profiles return insufficient evidence | ✅ | exact cell under 10 gives no number |
| Data checks and browser-vs-Python | ✅ | 28-check audit, 59-check self-test (`?selftest=1`) |
| Train / validation / test split | ✅ | deployed coefficients refit on 2005–2024, closures excluded |
| Visual analysis of similar groups | ✅ | hypotheses H1–H8, factor heat map, network |
| About six external users | ⬜ | kit updated in `evaluation/`; sessions not yet run |
| Report (30 Nov) | ⬜ | outline in `report/outline.md` |
| Demo (21/28 Nov) and peer evaluation | ⬜ | script in `DEMO_AND_STORY_GUIDE.md` |

## Remaining work, in order

1. **Run the 6-user test.** `evaluation/README.md` has the kit.
2. **Rehearse the demo.** `DEMO_AND_STORY_GUIDE.md`, including a backup recording.
3. **Write the report.** `report/outline.md` maps sections to figures and numbers.
4. **Package.** The zip's starting page is `index.html`; add the report PDF link there.
