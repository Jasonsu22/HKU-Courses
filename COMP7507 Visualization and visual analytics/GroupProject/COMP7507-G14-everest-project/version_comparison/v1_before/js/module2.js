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
  ];
  const rangeOf = (p) => ({
    all: [1900, 2100], pre: [1900, 1989], t1: [1990, 2014],
    t2: [2015, 2019], t3: [2020, 2024],
  }[p] || [1900, 2100]);

  const state = {
    side: "All", season: "All", period: "all", route: "All", campSide: "both",
  };

  // Shareable filters: ?side=North&season=Spring&period=t3&route=standard&camp=north
  (function readQuery() {
    const q = new URLSearchParams(location.search);
    const pick = (key, allowed) => {
      const v = q.get(key);
      if (v && allowed.includes(v)) state[key] = v;
    };
    pick("side", ["All", "South", "North"]);
    pick("season", ["All", "Spring", "Autumn", "Winter", "Summer"]);
    pick("period", PERIODS.map((p) => p.value));
    pick("route", ["All", "standard", "other"]);
    pick("camp", ["south", "north", "both"]);
  })();

  function rowsFiltered({ ignoreSide = false } = {}) {
    const [lo, hi] = rangeOf(state.period);
    return D.expeditions.filter((r) => {
      if (!ignoreSide && state.side !== "All" && r.side !== state.side) return false;
      if (state.season !== "All" && r.season !== state.season) return false;
      if (state.route === "standard" && !r.standard) return false;
      if (state.route === "other" && r.standard) return false;
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
    const label = `${state.side === "All" ? "Both sides" : state.side + " side"} · ${state.season === "All" ? "all seasons" : state.season} · ${
      PERIODS.find((p) => p.value === state.period).label}`;
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
        b.addEventListener("click", () => {
          state[g.key] = v;
          renderFilters();
          renderKpis();
          drawCompare();
          drawRoutes();
        });
        seg.appendChild(b);
      });
      wrap.appendChild(seg);
      box.appendChild(wrap);
    });
    const reset = el("button", { class: "ghost filter-reset" }, "Reset");
    reset.addEventListener("click", () => {
      Object.assign(state, { side: "All", season: "All", period: "all", route: "All" });
      renderFilters(); renderKpis(); drawCompare(); drawRoutes();
    });
    box.appendChild(reset);
  }

  // ------------------------------------------------------- compare grid
  const METRICS = [
    { key: "rate", title: "Summit success", fmt: (v) => fmt.pct(v, 0), sub: (s) => `n = ${fmt.int(s.n)}` },
    { key: "daysMedian", title: "Median days to summit", fmt: (v) => fmt.dec1(v), sub: (s) => `${fmt.int(s.n)} expeditions`, higherBetter: false },
    { key: "teamMedian", title: "Median team size", fmt: (v) => fmt.dec1(v), sub: (s) => `${fmt.int(s.members)} members total` },
    { key: "hiredPer10", title: "Hired staff per 10 members", fmt: (v) => fmt.dec1(v), sub: (s) => `${fmt.int(s.hired)} hired total` },
    { key: "o2share", title: "Oxygen used", fmt: (v) => fmt.pct(v, 0), sub: (s) => "share of expeditions" },
    { key: "deathsPer1000", title: "Deaths per 1,000 people", fmt: (v) => fmt.dec1(v), sub: (s) => `${fmt.int(s.deaths)} recorded deaths`, higherBetter: false },
  ];

  function drawCompare() {
    const hint = document.getElementById("m2-compare-hint");
    const south = stats(rowsFiltered({ ignoreSide: true }).filter((r) => r.side === "South"));
    const north = stats(rowsFiltered({ ignoreSide: true }).filter((r) => r.side === "North"));
    hint.textContent = `Season, period and route filters applied; side filter affects the KPIs only. South n=${fmt.int(south.n)}, north n=${fmt.int(north.n)}.`;

    mount(document.getElementById("m2-compare"), 360, (svg, w, h) => {
      const cols = 3, rows = 2;
      const gapX = 18, gapY = 14;
      const cw = (w - gapX * (cols - 1)) / cols;
      const chh = (h - gapY * (rows - 1)) / rows;
      const g = svg.append("g");

      METRICS.forEach((metric, i) => {
        const cx = (i % cols) * (cw + gapX);
        const cy = Math.floor(i / cols) * (chh + gapY);
        const cell = g.append("g").attr("transform", `translate(${cx},${cy})`);
        cell.append("rect").attr("width", cw).attr("height", chh).attr("rx", 9)
          .attr("fill", "#fbfaf7").attr("stroke", COLORS.line);

        cell.append("text").attr("x", 12).attr("y", 20).attr("font-size", 12)
          .attr("font-weight", 600).attr("fill", COLORS.ink).text(metric.title);

        const sv = south[metric.key], nv = north[metric.key];
        const isPct = metric.key === "rate" || metric.key === "o2share";
        const max = isPct ? 1 : (Math.max(sv || 0, nv || 0) * 1.15 || 1);
        const barMax = cw - 110;
        const barH = 13;
        const y0 = 44;

        [{ name: "South", v: sv, s: south, color: COLORS.south, y: y0 },
         { name: "North", v: nv, s: north, color: COLORS.north, y: y0 + 34 }].forEach((row) => {
          const label = cell.append("g").attr("transform", `translate(12,${row.y})`);
          label.append("text").attr("x", 0).attr("y", 10).attr("font-size", 10.5)
            .attr("fill", COLORS.muted).text(row.name);
          label.append("rect").attr("x", 44).attr("y", 2).attr("width", row.v ? (row.v / max) * barMax : 0)
            .attr("height", barH).attr("rx", 3).attr("fill", row.color).attr("opacity", 0.9);
          label.append("text").attr("x", 47 + (row.v ? (row.v / max) * barMax : 0)).attr("y", 12)
            .attr("font-size", 11.5).attr("font-weight", 600).attr("fill", COLORS.ink)
            .text(row.v == null ? "–" : metric.fmt(row.v));
          label.append("text").attr("x", 44).attr("y", 27).attr("font-size", 9.5)
            .attr("fill", COLORS.faint).text(row.s.n ? metric.sub(row.s) : "no records");
          label.append("rect").attr("x", -6).attr("y", -4).attr("width", cw - 8).attr("height", 42)
            .attr("fill", "transparent")
            .on("mousemove", (event) => U.tipShow(event,
              `<strong>${row.name} · ${metric.title}</strong><br>` +
              `${row.v == null ? "–" : metric.fmt(row.v)}<br>` +
              `<span class="tt-muted">${fmt.int(row.s.n)} expeditions · ${fmt.int(row.s.k)} successful<br>` +
              `${row.s.daysMedian ? "median " + fmt.dec1(row.s.daysMedian) + " days to summit" : "no summit-day records"}</span>`))
            .on("mouseleave", U.tipHide);
        });
      });
    });
  }

  // ------------------------------------------------------------- routes
  function drawRoutes() {
    const rows = rowsFiltered();
    const byRoute = d3.rollups(rows, (v) => {
      const sides = d3.rollups(v, (x) => x.length, (d) => d.side).sort((a, b) => b[1] - a[1]);
      return {
        route: v[0].family, side: sides[0][0],
        n: v.length, k: d3.sum(v, (d) => (d.success ? 1 : 0)),
        days: d3.median(v.map((d) => d.daysSummit).filter((x) => x != null && x > 0)),
      };
    }, (d) => d.family).map(([, v]) => v)
      .filter((d) => d.n >= 20)
      .sort((a, b) => b.k / b.n - a.k / a.n || b.n - a.n)
      .slice(0, 8);

    mount(document.getElementById("m2-routes"), 360, (svg, w, h) => {
      if (!byRoute.length) {
        svg.append("text").attr("x", w / 2).attr("y", h / 2).attr("text-anchor", "middle")
          .attr("fill", COLORS.faint).attr("font-size", 13)
          .text("No route family has 20+ expeditions in this filter — widen the period or season.");
        return;
      }
      const m = { top: 22, right: 84, bottom: 14, left: Math.min(230, w * 0.34) };
      const iw = w - m.left - m.right;
      const ih = h - m.top - m.bottom;
      const x = d3.scaleLinear().domain([0, 1]).range([0, iw]);
      const y = d3.scaleBand().domain(byRoute.map((d) => d.route)).range([m.top, m.top + ih]).padding(0.32);

      const g = svg.append("g");
      g.append("g").attr("transform", `translate(${m.left},0)`)
        .call(d3.axisTop(x).ticks(4).tickSize(-ih).tickFormat(d3.format(".0%")))
        .call((s) => {
          s.selectAll(".tick line").attr("stroke", COLORS.grid);
          s.selectAll(".tick text").attr("fill", COLORS.faint).attr("font-size", 10);
          s.select(".domain").remove();
        });

      g.selectAll("text.name")
        .data(byRoute).join("text")
        .attr("x", m.left - 10).attr("y", (d) => y(d.route) + y.bandwidth() / 2 + 1)
        .attr("text-anchor", "end").attr("font-size", 11).attr("fill", COLORS.ink)
        .text((d) => (d.route.length > 30 ? d.route.slice(0, 29) + "…" : d.route));

      g.selectAll("rect.bar")
        .data(byRoute).join("rect")
        .attr("x", m.left).attr("y", (d) => y(d.route))
        .attr("height", y.bandwidth())
        .attr("width", (d) => x(d.k / d.n))
        .attr("rx", 3)
        .attr("fill", (d) => COLORS.side[d.side] || COLORS.muted)
        .attr("opacity", (d) => (state.side === "All" || d.side === state.side ? 0.92 : 0.35));

      g.selectAll("text.val")
        .data(byRoute).join("text")
        .attr("x", (d) => m.left + x(d.k / d.n) + 8)
        .attr("y", (d) => y(d.route) + y.bandwidth() / 2 + 1)
        .attr("font-size", 10.5).attr("font-weight", 600).attr("fill", COLORS.ink)
        .text((d) => `${fmt.pct(d.k / d.n, 0)}  n=${fmt.int(d.n)}`);

      g.selectAll("rect.hit")
        .data(byRoute).join("rect")
        .attr("x", m.left).attr("y", (d) => y(d.route))
        .attr("width", iw).attr("height", y.bandwidth())
        .attr("fill", "transparent")
        .call((sel) => withTip(sel, (d) =>
          `<strong>${d.route}</strong><br>${d.side} side · ${fmt.int(d.n)} expeditions<br>` +
          `${fmt.int(d.k)} successful (${fmt.pct(d.k / d.n, 1)})<br>` +
          `<span class="tt-muted">${d.days ? "median " + fmt.dec1(d.days) + " days to summit" : "no summit-day records"}</span>`));
    });
  }

  // -------------------------------------------------------------- camps
  function drawCamps() {
    const sides = state.campSide === "both" ? ["South", "North"] : [state.campSide === "south" ? "South" : "North"];
    mount(document.getElementById("m2-camps"), 380, (svg, w, h) => {
      const m = { top: 26, right: 24, bottom: 22, left: 52 };
      const iw = w - m.left - m.right;
      const ih = h - m.top - m.bottom;
      const y = d3.scaleLinear().domain([4800, 9000]).range([m.top + ih, m.top]);
      const g = svg.append("g");

      g.append("g").attr("transform", `translate(${m.left},0)`)
        .call(d3.axisLeft(y).ticks(5).tickSize(-iw).tickFormat((v) => fmt.int(v) + " m"))
        .call((s) => {
          s.selectAll(".tick line").attr("stroke", COLORS.grid);
          s.selectAll(".tick text").attr("fill", COLORS.faint).attr("font-size", 10.5);
          s.select(".domain").remove();
        });

      const cols = sides.length === 2 ? [0.4, 0.6] : [0.5];
      sides.forEach((side, i) => {
        const cx = m.left + iw * cols[i];
        const series = D.camps[side.toLowerCase()].filter((c) => c.elev);
        const color = COLORS.side[side];

        g.append("line")
          .attr("x1", cx).attr("x2", cx)
          .attr("y1", y(series[series.length - 1].elev)).attr("y2", y(series[0].elev))
          .attr("stroke", color).attr("stroke-width", 2).attr("opacity", .35);

        series.forEach((c) => {
          const isSummit = c.label === "Smt";
          const dot = g.append("circle").attr("cx", cx).attr("cy", y(c.elev))
            .attr("r", isSummit ? 7 : 5).attr("fill", isSummit ? color : "#fff")
            .attr("stroke", color).attr("stroke-width", 2)
            .style("cursor", "help")
            .on("mousemove", (event) => U.tipShow(event,
              `<strong>${side} · ${c.name}</strong><br>median ${fmt.int(c.elev)} m<br>` +
              `${fmt.pct(c.share, 1)} of ${side.toLowerCase()} expeditions list this camp (n=${fmt.int(c.n)})<br>` +
              `<span class="tt-muted">${c.medianDate ? "typical date " + c.medianDate : "no dated records"}</span>`))
            .on("mouseleave", U.tipHide);

          // labels sit outside the pair of columns so they never collide
          const outward = sides.length === 2 ? (i === 0 ? "end" : "start") : "start";
          const lx = outward === "start" ? cx + 16 : cx - 16;
          const anchor = outward === "start" ? "start" : "end";
          const label = g.append("g").attr("transform", `translate(${lx},${y(c.elev)})`);
          label.append("text").attr("text-anchor", anchor).attr("y", 4)
            .attr("font-size", 11.5).attr("fill", COLORS.ink)
            .html(`${c.name} <tspan font-weight="600">${fmt.int(c.elev)} m</tspan>` +
                  `<tspan fill="${COLORS.faint}" font-size="10">  ${fmt.pct(c.share, 0)} · n=${fmt.int(c.n)}</tspan>`);

        });

        g.append("text").attr("x", cx).attr("y", m.top - 8).attr("text-anchor", "middle")
          .attr("font-size", 12).attr("font-weight", 600).attr("fill", color)
          .text(side + " side");
      });

      g.append("text").attr("x", m.left).attr("y", h - 4).attr("font-size", 10).attr("fill", COLORS.faint)
        .text("Schematic cross-section built from the campsite field (dates and altitudes), all seasons 1921–2024. No georeferencing.");
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
      <div class="current-src">
        ${cur.sources.map((s) => `<a href="${s.url}" target="_blank" rel="noopener">${s.publisher} · ${s.date}</a>`).join("")}
      </div>`;
  }

  function init() {
    try { if (window.GEO) window.GEO.init(); } catch (err) { console.warn("geo view failed", err); }
    renderFilters();
    renderKpis();
    drawCompare();
    drawRoutes();
    drawCamps();
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

  window.M2 = { init };
})();
