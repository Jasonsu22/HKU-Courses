/* Module 01 — historical evolution. */
(function () {
  "use strict";

  const D = window.EVEREST_DATA;
  const { fmt, COLORS, wilson, withTip, mount, el, statCard } = U;
  const state = { zoom: [1921, 2024], heat: "count", decade: null };

  function setDecade(dec) {
    state.decade = state.decade === dec ? null : dec;
    drawSuccess();
    drawHeat();
    drawDuration();
    const hint = document.getElementById("m1-success-hint");
    if (hint) {
      hint.textContent = state.decade
        ? `Highlighting ${state.decade}s across the decade, heatmap and duration charts — click it again to clear.`
        : "Share of expeditions with a summit on route 1; whiskers are 95% Wilson intervals. Click a decade to highlight it in the heatmap.";
    }
  }

  function success(d) {
    return d.n ? d.k / d.n : 0;
  }

  // ---------------------------------------------------------------- KPIs
  function renderKpis() {
    const h = D.headline;
    const box = document.getElementById("m1-kpis");
    box.innerHTML = "";
    box.append(
      statCard({
        value: fmt.int(h.expeditions),
        label: "expeditions",
        sub: `${h.years[0]}–${h.years[1]} · Everest only`,
      }),
      statCard({
        value: fmt.int(h.members),
        label: "member records",
        sub: "people, not unique climbers (~13.3k people)",
      }),
      statCard({
        value: fmt.pct(h.successfulExpeditions / h.expeditions, 1),
        label: "expeditions with a summit",
        sub: `${fmt.int(h.successfulExpeditions)} of ${fmt.int(h.expeditions)} (route 1)`,
        accent: true,
      }),
      statCard({
        value: fmt.int(h.deaths),
        label: "recorded deaths",
        sub: "208 members + 132 hired staff",
      })
    );
  }

  // ------------------------------------------------------ annual volumes
  function drawAnnual() {
    const box = document.getElementById("m1-annual");
    mount(box, 430, (svg, w, h) => {
      const m = { top: 18, right: 20, bottom: 26, left: 52 };
      const iw = w - m.left - m.right;
      const topH = (h - m.top - m.bottom) * 0.5;
      const gap = 34;
      const botH = h - m.top - m.bottom - topH - gap;
      const years = D.yearly.filter((d) => d.year >= state.zoom[0] && d.year <= state.zoom[1]);
      const [x0, x1] = state.zoom;

      const x = d3.scaleBand()
        .domain(years.map((d) => d.year))
        .range([m.left, m.left + iw])
        .paddingInner(0.28)
        .paddingOuter(0.06);

      const g = svg.append("g");

      // ---- top panel: expeditions
      const y1 = d3.scaleLinear()
        .domain([0, d3.max(years, (d) => d.n) * 1.08])
        .nice()
        .range([m.top + topH, m.top]);
      g.append("g")
        .attr("transform", `translate(${m.left},0)`)
        .call(d3.axisLeft(y1).ticks(4).tickSize(-iw).tickFormat(fmt.int))
        .call((s) => {
          s.selectAll(".tick line").attr("stroke", COLORS.grid);
          s.selectAll(".tick text").attr("fill", COLORS.faint).attr("font-size", 11);
          s.select(".domain").remove();
        });
      g.append("text").attr("x", m.left).attr("y", m.top - 4)
        .attr("font-size", 11).attr("fill", COLORS.muted).text("expeditions");

      const bars = g.selectAll("rect.exp")
        .data(years)
        .join("rect")
        .attr("class", "exp")
        .attr("x", (d) => x(d.year))
        .attr("width", x.bandwidth())
        .attr("y", (d) => y1(d.n))
        .attr("height", (d) => y1(0) - y1(d.n))
        .attr("fill", COLORS.north)
        .attr("rx", 1.5);

      // ---- bottom panel: member records
      const y2 = d3.scaleLinear()
        .domain([0, d3.max(years, (d) => d.members) * 1.1])
        .nice()
        .range([m.top + topH + gap + botH, m.top + topH + gap]);
      g.append("g")
        .attr("transform", `translate(${m.left},0)`)
        .call(d3.axisLeft(y2).ticks(4).tickSize(-iw).tickFormat(fmt.int))
        .call((s) => {
          s.selectAll(".tick line").attr("stroke", COLORS.grid);
          s.selectAll(".tick text").attr("fill", COLORS.faint).attr("font-size", 11);
          s.select(".domain").remove();
        });
      g.append("text").attr("x", m.left).attr("y", m.top + topH + gap - 4)
        .attr("font-size", 11).attr("fill", COLORS.muted).text("member records (participants)");

      const bars2 = g.selectAll("rect.mem")
        .data(years)
        .join("rect")
        .attr("class", "mem")
        .attr("x", (d) => x(d.year))
        .attr("width", x.bandwidth())
        .attr("y", (d) => y2(d.members))
        .attr("height", (d) => y2(0) - y2(d.members))
        .attr("fill", COLORS.teal)
        .attr("rx", 1.5);

      // ---- x axis
      const ticks = years.map((d) => d.year).filter((y) => y % 10 === 0 || y === x1);
      g.append("g")
        .attr("transform", `translate(0,${m.top + topH + gap + botH})`)
        .call(d3.axisBottom(x).tickValues(ticks).tickFormat(d3.format("d")).tickSize(4))
        .call((s) => {
          s.select(".domain").attr("stroke", COLORS.line);
          s.selectAll(".tick text").attr("fill", COLORS.faint).attr("font-size", 11);
        });

      // ---- annotation: 2020
      const d2020 = years.find((d) => d.year === 2020);
      if (d2020 && x1 - x0 > 30) {
        g.append("text")
          .attr("x", x(2020) + x.bandwidth() / 2)
          .attr("y", y1(0) - 7)
          .attr("text-anchor", "middle").attr("font-size", 10.5).attr("fill", COLORS.red)
          .text("2020: 3");
      }

      // ---- hover
      const hover = g.append("g").style("display", "none");
      const vline = hover.append("line").attr("stroke", COLORS.ink).attr("stroke-width", 1)
        .attr("stroke-dasharray", "2 3");
      const dot1 = hover.append("circle").attr("r", 3.2).attr("fill", COLORS.north);
      const dot2 = hover.append("circle").attr("r", 3.2).attr("fill", COLORS.teal);

      const overlay = g.append("rect")
        .attr("x", m.left).attr("y", m.top)
        .attr("width", iw).attr("height", topH + gap + botH)
        .attr("fill", "transparent")
        .style("cursor", "crosshair");

      const centres = years.map((d) => x(d.year) + x.bandwidth() / 2);
      overlay.on("mousemove", (event) => {
        const px = d3.pointer(event, g.node())[0];
        const i = Math.max(0, Math.min(years.length - 1, d3.bisectCenter(centres, px)));
        const d = years[i];
        const cx = x(d.year) + x.bandwidth() / 2;
        hover.style("display", null);
        vline.attr("x1", cx).attr("x2", cx).attr("y1", m.top).attr("y2", m.top + topH + gap + botH);
        dot1.attr("cx", cx).attr("cy", y1(d.n));
        dot2.attr("cx", cx).attr("cy", y2(d.members));
        U.tipShow(event,
          `<strong>${d.year}</strong><br>` +
          `${fmt.int(d.n)} expedition${d.n === 1 ? "" : "s"} · ${fmt.int(d.k)} with a summit<br>` +
          `${fmt.int(d.members)} members · ${fmt.int(d.hired)} hired<br>` +
          `<span class="tt-muted">${fmt.int(d.mDeaths)} member deaths · ${fmt.int(d.hDeaths)} hired deaths</span>`);
      }).on("mouseleave", () => {
        hover.style("display", "none");
        U.tipHide();
      });

      hover.raise();   // keep the crosshair above the event-capturing overlay
    });
  }

  // --------------------------------------------------- success by decade
  function drawSuccess() {
    mount(document.getElementById("m1-success"), 320, (svg, w, h) => {
      const m = { top: 16, right: 22, bottom: 34, left: 44 };
      const iw = w - m.left - m.right;
      const ih = h - m.top - m.bottom;
      const data = D.decades.filter((d) => d.n >= 5);
      const x = d3.scaleBand().domain(data.map((d) => d.decade)).range([m.left, m.left + iw]).padding(0.42);
      const y = d3.scaleLinear().domain([0, 1]).range([m.top + ih, m.top]);

      const g = svg.append("g");
      g.append("g")
        .attr("transform", `translate(${m.left},0)`)
        .call(d3.axisLeft(y).ticks(5).tickSize(-iw).tickFormat(d3.format(".0%")))
        .call((s) => {
          s.selectAll(".tick line").attr("stroke", COLORS.grid);
          s.selectAll(".tick text").attr("fill", COLORS.faint).attr("font-size", 11);
          s.select(".domain").remove();
        });

      const cx = (d) => x(d.decade) + x.bandwidth() / 2;
      g.selectAll("line.ci")
        .data(data)
        .join("line")
        .attr("class", "ci")
        .attr("x1", cx).attr("x2", cx)
        .attr("y1", (d) => y(wilson(d.k, d.n)[0]))
        .attr("y2", (d) => y(wilson(d.k, d.n)[1]))
        .attr("stroke", COLORS.northSoft).attr("stroke-width", 2)
        .attr("opacity", (d) => (state.decade && d.decade !== state.decade ? 0.25 : 1));

      g.selectAll("rect.bar")
        .data(data)
        .join("rect")
        .attr("class", "bar")
        .attr("x", (d) => x(d.decade) + x.bandwidth() * 0.18)
        .attr("width", x.bandwidth() * 0.64)
        .attr("y", (d) => y(success(d)))
        .attr("height", (d) => y(0) - y(success(d)))
        .attr("fill", (d) => (d.decade >= 2000 ? COLORS.rust : COLORS.north))
        .attr("rx", 2)
        .attr("opacity", (d) => (state.decade && d.decade !== state.decade ? 0.22 : 1));

      g.selectAll("text.k")
        .data(data)
        .join("text")
        .attr("x", cx)
        .attr("y", (d) => y(wilson(d.k, d.n)[1]) - 6)
        .attr("text-anchor", "middle")
        .attr("font-size", 10.5)
        .attr("fill", COLORS.muted)
        .text((d) => fmt.pct(success(d), 0));

      g.append("g")
        .attr("transform", `translate(0,${m.top + ih})`)
        .call(d3.axisBottom(x).tickFormat((d) => d + "s").tickSize(3))
        .call((s) => {
          s.select(".domain").attr("stroke", COLORS.line);
          s.selectAll(".tick text").attr("fill", COLORS.faint).attr("font-size", 11);
        });

      g.selectAll("rect.hit")
        .data(data)
        .join("rect")
        .attr("x", (d) => x(d.decade))
        .attr("y", m.top)
        .attr("width", x.bandwidth())
        .attr("height", ih)
        .attr("fill", "transparent")
        .style("cursor", "pointer")
        .on("click", (event, d) => setDecade(d.decade))
        .call((sel) => withTip(sel, (d) =>
          `<strong>${d.decade}s</strong><br>${fmt.int(d.k)} of ${fmt.int(d.n)} expeditions<br>` +
          `${fmt.pct(success(d), 1)} · 95% CI ${fmt.pct(wilson(d.k, d.n)[0])}–${fmt.pct(wilson(d.k, d.n)[1])}<br>` +
          `<span class="tt-muted">${fmt.int(d.members)} member records</span>`));
    });
  }

  // ------------------------------------------------------------- heatmap
  function drawHeat() {
    const hint = document.getElementById("m1-heat-hint");
    hint.textContent = state.heat === "count"
      ? "Number of expeditions (sqrt colour scale to spread the skewed counts). Cells with fewer than 5 are faded."
      : "Share of expeditions with a summit. Cells with fewer than 5 are faded.";

    mount(document.getElementById("m1-heat"), 320, (svg, w, h) => {
      const m = { top: 34, right: 12, bottom: 26, left: 62 };
      const iw = w - m.left - m.right;
      const ih = h - m.top - m.bottom;
      const decades = [...new Set(D.seasonDecade.map((d) => d.decade))];
      const seasons = ["Spring", "Autumn", "Winter", "Summer"];
      const lookup = new Map(D.seasonDecade.map((d) => [d.decade + "|" + d.season, d]));

      const x = d3.scaleBand().domain(decades).range([m.left, m.left + iw]).padding(0.12);
      const y = d3.scaleBand().domain(seasons).range([m.top, m.top + ih]).padding(0.16);

      const maxN = d3.max(D.seasonDecade, (d) => d.n);
      // counts are heavily skewed (two cells hold most expeditions), so colour by sqrt
      const rootN = Math.sqrt(maxN);
      const colorN = d3.scaleSequential([0, rootN], d3.interpolateRgbBasis(["#f4efe6", "#8fb3bf", "#1e4a5f"]));
      const colorR = d3.scaleSequential([0, 1], d3.interpolateRgbBasis(["#f4efe6", "#d9a184", "#a63d40"]));

      const g = svg.append("g");
      g.append("g")
        .attr("transform", `translate(${m.left},0)`)
        .call(d3.axisLeft(y).tickSize(0))
        .call((s) => {
          s.select(".domain").remove();
          s.selectAll("text").attr("fill", COLORS.ink).attr("font-size", 12).attr("dx", -8);
        });
      g.append("g")
        .attr("transform", `translate(0,${m.top + ih})`)
        .call(d3.axisBottom(x).tickFormat((d) => d + "s").tickSize(0))
        .call((s) => {
          s.select(".domain").remove();
          s.selectAll("text").attr("fill", COLORS.faint).attr("font-size", 10.5).attr("dy", 6);
        });

      const cells = decades.flatMap((dec) =>
        seasons.map((s) => lookup.get(dec + "|" + s) || { decade: dec, season: s, n: 0, k: 0 })
      );

      g.selectAll("rect.cell")
        .data(cells)
        .join("rect")
        .attr("class", "cell")
        .attr("x", (d) => x(d.decade))
        .attr("y", (d) => y(d.season))
        .attr("width", x.bandwidth())
        .attr("height", y.bandwidth())
        .attr("rx", 3)
        .attr("fill", (d) => {
          if (!d.n) return "#fbf9f5";
          return state.heat === "count" ? colorN(Math.sqrt(d.n)) : colorR(success(d));
        })
        .attr("opacity", (d) => (state.decade && d.decade !== state.decade ? 0.22 : d.n < 5 ? 0.35 : 1))
        .style("cursor", "pointer")
        .on("click", (event, d) => setDecade(d.decade))
        .call((sel) => withTip(sel, (d) => d.n
          ? `<strong>${d.season} · ${d.decade}s</strong><br>${fmt.int(d.k)} of ${fmt.int(d.n)} expeditions<br>` +
            `${fmt.pct(success(d), 1)} success · n = ${fmt.int(d.n)}`
          : `<strong>${d.season} · ${d.decade}s</strong><br>no recorded expeditions`));

      // legend (above the grid, right aligned)
      const lg = svg.append("g").attr("transform", `translate(${w - m.right - 110},8)`);
      const defs = svg.append("defs");
      const grad = defs.append("linearGradient").attr("id", state.heat === "count" ? "lgN" : "lgR");
      const scale = state.heat === "count" ? colorN : colorR;
      for (let i = 0; i <= 10; i++) {
        grad.append("stop").attr("offset", i * 10 + "%")
          .attr("stop-color", scale(state.heat === "count" ? (rootN * i) / 10 : i / 10));
      }
      lg.append("rect").attr("width", 110).attr("height", 7).attr("rx", 3.5).attr("fill", `url(#${state.heat === "count" ? "lgN" : "lgR"})`);
      lg.append("text").attr("x", 0).attr("y", 20).attr("font-size", 10).attr("fill", COLORS.faint)
        .text(state.heat === "count" ? "0" : "0%");
      lg.append("text").attr("x", 110).attr("y", 20).attr("text-anchor", "end").attr("font-size", 10).attr("fill", COLORS.faint)
        .text(state.heat === "count" ? fmt.int(maxN) : "100%");
    });
  }

  // ------------------------------------------------------------ duration
  function drawDuration() {
    mount(document.getElementById("m1-duration"), 320, (svg, w, h) => {
      const m = { top: 16, right: 22, bottom: 34, left: 44 };
      const iw = w - m.left - m.right;
      const ih = h - m.top - m.bottom;
      const data = D.durations;
      const x = d3.scaleBand().domain(data.map((d) => d.decade)).range([m.left, m.left + iw]).padding(0.36);
      const y = d3.scaleLinear().domain([0, d3.max(data, (d) => d.p90) * 1.08]).nice().range([m.top + ih, m.top]);

      const g = svg.append("g");
      g.append("g")
        .attr("transform", `translate(${m.left},0)`)
        .call(d3.axisLeft(y).ticks(4).tickSize(-iw))
        .call((s) => {
          s.selectAll(".tick line").attr("stroke", COLORS.grid);
          s.selectAll(".tick text").attr("fill", COLORS.faint).attr("font-size", 11);
          s.select(".domain").remove();
        });
      g.append("text").attr("x", m.left).attr("y", m.top - 4).attr("font-size", 11).attr("fill", COLORS.muted)
        .text("days, base camp → summit");

      const cx = (d) => x(d.decade) + x.bandwidth() / 2;
      g.selectAll("line.iqr")
        .data(data).join("line")
        .attr("x1", (d) => cx(d) - x.bandwidth() * 0.3)
        .attr("x2", (d) => cx(d) + x.bandwidth() * 0.3)
        .attr("y1", (d) => y(d.p10)).attr("y2", (d) => y(d.p90))
        .attr("stroke", COLORS.northSoft).attr("stroke-width", 1.6);

      g.selectAll("rect.iqr")
        .data(data).join("rect")
        .attr("x", cx).attr("width", x.bandwidth() * 0.34)
        .attr("y", (d) => y(d.p75))
        .attr("height", (d) => y(d.p25) - y(d.p75))
        .attr("fill", COLORS.north)
        .attr("opacity", (d) => (state.decade && d.decade !== state.decade ? 0.2 : 0.85))
        .attr("transform", (d) => `translate(${-x.bandwidth() * 0.17},0)`);

      g.selectAll("line.med")
        .data(data).join("line")
        .attr("x1", (d) => cx(d) - x.bandwidth() * 0.28)
        .attr("x2", (d) => cx(d) + x.bandwidth() * 0.28)
        .attr("y1", (d) => y(d.p50)).attr("y2", (d) => y(d.p50))
        .attr("stroke", "#fff").attr("stroke-width", 2.4);

      g.selectAll("text.medv")
        .data(data).join("text")
        .attr("x", cx).attr("y", (d) => y(d.p75) - 8)
        .attr("text-anchor", "middle").attr("font-size", 10.5).attr("fill", COLORS.muted)
        .text((d) => fmt.dec1(d.p50));

      g.append("g")
        .attr("transform", `translate(0,${m.top + ih})`)
        .call(d3.axisBottom(x).tickFormat((d) => d + "s").tickSize(3))
        .call((s) => {
          s.select(".domain").attr("stroke", COLORS.line);
          s.selectAll(".tick text").attr("fill", COLORS.faint).attr("font-size", 11);
        });

      g.selectAll("rect.hit")
        .data(data).join("rect")
        .attr("x", (d) => x(d.decade)).attr("y", m.top)
        .attr("width", x.bandwidth()).attr("height", ih).attr("fill", "transparent")
        .style("cursor", "pointer")
        .on("click", (event, d) => setDecade(d.decade))
        .call((sel) => withTip(sel, (d) =>
          `<strong>${d.decade}s</strong><br>median ${fmt.dec1(d.p50)} days<br>` +
          `IQR ${fmt.dec1(d.p25)}–${fmt.dec1(d.p75)} · 10–90th ${fmt.dec1(d.p10)}–${fmt.dec1(d.p90)}<br>` +
          `<span class="tt-muted">n = ${fmt.int(d.n)} expeditions with a summit day</span>`));
    });
  }

  // ----------------------------------------------------------- structure
  function drawStructure() {
    mount(document.getElementById("m1-structure"), 320, (svg, w, h) => {
      const m = { top: 16, right: 22, bottom: 34, left: 48 };
      const iw = w - m.left - m.right;
      const ih = h - m.top - m.bottom;
      const data = D.yearly;
      const x = d3.scaleLinear().domain([data[0].year, data[data.length - 1].year]).range([m.left, m.left + iw]);
      const y = d3.scaleLinear().domain([0, d3.max(data, (d) => d.members + d.hired) * 1.05]).nice().range([m.top + ih, m.top]);

      const g = svg.append("g");
      g.append("g")
        .attr("transform", `translate(${m.left},0)`)
        .call(d3.axisLeft(y).ticks(4).tickSize(-iw).tickFormat(d3.format(".2s")))
        .call((s) => {
          s.selectAll(".tick line").attr("stroke", COLORS.grid);
          s.selectAll(".tick text").attr("fill", COLORS.faint).attr("font-size", 11);
          s.select(".domain").remove();
        });

      const areaHired = d3.area()
        .x((d) => x(d.year)).y0(y(0)).y1((d) => y(d.hired)).curve(d3.curveMonotoneX);
      const areaMembers = d3.area()
        .x((d) => x(d.year)).y0((d) => y(d.hired)).y1((d) => y(d.members + d.hired)).curve(d3.curveMonotoneX);

      g.append("path").datum(data).attr("d", areaMembers).attr("fill", COLORS.north).attr("opacity", 0.85);
      g.append("path").datum(data).attr("d", areaHired).attr("fill", COLORS.sand).attr("opacity", 0.9);

      const lg = g.append("g").attr("transform", `translate(${m.left},${m.top - 6})`);
      lg.append("rect").attr("x", 0).attr("y", -6).attr("width", 9).attr("height", 9).attr("fill", COLORS.navy).attr("rx", 2);
      lg.append("text").attr("x", 14).attr("y", 3).attr("font-size", 10.5).attr("fill", COLORS.muted).text("members");
      lg.append("rect").attr("x", 82).attr("y", -6).attr("width", 9).attr("height", 9).attr("fill", COLORS.sand).attr("rx", 2);
      lg.append("text").attr("x", 96).attr("y", 3).attr("font-size", 10.5).attr("fill", COLORS.muted).text("hired staff");

      g.append("g")
        .attr("transform", `translate(0,${m.top + ih})`)
        .call(d3.axisBottom(x).ticks(6).tickFormat(d3.format("d")).tickSize(3))
        .call((s) => {
          s.select(".domain").attr("stroke", COLORS.line);
          s.selectAll(".tick text").attr("fill", COLORS.faint).attr("font-size", 11);
        });

      g.selectAll("rect.hit")
        .data(data).join("rect")
        .attr("x", (d) => x(d.year) - iw / data.length / 2)
        .attr("y", m.top).attr("width", iw / data.length).attr("height", ih)
        .attr("fill", "transparent")
        .call((sel) => withTip(sel, (d) =>
          `<strong>${d.year}</strong><br>${fmt.int(d.members)} members<br>` +
          `${fmt.int(d.hired)} hired staff<br>` +
          `<span class="tt-muted">${fmt.dec1(d.members ? d.hired / d.members : NaN)} hired per member</span>`));
    });
  }

  // ------------------------------------------------------------- oxygen
  function drawO2() {
    mount(document.getElementById("m1-o2"), 280, (svg, w, h) => {
      const m = { top: 18, right: 22, bottom: 30, left: 44 };
      const iw = w - m.left - m.right;
      const ih = h - m.top - m.bottom;
      const raw = D.yearly;
      const data = raw.map((d) => {
        const win = raw.filter((x) => Math.abs(x.year - d.year) <= 2);
        const n = d3.sum(win, (x) => x.n);
        const o2 = d3.sum(win, (x) => x.o2);
        return { year: d.year, share: n ? o2 / n : null, n };
      }).filter((d) => d.n >= 10 && d.share != null);
      const x = d3.scaleLinear().domain([data[0].year, data[data.length - 1].year]).range([m.left, m.left + iw]);
      const y = d3.scaleLinear().domain([0, 1]).range([m.top + ih, m.top]);

      const g = svg.append("g");
      g.append("g")
        .attr("transform", `translate(${m.left},0)`)
        .call(d3.axisLeft(y).ticks(4).tickSize(-iw).tickFormat(d3.format(".0%")))
        .call((s) => {
          s.selectAll(".tick line").attr("stroke", COLORS.grid);
          s.selectAll(".tick text").attr("fill", COLORS.faint).attr("font-size", 11);
          s.select(".domain").remove();
        });

      g.append("path").datum(data)
        .attr("d", d3.line().x((d) => x(d.year)).y((d) => y(d.share)).curve(d3.curveMonotoneX))
        .attr("fill", "none").attr("stroke", COLORS.rust).attr("stroke-width", 2);

      g.append("text").attr("x", m.left).attr("y", m.top - 4).attr("font-size", 10.5).attr("fill", COLORS.faint)
        .text("5-year rolling share");
      g.append("g")
        .attr("transform", `translate(0,${m.top + ih})`)
        .call(d3.axisBottom(x).ticks(5).tickFormat(d3.format("d")).tickSize(3))
        .call((s) => {
          s.select(".domain").attr("stroke", COLORS.line);
          s.selectAll(".tick text").attr("fill", COLORS.faint).attr("font-size", 11);
        });

      g.selectAll("circle")
        .data(data).join("circle")
        .attr("cx", (d) => x(d.year)).attr("cy", (d) => y(d.share)).attr("r", 2.2)
        .attr("fill", COLORS.rust).call((sel) => withTip(sel, (d) =>
          `<strong>${d.year}</strong><br>${fmt.int(d.o2)} of ${fmt.int(d.n)} expeditions used oxygen<br>` +
          `${fmt.pct(d.o2 / d.n, 1)} · n = ${fmt.int(d.n)}`));
    });
  }

  // ------------------------------------------------------------- deaths
  function drawDeaths() {
    mount(document.getElementById("m1-deaths"), 280, (svg, w, h) => {
      const m = { top: 18, right: 22, bottom: 46, left: 44 };
      const iw = w - m.left - m.right;
      const ih = h - m.top - m.bottom;
      const data = D.decades.filter((d) => d.n >= 5);
      const x = d3.scaleBand().domain(data.map((d) => d.decade)).range([m.left, m.left + iw]).padding(0.34);
      const y = d3.scaleLinear()
        .domain([0, d3.max(data, (d) => d.mDeaths + d.hDeaths) * 1.15 || 1])
        .nice().range([m.top + ih, m.top]);

      const g = svg.append("g");
      g.append("g")
        .attr("transform", `translate(${m.left},0)`)
        .call(d3.axisLeft(y).ticks(3).tickSize(-iw).tickFormat(fmt.int))
        .call((s) => {
          s.selectAll(".tick line").attr("stroke", COLORS.grid);
          s.selectAll(".tick text").attr("fill", COLORS.faint).attr("font-size", 11);
          s.select(".domain").remove();
        });

      g.selectAll("rect.m")
        .data(data).join("rect")
        .attr("x", (d) => x(d.decade))
        .attr("y", (d) => y(d.mDeaths))
        .attr("height", (d) => y(0) - y(d.mDeaths))
        .attr("width", x.bandwidth())
        .attr("fill", COLORS.red).attr("rx", 2);
      g.selectAll("rect.h")
        .data(data).join("rect")
        .attr("x", (d) => x(d.decade))
        .attr("y", (d) => y(d.mDeaths + d.hDeaths))
        .attr("height", (d) => y(d.mDeaths) - y(d.mDeaths + d.hDeaths))
        .attr("width", x.bandwidth())
        .attr("fill", COLORS.sand).attr("rx", 2);

      const cx = (d) => x(d.decade) + x.bandwidth() / 2;
      g.append("g")
        .attr("transform", `translate(0,${m.top + ih})`)
        .call(d3.axisBottom(x).tickFormat((d) => d + "s").tickSize(3))
        .call((s) => {
          s.select(".domain").attr("stroke", COLORS.line);
          s.selectAll(".tick text").attr("fill", COLORS.faint).attr("font-size", 11);
        });

      g.selectAll("text.rate")
        .data(data).join("text")
        .attr("x", cx).attr("y", m.top + ih + 30)
        .attr("text-anchor", "middle").attr("font-size", 9.5).attr("fill", COLORS.faint)
        .text((d) => {
          const denom = d.members + d.hired;
          return denom ? fmt.dec1(((d.mDeaths + d.hDeaths) / denom) * 1000) : "–";
        });
      g.append("text").attr("x", m.left).attr("y", h - 4).attr("font-size", 10).attr("fill", COLORS.faint)
        .text("deaths per 1,000 people on the mountain (below each decade)");

      g.selectAll("rect.hit")
        .data(data).join("rect")
        .attr("x", (d) => x(d.decade)).attr("y", m.top)
        .attr("width", x.bandwidth()).attr("height", ih).attr("fill", "transparent")
        .call((sel) => withTip(sel, (d) =>
          `<strong>${d.decade}s</strong><br>${fmt.int(d.mDeaths)} member deaths<br>` +
          `${fmt.int(d.hDeaths)} hired deaths<br>` +
          `<span class="tt-muted">per 1,000: ${fmt.dec1(((d.mDeaths + d.hDeaths) / (d.members + d.hired)) * 1000)}</span>`));

      // legend
      const lg = svg.append("g").attr("transform", `translate(${w - 168},${m.top - 10})`);
      lg.append("rect").attr("x", 0).attr("y", -6).attr("width", 9).attr("height", 9).attr("fill", COLORS.red).attr("rx", 2);
      lg.append("text").attr("x", 14).attr("y", 3).attr("font-size", 10.5).attr("fill", COLORS.muted).text("members");
      lg.append("rect").attr("x", 78).attr("y", -6).attr("width", 9).attr("height", 9).attr("fill", COLORS.sand).attr("rx", 2);
      lg.append("text").attr("x", 92).attr("y", 3).attr("font-size", 10.5).attr("fill", COLORS.muted).text("hired staff");
    });
  }

  // --------------------------------------------------------------- init
  function renderChips() {
    const box = document.getElementById("m1-era-chips");
    const opts = [
      { label: "All years", value: [1921, 2024] },
      { label: "1950–1990", value: [1950, 1990] },
      { label: "1990–2024", value: [1990, 2024] },
      { label: "2000–2024", value: [2000, 2024] },
    ];
    box.innerHTML = "";
    opts.forEach((o) => {
      const b = el("button", { class: "chip" + (o.value.join() === state.zoom.join() ? " is-active" : "") }, o.label);
      b.addEventListener("click", () => {
        state.zoom = o.value;
        renderChips();
        drawAnnual();
      });
      box.appendChild(b);
    });
  }

  function init() {
    renderKpis();
    renderChips();
    drawAnnual();
    drawSuccess();
    drawHeat();
    drawDuration();
    drawStructure();
    drawO2();
    drawDeaths();

    document.querySelectorAll("#m1-heat-toggle button").forEach((b) => {
      b.addEventListener("click", () => {
        document.querySelectorAll("#m1-heat-toggle button").forEach((x) => x.classList.remove("is-active"));
        b.classList.add("is-active");
        state.heat = b.dataset.mode;
        drawHeat();
      });
    });
  }

  window.M1 = { init };
})();
