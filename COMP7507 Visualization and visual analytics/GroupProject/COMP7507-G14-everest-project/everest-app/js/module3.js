/* Module 03 — profile form and historical estimate. */
(function () {
  "use strict";

  const M = window.EVEREST_MODEL;
  const { fmt, COLORS, mount, el, wilson, withTip } = U;

  const DEFAULTS = {
    age: "30s", sex: "M", season: "Spring", side: "South",
    route: "standard", team: 12, hired: 20, o2: 1,
  };
  const profile = { ...DEFAULTS };
  const listeners = [];

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
        <div><h2>Describe the plan</h2><p class="hint">Eight choices. Every view updates immediately.</p></div>
      </div>
      <div id="form-fields"></div>
      <div class="form-actions">
        <button class="btn btn--ghost" id="m3-reset">Reset</button>
        <button class="btn btn--ghost" id="m3-see-route">See this route</button>
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
    function group(labelText) {
      fields.appendChild(el("div", { class: "form-group-label" }, labelText));
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

    group("Who");
    let s = section("Age band");
    pills(s, ["u30", "30s", "40s", "50s", "60p"].map((v) => ({ value: v })), "age", (v) => AGE_LABEL[v]);

    s = section("Recorded sex");
    pills(s, [{ value: "F" }, { value: "M" }], "sex", (v) => (v === "F" ? "Female" : "Male"));

    group("Where and when");
    s = section("Target season");
    pills(s, [{ value: "Spring" }, { value: "Autumn" }, { value: "Winter" }, { value: "Summer" }], "season");

    s = section("Climbing side");
    pills(s, [{ value: "South" }, { value: "North" }], "side", (v) => (v === "South" ? "South (Nepal)" : "North (Tibet)"));

    s = section("Route group");
    pills(s, [{ value: "standard" }, { value: "other" }], "route",
      (v) => (v === "standard" ? "Standard route" : "Other route"));

    group("How");
    s = section("Team size (members)");
    slider(s, "team", 2, 80, 1, (v) => v);

    s = section("Hired support (staff above base camp)");
    slider(s, "hired", 0, 120, 1, (v) => v);

    s = section("Planned oxygen");
    pills(s, [{ value: 1 }, { value: 0 }], "o2", (v) => (v ? "Yes" : "No"));

    document.getElementById("m3-reset").addEventListener("click", () => {
      setProfile(DEFAULTS);
    });
    document.getElementById("m3-see-route").addEventListener("click", () => {
      if (window.M2 && window.M2.setFilters) {
        Store.go("routes");
        window.M2.setFilters({ side: profile.side, season: profile.season, route: profile.route, period: "d20" });
      }
    });
  }

  function setProfile(next) {
    Object.assign(profile, next);
    buildForm();
    update();
  }

  // ----------------------------------------------------------- result
  const pts = (x) => (Math.abs(x) < .005 ? "0" : d3.format("+.0f")(x * 100));

  // Every single change to the plan, with the model's answer and its bootstrap range.
  function whatIfRows(p) {
    const rows = [];
    const add = (label, patch) => {
      const q = { ...p, ...patch };
      const c = cohort(q);
      rows.push({ label, patch, q, p: predict(M.member, M.member.coef, q), ci: interval(M.member, q), n: c.level === "exact" ? c.n : 0 });
    };
    ["u30", "30s", "40s", "50s", "60p"].filter((v) => v !== p.age).forEach((v) => add(`Age ${AGE_LABEL[v]}`, { age: v }));
    add(p.sex === "M" ? "Female" : "Male", { sex: p.sex === "M" ? "F" : "M" });
    ["Spring", "Autumn", "Winter", "Summer"].filter((v) => v !== p.season).forEach((v) => add(`${v} season`, { season: v }));
    add(p.side === "South" ? "North side" : "South side", { side: p.side === "South" ? "North" : "South" });
    add(p.route === "standard" ? "Other route" : "Standard route", { route: p.route === "standard" ? "other" : "standard" });
    add(p.o2 ? "No oxygen" : "With oxygen", { o2: p.o2 ? 0 : 1 });
    if (p.team * 2 <= 80) add(`Team of ${p.team * 2}`, { team: p.team * 2, hired: Math.min(120, p.hired * 2) });
    if (Math.floor(p.team / 2) >= 2) add(`Team of ${Math.floor(p.team / 2)}`, { team: Math.floor(p.team / 2), hired: Math.floor(p.hired / 2) });
    if (p.hired * 2 <= 120 && p.hired > 0) add(`Hired staff ${p.hired * 2}`, { hired: p.hired * 2 });
    if (p.hired > 0) add(`Hired staff ${Math.floor(p.hired / 2)}`, { hired: Math.floor(p.hired / 2) });
    return rows.sort((a, b) => b.p - a.p);
  }

  function drawLadder(status) {
    const rows = whatIfRows(profile);
    const pNow = predict(M.member, M.member.coef, profile);
    const rowH = 25;
    const box = document.getElementById("m3-ladder");
    if (!box) return;
    mount(box, rows.length * rowH + 44, (svg, w, h) => {
      const m = { top: 26, right: w < 520 ? 74 : 150, bottom: 16, left: w < 520 ? 108 : 146 };
      const x = d3.scaleLinear().domain([0, 1]).range([m.left, w - m.right]);
      const g = svg.append("g");
      x.ticks(5).forEach((t) => {
        g.append("line").attr("x1", x(t)).attr("x2", x(t)).attr("y1", m.top - 6).attr("y2", h - m.bottom).attr("stroke", COLORS.grid);
        g.append("text").attr("x", x(t)).attr("y", m.top - 11).attr("text-anchor", "middle").attr("font-size", 10.5).attr("fill", COLORS.muted).text(d3.format(".0%")(t));
      });
      if (status !== "insufficient") {
        g.append("line").attr("x1", x(pNow)).attr("x2", x(pNow)).attr("y1", m.top - 6).attr("y2", h - m.bottom)
          .attr("stroke", COLORS.plan).attr("stroke-width", 2);
      }
      rows.forEach((r, i) => {
        const y = m.top + i * rowH + rowH / 2;
        const row = g.append("g").attr("class", "ladder-row").style("cursor", "pointer");
        const sparse = r.n < 10;
        row.append("rect").attr("x", 0).attr("y", y - rowH / 2).attr("width", w).attr("height", rowH).attr("fill", "transparent");
        row.append("text").attr("x", m.left - 10).attr("y", y + 4).attr("text-anchor", "end").attr("font-size", 12).attr("fill", COLORS.ink).text(r.label);
        if (sparse) {
          row.append("text").attr("x", w - m.right + 10).attr("y", y + 4).attr("font-size", 11.5).attr("fill", COLORS.muted)
            .text(w < 520 ? "too few" : "too few records");
        } else {
          const up = r.p >= pNow;
          const c = up ? COLORS.above : COLORS.below;
          row.append("line").attr("x1", x(r.ci[0])).attr("x2", x(r.ci[1])).attr("y1", y).attr("y2", y).attr("stroke", c).attr("stroke-width", 1.2).attr("opacity", .55);
          if (status !== "insufficient") {
            row.append("line").attr("x1", x(pNow)).attr("x2", x(r.p)).attr("y1", y).attr("y2", y).attr("stroke", c).attr("stroke-width", 3).attr("stroke-linecap", "round");
          }
          row.append("circle").attr("cx", x(r.p)).attr("cy", y).attr("r", 5.5).attr("fill", c).attr("stroke", "#fff").attr("stroke-width", 2);
          row.append("text").attr("x", w - m.right + 10).attr("y", y + 4).attr("font-size", 12).attr("fill", COLORS.ink)
            .html(status === "insufficient" ? fmt.pct(r.p, 0)
              : `<tspan font-weight="600">${pts(r.p - pNow)} pts</tspan>${w < 520 ? "" : `<tspan fill="${COLORS.muted}"> → ${pctSmart(r.p)}</tspan>`}`);
        }
        withTip(row, `<strong>${r.label}</strong><br>` + (sparse
          ? `Only ${fmt.int(r.n)} matching records, so no estimate is given. Click to try it anyway.`
          : `Model ${fmt.pct(r.p, 1)} · range ${fmt.pct(r.ci[0], 0)}–${fmt.pct(r.ci[1], 0)}<br><span class="tt-muted">${fmt.int(r.n)} matching records · click to apply</span>`));
        row.on("click", () => { U.tipHide(); setProfile(r.patch); });
      });
    });
  }

  // Forest-style strip: model range vs what comparable members actually did.
  function drawStrip(pModel, lo, hi) {
    const ps = M.member.boot.map((b) => predict(M.member, b, profile));
    const all = PD.cohortRows(profile, "exact");
    const hist = PD.total(all.filter((r) => r.year >= 2005));
    const late = PD.total(all.filter((r) => r.year >= 2020));
    const rows = [
      { label: "Model estimate", v: pModel, ci: [lo, hi], color: COLORS.plan, note: "95% bootstrap range" },
      { label: "Same plan, 2005–24", v: hist.rate, ci: wilson(hist.k, hist.n), color: COLORS.slate, note: `${fmt.int(hist.k)} of ${fmt.int(hist.n)} members`, n: hist.n },
      { label: "Same plan, 2020–24", v: late.rate, ci: wilson(late.k, late.n), color: COLORS.slate, note: `${fmt.int(late.k)} of ${fmt.int(late.n)} members`, n: late.n },
    ];
    mount(document.getElementById("m3-strip"), 148, (svg, w, h) => {
      const small = w < 560;
      const m = { top: 22, right: small ? 56 : 170, bottom: 8, left: small ? 110 : 138 };
      const x = d3.scaleLinear().domain([0, 1]).range([m.left, w - m.right]);
      const g = svg.append("g");
      x.ticks(5).forEach((t) => {
        g.append("line").attr("x1", x(t)).attr("x2", x(t)).attr("y1", m.top).attr("y2", h - m.bottom).attr("stroke", COLORS.grid);
        g.append("text").attr("x", x(t)).attr("y", m.top - 8).attr("text-anchor", "middle").attr("font-size", 10.5).attr("fill", COLORS.muted).text(d3.format(".0%")(t));
      });
      const rh = (h - m.top - m.bottom) / rows.length;
      // bootstrap density above the model row
      const bins = d3.bin().domain([0, 1]).thresholds(100)(ps);
      const dmax = d3.max(bins, (b) => b.length) || 1;
      rows.forEach((r, i) => {
        const y = m.top + rh * i + rh / 2 + 3;
        g.append("text").attr("x", m.left - 10).attr("y", y + 4).attr("text-anchor", "end").attr("font-size", 12)
          .attr("font-weight", i === 0 ? 600 : 400).attr("fill", COLORS.ink).text(r.label);
        if (i === 0) {
          g.selectAll("rect.den").data(bins.filter((b) => b.length)).join("rect")
            .attr("x", (b) => x(b.x0)).attr("width", (b) => Math.max(1.5, x(b.x1) - x(b.x0) - .4))
            .attr("y", (b) => y - 3 - (b.length / dmax) * 14).attr("height", (b) => (b.length / dmax) * 14)
            .attr("fill", COLORS.plan).attr("opacity", .35);
        }
        if (r.v == null || (r.n != null && r.n < 10)) {
          g.append("text").attr("x", m.left + 4).attr("y", y + 4).attr("font-size", 11.5).attr("fill", COLORS.muted)
            .text(`fewer than 10 records (n = ${fmt.int(r.n || 0)})`);
          return;
        }
        g.append("line").attr("x1", x(r.ci[0])).attr("x2", x(r.ci[1])).attr("y1", y).attr("y2", y).attr("stroke", r.color).attr("stroke-width", 2.4).attr("stroke-linecap", "round");
        g.append("circle").attr("cx", x(r.v)).attr("cy", y).attr("r", i === 0 ? 7 : 5.5).attr("fill", r.color).attr("stroke", "#fff").attr("stroke-width", 2)
          .call((s) => withTip(s, `<strong>${r.label}</strong><br>${fmt.pct(r.v, 1)} · range ${fmt.pct(r.ci[0], 0)}–${fmt.pct(r.ci[1], 0)}<br><span class="tt-muted">${r.note}</span>`));
        g.append("text").attr("x", w - m.right + 10).attr("y", y + 4).attr("font-size", 12).attr("fill", COLORS.ink)
          .html(`<tspan font-weight="600">${fmt.pct(r.v, 0)}</tspan>${small ? "" : `<tspan fill="${COLORS.muted}" font-size="11">  ${r.note}</tspan>`}`);
      });
    });
    return { hist, late };
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
      : coh.level === "exact" && coh.n >= 10 ? "limited" : coh.n >= 10 ? "limited" : "insufficient";

    const ladderHtml = `<div class="result-block" id="m3-ladder-block">
        <h3>${status === "insufficient" ? "What would give enough evidence" : "Change one thing"}</h3>
        <p class="hint" style="margin:-4px 0 6px">${status === "insufficient"
          ? "Model estimates for single changes; click one to apply it."
          : "How the estimate moves if you change one choice, in percentage points. Thin lines are model ranges. Click a row to apply it."}</p>
        <div class="chart" id="m3-ladder"></div>
      </div>`;

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
              <p>For context, the expedition-level model gives <b>${pctSmart(pExp)}</b> (${pctSmart(elo)}–${pctSmart(ehi)});
              ${expCoh.n ? `it rests on ${fmt.int(expCoh.n)} comparable expeditions.` : "there are no directly comparable expeditions either."}</p>
            </div>
          </div>
        </div>${ladderHtml}`;
      drawLadder(status);
      return;
    }

    const statusLabel = coh.level === "exact"
      ? `${fmt.int(coh.n)} exact matches${status === "limited" ? " — low" : ""}`
      : `No exact matches · ${fmt.int(coh.n)} in a wider group`;
    const expObs = expCoh.n ? expCoh.k / expCoh.n : null;
    const expGap = expCoh.n >= 10 && expObs != null ? Math.abs(pExp - expObs) : 0;

    box.innerHTML = `
      <div class="result-top">
        <div>
          <div class="result-label">Historical estimate for comparable members</div>
          <div class="big-prob">${pctSmart(pModel).replace("%", "")}<small>%</small></div>
          <div class="prob-ci">Model range ${pctSmart(lo)}–${pctSmart(hi)}, fitted on ${fmt.int(M.member.n)} members, 2005–2024</div>
        </div>
        <span class="status status--${status}">${statusLabel}</span>
      </div>
      <div class="chart" id="m3-strip" style="margin-top:12px"></div>
      <div class="reading" id="m3-reading"></div>
      <div class="prob-meta">
        <span>Expedition-level success <b>${fmt.pct(pExp, 0)}</b> (${fmt.pct(elo, 0)}–${fmt.pct(ehi, 0)})</span>
        <span>Comparable expeditions <b>${fmt.int(expCoh.n)}</b>${expObs == null ? "" : ` · observed <b>${fmt.pct(expObs, 0)}</b>`}</span>
      </div>
      ${ladderHtml}
      ${expGap > 0.12 ? `<p class="result-warn">The expedition model smooths this case: ${fmt.int(expCoh.k)} of ${fmt.int(expCoh.n)} comparable expeditions summited (${fmt.pct(expObs, 0)}) against a model figure of ${fmt.pct(pExp, 0)}. Where they disagree, trust the observed group.</p>` : ""}
      <p class="result-note">These are associations in historical records, not causal effects or a promise.</p>`;

    const { hist, late } = drawStrip(pModel, lo, hi);
    drawLadder(status);

    // The reading is computed for this plan, never a fixed sentence.
    const notes = [];
    if (hist.n >= 10) {
      const gap = pModel - hist.rate;
      notes.push(`${fmt.int(hist.k)} of ${fmt.int(hist.n)} members with this exact plan summited in 2005–2024 (${fmt.pct(hist.rate, 0)}); the model gives ${fmt.pct(pModel, 0)}${Math.abs(gap) < .03 ? ", close to that record." : ", because it also adjusts for team size, hired support and the other choices."}`);
    }
    if (late.n >= 10) {
      const gap = late.rate - pModel;
      notes.push(Math.abs(gap) < .03
        ? `The most recent period (2020–24) ran close to the model at ${fmt.pct(late.rate, 0)}.`
        : `The most recent period ran <b>${gap > 0 ? "higher" : "lower"}</b> than the model: ${fmt.pct(late.rate, 0)} in 2020–24, so this estimate may be ${gap > 0 ? "too low" : "too high"} for this plan today.`);
    } else {
      notes.push(`Too few members with this plan in 2020–24 to check it against recent seasons.`);
    }
    document.getElementById("m3-reading").innerHTML = notes.map((t) => `<p>${t}</p>`).join("");
  }

  const DRIVER_LABEL = {
    age: (lv) => `Age ${AGE_LABEL[lv] || lv}`,
    sex: (lv) => (lv === "F" ? "Female" : "Male"),
    season: (lv) => `${lv} season`,
    side: (lv) => `${lv} side`,
    route: (lv) => (lv === "other" ? "Non-standard route" : "Standard route"),
    o2: () => "Oxygen planned",
  };

  function cohortTable() {
    const keys = {
      exact: `${profile.age}|${profile.sex}|${profile.season}|${profile.side}|${profile.route}|${profile.o2}|${teamKey(profile.team)}`,
      mid: `${profile.age}|${profile.sex}|${profile.season}|${profile.side}|${profile.o2}`,
      broad: `${profile.age}|${profile.sex}|${profile.season}|${profile.side}`,
    };
    const labels = {
      exact: "Exact profile (all seven fields)",
      mid: "Same age, sex, season, side and oxygen",
      broad: "Same age, sex, season and side",
    };
    const coh = cohort(profile);
    const rows = ["exact", "mid", "broad"]
      .map((level) => ({ level, label: labels[level], hit: MEM_CELLS[level].get(keys[level]) }))
      .filter((r) => r.hit && r.hit.n > 0);
    document.getElementById("m3-cohorts").innerHTML = `
      <div class="card-head"><div><h2>Comparable cohorts</h2>
      <p class="hint">How the observed share changes with the matching rule (2005–2024, closures excluded). The highlighted row is the one the status label uses.</p></div></div>
      ${rows.length ? `<table class="cohort-table">
        <thead><tr><th>Matching rule</th><th>Records</th><th>Observed summit share</th></tr></thead>
        <tbody>${rows.map((r) => `<tr class="${r.level === coh.level ? "is-on" : ""}"><td>${r.label}</td><td>${fmt.int(r.hit.n)}</td><td>${fmt.pct(r.hit.k / r.hit.n, 1)}</td></tr>`).join("")}</tbody>
      </table>` : `<p class="hint">No comparable records for this plan.</p>`}`;
  }

  function renderClosureCard() {
    const c = M.meta.closure;
    const e = M.meta.closureEffect;
    document.getElementById("m3-closure-card").innerHTML = `
      <div class="card-head"><div><h2>Why the 2014–15 closures are excluded</h2></div></div>
      <p class="hint" style="max-width:none">The dataset's own notes say ${fmt.int(c.expeditions)} expeditions (${fmt.int(c.members)} climbing members)
      were abandoned because of the 2014 Sherpa strike and avalanche or the 2015 earthquake. Many stopped before anyone would use oxygen,
      so they appear as "no oxygen, no summit". That is not a fair oxygen comparison. Removing them moves the model's oxygen factor
      from about <b>${d3.format(".0f")(Math.exp(e.o2CoefWith))}×</b> to about <b>${d3.format(".0f")(Math.exp(e.o2CoefWithout))}×</b> the odds. Oxygen-free
      climbs remain rare and self-selected, so this is still an association. These expeditions stay visible in the historical charts on page 1.</p>`;
  }

  // ------------------------------------------------------- calibration
  let calMode = "test";
  function drawCalibration() {
    const source = calMode === "test" ? M.member.calibration : M.member.calibrationAll;
    const bins = source.filter((b) => b.n >= 20);
    document.getElementById("m3-cal-hint").textContent = calMode === "test"
      ? "Predicted vs observed share on the held-out 2020–2024 seasons, using the model trained on 1990–2014. Dots above the line mean under-prediction."
      : "Predicted vs observed on the 2005–2024 data the deployed model was fitted on. This shows fit, not out-of-sample skill.";
    mount(document.getElementById("m3-calibration"), 300, (svg, w, h) => {
      const m = { top: 12, right: 18, bottom: 38, left: 46 };
      const iw = w - m.left - m.right;
      const ih = h - m.top - m.bottom;
      const x = d3.scaleLinear().domain([0, 1]).range([m.left, m.left + iw]);
      const y = d3.scaleLinear().domain([0, 1]).range([m.top + ih, m.top]);
      const g = svg.append("g");
      U.axisY(g, y, m.left, iw, { format: d3.format(".0%") });
      U.axisX(g, x, m.top + ih, { ticks: 5, format: d3.format(".0%") });
      g.append("line").attr("x1", x(0)).attr("x2", x(1)).attr("y1", y(0)).attr("y2", y(1))
        .attr("stroke", COLORS.muted).attr("stroke-dasharray", "3 4");
      g.selectAll("circle").data(bins).join("circle")
        .attr("cx", (d) => x(d.predicted)).attr("cy", (d) => y(d.observed))
        .attr("r", (d) => 3 + Math.sqrt(d.n) / (calMode === "test" ? 2.2 : 4))
        .attr("fill", COLORS.slate).attr("opacity", .75).attr("stroke", "#fff").attr("stroke-width", 1.5)
        .call((s) => withTip(s, (d) => `<strong>predicted ${fmt.pct(d.predicted, 0)}</strong><br>observed ${fmt.pct(d.observed, 1)}<br><span class="tt-muted">n = ${fmt.int(d.n)} members</span>`));
      U.caption(g, m.left + iw / 2, h - 6, "predicted probability", "middle");
      U.caption(g, x(.62), y(.5), "on the line = well calibrated");
      U.caption(g, m.left + 4, m.top + 10, "observed share");
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
  let activeTab = "estimate";
  const tabRender = {};

  function syncUrl() {
    Store.writeParams({
      age: profile.age, sex: profile.sex, season: profile.season, side: profile.side,
      route: profile.route, team: profile.team, hired: profile.hired, o2: profile.o2,
    });
  }

  function renderActive() {
    if (activeTab === "estimate") renderResult();
    if (activeTab === "trust") { cohortTable(); renderClosureCard(); drawCalibration(); renderMetrics(); }
    (tabRender[activeTab] || []).forEach((f) => f());
  }

  function update() {
    cancelAnimationFrame(raf);
    raf = requestAnimationFrame(() => {
      if (document.getElementById("view-plan").classList.contains("is-active")) syncUrl();
      renderActive();
    });
  }

  function setTab(tab) {
    activeTab = tab;
    document.querySelectorAll("#m3-subtabs button").forEach((b) => {
      const on = b.dataset.tab === tab;
      b.classList.toggle("is-active", on);
      b.setAttribute("aria-selected", on ? "true" : "false");
    });
    document.querySelectorAll(".plan-tab").forEach((p) => p.classList.toggle("is-active", p.dataset.tab === tab));
    renderActive();
  }

  function drawTimeline() {
    const byYear = d3.rollups(PD.usable(), (v) => d3.sum(v, (r) => r.n), (r) => r.year);
    const data = d3.range(1990, 2025).map((y) => ({ year: y, v: (byYear.find((b) => b[0] === y) || [0, 0])[1] }));
    U.timeline(document.getElementById("m3-timeline"), {
      data, height: 62, getRange: () => PD.state.range, valueLabel: "climbing members per year",
      onChange: (r) => { PD.setRange(r || [1990, 2024]); if (!r) drawTimeline(); },
    });
    const n = PD.total(PD.live());
    document.getElementById("m3-range-label").textContent =
      `${PD.state.range[0]}–${PD.state.range[1]} · ${fmt.int(n.n)} members`;
  }

  function buildFindings() {
    const E = window.EVEREST_PLAN.expect;
    const def = E.defaultByPeriod;
    const r = (x) => fmt.pct(x.k / x.n, 0);
    const c = M.meta.closureEffect;
    U.findings("m3-findings", [
      {
        id: "H7", title: "A plan's chance is a stable number", verdict: "Rejected",
        text: () => `The default plan's group went ${r(def[1990])} (1990–94) → ${r(def[2010])} (2010–14) → ${r(def[2020])} (2020–24), while the model gives one number.`,
        apply: () => { setProfile(DEFAULTS); setTab("time"); U.spotlight("m3-card-through"); },
      },
      {
        id: "H8", title: "Oxygen multiplies your odds by about 69", verdict: "Overstated",
        text: () => `${fmt.int(E.noOxygen.closure)} of the ${fmt.int(E.noOxygen.members)} "no oxygen" members were on expeditions abandoned in the 2014–15 closures. Without them the factor is about ${d3.format(".0f")(Math.exp(c.o2CoefWithout))}×.`,
        apply: () => { setTab("trust"); U.spotlight("m3-closure-card"); },
      },
      {
        id: "H3", title: "More hired support is what drives success", verdict: "Mixed",
        text: () => `Look along the three "Hired" rows: the gap between them changes from period to period, so hired support alone doesn't explain success.`,
        apply: () => { setTab("time"); U.spotlight("m3-card-grid"); },
      },
    ]);
  }

  function init() {
    buildForm();
    buildFindings();
    drawTimeline();
    document.querySelectorAll("#m3-subtabs button").forEach((b) => b.addEventListener("click", () => setTab(b.dataset.tab)));
    document.getElementById("m3-closure").addEventListener("change", (e) => PD.setDropClosure(e.target.checked));
    U.seg("m3-cal-mode", calMode, (v) => { calMode = v; drawCalibration(); });
    PD.onChange(() => { drawTimeline(); renderActive(); });
    setTab(new URLSearchParams(location.search).get("tab") || "estimate");
  }

  window.M3 = {
    init,
    profile,
    setProfile,
    setTab,
    register(tab, fn) { (tabRender[tab] = tabRender[tab] || []).push(fn); },
    onProfile: update,
    _test: {
      member: (p) => predict(M.member, M.member.coef, p),
      expedition: (p) => predict(M.expedition, M.expedition.coef, p),
      cohort,
      expCohort,
    },
  };
})();
