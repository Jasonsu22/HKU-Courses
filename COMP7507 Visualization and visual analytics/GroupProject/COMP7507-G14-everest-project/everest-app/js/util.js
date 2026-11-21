/* Shared helpers: formatting, tooltip, responsive chart mount. */
(function () {
  "use strict";

  const fmt = {
    int: d3.format(","),
    pct: (x, d = 0) => (x == null || isNaN(x) ? "–" : d3.format("." + d + "%")(x)),
    dec1: (x) => (x == null || isNaN(x) ? "–" : d3.format(".1f")(x)),
    dec2: (x) => (x == null || isNaN(x) ? "–" : d3.format(".2f")(x)),
    dec3: (x) => (x == null || isNaN(x) ? "–" : d3.format(".3f")(x)),
    sign1: (x) => (x == null || isNaN(x) ? "–" : d3.format("+.1f")(x)),
  };

  // Colours are assigned by job and checked with the palette validator:
  // side pair + plan accent (categorical), one sequential hue, one diverging pair.
  const COLORS = {
    south: "#eb6834",
    north: "#2a78d6",
    navy: "#1e4a5f",
    slate: "#34495e",
    plan: "#d81b60",
    above: "#1b7837",
    below: "#762a83",
    mid: "#f0efec",
    southSoft: "#f4b193",
    northSoft: "#94bcec",
    ink: "#1b1e22",
    muted: "#6f6a62",
    faint: "#857f75",
    line: "#e6e0d6",
    grid: "#efeae2",
    accent: "#2c8a7e",
    rust: "#b4552d",
    teal: "#2c8a7e",
    sand: "#c19a5b",
    plum: "#6d4f7c",
    red: "#a63d40",
    green: "#4f7a4a",
    season: { Spring: "#1baf7a", Autumn: "#eda100", Winter: "#6250d6", Summer: "#e87ba4" },
    side: { South: "#eb6834", North: "#2a78d6" },
    series: ["#1baf7a", "#2a78d6", "#eda100", "#6250d6", "#eb6834"],
    end: {
      "Summit": "#1baf7a",
      "Weather & conditions": "#2a78d6",
      "Illness & exhaustion": "#eda100",
      "Accident": "#6250d6",
      "Logistics & difficulty": "#eb6834",
      "Season closure": "#1b1e22",
      "Other / unknown": "#b8b2a7",
    },
  };

  // Wilson score interval for a binomial proportion.
  function wilson(k, n, z = 1.96) {
    if (!n) return [0, 0];
    const p = k / n;
    const denom = 1 + (z * z) / n;
    const centre = (p + (z * z) / (2 * n)) / denom;
    const half =
      (z * Math.sqrt((p * (1 - p)) / n + (z * z) / (4 * n * n))) / denom;
    return [Math.max(0, centre - half), Math.min(1, centre + half)];
  }

  // ------------------------------------------------------------- tooltip
  const tipEl = () => document.getElementById("tooltip");
  function tipShow(event, html) {
    const el = tipEl();
    el.innerHTML = html;
    el.classList.add("is-on");
    const x = event.clientX;
    const y = event.clientY - 14;
    el.style.left = x + "px";
    el.style.top = y + "px";
    const rect = el.getBoundingClientRect();
    const left = Math.min(Math.max(rect.width / 2 + 10, x), window.innerWidth - rect.width / 2 - 10);
    el.style.left = left + "px";
    el.style.top = Math.max(rect.height + 12, y) + "px";
  }
  function tipHide() {
    tipEl().classList.remove("is-on");
  }

  // Attach hover + focus tooltip to a selection.
  function withTip(sel, html) {
    sel
      .on("mousemove", (event, d) => tipShow(event, typeof html === "function" ? html(d) : html))
      .on("mouseleave", tipHide)
      .on("blur", tipHide);
    return sel;
  }

  // --------------------------------------------------- responsive chart
  // Renders draw(svg, width, height) at the container's real pixel width and
  // re-renders on resize. Avoids blurry scaled viewBoxes.
  function mount(el, height, draw) {
    if (!el) return;
    const render = () => {
      const width = Math.max(280, el.clientWidth);
      d3.select(el).selectAll("*").remove();
      const svg = d3
        .select(el)
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .attr("viewBox", `0 0 ${width} ${height}`)
        .attr("role", "img");
      draw(svg, width, height);
    };
    render();
    if (el._ro) el._ro.disconnect();
    el._ro = new ResizeObserver(() => {
      clearTimeout(el._t);
      el._t = setTimeout(render, 120);
    });
    el._ro.observe(el);
    el._render = render;
  }

  // --------------------------------------------------------------- misc
  function el(tag, attrs = {}, text) {
    const n = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs)) {
      if (k === "class") n.className = v;
      else if (k === "html") n.innerHTML = v;
      else n.setAttribute(k, v);
    }
    if (text != null) n.textContent = text;
    return n;
  }

  function segmented(container, options, value, onChange, { activeClass = "is-active", attr = "data-value" } = {}) {
    container.innerHTML = "";
    options.forEach((opt) => {
      const b = el("button", { type: "button" }, opt.label);
      b.style.border = "0";
      b.style.background = "transparent";
      b.style.padding = "5px 11px";
      b.style.borderRadius = "999px";
      b.style.fontSize = "12px";
      b.style.color = "";
      b.addEventListener("click", () => {
        Array.from(container.children).forEach((c) => c.classList.remove(activeClass));
        b.classList.add(activeClass);
        onChange(opt.value);
      });
      if (opt.value === value) b.classList.add(activeClass);
      container.appendChild(b);
    });
  }

  function statCard({ value, label, sub, accent }) {
    const d = el("div", { class: "kpi" + (accent ? " kpi--accent" : "") });
    d.innerHTML = `<div class="kpi-value">${value}</div>
      <div class="kpi-label">${label}</div>
      ${sub ? `<div class="kpi-sub">${sub}</div>` : ""}`;
    return d;
  }

  // ------------------------------------------------------------ axes
  function axisY(g, y, x, iw, { ticks = 4, format, size = 11 } = {}) {
    const a = d3.axisLeft(y).ticks(ticks).tickSize(-iw);
    if (format) a.tickFormat(format);
    g.append("g").attr("transform", `translate(${x},0)`).call(a).call((s) => {
      s.selectAll(".tick line").attr("stroke", COLORS.grid);
      s.selectAll(".tick text").attr("fill", COLORS.muted).attr("font-size", size);
      s.select(".domain").remove();
    });
  }
  const YEAR = d3.format("d");
  function axisX(g, x, y, { ticks = 6, format = YEAR, values, size = 11 } = {}) {
    const a = d3.axisBottom(x).tickSize(3);
    if (values) a.tickValues(values);
    else if (x.ticks) a.tickValues(format === YEAR ? x.ticks(ticks).filter(Number.isInteger) : x.ticks(ticks));
    a.tickFormat(format);
    g.append("g").attr("transform", `translate(0,${y})`).call(a).call((s) => {
      s.select(".domain").attr("stroke", COLORS.line);
      s.selectAll(".tick line").attr("stroke", COLORS.line);
      s.selectAll(".tick text").attr("fill", COLORS.muted).attr("font-size", size);
    });
  }
  function caption(g, x, y, text, anchor = "start") {
    return g.append("text").attr("x", x).attr("y", y).attr("text-anchor", anchor)
      .attr("font-size", 11).attr("fill", COLORS.muted).text(text);
  }
  function emptyNote(svg, w, h, text) {
    svg.append("text").attr("x", w / 2).attr("y", h / 2).attr("text-anchor", "middle")
      .attr("font-size", 13).attr("fill", COLORS.muted).text(text);
  }

  // Legend drawn inside a chart. Text stays in ink; the swatch carries identity.
  function legend(g, x, y, items, { gap = 16 } = {}) {
    let cx = x;
    items.forEach((it) => {
      const row = g.append("g").attr("transform", `translate(${cx},${y})`);
      if (it.dash) {
        row.append("line").attr("x1", 0).attr("x2", 16).attr("y1", -4).attr("y2", -4)
          .attr("stroke", it.color).attr("stroke-width", 2).attr("stroke-dasharray", it.dash);
      } else if (it.line) {
        row.append("line").attr("x1", 0).attr("x2", 16).attr("y1", -4).attr("y2", -4)
          .attr("stroke", it.color).attr("stroke-width", 2.4);
      } else {
        row.append("rect").attr("y", -9).attr("width", 10).attr("height", 10).attr("rx", 2).attr("fill", it.color);
      }
      const off = it.dash || it.line ? 21 : 14;
      row.append("text").attr("x", off).attr("y", 0).attr("font-size", 11).attr("fill", COLORS.ink).text(it.label);
      cx += off + it.label.length * 6 + gap;
    });
  }

  // ------------------------------------------------------------- scales
  function diverging(max) {
    return d3.scaleLinear().domain([-max, 0, max]).range([COLORS.below, COLORS.mid, COLORS.above]).clamp(true);
  }
  function sequential(max) {
    return d3.scaleSequential([0, max], d3.interpolateRgbBasis(["#e3edfb", "#86b6ef", "#2a78d6", "#104281"]));
  }
  // Readable text on a filled cell.
  function inkOn(fill) {
    const c = d3.lab(fill);
    return c.l > 62 ? COLORS.ink : "#fff";
  }
  let hatchCount = 0;
  function hatch(svg) {
    const id = "hatch" + ++hatchCount;
    const p = svg.append("defs").append("pattern").attr("id", id).attr("width", 6).attr("height", 6)
      .attr("patternUnits", "userSpaceOnUse").attr("patternTransform", "rotate(45)");
    p.append("rect").attr("width", 6).attr("height", 6).attr("fill", "#f7f5f1");
    p.append("line").attr("x1", 0).attr("x2", 0).attr("y1", 0).attr("y2", 6).attr("stroke", "#c4bdb1").attr("stroke-width", 2);
    return `url(#${id})`;
  }
  function gradientLegend(svg, x, y, w, scale, [lo, hi], labels) {
    const id = "grad" + ++hatchCount;
    const grad = svg.append("defs").append("linearGradient").attr("id", id);
    d3.range(0, 1.01, 0.1).forEach((t) => grad.append("stop").attr("offset", t * 100 + "%").attr("stop-color", scale(lo + (hi - lo) * t)));
    const g = svg.append("g").attr("transform", `translate(${x},${y})`);
    g.append("rect").attr("width", w).attr("height", 8).attr("rx", 3).attr("fill", `url(#${id})`);
    labels.forEach(([t, text]) => g.append("text").attr("x", w * t).attr("y", 20).attr("font-size", 10.5)
      .attr("text-anchor", t === 0 ? "start" : t === 1 ? "end" : "middle").attr("fill", COLORS.muted).text(text));
  }

  // --------------------------------------------------------- event marks
  // Reasons for 2014 and 2015 come from the dataset's own termnote field.
  const EVENTS = [
    { year: 2014, label: "2014", tip: "<strong>2014</strong><br>Most Nepal-side expeditions abandoned: notes cite the Sherpa strike and a fatal avalanche" },
    { year: 2015, label: "2015", tip: "<strong>2015</strong><br>Season abandoned on both sides: notes cite the earthquake" },
    { year: 2020, label: "2020", tip: "<strong>2020</strong><br>Only 3 expeditions recorded" },
  ];
  function eventMarks(g, x, top, bottom, { labels = true, all = false } = {}) {
    const [a, b] = x.domain();
    const source = window.EVEREST_EVENTS || EVENTS;
    const events = all ? source : source.filter((e) => e.mark !== false);
    events.filter((e) => e.year >= a && e.year <= b).forEach((e) => {
      const px = x(e.year);
      const tip = e.summary ? `<strong>${e.label} · ${e.title}</strong><br>${e.summary}` : e.tip;
      g.append("line").attr("x1", px).attr("x2", px).attr("y1", top).attr("y2", bottom)
        .attr("stroke", COLORS.ink).attr("stroke-width", 1).attr("stroke-dasharray", "2 3").attr("opacity", .55);
      if (labels) {
        g.append("text").attr("x", px + (e.year === 2014 ? -3 : 3)).attr("y", top + 9)
          .attr("text-anchor", e.year === 2014 ? "end" : "start").attr("font-size", 10).attr("fill", COLORS.muted).text(e.label);
      }
      g.append("rect").attr("x", px - 5).attr("y", top).attr("width", 10).attr("height", bottom - top)
        .attr("fill", "transparent").call((s) => withTip(s, tip));
    });
  }

  // ------------------------------------------------------- timeline brush
  // Overview + detail: bars for context, a brush that drives every linked view.
  function timeline(box, { data, height = 74, getRange, onChange, valueLabel = "" }) {
    mount(box, height, (svg, w, h) => {
      const m = { top: 6, right: 12, bottom: 20, left: 12 };
      const years = data.map((d) => d.year);
      const x = d3.scaleLinear().domain([d3.min(years), d3.max(years) + 1]).range([m.left, w - m.right]);
      const y = d3.scaleLinear().domain([0, d3.max(data, (d) => d.v) || 1]).range([h - m.bottom, m.top]);
      const bw = Math.max(1, x(1) - x(0) - 1);
      const bars = svg.append("g").selectAll("rect").data(data).join("rect")
        .attr("x", (d) => x(d.year)).attr("width", bw).attr("y", (d) => y(d.v))
        .attr("height", (d) => y(0) - y(d.v)).attr("rx", 1);
      const paint = () => {
        const [a, b] = getRange();
        bars.attr("fill", (d) => (d.year >= a && d.year <= b ? COLORS.slate : "#d6cfc3"));
      };
      paint();
      axisX(svg.append("g"), x, h - m.bottom, { ticks: Math.min(12, Math.round(w / 80)), size: 10.5 });
      const brush = d3.brushX().extent([[m.left, m.top - 2], [w - m.right, h - m.bottom + 1]])
        .on("brush", (event) => {
          if (!event.selection || !event.sourceEvent) return;
          box.dataset.preview = 1;
        })
        .on("end", (event) => {
          if (!event.sourceEvent) return;
          if (!event.selection) { onChange(null); return; }
          const a = Math.round(x.invert(event.selection[0]));
          const b = Math.max(a, Math.round(x.invert(event.selection[1])) - 1);
          onChange([a, b]);
        });
      const gb = svg.append("g").attr("class", "tl-brush").call(brush);
      gb.call(brush.move, [x(getRange()[0]), x(getRange()[1] + 1)]);
      gb.selectAll(".selection").attr("fill", COLORS.plan).attr("fill-opacity", .08).attr("stroke", COLORS.plan).attr("stroke-width", 1.4);
      svg.attr("aria-label", `Timeline brush: ${valueLabel}`);
    });
  }

  // ------------------------------------------------------- horizon graph
  // Two-band horizon: positive and negative layers folded onto one baseline.
  function horizon(g, svg, { series, x, top, height, step, color = [COLORS.above, COLORS.below] }) {
    const defined = series.filter((d) => d.v != null);
    if (!defined.length) return;
    const id = "hclip" + ++hatchCount;
    svg.append("defs").append("clipPath").attr("id", id).append("rect")
      .attr("x", x.range()[0]).attr("y", top).attr("width", x.range()[1] - x.range()[0]).attr("height", height);
    const layer = g.append("g").attr("clip-path", `url(#${id})`);
    [[1, color[0]], [-1, color[1]]].forEach(([sign, c]) => {
      [0, 1].forEach((band) => {
        const y = (v) => top + height - ((Math.max(0, sign * v) - band * step) / step) * height;
        layer.append("path").datum(series)
          .attr("d", d3.area().defined((d) => d.v != null).x((d) => x(d.x)).y0(top + height).y1((d) => y(d.v)).curve(d3.curveStepAfter))
          .attr("fill", c).attr("opacity", band === 0 ? .45 : .95);
      });
    });
    g.append("line").attr("x1", x.range()[0]).attr("x2", x.range()[1]).attr("y1", top + height).attr("y2", top + height)
      .attr("stroke", COLORS.line);
  }

  // -------------------------------------------------------------- findings
  // Hypothesis cards: each one sets the charts to the state that shows its evidence.
  const FINDINGS = new Map();
  function findings(boxId, items) {
    const box = document.getElementById(boxId);
    if (!box) return;
    box.innerHTML = `<div class="findings-head">Hypotheses to test on this page</div><div class="findings-grid"></div>`;
    const grid = box.querySelector(".findings-grid");
    items.forEach((it) => {
      FINDINGS.set(it.id, it);
      const c = el("article", { class: "finding", id: "finding-" + it.id });
      c.innerHTML = `<div class="finding-top"><span class="finding-id">${it.id}</span><span class="finding-verdict">${it.verdict}</span></div>
        <h3>${it.title}</h3><p>${it.text()}</p>`;
      const b = el("button", { type: "button", class: "finding-go" }, "Show the evidence");
      b.addEventListener("click", () => it.apply());
      c.appendChild(b);
      grid.appendChild(c);
    });
  }
  function spotlight(id) {
    const n = document.getElementById(id);
    if (!n) return;
    let parent = n.parentElement;
    while (parent) {
      if (parent.tagName === "DETAILS") parent.open = true;
      parent = parent.parentElement;
    }
    n.scrollIntoView({ behavior: "smooth", block: "center" });
    n.classList.remove("is-spot");
    void n.offsetWidth;
    n.classList.add("is-spot");
  }
  function seg(boxId, value, onChange) {
    const box = document.getElementById(boxId);
    if (!box) return;
    const buttons = box.querySelectorAll("button");
    const set = (v) => buttons.forEach((b) => b.classList.toggle("is-active", b.dataset.mode === String(v)));
    set(value);
    buttons.forEach((b) => b.addEventListener("click", () => { set(b.dataset.mode); onChange(b.dataset.mode); }));
    return set;
  }

  window.U = {
    axisY, axisX, caption, emptyNote, legend, diverging, sequential, inkOn, hatch, gradientLegend,
    EVENTS, eventMarks, timeline, horizon, findings, FINDINGS, spotlight, seg,
    fmt,
    COLORS,
    wilson,
    tipShow,
    tipHide,
    withTip,
    mount,
    el,
    segmented,
    statCard,
  };
})();
