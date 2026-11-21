# Demo and story guide

How to tell the story of the Everest project, what to click, and what to say.

- **In-class discussion:** use [Section 7](#7-in-class-discussion-explaining-the-changes).
- **Live demo (21 or 28 Nov):** use [Sections 1 to 5](#1-the-story-in-one-minute).
- **Quick numbers:** [Section 6](#6-numbers-cheat-sheet).

> **Check first:** the requirements page gives no time limit for the demo. This script is 8 minutes because our README assumed that. Confirm with the teacher or Moodle. [Section 4](#4-if-you-have-less-time) has a 5-minute version.

---

## 1. The story in one minute

The requirement says a walkthrough, not a formal talk, and to "wisely choose one or two main visualizations". The demo follows the original decision-support story rather than turning the event layer into a separate topic: **understand the historical context → compare the route and timing choices → evaluate a particular plan**.

> **The question:** Everest planning is not one go / no-go decision. How can historical evidence help us compare side, season, route, support and oxygen without overclaiming what the records prove?

| Act | Page | Story job | Evidence |
|---|---|---|---|
| 1 | History | Supporting role: establish the background a planner needs. | Scale, seasons, success, support, oxygen and risk have changed. Historical events explain interruptions in particular seasons; they are context, not a separate causal story. |
| 2 | Routes | **Core module:** use that background to compare actual choices. | Filter side, season, period and route group; compare the sides like for like, inspect where expeditions stop, and connect the evidence to the terrain. |
| 3 | Your plan | **Core module:** turn the choices into a bounded historical estimate. | Show comparable records, uncertainty and change through time. The 2014–15 background returns only where it helps explain a model limitation. |

**The role of the new event content:** it strengthens the historical background. It helps viewers understand why individual seasons look different and why cancelled expeditions should not be treated as ordinary no-oxygen attempts. It does not replace the decision-support path.

**The one sentence to remember:**

> "We turn historical records into a planning path: understand the context, compare the choices, then inspect what comparable plans achieved—with uncertainty and limitations."

The hypotheses remain useful evidence inside this path, but they are not a list of eight separate presentations.

---

## 2. Before you present

**The day before**
- [ ] Open `everest-app/index.html` on the presenting laptop by double-clicking it. It needs no internet.
- [ ] Open `everest-app/index.html?selftest=1` and confirm **59 of 59 checks passed**.
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

Speakers follow the module owners in the proposal, as a suggestion. Swap as you like. Keep the original planner's path visible: **background → route choices → a particular plan**. The hypotheses support that path; they are not separate presentations.

Each step has a **Do** (what to click) and a **Say** (what to say). Expand **Further historical analysis** or **Questions and evidence** when you need a hypothesis card. Event and finding links open their target disclosure section automatically.

### 0:00–0:40 · The planning problem (Lin Huaizhong)

**Do:** Stay at the top of 01 History with **All years** selected.

**Say:**
> "Everest planning is usually framed as one decision: go or do not go. The historical records instead let us explore several choices: which side, which season, which route, and how much support and oxygen. Our app follows that planning path. First we establish the historical background, then compare routes under comparable conditions, and finally ask what happened to historical plans resembling ours—always with sample sizes, uncertainty and limitations."

### 0:40–1:25 · Historical background for a planner (Wang Chenyu)

**Do:**
1. Drag across the top chart from about 2005 to the end, then click **All years**.
2. On card **H1**, click **Show the evidence**.

**Say:**
> "Before comparing choices, we need to understand the historical baseline. Expedition success rose from about 30% before 1990 to about 89% recently, while support and oxygen also changed. But the rise is not universal across peaks: Lhotse improved from 32% to 85%, whereas Baruntse went from 40% to 33% on only 24 recent expeditions. So history is not one simple trend that can be applied uncritically to every plan."

**Technique to name:** overview + detail, horizon graph.

### 1:25–2:00 · Events as one part of the background (Wang Chenyu)

**Do:**
1. Scroll to **Events and turning points**.
2. Select **2014**, point to the three fixed windows, then select **2015**.
3. Click **See how expeditions ended** and point to **Season closure**.

**Say:**
> "One part of that background is the events behind unusual seasons. In 2014, 11 of 68 expeditions had a summit, compared with 206 of 282 in the previous three years. In 2015, none of 81 did. The cards link these records to the avalanche, strike and earthquake, and the black segments show the closures in our data. These comparisons help a viewer read particular seasons; they do not attempt to prove what caused the long-term rise."

**Technique to name:** event annotation, fixed-window comparison, coordinated views.

### 2:00–2:25 · Reading risk before comparing plans (Wang Chenyu)

**Do:**
1. Return to card **H2** and click **Show the evidence**. This restores all years and opens **Per 100 summiters**.
2. Click **Per 1,000 members**.

**Say:**
> "The historical background also includes risk, but its meaning depends on the denominator. Deaths per 100 summiters fell from about 39 to about 1, while member deaths per 1,000 members fell only from about 20 to about 12. Before using history in a plan, we need to know not just the trend, but exactly what each rate measures."

**Technique to name:** data transformation.

### 2:25–3:35 · Compare the route choices (Su Chuanzhou)

**Transition:** "With that context in place, we can now compare the actual choices: side, season and route."

**Do:**
1. Click tab **02 Routes**, then **H6 → Show the evidence**.
2. Move slowly along **How far up expeditions got**; point to the linked camp profile, map and 3D terrain.
3. Change the season filter and watch the camp percentages.
4. On card **H4**, click **Show the evidence**.

**Say:**
> "This is the first core module: comparing the choices. One set of filters recomputes every view, including the terrain. Hovering an altitude links the funnel, camp profile, map and 3D view, so we can connect outcomes to the route rather than reading a table alone.
> Fewer expeditions now stop high on the standard routes: reaching 8,840 metres went from 63% to 87% on the south, and from 44% to 91% on the north. But we should not turn a small recent north-side sample into a recommendation. The intervals and sample sizes stay visible precisely because this is a planning comparison, not a league table."

**Technique to name:** coordinated multiple views, contour plot, horizon strip.

### 3:35–3:55 · Add the timing choice (Su Chuanzhou)

**Do:** On card **H5**, click **Show the evidence**. Point to the bars and the **Summit calendar**.

**Say:**
> "Timing is another choice in the plan. Arriving early at base camp shows little difference: success stays between 71% and 75% across arrival windows. But summit days cluster tightly in mid to late May. The comparison separates what a planner can choose from the environmental window visible in past records."

**Technique to name:** heat map.

### 3:55–5:15 · **Turn the choices into a plan. H7** (Cheng Jionghao)

**Transition:** "We have compared the choices. What would a combination of them have meant for people like us?"

**Do:**
1. Click **Use this as my plan →**, then **Reset** the form.
2. Point to the estimate and the observed comparable group.
3. Open **Over time**; point to the observed line, model line and recent period.

**Say:**
> "Here is a default plan: 30s, male, spring, south, standard route, with oxygen. The model gives about 75%, next to what comparable historical members actually did. This is the point where the background and route comparison become a particular planning scenario.
> But one number is not enough. The same plan's group moved from 54% in 1990–94 to 82% in 2010–14, then 71% in 2020–24. The estimate averages across different periods and is slightly high for the most recent one. Sparse evidence is marked, and an exact plan with fewer than ten records returns insufficient evidence instead of a confident number."

**Technique to name:** time series with interval band, heat map with a diverging scale.

### 5:15–6:30 · **Understand the choices and the model's limits. H8** (Cheng Jionghao)

**Do:**
1. Open **Connections**, hover **No oxygen**, then toggle **Matrix** and back.
2. Move the period between about 1990–2004 and 2005–2024.
3. Open **Trust** and point to **Why the 2014–15 closures are excluded**.

**Say:**
> "The network shows which planning choices occur together more often than chance. Autumn, non-standard routes and no oxygen form one distinct cluster; the matrix provides the same evidence without edge clutter.
> The historical events return here only because they affect interpretation. Of 1,295 no-oxygen members, 794 belonged to expeditions abandoned in 2014–15; many stopped before oxygen would have been used. Treating them as ordinary no-oxygen attempts inflated the apparent oxygen factor to about 69 times the odds. After excluding those closures, it is about 22, while held-out accuracy barely changes. Historical context therefore helps us avoid misreading one of the plan inputs."

**Technique to name:** force-directed layout, filtering, ego network, adjacency matrix.

> **Be accurate here:** the network didn't reveal the closures by itself. The no-oxygen records clustered in 2014–15, and the expedition notes explained why. The event view supplies background, not causal proof.

### 6:30–7:20 · Inspect the records behind the plan (Lin Huaizhong)

**Transition:** "After the estimate and its caveats, we return to the actual historical cases."

**Do:**
1. Open **Records**.
2. Brush the **Team size** axis; point to the count and closest-matches table.

**Say:**
> "Each line is one real expedition. Brushing an axis filters the records and updates the closest matches, while pink diamonds locate our plan. The user does not have to trust a black-box probability: they can inspect the historical cases behind it and judge whether the comparison is meaningful."

**Technique to name:** parallel coordinates, brushing and linking.

### 7:20–8:00 · Close the planning path (Qin Yuhong)

**Do:** Switch to the self-test tab, then return to **Data & methods** if time allows.

**Say:**
> "Our story is therefore the original planning path: understand the historical background, compare route and timing choices, and examine a particular plan through comparable records and an uncertainty-aware estimate. The events strengthen the background; they do not turn the tool into a causal explanation. We checked the numbers with 59 browser-versus-Python tests and a 28-check data audit. The tool exposes evidence and its limits—it does not make the climbing decision for you."

---

## 4. If you have less time

**5-minute version.** Keep the same planning path and compress each step:

| Time | Step |
|---|---|
| 0:00–0:30 | The planning problem: side, season, route, support and oxygen |
| 0:30–1:10 | Historical background; use the 2014–15 events as one example |
| 1:10–2:10 | **Routes:** compare choices and link the funnel to the map |
| 2:10–3:25 | **Your plan:** estimate plus change through time |
| 3:25–4:20 | Choices network; use the closure background to explain H8 |
| 4:20–5:00 | Comparable records, limitations and self-test |

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
| How do you know numbers are right? | A 28-check audit against the proposal, and a 59-check browser-vs-Python self-test. |
| What would you do next? | Run the user test, evaluate over rolling periods, and add new seasons as a separate layer. |

**Avoid saying**
- "This predicts whether you'll summit." Say "historical association" or "estimate".
- "Oxygen causes..." or "Better gear caused..." The data has no gear or forecast fields.
- "The data proves..." Say "the records suggest" or "is consistent with".
- "This agency is better." The chart shows association only.
- "The event caused the whole change." The event cards provide cited context and descriptive windows, not causal estimates.
- "2020 had a low success rate." Only 3 expeditions were recorded and all 3 had a summit; the clear change is scale, and the sample is too small for a success-rate conclusion.
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
| **Events** | 2014: 11/68 with a summit; 2015: 0/81; 2016–18: 220/263. 2020: only 3 expeditions, 3/3 with a summit |
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
- **Now:** the original History → Routes → Your plan decision path is linked throughout, with one-click evidence for its claims.
- **Historical background:** the event explorer explains unusual seasons such as 2014–15 without presenting events as causes of every long-term change.
- **Techniques added:** horizon, index, stacked and contour plots, box plots, heat maps, force-directed networks, adjacency matrix, treemap, icicle, parallel coordinates, overview + detail, linking and brushing.
- **Key finding:** the historical closure background also matters to the model: abandoned 2014–15 expeditions inflated the oxygen factor to about 69×; without them it's about 22×.

### Suggested slide 2: Difficulties and next steps

- **Difficulties:** thin recent north-side data, sparse combinations, oxygen and hired staff recorded during the expedition, and messy agency names.
- **Next:** run the six-person user test, revise, rehearse, and write the report.

### What to show (about 3 minutes)

1. Open History and select **2014** in **Events and turning points** to show the new historical background in its intended role.
2. Open `version_comparison/compare.html` and show **page 3 side by side**. Click **Your plan through time**.
3. Open the app's **Connections** tab and use H8 to show how the closure background changes interpretation of a plan input.

### How to explain it

> "We kept our original decision-support story: historical background, route comparison, and a particular plan. After your feedback, we added more of the visualization techniques from class where they answer a real planning question. The new event explorer strengthens the historical background rather than becoming a separate story. It also helps explain why cancelled 2014–15 expeditions should not be treated as ordinary no-oxygen attempts in the model."

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
| Wang Chenyu | Historical evolution | Timeline brush, event background and fixed windows, horizon graph, denominators, nation and agency network |
| Su Chuanzhou | Routes and map | Filter linking, funnel, contours, treemap, why the route line is schematic |
| Cheng Jionghao | Profile estimator | Baselines, calibration, the retrain, why time isn't a model term |
| Lin Huaizhong | Integration and evaluation | User path, shared state between pages, offline packaging, user test |

Since this upgrade was built quickly, everyone should open their part of the app and rehearse it. The peer evaluation and Part II of the report are individual, so make sure each person's description matches what they actually did.
