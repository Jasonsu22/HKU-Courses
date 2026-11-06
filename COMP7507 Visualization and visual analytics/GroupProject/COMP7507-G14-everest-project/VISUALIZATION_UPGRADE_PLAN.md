# Everest project: visualization upgrade plan

**Status: approved and built.** Baseline commit: `8e6b16f` on local branch `comp7507-everest-viz` (not pushed).

Decisions taken: model retrained without the closures (using a rule from the dataset's `termnote` field), operator network included, one local commit per page.
Numbers below are the planning estimates. A few moved slightly when recomputed (for example H8 is 794, not 802, and the factor is about 22×); `DEMO_AND_STORY_GUIDE.md` has the final figures.

This plan covers all three pages of the HTML app. It answers your three questions:

| Your question | Section |
|---|---|
| How will it be demonstrated? | [Section 7](#7-how-it-will-be-demonstrated) |
| What will be shown? | [Sections 3 to 5](#3-page-1-history) (per page) and [Section 2](#2-the-story-the-whole-app-will-tell) (the story) |
| What visualization techniques will be used? | [Section 6](#6-visualization-techniques-mapped-to-the-slides) and the tables in Sections 3 to 5 |

---

## 1. Why change the app

**The grade depends on exploration.** The course rubric gives "mostly descriptive visualizations" C to B-, and "mostly explorative visualizations with effective applications of visual analysis" B+ and above. Complexity of variables and use of multiple data sources also count.

Today the app is accurate and well audited, but it is mostly descriptive:
- Most charts show one fixed answer, and only decade highlighting and the page 2 filters change what you see.
- Pages do not connect to each other.
- Bars and tints are pale, and nothing stands out at a glance.
- Page 3 shows one flat number with no sense of time or connection.

**What the teacher asked for.** My reading of "model visualization tag" is "use the visualization techniques taught in class as much as possible". That phrase does not appear in the slides, so please correct me if the teacher meant something else.

**The rule for adding a chart.** Every view must answer a question a planner or analyst would really ask, and must use a technique we can justify from the slides. Techniques that don't fit are listed as rejected in Section 6, which is a good thing to say in the demo and the report.

**Numbers in this plan** come from quick read-only checks of the CSVs. Each one will be recomputed in the pipeline before it appears in the app or report.

---

## 2. The story the whole app will tell

Today the pages are three separate topics. They become one line of reasoning:

> **"Everest success rose from about 30% to about 89%. Why, for whom, and does it apply to my plan?"**

| Step | Page | Question | Evidence the page will show |
|---|---|---|---|
| 1 | History | Did the mountain get easier? | Success rose on Everest, but not on every Himalayan peak (Baruntse went from 40% to 33%). Risk fell much less per person than per summit. |
| 2 | Routes | Does where and when you climb matter? | The south and north gap changes over time and is thin in 2020–24. Summit days cluster tightly around 19–23 May. |
| 3 | Your plan | Does this apply to me, and how far can I trust it? | The plan's own success through time, how choices connect, and which real expeditions resemble it. |

### Hypotheses the app will test

The course assesses hypothesis generation and verification, so these become a visible feature. Each page gets a **Findings** rail: clicking a finding sets the charts to the state that shows the evidence.

| # | Hypothesis | What the data suggests so far | Where |
|---|---|---|---|
| H1 | Success rose everywhere, because of better gear and weather forecasting | **Partly rejected.** Everest 30% → 89%, Lhotse 32% → 85%, but Baruntse 40% → 33% and Manaslu 33% → 53% | Page 1 |
| H2 | Climbing has become much safer | **Depends on the denominator.** From before 1990 to 2020–24, deaths per 100 summiters fell from 38.7 to 1.2, but member deaths per 1,000 members only fell from 19.6 to 11.7, and 2020–24 is above the 2010s (8.6) | Page 1 |
| H3 | More hired support is what drives success | **Mixed.** Hired staff per member rose from 0.60 (1990s) to 1.47 (2020–24). The link to success is modest (correlation about 0.19 at expedition level) and not consistent across periods | Pages 1 and 3 |
| H4 | The south side is better | **Not stable.** South was ahead in the 1990s. North looks far ahead in 2020–24 (83% vs 61% of members), but on only 107 members | Page 2 |
| H5 | Arriving early at base camp helps | **Not supported.** Spring standard-route success is 71–75% in every arrival window (2005–24) | Page 2 |
| H6 | Fewer expeditions fail high on the mountain now | **Supported.** Share of south standard-route expeditions reaching 8,840 m rose from 63% to 87%, and north from 44% to 91% (small recent north sample) | Page 2 |
| H7 | A plan's chance is a stable number | **Rejected.** The default plan's group went 54% (1990–94) → 82% (2010–14) → 71% (2020–24), while the app shows one flat 75% | Page 3 |
| H8 | Oxygen multiplies your odds by about 69 times | **Overstated.** 802 of the 1,295 "no oxygen" members come from the cancelled 2014 and 2015 seasons. Removing those years takes the crude odds ratio from 90 to 33 | Page 3 |

---

## 3. Page 1: History

**Goal:** move from "here are the trends" to "explain why things changed".

**Layout**

```
[ KPIs ]                                     [ Findings rail: H1, H2, H3 ]
[ Timeline overview with brush + events: 2014, 2015, 2020 ]   <- controls everything below
Section A  Scale and seasons     | stacked graph        | season x decade heatmap
Section B  Success               | success + intervals  | peak comparison (horizon graph)
Section C  Effort and support    | duration box plots   | support structure | oxygen
Section D  Risk and failure      | deaths, switchable denominator | how expeditions ended
Section E  Who climbs with whom  | operator network
```

### Defects to fix

| Chart | Problem | Fix |
|---|---|---|
| Days from base camp to summit | **Bug:** whiskers are drawn at a slant (`module1.js:372`, `x1` differs from `x2`) | Proper vertical box plots |
| Members and hired staff | The smoothed curve invents shape between years | Unsmoothed yearly steps, or 3-year bins |
| Summit success by decade | Rust bars for 2000 onward have no legend | One colour; highlight only on selection |
| Oxygen use | The 5-year smoothing is only named on the axis, and the 2010s dip is unexplained | Show yearly points behind the smooth line, and mark the 2014–15 events |
| Annual chart | The "2020" label collides with the bars | Move it to the shared events layer |
| Season × decade | Too pale to read | Stronger sequential colour with a clear legend |

### New and upgraded views

| View | Status | Technique | Question | Interaction |
|---|---|---|---|---|
| Timeline overview | Upgrade of the annual chart | Overview + detail, brushing | Which period am I looking at? | Drag a year range. All page 1 charts update. Existing chips become shortcuts. |
| Season composition | New | Stacked graph | Which season drove growth? | Count / share toggle |
| Season × decade | Upgrade | Heat map | When did autumn disappear? | Counts / success toggle; linked highlight |
| Success with intervals | Upgrade | Line + interval band, or bars by decade | Did success really change? | Decade / year toggle; click to link |
| Peak comparison | New, uses all 11,425 expeditions plus `peaks.csv` | Horizon graph, with index chart as toggle | Is Everest special? | Hover to read a year across all 8 peaks |
| Duration | Fix | Box plots | Is climbing faster? | Split by side |
| Support structure | Upgrade | Stacked graph + hired-per-member line | Did staffing change? | Linked to brush |
| Oxygen use | Upgrade | Time series | Did oxygen use change? | Linked to brush |
| Deaths and risk | Upgrade | Time series + data transformation | Did it get safer? | **Switch denominator:** per 1,000 members, per 1,000 hired staff, per 100 summiters. This is the H2 finding. |
| How expeditions ended | New, uses `termreason` | Stacked graph | Why do attempts fail, and did that change? | Count / share toggle; click a reason to highlight |
| Operator network | New, uses `agency` and `nation` | Force-directed layout, filtering, network metrics | Who climbs with whom, and do well-connected operators do better? | Period slider, minimum-expeditions filter, click for ego network |

### Operator network details

- **Nodes:** expedition nations and trekking agencies (bipartite).
- **Edges:** number of expeditions between them.
- **Encoding:** node size shows expeditions, colour shows success, and degree and betweenness appear in the tooltip and can be used for sizing.
- **Scale:** 2005–24 has 73 nations, 240 raw agency names and 591 edges, but only 70 edges with 5 or more expeditions. Filtering makes it readable.
- **Why it's interesting:** agencies of similar size differ a lot, for example Himalayan Guides at 78% (119 expeditions) vs Monterosa Treks at 45% (49 expeditions). These are raw associations, not a ranking of quality.
- **Data work needed:** agency names are messy, such as `Asian Trekking (Climbalaya pmt)`. The pipeline will clean them. The "(X pmt)" text appears to name a permit holder, which could become a second type of edge. I'll confirm this before relying on it.

---

## 4. Page 2: Routes

**Goal:** make this the real exploration view the proposal promised, with **charts connected to the map**. The proposal says the route panel "will connect charts to a 2D map and a 3D terrain view". Today the map and 3D view ignore the filters entirely.

**Layout**

```
[ Filter bar: side, season, period, route group ]      [ Findings rail: H4, H5, H6 ]
[ KPIs ]
Section A  South vs north   | six-metric comparison | side gap through time
Section B  Which route      | route treemap / family bars with intervals
Section C  Where on the mountain | altitude funnel <-> 2D map (with contours) <-> 3D terrain
Section D  When             | summit calendar
Section E  Current          | 2026 layer (still separate)
[ Button: "Use this as my plan" -> page 3 ]
```

### Defects to fix

| Chart | Problem | Fix |
|---|---|---|
| South vs north | Six tiny pale bars, with no uncertainty on rates | Dumbbell small multiples with intervals and clear n |
| Route families | Colour implies side, but "Other" and "West shoulder" mix both | Colour by success or neutral, side as a label, Wilson intervals added |
| Map and 3D | Do not respond to filters | Linked to filters (below) |
| Docs | README still says there are no coordinates and the panel is only schematic | Update the text |

### New and upgraded views

| View | Status | Technique | Question | Interaction |
|---|---|---|---|---|
| Six-metric comparison | Upgrade | Small multiples, dumbbell | How do the sides compare under these filters? | Recomputed by filter |
| Side gap through time | New | Time series with bands + horizon strip of South minus North | Is the gap stable? | Filter-aware; gray-out where n is small |
| Route treemap | New (toggle with bars) | Squarified treemap: side → family → raw route | Which of the 137 route names matter? | Click to zoom and set the filter. Toggle to ranked bars because two routes dominate. |
| Altitude funnel | New, uses `highpoint` | Layered survival curve by altitude | Where do expeditions stop? | Hover an altitude to light up that camp on the map and 3D view |
| 2D map | Upgrade | Geographic map + **contour plot** from our elevation grid | What does the terrain look like here? | Contour toggle. Route line width and colour show the funnel share under the current filters. |
| 3D terrain | Upgrade | 3D terrain, linked view | How does the route sit in the terrain? | Same filter-driven route colouring; hover links to funnel |
| Camp altitude profile | Keep, linked | Linked highlighting | Which camps do records list? | Hover links with map and funnel |
| Summit calendar | New, uses `smtdate` | Heat map (day × year) | When is the summit window, and has it moved? | Side facet; hover for counts; filter-aware |
| 2026 card | Small upgrade | Separate labelled layer | How does 2026 compare? | Hollow marker for 1,008, clearly outside the dataset |

### Linking

Filter bar → all charts, map and 3D. Altitude hover → funnel, camp profile, map, 3D. This is the course's **coordinated multiple views**, and a good moment in the demo. If 3D gets slow on a laptop, it will update only when the filter is released.

---

## 5. Page 3: Your plan

**Goal:** turn one flat number into "how this plan behaves through time, what it connects to, and which real expeditions resemble it".

**Layout**

```
+----------------+----------------------------------------------------------+
| Plan form      | Timeline brush (shared by every view on this page)        |
| (stays pinned) | [Estimate] [Over time] [Connections] [Records] [Trust]    |
| 8 choices      | ...section content...                                     |
+----------------+----------------------------------------------------------+
```

| Section | View | Technique | Question | Interaction |
|---|---|---|---|---|
| **Estimate** | Uncertainty strip (bootstrap range, model, observed group) | Histogram or strip, preattentive pop-out | How sure is this number? | Updates live with the form |
| | **What-if ladder**, replacing the pale bars and "69×" | Dumbbell chart in percentage points | Which single change matters most? | Click a row to apply it |
| **Over time** | **Your plan through time** (headline view) | Time series, interval band, overview + detail | Was this plan always this good? | Brush; event marks at 2014, 2015, 2020 |
| | Factor × period grid | Heat map with a diverging scale around each period's average; small samples hatched | When does each factor matter? | Click a row to send it to the index chart |
| | Factor lines | Index chart with a movable reference year | Which groups improved fastest? | Drag the reference year |
| **Connections** | **Factor network** (headline view) | Force-directed layout, edge filtering, ego network | Which choices travel together, and do they lift or sink success? | Period slider, edge threshold, plan highlighted |
| | Same data as a grid | Adjacency matrix, changing representation | The same question without edge clutter | Toggle; matrix reordering |
| | Plan decision tree | Layered tree (icicle), focus + context | Where does this plan sit among all plans? | Click to zoom or set the form |
| **Records** | Expedition explorer | Parallel coordinates, brushing, dimension ordering | Which real expeditions resemble this plan? | Brush axes, reorder axes; the plan is drawn as a highlighted line; linked to the closest-expeditions table |
| **Trust** | Calibration and model card | Scatter plot, table | How far can I trust the model? | Period toggle |
| | Comparable cohorts | Linked table | How does the matching rule change the answer? | Highlights the rule in use |

**Corrections:**
- The note calling the estimate a "conservative baseline" is wrong for the default plan (71% in 2020–24 vs a model figure of 75%). It will be calculated for each plan.
- The "69×" odds factor gets replaced because people read it as "69 times the chance".

### Decision needed: the cancelled seasons

Many members in 2014–15 never climbed high enough to use oxygen, so they are recorded as "no oxygen" and failed. That inflates the oxygen effect.

| Option | What changes | Downside |
|---|---|---|
| **A. Retrain (recommended).** Exclude 2015 and 2014 South from model training. | Estimates, model card, 8 self-test predictions, and answer keys in the user test | Report must explain the change |
| B. Keep the model and add a warning. | Only a visible warning and a note | The inflated number stays on the page |

The exclusion would be a clearly documented rule, and the excluded seasons would stay visible in every historical chart.

---

## 6. Visualization techniques mapped to the slides

**Used** means it is in the plan. **Rejected** means considered and left out for a stated reason. **Stretch** means only if time allows.

### Lecture 02: Perception and colour

| Topic | Decision | Where and how |
|---|---|---|
| Preattentive pop-out | Used | The current plan or selection is the only strongly saturated element |
| Salience, conjunctions | Used | Selection uses colour plus stroke, not colour alone |
| Colour to label | Used | South and north keep one fixed colour pair across all pages |
| Colour to quantify | Used | One sequential scale for counts, one diverging scale for "above or below average" |
| Lightness and contrast | Used | Fixes the pale look; small text and marks checked for contrast |
| Colour blindness | Used | Palette simulated for colour-blind vision; meaning never relies on hue alone |

The diverging scale will not reuse rust and navy, because those already mean south and north. Exact colours get validated when building.

### Lecture 03: Temporal and multivariate data

| Topic | Decision | Where |
|---|---|---|
| Bar chart, histogram | Used | Annual overview; uncertainty strip |
| Box plot | Used | Page 1 duration (replaces the broken version) |
| Line graph, time series | Used | Pages 1, 2, 3 |
| Scatter plot | Used | Page 3 calibration |
| Contour plot | Used | Page 2 map, from our elevation grid |
| Index chart | Used | Page 3 factor lines; page 1 peak comparison toggle |
| Stacked graph | Used | Page 1 seasons, support, how expeditions ended |
| Horizon graph | Used | Page 1 peak comparison; page 2 side gap |
| Heat map | Used | Pages 1, 2, 3 |
| Parallel coordinates, dimension ordering | Used | Page 3 records |
| Scatter plot matrix | Rejected | Parallel coordinates cover the same data with less space, and most variables are categorical |
| Spiral graph | Rejected | No yearly cycle to reveal, since the season is already an explicit variable |
| Chernoff faces | Rejected | Hard to read accurately, and faces are in poor taste for data that includes deaths |
| Dimension reduction | Rejected | Mostly categorical variables, and axes would be hard to explain to a planner. Possible stretch goal. |

### Lecture 04: Interaction

| Topic | Decision | Where |
|---|---|---|
| Changing representation | Used | Network / matrix, treemap / bars, horizon / index |
| Data transformation | Used | Risk denominators, indexing, counts / shares |
| Selection and filtering | Used | Filter bar, sliders, form, edge threshold |
| Coordinated views, linking and brushing | Used | All pages |
| Overview + detail | Used | Timeline brush on pages 1 and 3 |
| Zooming | Used | Treemap, icicle |
| Focus + context | Used | Icicle zoom keeps the path to the root visible |
| Fisheye, hyperbolic | Rejected | Spatial judgment matters here, and the slides warn distortion hurts that |

### Lecture 05: Trees

| Topic | Decision | Where |
|---|---|---|
| Layered diagram (icicle) | Used | Page 3 plan tree |
| Treemap (squarified) | Used | Page 2 route hierarchy |
| Node-link, radial, cone, balloon, hyperbolic | Rejected | Depth is only 5 and sizes matter most, which a node-link tree shows poorly |
| Voronoi, circular treemaps | Rejected | Add decoration and make areas harder to compare |

### Lecture 06: Networks

| Topic | Decision | Where |
|---|---|---|
| Force-directed layout | Used | Page 1 operators; page 3 factors. Seeded so the layout looks the same every time, as the slides recommend for predictability. |
| Adjacency matrix | Used | Page 3 toggle |
| Filtering | Used | Minimum edge weight, ego network |
| Network metrics | Used on page 1 | Degree and betweenness on the operator network. On the factor network, I use simple connection strength because centrality means little on a constructed graph. |
| Clustering | Stretch | Group agencies or nations if the page 1 network looks cluttered |
| Edge bundling | Rejected | Too few edges remain after filtering to need it |

---

## 7. How it will be demonstrated

### 7.1 How you will review my work

1. **Three review checkpoints.** I stop after each page, in the order below, with screenshots for you to approve.
2. **Before and after gallery.** `everest-app/docs/screens/before/` and `after/`, with one matching state per view.
3. **Exact code diff.** Everything can be compared with the baseline `8e6b16f`, however Decision 5 in Section 12 goes. To review:

```bash
git diff 8e6b16f -- "COMP7507 Visualization and visual analytics/GroupProject/COMP7507-G14-everest-project"
```

4. **Self-test panel.** `?selftest=1` currently passes 23 of 23. It will grow to cover the new views, comparing browser numbers with Python.
5. **Direct links.** Each finding has a link that reproduces it exactly, so you can check any claim in one click.

### 7.2 The live class demo

The requirement is a walkthrough, not a formal talk, and it says to "wisely choose one or two main visualizations". So the demo focuses on two hero views: **Your plan through time** and the **Factor network**.

The requirements page gives no time limit. Our README assumes 8 minutes, so please confirm that. The speakers below follow the proposal's module owners, as a suggestion.

| Time | Speaker | On screen | What to say | Technique to name |
|---|---|---|---|---|
| 0:00–0:40 | E | Page 1 top | The question: success rose from about 30% to 89%. Why, for whom, and does it apply to me? | |
| 0:40–1:40 | B | Brush timeline; peak horizon graph | H1: not every peak improved. Everest did, Baruntse did not. | Overview + detail, horizon graph |
| 1:40–2:20 | B | Switch risk denominator | H2: safety looks very different per summit vs per person. | Data transformation |
| 2:20–3:30 | C | Filter page 2; hover altitude funnel; map and 3D respond | H4 and H6: the gap is unstable and thin, and failures high up have dropped. | Coordinated views, contours |
| 3:30–4:00 | C | Summit calendar | H5: base camp arrival barely matters, but summit days cluster. | Heat map |
| 4:00–5:30 | D | "Use as my plan"; **Your plan through time** | H7: one flat number hides 54% → 82% → 71%. | Time series, interval bands |
| 5:30–6:45 | D | **Factor network**, period slider, switch to matrix | Which choices cluster and how that changed, plus H8 on oxygen and cancelled seasons. | Force layout, ego network, matrix |
| 6:45–7:30 | E | Parallel coordinates with brushing, then calibration | Real comparable expeditions, and how far to trust the model. | Parallel coordinates, brushing |
| 7:30–8:00 | A | Self-test panel and limitations | Data audit, associations not causes, what we can't claim. | |

**Demo safeguards:**
- Use prepared deep links, one per step, so nobody has to set up filters live.
- Run everything offline from `index.html`, tested on the presenting laptop.
- Keep a screen recording as backup, since the requirements allow video clips. If WebGL fails, the 2D map still works.
- Rehearse at projector resolution, and check that chart text is readable from the back of the room, which the demo rubric assesses.

### 7.3 User testing

The six-person test hasn't run yet, so it will cover the new app:
- Answer keys get rechecked for all tasks. T4 and T5 will change if the model is retrained, and T3 and T6 refer to panels and limitations that are changing.
- **T7 (new):** use the plan-through-time view to judge whether a plan's success is stable.
- **T8 (new):** use the network or matrix to name two choices that occur together and what happens to success.
- Session length gets checked, since it's currently 25 minutes and two more tasks may push it over.

---

## 8. Shared work across all pages

| Item | What |
|---|---|
| Shared state | New `js/store.js` holds filters, the plan and the year range, so pages can pass state. Adds page 2 → "Use as my plan" and page 3 → "See this route". All state remains in the URL. |
| Design system | Shared colour tokens, legends, event marks, card headers, section navigation |
| Findings rail | One component on all three pages; clicking applies the state for that finding |
| Small-sample rule | One consistent treatment on all charts: hatched or faded with n visible. Fewer than 10 records still gives "insufficient evidence" on page 3. |
| Accessibility | Keyboard access for main controls, labels on charts, non-colour cues |
| Performance | Sections render only when opened; network layouts are seeded; no network requests |

### Files

| File | Change |
|---|---|
| `everest-app/pipeline/build_plan_data.py` | **New.** Anonymised member rows (no names), cleaned agency names, season-closure flag, peak comparison, network edges |
| `everest-app/pipeline/prepare.py`, `build_data.py` | Add `highpoint`, `termreason`, `smtdate`, `bcdate`, `agency`, `nation` to the data |
| `everest-app/pipeline/train_model.py` | Only if option A is chosen |
| `everest-app/data/` | Regenerated; one new compact data file (estimated at a few hundred KB) |
| `everest-app/js/store.js`, `components.js` | **New.** Shared state and chart helpers |
| `everest-app/js/module1.js`, `module2.js`, `geo.js`, `module3.js` | Upgraded |
| `everest-app/js/plan_time.js`, `plan_links.js`, `plan_records.js`, `network.js` | **New.** Keeps `module3.js` a manageable size |
| `everest-app/index.html`, `css/app.css` | New sections and design tokens |
| `everest-app/js/selftest.js` | More checks |
| No new libraries | D3 and three.js are already vendored, so it stays offline |

---

## 9. Proposal and document changes

The proposal has been submitted, so these go in the report as "changes since the proposal", with the reason for each.

| Proposal item | Change | Reason |
|---|---|---|
| Methods: heatmap, linked intervals, maps | Add temporal, network, tree and multivariate views | Teacher feedback and the rubric |
| "Only variables available before an expedition" | Oxygen and hired staff are recorded during it. State this plainly, and handle the cancelled seasons. | The promise isn't fully met today |
| "Estimate recorded expedition summit success" | Member-level headline, expedition-level context | Age and sex exist only for members |
| "MapLibre GL JS", NASA SRTM | three.js, with SRTM tiles from Mapzen / AWS | Already built this way; offline |
| "Visual analysis" on similar groups | Now delivered through the hypotheses and page 3 | Currently only partial |
| Data sources | Adds `peaks.csv` and all-peak expeditions, on top of SRTM and OpenStreetMap | The requirements recommend multiple sources |
| Current 2025–2026 indicators | 2026 spring only | Sources cover 2026 only |

### Documents to update

| Document | Update |
|---|---|
| `README.md` (project) | Status table; remove references to proposal files and a zip that aren't in the folder |
| `everest-app/README.md` | Stale "no coordinates, schematic only" statement; new views; test counts |
| `report/outline.md` | Stale "did not use MapLibre/3D" text. **Add Part II (individual contributions, up to 5 pages each)** and the "three highlights" bullets, both required but missing. Up to 20 pages allowed for Part I. |
| `discussion_1_prep.md` | Leave as a historical record; new notes go in a discussion 2 file |
| `evaluation/` | New tasks and answer keys |
| Submission package | The requirements ask for a starting `index.html` linking all files and reports, so add one at the zip root |

---

## 10. Build order and dates

Key dates: in-class discussions on 7 and 14 November, demo on 21 or 28 November, submission on 30 November. Dates below are targets.

| Phase | Work | Target | You review |
|---|---|---|---|
| 0 | Your decisions (Section 12) | 6–7 Nov | |
| 1 | Data pipeline, shared state, design system, page 1 chart fixes | by 8 Nov | Data and first fixes |
| 2 | **Page 3:** all sections | by 10 Nov | **Checkpoint 1** |
| 3 | **Page 1:** new views | by 11 Nov | **Checkpoint 2** |
| 4 | **Page 2:** filter-linked map, new views | by 13 Nov | **Checkpoint 3** |
| 5 | Findings rail, cross-page links, self-test, documents | by 14 Nov | Ready for 14 Nov discussion |
| 6 | Six-person user test and revisions | 14–20 Nov | Results |
| 7 | Demo rehearsal, recording, report figures, package | by 21 Nov | Final check |

Page 3 goes first because that's where you asked for the most change. The proposal ranks page 2 as its top priority, so its map-chart linking is on the "won't be cut" list below, even though it's built last.

### If time runs short, cut in this order

1. Dimension reduction, clustering (already stretch goals)
2. Permit-holder edges in the operator network
3. Page 1 operator network
4. Route treemap (keep ranked bars)
5. Horizon strip on page 2 (keep the line chart)
6. Index chart on page 3 (keep the heat map)

The two hero views, map-chart linking, denominators, uncertainty and small-sample rules won't be cut.

---

## 11. Definition of done and risks

### Done means

- [ ] All page views render at 1440, 1000 and 700 px, with no console errors or network requests
- [ ] Self-test passes, including new browser-vs-Python checks for each new view
- [ ] Headline counts unchanged: 2,347 expeditions, 25,274 member records, 1,479 successes, 340 deaths
- [ ] Every rate shows numerator, denominator and n, in the chart or tooltip
- [ ] Every finding link reproduces its claim, and each hypothesis number is rechecked
- [ ] Empty and sparse states work for extreme filter and plan combinations
- [ ] Before and after screenshots captured
- [ ] Nothing pushed to GitHub without your say-so

### Risks

| Risk | Handling |
|---|---|
| Too many charts, which crowds the demo | Sections and a clear path; demo focuses on two hero views; cut list above |
| Network looks like a hairball | Edge filtering by default, matrix as an alternative, seeded layouts |
| Readers take associations as causes | Same disclaimer as today, plus "association" wording in every finding |
| Small samples look like findings (north 2020–24) | Hatching, n always visible, findings state the sample size |
| Agency names can't be cleaned reliably | Show only agencies above a threshold, document the rule, or cut the view (it's on the cut list) |
| Teammates' work is affected | Work stays on a branch, one reviewable set of changes per page. If teammates have newer copies, tell me before I start. |
| Retraining changes numbers already presented | Report explains it with before and after values |

---

## 12. Decisions I need from you

| # | Decision | Options | My recommendation |
|---|---|---|---|
| 1 | Cancelled 2014–15 seasons in the model | Retrain or keep with a warning (Section 5) | **Retrain** |
| 2 | Meaning of "model visualization tag" | My reading is "techniques taught in class" | Confirm, or tell me what the teacher said |
| 3 | Demo length | The requirements don't state it; README assumes 8 minutes | Confirm from Moodle or the teacher |
| 4 | Operator network (agencies and nations) | Include or skip. It goes beyond the proposal's listed fields, but adds a real network. | **Include**, and cut it first if time runs short |
| 5 | Commit style while I work | Leave changes uncommitted for review, or one local commit per page | **One local commit per page**, since page-by-page diffs are easier to review. Still no push. |
