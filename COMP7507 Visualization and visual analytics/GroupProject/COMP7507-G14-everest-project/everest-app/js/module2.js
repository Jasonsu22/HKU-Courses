/* Module 02 — route and current-situation explorer. */
(function () {
  "use strict";

  const D = window.EVEREST_DATA;
  const { fmt, COLORS, wilson, withTip, mount, el, statCard } = U;

  const PERIODS = [
    { label: "All", value: "all" },
    { label: "pre-1990", value: "pre" },
    { label: "1990–2014", value: "t1" },
    { label: "2015–2019", value: "t2" },
    { label: "2020–2024", value: "t3" },
    { label: "2005–2024", value: "d20" },
  ];
  const rangeOf = (p) => ({
    all: [1900, 2100], pre: [1900, 1989], t1: [1990, 2014],
    t2: [2015, 2019], t3: [2020, 2024], d20: [2005, 2024],
  }[p] || [1900, 2100]);

  const DEFAULT_FILTERS = { side: "All", season: "Spring", period: "d20", route: "standard" };
  const ALL_HISTORY = { side: "All", season: "All", period: "all", route: "All" };
  const state = {
    ...DEFAULT_FILTERS, campSide: "both", family: null, routesMode: "bars",
  };
  let hoverAlt = null;

  function currentFilterLabel() {
    const side = state.side === "All" ? "Both sides" : `${state.side} side`;
    const season = state.season === "All" ? "all seasons" : state.season;
    const period = PERIODS.find((p) => p.value === state.period).label;
    const route = state.route === "All" ? "all routes" : state.route === "standard" ? "standard routes" : "other routes";
    return `${side} · ${season} · ${period} · ${route}`;
  }

  // Shareable filters: ?side=North&season=Spring&period=t3&route=standard&camp=north
  (function readQuery() {
    const q = new URLSearchParams(location.search);
    const onRoutes = location.hash.startsWith("#routes");
    const pick = (key, allowed, stateKey = key) => {
      const v = q.get("r_" + key) || (onRoutes ? q.get(key) : null);
      if (v && allowed.includes(v)) state[stateKey] = v;
    };
    pick("side", ["All", "South", "North"]);
    pick("season", ["All", "Spring", "Autumn", "Winter", "Summer"]);
    pick("period", PERIODS.map((p) => p.value));
    pick("route", ["All", "standard", "other"]);
    pick("camp", ["south", "north", "both"], "campSide");
  })();

  function rowsFiltered({ ignoreSide = false } = {}) {
    const [lo, hi] = rangeOf(state.period);
    return D.expeditions.filter((r) => {
      if (!ignoreSide && state.side !== "All" && r.side !== state.side) return false;
      if (state.season !== "All" && r.season !== state.season) return false;
      if (state.route === "standard" && !r.standard) return false;
      if (state.route === "other" && r.standard) return false;
      if (state.family && r.family !== state.family) return false;
      return r.year >= lo && r.year <= hi;
    });
  }

  function stats(rows) {
    const n = rows.length;
    const k = rows.reduce((a, r) => a + (r.success ? 1 : 0), 0);
    const days = rows.map((r) => r.daysSummit).filter((v) => v != null && v > 0);
    const team = rows.map((r) => r.members).filter((v) => v > 0);
    const members = d3.sum(rows, (r) => r.members);
    const hired = d3.sum(rows, (r) => r.hired);
    const deaths = d3.sum(rows, (r) => r.mDeaths + r.hDeaths);
    const o2 = rows.reduce((a, r) => a + (r.o2 ? 1 : 0), 0);
    return {
      n, k, rate: n ? k / n : null, ci: n ? wilson(k, n) : [0, 0],
      daysMedian: days.length ? d3.median(days) : null,
      teamMedian: team.length ? d3.median(team) : null,
      members, hired, deaths,
      hiredPer10: members ? (hired / members) * 10 : null,
      o2share: n ? o2 / n : null,
      deathsPer1000: members + hired ? (deaths / (members + hired)) * 1000 : null,
    };
  }

  // ---------------------------------------------------------------- KPIs
  function renderKpis() {
    const s = stats(rowsFiltered());
    const box = document.getElementById("m2-kpis");
    box.innerHTML = "";
    if (!s.n) {
      box.innerHTML = `<div class="kpi" style="grid-column:1/-1"><div class="kpi-label">No expeditions match these filters. Try a wider period or season.</div></div>`;
      return;
    }
    const label = currentFilterLabel();
    box.append(
      statCard({
        value: fmt.int(s.n),
        label: "expeditions in this filter",
        sub: label,
      }),
      statCard({
        value: s.rate == null ? "–" : fmt.pct(s.rate, 1),
        label: "expeditions with a summit",
        sub: `${fmt.int(s.k)} of ${fmt.int(s.n)} · 95% CI ${fmt.pct(s.ci[0])}–${fmt.pct(s.ci[1])}`,
        accent: true,
      }),
      statCard({
        value: s.daysMedian == null ? "–" : fmt.dec1(s.daysMedian) + " d",
        label: "median days, base camp → summit",
        sub: "only expeditions with a recorded summit day",
      }),
      statCard({
        value: s.teamMedian == null ? "–" : fmt.dec1(s.teamMedian),
        label: "median team size",
        sub: `${fmt.dec1(s.hiredPer10)} hired staff per 10 members`,
      })
    );
  }

  // ------------------------------------------------------------ filters
  function renderAll() {
    renderFilters();
    renderKpis();
    drawCompare();
    drawGap();
    drawRoutes();
    drawFunnel();
    drawCalendar();
    drawBc();
    if (window.GEO) GEO.update(reachFn());
    Store.writeParams({
      r_side: state.side === "All" ? null : state.side,
      r_season: state.season === "All" ? null : state.season,
      r_period: state.period === "all" ? null : state.period,
      r_route: state.route === "All" ? null : state.route,
    });
  }

  function renderFilters() {
    const box = document.getElementById("m2-filters");
    box.innerHTML = "";
    const groups = [
      { key: "side", label: "Side", options: ["All", "South", "North"] },
      { key: "season", label: "Season", options: ["All", "Spring", "Autumn", "Winter", "Summer"] },
      { key: "period", label: "Period", options: PERIODS.map((p) => p.value), format: (v) => PERIODS.find((p) => p.value === v).label },
      { key: "route", label: "Route group", options: ["All", "standard", "other"], format: (v) => (v === "All" ? "All" : v === "standard" ? "Standard" : "Other") },
    ];
    groups.forEach((g) => {
      const wrap = el("div", { class: "filter-group" });
      wrap.append(el("div", { class: "filter-label" }, g.label));
      const seg = el("div", { class: "seg" });
      g.options.forEach((v) => {
        const b = el("button", { type: "button" }, g.format ? g.format(v) : v);
        if (state[g.key] === v) b.classList.add("is-active");
        b.addEventListener("click", () => { state[g.key] = v; renderAll(); });
        seg.appendChild(b);
      });
      wrap.appendChild(seg);
      box.appendChild(wrap);
    });
    const actions = el("div", { class: "filter-actions" });
    if (state.family) {
      const chip = el("button", { type: "button", class: "filter-chip" }, `${state.family} ✕`);
      chip.addEventListener("click", () => { state.family = null; renderAll(); });
      actions.appendChild(chip);
    }
    const toPlan = el("button", { type: "button", class: "ghost" }, "Use this as my plan →");
    toPlan.title = "Copies the side, season and route group into page 3";
    toPlan.addEventListener("click", () => {
      Store.go("plan");
      const patch = {};
      if (state.side !== "All") patch.side = state.side;
      if (state.season !== "All") patch.season = state.season;
      if (state.route !== "All") patch.route = state.route;
      window.M3.setProfile(patch);
    });
    const allHistory = el("button", { type: "button", class: "ghost" }, "All history");
    allHistory.title = "Show all years, seasons and route groups";
    allHistory.addEventListener("click", () => { Object.assign(state, ALL_HISTORY, { family: null }); renderAll(); });
    const reset = el("button", { type: "button", class: "ghost filter-reset" }, "Reset");
    reset.title = "Return to the recent spring standard-route view";
    reset.addEventListener("click", () => { Object.assign(state, DEFAULT_FILTERS, { family: null }); renderAll(); });
    actions.append(toPlan, allHistory, reset);
    box.appendChild(actions);
  }

  // ------------------------------------------------------- compare grid
  const METRICS = [
    { key: "rate", title: "Summit success", fmt: (v) => fmt.pct(v, 0), pct: true, ci: (s) => s.ci, sub: (s) => `${fmt.int(s.k)} of ${fmt.int(s.n)}` },
    { key: "daysMedian", title: "Median days to summit", fmt: (v) => fmt.dec1(v), sub: (s) => `${fmt.int(s.n)} expeditions` },
    { key: "teamMedian", title: "Median team size", fmt: (v) => fmt.dec1(v), sub: (s) => `${fmt.int(s.members)} members` },
    { key: "hiredPer10", title: "Hired staff per 10 members", fmt: (v) => fmt.dec1(v), sub: (s) => `${fmt.int(s.hired)} hired` },
    { key: "o2share", title: "Oxygen used", fmt: (v) => fmt.pct(v, 0), pct: true, ci: (s) => wilson(s.o2, s.n), sub: () => "of expeditions" },
    { key: "deathsPer1000", title: "Deaths per 1,000 people", fmt: (v) => fmt.dec1(v), sub: (s) => `${fmt.int(s.deaths)} deaths` },
  ];

  function drawCompare() {
    const hint = document.getElementById("m2-compare-hint");
    const south = stats(rowsFiltered({ ignoreSide: true }).filter((r) => r.side === "South"));
    const north = stats(rowsFiltered({ ignoreSide: true }).filter((r) => r.side === "North"));
    hint.textContent = `Expedition-level · ${currentFilterLabel()}. South n = ${fmt.int(south.n)}, north n = ${fmt.int(north.n)}. Lines through the rate dots are 95% intervals.`;

    mount(document.getElementById("m2-compare"), 396, (svg, w, h) => {
      const cols = w < 460 ? 1 : 2;
      const rows = Math.ceil(METRICS.length / cols);
      const rh = h / rows;
      const cw = w / cols;
      const g = svg.append("g");
      METRICS.forEach((metric, i) => {
        const cell = g.append("g").attr("transform", `translate(${(i % cols) * cw},${Math.floor(i / cols) * rh})`);
        const iw = cw - 34;
        cell.append("text").attr("x", 8).attr("y", 16).attr("font-size", 12.5).attr("font-weight", 600).attr("fill", COLORS.ink).text(metric.title);
        const sv = south[metric.key], nv = north[metric.key];
        const max = metric.pct ? 1 : (Math.max(sv || 0, nv || 0) * 1.25 || 1);
        const x = d3.scaleLinear().domain([0, max]).range([16, iw]);
        const yy = 40;
        cell.append("line").attr("x1", x(0)).attr("x2", x(max)).attr("y1", yy).attr("y2", yy).attr("stroke", COLORS.line).attr("stroke-width", 2);
        [0, max].forEach((t) => cell.append("text").attr("x", x(t)).attr("y", yy + 25).attr("text-anchor", t ? "end" : "start").attr("font-size", 10).attr("fill", COLORS.muted).text(metric.pct ? d3.format(".0%")(t) : d3.format(".0f")(t)));
        if (sv != null && nv != null) {
          cell.append("line").attr("x1", x(sv)).attr("x2", x(nv)).attr("y1", yy).attr("y2", yy).attr("stroke", COLORS.ink).attr("stroke-width", 3);
        }
        [{ name: "South", v: sv, s: south, c: COLORS.south, dy: -7 }, { name: "North", v: nv, s: north, c: COLORS.north, dy: 7 }].forEach((row) => {
          if (row.v == null) return;
          const cy = yy + row.dy;
          if (metric.ci) {
            const [lo, hi] = metric.ci(row.s);
            cell.append("line").attr("x1", x(lo)).attr("x2", x(hi)).attr("y1", cy).attr("y2", cy).attr("stroke", row.c).attr("stroke-width", 2);
          }
          cell.append("circle").attr("cx", x(row.v)).attr("cy", cy).attr("r", 7.5).attr("fill", row.c).attr("stroke", "#fff").attr("stroke-width", 1.5);
          cell.append("text").attr("x", x(row.v)).attr("y", cy + 3.5).attr("text-anchor", "middle").attr("font-size", 9.5).attr("font-weight", 700).attr("fill", "#fff").attr("pointer-events", "none").text(row.name[0]);
        });
        const text = cell.append("text").attr("x", 8).attr("y", yy + 42).attr("font-size", 11.5).attr("fill", COLORS.ink);
        const part = (name, v, s) => `<tspan font-weight="600">${name} ${v == null ? "–" : metric.fmt(v)}</tspan><tspan fill="${COLORS.muted}" font-size="10.5"> ${s.n ? metric.sub(s) : "no records"}</tspan>`;
        text.html(part("S", sv, south));
        cell.append("text").attr("x", 8).attr("y", yy + 57).attr("font-size", 11.5).attr("fill", COLORS.ink).html(part("N", nv, north));
      });
    });
  }

  // ---------------------------------------------------------- gap over time
  function drawGap() {
    const list = rowsFiltered({ ignoreSide: true });
    const [pa, pb] = rangeOf(state.period);
    const a = Math.max(1980, pa), b = Math.min(2024, pb);
    const years = d3.range(a, b + 1);
    const series = (side) => {
      const by = d3.rollup(list.filter((r) => r.side === side), (v) => ({ n: v.length, k: v.filter((r) => r.success).length }), (r) => r.year);
      return years.map((y) => {
        let n = 0, k = 0;
        [y - 1, y, y + 1].forEach((q) => { const t = by.get(q); if (t) { n += t.n; k += t.k; } });
        return { x: y, n, k, rate: n >= 5 ? k / n : null };
      });
    };
    const S = series("South"), N = series("North");
    const gap = years.map((y, i) => ({ x: y, v: S[i].rate != null && N[i].rate != null ? S[i].rate - N[i].rate : null }));
    document.getElementById("m2-gap-hint").textContent =
      `Expedition-level · ${currentFilterLabel()}. Three-year success on each side, with 95% bands. Points with fewer than 5 expeditions are left out. The strip shows which side leads; darker means over 20 points.`;
    mount(document.getElementById("m2-gap"), 396, (svg, w, h) => {
      if (years.length < 3 || !gap.some((d) => d.v != null)) { U.emptyNote(svg, w, h, "Too few expeditions on one side to compare through time."); return; }
      const m = { top: 28, right: 14, bottom: 24, left: 42 };
      const stripH = 26, gapH = 40;
      const x = d3.scaleLinear().domain([a, b]).range([m.left, w - m.right]);
      const bottom = h - m.bottom - stripH - gapH;
      const y = d3.scaleLinear().domain([0, 1]).range([bottom, m.top]);
      const g = svg.append("g");
      U.axisY(g, y, m.left, w - m.left - m.right, { format: d3.format(".0%"), ticks: 5 });
      U.axisX(g, x, bottom, { ticks: Math.round(w / 90) });
      U.eventMarks(g, x, m.top, bottom);
      [{ d: S, c: COLORS.south, name: "South" }, { d: N, c: COLORS.north, name: "North" }].forEach((s) => {
        g.append("path").datum(s.d).attr("d", d3.area().defined((q) => q.rate != null).x((q) => x(q.x)).y0((q) => y(wilson(q.k, q.n)[0])).y1((q) => y(wilson(q.k, q.n)[1]))).attr("fill", s.c).attr("opacity", .15);
        g.append("path").datum(s.d).attr("d", d3.line().defined((q) => q.rate != null).x((q) => x(q.x)).y((q) => y(q.rate))).attr("fill", "none").attr("stroke", s.c).attr("stroke-width", 2.4);
      });
      U.legend(g, m.left, 13, [{ label: "South", color: COLORS.south, line: true }, { label: "North", color: COLORS.north, line: true }]);
      const top = bottom + gapH - 8;
      U.caption(g, m.left, top - 5, "Who leads:");
      g.append("text").attr("x", m.left + 62).attr("y", top - 5).attr("font-size", 11).attr("fill", COLORS.ink).text("orange = south, blue = north");
      U.horizon(g, svg, { series: gap, x, top, height: stripH, step: .2, color: [COLORS.south, COLORS.north] });
      g.append("rect").attr("x", m.left).attr("y", m.top).attr("width", w - m.left - m.right).attr("height", top + stripH - m.top).attr("fill", "transparent")
        .on("mousemove", (event) => {
          const yr = Math.max(a, Math.min(b, Math.round(x.invert(d3.pointer(event, svg.node())[0]))));
          const i = years.indexOf(yr);
          const line = (name, q) => `${name}: ${q.rate == null ? `too few (n = ${fmt.int(q.n)})` : `${fmt.int(q.k)} of ${fmt.int(q.n)}, ${fmt.pct(q.rate, 0)}`}`;
          U.tipShow(event, `<strong>${yr - 1}–${yr + 1}</strong><br>${line("South", S[i])}<br>${line("North", N[i])}`);
        }).on("mouseleave", U.tipHide);
    });
  }

  // ------------------------------------------------------------- routes
  function drawRoutes() {
    document.getElementById("m2-routes-hint").textContent = state.routesMode === "bars"
      ? `Expedition-level · ${currentFilterLabel()}. Grouped by the leading route name, at least 20 expeditions, ranked by success with 95% intervals.`
      : `Expedition-level · ${currentFilterLabel()}. Area shows expeditions; colour shows success against the filtered average. Click a family to filter everything to it and see its raw route names.`;
    if (state.routesMode === "tree") { drawTreemap(); return; }
    const rows = rowsFiltered();
    const byRoute = d3.rollups(rows, (v) => ({
      route: v[0].family,
      n: v.length, k: d3.sum(v, (d) => (d.success ? 1 : 0)),
      days: d3.median(v.map((d) => d.daysSummit).filter((x) => x != null && x > 0)),
    }), (d) => d.family).map(([, v]) => v)
      .filter((d) => d.n >= 20)
      .sort((a, b) => b.k / b.n - a.k / a.n || b.n - a.n)
      .slice(0, 8);
    const colorOf = (d) => (d.route.startsWith("South") ? COLORS.south : d.route.startsWith("North") ? COLORS.north : COLORS.slate);

    mount(document.getElementById("m2-routes"), 54 + Math.max(1, byRoute.length) * 40, (svg, w, h) => {
      if (!byRoute.length) { U.emptyNote(svg, w, h, "No route family has 20+ expeditions in this filter. Widen the period or season."); return; }
      const m = { top: 24, right: 96, bottom: 8, left: Math.min(190, w * .34) };
      const x = d3.scaleLinear().domain([0, 1]).range([m.left, w - m.right]);
      const y = d3.scaleBand().domain(byRoute.map((d) => d.route)).range([m.top, h - m.bottom]).padding(.34);
      const g = svg.append("g");
      x.ticks(5).forEach((t) => {
        g.append("line").attr("x1", x(t)).attr("x2", x(t)).attr("y1", m.top).attr("y2", h - m.bottom).attr("stroke", COLORS.grid);
        g.append("text").attr("x", x(t)).attr("y", m.top - 8).attr("text-anchor", "middle").attr("font-size", 10.5).attr("fill", COLORS.muted).text(d3.format(".0%")(t));
      });
      byRoute.forEach((d) => {
        const row = g.append("g").style("cursor", "pointer");
        const yy = y(d.route), bh = y.bandwidth();
        const [lo, hi] = wilson(d.k, d.n);
        row.append("text").attr("x", m.left - 10).attr("y", yy + bh / 2 + 4).attr("text-anchor", "end").attr("font-size", 12).attr("fill", COLORS.ink).text(d.route);
        row.append("rect").attr("x", m.left).attr("y", yy).attr("height", bh).attr("width", x(d.k / d.n) - m.left).attr("rx", 3).attr("fill", colorOf(d));
        row.append("line").attr("x1", x(lo)).attr("x2", x(hi)).attr("y1", yy + bh / 2).attr("y2", yy + bh / 2).attr("stroke", COLORS.ink).attr("stroke-width", 1.6);
        row.append("text").attr("x", w - m.right + 8).attr("y", yy + bh / 2 + 4).attr("font-size", 12).attr("fill", COLORS.ink)
          .html(`<tspan font-weight="600">${fmt.pct(d.k / d.n, 0)}</tspan><tspan fill="${COLORS.muted}" font-size="10.5"> n=${fmt.int(d.n)}</tspan>`);
        row.append("rect").attr("x", 0).attr("y", yy - 4).attr("width", w).attr("height", bh + 8).attr("fill", "transparent");
        withTip(row, `<strong>${d.route}</strong><br>${fmt.int(d.k)} of ${fmt.int(d.n)} successful (${fmt.pct(d.k / d.n, 1)})<br><span class="tt-muted">${d.days ? "median " + fmt.dec1(d.days) + " days to summit · " : ""}click to filter</span>`);
        row.on("click", () => { U.tipHide(); state.family = state.family === d.route ? null : d.route; renderAll(); });
      });
    });
  }

  function drawTreemap() {
    const rows = rowsFiltered();
    const base = rows.length ? rows.filter((r) => r.success).length / rows.length : 0;
    const color = U.diverging(.35);
    const summary = (v) => ({ n: v.length, k: v.filter((r) => r.success).length });
    const data = state.family
      ? { name: state.family, children: d3.rollups(rows, summary, (r) => r.route).map(([name, s]) => ({ name, ...s })) }
      : { name: "All", children: d3.rollups(rows, (v) => v, (r) => r.side).map(([side, v]) => ({
          name: side, children: d3.rollups(v, summary, (r) => r.family).map(([name, s]) => ({ name, family: name, ...s })),
        })) };
    mount(document.getElementById("m2-routes"), 400, (svg, w, h) => {
      if (!rows.length) { U.emptyNote(svg, w, h, "No expeditions match these filters."); return; }
      const root = d3.hierarchy(data).sum((d) => (d.children ? 0 : d.n)).sort((a, b) => b.value - a.value);
      d3.treemap().tile(d3.treemapSquarify).size([w, h - 26]).paddingInner(2).paddingTop((d) => (d.depth === 1 && d.children ? 18 : 0)).round(true)(root);
      const pattern = U.hatch(svg);
      U.gradientLegend(svg, w - 174, h - 22, 170, color, [-.35, .35], [[0, "−35 pts"], [.5, "average"], [1, "+35 pts"]]);
      const g = svg.append("g");
      root.descendants().filter((d) => d.depth === 1 && d.children).forEach((d) => {
        g.append("text").attr("x", d.x0 + 2).attr("y", d.y0 + 13).attr("font-size", 12).attr("font-weight", 600).attr("fill", COLORS.ink).text(`${d.data.name} side · ${fmt.int(d.value)} expeditions`);
      });
      const leaf = g.selectAll("g.leaf").data(root.leaves()).join("g").attr("class", "leaf").attr("transform", (d) => `translate(${d.x0},${d.y0})`).style("cursor", (d) => (d.data.family ? "pointer" : "default"));
      const fillOf = (d) => (d.data.n < 5 ? pattern : color(d.data.k / d.data.n - base));
      leaf.append("rect").attr("width", (d) => Math.max(0, d.x1 - d.x0)).attr("height", (d) => Math.max(0, d.y1 - d.y0)).attr("rx", 3).attr("fill", fillOf);
      leaf.filter((d) => d.x1 - d.x0 > 70 && d.y1 - d.y0 > 30).each(function (d) {
        const ink = d.data.n < 5 ? COLORS.ink : U.inkOn(color(d.data.k / d.data.n - base));
        const max = Math.floor((d.x1 - d.x0 - 10) / 6.2);
        const name = d.data.name.length > max ? d.data.name.slice(0, max - 1) + "…" : d.data.name;
        d3.select(this).append("text").attr("x", 6).attr("y", 16).attr("font-size", 11.5).attr("font-weight", 600).attr("fill", ink).text(name);
        d3.select(this).append("text").attr("x", 6).attr("y", 30).attr("font-size", 10.5).attr("fill", ink).text(`${fmt.pct(d.data.k / d.data.n, 0)} · n=${fmt.int(d.data.n)}`);
      });
      withTip(leaf, (d) => `<strong>${d.data.name}</strong><br>${fmt.int(d.data.k)} of ${fmt.int(d.data.n)} expeditions (${fmt.pct(d.data.k / d.data.n, 0)})${d.data.family ? `<br><span class="tt-muted">Click to filter and see raw route names</span>` : ""}`);
      leaf.on("click", (e, d) => { if (d.data.family) { U.tipHide(); state.family = d.data.family; renderAll(); } });
    });
  }

  // ---------------------------------------------------------- altitude funnel
  // Tolerance: a recorded high point within 60 m of a camp's elevation counts as reaching it.
  function validHp(side) {
    return rowsFiltered({ ignoreSide: true }).filter((r) => r.side === side && r.hp);
  }
  function reachFn() {
    const cache = { south: validHp("South"), north: validHp("North") };
    return (side, elev) => {
      const list = cache[side];
      return list.length >= 5 ? list.filter((r) => r.hp >= elev - 60).length / list.length : null;
    };
  }

  let funnelApi = null;
  function drawFunnel() {
    const data = ["South", "North"].map((side) => ({ side, list: validHp(side) }));
    document.getElementById("m2-funnel-hint").innerHTML =
      `Share of filtered expeditions whose recorded high point reached each altitude (south n = ${fmt.int(data[0].list.length)}, north n = ${fmt.int(data[1].list.length)}). Hover to light up that altitude on the profile, map and 3D view.`;
    const alts = d3.range(5400, 8851, 50);
    mount(document.getElementById("m2-funnel"), 380, (svg, w, h) => {
      const m = { top: 28, right: 16, bottom: 34, left: 42 };
      const x = d3.scaleLinear().domain([5400, 8849]).range([m.left, w - m.right]);
      const y = d3.scaleLinear().domain([0, 1]).range([h - m.bottom, m.top]);
      const g = svg.append("g");
      U.axisY(g, y, m.left, w - m.left - m.right, { format: d3.format(".0%") });
      U.axisX(g, x, h - m.bottom, { ticks: Math.round(w / 90), format: d3.format(",") });
      U.caption(g, (m.left + w - m.right) / 2, h - 4, "Altitude (m)", "middle");
      const usable = data.filter((d) => d.list.length >= 5);
      if (!usable.length) { U.emptyNote(svg, w, h, "Too few expeditions with a recorded high point."); return; }
      usable.forEach((d) => {
        const pts = alts.map((a) => ({ a, s: d.list.filter((r) => r.hp >= Math.min(a, 8789)).length / d.list.length }));
        d.pts = pts;
        g.append("path").datum(pts).attr("d", d3.line().x((q) => x(q.a)).y((q) => y(q.s)).curve(d3.curveStepAfter)).attr("fill", "none").attr("stroke", COLORS.side[d.side]).attr("stroke-width", 2.6);
      });
      U.legend(g, m.left, 13, usable.map((d) => ({ label: d.side, color: COLORS.side[d.side], line: true })));
      const cross = g.append("line").attr("y1", m.top).attr("y2", h - m.bottom).attr("stroke", COLORS.plan).attr("stroke-width", 2).attr("opacity", 0);
      funnelApi = (alt) => { if (alt == null) cross.attr("opacity", 0); else cross.attr("x1", x(alt)).attr("x2", x(alt)).attr("opacity", 1); };
      g.append("rect").attr("x", m.left).attr("y", m.top).attr("width", w - m.left - m.right).attr("height", h - m.top - m.bottom).attr("fill", "transparent")
        .on("mousemove", (event) => {
          const alt = Math.round(x.invert(d3.pointer(event, svg.node())[0]) / 50) * 50;
          setHoverAlt(alt);
          U.tipShow(event, `<strong>${fmt.int(alt)} m</strong><br>` + usable.map((d) => {
            const k = d.list.filter((r) => r.hp >= Math.min(alt, 8789)).length;
            return `${d.side}: ${fmt.int(k)} of ${fmt.int(d.list.length)} (${fmt.pct(k / d.list.length, 0)})`;
          }).join("<br>"));
        })
        .on("mouseleave", () => { setHoverAlt(null); U.tipHide(); });
    });
  }

  function setHoverAlt(alt) {
    hoverAlt = alt;
    if (funnelApi) funnelApi(alt);
    if (campsApi) campsApi(alt);
    if (window.GEO) GEO.highlight(alt);
  }

  // -------------------------------------------------------------- camps
  let campsApi = null;
  function drawCamps() {
    const sides = state.campSide === "both" ? ["South", "North"] : [state.campSide === "south" ? "South" : "North"];
    mount(document.getElementById("m2-camps"), 380, (svg, w, h) => {
      const m = { top: 26, right: 8, bottom: 8, left: 50 };
      const iw = w - m.left - m.right;
      const y = d3.scaleLinear().domain([4800, 9000]).range([h - m.bottom, m.top]);
      const g = svg.append("g");
      U.axisY(g, y, m.left, iw, { ticks: 5, format: (v) => fmt.int(v) + " m", size: 10.5 });
      const cols = sides.length === 2 ? [0.31, 0.69] : [0.4];
      sides.forEach((side, i) => {
        const cx = m.left + iw * cols[i];
        const series = D.camps[side.toLowerCase()].filter((c) => c.elev);
        const color = COLORS.side[side];
        g.append("line").attr("x1", cx).attr("x2", cx).attr("y1", y(series[series.length - 1].elev)).attr("y2", y(series[0].elev)).attr("stroke", color).attr("stroke-width", 3);
        series.forEach((c) => {
          const isSummit = c.label === "Smt";
          g.append("circle").attr("cx", cx).attr("cy", y(c.elev)).attr("r", isSummit ? 7 : 5.5).attr("fill", isSummit ? color : "#fff").attr("stroke", color).attr("stroke-width", 2.4).style("cursor", "help")
            .on("mouseenter", () => setHoverAlt(c.elev))
            .on("mousemove", (event) => U.tipShow(event,
              `<strong>${side} · ${c.name}</strong><br>median ${fmt.int(c.elev)} m<br>` +
              `${fmt.pct(c.share, 1)} of ${side.toLowerCase()} expeditions list this camp (n=${fmt.int(c.n)})<br>` +
              `<span class="tt-muted">${c.medianDate ? "typical date " + c.medianDate : "no dated records"}</span>`))
            .on("mouseleave", () => { setHoverAlt(null); U.tipHide(); });
          const left = sides.length === 2 && i === 0;
          g.append("text").attr("x", left ? cx - 13 : cx + 13).attr("y", y(c.elev) + 4).attr("text-anchor", left ? "end" : "start").attr("font-size", w < 520 ? 10.5 : 11.5).attr("fill", COLORS.ink)
            .html(`${c.label === "Smt" ? "Summit" : c.label} <tspan font-weight="600">${fmt.int(c.elev)}</tspan><tspan fill="${COLORS.muted}" font-size="10"> ${fmt.pct(c.share, 0)}</tspan>`);
        });
        g.append("text").attr("x", cx).attr("y", m.top - 8).attr("text-anchor", "middle").attr("font-size", 12).attr("font-weight", 600).attr("fill", COLORS.ink).text(side + " side");
      });
      const cross = g.append("line").attr("x1", m.left).attr("x2", w - m.right).attr("stroke", COLORS.plan).attr("stroke-width", 2).attr("opacity", 0).attr("pointer-events", "none");
      campsApi = (alt) => { if (alt == null) cross.attr("opacity", 0); else cross.attr("y1", y(alt)).attr("y2", y(alt)).attr("opacity", 1); };
    });
  }

  // ------------------------------------------------------------- calendar
  const dayLabel = (doy) => {
    const t = new Date(2023, 0, doy);
    return d3.timeFormat("%b %-d")(t);
  };
  function drawCalendar() {
    // Spring and autumn windows are months apart, so "all seasons" shows spring, where 88% of expeditions are.
    const seasonNote = state.season === "All" ? "Spring only. " : "";
    const pool = rowsFiltered({ ignoreSide: true }).filter((r) => r.success && r.smt && (state.season !== "All" || r.season === "Spring"));
    const hint = document.getElementById("m2-calendar-hint");
    if (!pool.length) {
      hint.textContent = "First summit day of each successful expedition.";
      mount(document.getElementById("m2-calendar"), 300, (svg, w, h) => U.emptyNote(svg, w, h, "No dated summits under these filters."));
      return;
    }
    const q = pool.map((r) => r.smt).sort(d3.ascending);
    const lo = d3.quantileSorted(q, .25), hi = d3.quantileSorted(q, .75);
    hint.textContent = `${seasonNote}First summit day of each successful expedition (n = ${fmt.int(pool.length)}), by year. Half of these fall between ${dayLabel(Math.round(lo))} and ${dayLabel(Math.round(hi))}.`;
    const yMin = Math.floor(d3.quantileSorted(q, .01)) - 2, yMax = Math.ceil(d3.quantileSorted(q, .99)) + 2;
    const shown = pool.filter((r) => r.smt >= yMin && r.smt <= yMax);
    const y0 = Math.max(1990, d3.min(shown, (r) => r.year)), y1 = d3.max(shown, (r) => r.year);
    const sides = ["South", "North"];
    mount(document.getElementById("m2-calendar"), 400, (svg, w, h) => {
      const m = { top: 30, right: 8, bottom: 24, left: 52 };
      const gap = 18;
      const fh = (h - m.top - m.bottom - gap) / 2;
      const xs = d3.scaleBand().domain(d3.range(y0, y1 + 1)).range([m.left, w - m.right]).padding(.04);
      const counts = d3.rollups(shown, (v) => v.length, (r) => r.side, (r) => r.year, (r) => r.smt);
      const max = d3.max(counts, ([, a]) => d3.max(a, ([, b]) => d3.max(b, ([, c]) => c))) || 1;
      const color = U.sequential(max);
      const g = svg.append("g");
      U.gradientLegend(svg, w - 136, 0, 130, color, [0, max], [[0, "1"], [1, max + " expeditions"]]);
      sides.forEach((side, i) => {
        const top = m.top + i * (fh + gap);
        const ys = d3.scaleLinear().domain([yMin, yMax + 1]).range([top, top + fh]);
        g.append("rect").attr("x", m.left).attr("y", top).attr("width", w - m.left - m.right).attr("height", fh).attr("fill", "#faf8f4");
        g.append("text").attr("x", 0).attr("y", top + 11).attr("font-size", 11.5).attr("font-weight", 600).attr("fill", COLORS.ink).text(side);
        ys.ticks(4).filter((t) => Number.isInteger(t)).forEach((t) => g.append("text").attr("x", m.left - 6).attr("y", ys(t) + 8).attr("text-anchor", "end").attr("font-size", 10).attr("fill", COLORS.muted).text(dayLabel(t)));
        const entry = counts.find(([s]) => s === side);
        if (!entry) return;
        entry[1].forEach(([year, days]) => days.forEach(([doy, c]) => {
          if (year < y0) return;
          g.append("rect").attr("x", xs(year)).attr("width", xs.bandwidth()).attr("y", ys(doy)).attr("height", Math.max(1.5, ys(doy + 1) - ys(doy) - .5)).attr("fill", color(c))
            .call((s) => withTip(s, `<strong>${dayLabel(doy)}, ${year} · ${side}</strong><br>${fmt.int(c)} expedition${c === 1 ? "" : "s"} first summited`));
        }));
      });
      const ticks = xs.domain().filter((yr) => yr % 5 === 0);
      U.axisX(g, xs, h - m.bottom, { values: ticks });
    });
  }

  // ---------------------------------------------------------- base camp windows
  const BC_WINDOWS = [
    { lo: 0, hi: 95, label: "Before Apr 6" }, { lo: 96, hi: 105, label: "Apr 6–15" },
    { lo: 106, hi: 115, label: "Apr 16–25" }, { lo: 116, hi: 366, label: "After Apr 25" },
  ];
  function drawBc() {
    const pool = rowsFiltered().filter((r) => r.bc && r.season === "Spring");
    const data = BC_WINDOWS.map((b) => {
      const v = pool.filter((r) => r.bc >= b.lo && r.bc <= b.hi);
      return { ...b, n: v.length, k: v.filter((r) => r.success).length };
    });
    document.getElementById("m2-bc-hint").textContent = "Expedition success by base camp arrival date, spring only, under the current filters.";
    mount(document.getElementById("m2-bc"), 400, (svg, w, h) => {
      if (!pool.length) { U.emptyNote(svg, w, h, "No spring expeditions with a base camp date here."); return; }
      const m = { top: 14, right: 10, bottom: 46, left: 42 };
      const x = d3.scaleBand().domain(data.map((d) => d.label)).range([m.left, w - m.right]).padding(.28);
      const y = d3.scaleLinear().domain([0, 1]).range([h - m.bottom, m.top]);
      const pattern = U.hatch(svg);
      const g = svg.append("g");
      U.axisY(g, y, m.left, w - m.left - m.right, { format: d3.format(".0%"), ticks: 5 });
      data.forEach((d) => {
        const cx = x(d.label) + x.bandwidth() / 2;
        g.append("text").attr("x", cx).attr("y", h - m.bottom + 16).attr("text-anchor", "middle").attr("font-size", w < 340 ? 9.5 : 11).attr("fill", COLORS.ink).text(d.label);
        g.append("text").attr("x", cx).attr("y", h - m.bottom + 31).attr("text-anchor", "middle").attr("font-size", 10.5).attr("fill", COLORS.muted).text(`n=${fmt.int(d.n)}`);
        if (!d.n) return;
        const rate = d.k / d.n, [lo, hi] = wilson(d.k, d.n);
        const bar = g.append("rect").attr("x", x(d.label)).attr("width", x.bandwidth()).attr("y", y(rate)).attr("height", y(0) - y(rate)).attr("rx", 3).attr("fill", d.n < 10 ? pattern : COLORS.slate);
        withTip(bar, `<strong>${d.label}</strong><br>${fmt.int(d.k)} of ${fmt.int(d.n)} expeditions (${fmt.pct(rate, 0)})<br><span class="tt-muted">95% range ${fmt.pct(lo, 0)}–${fmt.pct(hi, 0)}</span>`);
        g.append("line").attr("x1", cx).attr("x2", cx).attr("y1", y(lo)).attr("y2", y(hi)).attr("stroke", COLORS.ink).attr("stroke-width", 1.6).attr("pointer-events", "none");
        g.append("text").attr("x", cx).attr("y", y(hi) - 6).attr("text-anchor", "middle").attr("font-size", 12).attr("font-weight", 600).attr("fill", COLORS.ink).text(fmt.pct(rate, 0));
      });
    });
  }

  // ------------------------------------------------------------- current
  function renderCurrent() {
    const box = document.getElementById("m2-current");
    const cur = D.current;
    box.innerHTML = `
      <div class="card-head">
        <div>
          <h2>${cur.label}</h2>
          <p class="hint">Kept separate from the 1921–2024 microdata: these are aggregate counts from the Department of Tourism, not expedition records.</p>
        </div>
      </div>
      <div class="current-grid">
        ${cur.items.map((it) => `
          <div class="current-item">
            <div class="v">${it.value}</div>
            <div class="l">${it.label}</div>
            <div class="n">${it.note}</div>
          </div>`).join("")}
      </div>
      <div class="mini-chart">
        <p class="hint" style="margin:0 0 6px">Summits per year from the dataset (members plus hired staff), with the 2026 news figure as a hollow marker. The 2026 count comes from a different source and is not part of the records.</p>
        <div class="chart" id="m2-current-chart"></div>
      </div>
      <div class="current-src">
        ${cur.sources.map((s) => `<a href="${s.url}" target="_blank" rel="noopener">${s.publisher} · ${s.date}</a>`).join("")}
      </div>`;
    const data = D.yearly.filter((d) => d.year >= 2005).map((d) => ({ year: d.year, v: d.summits + d.summitsHired }));
    mount(document.getElementById("m2-current-chart"), 150, (svg, w, h) => {
      const m = { top: 14, right: 12, bottom: 22, left: 40 };
      const x = d3.scaleBand().domain(d3.range(2005, 2027)).range([m.left, w - m.right]).padding(.2);
      const y = d3.scaleLinear().domain([0, 1100]).range([h - m.bottom, m.top]);
      const g = svg.append("g");
      U.axisY(g, y, m.left, w - m.left - m.right, { ticks: 3, format: fmt.int });
      U.axisX(g, x, h - m.bottom, { values: [2005, 2010, 2015, 2020, 2026] });
      g.selectAll("rect").data(data).join("rect").attr("x", (d) => x(d.year)).attr("width", x.bandwidth()).attr("y", (d) => y(d.v)).attr("height", (d) => y(0) - y(d.v)).attr("rx", 2).attr("fill", COLORS.slate)
        .call((s) => withTip(s, (d) => `<strong>${d.year}</strong><br>${fmt.int(d.v)} summits in the dataset`));
      g.append("rect").attr("x", x(2026)).attr("width", x.bandwidth()).attr("y", y(1008)).attr("height", y(0) - y(1008)).attr("rx", 2).attr("fill", "#fff").attr("stroke", COLORS.ink).attr("stroke-width", 1.6).attr("stroke-dasharray", "3 2")
        .call((s) => withTip(s, `<strong>2026 spring</strong><br>1,008 summits (news report)<br><span class="tt-muted">Not in the dataset</span>`));
    });
  }

  function buildFindings() {
    const E = window.EVEREST_PLAN.expect;
    const r = (x) => fmt.pct(x.k / x.n, 0);
    const w = E.bcWindows;
    const rates = w.map((b) => b.k / b.n);
    const nineties = (side) => PD.total(PD.rows.filter((q) => !q.closure && q.side === side && q.year >= 1990 && q.year <= 1999));
    U.findings("m2-findings", [
      {
        id: "H4", title: "Is the south side better for members?", verdict: "Not stable",
        text: () => `Members in the 1990s: south ${r(nineties("South"))}, north ${r(nineties("North"))}. In 2020–24: south ${r(E.members2024.South)}, north ${r(E.members2024.North)}, but on only ${fmt.int(E.members2024.North.n)} north members.`,
        apply: () => { setFilters({ side: "All", season: "Spring", route: "standard", period: "all", family: null }); U.spotlight("m2-card-gap"); },
      },
      {
        id: "H5", title: "Arriving early at base camp helps", verdict: "Not supported",
        text: () => `Spring standard-route success, 2005–24, stays between ${fmt.pct(d3.min(rates), 0)} and ${fmt.pct(d3.max(rates), 0)} across all four arrival windows. Summit days cluster far more tightly than arrival days.`,
        apply: () => { setFilters({ side: "All", season: "Spring", route: "standard", period: "d20", family: null }); U.spotlight("m2-card-bc"); },
      },
      {
        id: "H6", title: "Fewer expeditions stop high on the mountain now", verdict: "Supported",
        text: () => `Standard-route expeditions reaching 8,840 m, before 2000 vs 2016–24: south ${r(E.reach.southEarly)} → ${r(E.reach.southLate)}, north ${r(E.reach.northEarly)} → ${r(E.reach.northLate)} (recent north n = ${fmt.int(E.reach.northLate.n)}).`,
        apply: () => { setFilters({ side: "All", season: "All", route: "standard", period: "t3", family: null }); U.spotlight("m2-card-funnel"); },
      },
    ]);
  }

  function setFilters(next) {
    Object.assign(state, next);
    renderAll();
  }

  function init() {
    try { if (window.GEO) window.GEO.init(); } catch (err) { console.warn("geo view failed", err); }
    buildFindings();
    U.seg("m2-routes-mode", state.routesMode, (v) => { state.routesMode = v; drawRoutes(); });
    drawCamps();
    renderAll();
    renderCurrent();
    document.querySelectorAll("#m2-camp-side button").forEach((b) => {
      b.classList.toggle("is-active", b.dataset.side === state.campSide);
      b.addEventListener("click", () => {
        document.querySelectorAll("#m2-camp-side button").forEach((x) => x.classList.remove("is-active"));
        b.classList.add("is-active");
        state.campSide = b.dataset.side;
        drawCamps();
      });
    });
  }

  window.M2 = { init, setFilters };
})();
