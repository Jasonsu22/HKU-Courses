# How to write the final report

A section-by-section guide for the COMP7507 Group 14 report, based on the course requirements and marking rubric. Use it with [outline.md](outline.md), which is the skeleton to fill in.

**Due 30 November:** the work ZIP, its `index.html`, and the combined report as one PDF. The critique and peer evaluation are due 5 December.

---

## 1. What you must hand in

| Item | Rule |
|---|---|
| **Report** | One PDF for the group |
| **Part I: Overall work** | At most 20 pages, not counting the title page and references |
| **Part II: Individual contributions** | At most 5 pages for each member |
| **Work product** | One ZIP with an `index.html` linking every submitted file, including the reports. The project's root `index.html` is ready; add the PDF link. |

### Part I must include

- [ ] Project title and objectives
- [ ] Group number, names and student IDs
- [ ] Highlights of the work in **exactly three** bullet points
- [ ] The visualizations you created
- [ ] Their effectiveness: how you used them to develop hypotheses and understand the data
- [ ] Different methods you tried, and why you chose what you did
- [ ] Difficulties you encountered
- [ ] Things you wanted to do but haven't, and why
- [ ] Limitations of the visualizations and tools
- [ ] References

### Part II must include, for each member

- [ ] Name
- [ ] Details of tasks completed
- [ ] Results or findings of those tasks, with images or references to Part I

---

## 2. What earns the marks

The overall grade guide is the most important thing to design around:

| Your report shows | Grade range |
|---|---|
| Pure data presentation | D or below |
| Mostly descriptive visualizations showing patterns and trends | C to B- |
| Some explorative visualizations with visual analysis | B- to B+ |
| **Mostly explorative visualizations with effective visual analysis** | **B+ and above** |

The grade also depends on quality, complexity and dimensionality of variables, and use of multiple data sources.

### Rubric rows and what "Sophisticated" needs

| Rubric row | What it asks for | How this report meets it |
|---|---|---|
| **Title and objectives** | Very clearly developed objectives; relevant title | State the one question (Section 4.1), and three things a planner can do with the tool |
| **Highlights** | Precise and concise, in three bullets | Section 4.2 has drafts |
| **Work quality** | Effective explorative use throughout the analysis workflow; effective visual cues, interactions and dashboard design | Organise results around hypotheses H1–H8. Explain encoding and interaction choices. |
| **Justifications and discussions** | Deep understanding of issues and limitations; lucid justification of each visualization | Use the pattern in Section 3; include rejected techniques and honest limits |
| **Structure and visuals** | Clear logic; all required elements present; visuals clarify ideas | Follow Section 4 and use the checklist above |
| **Mechanics** | Very few language errors; careful citations | Section 9 and Section 11 |

**The main risk:** a report that walks through each chart in turn reads as descriptive, even though the app is explorative. Write about **what you asked, what you saw and what you concluded**, and use charts as evidence.

---

## 3. The pattern for every visualization

Use these six steps for each major view, in about 100–200 words plus a figure. This one pattern covers most of what the rubric asks about.

1. **Question.** What did we need to find out?
2. **Design.** Which technique, which encodings, which interactions?
3. **Why this design.** Why does it suit this data, and what alternative did we reject?
4. **What we saw.** State the pattern with numbers and sample sizes.
5. **What it means.** Which hypothesis does this support, weaken or reject?
6. **Limit.** What can't this view tell us?

### Worked example (adapt it in your own words)

> **Is a plan's chance stable over time?** The original page showed one estimate, which implied that it was. We tested this with a time series of the observed summit share for members matching a plan, in five-year periods from 1990, drawn against all climbing members and the flat model estimate. A line suits an ordered time variable, and a 95% Wilson band keeps sample size visible, because the groups vary from 62 to 195 members. We rejected bars, which make small changes between adjacent periods harder to follow, and a year-by-year view, which had too few members per year for a single plan.
>
> For the default plan, the share rose from 54% in 1990–94 (36 of 67) to 82% in 2010–14 (91 of 111), then fell to 71% in 2020–24 (123 of 173). The model gives 75%. This rejects hypothesis H7: the estimate is an average over different periods, and for this plan it's slightly above recent experience. Because the model has no time term, the page now calculates a note comparing each plan with its 2020–24 record. The view can't separate why the share changed, since season conditions, client mix and support all moved together.

---

## 4. Part I, section by section

Page counts are suggested, and total 20. Adjust them, but keep Results as the largest section.

| Section | Pages |
|---|---|
| 4.1 Title, objectives | 0.5 |
| 4.2 Highlights | 0.25 |
| 4.3 Introduction | 0.75 |
| 4.4 Data and preparation | 2.5 |
| 4.5 Visualizations and design rationale | 5 |
| 4.6 Visual analysis results (H1–H8) | 6 |
| 4.7 Estimation method | 1.5 |
| 4.8 Evaluation | 1.5 |
| 4.9 Methods tried, difficulties, limitations, future work | 2 |
| 4.10 Conclusion | 0.5 |

References and the title page don't count towards the limit. If you add appendices, check with the teacher whether they count; plan for them to count.

### 4.1 Title and objectives

Use the proposal's title: *Everest Climbing Decision Big Data Support: History, Routes, and Profile-Based Summit-Success Estimation*.

State the question, then the objectives:

> Everest success rose from about 30% before 1990 to about 89% in 2020–24. Our objective is to help people planning an expedition understand why, for whom, and whether it applies to their plan.

Three objectives work well:
- Explain how Everest climbing changed, and test common explanations for it.
- Compare sides, routes and timing fairly, connecting the charts to the terrain.
- Give a plan-based estimate that shows its uncertainty, its behaviour over time and when evidence is insufficient.

### 4.2 Highlights (exactly three bullets)

Draft:

1. **Eight hypotheses tested visually.** Each is reproducible in one click, and several common assumptions were rejected or weakened.
2. **Coordinated views across three pages.** Temporal, network, tree and multivariate techniques are linked, so filters and brushes drive every chart, the map and the 3D terrain.
3. **Data checking that changed a result.** An audit and a rule built from the dataset's own notes removed abandoned 2014–15 expeditions, cutting an inflated oxygen factor from about 69× to about 22×, and a 53-check self-test verifies the browser against Python.

### 4.3 Introduction

- Planning Everest is several decisions under uncertainty, not one yes or no.
- Explain the gap: totals without denominators and single numbers without uncertainty can mislead planners.
- Introduce the three-part path: did it get easier, do route and timing matter, and does it apply to me?
- Give a short roadmap of the report.

Only claim things about other tools if you've actually looked at them, and cite them.

### 4.4 Data and preparation

**Sources** (the rubric rewards multiple sources, so make this clear):

| Source | Used for |
|---|---|
| Himalayan Database via Maven Analytics: `exped.csv`, `members.csv`, `peaks.csv` | All analysis, including 8 peaks for comparison |
| `himalayan_data_dictionary.csv` | Field definitions |
| SRTM 30 m elevation (Mapzen / AWS Terrain Tiles) | 2D map, contours, 3D terrain |
| OpenStreetMap (ODbL) | Camp, col and peak positions |
| Kathmandu Post and Radio Nepal, 2026 | Separate 2026 layer only, never merged |

**Key counts:** 11,425 expeditions, about 89,000 member rows, 480 peaks, 15,586 references. For Everest: 2,347 expeditions and 25,274 member records, 1921–2024. `refer.csv` wasn't used in the app, so don't list it as a source of analysis.

**Data problems you found and handled.** This is strong material, so give each its numbers:

| Problem | Evidence | What you did |
|---|---|---|
| `expid` repeats across centuries | `EVER21101` is both 1921 and 2021 | Join on peak, year and expedition ID |
| `members.myear` is unreliable | Disagrees with its expedition in 34.8% of rows, 96% before 2000 | Take the year from the expedition |
| Hired staff are only partly listed | 8,323 of 15,533 on Everest | Use expedition-level hired counts |
| 2014–15 closures distort outcomes | Notes cite the strike, an avalanche or the earthquake | Flag 130 expeditions (797 climbing members) by rule |
| 137 route names, most used rarely | Only 14 route names within a side have 5 or more expeditions | Group into route families |
| Agency names are inconsistent | For example `Asian Trekking (Climbalaya pmt)` | Strip bracketed text and take the first agency |

**Include the closure rule word for word:** year is 2014 or 2015, no summit, and `termnote` mentions earthquake, strike or avalanche. Explain that those expeditions stay in the history charts, and that page 3 has a checkbox to add them back.

### 4.5 Visualizations and design rationale

Describe the system as a whole, then the design principles. Save detailed findings for 4.6.

**Overall flow.** History → Routes → Your plan, with shared colours, shared period brushes and links between pages.

**Design principles, each tied to a lecture:**

| Principle | How to describe it | Lecture |
|---|---|---|
| Preattentive pop-out | Pink marks only the current plan or selection | Perception and colour |
| Colour by job | Fixed side colours, one sequential hue, one diverging pair with a neutral midpoint | Perception and colour |
| Colour-blind safety | Palette checked with a simulation; labels and shapes also carry meaning | Perception and colour |
| Overview + detail | Timeline brushes on pages 1 and 3 | Interaction |
| Coordinated views | Filters and altitude hover link charts, map and 3D | Interaction |
| Data transformation | Switchable death-rate denominators, indexing, counts or shares | Interaction |
| Predictable graph layout | Fixed start and tick count, so changes in the picture come from the data | Networks |
| Showing uncertainty | Intervals on rates, hatching for small samples, refusal below 10 records | Project requirement |

**Then a table of views, one row each.** Choose the six to eight most important for the full pattern in Section 3.

| Page | View | Technique | Question |
|---|---|---|---|
| 1 | Timeline | Overview + detail, brushing | Which period? |
| 1 | Seasons over time | Stacked graph | Which season drove growth? |
| 1 | Season × decade | Heat map | When did autumn fade? |
| 1 | Peak comparison | Horizon graph, index chart | Is Everest special? |
| 1 | Duration | Box plots | Is climbing faster? |
| 1 | Deaths | Data transformation | Did it get safer? |
| 1 | How expeditions ended | Stacked graph | Why do attempts fail? |
| 1 | Nations and agencies | Force layout, filtering, degree, betweenness | Who climbs with whom? |
| 2 | Six measures | Small multiples, dumbbell | How do the sides compare? |
| 2 | Gap through time | Time series, horizon strip | Is the gap stable? |
| 2 | Route families | Bars, squarified treemap | Which routes matter? |
| 2 | Altitude funnel | Step chart linked to map and 3D | Where do expeditions stop? |
| 2 | Map and terrain | Map, contour plot, 3D | Where is this on the mountain? |
| 2 | Summit calendar | Heat map | When do people summit? |
| 3 | What-if ladder | Dumbbell | Which single change matters most? |
| 3 | Plan through time | Time series with band | Is this plan stable? |
| 3 | Factor × period | Diverging heat map | When does each factor matter? |
| 3 | Group index | Index chart | Which groups improved fastest? |
| 3 | Factor network and matrix | Force layout, adjacency matrix | Which choices travel together? |
| 3 | Plan tree | Icicle | Where does this plan sit? |
| 3 | Expedition explorer | Parallel coordinates, brushing | Which real expeditions resemble this plan? |
| 3 | Calibration | Scatter plot | Can the model be trusted? |

**Show that you made choices.** Mention rejected techniques and why:

| Rejected | Reason |
|---|---|
| Spiral graph | No yearly cycle to reveal, because season is already an explicit variable |
| Chernoff faces | Hard to read accurately, and unsuitable with data on deaths |
| Scatter plot matrix | Most variables are categorical; parallel coordinates fit better |
| Dimension reduction | Mixed categorical data, and the axes would be hard for planners to read |
| Node-link, radial and hyperbolic trees | Depth is only 5 and size matters most, which an icicle shows better |
| Edge bundling | Few edges remain after filtering |
| Fisheye distortion | Reading values accurately matters here, and the slides warn distortion harms spatial judgment |

### 4.6 Visual analysis results (the heart of the report)

This section earns the top grade band. Give each hypothesis its own subsection: claim, figure, evidence, verdict, limit.

Take the numbers from [the demo guide's cheat sheet](../DEMO_AND_STORY_GUIDE.md#6-numbers-cheat-sheet). Reproduce each finding with its link, such as `everest-app/index.html?finding=H7`.

| # | Hypothesis | Verdict | Be careful to say |
|---|---|---|---|
| H1 | Success rose everywhere | Partly rejected | Baruntse's recent sample is 24 expeditions. The data has no gear or forecast fields, so don't name a cause. |
| H2 | Climbing has become much safer | Depends on the denominator | Per-summit figures improve partly because far more people summit. Note the different denominators. |
| H3 | More hired support drives success | Mixed | Both rose over time, which isn't proof of cause. Compare support levels within each period. |
| H4 | The south side is better | Not stable | 2020–24 north has only 103 members and 11 expeditions, so don't recommend a side. |
| H5 | Arriving early helps | Not supported | This describes the expeditions in the records. It doesn't show that arrival date has no effect for an individual. |
| H6 | Fewer stop high on the mountain | Supported | Compare within standard routes; recent north has 114 expeditions. |
| H7 | A plan's chance is stable | Rejected | Say which plan, and give n for each period. |
| H8 | Oxygen multiplies odds by about 69 | Overstated | About 22× is still an association among self-selected people, not an effect of oxygen. |

**Answer the proposal's question directly.** The proposal asks whether seasonal and route differences remain after comparing similar groups. Add a subsection with this evidence:

- **All periods:** south 68.2% (961 of 1,409), north 55.2% (518 of 938).
- **Before 2000:** south 52.7% (139 of 264), north 30.3% (82 of 271).
- **2000 onward:** south 71.8% (822 of 1,145), north 65.4% (436 of 667).
- **Spring 2020–24:** south 90.8% (157 of 173), north 84.6% (11 of 13), which is too few north expeditions to read as a difference.
- **Autumn:** south 38.3% (49 of 128), north 7.8% (8 of 102).
- **Conclusion:** the overall gap shrinks a lot when comparing similar periods and seasons, so much of it reflects when and how each side was climbed. Keep this as an association.

**Show how one finding led to the next.** The rubric asks for a clear line of reasoning. For example: the rise isn't universal (H1) → so look at how people climb (H3, H6) → so look at one plan over time (H7) → so ask what the model's biggest factor really means (H8).

### 4.7 Estimation method

- Two regularised logistic regressions: member (headline) and expedition (context). Age and sex exist only for members.
- Features: age band, sex, season, side, route group, team size, hired support, oxygen.
- Time split from the proposal: train 1990–2014, validate 2015–2019, test 2020–2024. Deployed coefficients refit on 2005–2024.
- 95% ranges from 300 bootstrap refits.
- Comparable cohorts at three levels, and insufficient evidence below 10 exact records.

**Results table (held-out 2020–24):**

| Model | Baseline or model | Brier | Log loss | AUC |
|---|---|---|---|---|
| Member (n = 1,809) | Constant | 0.286 | 0.766 | 0.500 |
| | Side × season | 0.253 | 0.699 | 0.476 |
| | **Logistic** | **0.220** | **0.628** | **0.651** |
| Expedition (n = 184) | Constant | 0.156 | 0.500 | 0.500 |
| | Side × season | 0.109 | 0.387 | 0.593 |
| | **Logistic** | **0.044** | **0.188** | **0.942** |

**Discuss these openly:**
- AUC 0.651 means the member model ranks only moderately well. Don't oversell it.
- The expedition AUC is high largely because oxygen use separates outcomes so strongly, and oxygen is recorded during the expedition.
- The calibration chart shows under-prediction in most bins for 2020–24, for example predicted 56% against observed 68%. Yet the default plan runs below the model, so overall calibration doesn't apply to every plan.
- Before and after the closure rule: the oxygen coefficient moved from 4.23 to 3.07, and test metrics barely changed. Explain that this fixes interpretation rather than accuracy.
- The comparable-cohort ladder for the default plan: exact 75.0% (440 of 587), same oxygen 73.4% (920 of 1,254), widest 69.8% (923 of 1,323).

**Answer the obvious objection.** The proposal promised only pre-expedition variables, but oxygen and hired staff are recorded during the expedition. State that clearly, and explain that the estimate therefore describes comparable historical expeditions and isn't a strict forecast.

### 4.8 Evaluation

**Write this only after the sessions have really happened.** Report what happened, even if it's unflattering.

- Protocol: `evaluation/README.md`, eight tasks, 30 minutes, about six external participants.
- Table: task, Y/P/N counts, median time, mean confidence.
- Two or three real quotes showing misunderstandings.
- What you changed because of the results, and what you decided not to change.
- Threats: small convenience sample, one moderator, participants may not be real climbers.

> **Important:** `evaluation/record_sheet.csv` already has P01 rows dated 2026-10-24, while the project README says no sessions have been run. Find out whether they're examples or a real session. If they're examples, delete them before starting, and don't report them as results.

If you run out of time, report fewer real sessions and say so. Never fill the table with estimates.

### 4.9 Methods tried, difficulties, limitations, future work

The requirements ask for these directly, and they carry the "Justifications and Discussions" row.

**Methods tried and why you moved on:**

| Tried first | Moved to | Why |
|---|---|---|
| Schematic route profile only | Hillshade map and 3D terrain, with the profile kept | The tutor discussion and the proposal's goal of connecting charts to terrain. *Check this against your discussion notes before writing it.* |
| MapLibre GL JS (in the proposal) | three.js with SRTM and OpenStreetMap | Fully offline operation |
| Estimate expedition success only | Member-level headline, expedition-level context | Age and sex exist only for members |
| Deploy the 1990–2014 model | Refit on 2005–2024 | Success rates shifted strongly by period |
| Fit on all expeditions | Exclude the 2014–15 closures | Abandoned expeditions inflated the oxygen effect |
| Raw route names | Route families, with a drill-down | 137 names fragment the data |
| One flat estimate and pale driver bars | Strip, what-if ladder and plan through time | Teacher feedback, and H7 and H8 showed one number misleads |
| Odds factors such as "69×" | Percentage-point changes | People can misread odds as probability |
| Descriptive charts by topic | Hypotheses with linked evidence | Rubric and teacher feedback |

**Difficulties:**
- Data quality: year mismatches, ID collisions, partly listed hired staff.
- Sparse combinations: few autumn, non-standard or oxygen-free records.
- Thin recent north-side data after 2020.
- The source has no coordinates or route geometry.
- Running entirely offline: browsers block WebGL from reading image files on a double-clicked page, which left the 3D terrain black until the texture was embedded. It's a good honest example, and it was caught by opening the page the way a user would.
- Keeping many coordinated views readable.

**Wanted to do but haven't, and why** (from the plan, and all true of the current build):
- Matrix reordering and draggable parallel-coordinate axes: the time went to core views.
- Permit-holder links in the agency network: the data dictionary doesn't define "(X pmt)", so the meaning can't be confirmed.
- Network clustering and dimension reduction: optional, with little benefit for this data.
- Rolling-origin model evaluation, and keyboard access inside charts.
- Surveyed route tracks: no verifiable open data was used for this.

**Limitations:**
- Records are observational, so everything is association, not cause.
- Oxygen and hired staff are recorded during the expedition.
- The model has no time term, and its AUC is moderate.
- The closure rule relies on notes, so it might miss or include a few expeditions wrongly.
- Agency cleaning is simple and approximate.
- People who climb without oxygen are self-selected.
- Member records aren't unique climbers.
- The dataset ends in 2024; the 2026 figures come from news reports and may not be counted the same way.
- The line between camps is schematic.
- Testing used one main browser setup, and a small user sample.

### 4.10 Conclusion

Keep it short. State the answer to the opening question, what a planner can do with the tool, and what it deliberately refuses to do. End with future work.

---

## 5. Figures

Every figure needs a number, a caption that states the finding, and a mention in the text.

- **Weak caption:** "Figure 5. Peak comparison chart."
- **Strong caption:** "Figure 5. Success rose on Everest and Lhotse but not Baruntse, so the rise isn't universal (three-year success against each peak's own average)."

**Avoid full-page screenshots** of the app in the body, since their text becomes unreadable. Crop to the chart you're discussing, and keep at most one overview image per page of the app.

**How to capture:** open the link, click the finding, then take a browser screenshot of the card. On a Mac, press Cmd+Shift+4, then Space, then click the window. Use a wide window at 100% zoom, or 200% for sharper images.

| Figure | Link (from `everest-app/index.html`) | Shows |
|---|---|---|
| System overview | Plain page, History tab | Overall layout |
| Timeline brush | `?from=2005&to=2024` | Linked charts |
| Peak comparison | `?finding=H1` | H1 |
| Deaths by denominator | `?finding=H2` | H2 (capture two states) |
| Support structure | `?finding=H3` | H3 |
| Agency network | History tab, last card | Network with metrics |
| Gap through time | `?finding=H4` | H4 |
| Base camp arrival and calendar | `?finding=H5` | H5 |
| Funnel | `?finding=H6` | H6 |
| Map and 3D | Routes tab, "Route and terrain" | Coordinated views |
| Estimate and ladder | `?tab=estimate#plan` | Estimate |
| Plan through time | `?finding=H7` | H7 |
| Factor heat map | `?tab=time#plan` | H3 |
| Factor network and matrix | `?tab=links#plan` | Connections |
| Closure explanation | `?finding=H8` | H8 |
| Parallel coordinates | `?tab=records#plan` | Comparable expeditions |
| Calibration | `?tab=trust#plan` | Model trust |
| Before and after | `../version_comparison/screens/` | Design change |
| Data audit | `../proposal_check/figs/` | Data quality |

---

## 6. Part II: individual contributions

Each member writes their own, up to 5 pages. Use this structure:

```text
Name and student ID

1. My role (2–3 sentences)

2. Tasks I completed
   - Task: what I did, and which files or views it covers
   - Decision: an option I chose, and why

3. Results and findings
   - What my work showed, with figures or Part I references
   - A problem I hit, and how I solved it

4. What I'd do differently (optional, 2–3 sentences)
```

**Starting points from the proposal's division of work** (each person must replace this with what they actually did):

| Member | Proposed role |
|---|---|
| Qin Yuhong | Data and provenance: cleaning, keys, cohorts, dictionary |
| Wang Chenyu | Historical evolution: trends, season comparisons, interval charts |
| Su Chuanzhou | Route and map explorer: waypoints, 2D and 3D, route comparison |
| Cheng Jionghao | Profile estimator: baselines, model, explanation charts |
| Lin Huaizhong | Integration and evaluation: linking modules, user tests, packaging |

Up to 15% of marks may be moderated by peer evaluation, so each description should match what teammates would say.

---

## 7. Be open about AI assistance

Much of this code and these documents was produced with an AI coding assistant, including this upgrade. Handle that carefully:

- **Check the rules first.** The requirements warn that plagiarism risks losing all project marks and tell you to read the policies on Moodle. Look for the course's AI rules, and ask the teacher if they're unclear. Your labs used AI-assisted coding, but that doesn't by itself settle what's allowed in the report.
- **Declare it.** Say which parts used AI and how the group checked the results. A short statement in Part I and accurate wording in Part II is usually the safest approach, unless the course asks for something else.
- **Make sure you understand it.** Each member should be able to explain their views and the numbers in their section, because the demo and report will test that.
- **Write in your own words.** Don't paste the drafts and examples in this guide or the demo guide unchanged. Treat them as notes.

---

## 8. Writing rules

| Instead of | Write |
|---|---|
| "Oxygen increases success" | "Oxygen use is strongly associated with summiting" |
| "This predicts your chance" | "Comparable members historically reached the summit at..." |
| "The data proves" | "The records suggest" or "are consistent with" |
| "Better gear caused the rise" | "The data has no gear fields, so we can't test this directly" |
| "Success is much higher" | "Success rose from 29% (41 of 141) to 89% (168 of 189)" |
| "The chart shows many things" | State the one pattern that matters |
| "As you can see" | State what the reader should see |

**Rates.** Give the numerator and denominator at least the first time, and mention sample size when it's small.

**Terms.** Use these the same way throughout:
- **Expedition success:** at least one climber reached the summit on route 1.
- **Member success:** that member reached the summit.
- **Member records:** participation rows, not unique climbers.
- **Closures:** expeditions flagged by the rule in Section 4.4.
- **Side:** host country (Nepal is south, China is north).

**Numbers.** Take them from the app or the cheat sheet, not from memory, and not from older documents such as `discussion_1_prep.md`, whose model and project status are out of date.

---

## 9. References

Use one citation style throughout, such as APA or IEEE. **Check each entry against its source before submitting, including page numbers and DOIs.** Include access dates for websites.

**Data**
- The Himalayan Database: The expedition archives of Elizabeth Hawley. https://www.himalayandatabase.com/
- Maven Analytics. Himalayan Expeditions [Data set]. https://mavenanalytics.io/data-playground/himalayan-expeditions
- Mapzen / AWS Open Data. Terrain Tiles. https://registry.opendata.aws/terrain-tiles/
- NASA. Shuttle Radar Topography Mission (SRTM), as cited in the proposal.
- OpenStreetMap contributors (ODbL). https://www.openstreetmap.org/
- The Kathmandu Post (2026, May 29) and Radio Nepal (2026, June 10), as cited in the proposal.

**Tools:** D3 (d3js.org) and three.js (threejs.org).

**Methods and visualization** (the first group appears in the course slides; the second is commonly cited for techniques you used, so read before citing):

*From the slides:*
- Shneiderman, B. (1996). The eyes have it: A task by data type taxonomy for information visualizations. *IEEE Symposium on Visual Languages*.
- Keim, D. (2002). Information visualization and visual data mining. *IEEE TVCG*, 8(1).
- Cockburn, A., Karlson, A., & Bederson, B. A review of overview+detail, zooming, and focus+context interfaces. *ACM Computing Surveys*.
- Ware, C. (2013). *Information Visualization: Perception for Design* (3rd ed.).
- Fruchterman, T., & Reingold, E. (1991). Graph drawing by force-directed placement. *Software: Practice and Experience*, 21(11).
- Brandes, U. (2001). A faster algorithm for betweenness centrality. *Journal of Mathematical Sociology*.
- Andrienko, N., et al. (2020). *Visual Analytics for Data Scientists*.

*Also worth finding:*
- Heer, J., Bostock, M., & Ogievetsky, V. (2010). A tour through the visualization zoo. *Communications of the ACM*.
- Heer, J., Kong, N., & Agrawala, M. (2009). Sizing the horizon. *CHI*.
- Bruls, M., Huizing, K., & van Wijk, J. (2000). Squarified treemaps. *EuroVis (VisSym)*.
- Inselberg, A. (1985). The plane with parallel coordinates. *The Visual Computer*.
- Wilson, E. B. (1927). Probable inference, the law of succession, and statistical inference. *JASA*.
- Brier, G. W. (1950). Verification of forecasts expressed in terms of probability. *Monthly Weather Review*.

---

## 10. Who does what, and when

Dates are suggestions, working back from 30 November.

| By | Task | Owner |
|---|---|---|
| 8 Nov | Agree the outline, section owners and citation style. Check AI rules. | All |
| 14 Nov | Capture figures; draft data (4.4) and design (4.5) | Qin, Wang, Su |
| 16 Nov | Draft results H1–H6 | Wang, Su |
| 16 Nov | Draft results H7–H8 and method (4.7) | Cheng |
| 20 Nov | Run user tests | Lin |
| 23 Nov | Draft evaluation (4.8), and discussion (4.9) | Lin, all |
| 25 Nov | Part II drafts | Each member |
| 26 Nov | Full read-through, and apply demo feedback | All |
| 28 Nov | Edit for one voice; check every number and reference | One editor, one checker |
| 29 Nov | Package the ZIP and test `index.html` on another computer | Lin |
| 30 Nov | **Submit** | |
| 5 Dec | Critique and peer evaluation | Each member |

Your demo is on 21 or 28 November. If it's the 21st, the draft results will double as demo preparation.

---

## 11. Final checks before submitting

**Requirements**
- [ ] Part I is at most 20 pages, and each Part II at most 5
- [ ] Everything in Section 1's checklists is present
- [ ] Exactly three highlight bullets
- [ ] One single PDF

**Analysis**
- [ ] Results are organised around questions, not a tour of charts
- [ ] Each hypothesis has a figure, numbers, a verdict and a limit
- [ ] The proposal's question about similar groups is answered directly
- [ ] Rejected methods and techniques are justified

**Accuracy**
- [ ] Every number was checked against the app or cheat sheet by someone other than its writer
- [ ] `?selftest=1` passes
- [ ] No cause-and-effect wording
- [ ] Evaluation contains only real sessions
- [ ] AI use follows course rules and is declared

**Presentation**
- [ ] Figures are readable in print, and have captions stating a finding
- [ ] Every figure is mentioned in the text
- [ ] Spelling, grammar and terms are consistent
- [ ] Every reference is cited, and every citation is listed

**Package**
- [ ] Root `index.html` links to the report PDF, and the "add the link" note is removed
- [ ] ZIP opened on another computer by double-clicking, with 3D terrain showing
- [ ] Decide whether to include `version_comparison/`, and whether the file size is acceptable
- [ ] Nothing depends on a local path or a server
