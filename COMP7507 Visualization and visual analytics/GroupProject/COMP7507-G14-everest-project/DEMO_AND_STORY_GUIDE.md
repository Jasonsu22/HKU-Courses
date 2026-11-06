# Demo and story guide

How to tell the story of the Everest project, what to click, and what to say.

- **In-class discussion:** use [Section 7](#7-in-class-discussion-explaining-the-changes).
- **Live demo (21 or 28 Nov):** use [Sections 1 to 5](#1-the-story-in-one-minute).
- **Quick numbers:** [Section 6](#6-numbers-cheat-sheet).

> **Check first:** the requirements page gives no time limit for the demo. This script is 8 minutes because our README assumed that. Confirm with the teacher or Moodle. [Section 4](#4-if-you-have-less-time) has a 5-minute version.

---

## 1. The story in one minute

The requirement says a walkthrough, not a formal talk, and to "wisely choose one or two main visualizations". So the demo follows one question, and spends the most time on two views: **Your plan through time** and the **Factor network**.

> **The question:** Everest success rose from about 30% to about 89%. Why, for whom, and does it apply to my plan?

| Act | Page | Question | Answer the data gives |
|---|---|---|---|
| 1 | History | Did the mountain get easier? | Not simply. Some peaks didn't improve, and safety depends on how you measure it. |
| 2 | Routes | Do where and when matter? | The south-north gap isn't stable, base camp timing barely matters, and fewer expeditions stop high up. |
| 3 | Your plan | Does this apply to me? | One number hides a lot: this plan moved from 54% to 82% to 71%. Choices also cluster, and one famous factor was inflated. |

**The one sentence to remember:**

> "We didn't build charts to show that success went up. We used them to test eight explanations, and several of them turned out to be wrong or weaker than they looked."

That line matters because the rubric gives B+ and above for "mostly explorative visualizations with effective applications of visual analysis", and asks about hypothesis generation and verification.

---

## 2. Before you present

**The day before**
- [ ] Open `everest-app/index.html` on the presenting laptop by double-clicking it. It needs no internet.
- [ ] Open `everest-app/index.html?selftest=1` and confirm **52 of 52 checks passed**.
- [ ] Go to Routes and check the 3D terrain appears. If it shows a WebGL message, the map still works, so say "the 2D map shows the same data".
- [ ] Record the full run as a backup video. The requirements allow video clips.
- [ ] Rehearse with a timer at projector resolution, and check text is readable from the back. The rubric assesses this.

**Right before**
- [ ] Use Chrome at 100% zoom, with notifications off.
- [ ] Tab 1: `everest-app/index.html` (reload so it starts fresh).
- [ ] Tab 2: `everest-app/index.html?selftest=1`.
- [ ] Make sure the page is at the top, on 01 History.

**Delivery**
- Speak to the audience, not the screen, and don't read this script word for word. Learn the key numbers and say them your own way.
- Move the mouse slowly and pause after each click, because people need a moment to see what changed.
- Name the technique when you use it. The course is grading whether you can apply and justify these.

---

## 3. The 8-minute script

Speakers follow the module owners in the proposal, as a suggestion. Swap as you like.

Each step has a **Do** (what to click) and a **Say** (what to say).

### 0:00–0:40 · The question (Lin Huaizhong)

**Do:** Stay at the top of 01 History.

**Say:**
> "Everest success rose from about 30% before 1990 to about 89% today. The easy story is that the mountain got easier. We wanted to test that. So our app has three pages: did it really get easier, do route and timing matter, and what does this mean for one person's plan? Each page starts with hypotheses, and you can click to see the evidence."

### 0:40–1:40 · Was it everywhere? H1 (Wang Chenyu)

**Do:**
1. Drag across the bars of the top chart, from about 2005 to the end. Let the charts update.
2. Click **All years**.
3. On card **H1**, click **Show the evidence**. The page scrolls to the peak comparison.

**Say:**
> "This top chart is overview plus detail. Drag a period, and every chart on the page follows.
> Our first hypothesis: success rose everywhere, because of better gear and forecasting. This horizon graph compares eight peaks against their own averages. Green is above average, purple is below. Everest goes from purple to green. Lhotse does too, from 32% to 85%. But Baruntse went from 40% to 33%, on only 24 recent expeditions. So the rise is real, but it isn't universal. Better gear alone can't be the whole answer."

**Technique to name:** overview + detail, horizon graph.

### 1:40–2:20 · Is it safer? H2 (Wang Chenyu)

**Do:**
1. On card **H2**, click **Show the evidence**. It opens on **Per 100 summiters**.
2. Click **Per 1,000 members**.

**Say:**
> "Is it safer? Look at deaths per 100 summiters: before 1990 it was about 39, and now it's about 1. That looks like a huge success. Now change only the denominator. Member deaths per 1,000 members fell much less, from about 20 to about 12, and that's higher than the 2010s. Far more people reach the top, so 'per summit' flatters the trend. The same data gives a different story depending on the denominator, so we let you switch it."

**Technique to name:** data transformation.

### 2:20–3:30 · Where do they stop? H6 and H4 (Su Chuanzhou)

**Do:**
1. Click tab **02 Routes**.
2. On card **H6**, click **Show the evidence**.
3. Move the mouse slowly along the **How far up expeditions got** chart. Point at the camp profile line.
4. Scroll to **Route and terrain**, and hover along the funnel again if it's visible.
5. Click **Spring** or **All** in the Season filter and watch the percentages on the map change.
6. On card **H4**, click **Show the evidence**.

**Say:**
> "The filters now drive every view, including the terrain. This funnel shows how far expeditions got. Hover at an altitude, and it lights up in the camp profile, the map and the 3D view. That's coordinated multiple views.
> On the map, route width and the percentages show the share reaching that camp, under the current filter. The contour lines come from the same elevation data as the 3D model. The line between camps is schematic, and we label it that way.
> Fewer expeditions now stop high up: reaching 8,840 metres on the standard route went from 63% to 87% on the south, and from 44% to 91% on the north.
> Is the south side better? It led in the 1990s, 26% to 18% of members. In 2020–24 the north looks far ahead, 85% to 61%, but that's only 103 members. This band shows that uncertainty. So we'd call that gap not stable, and we wouldn't recommend a side from it."

**Technique to name:** coordinated multiple views, contour plot, horizon strip.

### 3:30–4:00 · Does timing matter? H5 (Su Chuanzhou)

**Do:** On card **H5**, click **Show the evidence**. Point at the bars, then at the **Summit calendar** beside them.

**Say:**
> "Does arriving early at base camp help? We expected yes. In spring on the standard route, success stays between 71% and 75% whichever window you arrive in. So this hypothesis wasn't supported. Meanwhile, the calendar shows summit days packed into a narrow window in mid to late May. When you summit looks far more concentrated than when you arrive."

**Technique to name:** heat map.

### 4:00–5:30 · **Main view 1: Your plan through time. H7** (Cheng Jionghao)

**Do:**
1. Click **Use this as my plan →** in the filter bar. This opens 03 Your plan.
2. Click **Reset** on the form.
3. Point at the big number and the three rows under it.
4. Click tab **Over time**.
5. Point at the pink line, the dashed model line, and the last point.
6. Change **Oxygen** to No, then back to Yes, or click rows in the heat map if time allows.

**Say:**
> "Page 2 passes its choices to page 3. Here's a default plan: 30s, male, spring, south, standard route, with oxygen. The model says 75%, with a range, next to what real members with this plan did.
> The old version of our page stopped there, with one flat number. This chart is why we changed it. The same plan's group was 54% in the early 1990s, 82% in 2010–14, and 71% most recently. So 75% is an average across very different periods, and it's actually a little high for this plan today. The page calculates that sentence for each plan.
> Hollow points and hatched cells mean too few records. If an exact plan has under 10 records, we refuse to give a number at all."

**Technique to name:** time series with interval band, heat map with a diverging scale.

### 5:30–6:45 · **Main view 2: Factor network. H8** (Cheng Jionghao)

**Do:**
1. Click tab **Connections**.
2. Hover **No oxygen** so its links stand out.
3. Click **Matrix**, then back to **Network**.
4. Drag the period on the timeline brush to about 1990–2004, then back to 2005–2024.
5. Click tab **Trust**, and point at **Why the 2014–15 closures are excluded**.

**Say:**
> "These are the connections between choices, as a force-directed network. A link means two choices occur together more often than chance, and colour shows how those people did. See this purple cluster: autumn, non-standard routes, no oxygen. Autumn with a non-standard route is about 21 times as common as chance, and none of those 45 members summited.
> The matrix shows the same data without edge clutter. We keep the layout fixed, so moving the period changes the links and not the picture. In 1990–2004 these links are much weaker, around 2 times chance. That style of climbing has since become a small, separate niche.
> Looking closer at oxygen led to our most important finding. The old model said oxygen multiplied your odds by 69. But the dataset's own notes show that 794 of the 1,295 'no oxygen' members were on expeditions abandoned in 2014 and 2015, because of the Sherpa strike, an avalanche and the earthquake. Many stopped before anyone would use oxygen. So that wasn't a fair comparison. We removed them and retrained, and the factor fell to about 22. Accuracy on held-out data barely changed."

**Technique to name:** force-directed layout, filtering, ego network, adjacency matrix.

> **Be accurate here:** the network didn't reveal the closures by itself. What pointed to them was the 'no oxygen' records clustering in 2014–15, and the notes then explained why. If asked, say that plainly.

### 6:45–7:30 · Real expeditions (Lin Huaizhong)

**Do:**
1. Click tab **Records**.
2. Drag on the **Team size** axis to select a range. Point at the count and table below.

**Say:**
> "Each line is one real expedition. Drag on any axis to filter, and the summary and the closest matches update. Pink diamonds mark this plan on the two axes it sets. So at the end, you aren't just given a probability, you can inspect the actual expeditions behind it."

**Technique to name:** parallel coordinates, brushing and linking.

### 7:30–8:00 · Can you trust it? (Qin Yuhong)

**Do:** Switch to Tab 2, showing the self-test panel.

**Say:**
> "We checked ourselves. This self-test recomputes numbers in the browser and compares them with Python: 52 checks, all passing. We also audited the dataset against the proposal. These are associations in historical records, not causes, and not a promise anyone will summit. Oxygen and hired staff are recorded during the expedition, not before it, so this describes comparable expeditions rather than forecasting yours. Thank you."

---

## 4. If you have less time

**5-minute version.** Keep these and skip the rest:

| Time | Step |
|---|---|
| 0:00–0:30 | The question |
| 0:30–1:15 | H1 peak comparison |
| 1:15–2:15 | H6 funnel, linked to the map |
| 2:15–3:30 | **H7 Your plan through time** |
| 3:30–4:30 | **Factor network and H8** |
| 4:30–5:00 | Limitations and self-test |

**If something breaks**
- **Chart looks wrong:** reload the page. Findings still set the state in one click.
- **3D fails:** use the 2D map and say so.
- **Laptop fails:** play the backup recording and narrate it.
- **Running over time:** skip Records, and go straight to the closing limitations.

---

## 5. Likely questions

| Question | Answer |
|---|---|
| Why not just give one number? | Because this plan alone ranged from 54% to 82%. A single number hides time, sample size and uncertainty. |
| Is oxygen causing success? | We can't say that. It's an association, and people who skip oxygen are self-selected. Even without closures, almost nobody without oxygen summited in these records. |
| Why remove 2014–15? Isn't that cherry-picking? | We only removed expeditions whose own notes cite the strike, an avalanche or the earthquake, and that didn't summit: 130 in total. It's a stated rule. They stay in the history charts, and page 3 has a checkbox to add them back. |
| Did retraining improve the model? | Not on held-out accuracy, which barely moved (Brier 0.221 to 0.220). It fixed an inflated coefficient, which matters when we're explaining factors. |
| Why does the model under-predict recent seasons? | It has no time term and averages 2005–2024. The calibration chart shows this, and the plan-through-time view makes it visible per plan. |
| Why not add year to the model? | A future year isn't something the training data covers, so extrapolating it would claim more than we can support. We show time separately. |
| Why a member-level estimate when the proposal says expedition? | Age and sex exist only for members. We show both levels on page 3. |
| Why three.js, not MapLibre? | It runs fully offline. The dataset has no coordinates, so terrain comes from SRTM and camps from OpenStreetMap. |
| Is the route line accurate? | No, it connects camps as a schematic, and the footnote says so. |
| Why these chart types? | Each answers a specific question. We also rejected some: spiral graphs because the season is already explicit, and Chernoff faces because they read poorly and are in bad taste with data on deaths. |
| Why is the network layout fixed? | The slides raise predictability. A fixed layout means a change in the picture is a change in the data. |
| Do well-connected agencies do better? | We show the association, but agencies differ in clients and routes, so it's not a quality ranking. |
| How do you know numbers are right? | A 28-check audit against the proposal, and a 52-check browser-vs-Python self-test. |
| What would you do next? | Run the user test, evaluate over rolling periods, and add new seasons as a separate layer. |

**Avoid saying**
- "This predicts whether you'll summit." Say "historical association" or "estimate".
- "Oxygen causes..." or "Better gear caused..." The data has no gear or forecast fields.
- "The data proves..." Say "the records suggest" or "is consistent with".
- "This agency is better." The chart shows association only.
- "COVID caused 2020." The dataset only shows 3 expeditions, so say "only 3 expeditions recorded", or cite a source.
- Any user-test results, until the sessions have really been run.

---

## 6. Numbers cheat sheet

All of these are checked by the self-test or shown in the app.

| Topic | Number |
|---|---|
| Dataset | 2,347 Everest expeditions, 25,274 member records, 1921–2024 |
| Overall success | 1,479 of 2,347 = 63.0% |
| Recorded deaths | 340 (208 members, 132 hired) |
| **H1** before 1990 → 2020–24 | Everest 30% → 89%, Lhotse 32% → 85%, Manaslu 33% → 53%, Baruntse 40% → 33% (24 recent expeditions) |
| **H2** before 1990 → 2020–24 | Deaths per 100 summiters 38.7 → 1.2. Member deaths per 1,000 members 19.6 → 11.7 (2010s: 8.6) |
| **H3** | Hired staff per member 0.60 (1990s) → 1.47 (2020–24). Mixed across support levels |
| **H4** members | 1990s: south 26%, north 18%. 2020–24: south 61%, north 85% (103 north members) |
| **H5** | Spring standard route, 2005–24: 71–75% across arrival windows |
| Summit window | Spring, half of first summits fall between May 17 and May 23 |
| **H6** before 2000 → 2016–24 | Reaching 8,840 m: south 63% → 87%, north 44% → 91% (114 recent north expeditions) |
| **H7** default plan | 54% (1990–94), 82% (2010–14), 71% (2020–24), model 75% |
| **H8** | 794 of 1,295 no-oxygen members from closures; factor about 69× → about 22× |
| Closure rule | 130 expeditions, 797 members |
| Network | Autumn + other route 21× chance, 0 of 45 summited (2005–24). Autumn + no oxygen 12×, 0 of 98 |
| Held-out member model | Brier 0.220, log loss 0.628, AUC 0.651 |
| Held-out expedition model | Brier 0.044, log loss 0.188, AUC 0.942 |

---

## 7. In-class discussion: explaining the changes

The requirements ask for 1–2 slides covering what's been done, difficulties, and what's next. They need to be submitted afterwards. Each session is about 10 minutes.

### Suggested slide 1: What we changed

- **Your feedback:** use the visualization techniques taught in class more fully, and make page 3 less plain.
- **Before:** mostly descriptive charts, separate pages, and one flat estimate.
- **Now:** one question across three pages, and eight hypotheses, each with one-click evidence.
- **Techniques added:** horizon, index, stacked and contour plots, box plots, heat maps, force-directed networks, adjacency matrix, treemap, icicle, parallel coordinates, overview + detail, linking and brushing.
- **Key finding:** abandoned 2014–15 expeditions inflated the oxygen factor to about 69×; without them it's about 22×.

### Suggested slide 2: Difficulties and next steps

- **Difficulties:** thin recent north-side data, sparse combinations, oxygen and hired staff recorded during the expedition, and messy agency names.
- **Next:** run the six-person user test, revise, rehearse, and write the report.

### What to show (about 3 minutes)

1. Open `version_comparison/compare.html` and show **page 3 side by side**. Click **Your plan through time** in the list.
2. Open the app's **Connections** tab, since connections and time variation were what we set out to add.
3. Show one finding, H8, as an example of visual analysis changing a result.

### How to explain it

> "After the last discussion, you suggested we use more of the techniques from class. We looked at each lecture and asked which technique answers a real question in our data. Page 3 now shows time variation and connections rather than a pale bar chart. We also linked all the pages, and turned our claims into hypotheses people can check. We left some techniques out on purpose, and we can explain why."

### Questions to ask the teacher

1. Is this the balance you had in mind, or do you expect more of any technique? (We read your advice as "use the techniques taught in class as much as possible", so please correct that if we misunderstood.)
2. How long is the demo, and should all five members speak?
3. Is it acceptable to exclude the 130 abandoned expeditions from the model, since we keep them visible and state the rule?
4. Is a member-level estimate acceptable, given the proposal said expedition-level? We show both.
5. Are we OK with oxygen and hired staff as plan inputs, given they're recorded during the expedition and we say so?

---

## 8. What each person should be ready to explain

| Member | Module in the proposal | Be ready to explain |
|---|---|---|
| Qin Yuhong | Data and provenance | Composite keys, the `myear` problem, the closure rule, the self-test |
| Wang Chenyu | Historical evolution | Timeline brush, horizon graph, denominators, nation and agency network |
| Su Chuanzhou | Routes and map | Filter linking, funnel, contours, treemap, why the route line is schematic |
| Cheng Jionghao | Profile estimator | Baselines, calibration, the retrain, why time isn't a model term |
| Lin Huaizhong | Integration and evaluation | User path, shared state between pages, offline packaging, user test |

Since this upgrade was built quickly, everyone should open their part of the app and rehearse it. The peer evaluation and Part II of the report are individual, so make sure each person's description matches what they actually did.
