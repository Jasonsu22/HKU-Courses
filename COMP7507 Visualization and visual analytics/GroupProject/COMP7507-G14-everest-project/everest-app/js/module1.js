/* Module 01 — historical evolution. A timeline brush drives every chart on the page. */
(function () {
  "use strict";

  const D = window.EVEREST_DATA;
  const PL = window.EVEREST_PLAN;
  const { fmt, COLORS, wilson, withTip, mount, el, statCard } = U;
  const FULL = [1921, 2024];
  const state = {
    range: FULL.slice(), heat: "count", decade: null, season: "count", success: "decade",
    peaks: "horizon", duration: "all", deaths: "count", ended: "share",
  };

  const inRange = (y) => y >= state.range[0] && y <= state.range[1];
  const decadeInRange = (d) => d + 9 >= state.range[0] && d <= state.range[1];
  const dimmed = (d) => (state.decade != null ? d !== state.decade : !decadeInRange(d));
  const rows = () => D.expeditions.filter((r) => inRange(r.year));
  const rangeBand = (g, x, top, bottom) => {
    if (state.range[0] === FULL[0] && state.range[1] === FULL[1]) return;
    const [a, b] = x.domain();
    g.append("rect").attr("x", x(Math.max(a, state.range[0]))).attr("y", top)
      .attr("width", Math.max(0, x(Math.min(b, state.range[1] + 1)) - x(Math.max(a, state.range[0])))).attr("height", bottom - top)
      .attr("fill", COLORS.plan).attr("opacity", .06);
  };

  function setDecade(dec) {
    state.decade = state.decade === dec ? null : dec;
    drawSuccess(); drawHeat(); drawDuration();
  }

  // ---------------------------------------------------------------- KPIs
  function renderKpis() {
    const r = rows();
    const box = document.getElementById("m1-kpis");
    const k = r.filter((x) => x.success).length;
    const deaths = d3.sum(r, (x) => x.mDeaths + x.hDeaths);
    const m = d3.sum(r, (x) => x.mDeaths);
    const ci = wilson(k, r.length);
    box.innerHTML = "";
    box.append(
      statCard({ value: fmt.int(r.length), label: "expeditions", sub: `${state.range[0]}–${state.range[1]} · Everest only` }),
      state.range[0] === FULL[0] && state.range[1] === FULL[1]
        ? statCard({ value: fmt.int(D.headline.members), label: "member records", sub: "participation rows, not unique climbers" })
        : statCard({ value: fmt.int(d3.sum(r, (x) => x.members)), label: "members on those expeditions", sub: "per expedition, not unique climbers" }),
      statCard({ value: r.length ? fmt.pct(k / r.length, 1) : "–", label: "expeditions with a summit", sub: `${fmt.int(k)} of ${fmt.int(r.length)} · 95% CI ${fmt.pct(ci[0])}–${fmt.pct(ci[1])}`, accent: true }),
      statCard({ value: fmt.int(deaths), label: "recorded deaths", sub: `${fmt.int(m)} members + ${fmt.int(deaths - m)} hired staff` })
    );
    const label = document.getElementById("m1-range-label");
    if (label) label.textContent = `Now showing ${state.range[0]}–${state.range[1]}.`;
  }

  // ------------------------------------------------------ annual + brush
  function drawAnnual() {
    const box = document.getElementById("m1-annual");
    const byYear = new Map(D.yearly.map((d) => [d.year, d]));
    mount(box, 330, (svg, w, h) => {
      const m = { top: 18, right: 14, bottom: 24, left: 46 };
      const gap = 26;
      const topH = (h - m.top - m.bottom - gap) * .55;
      const botH = h - m.top - m.bottom - gap - topH;
      const x = d3.scaleLinear().domain([FULL[0], FULL[1] + 1]).range([m.left, w - m.right]);
      const bw = Math.max(1, x(1) - x(0) - 1);
      const y1 = d3.scaleLinear().domain([0, d3.max(D.yearly, (d) => d.n)]).nice().range([m.top + topH, m.top]);
      const y2 = d3.scaleLinear().domain([0, d3.max(D.yearly, (d) => d.members)]).nice().range([m.top + topH + gap + botH, m.top + topH + gap]);
      const g = svg.append("g");
      U.axisY(g, y1, m.left, w - m.left - m.right, { format: fmt.int });
      U.axisY(g, y2, m.left, w - m.left - m.right, { format: fmt.int });
      U.caption(g, m.left, m.top - 5, "Expeditions");
      U.caption(g, m.left, m.top + topH + gap - 5, "Members");
      const fill = (d, on, off) => (inRange(d.year) ? on : off);
      const bars1 = g.selectAll("rect.a").data(D.yearly).join("rect").attr("class", "a")
        .attr("x", (d) => x(d.year)).attr("width", bw).attr("y", (d) => y1(d.n)).attr("height", (d) => y1(0) - y1(d.n)).attr("rx", 1);
      const bars2 = g.selectAll("rect.b").data(D.yearly).join("rect").attr("class", "b")
        .attr("x", (d) => x(d.year)).attr("width", bw).attr("y", (d) => y2(d.members)).attr("height", (d) => y2(0) - y2(d.members)).attr("rx", 1);
      const paint = () => {
        bars1.attr("fill", (d) => fill(d, COLORS.slate, "#d6cfc3"));
        bars2.attr("fill", (d) => fill(d, COLORS.slate, "#d6cfc3"));
      };
      paint();
      U.axisX(g, x, m.top + topH + gap + botH, { ticks: Math.round(w / 90) });
      U.eventMarks(g.append("g").attr("pointer-events", "none"), x, m.top, m.top + topH + gap + botH);

      const brush = d3.brushX().extent([[m.left, m.top], [w - m.right, m.top + topH + gap + botH]])
        .on("end", (event) => {
          if (!event.sourceEvent) return;
          if (!event.selection) { setRange(FULL.slice()); return; }
          const a = Math.max(FULL[0], Math.round(x.invert(event.selection[0])));
          const b = Math.min(FULL[1], Math.max(a, Math.round(x.invert(event.selection[1])) - 1));
          setRange([a, b]);
        });
      const gb = svg.append("g").call(brush);
      gb.selectAll(".selection").attr("fill", COLORS.plan).attr("fill-opacity", .07).attr("stroke", COLORS.plan).attr("stroke-width", 1.4);
      if (state.range[0] !== FULL[0] || state.range[1] !== FULL[1]) gb.call(brush.move, [x(state.range[0]), x(state.range[1] + 1)]);
      gb.select(".overlay").on("mousemove.tip", (event) => {
        const yr = Math.floor(x.invert(d3.pointer(event, svg.node())[0]));
        const d = byYear.get(yr);
        if (!d) { U.tipShow(event, `<strong>${yr}</strong><br>No recorded expeditions`); return; }
        U.tipShow(event, `<strong>${d.year}</strong><br>${fmt.int(d.n)} expedition${d.n === 1 ? "" : "s"} · ${fmt.int(d.k)} with a summit<br>${fmt.int(d.members)} members · ${fmt.int(d.hired)} hired<br><span class="tt-muted">Drag to choose a period</span>`);
      }).on("mouseleave.tip", U.tipHide);
    });
  }

  // ------------------------------------------------------ season stack
  function drawSeason() {
    const seasons = ["Spring", "Autumn", "Winter", "Summer"];
    const years = d3.range(1950, 2025);
    const by = d3.rollup(D.expeditions, (v) => v.length, (r) => r.year, (r) => r.season);
    const data = years.map((y) => {
      const o = { year: y };
      seasons.forEach((s) => { o[s] = (by.get(y) && by.get(y).get(s)) || 0; });
      o.total = d3.sum(seasons, (s) => o[s]);
      return o;
    });
    mount(document.getElementById("m1-season"), 320, (svg, w, h) => {
      const m = { top: 26, right: 12, bottom: 26, left: 40 };
      const a = Math.max(1950, state.range[0]), b = Math.max(a + 1, state.range[1]);
      const x = d3.scaleLinear().domain([a, b + 1]).range([m.left, w - m.right]);
      const share = state.season === "share";
      const shown = data.filter((d) => d.year >= a && d.year <= b);
      const y = d3.scaleLinear().domain(share ? [0, 1] : [0, d3.max(shown, (d) => d.total) || 1]).nice().range([h - m.bottom, m.top]);
      const stack = d3.stack().keys(seasons).value((d, k) => (share ? (d.total ? d[k] / d.total : 0) : d[k]))(shown);
      const g = svg.append("g");
      U.axisY(g, y, m.left, w - m.left - m.right, { format: share ? d3.format(".0%") : fmt.int });
      stack.forEach((layer) => {
        g.selectAll(null).data(layer).join("rect")
          .attr("x", (d) => x(d.data.year)).attr("width", Math.max(1, x(1) - x(0) - 1))
          .attr("y", (d) => y(d[1])).attr("height", (d) => Math.max(0, y(d[0]) - y(d[1])))
          .attr("fill", COLORS.season[layer.key])
          .call((s) => withTip(s, (d) => `<strong>${d.data.year} · ${layer.key}</strong><br>${fmt.int(d.data[layer.key])} of ${fmt.int(d.data.total)} expeditions`));
      });
      U.axisX(g, x, h - m.bottom, { ticks: Math.round(w / 90) });
      U.legend(g, m.left, 13, seasons.map((s) => ({ label: s, color: COLORS.season[s] })));
    });
  }

  // ------------------------------------------------------------- heatmap
  function drawHeat() {
    document.getElementById("m1-heat-hint").textContent = state.heat === "count"
      ? "Number of expeditions (square-root colour scale). Fewer than 5 is hatched. Click a decade to link it across charts."
      : "Share of expeditions with a summit. Fewer than 5 is hatched. Click a decade to link it across charts.";
    mount(document.getElementById("m1-heat"), 320, (svg, w, h) => {
      const m = { top: 36, right: 6, bottom: 24, left: 56 };
      const decades = [...new Set(D.seasonDecade.map((d) => d.decade))];
      const seasons = ["Spring", "Autumn", "Winter", "Summer"];
      const lookup = new Map(D.seasonDecade.map((d) => [d.decade + "|" + d.season, d]));
      const x = d3.scaleBand().domain(decades).range([m.left, w - m.right]).padding(.06);
      const y = d3.scaleBand().domain(seasons).range([m.top, h - m.bottom]).padding(.08);
      const maxN = d3.max(D.seasonDecade, (d) => d.n);
      const colorN = U.sequential(Math.sqrt(maxN));
      const colorR = U.sequential(1);
      const pattern = U.hatch(svg);
      const g = svg.append("g");
      seasons.forEach((s) => g.append("text").attr("x", m.left - 8).attr("y", y(s) + y.bandwidth() / 2 + 4).attr("text-anchor", "end").attr("font-size", 12).attr("fill", COLORS.ink).text(s));
      decades.forEach((d) => g.append("text").attr("x", x(d) + x.bandwidth() / 2).attr("y", h - 8).attr("text-anchor", "middle").attr("font-size", 10.5)
        .attr("fill", dimmed(d) ? COLORS.faint : COLORS.ink).text(w < 480 ? "'" + String(d).slice(2) : d + "s"));
      const cells = decades.flatMap((dec) => seasons.map((s) => lookup.get(dec + "|" + s) || { decade: dec, season: s, n: 0, k: 0 }));
      const fillOf = (d) => (state.heat === "count" ? colorN(Math.sqrt(d.n)) : colorR(d.k / d.n));
      g.selectAll("rect.cell").data(cells).join("rect").attr("class", "cell")
        .attr("x", (d) => x(d.decade)).attr("y", (d) => y(d.season)).attr("width", x.bandwidth()).attr("height", y.bandwidth()).attr("rx", 3)
        .attr("fill", (d) => (d.n === 0 ? "#fbf9f5" : d.n < 5 ? pattern : fillOf(d)))
        .attr("opacity", (d) => (dimmed(d.decade) ? .22 : 1)).style("cursor", "pointer")
        .on("click", (e, d) => setDecade(d.decade))
        .call((s) => withTip(s, (d) => (d.n
          ? `<strong>${d.season} · ${d.decade}s</strong><br>${fmt.int(d.k)} of ${fmt.int(d.n)} expeditions (${fmt.pct(d.k / d.n, 1)})`
          : `<strong>${d.season} · ${d.decade}s</strong><br>No recorded expeditions`)));
      cells.filter((d) => d.n >= 5 && x.bandwidth() > 28).forEach((d) => {
        g.append("text").attr("x", x(d.decade) + x.bandwidth() / 2).attr("y", y(d.season) + y.bandwidth() / 2 + 4).attr("text-anchor", "middle")
          .attr("font-size", 10.5).attr("pointer-events", "none").attr("fill", U.inkOn(fillOf(d))).attr("opacity", dimmed(d.decade) ? .3 : 1)
          .text(state.heat === "count" ? fmt.int(d.n) : d3.format(".0%")(d.k / d.n));
      });
      if (state.heat === "count") U.gradientLegend(svg, w - 136, 2, 130, colorN, [0, Math.sqrt(maxN)], [[0, "0"], [1, fmt.int(maxN)]]);
      else U.gradientLegend(svg, w - 136, 2, 130, colorR, [0, 1], [[0, "0%"], [1, "100%"]]);
    });
  }

  // ------------------------------------------------------------- success
  function drawSuccess() {
    document.getElementById("m1-success-hint").textContent = state.success === "decade"
      ? "Share of expeditions with a summit on route 1, with 95% intervals. Click a decade to link it across charts."
      : "Share of expeditions with a summit per year, with a 95% band. Years with fewer than 5 expeditions are left out.";
    mount(document.getElementById("m1-success"), 320, (svg, w, h) => {
      const m = { top: 18, right: 14, bottom: 26, left: 42 };
      const y = d3.scaleLinear().domain([0, 1]).range([h - m.bottom, m.top]);
      const g = svg.append("g");
      U.axisY(g, y, m.left, w - m.left - m.right, { format: d3.format(".0%"), ticks: 5 });
      if (state.success === "decade") {
        const data = D.decades.filter((d) => d.n >= 5);
        const x = d3.scaleBand().domain(data.map((d) => d.decade)).range([m.left, w - m.right]).padding(.3);
        const cx = (d) => x(d.decade) + x.bandwidth() / 2;
        g.selectAll("rect.bar").data(data).join("rect").attr("class", "bar")
          .attr("x", (d) => x(d.decade)).attr("width", x.bandwidth()).attr("y", (d) => y(d.k / d.n)).attr("height", (d) => y(0) - y(d.k / d.n)).attr("rx", 3)
          .attr("fill", (d) => (state.decade === d.decade ? COLORS.plan : COLORS.slate)).attr("opacity", (d) => (dimmed(d.decade) ? .22 : 1));
        g.selectAll("line.ci").data(data).join("line").attr("x1", cx).attr("x2", cx)
          .attr("y1", (d) => y(wilson(d.k, d.n)[0])).attr("y2", (d) => y(wilson(d.k, d.n)[1]))
          .attr("stroke", COLORS.ink).attr("stroke-width", 1.4).attr("opacity", (d) => (dimmed(d.decade) ? .25 : 1));
        g.selectAll("text.v").data(data).join("text").attr("x", cx).attr("y", (d) => y(wilson(d.k, d.n)[1]) - 5).attr("text-anchor", "middle")
          .attr("font-size", 11).attr("font-weight", 600).attr("fill", COLORS.ink).attr("opacity", (d) => (dimmed(d.decade) ? .35 : 1)).text((d) => fmt.pct(d.k / d.n, 0));
        U.axisX(g, x, h - m.bottom, { format: (d) => (w < 460 ? "'" + String(d).slice(2) : d + "s") });
        g.selectAll("rect.hit").data(data).join("rect").attr("x", (d) => x(d.decade)).attr("y", m.top).attr("width", x.bandwidth()).attr("height", h - m.top - m.bottom)
          .attr("fill", "transparent").style("cursor", "pointer").on("click", (e, d) => setDecade(d.decade))
          .call((s) => withTip(s, (d) => `<strong>${d.decade}s</strong><br>${fmt.int(d.k)} of ${fmt.int(d.n)} expeditions<br>${fmt.pct(d.k / d.n, 1)} · 95% CI ${fmt.pct(wilson(d.k, d.n)[0])}–${fmt.pct(wilson(d.k, d.n)[1])}`));
      } else {
        const a = Math.max(1950, state.range[0]), b = Math.max(a + 1, state.range[1]);
        const data = D.yearly.filter((d) => d.n >= 5 && d.year >= a && d.year <= b);
        const x = d3.scaleLinear().domain([a, b]).range([m.left, w - m.right]);
        if (data.length) {
          g.append("path").datum(data).attr("d", d3.area().x((d) => x(d.year)).y0((d) => y(wilson(d.k, d.n)[0])).y1((d) => y(wilson(d.k, d.n)[1])))
            .attr("fill", COLORS.slate).attr("opacity", .18);
          g.append("path").datum(data).attr("d", d3.line().x((d) => x(d.year)).y((d) => y(d.k / d.n))).attr("fill", "none").attr("stroke", COLORS.slate).attr("stroke-width", 2);
          U.eventMarks(g, x, m.top, h - m.bottom);
          g.selectAll("circle").data(data).join("circle").attr("cx", (d) => x(d.year)).attr("cy", (d) => y(d.k / d.n)).attr("r", 4).attr("fill", COLORS.slate).attr("stroke", "#fff").attr("stroke-width", 1)
            .call((s) => withTip(s, (d) => `<strong>${d.year}</strong><br>${fmt.int(d.k)} of ${fmt.int(d.n)} expeditions (${fmt.pct(d.k / d.n, 0)})`));
        }
        U.axisX(g, x, h - m.bottom, { ticks: Math.round(w / 90) });
      }
    });
  }

  // --------------------------------------------------------------- peaks
  function peakSeries(p) {
    const by = new Map(p.years.map(([y, n, k]) => [y, { n, k }]));
    const all = p.years.filter(([y]) => y >= 1980);
    const mean = d3.sum(all, (d) => d[2]) / d3.sum(all, (d) => d[1]);
    return { mean, values: d3.range(1980, 2025).map((y) => {
      let n = 0, k = 0;
      [y - 1, y, y + 1].forEach((q) => { const s = by.get(q); if (s) { n += s.n; k += s.k; } });
      return { x: y, n, k, rate: n >= 5 ? k / n : null, v: n >= 5 ? k / n - mean : null };
    }) };
  }

  function drawPeaks() {
    const peaks = [...PL.peaks].sort((a, b) => (a.id === "EVER" ? -1 : b.id === "EVER" ? 1 : b.height - a.height));
    document.getElementById("m1-peaks-hint").textContent = state.peaks === "horizon"
      ? "Three-year success on the most-attempted peaks in the database, against each peak's own 1980–2024 average. Green is above it, purple below; darker bands mean over 20 points away."
      : "Three-year success on the same peaks, indexed to 100 in 2000. Everest is highlighted.";
    const rowH = 31;
    mount(document.getElementById("m1-peaks"), Math.max(320, peaks.length * rowH + 40), (svg, w, h) => {
      const m = { top: 10, right: 14, bottom: 26, left: 92 };
      if (state.peaks === "horizon") {
        const x = d3.scaleLinear().domain([1980, 2024]).range([m.left, w - m.right]);
        const g = svg.append("g");
        rangeBand(g, x, m.top, h - m.bottom);
        peaks.forEach((p, i) => {
          const s = peakSeries(p);
          const top = m.top + i * rowH;
          g.append("text").attr("x", m.left - 8).attr("y", top + 18).attr("text-anchor", "end").attr("font-size", 12)
            .attr("font-weight", p.id === "EVER" ? 700 : 400).attr("fill", COLORS.ink).text(p.name);
          U.horizon(g, svg, { series: s.values, x, top, height: rowH - 5, step: .2 });
          g.append("rect").attr("x", m.left).attr("y", top).attr("width", w - m.left - m.right).attr("height", rowH - 5).attr("fill", "transparent")
            .on("mousemove", (event) => {
              const yr = Math.round(x.invert(d3.pointer(event, svg.node())[0]));
              const d = s.values.find((q) => q.x === yr);
              U.tipShow(event, `<strong>${p.name} · ${yr}</strong><br>` + (d && d.rate != null
                ? `${fmt.int(d.k)} of ${fmt.int(d.n)} expeditions (3 years): ${fmt.pct(d.rate, 0)}<br><span class="tt-muted">Own average ${fmt.pct(s.mean, 0)}</span>` : "Too few expeditions"));
            }).on("mouseleave", U.tipHide);
        });
        U.axisX(g, x, h - m.bottom, { ticks: Math.round(w / 110) });
      } else {
        const m2 = { ...m, left: 40, right: 82 };
        const x = d3.scaleLinear().domain([1985, 2024]).range([m2.left, w - m2.right]);
        const series = peaks.map((p) => {
          const s = peakSeries(p);
          const ref = s.values.find((q) => q.x === 2000);
          return { p, values: s.values.filter((q) => q.x >= 1985).map((q) => ({ ...q, idx: q.rate != null && ref && ref.rate ? (q.rate / ref.rate) * 100 : null })) };
        });
        const y = d3.scaleLinear().domain([0, Math.min(260, d3.max(series.flatMap((s) => s.values), (q) => q.idx) || 200)]).nice().range([h - m2.bottom, m2.top]).clamp(true);
        const g = svg.append("g");
        U.axisY(g, y, m2.left, w - m2.left - m2.right, { ticks: 5 });
        U.axisX(g, x, h - m2.bottom, { ticks: Math.round(w / 110) });
        g.append("line").attr("x1", m2.left).attr("x2", w - m2.right).attr("y1", y(100)).attr("y2", y(100)).attr("stroke", COLORS.ink);
        const line = d3.line().defined((q) => q.idx != null).x((q) => x(q.x)).y((q) => y(q.idx));
        [...series].reverse().forEach((s) => {
          const on = s.p.id === "EVER";
          g.append("path").datum(s.values).attr("d", line).attr("fill", "none").attr("stroke", on ? COLORS.plan : "#b0a99d").attr("stroke-width", on ? 3 : 1.4)
            .call((sel) => withTip(sel, `<strong>${s.p.name}</strong><br>${fmt.int(s.p.height)} m`));
        });
        const ends = series.map((s) => { const l = [...s.values].reverse().find((q) => q.idx != null); return { name: s.p.name, on: s.p.id === "EVER", y: y(l ? l.idx : 100) + 4 }; }).sort((a, b) => a.y - b.y);
        ends.forEach((e, i) => { if (i && e.y - ends[i - 1].y < 12) e.y = ends[i - 1].y + 12; });
        ends.forEach((e) => g.append("text").attr("x", w - m2.right + 6).attr("y", e.y).attr("font-size", 10.5).attr("font-weight", e.on ? 700 : 400).attr("fill", e.on ? COLORS.ink : COLORS.muted).text(e.name));
      }
    });
  }

  // ------------------------------------------------------------ duration
  function quant(vals) {
    const v = vals.slice().sort(d3.ascending);
    return { n: v.length, p10: d3.quantileSorted(v, .1), p25: d3.quantileSorted(v, .25), p50: d3.quantileSorted(v, .5), p75: d3.quantileSorted(v, .75), p90: d3.quantileSorted(v, .9) };
  }
  function drawDuration() {
    const valid = D.expeditions.filter((r) => r.daysSummit != null && r.daysSummit >= 5 && r.daysSummit <= 130);
    const decades = D.durations.map((d) => d.decade);
    const groups = state.duration === "side" ? ["South", "North"] : ["All"];
    const data = decades.flatMap((dec) => groups.map((gr) => {
      const v = valid.filter((r) => Math.floor(r.year / 10) * 10 === dec && (gr === "All" || r.side === gr)).map((r) => r.daysSummit);
      return v.length >= 5 ? { decade: dec, group: gr, ...quant(v) } : null;
    })).filter(Boolean);
    mount(document.getElementById("m1-duration"), 320, (svg, w, h) => {
      const m = { top: 24, right: 12, bottom: 26, left: 40 };
      const x = d3.scaleBand().domain(decades).range([m.left, w - m.right]).padding(.2);
      const sub = d3.scaleBand().domain(groups).range([0, x.bandwidth()]).padding(.14);
      const y = d3.scaleLinear().domain([0, d3.max(data, (d) => d.p90) * 1.05]).nice().range([h - m.bottom, m.top]);
      const g = svg.append("g");
      U.axisY(g, y, m.left, w - m.left - m.right);
      U.axisX(g, x, h - m.bottom, { format: (d) => d + "s" });
      const color = (d) => (d.group === "All" ? COLORS.slate : COLORS.side[d.group]);
      data.forEach((d) => {
        const bx = x(d.decade) + sub(d.group), bw = sub.bandwidth(), cx = bx + bw / 2;
        const box = g.append("g").attr("opacity", dimmed(d.decade) ? .22 : 1).style("cursor", "pointer");
        box.append("line").attr("x1", cx).attr("x2", cx).attr("y1", y(d.p10)).attr("y2", y(d.p90)).attr("stroke", COLORS.ink).attr("stroke-width", 1.2);
        [d.p10, d.p90].forEach((v) => box.append("line").attr("x1", cx - bw * .22).attr("x2", cx + bw * .22).attr("y1", y(v)).attr("y2", y(v)).attr("stroke", COLORS.ink).attr("stroke-width", 1.2));
        box.append("rect").attr("x", bx).attr("width", bw).attr("y", y(d.p75)).attr("height", Math.max(1, y(d.p25) - y(d.p75))).attr("fill", color(d)).attr("rx", 2);
        box.append("line").attr("x1", bx).attr("x2", bx + bw).attr("y1", y(d.p50)).attr("y2", y(d.p50)).attr("stroke", "#fff").attr("stroke-width", 2.2);
        if (groups.length === 1) box.append("text").attr("x", cx).attr("y", y(d.p90) - 5).attr("text-anchor", "middle").attr("font-size", 11).attr("font-weight", 600).attr("fill", COLORS.ink).text(fmt.dec1(d.p50).replace(".0", ""));
        box.append("rect").attr("x", bx).attr("width", bw).attr("y", m.top).attr("height", h - m.top - m.bottom).attr("fill", "transparent")
          .on("click", () => setDecade(d.decade))
          .call((s) => withTip(s, `<strong>${d.decade}s${d.group === "All" ? "" : " · " + d.group}</strong><br>Median ${fmt.dec1(d.p50)} days<br>Middle 50% ${fmt.dec1(d.p25)}–${fmt.dec1(d.p75)} · 10–90th ${fmt.dec1(d.p10)}–${fmt.dec1(d.p90)}<br><span class="tt-muted">n = ${fmt.int(d.n)} expeditions with a summit day</span>`));
      });
      if (groups.length === 2) U.legend(g, m.left, 14, groups.map((s) => ({ label: s, color: COLORS.side[s] })));
      else U.caption(g, m.left, 14, "Days");
    });
  }

  // ----------------------------------------------------------- structure
  function drawStructure() {
    mount(document.getElementById("m1-structure"), 356, (svg, w, h) => {
      const m = { top: 26, right: 12, bottom: 24, left: 44 };
      const gap = 24;
      const mainH = (h - m.top - m.bottom - gap) * .68;
      const a = Math.max(1950, state.range[0]), b = Math.max(a + 1, state.range[1]);
      const data = D.yearly.filter((d) => d.year >= a && d.year <= b);
      const x = d3.scaleLinear().domain([a, b + 1]).range([m.left, w - m.right]);
      const bw = Math.max(1, x(1) - x(0) - 1);
      const y = d3.scaleLinear().domain([0, d3.max(data, (d) => d.members + d.hired) || 1]).nice().range([m.top + mainH, m.top]);
      const g = svg.append("g");
      U.axisY(g, y, m.left, w - m.left - m.right, { format: d3.format(",") });
      g.selectAll("rect.m").data(data).join("rect").attr("x", (d) => x(d.year)).attr("width", bw).attr("y", (d) => y(d.members)).attr("height", (d) => y(0) - y(d.members)).attr("fill", COLORS.slate);
      g.selectAll("rect.h").data(data).join("rect").attr("x", (d) => x(d.year)).attr("width", bw).attr("y", (d) => y(d.members + d.hired)).attr("height", (d) => y(d.members) - y(d.members + d.hired) - (d.hired ? .6 : 0)).attr("fill", "#eda100");
      U.legend(g, m.left, 13, [{ label: "Members", color: COLORS.slate }, { label: "Hired staff", color: "#eda100" }]);
      const top2 = m.top + mainH + gap, bottom = h - m.bottom;
      const ratio = data.filter((d) => d.members >= 10).map((d) => ({ year: d.year, v: d.hired / d.members }));
      const y2 = d3.scaleLinear().domain([0, Math.max(2, d3.max(ratio, (d) => d.v) || 2)]).nice().range([bottom, top2]);
      U.axisY(g, y2, m.left, w - m.left - m.right, { ticks: 3, format: d3.format(".1f") });
      U.caption(g, m.left, top2 - 6, "Hired staff per member");
      g.append("path").datum(ratio).attr("d", d3.line().x((d) => x(d.year + .5)).y((d) => y2(d.v))).attr("fill", "none").attr("stroke", COLORS.ink).attr("stroke-width", 2);
      U.axisX(g, x, bottom, { ticks: Math.round(w / 90) });
      g.selectAll("rect.hit").data(data).join("rect").attr("x", (d) => x(d.year)).attr("y", m.top).attr("width", x(1) - x(0)).attr("height", bottom - m.top).attr("fill", "transparent")
        .call((s) => withTip(s, (d) => `<strong>${d.year}</strong><br>${fmt.int(d.members)} members · ${fmt.int(d.hired)} hired<br><span class="tt-muted">${d.members ? fmt.dec2(d.hired / d.members) : "–"} hired per member</span>`));
    });
  }

  // ------------------------------------------------------------- oxygen
  function drawO2() {
    const years = d3.range(1965, 2025);
    const of = (drop) => {
      const pool = D.expeditions.filter((r) => !(drop && r.closure));
      const by = d3.rollup(pool, (v) => ({ n: v.length, o2: v.filter((r) => r.o2).length }), (r) => r.year);
      return years.map((y) => {
        const s = by.get(y) || { n: 0, o2: 0 };
        let n = 0, k = 0;
        d3.range(y - 2, y + 3).forEach((q) => { const t = by.get(q); if (t) { n += t.n; k += t.o2; } });
        return { year: y, n: s.n, o2: s.o2, roll: n >= 10 ? k / n : null };
      });
    };
    const all = of(false), live = of(true);
    mount(document.getElementById("m1-o2"), 240, (svg, w, h) => {
      const m = { top: 26, right: 14, bottom: 24, left: 42 };
      const a = Math.max(1965, state.range[0]), b = Math.max(a + 1, state.range[1]);
      const x = d3.scaleLinear().domain([a, b]).range([m.left, w - m.right]);
      const y = d3.scaleLinear().domain([0, 1]).range([h - m.bottom, m.top]);
      const g = svg.append("g");
      U.axisY(g, y, m.left, w - m.left - m.right, { format: d3.format(".0%") });
      U.axisX(g, x, h - m.bottom, { ticks: Math.round(w / 90) });
      U.eventMarks(g, x, m.top, h - m.bottom);
      const clip = (d) => d.year >= a && d.year <= b;
      const r = d3.scaleSqrt().domain([0, 100]).range([1.5, 6]);
      g.selectAll("circle").data(all.filter((d) => clip(d) && d.n)).join("circle").attr("cx", (d) => x(d.year)).attr("cy", (d) => y(d.o2 / d.n)).attr("r", (d) => r(d.n))
        .attr("fill", "#b8b2a7").attr("opacity", .85)
        .call((s) => withTip(s, (d) => `<strong>${d.year}</strong><br>${fmt.int(d.o2)} of ${fmt.int(d.n)} expeditions used oxygen (${fmt.pct(d.o2 / d.n, 0)})`));
      const line = d3.line().defined((d) => d.roll != null).x((d) => x(d.year)).y((d) => y(d.roll));
      g.append("path").datum(all.filter(clip)).attr("d", line).attr("fill", "none").attr("stroke", COLORS.slate).attr("stroke-width", 2.2);
      g.append("path").datum(live.filter(clip)).attr("d", line).attr("fill", "none").attr("stroke", COLORS.plan).attr("stroke-width", 2).attr("stroke-dasharray", "5 4");
      U.legend(g, m.left, 13, [{ label: "All expeditions, 5-year average", color: COLORS.slate, line: true }, { label: "Excluding 2014–15 closures", color: COLORS.plan, dash: "5 4" }]);
    });
  }

  // ------------------------------------------------------------- deaths
  function drawDeaths() {
    const mode = state.deaths;
    const hints = {
      count: "Member and hired-staff deaths per decade.",
      members: "Member deaths per 1,000 members on those expeditions.",
      hired: "Hired-staff deaths per 1,000 hired staff on those expeditions.",
      summits: "All recorded deaths per 100 people who reached the summit. The story changes with the denominator.",
    };
    document.getElementById("m1-deaths-hint").textContent = hints[mode];
    mount(document.getElementById("m1-deaths"), 286, (svg, w, h) => {
      const m = { top: 24, right: 12, bottom: 26, left: 42 };
      const data = D.decades.filter((d) => d.n >= 5 && d.decade >= 1950);
      const value = (d) => {
        if (mode === "members") return d.members ? (d.mDeaths / d.members) * 1000 : null;
        if (mode === "hired") return d.hired ? (d.hDeaths / d.hired) * 1000 : null;
        if (mode === "summits") { const s = d.summits + d.summitsHired; return s ? ((d.mDeaths + d.hDeaths) / s) * 100 : null; }
        return d.mDeaths + d.hDeaths;
      };
      const x = d3.scaleBand().domain(data.map((d) => d.decade)).range([m.left, w - m.right]).padding(.26);
      const y = d3.scaleLinear().domain([0, d3.max(data, value) * 1.12 || 1]).nice().range([h - m.bottom, m.top]);
      const g = svg.append("g");
      U.axisY(g, y, m.left, w - m.left - m.right);
      U.axisX(g, x, h - m.bottom, { format: (d) => (w < 460 ? "'" + String(d).slice(2) : d + "s") });
      const op = (d) => (decadeInRange(d.decade) ? 1 : .22);
      if (mode === "count") {
        g.selectAll("rect.m").data(data).join("rect").attr("x", (d) => x(d.decade)).attr("width", x.bandwidth()).attr("y", (d) => y(d.mDeaths)).attr("height", (d) => y(0) - y(d.mDeaths)).attr("fill", COLORS.slate).attr("opacity", op);
        g.selectAll("rect.h").data(data).join("rect").attr("x", (d) => x(d.decade)).attr("width", x.bandwidth()).attr("y", (d) => y(d.mDeaths + d.hDeaths)).attr("height", (d) => Math.max(0, y(d.mDeaths) - y(d.mDeaths + d.hDeaths) - 1)).attr("fill", "#eda100").attr("opacity", op);
        U.legend(g, m.left, 13, [{ label: "Members", color: COLORS.slate }, { label: "Hired staff", color: "#eda100" }]);
      } else {
        g.selectAll("rect.v").data(data.filter((d) => value(d) != null)).join("rect").attr("x", (d) => x(d.decade)).attr("width", x.bandwidth())
          .attr("y", (d) => y(value(d))).attr("height", (d) => y(0) - y(value(d))).attr("rx", 3).attr("fill", COLORS.slate).attr("opacity", op);
      }
      g.selectAll("text.v").data(data.filter((d) => value(d) != null)).join("text").attr("x", (d) => x(d.decade) + x.bandwidth() / 2).attr("y", (d) => y(value(d)) - 5)
        .attr("text-anchor", "middle").attr("font-size", 11).attr("font-weight", 600).attr("fill", COLORS.ink).attr("opacity", op)
        .text((d) => (mode === "count" ? fmt.int(value(d)) : fmt.dec1(value(d))));
      g.selectAll("rect.hit").data(data).join("rect").attr("x", (d) => x(d.decade)).attr("y", m.top).attr("width", x.bandwidth()).attr("height", h - m.top - m.bottom).attr("fill", "transparent")
        .call((s) => withTip(s, (d) => `<strong>${d.decade}s</strong><br>${fmt.int(d.mDeaths)} member and ${fmt.int(d.hDeaths)} hired deaths<br>${fmt.int(d.members)} members · ${fmt.int(d.hired)} hired<br><span class="tt-muted">${fmt.int(d.summits + d.summitsHired)} reached the summit</span>`));
    });
  }

  // ---------------------------------------------------------- how it ended
  const END_ORDER = ["Summit", "Weather & conditions", "Illness & exhaustion", "Accident", "Logistics & difficulty", "Season closure", "Other / unknown"];
  function drawEnded() {
    const periods = d3.range(1975, 2021, 5);
    const data = periods.map((p) => {
      const list = D.expeditions.filter((r) => r.year >= p && r.year <= p + 4);
      const o = { p, n: list.length };
      END_ORDER.forEach((c) => { o[c] = list.filter((r) => r.end === c).length; });
      return o;
    });
    mount(document.getElementById("m1-ended"), 340, (svg, w, h) => {
      const m = { top: 64, right: 10, bottom: 26, left: 42 };
      const x = d3.scaleBand().domain(periods).range([m.left, w - m.right]).padding(.14);
      const share = state.ended === "share";
      const y = d3.scaleLinear().domain(share ? [0, 1] : [0, d3.max(data, (d) => d.n)]).nice().range([h - m.bottom, m.top]);
      const g = svg.append("g");
      U.axisY(g, y, m.left, w - m.left - m.right, { format: share ? d3.format(".0%") : fmt.int });
      U.axisX(g, x, h - m.bottom, { format: (d) => (w < 560 ? "'" + String(d).slice(2) : `${d}–${String(d + 4).slice(2)}`), size: w < 620 ? 9.5 : 10.5 });
      d3.stack().keys(END_ORDER).value((d, k) => (share ? d[k] / d.n : d[k]))(data).forEach((layer) => {
        g.selectAll(null).data(layer).join("rect").attr("x", (d) => x(d.data.p)).attr("width", x.bandwidth())
          .attr("y", (d) => y(d[1])).attr("height", (d) => Math.max(0, y(d[0]) - y(d[1]) - (d[1] > d[0] ? 1 : 0))).attr("fill", COLORS.end[layer.key])
          .attr("opacity", (d) => (d.data.p + 4 >= state.range[0] && d.data.p <= state.range[1] ? 1 : .25))
          .call((s) => withTip(s, (d) => `<strong>${d.data.p}–${String(d.data.p + 4).slice(2)} · ${layer.key}</strong><br>${fmt.int(d.data[layer.key])} of ${fmt.int(d.data.n)} expeditions (${fmt.pct(d.data[layer.key] / d.data.n, 0)})`));
      });
      // wrapped legend: two rows above the plot
      const perRow = w < 520 ? 3 : 4;
      d3.range(0, END_ORDER.length, perRow).forEach((i, r) => {
        U.legend(g, m.left, 13 + r * 17, END_ORDER.slice(i, i + perRow).map((c) => ({ label: c, color: COLORS.end[c] })), { gap: 8 });
      });
    });
  }

  function drawNet() {
    const a = Math.max(state.range[0], 1990);
    const list = D.expeditions.filter((r) => r.year >= a && r.year <= state.range[1]);
    window.OperatorNet.draw(list, `${a}–${state.range[1]}`);
  }

  // --------------------------------------------------------------- range
  function drawLinked() {
    renderKpis();
    drawSeason(); drawHeat(); drawSuccess(); drawPeaks(); drawDuration();
    drawStructure(); drawO2(); drawDeaths(); drawEnded(); drawNet();
  }
  function setRange(r) {
    state.range = r;
    state.decade = null;
    renderChips();
    drawAnnual();
    drawLinked();
    Store.writeParams({ from: r[0] === FULL[0] ? null : r[0], to: r[1] === FULL[1] ? null : r[1] });
  }

  function renderChips() {
    const box = document.getElementById("m1-era-chips");
    const opts = [
      { label: "All years", value: FULL },
      { label: "1950–1989", value: [1950, 1989] },
      { label: "1990–2004", value: [1990, 2004] },
      { label: "2005–2024", value: [2005, 2024] },
    ];
    box.innerHTML = "";
    opts.forEach((o) => {
      const b = el("button", { class: "chip" + (o.value.join() === state.range.join() ? " is-active" : "") }, o.label);
      b.addEventListener("click", () => setRange(o.value.slice()));
      box.appendChild(b);
    });
  }

  function buildFindings() {
    const E = PL.expect;
    const r = (x) => fmt.pct(x.k / x.n, 0);
    const pts = E.peaks;
    const per = (x) => ({ m: (x.mDeaths / x.members) * 1000, s: ((x.mDeaths + x.hDeaths) / x.summits) * 100 });
    const ra = per(E.risk.early), rl = per(E.risk.late), rt = per(E.risk.tens);
    const ratio = (x) => d3.format(".2f")(x.hired / x.members);
    U.findings("m1-findings", [
      {
        id: "H1", title: "Success rose everywhere", verdict: "Partly rejected",
        text: () => `Before 1990 vs 2020–24: Everest ${r(pts.EVER.early)} → ${r(pts.EVER.late)}, Lhotse ${r(pts.LHOT.early)} → ${r(pts.LHOT.late)}, Manaslu ${r(pts.MANA.early)} → ${r(pts.MANA.late)}, but Baruntse ${r(pts.BARU.early)} → ${r(pts.BARU.late)} (only ${pts.BARU.late.n} recent expeditions).`,
        apply: () => { setPeaks("horizon"); U.spotlight("m1-card-peaks"); },
      },
      {
        id: "H2", title: "Climbing has become much safer", verdict: "Depends on the denominator",
        text: () => `Before 1990 vs 2020–24: deaths per 100 summiters fell from ${fmt.dec1(ra.s)} to ${fmt.dec1(rl.s)}, but member deaths per 1,000 members only fell from ${fmt.dec1(ra.m)} to ${fmt.dec1(rl.m)}, above the 2010s (${fmt.dec1(rt.m)}).`,
        apply: () => { setDeaths("summits"); U.spotlight("m1-card-deaths"); },
      },
      {
        id: "H3", title: "More hired support is what drives success", verdict: "Mixed",
        text: () => `Hired staff per member rose from ${ratio(E.hiredPerMember.nineties)} in the 1990s to ${ratio(E.hiredPerMember.late)} in 2020–24, alongside rising success. Rising together isn't proof of cause, so page 3 compares support levels within each period.`,
        apply: () => { setRange([1990, 2024]); U.spotlight("m1-card-structure"); },
      },
    ]);
  }

  let setPeaks = () => {}, setDeaths = () => {};

  function init() {
    const q = Store.readParams();
    if (q.has("from") || q.has("to")) {
      const a = Math.max(FULL[0], +q.get("from") || FULL[0]), b = Math.min(FULL[1], +q.get("to") || FULL[1]);
      if (a <= b) state.range = [a, b];
    }
    renderChips();
    buildFindings();
    drawAnnual();
    U.seg("m1-season-mode", state.season, (v) => { state.season = v; drawSeason(); });
    U.seg("m1-heat-toggle", state.heat, (v) => { state.heat = v; drawHeat(); });
    U.seg("m1-success-mode", state.success, (v) => { state.success = v; drawSuccess(); });
    const sp = U.seg("m1-peaks-mode", state.peaks, (v) => { state.peaks = v; drawPeaks(); });
    setPeaks = (v) => { state.peaks = v; sp(v); drawPeaks(); };
    U.seg("m1-duration-mode", state.duration, (v) => { state.duration = v; drawDuration(); });
    const sd = U.seg("m1-deaths-mode", state.deaths, (v) => { state.deaths = v; drawDeaths(); });
    setDeaths = (v) => { state.deaths = v; sd(v); drawDeaths(); };
    U.seg("m1-ended-mode", state.ended, (v) => { state.ended = v; drawEnded(); });
    window.OperatorNet.setup(drawNet);
    drawLinked();
  }

  window.M1 = { init };
})();
