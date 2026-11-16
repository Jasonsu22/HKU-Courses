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

  const COLORS = {
    south: "#b4552d",
    north: "#1e4a5f",
    navy: "#1e4a5f",
    southSoft: "#d9a184",
    northSoft: "#6f97a6",
    ink: "#1b1e22",
    muted: "#6f6a62",
    faint: "#9a948a",
    line: "#e6e0d6",
    grid: "#efeae2",
    accent: "#2c8a7e",
    rust: "#b4552d",
    teal: "#2c8a7e",
    sand: "#c19a5b",
    plum: "#6d4f7c",
    red: "#a63d40",
    green: "#4f7a4a",
    season: {
      Spring: "#b4552d",
      Autumn: "#c19a5b",
      Winter: "#1e4a5f",
      Summer: "#2c8a7e",
    },
    side: { South: "#b4552d", North: "#1e4a5f" },
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

  window.U = {
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
