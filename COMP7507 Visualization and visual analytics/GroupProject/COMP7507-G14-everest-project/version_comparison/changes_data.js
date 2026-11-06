/* What changed between the baseline (8e6b16f) and the upgraded app. Used by compare.html and both snapshots. */
window.CHANGES = [
  // ---------------------------------------------------- page 1
  { view: "history", type: "NEW", title: "Hypothesis cards", after: "#m1-findings", note: "H1–H3 state a claim, a verdict and the numbers. \"Show the evidence\" sets the charts for you." },
  { view: "history", type: "UPGRADED", title: "Annual chart is now a timeline brush", before: "#m1-annual", after: "#m1-card-annual", note: "Drag a period and every chart follows. Time axis fixed: years with no records used to be squeezed out.", beforeNote: "Period buttons only changed this one chart, and missing years were squeezed out of the axis." },
  { view: "history", type: "NEW", title: "Seasons over time", after: "#m1-card-season", note: "Stacked graph, count or share, showing which season drove growth." },
  { view: "history", type: "UPGRADED", title: "Season × decade heat map", before: "#m1-heat", after: "#m1-card-heat", note: "Stronger colour scale, values inside cells, hatching for small samples.", beforeNote: "Pale colour scale; no values in the cells." },
  { view: "history", type: "UPGRADED", title: "Summit success", before: "#m1-success", after: "#m1-card-success", note: "One colour with a clear selection, plus a year view with a 95% band.", beforeNote: "Rust bars from 2000 on had no legend or explanation." },
  { view: "history", type: "NEW", title: "Everest compared with other peaks", after: "#m1-card-peaks", note: "Horizon graph and index chart across 8 peaks, using the wider dataset. Tests H1." },
  { view: "history", type: "FIXED", title: "Duration box plots", before: "#m1-duration", after: "#m1-card-duration", note: "Proper vertical box plots, with an option to split by side.", beforeNote: "Bug: whiskers were drawn at a slant." },
  { view: "history", type: "FIXED", title: "Members and hired staff", before: "#m1-structure", after: "#m1-card-structure", note: "Real yearly bars, plus hired staff per member on its own axis.", beforeNote: "Smoothed curve invented shape between years." },
  { view: "history", type: "UPGRADED", title: "Oxygen use", before: "#m1-o2", after: "#m1-card-o2", note: "Shows single years and a second line without the 2014–15 closures, explaining the dip.", beforeNote: "Unexplained dip around 2014–15." },
  { view: "history", type: "UPGRADED", title: "Deaths with switchable denominator", before: "#m1-deaths", after: "#m1-card-deaths", note: "Count, per 1,000 members, per 1,000 hired, per 100 summiters. Tests H2.", beforeNote: "Counts with one small rate row beneath." },
  { view: "history", type: "NEW", title: "How expeditions ended", after: "#m1-card-ended", note: "Stacked graph of recorded reasons, including season closures found from the dataset's notes." },
  { view: "history", type: "NEW", title: "Nation and agency network", after: "#m1-card-net", note: "Force-directed network with filtering, ego view, degree and betweenness." },

  // ---------------------------------------------------- page 2
  { view: "routes", type: "NEW", title: "Hypothesis cards", after: "#m2-findings", note: "H4–H6 with one-click evidence." },
  { view: "routes", type: "UPGRADED", title: "Filters reach everything", before: "#m2-filters", after: "#m2-filters", note: "Filters now drive map and 3D too. New 2005–2024 period and \"Use this as my plan\".", beforeNote: "Filters changed only the KPIs and two charts." },
  { view: "routes", type: "UPGRADED", title: "South vs north", before: "#m2-compare", after: "#m2-card-compare", note: "Dumbbell small multiples with 95% intervals on rates.", beforeNote: "Six pale bars with no uncertainty." },
  { view: "routes", type: "NEW", title: "Gap through time", after: "#m2-card-gap", note: "Each side with a band, and a horizon strip showing who leads. Tests H4." },
  { view: "routes", type: "UPGRADED", title: "Route families and treemap", before: "#m2-routes", after: "#m2-card-routes", note: "Intervals on bars, plus a treemap that drills into raw route names and sets a filter.", beforeNote: "No intervals; colour wrongly implied a side for mixed families." },
  { view: "routes", type: "NEW", title: "Altitude funnel", after: "#m2-card-funnel", note: "Share of expeditions reaching each altitude. Hover to light up the profile, map and 3D. Tests H6." },
  { view: "routes", type: "UPGRADED", title: "Camp profile is linked", before: "#m2-camps", after: "#m2-card-camps", note: "Hovering links with the funnel, map and 3D view.", beforeNote: "Stood alone, linked to nothing." },
  { view: "routes", type: "UPGRADED", title: "Map and 3D follow the filters", before: "#geo-card", after: "#geo-card", note: "Route width and camp percentages show the share reaching that altitude. Contour plot added. Exaggeration note corrected to ×1.7.", beforeNote: "Ignored all filters. Footnote said ×1.9; the code uses ×1.7." },
  { view: "routes", type: "NEW", title: "Summit calendar", after: "#m2-card-calendar", note: "Heat map of day × year by side, showing the summit window." },
  { view: "routes", type: "NEW", title: "Base camp arrival", after: "#m2-card-bc", note: "Success by arrival window, which tests and rejects H5." },
  { view: "routes", type: "UPGRADED", title: "2026 layer", before: "#m2-current", after: "#m2-current", note: "Adds a yearly chart with 2026 as a hollow marker. Still separate from the data.", beforeNote: "Numbers only, with no history to compare." },

  // ---------------------------------------------------- page 3
  { view: "plan", type: "NEW", title: "Hypothesis cards", after: "#m3-findings", note: "H7, H8 and H3 with one-click evidence." },
  { view: "plan", type: "NEW", title: "Shared period and closure switch", after: "#m3-timeline-card", note: "One brush drives all page 3 views. The switch adds the 2014–15 closures back to compare." },
  { view: "plan", tab: "estimate", type: "UPGRADED", title: "Estimate and what-if ladder", before: "#m3-result", after: "#m3-result", note: "Uncertainty strip and a clickable ladder in percentage points. The reading is calculated per plan.", beforeNote: "Pale bars, a 69× odds factor people misread, and a \"conservative\" note that is wrong for the default plan." },
  { view: "plan", tab: "time", type: "NEW", title: "Your plan through time", after: "#m3-card-through", note: "Headline view. Shows 54% → 82% → 71% where the old page showed one flat number. Tests H7." },
  { view: "plan", tab: "time", type: "NEW", title: "Factor × period heat map", after: "#m3-card-grid", note: "Each factor against that period's average, on a diverging scale. Small samples are hatched." },
  { view: "plan", tab: "time", type: "NEW", title: "Index chart", after: "#m3-card-index", note: "Which groups improved fastest, with a movable reference period." },
  { view: "plan", tab: "links", type: "NEW", title: "Factor network and matrix", after: "#m3-card-net", note: "Headline view. Force layout with a fixed seed, edge filter, ego view, and an adjacency matrix toggle." },
  { view: "plan", tab: "links", type: "NEW", title: "Plan decision tree", after: "#m3-card-tree", note: "Icicle with your plan's path outlined. Click to zoom; apply a branch to the form." },
  { view: "plan", tab: "records", type: "NEW", title: "Expedition explorer", after: "#m3-card-pcp", note: "Parallel coordinates with brushing, axis ordering and a linked closest-expeditions table." },
  { view: "plan", tab: "trust", type: "UPGRADED", title: "Calibration", before: "#m3-calibration", after: "#m3-calibration", note: "Toggle between held-out and fitted data." },
  { view: "plan", tab: "trust", type: "UPGRADED", title: "Model card numbers", before: "#m3-metrics-card", after: "#m3-metrics-card", note: "Retrained without closures. Held-out accuracy is essentially unchanged.", beforeNote: "Trained with the abandoned 2014–15 expeditions included." },
  { view: "plan", tab: "trust", type: "NEW", title: "Why the closures are excluded", after: "#m3-closure-card", note: "Explains the rule, which comes from the dataset's own notes, and the effect on oxygen." },
];

window.CHANGE_NUMBERS = [
  ["Member model: oxygen factor (odds)", "about 69×", "about 22×"],
  ["Member model: fitted on", "8,872 members", "8,075 members"],
  ["Member model: base rate", "53.5%", "58.8%"],
  ["Member model: held-out Brier / log loss / AUC", "0.221 / 0.627 / 0.651", "0.220 / 0.628 / 0.651"],
  ["Expedition model: fitted on", "1,495 expeditions", "1,365 expeditions"],
  ["Expedition model: held-out Brier / log loss / AUC", "0.042 / 0.188 / 0.941", "0.044 / 0.188 / 0.942"],
  ["Default plan estimate", "74.5%", "74.6%"],
  ["60+, no oxygen estimate", "0.9%", "2.8%"],
  ["Task T5 plan (40–49, no oxygen) estimate", "about 3%", "about 10%"],
  ["Self-test checks", "23", "52"],
];
