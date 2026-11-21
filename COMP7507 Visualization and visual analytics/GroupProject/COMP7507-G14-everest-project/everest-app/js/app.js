/* App shell: view routing, lazy module init, data & methods panel. */
(function () {
  "use strict";

  const D = window.EVEREST_DATA;
  const M = window.EVEREST_MODEL;
  const { fmt } = U;

  const started = {};
  const starters = {
    history: () => window.M1.init(),
    routes: () => window.M2.init(),
    plan: () => window.M3.init(),
  };

  function show(name, push) {
    if (!starters[name]) name = "history";
    document.querySelectorAll(".tab").forEach((t) => {
      const on = t.dataset.view === name;
      t.classList.toggle("is-active", on);
      t.setAttribute("aria-selected", on ? "true" : "false");
    });
    document.querySelectorAll(".view").forEach((v) => {
      v.classList.toggle("is-active", v.id === "view-" + name);
    });
    if (!started[name]) {
      started[name] = true;
      starters[name]();
    }
    if (push) history.replaceState(null, "", "#" + name);
    window.scrollTo({ top: 0, behavior: "instant" });
  }

  document.querySelectorAll(".tab").forEach((t) => {
    t.addEventListener("click", () => show(t.dataset.view, true));
  });

  window.addEventListener("hashchange", () => {
    show((location.hash || "#history").slice(1), false);
  });

  // ------------------------------------------------------------ methods
  function methodsHtml() {
    const meta = D.meta;
    const member = M.member;
    const exped = M.expedition;
    const row = (label, obj) => {
      const t = obj.test || {};
      return `<tr><td>${label}</td><td>${fmt.dec3(t.brier)}</td><td>${fmt.dec3(t.logloss)}</td><td>${t.auc ? fmt.dec3(t.auc) : "–"}</td><td>${fmt.int(t.n)}</td></tr>`;
    };
    return `
      <h3>The data</h3>
      <p><strong>${meta.source.name}</strong>, built on ${meta.source.basedOn}. Snapshot: ${meta.source.snapshot}.
      ${fmt.int(meta.counts.expedition_rows)} Everest expeditions and
      ${fmt.int(meta.counts.member_rows)} Everest participation records, 1921–2024.</p>
      <p>The expedition CSV has no coordinates or route geometry. The terrain view is therefore built from
      public SRTM 30 m elevation tiles (Mapzen / AWS Open Data), and camp, col and peak positions come from
      OpenStreetMap under ODbL. The dashed connecting line is a schematic route, not a surveyed track;
      camp altitudes are OSM tags cross-checked against the database medians.</p>

      <h3>Definitions used everywhere</h3>
      <ul>
        <li><strong>Expedition success</strong>: <code>success1</code> — at least one climber reached the summit on route 1.
          It is not the share of members who summited.</li>
        <li><strong>Member success</strong>: <code>msuccess</code> — the individual member reached the summit.</li>
        <li><strong>Hired staff</strong>: counts and rates always come from the expedition fields
          <code>tothired</code> / <code>smthired</code>, because the member table lists only about half of the hired personnel.</li>
        <li><strong>Side</strong>: host country (Nepal = south, China = north). Route names are only used to separate
          the standard route from everything else.</li>
        <li><strong>Year</strong>: taken from the expedition record. The member table's own year field disagrees with its
          expedition in 34.8% of rows (96% before 2000), so it is not used for filtering.</li>
      </ul>

      <h3>Historical events</h3>
      <p>The History event explorer combines cited historical context with fixed-window descriptive comparisons.
      These windows show what was recorded before, during and after an event; they do not estimate a causal effect.
      The 2014–15 closure flags come from the expedition notes, while the linked news sources provide the external context.</p>

      <h3>The estimate</h3>
      <p>Two regularised logistic regressions using age band, recorded sex, season, side, route group, team size,
      hired support and oxygen. Expeditions abandoned because of the 2014 strike and avalanche or the 2015 earthquake
      (${fmt.int(M.meta.closure.expeditions)} expeditions, identified from the dataset's own notes) are excluded from fitting.</p>
      <ul>
        <li><strong>Member model</strong> (headline): probability that a climbing member with this profile summited.
          Population: non-hired climbing members, 2005–2024, age 15–80, closures excluded. n = ${fmt.int(member.n)},
          base rate ${fmt.pct(member.baseRate, 1)}. L2 penalty λ = ${member.lambda}.</li>
        <li><strong>Expedition model</strong> (context): probability that the expedition put at least one climber on
          the summit via route 1. n = ${fmt.int(exped.n)}, base rate ${fmt.pct(exped.baseRate, 1)}.</li>
      </ul>
      <p>Evaluation follows the proposal's time split: trained on 1990–2014, validated on 2015–2019, tested on
      2020–2024. Because success rates shifted strongly across decades, the deployed model is refitted on
      the last 20 seasons (${member.deployWindow[0]}–${member.deployWindow[1]}). Intervals are 95% ranges from
      300 bootstrap refits.</p>

      <h3>Held-out performance (2020–2024)</h3>
      <table class="metrics-table">
        <thead><tr><th>Member model</th><th>Brier</th><th>Log loss</th><th>AUC</th><th>n</th></tr></thead>
        <tbody>
          ${row("Constant rate", member.metrics.constant)}
          ${row("Side × season", member.metrics.sideSeason)}
          ${row("Logistic regression", member.metrics.model)}
        </tbody>
      </table>
      <table class="metrics-table" style="margin-top:12px">
        <thead><tr><th>Expedition model</th><th>Brier</th><th>Log loss</th><th>AUC</th><th>n</th></tr></thead>
        <tbody>
          ${row("Constant rate", exped.metrics.constant)}
          ${row("Side × season", exped.metrics.sideSeason)}
          ${row("Logistic regression", exped.metrics.model)}
        </tbody>
      </table>

      <h3>Known limitations</h3>
      <ul>
        <li>Success changes over time and the model has no time term. Overall 2020–2024 ran higher than the model
          (see the calibration chart), but individual plans vary, so "Your plan through time" checks each plan against recent seasons.</li>
        <li>Oxygen is close to a perfect separator in recent records (almost no oxygen-free member summited), even after excluding closures.
          The oxygen-free estimates rest on few, self-selected cases.</li>
        <li>"Oxygen used" and "hired staff above base camp" are recorded during the expedition rather than
          entered as a plan. They are treated as plan attributes here; the estimate is therefore a description
          of comparable historical expeditions, not a strict pre-trip forecast.</li>
        <li>Records are observational: associations, not causal effects, and certainly not a guarantee.</li>
        <li>Small cells are returned as insufficient evidence rather than as an overconfident number.</li>
      </ul>

      <h3>Reproducibility</h3>
      <p>Everything on this page is generated offline from the CSV snapshot. SHA-256 checksums:</p>
      <div class="sources">
        ${Object.entries(meta.checksums).map(([f, h]) => `<div><code>${f}</code> · ${h.slice(0, 16)}…</div>`).join("")}
      </div>

      <h3>Sources</h3>
      <div class="sources">
        <a href="https://registry.opendata.aws/terrain-tiles/" target="_blank" rel="noopener">Mapzen / AWS Terrain Tiles (SRTM)</a>
        <a href="https://www.openstreetmap.org/" target="_blank" rel="noopener">OpenStreetMap contributors (ODbL)</a>
      </div>
      <div class="sources">
        <a href="https://www.himalayandatabase.com/" target="_blank" rel="noopener">The Himalayan Database</a>
        <a href="https://mavenanalytics.io/data-playground/himalayan-expeditions" target="_blank" rel="noopener">Maven Analytics · Himalayan Expeditions</a>
        ${D.current.sources.map((s) => `<a href="${s.url}" target="_blank" rel="noopener">${s.publisher} · ${s.title}</a>`).join("")}
      </div>
      <p style="margin-top:14px;font-size:12px;color:#9a948a">Built ${meta.built}. No network requests at runtime.
        <a href="?selftest=1#history" style="color:#1e4a5f">Run the browser ↔ Python self-test</a>.</p>
    `;
  }

  const modal = document.getElementById("methods-modal");
  const body = document.getElementById("methods-body");
  function openMethods() {
    body.innerHTML = methodsHtml();
    modal.classList.add("is-open");
    modal.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  }
  function closeMethods() {
    modal.classList.remove("is-open");
    modal.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  }
  document.getElementById("open-methods").addEventListener("click", openMethods);
  document.getElementById("close-methods").addEventListener("click", closeMethods);
  modal.addEventListener("click", (e) => { if (e.target === modal) closeMethods(); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeMethods(); });
  document.querySelectorAll("details.secondary").forEach((details) => {
    details.addEventListener("toggle", () => {
      if (details.open) setTimeout(() => window.dispatchEvent(new Event("resize")), 60);
    });
  });

  window.APP = { show };

  // ---------------------------------------------------------------- boot
  show((location.hash || "#history").slice(1), false);
  // ?finding=H7 reproduces a finding in one click
  const wanted = new URLSearchParams(location.search).get("finding");
  if (wanted) {
    const owner = /^H[123]$/.test(wanted) ? "history" : /^H[456]$/.test(wanted) ? "routes" : "plan";
    show(owner, true);
    setTimeout(() => { const f = U.FINDINGS.get(wanted); if (f) f.apply(); }, 150);
  }
  if (new URLSearchParams(location.search).has("methods")) openMethods();
})();
