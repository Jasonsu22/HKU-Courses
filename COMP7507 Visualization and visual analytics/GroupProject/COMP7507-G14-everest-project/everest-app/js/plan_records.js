/* Page 3 · Records: parallel coordinates of real expeditions, linked to a closest-match table. */
(function () {
  "use strict";

  const { fmt, COLORS, mount, withTip } = U;
  const local = { scope: "match", order: "logic", brushes: {} };

  const DIMS = [
    { key: "year", title: "Year", get: (r) => r.year, scale: () => d3.scaleLinear(), nice: false, format: d3.format("d") },
    { key: "members", title: "Team size", get: (r) => r.members, scale: () => d3.scaleLog(), format: d3.format("d"), ticks: [1, 3, 10, 30, 100], clamp: 1 },
    { key: "support", title: "Hired per member", get: (r) => (r.members ? r.hired / r.members : null), scale: () => d3.scaleSqrt(), format: d3.format(".1f"), ticks: [0, .5, 1, 2, 4, 8] },
    { key: "days", title: "Days to summit", get: (r) => (r.daysSummit > 0 && r.daysSummit <= 130 ? r.daysSummit : null), scale: () => d3.scaleLinear(), format: d3.format("d") },
    { key: "hp", title: "High point (m)", get: (r) => (r.hp && r.hp >= 5000 ? r.hp : null), scale: () => d3.scaleLinear(), format: d3.format(",") },
    { key: "deaths", title: "Deaths", get: (r) => r.mDeaths + r.hDeaths, scale: () => d3.scaleLinear(), format: d3.format("d") },
  ];

  function pool() {
    const p = M3.profile;
    const [a, b] = PD.state.range;
    return window.EVEREST_DATA.expeditions.filter((r) =>
      r.members > 0 && r.year >= a && r.year <= b && !(PD.state.dropClosure && r.closure) &&
      (local.scope === "all" || (r.side === p.side && r.season === p.season)));
  }

  function correlation(rows, dim) {
    const pairs = rows.map((r) => [dim.get(r), r.success ? 1 : 0]).filter(([v]) => v != null);
    if (pairs.length < 5) return 0;
    const mx = d3.mean(pairs, (d) => d[0]), my = d3.mean(pairs, (d) => d[1]);
    let sxy = 0, sx = 0, sy = 0;
    pairs.forEach(([x, y]) => { sxy += (x - mx) * (y - my); sx += (x - mx) ** 2; sy += (y - my) ** 2; });
    return sx && sy ? sxy / Math.sqrt(sx * sy) : 0;
  }

  // Rank expeditions by closeness to the plan on team size and hired support, preferring recent ones.
  function closest(rows, k = 5) {
    const p = M3.profile;
    const support = Math.log1p(p.hired / Math.max(p.team, 1));
    const same = rows.filter((r) => r.standard === (p.route === "standard") && (r.o2 ? 1 : 0) === p.o2);
    return (same.length ? same : rows).map((r) => ({
      r,
      score: Math.abs(Math.log(r.members) - Math.log(Math.max(p.team, 1))) +
        Math.abs(Math.log1p(r.hired / r.members) - support) + (2024 - r.year) / 60,
    })).sort((a, b) => a.score - b.score).slice(0, k).map((x) => x.r);
  }

  function renderTable(selected, totalN) {
    const box = document.getElementById("m3-pcp-table");
    const k = selected.filter((r) => r.success).length;
    const rows = closest(selected);
    box.innerHTML = `<p class="pcp-summary"><b>${fmt.int(selected.length)}</b> of ${fmt.int(totalN)} expeditions selected · <b>${fmt.int(k)}</b> put someone on the summit (${selected.length ? fmt.pct(k / selected.length, 0) : "–"})</p>
      <h3 class="tbl-title">Closest to this plan, within the selection</h3>
      ${rows.length ? `<table class="cohort-table">
        <thead><tr><th>Year · route</th><th>Team / hired</th><th>How it ended</th></tr></thead>
        <tbody>${rows.map((r) => `<tr><td>${r.year} · ${r.side} · ${r.route.length > 34 ? r.route.slice(0, 33) + "…" : r.route}</td>
          <td>${fmt.int(r.members)} / ${fmt.int(r.hired)}</td>
          <td>${r.success ? `Summit · ${fmt.int(r.summits)} members` : r.end}</td></tr>`).join("")}</tbody>
      </table>` : `<p class="hint">No expedition matches this selection. Clear a brush or widen the period.</p>`}`;
    return rows;
  }

  function draw() {
    const rows = pool();
    const p = M3.profile;
    const dims = [...DIMS];
    if (local.order === "corr") dims.sort((a, b) => Math.abs(correlation(rows, b)) - Math.abs(correlation(rows, a)));
    const [ra, rb] = PD.state.range;
    document.getElementById("m3-pcp-hint").innerHTML =
      `Each line is one expedition, ${ra}–${rb}${local.scope === "match" ? `, ${p.side} side in ${p.season}` : ""}. Drag along any axis to select a range. Green lines reached the summit, purple did not; pink lines are the closest matches.` +
      (local.order === "corr" ? " Axes run from the strongest to the weakest correlation with reaching the summit." : "");

    mount(document.getElementById("m3-pcp"), 420, (svg, w, h) => {
      if (!rows.length) { U.emptyNote(svg, w, h, "No expeditions in this period and scope."); renderTable([], 0); return; }
      const m = { top: 34, right: 34, bottom: 16, left: 34 };
      const x = d3.scalePoint().domain(dims.map((d) => d.key)).range([m.left, w - m.right]);
      const y = {};
      dims.forEach((d) => {
        const vals = rows.map(d.get).filter((v) => v != null);
        const [lo, hi] = d3.extent(vals);
        let dom = [lo, hi];
        if (d.key === "members") dom = [1, Math.max(hi, 2)];
        if (d.key === "support" || d.key === "deaths") dom = [0, Math.max(hi, 1)];
        if (dom[0] === dom[1]) dom = [dom[0] - 1, dom[1] + 1];
        y[d.key] = d.scale().domain(dom).range([h - m.bottom, m.top]);
      });
      const yOf = (d, r) => {
        let v = d.get(r);
        if (v == null) return null;
        if (d.key === "members") v = Math.max(1, v);
        return y[d.key](v);
      };
      const lineGen = d3.line().defined((a) => a[1] != null);
      const pathOf = (r) => lineGen(dims.map((d) => [x(d.key), yOf(d, r)]));
      const base = svg.append("g").attr("fill", "none");
      const lines = base.selectAll("path").data(rows).join("path")
        .attr("d", pathOf).attr("stroke", (r) => (r.success ? COLORS.above : COLORS.below)).attr("stroke-width", 1);
      const accent = svg.append("g").attr("fill", "none");

      function refresh() {
        const active = Object.entries(local.brushes).filter(([k]) => dims.some((d) => d.key === k));
        const selected = rows.filter((r) => active.every(([k, range]) => {
          const d = dims.find((q) => q.key === k);
          const py = yOf(d, r);
          return py != null && py >= range[0] && py <= range[1];
        }));
        const set = new Set(selected);
        const faint = rows.length > 400 ? .14 : .28;
        lines.attr("stroke-opacity", (r) => (set.has(r) ? faint : .025));
        const top = renderTable(selected, rows.length);
        accent.selectAll("path").data(top).join("path").attr("d", pathOf)
          .attr("stroke", COLORS.plan).attr("stroke-width", 2.4).attr("stroke-opacity", .95)
          .style("cursor", "help").call((s) => withTip(s, (r) => `<strong>${r.year} · ${r.side}</strong><br>${r.route}<br>${fmt.int(r.members)} members · ${fmt.int(r.hired)} hired<br>${r.success ? "Summit" : r.end}`));
      }

      dims.forEach((d) => {
        const g = svg.append("g").attr("transform", `translate(${x(d.key)},0)`);
        const axis = d3.axisLeft(y[d.key]).tickFormat(d.format).tickSize(4);
        if (d.ticks) axis.tickValues(d.ticks.filter((t) => t >= y[d.key].domain()[0] && t <= y[d.key].domain()[1]));
        else axis.ticks(6);
        g.call(axis).call((s) => {
          s.selectAll("text").attr("font-size", 10.5).attr("fill", COLORS.ink).attr("paint-order", "stroke").attr("stroke", "#fff").attr("stroke-width", 3);
          s.select(".domain").attr("stroke", COLORS.ink);
          s.selectAll(".tick line").attr("stroke", COLORS.ink);
        });
        g.append("text").attr("y", m.top - 16).attr("text-anchor", d === dims[0] ? "start" : d === dims[dims.length - 1] ? "end" : "middle")
          .attr("x", d === dims[0] ? -24 : d === dims[dims.length - 1] ? 24 : 0).attr("font-size", w < 560 ? 10.5 : 12).attr("font-weight", 600).attr("fill", COLORS.ink).text(d.title);
        // plan markers exist only on the two axes the plan actually sets
        const planV = d.key === "members" ? Math.max(1, p.team) : d.key === "support" ? p.hired / Math.max(p.team, 1) : null;
        if (planV != null) {
          g.append("path").attr("transform", `translate(0,${y[d.key](planV)})`).attr("d", d3.symbol(d3.symbolDiamond, 110)())
            .attr("fill", COLORS.plan).attr("stroke", "#fff").attr("stroke-width", 1.5)
            .call((s) => withTip(s, `<strong>Your plan</strong><br>${d.title}: ${d.format(planV)}`));
        }
        const brush = d3.brushY().extent([[-13, m.top], [13, h - m.bottom]])
          .on("end", (event) => {
            if (!event.sourceEvent) return;
            if (event.selection) local.brushes[d.key] = event.selection; else delete local.brushes[d.key];
            refresh();
          });
        const gb = g.append("g").call(brush);
        gb.selectAll(".selection").attr("fill", COLORS.plan).attr("fill-opacity", .18).attr("stroke", COLORS.plan);
        if (local.brushes[d.key]) gb.call(brush.move, local.brushes[d.key]);
      });
      refresh();
    });
  }

  // Scripts load at the end of <body>, before app.js boots, so the page is ready here.
  (function setup() {
    M3.register("records", draw);
    U.seg("m3-pcp-scope", local.scope, (v) => { local.scope = v; local.brushes = {}; draw(); });
    U.seg("m3-pcp-order", local.order, (v) => { local.order = v; draw(); });
  })();
})();
