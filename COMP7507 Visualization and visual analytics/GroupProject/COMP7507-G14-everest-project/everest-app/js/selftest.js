/* Browser-vs-Python self test: ?selftest=1 */
(function () {
  "use strict";

  const D = window.EVEREST_DATA;
  const M = window.EVEREST_MODEL;
  const { fmt } = U;

  const TOL = 0.002;

  function run() {
    const checks = [];
    const add = (area, name, pass, detail) => checks.push({ area, name, pass, detail });

    // ---- headline counts -------------------------------------------------
    const succ = D.expeditions.filter((r) => r.success).length;
    const deaths = d3.sum(D.expeditions, (r) => r.mDeaths + r.hDeaths);
    add("counts", "2,347 expeditions in the payload", D.expeditions.length === 2347,
      `${fmt.int(D.expeditions.length)}`);
    add("counts", "1,479 successful expeditions", succ === 1479, `${fmt.int(succ)}`);
    add("counts", "340 recorded deaths", deaths === 340, `${fmt.int(deaths)}`);
    add("counts", "yearly rows sum to 2,347", d3.sum(D.yearly, (d) => d.n) === 2347,
      `${fmt.int(d3.sum(D.yearly, (d) => d.n))}`);
    add("counts", "season×decade cells sum to 2,347",
      d3.sum(D.seasonDecade, (d) => d.n) === 2347,
      `${fmt.int(d3.sum(D.seasonDecade, (d) => d.n))}`);
    add("counts", "south + north = 2,347",
      d3.sum(D.expeditions, (r) => (r.side === "South" ? 1 : 0)) +
      d3.sum(D.expeditions, (r) => (r.side === "North" ? 1 : 0)) === 2347,
      `${fmt.int(d3.sum(D.expeditions, (r) => (r.side === "South" ? 1 : 0)))} + ${fmt.int(d3.sum(D.expeditions, (r) => (r.side === "North" ? 1 : 0)))}`);
    add("counts", "25,274 Everest member rows", D.meta.counts.member_rows === 25274,
      `${fmt.int(D.meta.counts.member_rows)}`);

    // ---- model predictions vs Python --------------------------------------
    M.selftest.profiles.forEach((t) => {
      const pm = window.M3._test.member(t.profile);
      const pe = window.M3._test.expedition(t.profile);
      add("model", `${t.name}: member ${fmt.pct(t.member, 2)}`,
        Math.abs(pm - t.member) <= TOL, `browser ${fmt.pct(pm, 2)}`);
      add("model", `${t.name}: expedition ${fmt.pct(t.expedition, 2)}`,
        Math.abs(pe - t.expedition) <= TOL, `browser ${fmt.pct(pe, 2)}`);

      if (t.memberCell) {
        const cell = window.M3._test.cohort(t.profile);
        add("cohort", `${t.name}: member cell n=${fmt.int(t.memberCell.n)}`,
          cell.n === t.memberCell.n && cell.k === t.memberCell.k,
          `browser n=${fmt.int(cell.n)}, k=${fmt.int(cell.k)}`);
      }
      if (t.expeditionCell) {
        const cell = window.M3._test.expCohort(t.profile);
        add("cohort", `${t.name}: expedition cell n=${fmt.int(t.expeditionCell.n)}`,
          cell.n === t.expeditionCell.n && cell.k === t.expeditionCell.k,
          `browser n=${fmt.int(cell.n)}, k=${fmt.int(cell.k)}`);
      }
    });

    // ---- camps ------------------------------------------------------------
    const southSummit = D.camps.south.find((c) => c.label === "Smt");
    const northSummit = D.camps.north.find((c) => c.label === "Smt");
    add("camps", "summit elevation = 8,849 m on both sides",
      southSummit.elev === 8849 && northSummit.elev === 8849,
      `${southSummit.elev} / ${northSummit.elev}`);
    add("camps", "south camps ascend monotonically",
      D.camps.south.every((c, i, a) => i === 0 || c.elev >= a[i - 1].elev),
      D.camps.south.map((c) => fmt.int(c.elev)).join(" → "));

    add("terrain", "3D texture is embedded, so it loads from a double-clicked file",
      typeof window.TERRAIN_TEXTURE === "string" && window.TERRAIN_TEXTURE.startsWith("data:image/"),
      window.TERRAIN_TEXTURE ? `${fmt.int(window.TERRAIN_TEXTURE.length)} characters` : "missing");

    // ---- new views: browser recomputes from rows; expected values come from Python ----
    const E = window.EVEREST_PLAN.expect;
    const PD = window.PD;
    const same = (a, b) => a.n === b.n && a.k === b.k;
    const ks = (o) => `${fmt.int(o.k)} of ${fmt.int(o.n)}`;
    const allRows = PD.total(PD.rows);
    add("plan data", `member table = ${fmt.int(E.tuples.rows)} rows`, allRows.n === E.tuples.rows && allRows.k === E.tuples.k, ks(allRows));
    add("plan data", `closure members = ${fmt.int(E.tuples.closure)}`, PD.total(PD.rows.filter((r) => r.closure)).n === E.tuples.closure, fmt.int(PD.total(PD.rows.filter((r) => r.closure)).n));
    add("plan data", `closure expeditions = ${fmt.int(E.closureExpeditions)}`, D.expeditions.filter((r) => r.closure).length === E.closureExpeditions, fmt.int(D.expeditions.filter((r) => r.closure).length));
    add("plan data", "model refit: oxygen coefficient recorded", M.meta.closureEffect.o2CoefWith > M.meta.closureEffect.o2CoefWithout, `${M.meta.closureEffect.o2CoefWith} → ${M.meta.closureEffect.o2CoefWithout}`);

    const def = { age: "30s", sex: "M", season: "Spring", side: "South", route: "standard", team: 12, hired: 20, o2: 1 };
    const live = PD.rows.filter((r) => !r.closure);
    Object.entries(E.defaultByPeriod).forEach(([y, want]) => {
      const got = PD.total(PD.cohortRows(def, "exact", live).filter((r) => r.year >= +y && r.year <= +y + 4));
      add("through time", `default plan ${y}–${+y + 4}: ${ks(want)}`, same(got, want), ks(got));
    });
    ["South", "North"].forEach((side) => {
      const got = PD.total(live.filter((r) => r.side === side && r.year >= 2020));
      add("findings", `H4 ${side} members 2020–24: ${ks(E.members2024[side])}`, same(got, E.members2024[side]), ks(got));
    });
    const noO2 = PD.rows.filter((r) => r.o2 === 0 && r.year >= 2005);
    const noT = PD.total(noO2);
    add("findings", `H8 no-oxygen members: ${fmt.int(E.noOxygen.members)}, ${fmt.int(E.noOxygen.closure)} from closures`,
      noT.n === E.noOxygen.members && PD.total(noO2.filter((r) => r.closure)).n === E.noOxygen.closure,
      `${fmt.int(noT.n)}, ${fmt.int(PD.total(noO2.filter((r) => r.closure)).n)}`);

    const ev = (a, b) => D.expeditions.filter((r) => r.year >= a && r.year <= b);
    const risk = (a, b, want, name) => {
      const x = ev(a, b);
      const got = { m: d3.sum(x, (r) => r.mDeaths), h: d3.sum(x, (r) => r.hDeaths), mem: d3.sum(x, (r) => r.members), hir: d3.sum(x, (r) => r.hired), s: d3.sum(x, (r) => r.summits + r.summitsHired) };
      add("findings", `H2 risk totals, ${name}`, got.m === want.mDeaths && got.h === want.hDeaths && got.mem === want.members && got.hir === want.hired && got.s === want.summits,
        `${got.m}+${got.h} deaths, ${fmt.int(got.s)} summiters`);
    };
    risk(1900, 1989, E.risk.early, "before 1990");
    risk(2010, 2019, E.risk.tens, "2010s");
    risk(2020, 2024, E.risk.late, "2020–24");

    const peak = (id) => window.EVEREST_PLAN.peaks.find((p) => p.id === id);
    ["EVER", "LHOT", "BARU", "MANA"].forEach((id) => {
      const sum = (a, b) => {
        const y = peak(id).years.filter(([yr]) => yr >= a && yr <= b);
        return { n: d3.sum(y, (d) => d[1]), k: d3.sum(y, (d) => d[2]) };
      };
      const got = sum(2020, 2024);
      add("findings", `H1 ${peak(id).name} 2020–24: ${ks(E.peaks[id].late)}`, same(got, E.peaks[id].late), ks(got));
    });

    const std = (side, a, b) => ev(a, b).filter((r) => r.side === side && r.standard && r.hp);
    [["southEarly", "South", 1900, 1999], ["southLate", "South", 2016, 2024], ["northEarly", "North", 1900, 1999], ["northLate", "North", 2016, 2024]].forEach(([key, side, a, b]) => {
      const x = std(side, a, b);
      const got = { n: x.length, k: x.filter((r) => r.hp >= 8840).length };
      add("findings", `H6 ${key} reach 8,840 m: ${ks(E.reach[key])}`, same(got, E.reach[key]), ks(got));
    });
    E.bcWindows.forEach((w) => {
      const x = ev(2005, 2024).filter((r) => r.season === "Spring" && r.standard && r.bc && r.bc >= w.lo && r.bc <= w.hi);
      const got = { n: x.length, k: x.filter((r) => r.success).length };
      add("findings", `H5 base camp day ${w.lo}–${w.hi}: ${ks(w)}`, same(got, w), ks(got));
    });

    const events = window.EVEREST_EVENTS || [];
    add("events", "five chronological events with sources and comparison windows",
      events.length === 5 && events.every((e, i) => e.source && e.source.url && e.windows.length === 3 && (!i || e.year >= events[i - 1].year)),
      events.map((e) => e.label).join(" · "));
    events.forEach((event) => {
      const got = event.windows.map((w) => window.HistoryEvents._test.summary(w.range));
      const want = E.events[event.id] || [];
      const pass = got.length === want.length && got.every((s, i) => s.n === want[i].n && s.k === want[i].k && s.members === want[i].members && s.hired === want[i].hired);
      add("events", `${event.label} ${event.title}: all three windows match Python`, pass,
        got.map((s, i) => `${event.windows[i].label}: ${ks(s)}`).join(" · "));
    });

    render(checks);
  }

  function render(checks) {
    const pass = checks.filter((c) => c.pass).length;
    const all = checks.length;
    d3.selectAll(".selftest").remove();
    const panel = d3.select("body").append("div").attr("class", "selftest");
    panel.append("div").attr("class", "selftest-card").html(`
      <div class="selftest-head">
        <div>
          <div class="selftest-kicker">browser ↔ python self-test</div>
          <h2>${pass === all ? `${all} of ${all} checks passed` : `${pass} of ${all} checks passed — see failures`}</h2>
          <p>Rows are recomputed in the browser from <code>data/everest_data.js</code>,
          <code>data/model.js</code>, <code>data/plan_data.js</code> and <code>data/events.json</code>;
          expected values were written by <code>pipeline/train_model.py</code> and <code>pipeline/build_plan_data.py</code>.</p>
        </div>
        <button class="ghost" id="selftest-close">Close ✕</button>
      </div>
      <div class="selftest-grid">
        ${checks.map((c) => `<div class="selftest-row ${c.pass ? "ok" : "bad"}">
          <span class="st">${c.pass ? "PASS" : "FAIL"}</span>
          <span class="area">${c.area}</span>
          <span class="name">${c.name}</span>
          <span class="detail">${c.detail || ""}</span>
        </div>`).join("")}
      </div>
      <div class="selftest-foot">Run with <code>?selftest=1</code>. Tolerances: ±0.2 percentage points on model
      predictions, exact on counts and cohort sizes.</div>
    `);
    panel.select("#selftest-close").on("click", () => panel.remove());
  }

  if (new URLSearchParams(location.search).has("selftest")) {
    window.addEventListener("load", run);
    window.runSelfTest = run;
  }
})();
