/* Page 3 shared data: decodes the anonymous member table and holds the shared period. */
(function () {
  "use strict";

  const P = window.EVEREST_PLAN;
  const L = P.levels;
  const STEP = P.columns.length;
  const rows = [];
  for (let i = 0; i < P.tuples.length; i += STEP) {
    const t = P.tuples;
    rows.push({
      year: t[i], age: L.age[t[i + 1]], sex: L.sex[t[i + 2]], season: L.season[t[i + 3]],
      side: L.side[t[i + 4]], route: L.route[t[i + 5]], o2: t[i + 6], team: L.team[t[i + 7]],
      sup: L.support[t[i + 8]], closure: !!t[i + 9], n: t[i + 10], k: t[i + 11],
    });
  }

  const state = { range: [2005, 2024], dropClosure: true };
  const listeners = [];
  const teamKey = (t) => (t <= 8 ? "s" : t <= 20 ? "m" : "l");
  const supKey = (r) => (r < .5 ? "lt05" : r < 1 ? "05to1" : r <= 2 ? "1to2" : "gt2");

  function total(list) {
    let n = 0, k = 0;
    for (const r of list) { n += r.n; k += r.k; }
    return { n, k, rate: n ? k / n : null };
  }
  const usable = () => rows.filter((r) => !(state.dropClosure && r.closure));
  const live = () => usable().filter((r) => r.year >= state.range[0] && r.year <= state.range[1]);

  // Matching rules are the same three used by the model's comparable cohorts.
  const RULES = {
    exact: { label: "same age band, sex, season, side, route, oxygen and team-size band", fields: ["age", "sex", "season", "side", "route", "o2", "team"] },
    mid: { label: "same age band, sex, season, side and oxygen", fields: ["age", "sex", "season", "side", "o2"] },
    broad: { label: "same age band, sex, season and side", fields: ["age", "sex", "season", "side"] },
  };
  function cohortRows(p, rule, list) {
    const q = { ...p, team: teamKey(p.team) };
    const f = RULES[rule].fields;
    return (list || usable()).filter((r) => f.every((x) => r[x] === q[x]));
  }

  const PERIODS = d3.range(1990, 2021, 5).map((y) => ({ a: y, b: y + 4, mid: y + 2.5, label: `${y}–${String(y + 4).slice(2)}` }));

  // Attributes used as rows in the factor grid and as nodes in the network.
  const ATTRS = [
    { id: "South", group: "Side", label: "South side", test: (r) => r.side === "South", plan: (p) => p.side === "South" },
    { id: "North", group: "Side", label: "North side", test: (r) => r.side === "North", plan: (p) => p.side === "North" },
    { id: "Spring", group: "Season", label: "Spring", test: (r) => r.season === "Spring", plan: (p) => p.season === "Spring" },
    { id: "Autumn", group: "Season", label: "Autumn", test: (r) => r.season === "Autumn", plan: (p) => p.season === "Autumn" },
    { id: "Std", group: "Route", label: "Standard route", test: (r) => r.route === "standard", plan: (p) => p.route === "standard" },
    { id: "Other", group: "Route", label: "Other route", test: (r) => r.route === "other", plan: (p) => p.route === "other" },
    { id: "O2", group: "Oxygen", label: "Oxygen", test: (r) => r.o2 === 1, plan: (p) => p.o2 === 1 },
    { id: "NoO2", group: "Oxygen", label: "No oxygen", test: (r) => r.o2 === 0, plan: (p) => p.o2 === 0 },
    { id: "M", group: "Sex", label: "Male", test: (r) => r.sex === "M", plan: (p) => p.sex === "M" },
    { id: "F", group: "Sex", label: "Female", test: (r) => r.sex === "F", plan: (p) => p.sex === "F" },
    { id: "u30", group: "Age", label: "Under 30", test: (r) => r.age === "u30", plan: (p) => p.age === "u30" },
    { id: "30s", group: "Age", label: "30–39", test: (r) => r.age === "30s", plan: (p) => p.age === "30s" },
    { id: "40s", group: "Age", label: "40–49", test: (r) => r.age === "40s", plan: (p) => p.age === "40s" },
    { id: "50s", group: "Age", label: "50–59", test: (r) => r.age === "50s", plan: (p) => p.age === "50s" },
    { id: "60p", group: "Age", label: "60+", test: (r) => r.age === "60p", plan: (p) => p.age === "60p" },
    { id: "TeamS", group: "Team", label: "Team ≤ 8", test: (r) => r.team === "s", plan: (p) => teamKey(p.team) === "s" },
    { id: "TeamM", group: "Team", label: "Team 9–20", test: (r) => r.team === "m", plan: (p) => teamKey(p.team) === "m" },
    { id: "TeamL", group: "Team", label: "Team > 20", test: (r) => r.team === "l", plan: (p) => teamKey(p.team) === "l" },
    { id: "SupLo", group: "Support", label: "Hired < 1 per member", test: (r) => r.sup === "lt05" || r.sup === "05to1", plan: (p) => p.hired / Math.max(p.team, 1) < 1 },
    { id: "SupMid", group: "Support", label: "Hired 1–2 per member", test: (r) => r.sup === "1to2", plan: (p) => { const x = p.hired / Math.max(p.team, 1); return x >= 1 && x <= 2; } },
    { id: "SupHi", group: "Support", label: "Hired > 2 per member", test: (r) => r.sup === "gt2", plan: (p) => p.hired / Math.max(p.team, 1) > 2 },
  ];

  window.PD = {
    rows, state, total, usable, live, RULES, cohortRows, PERIODS, ATTRS, teamKey, supKey,
    onChange(fn) { listeners.push(fn); },
    setRange(range) { state.range = range; listeners.forEach((f) => f()); },
    setDropClosure(v) { state.dropClosure = v; listeners.forEach((f) => f()); },
  };
})();
