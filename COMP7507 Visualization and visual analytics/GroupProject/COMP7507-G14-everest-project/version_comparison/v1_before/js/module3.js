/* Module 03 — profile form and historical estimate. */
(function () {
  "use strict";

  const M = window.EVEREST_MODEL;
  const { fmt, COLORS, mount, el } = U;

  const DEFAULTS = {
    age: "30s", sex: "M", season: "Spring", side: "South",
    route: "standard", team: 12, hired: 20, o2: 1,
  };
  const profile = { ...DEFAULTS };

  // Shareable scenarios: ?age=40s&sex=F&season=Autumn&side=North&route=other&team=20&hired=30&o2=0
  (function readQuery() {
    const q = new URLSearchParams(location.search);
    const one = (k, cast) => {
      if (!q.has(k)) return;
      const v = cast ? cast(q.get(k)) : q.get(k);
      if (v != null) profile[k] = v;
    };
    one("age", (v) => (["u30", "30s", "40s", "50s", "60p"].includes(v) ? v : null));
    one("sex", (v) => (["M", "F"].includes(v) ? v : null));
    one("season", (v) => (["Spring", "Autumn", "Winter", "Summer"].includes(v) ? v : null));
    one("side", (v) => (["South", "North"].includes(v) ? v : null));
    one("route", (v) => (["standard", "other"].includes(v) ? v : null));
    one("team", (v) => (Number.isFinite(+v) ? Math.min(80, Math.max(2, +v)) : null));
    one("hired", (v) => (Number.isFinite(+v) ? Math.min(120, Math.max(0, +v)) : null));
    one("o2", (v) => (v === "1" || v === "0" ? +v : null));
  })();

  const AGE_LABEL = { u30: "under 30", "30s": "30–39", "40s": "40–49", "50s": "50–59", "60p": "60+" };
  const LEVEL_LABEL = {
    u30: "under 30", "30s": "30–39", "40s": "40–49", "50s": "50–59", "60p": "60+",
    F: "female", M: "male", Autumn: "autumn", Winter: "winter", Summer: "summer",
    North: "north side", other: "non-standard route", 1: "oxygen planned", 0: "no oxygen",
  };

  const teamKey = (t) => (t <= 8 ? "s" : t <= 20 ? "m" : "l");
  const sigmoid = (z) => 1 / (1 + Math.exp(-Math.max(-35, Math.min(35, z))));
  // small probabilities need a decimal, otherwise "0.6%" prints as "1%"
  const pctSmart = (x) => (x == null ? "–" : x < 0.1 ? d3.format(".1%")(x) : d3.format(".0%")(x));
  const dot = (a, b) => a.reduce((s, v, i) => s + v * b[i], 0);

  function design(model, p) {
    const x = [1];
    model.features.forEach((f) => {
      if (f.kind === "onehot") {
        x.push(p[f.group] === f.level ? 1 : 0);
      } else if (f.group === "team_log") {
        x.push((Math.log(Math.max(p.team, 1)) - f.mean) / f.sd);
      } else {
        x.push((Math.log1p(p.hired / Math.max(p.team, 1)) - f.mean) / f.sd);
      }
    });
    return x;
  }

  function predict(model, coef, p) {
    return sigmoid(dot(coef, design(model, p)));
  }

  function interval(model, p) {
    const ps = model.boot.map((b) => predict(model, b, p)).sort(d3.ascending);
    const q = (t) => ps[Math.min(ps.length - 1, Math.max(0, Math.round(t * (ps.length - 1))))];
    return [q(0.025), q(0.975)];
  }

  function cellLookup(model) {
    const maps = {};
    Object.entries(model.cells).forEach(([level, rows]) => {
      maps[level] = new Map(rows.map(([k, n, s]) => [k, { n, k: s }]));
    });
    return maps;
  }
  const MEM_CELLS = cellLookup(M.member);
  const EXP_CELLS = cellLookup(M.expedition);

  function cohort(p) {
    const keys = {
      exact: `${p.age}|${p.sex}|${p.season}|${p.side}|${p.route}|${p.o2}|${teamKey(p.team)}`,
      mid: `${p.age}|${p.sex}|${p.season}|${p.side}|${p.o2}`,
      broad: `${p.age}|${p.sex}|${p.season}|${p.side}`,
    };
    for (const level of ["exact", "mid", "broad"]) {
      const hit = MEM_CELLS[level].get(keys[level]);
      if (hit && hit.n > 0) return { level, ...hit, key: keys[level] };
    }
    return { level: "none", n: 0, k: 0 };
  }

  function expCohort(p) {
    const keys = {
      exact: `${p.season}|${p.side}|${p.route}|${p.o2}|${teamKey(p.team)}`,
      mid: `${p.season}|${p.side}|${p.o2}`,
      broad: `${p.season}|${p.side}`,
    };
    for (const level of ["exact", "mid", "broad"]) {
      const hit = EXP_CELLS[level].get(keys[level]);
      if (hit && hit.n > 0) return { level, ...hit, key: keys[level] };
    }
    return { level: "none", n: 0, k: 0 };
  }

  // ------------------------------------------------------------- form
  function buildForm() {
    const box = document.getElementById("m3-form");
    box.innerHTML = `
      <div class="card-head" style="margin-bottom:4px">
        <div><h2>Describe the plan</h2><p class="hint">Eight choices. Everything updates immediately.</p></div>
      </div>
      <div id="form-fields"></div>
      <div class="form-actions">
        <button class="btn btn--ghost" id="m3-reset">Reset to a default plan</button>
      </div>
      <p class="form-note">Nothing is sent anywhere: the estimate is computed in this page from exported model
      coefficients. Historical records only — not medical or safety advice.</p>`;

    const fields = document.getElementById("form-fields");

    function section(labelText) {
      const s = el("div", { class: "form-section" });
      s.appendChild(el("div", { class: "field-label" }, labelText));
      fields.appendChild(s);
      return s;
    }
    function pills(parent, options, key, format = (v) => v) {
      const wrap = el("div", { class: "pills" });
      options.forEach((o) => {
        const b = el("button", { type: "button", class: "pill" + (profile[key] === o.value ? " is-active" : "") }, format(o.value));
        b.addEventListener("click", () => {
          profile[key] = o.value;
          wrap.querySelectorAll(".pill").forEach((x) => x.classList.remove("is-active"));
          b.classList.add("is-active");
          update();
        });
        wrap.appendChild(b);
      });
      parent.appendChild(wrap);
    }
    function slider(parent, key, min, max, step, format) {
      const row = el("div", { class: "range-row" });
      const input = el("input", { type: "range", min, max, step, value: profile[key], class: "range" });
      const out = el("output", {}, format(profile[key]));
      input.addEventListener("input", () => {
        profile[key] = +input.value;
        out.textContent = format(profile[key]);
        update();
      });
      row.append(input, out);
      parent.appendChild(row);
    }

    let s = section("Age band");
    pills(s, ["u30", "30s", "40s", "50s", "60p"].map((v) => ({ value: v })), "age", (v) => AGE_LABEL[v]);

    s = section("Recorded sex");
    pills(s, [{ value: "F" }, { value: "M" }], "sex", (v) => (v === "F" ? "Female" : "Male"));

    s = section("Target season");
    pills(s, [{ value: "Spring" }, { value: "Autumn" }, { value: "Winter" }, { value: "Summer" }], "season");

    s = section("Climbing side");
    pills(s, [{ value: "South" }, { value: "North" }], "side", (v) => (v === "South" ? "South (Nepal)" : "North (Tibet)"));

    s = section("Route group");
    pills(s, [{ value: "standard" }, { value: "other" }], "route",
      (v) => (v === "standard" ? "Standard route" : "Other route"));

    s = section("Team size (members)");
    slider(s, "team", 2, 80, 1, (v) => v);

    s = section("Hired support (staff above base camp)");
    slider(s, "hired", 0, 120, 1, (v) => v);

    s = section("Planned oxygen");
    pills(s, [{ value: 1 }, { value: 0 }], "o2", (v) => (v ? "Yes" : "No"));

    document.getElementById("m3-reset").addEventListener("click", () => {
      Object.assign(profile, DEFAULTS);
      buildForm();
      update();
    });
  }

  // ----------------------------------------------------------- result
  function driverRows(p) {
    const x = design(M.member, p);
    return M.member.features
      .map((f, i) => ({ f, v: M.member.coef[i + 1] * x[i + 1] }))
      .filter((d) => Math.abs(d.v) > 0.01)
      .sort((a, b) => Math.abs(b.v) - Math.abs(a.v))
      .slice(0, 5);
  }

  function renderResult() {
    const box = document.getElementById("m3-result");
    const pModel = predict(M.member, M.member.coef, profile);
    const [lo, hi] = interval(M.member, profile);
    const coh = cohort(profile);
    const pExp = predict(M.expedition, M.expedition.coef, profile);
    const [elo, ehi] = interval(M.expedition, profile);
    const expCoh = expCohort(profile);

    const status = coh.level === "exact" && coh.n >= 50 ? "good"
      : coh.n >= 10 ? "limited" : "insufficient";

    if (status === "insufficient") {
      const obs = coh.n > 0 ? `${fmt.int(coh.k)} of ${fmt.int(coh.n)} summited (${fmt.pct(coh.k / coh.n, 1)})` : "no records at all";
      box.innerHTML = `
        <div class="result-top">
          <div>
            <div class="result-label">Personal estimate</div>
            <div class="insufficient">
              <h3>Insufficient evidence</h3>
              <p>This exact profile (age band, sex, season, side, route group, oxygen and team size)
              matches <b>${fmt.int(coh.n)}</b> historical climbing records. That is too few to report a
              number without overstating confidence.</p>
              <p class="obs">Closest comparison available: ${obs}.</p>
              <p>Try a standard route, the spring season, or a wider team-size band. For context, the
              expedition-level model gives <b>${pctSmart(pExp)}</b> (${pctSmart(elo)}–${pctSmart(ehi)});
              ${expCoh.n ? `it rests on ${fmt.int(expCoh.n)} comparable expeditions.` : "there are no directly comparable expeditions either."}</p>
            </div>
          </div>
        </div>`;
      return;
    }

    const obsRate = coh.n ? coh.k / coh.n : null;
    const expObs = expCoh.n ? expCoh.k / expCoh.n : null;
    const expGap = expCoh.n >= 10 && expObs != null ? Math.abs(pExp - expObs) : 0;
    const expRows = closestExpeditions(profile, 5);
    const drivers = driverRows(profile);
    const maxAbs = d3.max(drivers, (d) => Math.abs(d.v)) || 1;
    const statusLabel = status === "good"
      ? `${fmt.int(coh.n)} comparable records`
      : `${fmt.int(coh.n)} comparable records — low`;

    box.innerHTML = `
      <div class="result-top">
        <div>
          <div class="result-label">Chance of summiting, this profile</div>
          <div class="big-prob">${pctSmart(pModel).replace("%", "")}<small>%</small></div>
          <div class="prob-ci">95% model interval ${pctSmart(lo)}–${pctSmart(hi)} · n = ${fmt.int(M.member.n)}</div>
        </div>
        <span class="status status--${status}">${statusLabel}</span>
      </div>

      <div class="prob-bar">
        <div class="ci" style="left:${lo * 100}%;width:${(hi - lo) * 100}%"></div>
        <div class="fill" style="width:${pModel * 100}%"></div>
      </div>

      <div class="prob-meta">
        <span>Comparable members <b>${fmt.int(coh.n)}</b></span>
        <span>Observed in that group <b>${obsRate == null ? "–" : fmt.pct(obsRate, 1)}</b></span>
        <span>Expedition-level success <b>${fmt.pct(pExp, 0)}</b> (${fmt.pct(elo, 0)}–${fmt.pct(ehi, 0)})</span>
        <span>Comparable expeditions <b>${fmt.int(expCoh.n)}</b>${expObs == null ? "" : ` · observed <b>${fmt.pct(expObs, 0)}</b>`}</span>
      </div>

      <div class="result-body">
        <div class="result-block">
          <h3>What moves the estimate</h3>
          <div class="drivers">
            ${drivers.map((d) => {
              const factor = Math.exp(d.v);
              const w = (Math.abs(d.v) / maxAbs) * 100;
              const pos = d.v > 0;
              return `<div class="driver">
                <div>
                  <div>${labelOf(d.f)}</div>
                  <div class="bar"><i style="left:0;width:${w}%;background:${pos ? COLORS.navy : COLORS.rust}"></i></div>
                </div>
                <div class="val">${factor >= 10 ? d3.format(".0f")(factor) : d3.format(".1f")(factor)}×</div>
              </div>`;
            }).join("") || `<p class="hint">This profile sits at the reference level, so nothing moves it.</p>`}
          </div>
          <p class="result-note">Factors are relative to under 30 · male · spring · south side ·
          standard route · no oxygen. They are associations in the records, not causal effects.</p>
        </div>
        <div class="result-block">
          <h3>Reading it</h3>
          <p style="font-size:13px;color:#3c4046">
            ${fmt.int(coh.k)} of ${fmt.int(coh.n)} historical climbing members with this profile reached
            the summit (${obsRate == null ? "–" : fmt.pct(obsRate, 1)}). The model estimate is
            ${fmt.pct(pModel, 0)}${Math.abs(pModel - (obsRate || 0)) < 0.03
              ? ", essentially the raw group rate because this profile sits near the model average."
              : ", adjusting the raw group rate for team size, hired support and the other profile fields."}
          </p>
          <p style="font-size:12.5px;color:#6f6a62;margin-top:8px">
            The model is fitted on 2005–2024 and averages across those seasons; 2020–2024 ran higher,
            so treat this as a conservative baseline. Oxygen is close to a perfect separator in recent
            records, which makes the oxygen coefficient large.
          </p>
          ${status === "limited" ? `<p style="font-size:12.5px;color:#8a6a1f;margin-top:8px">Only ${fmt.int(coh.n)} directly comparable records: read the interval as wider than it looks.</p>` : ""}
          ${expGap > 0.12 ? `<p style="font-size:12.5px;color:#8a6a1f;margin-top:8px">The expedition model smooths this case: ${fmt.int(expCoh.k)} of ${fmt.int(expCoh.n)} comparable expeditions summited (${fmt.pct(expObs, 0)}) against a model figure of ${fmt.pct(pExp, 0)}. Where they disagree, trust the observed group.</p>` : ""}
        </div>
        <div class="result-block" style="grid-column:1 / -1">
          <h3>Comparable cohorts</h3>
          <table class="cohort-table">
            <thead><tr><th>Matching rule</th><th>Records</th><th>Observed summit share</th></tr></thead>
            <tbody>
              ${cohortRows(profile).map((r) => `<tr class="${r.level === coh.level ? "is-on" : ""}">
                <td>${r.label}</td><td>${fmt.int(r.hit.n)}</td><td>${fmt.pct(r.hit.k / r.hit.n, 1)}</td>
              </tr>`).join("")}
            </tbody>
          </table>
        </div>
        <div class="result-block" style="grid-column:1 / -1">
          <h3>Closest historical expeditions</h3>
          <p class="hint" style="margin:-4px 0 8px">Same side, season, route group and oxygen setting; ranked by team size, hired support and recency.</p>
          ${expRows.length ? `<table class="cohort-table">
            <thead><tr><th>Year · route</th><th>Team / hired</th><th>Result</th></tr></thead>
            <tbody>
              ${expRows.map((r) => `<tr>
                <td>${r.year} · ${r.route.length > 42 ? r.route.slice(0, 41) + "…" : r.route}</td>
                <td>${fmt.int(r.members)} / ${fmt.int(r.hired)}</td>
                <td>${r.success ? "someone summited" : "no summit"}${r.summits ? ` · ${fmt.int(r.summits)} members` : ""}</td>
              </tr>`).join("")}
            </tbody>
          </table>` : `<p class="hint">No historical expedition matches this side, season, route group and oxygen setting.</p>`}
        </div>
      </div>`;
  }

  const DRIVER_LABEL = {
    age: (lv) => `Age ${AGE_LABEL[lv] || lv}`,
    sex: (lv) => (lv === "F" ? "Female" : "Male"),
    season: (lv) => `${lv} season`,
    side: (lv) => `${lv} side`,
    route: (lv) => (lv === "other" ? "Non-standard route" : "Standard route"),
    o2: () => "Oxygen planned",
  };
  // Rank the historical expeditions that most resemble this plan.
  function closestExpeditions(p, k = 5) {
    const pool = window.EVEREST_DATA.expeditions.filter((r) =>
      r.season === p.season && r.side === p.side &&
      r.standard === (p.route === "standard") &&
      (r.o2 ? 1 : 0) === p.o2 && r.members > 0);
    if (!pool.length) return [];
    const support = Math.log1p(p.hired / Math.max(p.team, 1));
    return pool.map((r) => {
      const teamDist = Math.abs(Math.log(r.members) - Math.log(Math.max(p.team, 1)));
      const supDist = Math.abs(Math.log1p(r.hired / r.members) - support);
      const recency = (2024 - r.year) / 60;
      return { r, score: teamDist + supDist + recency };
    }).sort((a, b) => a.score - b.score).slice(0, k).map((x) => x.r);
  }

  function cohortRows(p) {
    const keys = {
      exact: `${p.age}|${p.sex}|${p.season}|${p.side}|${p.route}|${p.o2}|${teamKey(p.team)}`,
      mid: `${p.age}|${p.sex}|${p.season}|${p.side}|${p.o2}`,
      broad: `${p.age}|${p.sex}|${p.season}|${p.side}`,
    };
    const labels = {
      exact: "Exact profile (all seven fields)",
      mid: "Same age, sex, season, side and oxygen",
      broad: "Same age, sex, season and side",
    };
    return ["exact", "mid", "broad"]
      .map((level) => ({ level, label: labels[level], hit: MEM_CELLS[level].get(keys[level]) }))
      .filter((r) => r.hit && r.hit.n > 0)
      .filter((r, i, arr) => i === 0 || r.hit.n !== arr[i - 1].hit.n);
  }

  function labelOf(f) {
    if (f.kind === "numeric") return f.label;
    const fn = DRIVER_LABEL[f.group];
    return fn ? fn(f.level) : `${f.label}: ${f.level}`;
  }

  // ------------------------------------------------------- calibration
  function drawCalibration() {
    const bins = M.member.calibration.filter((b) => b.n >= 20);
    mount(document.getElementById("m3-calibration"), 300, (svg, w, h) => {
      const m = { top: 12, right: 18, bottom: 38, left: 46 };
      const iw = w - m.left - m.right;
      const ih = h - m.top - m.bottom;
      const x = d3.scaleLinear().domain([0, 1]).range([m.left, m.left + iw]);
      const y = d3.scaleLinear().domain([0, 1]).range([m.top + ih, m.top]);
      const g = svg.append("g");
      g.append("g").attr("transform", `translate(${m.left},0)`)
        .call(d3.axisLeft(y).ticks(4).tickSize(-iw).tickFormat(d3.format(".0%")))
        .call((s) => {
          s.selectAll(".tick line").attr("stroke", COLORS.grid);
          s.selectAll(".tick text").attr("fill", COLORS.faint).attr("font-size", 10.5);
          s.select(".domain").remove();
        });
      g.append("g").attr("transform", `translate(0,${m.top + ih})`)
        .call(d3.axisBottom(x).ticks(5).tickFormat(d3.format(".0%")))
        .call((s) => {
          s.selectAll(".tick line").attr("stroke", COLORS.grid);
          s.selectAll(".tick text").attr("fill", COLORS.faint).attr("font-size", 10.5);
          s.select(".domain").attr("stroke", COLORS.line);
        });
      g.append("line").attr("x1", x(0)).attr("x2", x(1)).attr("y1", y(0)).attr("y2", y(1))
        .attr("stroke", COLORS.faint).attr("stroke-dasharray", "3 4");

      g.selectAll("circle")
        .data(bins).join("circle")
        .attr("cx", (d) => x(d.predicted)).attr("cy", (d) => y(d.observed))
        .attr("r", (d) => 3 + Math.sqrt(d.n) / 2.2)
        .attr("fill", COLORS.navy).attr("opacity", .55)
        .on("mousemove", (event, d) => U.tipShow(event,
          `<strong>predicted ${fmt.pct(d.predicted, 0)}</strong><br>observed ${fmt.pct(d.observed, 1)}<br>` +
          `<span class="tt-muted">n = ${fmt.int(d.n)} members</span>`))
        .on("mouseleave", U.tipHide);

      g.append("text").attr("x", m.left + iw / 2).attr("y", h - 6)
        .attr("text-anchor", "middle").attr("font-size", 10.5).attr("fill", COLORS.faint)
        .text("predicted probability · test seasons 2020–2024");
      g.append("text").attr("x", x(0.5)).attr("y", y(0.06)).attr("text-anchor", "end")
        .attr("font-size", 10).attr("fill", COLORS.faint).text("dashed: perfect calibration");
      g.append("text").attr("x", m.left + 4).attr("y", m.top + 2)
        .attr("font-size", 10).attr("fill", COLORS.faint).text("observed");
    });
  }

  // ---------------------------------------------------------- metrics
  function renderMetrics() {
    const mm = M.member;
    const em = M.expedition;
    const row = (label, obj, cls) => `<tr class="${cls || ""}"><td>${label}</td>
      <td>${fmt.dec3(obj.brier)}</td><td>${fmt.dec3(obj.logloss)}</td>
      <td>${obj.auc ? fmt.dec3(obj.auc) : "–"}</td></tr>`;
    document.getElementById("m3-metrics-card").innerHTML = `
      <div class="card-head"><div>
        <h2>Model card</h2>
        <p class="hint">Held-out 2020–2024 seasons. Lower Brier and log loss are better; AUC is ranking only.</p>
      </div></div>
      <table class="metrics-table">
        <thead><tr><th>Member model</th><th>Brier</th><th>Log loss</th><th>AUC</th></tr></thead>
        <tbody>
          ${row("Constant rate", mm.metrics.constant.test)}
          ${row("Side × season", mm.metrics.sideSeason.test)}
          ${row("Logistic regression", mm.metrics.model.test, "best")}
        </tbody>
      </table>
      <table class="metrics-table" style="margin-top:14px">
        <thead><tr><th>Expedition model</th><th>Brier</th><th>Log loss</th><th>AUC</th></tr></thead>
        <tbody>
          ${row("Constant rate", em.metrics.constant.test)}
          ${row("Side × season", em.metrics.sideSeason.test)}
          ${row("Logistic regression", em.metrics.model.test, "best")}
        </tbody>
      </table>
      <p class="metrics-note">Trained on 1990–2014, validated on 2015–2019, tested on 2020–2024;
      deployed coefficients refit on ${mm.deployWindow[0]}–${mm.deployWindow[1]}.
      Member n = ${fmt.int(mm.n)} (${fmt.pct(mm.baseRate, 1)} summit share); expedition n = ${fmt.int(em.n)}
      (${fmt.pct(em.baseRate, 1)}). Bootstrap intervals from 300 refits.</p>`;
  }

  // ------------------------------------------------------------- update
  let raf = 0;
  function update() {
    cancelAnimationFrame(raf);
    raf = requestAnimationFrame(renderResult);
  }

  function init() {
    buildForm();
    renderResult();
    drawCalibration();
    renderMetrics();
  }

  window.M3 = {
    init,
    _test: {
      member: (p) => predict(M.member, M.member.coef, p),
      expedition: (p) => predict(M.expedition, M.expedition.coef, p),
      cohort,
      expCohort,
    },
  };
})();
