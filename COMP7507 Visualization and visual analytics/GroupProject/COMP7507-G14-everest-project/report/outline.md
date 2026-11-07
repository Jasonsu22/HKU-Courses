# Report outline — Everest climbing decision support

**How to write each section: see [REPORT_GUIDE.md](REPORT_GUIDE.md).**

Required format: one PDF. **Part I** up to 20 pages (excluding title page and references), **Part II**
up to 5 pages per member. Every figure below can be captured from the app; the numbers are the ones the
app and the audit use.

## Required items checklist (from the project requirements)

- [ ] Project title and objectives; group number, names, student IDs
- [ ] **Highlights of the work in THREE bullet points** (draft below)
- [ ] Visualizations created, and their effectiveness for developing hypotheses
- [ ] Methods tried and why we chose them (including rejected techniques; see the upgrade plan, Section 6)
- [ ] Difficulties; things not done and why; limitations; references
- [ ] **Part II: individual contributions** for each of the five members (tasks, results or findings)

### Three highlights (draft)

1. An audited data layer, including a rule based on the dataset's own notes that removes cancelled 2014–15 expeditions and cuts an inflated oxygen effect from about 69× to about 22× the odds.
2. Coordinated views across three pages, using temporal, network, tree and multivariate techniques, where filters and brushes drive every chart, the map and the 3D terrain.
3. Eight hypotheses tested visually, each reproducible in one click, ending in a plan estimate that shows its uncertainty, its behaviour through time and when evidence is insufficient.

---

## 1. Abstract (≈180 words)

One paragraph: the decision problem; the three linked views; the data audit; the two models and their
held-out performance; the main finding (side/season differences survive like-for-like comparison, but
the estimate must be read as a historical association with wide uncertainty); one line on limitations.

## 2. Introduction (≈600 words)

- Everest planning is a decision under uncertainty, not a single “go / no-go”.
- Three questions a planner actually asks: *what changed? how do the sides compare? what did people
  like me achieve?*
- Why existing dashboards are not enough: totals without denominators; maps without coordinates;
  predictions without calibration.
- Contributions, stated as four bullets: (1) audited data layer, (2) linked historical/route explorer,
  (3) calibrated profile estimate with an insufficient-evidence rule, (4) open offline implementation.

## 3. Related work (≈450 words)

- The Himalayan Database as the reference archive; Maven Analytics distribution.
- Visual analytics for outdoor/expedition decisions (small multiples, linked views, uncertainty).
- Calibration and proper scoring rules (Brier, log loss) versus accuracy.
- Why three.js rather than MapLibre: fully offline, and the expedition CSV has no coordinates, so terrain comes from SRTM tiles and camps from OpenStreetMap.

## 4. Data (≈900 words)

Table 1 — snapshot and audit summary (from `proposal_check/claim_checks.csv`):

| Item | Value |
|---|---|
| expeditions / member records / peaks / references | 11,425 / 89,000 / 480 / 15,586 |
| Everest subset | 2,347 expeditions, 25,274 participation records, 1921–2024 |
| successful expeditions (route 1) | 1,479 (63.0%) |
| recorded deaths | 208 members + 132 hired = 340 |

Three traps that shaped the implementation (each with the number from the audit):

1. **`expid` collides across centuries** — `EVER21101` is 1921 *and* 2021; joins use
   `(peakid, year, expid)`; 49 member rows are assigned by rule.
2. **`members.myear` is wrong before 2000** — 96.1% of pre-2000 rows disagree with their expedition;
   year is taken from the expedition record. `mseason` matches 89,000/89,000.
3. **Hired staff are only half listed** — 8,323 of 15,533 on Everest; hired rates use expedition fields.

Also: rates always carry numerator, denominator, unit and n; counts and rates are never mixed in one
axis; the schematic panel is labelled because no coordinates exist (2,319 campsite strings, 0 with
coordinates).

## 5. Design (≈1,100 words)

### 5.1 Story and product path
History → Routes → Your plan; one offline page, three tabs, shared definitions.

### 5.2 Module 01 — history
Figure 1 (screenshot `docs/screens/history.png`): annual scale (two aligned panels, no dual axis),
decade success with Wilson intervals, season × decade heatmap (sqrt colour for skewed counts),
duration quantiles, support structure, oxygen, deaths with rate per 1,000.
Interaction: decade highlighting across three charts; year-range chips.

### 5.3 Module 02 — routes and terrain
Figure 2 (`docs/screens/routes.png`): filter bar (side, season, period, route group), six-metric
like-for-like panel, route families (≥20 expeditions), camp altitude cross-section.

A dedicated **route & terrain** card adds the geographic layer the CSV lacks:

- SRTM 30 m elevation model (Mapzen / AWS Open Data tiles) rendered as a hillshade map
  and as an interactive WebGL terrain mesh (three.js, vertical exaggeration ×1.7).
- Camp chains, cols and peaks mapped from OpenStreetMap (ODbL), with OSM elevations
  cross-checked against the database medians in the tooltip; a dashed line connects the
  camps (schematic, not a surveyed track); graticule, scale bar, north arrow and
  attribution are drawn on the map.

The 2026 layer remains separate and never merged.

### 5.4 Module 03 — plan
Figure 3 (`docs/screens/plan.png`): form, probability with bootstrap interval, comparable cohort
ladder, closest historical expeditions, drivers, calibration, model card.
The “insufficient evidence” path (exact cell < 10) is a design decision, not an error state.

### 5.5 Encoding and interaction choices
Small multiples over dual axes; interval marks for every rate; sample size visible; dimming for
missing data; empty states instead of zeros; URL-encoded scenarios for sharing/reproduction.

## 6. Method (≈800 words)

- Two regularised logistic regressions; member model is the headline because age and sex only exist
  at member level; expedition model as context.
- Predictors (8), all known before the expedition in principle; caveat that “oxygen used” and “hired
  above BC” are recorded during the expedition.
- Time split 1990–2014 / 2015–2019 / 2020–2024; deployment refit 2005–2024; λ = 1 chosen on validation.
- Closure rule: 130 expeditions abandoned in 2014–15 per `termnote` excluded from fitting; oxygen factor about 69× → 22×. Show before and after values.
- Baselines: constant rate, side × season.
- Metrics: Brier, log loss, AUC, 10-bin calibration; 95% intervals from 300 bootstrap refits.
- Comparable cohorts: exact / mid / broad matching; sparse → insufficient evidence.

Table 2 — held-out 2020–2024 performance (from the model card):

| Member model | Brier | Log loss | AUC |
|---|---|---|---|
| Constant | 0.286 | 0.766 | 0.500 |
| Side × season | 0.253 | 0.699 | 0.476 |
| Logistic | 0.220 | 0.628 | 0.651 |

| Expedition model | Brier | Log loss | AUC |
|---|---|---|---|
| Constant | 0.156 | 0.500 | 0.500 |
| Side × season | 0.109 | 0.387 | 0.593 |
| Logistic | 0.044 | 0.188 | 0.942 |

## 7. Results (≈1,000 words)

Organise this section around hypotheses H1 to H8 (`DEMO_AND_STORY_GUIDE.md` has the current numbers).

### 7.1 What changed
Expedition success 29.1% in the 1980s → 88.9% in 2020–2024; median BC→summit 44 → 28 days; hired staff
per member rose from 0.60 in the 1990s to 1.47 in 2020–2024; oxygen use 76.3% overall and 92.6% in 2020–2024.
Figure 1 again or a cropped panel.

### 7.2 Do side and season differences survive like-for-like comparison?
Spring 2020–2024: south 157/173 = **90.8%**, north 11/13 = **84.6%** — the gap is small and the north
sample is tiny. All-season and all-period: south 68.2% vs north 55.2%. Before 2000: 52.7% vs 30.3%. From 2000: 71.8% vs 65.4%.
Autumn: south 38.3% (49/128) vs north 7.8% (8/102). The overall gap shrinks a lot when comparing similar periods and seasons.
Module 03 shows how the matching rule matters for the default profile: exact 75.0% (440/587), same oxygen 73.4% (920/1,254), widest 69.8% (923/1,323).

### 7.3 Model behaviour and where it fails
Calibration points sit above the diagonal for 2020–2024 (under-prediction); oxygen is a near-perfect
separator, so oxygen-free estimates are unstable and are flagged; the expedition model smooths the
oxygen-free case, and the UI shows the observed comparable group next to it with a caution.

### 7.4 Reproducibility check
The browser ↔ Python self-test: 53/53 checks (`?selftest=1`), including 8 model predictions, 6
cohort counts and the numbers behind every finding. Appendix B holds the 28-row audit table and the file checksums.

## 8. Evaluation (≈600 words — fill after the six sessions)

- Protocol in `evaluation/README.md`; tasks T1–T6; metrics completion, time, prompts, confidence.
- Table 3: task, Y/P/N, median time, mean confidence.
- Two verbatim quotes illustrating the most common misunderstandings.
- Revisions made (revision log) and what was intentionally not changed.
- Threats: 6 participants, convenience sample, one moderator, no audio recording.

## 9. Discussion and limitations (≈500 words)

- Observational data; associations only; no causal claim for oxygen, support or route choice.
- The expedition CSV itself has no coordinates; the terrain layer is therefore assembled from public
  sources (SRTM tiles, OpenStreetMap camps), and the route line between camps remains schematic.
- Era drift: the deployed model averages 2005–2024 and still under-predicts 2021–2024.
- Small cells and self-selection (who attempts without oxygen).
- Offline, static 2024 snapshot; 2026 layer is aggregate only.

## 10. Conclusion and future work (≈300 words)

- What a planner can do with the tool; what it deliberately refuses to do.
- Future: verified waypoint/DEM layer, per-expedition drill-down, rolling-origin calibration,
  live season ingestion with a clear separation from microdata.

## 11. References (Part I ends here)

The proposal's [1]–[10] plus the two 2026 news sources; cite the Himalayan Database download and the
Maven Analytics page with access dates.

## Appendix

A. 28-row claim audit (`proposal_check/claim_checks.csv`, condensed).
B. File checksums (`data/everest_data.js` → `meta.checksums`).
C. Participant task sheet (PDF).
D. Model feature list and coefficients (`data/model.json`).

---

## Part II — individual contributions (up to 5 pages per member)

One section per member: name, details of tasks completed, results or findings (referencing Part I figures).
Each member writes their own. The module ownership in the proposal's Part C is a starting point.

---

### Figures checklist

| Fig | Source | Status |
|---|---|---|
| 1 History view | `everest-app/docs/screens/history.png` | ready |
| 2 Routes view | `everest-app/docs/screens/routes.png` | ready |
| 3 Plan view | `everest-app/docs/screens/plan.png` | ready |
| 4 Data audit figures | `proposal_check/figs/` | ready |
| 4b 2D map / 3D terrain close-up | `everest-app/data/terrain/` render or screenshot | capture |
| 4c Route & terrain card | crop of `docs/screens/routes.png` | ready |
| 5 Self-test panel | screenshot `?selftest=1` | capture before submission |
| 6 Evaluation results | after the six sessions | pending |
