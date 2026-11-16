/* Page 3 · Over time: plan through time, factor × period heat map, index chart. */
(function () {
  "use strict";

  const { fmt, COLORS, mount, wilson, withTip } = U;
  const MIN_N = 10;
  const local = { rule: "exact", picks: ["u30", "30s", "40s", "50s", "60p"], ref: 2005 };

  function periodStats(list, p) {
    return PD.total(list.filter((r) => r.year >= p.a && r.year <= p.b));
  }

  // ------------------------------------------------- plan through time
  function drawThrough() {
    const profile = M3.profile;
    const cohort = PD.cohortRows(profile, local.rule);
    const all = PD.usable();
    const series = PD.PERIODS.map((p) => ({ ...p, ...periodStats(cohort, p), all: periodStats(all, p).rate }));
    const model = M3._test.member(profile);
    const shown = series.filter((d) => d.n >= MIN_N);
    document.getElementById("m3-through-hint").innerHTML =
      `Members with the ${PD.RULES[local.rule].label}. The band is a 95% interval; hollow points have fewer than ${MIN_N} members.` +
      (shown.length ? "" : ` <b>This rule has too few records in every period, so try a wider one.</b>`);

    mount(document.getElementById("m3-through"), 340, (svg, w, h) => {
      const m = { top: 30, right: w < 560 ? 22 : 118, bottom: 44, left: 44 };
      const x = d3.scaleLinear().domain([1990, 2025]).range([m.left, w - m.right]);
      const y = d3.scaleLinear().domain([0, 1]).range([h - m.bottom, m.top]);
      const g = svg.append("g");
      U.axisY(g, y, m.left, w - m.left - m.right, { format: d3.format(".0%"), ticks: 5 });
      U.axisX(g, x, h - m.bottom, { values: d3.range(1990, 2026, 5) });

      // selected period context
      const [ra, rb] = PD.state.range;
      g.append("rect").attr("x", x(ra)).attr("width", Math.max(0, x(rb + 1) - x(ra))).attr("y", m.top).attr("height", h - m.top - m.bottom)
        .attr("fill", COLORS.plan).attr("opacity", .05);
      U.eventMarks(g, x, m.top, h - m.bottom);

      // all members
      g.append("path").datum(series.filter((d) => d.all != null))
        .attr("d", d3.line().x((d) => x(d.mid)).y((d) => y(d.all)))
        .attr("fill", "none").attr("stroke", "#a8a196").attr("stroke-width", 2);

      // model
      g.append("line").attr("x1", x(2005)).attr("x2", x(2025)).attr("y1", y(model)).attr("y2", y(model))
        .attr("stroke", COLORS.ink).attr("stroke-width", 1.6).attr("stroke-dasharray", "6 4");

      // plan band + line (only through periods with enough records)
      const line = d3.line().defined((d) => d.n >= MIN_N).x((d) => x(d.mid)).y((d) => y(d.rate));
      const band = d3.area().defined((d) => d.n >= MIN_N).x((d) => x(d.mid))
        .y0((d) => y(wilson(d.k, d.n)[0])).y1((d) => y(wilson(d.k, d.n)[1]));
      g.append("path").datum(series).attr("d", band).attr("fill", COLORS.plan).attr("opacity", .15);
      g.append("path").datum(series).attr("d", line).attr("fill", "none").attr("stroke", COLORS.plan).attr("stroke-width", 3);

      series.filter((d) => d.n > 0).forEach((d) => {
        const ok = d.n >= MIN_N;
        const dot = g.append("circle").attr("cx", x(d.mid)).attr("cy", y(d.rate)).attr("r", ok ? 6 : 4.5)
          .attr("fill", ok ? COLORS.plan : "#fff").attr("stroke", ok ? "#fff" : COLORS.plan).attr("stroke-width", 2);
        if (ok && (w > 620 || d.a % 10 === 0)) {
          g.append("text").attr("x", x(d.mid)).attr("y", y(d.rate) - 11).attr("text-anchor", "middle")
            .attr("font-size", 12).attr("font-weight", 600).attr("fill", COLORS.ink)
            .attr("paint-order", "stroke").attr("stroke", "#fff").attr("stroke-width", 3).text(fmt.pct(d.rate, 0));
        }
        withTip(dot, `<strong>${d.label}</strong><br>${fmt.int(d.k)} of ${fmt.int(d.n)} members summited<br>` +
          `${fmt.pct(d.rate, 1)} · range ${fmt.pct(wilson(d.k, d.n)[0], 0)}–${fmt.pct(wilson(d.k, d.n)[1], 0)}` +
          (ok ? "" : `<br><span class="tt-muted">Too few records to read as a trend</span>`));
      });
      // sample sizes under the axis
      series.forEach((d) => {
        g.append("text").attr("x", x(d.mid)).attr("y", h - m.bottom + 30).attr("text-anchor", "middle")
          .attr("font-size", 10.5).attr("fill", COLORS.muted).text(w > 480 || d.a % 10 === 0 ? `n=${fmt.int(d.n)}` : "");
      });

      if (w >= 560) {
        const endY = (v) => y(v) + 4;
        const last = [...series].reverse().find((d) => d.n >= MIN_N);
        const labels = [{ y: endY(model), t: `Model ${fmt.pct(model, 0)}`, c: COLORS.ink }];
        if (last) labels.push({ y: endY(last.rate), t: "This plan", c: COLORS.plan, weight: 600 });
        const lastAll = series[series.length - 1];
        labels.push({ y: endY(lastAll.all), t: "All members", c: COLORS.muted });
        labels.sort((a, b) => a.y - b.y);
        labels.forEach((l, i) => { if (i && l.y - labels[i - 1].y < 14) l.y = labels[i - 1].y + 14; });
        labels.forEach((l) => g.append("text").attr("x", x(2025) + 8).attr("y", l.y).attr("font-size", 12)
          .attr("font-weight", l.weight || 400).attr("fill", l.c === COLORS.plan ? COLORS.ink : l.c).text(l.t));
      } else {
        U.legend(g, m.left, 14, [
          { label: "This plan", color: COLORS.plan, line: true },
          { label: "All members", color: "#a8a196", line: true },
          { label: "Model", color: COLORS.ink, dash: "6 4" },
        ], { gap: 10 });
      }
    });
  }

  // ------------------------------------------------- factor × period grid
  function gridData() {
    const all = PD.usable();
    const base = PD.PERIODS.map((p) => periodStats(all, p));
    return PD.ATTRS.map((a) => {
      const rows = all.filter(a.test);
      return { a, cells: PD.PERIODS.map((p, i) => { const s = periodStats(rows, p); return { ...s, p, delta: s.n ? s.rate - base[i].rate : null, base: base[i].rate }; }) };
    });
  }

  function drawGrid() {
    const data = gridData();
    const rowH = 22;
    let groupGaps = 0;
    data.forEach((d, i) => { if (i && d.a.group !== data[i - 1].a.group) groupGaps += 1; });
    const height = 58 + data.length * rowH + groupGaps * 7;
    mount(document.getElementById("m3-grid"), height, (svg, w) => {
      const m = { top: 50, right: 4, left: w < 560 ? 124 : 158 };
      const cols = PD.PERIODS.length;
      const cw = (w - m.left - m.right) / cols;
      const color = U.diverging(.35);
      const pattern = U.hatch(svg);
      const g = svg.append("g");
      U.gradientLegend(svg, Math.max(m.left, w - 200), 0, 190, color, [-.35, .35], [[0, "−35 pts"], [.5, "average"], [1, "+35 pts"]]);
      PD.PERIODS.forEach((p, i) => {
        const inRange = p.b >= PD.state.range[0] && p.a <= PD.state.range[1];
        g.append("text").attr("x", m.left + cw * i + cw / 2).attr("y", m.top - 6).attr("text-anchor", "middle")
          .attr("font-size", cw < 50 ? 9.5 : 11).attr("font-weight", inRange ? 600 : 400)
          .attr("fill", inRange ? COLORS.ink : COLORS.muted).text(p.label);
      });
      let y = m.top;
      data.forEach((d, ri) => {
        if (ri && d.a.group !== data[ri - 1].a.group) y += 7;
        const onPlan = d.a.plan(M3.profile);
        const picked = local.picks.includes(d.a.id);
        const row = g.append("g").style("cursor", "pointer");
        row.append("rect").attr("x", 0).attr("y", y).attr("width", w).attr("height", rowH).attr("fill", "transparent");
        if (onPlan) row.append("circle").attr("cx", 6).attr("cy", y + rowH / 2).attr("r", 4).attr("fill", COLORS.plan);
        row.append("text").attr("x", 16).attr("y", y + rowH / 2 + 4).attr("font-size", 12)
          .attr("font-weight", onPlan || picked ? 600 : 400).attr("fill", COLORS.ink)
          .text(d.a.label + (picked ? " ·" : ""));
        d.cells.forEach((c, i) => {
          const sparse = c.n < MIN_N;
          const fill = sparse ? pattern : color(c.delta);
          const cell = row.append("rect").attr("x", m.left + cw * i + 1).attr("y", y + 1).attr("width", cw - 2).attr("height", rowH - 2).attr("rx", 3).attr("fill", fill);
          if (!sparse && cw >= 46) {
            row.append("text").attr("x", m.left + cw * i + cw / 2).attr("y", y + rowH / 2 + 4).attr("text-anchor", "middle")
              .attr("font-size", 11).attr("fill", U.inkOn(color(c.delta))).attr("pointer-events", "none")
              .text(d3.format("+.0f")(c.delta * 100));
          }
          withTip(cell, `<strong>${d.a.label} · ${c.p.label}</strong><br>` + (c.n
            ? `${fmt.int(c.k)} of ${fmt.int(c.n)} members (${fmt.pct(c.rate, 0)})<br>Period average ${fmt.pct(c.base, 0)}${sparse ? `<br><span class="tt-muted">Fewer than ${MIN_N} records</span>` : ""}`
            : "No records"));
        });
        row.on("click", () => {
          const id = d.a.id;
          local.picks = local.picks.includes(id) ? local.picks.filter((x) => x !== id) : [...local.picks, id].slice(-5);
          drawGrid();
          drawIndex();
        });
        y += rowH;
      });
    });
  }

  // ---------------------------------------------------------- index chart
  function drawIndex() {
    const all = PD.usable();
    const picks = PD.ATTRS.filter((a) => local.picks.includes(a.id));
    const refP = PD.PERIODS.find((p) => p.a === local.ref);
    document.getElementById("m3-index-hint").textContent =
      `Summit share as an index, with ${refP.label} = 100. Click the chart to move the reference period; click rows in the grid above to choose up to five groups. Gaps mean fewer than ${MIN_N} records.`;
    const color = (a) => COLORS.series[PD.ATTRS.indexOf(a) % COLORS.series.length];
    const series = picks.map((a, i) => {
      const rows = all.filter(a.test);
      const ref = periodStats(rows, refP);
      return { a, c: COLORS.series[i], ok: ref.n >= MIN_N && ref.rate > 0, values: PD.PERIODS.map((p) => {
        const s = periodStats(rows, p);
        return { p, ...s, idx: ref.n >= MIN_N && ref.rate > 0 && s.n >= MIN_N ? (s.rate / ref.rate) * 100 : null };
      }) };
    });
    mount(document.getElementById("m3-index"), 310, (svg, w, h) => {
      const m = { top: 34, right: 18, bottom: 28, left: 44 };
      const x = d3.scaleLinear().domain([1992.5, 2022.5]).range([m.left, w - m.right]);
      const vals = series.flatMap((s) => s.values.map((v) => v.idx)).filter((v) => v != null);
      if (!vals.length) { U.emptyNote(svg, w, h, "Pick a group with enough records in the reference period."); return; }
      const y = d3.scaleLinear().domain([0, Math.max(120, d3.max(vals) * 1.08)]).nice().range([h - m.bottom, m.top]);
      const g = svg.append("g");
      U.axisY(g, y, m.left, w - m.left - m.right, { ticks: 5 });
      U.axisX(g, x, h - m.bottom, { values: PD.PERIODS.map((p) => p.mid), format: (v) => (w < 480 ? String(Math.floor(v)).slice(2) : PD.PERIODS.find((p) => p.mid === v).label), size: 10.5 });
      g.append("line").attr("x1", m.left).attr("x2", w - m.right).attr("y1", y(100)).attr("y2", y(100)).attr("stroke", COLORS.ink).attr("stroke-width", 1);
      g.append("line").attr("x1", x(refP.mid)).attr("x2", x(refP.mid)).attr("y1", m.top).attr("y2", h - m.bottom).attr("stroke", COLORS.plan).attr("stroke-width", 2);
      U.caption(g, x(refP.mid), m.top - 5, "reference = 100", "middle");
      const line = d3.line().defined((d) => d.idx != null).x((d) => x(d.p.mid)).y((d) => y(d.idx));
      series.forEach((s) => {
        g.append("path").datum(s.values).attr("d", line).attr("fill", "none").attr("stroke", s.c).attr("stroke-width", 2.2);
        s.values.filter((v) => v.idx != null).forEach((v) => {
          g.append("circle").attr("cx", x(v.p.mid)).attr("cy", y(v.idx)).attr("r", 4.5).attr("fill", s.c).attr("stroke", "#fff").attr("stroke-width", 1.5)
            .call((sel) => withTip(sel, `<strong>${s.a.label} · ${v.p.label}</strong><br>Index ${d3.format(".0f")(v.idx)}<br>${fmt.pct(v.rate, 0)} · ${fmt.int(v.k)} of ${fmt.int(v.n)}`));
        });
      });
      U.legend(g, m.left, 14, series.map((s) => ({ label: s.a.label + (s.ok ? "" : " (no reference)"), color: s.c, line: true })), { gap: 10 });
      // click to move the reference period; circles stay hoverable above this layer
      svg.insert("rect", ":first-child").attr("x", m.left).attr("y", m.top).attr("width", w - m.left - m.right).attr("height", h - m.top - m.bottom)
        .attr("fill", "transparent").style("cursor", "ew-resize")
        .on("click", (event) => {
          const px = d3.pointer(event)[0];
          local.ref = d3.least(PD.PERIODS, (p) => Math.abs(x(p.mid) - px)).a;
          drawIndex();
        });
    });
  }

  function render() {
    drawThrough();
    drawGrid();
    drawIndex();
  }

  // Scripts load at the end of <body>, before app.js boots, so the page is ready here.
  (function setup() {
    M3.register("time", render);
    const set = U.seg("m3-rule", local.rule, (v) => { local.rule = v; drawThrough(); });
    window.PlanTime = { setRule(v) { local.rule = v; set(v); drawThrough(); } };
  })();
})();
