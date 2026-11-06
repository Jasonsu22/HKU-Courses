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
          <p>Rows are recomputed in the browser from <code>data/everest_data.js</code> and
          <code>data/model.js</code>; expected values were written by <code>pipeline/train_model.py</code>.</p>
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
