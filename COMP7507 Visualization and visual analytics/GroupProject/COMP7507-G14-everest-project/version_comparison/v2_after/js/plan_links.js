/* Page 3 · Connections: factor network, adjacency matrix, plan decision tree (icicle). */
(function () {
  "use strict";

  const { fmt, COLORS, mount, withTip } = U;
  const MIN_PAIR = 20;
  const local = { view: "net", scope: "all", lift: 1.3, pinned: null, order: "group", path: [] };

  // ---------------------------------------------------------- association
  function association(rows) {
    const nodes = PD.ATTRS.map((a) => {
      const hit = rows.filter(a.test);
      return { a, id: a.id, ...PD.total(hit), hit };
    });
    const base = PD.total(rows);
    const links = [];
    nodes.forEach((s, i) => {
      for (let j = i + 1; j < nodes.length; j++) {
        const t = nodes[j];
        if (s.a.group === t.a.group || !s.n || !t.n) continue;
        const both = PD.total(s.hit.filter(t.a.test));
        const lift = both.n && base.n ? (both.n * base.n) / (s.n * t.n) : 0;
        links.push({ source: s.id, target: t.id, s, t, n: both.n, k: both.k, rate: both.rate, lift });
      }
    });
    return { nodes, links, base };
  }

  // The layout is computed once from 2005–24 and stays fixed, so moving the
  // period slider changes the links rather than rearranging the picture.
  let layout = null;
  function buildLayout() {
    if (layout) return layout;
    const rows = PD.rows.filter((r) => !r.closure && r.year >= 2005);
    const { nodes, links } = association(rows);
    const simNodes = nodes.map((n) => ({ id: n.id, group: n.a.group }));
    const simLinks = links.filter((l) => l.n >= MIN_PAIR && l.lift >= 1.1).map((l) => ({ source: l.source, target: l.target, strength: Math.min(1, (l.lift - 1) * 1.1) }));
    // Deterministic start: same input, same picture every time.
    simNodes.forEach((n, i) => {
      const t = (i / simNodes.length) * 2 * Math.PI;
      n.x = 300 * Math.cos(t); n.y = 200 * Math.sin(t);
    });
    const sim = d3.forceSimulation(simNodes)
      .force("link", d3.forceLink(simLinks).id((d) => d.id).distance(120).strength((d) => .04 + d.strength * .16))
      .force("charge", d3.forceManyBody().strength(-900))
      .force("x", d3.forceX().strength(.03)).force("y", d3.forceY().strength(.1))
      .force("collide", d3.forceCollide(66))
      .stop();
    sim.tick(500);
    const ex = d3.extent(simNodes, (d) => d.x), ey = d3.extent(simNodes, (d) => d.y);
    layout = new Map(simNodes.map((n) => [n.id, { x: (n.x - ex[0]) / (ex[1] - ex[0]), y: (n.y - ey[0]) / (ey[1] - ey[0]) }]));
    return layout;
  }

  function hint(extra) {
    const [a, b] = PD.state.range;
    document.getElementById("m3-net-hint").innerHTML = `Climbing members ${a}–${b}. ${extra}`;
  }

  // ------------------------------------------------------------- network
  function drawNetwork() {
    const pos = buildLayout();
    const { nodes, links, base } = association(PD.live());
    const planIds = new Set(PD.ATTRS.filter((a) => a.plan(M3.profile)).map((a) => a.id));
    const color = U.diverging(.35);
    let edges = links.filter((l) => l.n >= MIN_PAIR && l.lift >= local.lift);
    if (local.scope === "plan") edges = edges.filter((l) => planIds.has(l.source) || planIds.has(l.target));
    hint(`Each circle is a choice; size shows members and colour shows summit share against the ${fmt.pct(base.rate, 0)} average. A link means two choices occur together more often than chance, and its colour shows how the members with both did. <b>${edges.length}</b> links shown. Pink rings mark your plan.`);

    mount(document.getElementById("m3-net"), 520, (svg, w, h) => {
      if (!base.n) { U.emptyNote(svg, w, h, "No records in this period."); return; }
      const pad = { x: 74, y: 44 };
      const px = (id) => pad.x + pos.get(id).x * (w - pad.x * 2);
      const py = (id) => pad.y + 8 + pos.get(id).y * (h - pad.y * 2 - 20);
      const r = d3.scaleSqrt().domain([0, d3.max(nodes, (n) => n.n) || 1]).range([3, 25]);
      U.gradientLegend(svg, 4, 0, 170, color, [-.35, .35], [[0, "−35 pts"], [.5, "average"], [1, "+35 pts"]]);

      const edgeSel = svg.append("g").selectAll("line").data(edges).join("line")
        .attr("x1", (d) => px(d.source)).attr("y1", (d) => py(d.source))
        .attr("x2", (d) => px(d.target)).attr("y2", (d) => py(d.target))
        .attr("stroke", (d) => color(d.rate - base.rate))
        .attr("stroke-width", (d) => Math.min(9, 1.2 + (d.lift - 1) * 2.2))
        .attr("stroke-opacity", .85)
        .call((s) => withTip(s, (d) => `<strong>${d.s.a.label} + ${d.t.a.label}</strong><br>${d3.format(".1f")(d.lift)}× as common as chance<br>${fmt.int(d.k)} of ${fmt.int(d.n)} summited (${fmt.pct(d.rate, 0)})`));

      const nodeSel = svg.append("g").selectAll("g").data(nodes).join("g")
        .attr("transform", (d) => `translate(${px(d.id)},${py(d.id)})`).style("cursor", "pointer");
      nodeSel.filter((d) => planIds.has(d.id)).append("circle").attr("r", (d) => r(d.n) + 4).attr("fill", "none").attr("stroke", COLORS.plan).attr("stroke-width", 3);
      nodeSel.append("circle").attr("r", (d) => r(d.n)).attr("fill", (d) => (d.n >= 10 ? color(d.rate - base.rate) : "#efeae2"))
        .attr("stroke", COLORS.ink).attr("stroke-width", .8);
      nodeSel.append("text").attr("y", (d) => r(d.n) + 15).attr("text-anchor", "middle").attr("font-size", 11.5)
        .attr("font-weight", (d) => (planIds.has(d.id) ? 600 : 400)).attr("fill", COLORS.ink)
        .attr("paint-order", "stroke").attr("stroke", "#fff").attr("stroke-width", 3).text((d) => d.a.label.replace(" per member", ""));
      withTip(nodeSel, (d) => `<strong>${d.a.label}</strong><br>${fmt.int(d.n)} members · ${d.n ? fmt.pct(d.rate, 0) : "–"} summited<br><span class="tt-muted">Links shown: ${edges.filter((l) => l.source === d.id || l.target === d.id).length}. Click to isolate.</span>`);

      const focus = (id) => {
        const near = new Set(id ? [id] : []);
        edges.forEach((l) => { if (l.source === id) near.add(l.target); if (l.target === id) near.add(l.source); });
        nodeSel.attr("opacity", (d) => (!id || near.has(d.id) ? 1 : .18));
        edgeSel.attr("stroke-opacity", (d) => (!id ? .85 : d.source === id || d.target === id ? 1 : .04));
      };
      nodeSel.on("mouseenter", (e, d) => focus(d.id)).on("mouseleave", () => focus(local.pinned))
        .on("click", (e, d) => { local.pinned = local.pinned === d.id ? null : d.id; focus(local.pinned); });
      focus(local.pinned);
    });
  }

  // -------------------------------------------------------------- matrix
  function drawMatrix() {
    const { nodes, links, base } = association(PD.live());
    const planIds = new Set(PD.ATTRS.filter((a) => a.plan(M3.profile)).map((a) => a.id));
    const shown = local.scope === "plan" ? nodes : nodes;
    const color = U.diverging(.35);
    const lookup = new Map();
    links.forEach((l) => { lookup.set(l.source + "|" + l.target, l); lookup.set(l.target + "|" + l.source, l); });
    hint(`Same data as the network, without edge clutter. Colour shows summit share for members with both choices, against the ${fmt.pct(base.rate, 0)} average. A dark outline marks pairs at least ${d3.format(".1f")(local.lift)}× as common as chance. Pairs under ${MIN_PAIR} members are hatched.`);
    const box = document.getElementById("m3-net");
    const size = Math.min(box.clientWidth, 720);
    mount(box, Math.max(360, size), (svg, w) => {
      const left = w < 560 ? 104 : 134, top = w < 560 ? 90 : 112;
      const s = Math.max(10, Math.min(30, (Math.min(w, 760) - left - 6) / shown.length));
      const pattern = U.hatch(svg);
      const g = svg.append("g");
      const order = shown.map((n) => n.id);
      shown.forEach((n, i) => {
        const on = planIds.has(n.id);
        g.append("text").attr("x", left - 6).attr("y", top + i * s + s / 2 + 3.5).attr("text-anchor", "end").attr("font-size", Math.min(11.5, s * .8))
          .attr("font-weight", on ? 700 : 400).attr("fill", on ? COLORS.plan : COLORS.ink).text(n.a.label);
        g.append("text").attr("transform", `translate(${left + i * s + s / 2 + 3},${top - 6}) rotate(-55)`).attr("font-size", Math.min(11.5, s * .8))
          .attr("font-weight", on ? 700 : 400).attr("fill", on ? COLORS.plan : COLORS.ink).text(n.a.label);
      });
      order.forEach((a, i) => order.forEach((b, j) => {
        const l = lookup.get(a + "|" + b);
        if (!l) return;
        const sparse = l.n < MIN_PAIR;
        const rect = g.append("rect").attr("x", left + j * s + .5).attr("y", top + i * s + .5).attr("width", s - 1).attr("height", s - 1).attr("rx", 2)
          .attr("fill", sparse ? pattern : color(l.rate - base.rate))
          .attr("stroke", !sparse && l.lift >= local.lift ? COLORS.ink : "none").attr("stroke-width", 1.4);
        withTip(rect, `<strong>${l.s.a.label} + ${l.t.a.label}</strong><br>${fmt.int(l.n)} members · ${d3.format(".1f")(l.lift)}× as common as chance` +
          (l.n ? `<br>${fmt.int(l.k)} summited (${fmt.pct(l.rate, 0)})` : ""));
      }));
      if (w > 880) U.gradientLegend(svg, left + s * shown.length + 30, top, 170, color, [-.35, .35], [[0, "−35 pts"], [.5, "average"], [1, "+35 pts"]]);
      else U.gradientLegend(svg, 4, 0, 90, color, [-.35, .35], [[0, "−"], [1, "+"]]);
    });
  }

  // --------------------------------------------------------------- icicle
  const LEVELS = [
    { key: "side", title: "Side", label: (v) => `${v} side`, of: (r) => r.side, plan: (p) => p.side },
    { key: "season", title: "Season", label: (v) => v, of: (r) => r.season, plan: (p) => p.season },
    { key: "route", title: "Route", label: (v) => (v === "standard" ? "Standard route" : "Other route"), of: (r) => r.route, plan: (p) => p.route },
    { key: "o2", title: "Oxygen", label: (v) => (v ? "Oxygen" : "No oxygen"), of: (r) => r.o2, plan: (p) => p.o2 },
    { key: "team", title: "Team", label: (v) => ({ s: "Team ≤ 8", m: "Team 9–20", l: "Team > 20" }[v]), of: (r) => r.team, plan: (p) => PD.teamKey(p.team) },
  ];

  function nest(rows, depth = 0) {
    if (depth === LEVELS.length) return [];
    return d3.rollups(rows, (v) => v, LEVELS[depth].of).map(([value, v]) => {
      const t = PD.total(v);
      return { value, depth: depth + 1, n: t.n, k: t.k, rate: t.rate, children: nest(v, depth + 1) };
    });
  }

  function drawTree() {
    const rows = PD.live();
    const total = PD.total(rows);
    const rootData = { value: "All", n: total.n, k: total.k, rate: total.rate, children: nest(rows) };
    const root = d3.hierarchy(rootData).sum((d) => (d.children && d.children.length ? 0 : d.n))
      .sort((a, b) => b.value - a.value);
    const color = U.diverging(.35);
    const plan = M3.profile;
    const nodePath = (n) => n.ancestors().reverse().slice(1).map((a) => a.data.value);
    const samePrefix = (a, b) => a.every((v, i) => v === b[i]);
    const planPath = LEVELS.map((l) => l.plan(plan));

    let focus = root;
    local.path.forEach((v) => {
      const next = focus.children && focus.children.find((c) => c.data.value === v);
      if (next) focus = next;
    });
    const focusPath = nodePath(focus);

    const crumb = document.getElementById("m3-tree-crumb");
    crumb.innerHTML = "";
    const addCrumb = (label, path) => {
      const b = document.createElement("button");
      b.type = "button"; b.textContent = label;
      b.addEventListener("click", () => { local.path = path; drawTree(); });
      crumb.append(b, " › ");
    };
    addCrumb("All plans", []);
    focusPath.forEach((v, i) => addCrumb(LEVELS[i].label(v), focusPath.slice(0, i + 1)));
    crumb.append(`${fmt.int(focus.data.n)} members · ${focus.data.n ? fmt.pct(focus.data.k / focus.data.n, 0) : "–"} summited`);

    mount(document.getElementById("m3-tree"), 300, (svg, w, h) => {
      if (!total.n) { U.emptyNote(svg, w, h, "No records in this period."); return; }
      const left = w < 520 ? 0 : 62, top = 2;
      const rowH = (h - top) / (LEVELS.length + 1);
      const partition = d3.partition().size([1, 1]);
      partition(root);
      const x = d3.scaleLinear().domain([focus.x0, focus.x1]).range([left, w]).clamp(true);
      const pattern = U.hatch(svg);
      const g = svg.append("g");
      if (left) ["All", ...LEVELS.map((l) => l.title)].forEach((t, i) => {
        g.append("text").attr("x", 0).attr("y", top + rowH * i + rowH / 2 + 4).attr("font-size", 11).attr("fill", COLORS.muted).text(t);
      });
      const cells = root.descendants().filter((d) => x(d.x1) - x(d.x0) > .3);
      const cell = g.selectAll("g").data(cells).join("g")
        .attr("transform", (d) => `translate(${x(d.x0)},${top + d.depth * rowH})`).style("cursor", "pointer");
      const isPlan = (d) => d.depth > 0 && samePrefix(nodePath(d), planPath);
      cell.append("rect")
        .attr("width", (d) => Math.max(1, x(d.x1) - x(d.x0) - 1)).attr("height", rowH - 2).attr("rx", 2)
        .attr("fill", (d) => (d.data.n < 10 ? pattern : color(d.data.k / d.data.n - total.rate)))
        .attr("stroke", (d) => (isPlan(d) ? COLORS.plan : "none")).attr("stroke-width", 3);
      cell.filter((d) => x(d.x1) - x(d.x0) > 56).append("text").attr("x", 6).attr("y", rowH / 2 + 4).attr("font-size", 11.5)
        .attr("fill", (d) => (d.data.n < 10 ? COLORS.ink : U.inkOn(color(d.data.k / d.data.n - total.rate))))
        .text((d) => {
          const name = d.depth ? LEVELS[d.depth - 1].label(d.data.value) : "All plans";
          const width = x(d.x1) - x(d.x0);
          const full = `${name} · ${fmt.pct(d.data.k / d.data.n, 0)}`;
          return full.length * 6.2 < width ? full : name.length * 6.2 < width ? name : "";
        });
      withTip(cell, (d) => `<strong>${d.depth ? d.ancestors().reverse().slice(1).map((a) => LEVELS[a.depth - 1].label(a.data.value)).join(" › ") : "All plans"}</strong><br>${fmt.int(d.data.k)} of ${fmt.int(d.data.n)} members summited (${fmt.pct(d.data.k / d.data.n, 0)})` +
        (d.data.n < 10 ? `<br><span class="tt-muted">Fewer than 10 records</span>` : ""));
      cell.on("click", (e, d) => { U.tipHide(); local.path = nodePath(d); drawTree(); });
    });
  }

  function applyBranch() {
    const patch = {};
    local.path.forEach((v, i) => {
      const key = LEVELS[i].key;
      if (key === "team") {
        patch.team = { s: 6, m: 12, l: 30 }[v];
      } else patch[key] = v;
    });
    M3.setProfile(patch);
  }

  function drawConnections() {
    document.getElementById("m3-lift-out").textContent = d3.format(".1f")(local.lift) + "×";
    if (local.view === "net") drawNetwork(); else drawMatrix();
  }

  function render() {
    drawConnections();
    drawTree();
  }

  // Scripts load at the end of <body>, before app.js boots, so the page is ready here.
  (function setup() {
    M3.register("links", render);
    const setView = U.seg("m3-net-view", local.view, (v) => { local.view = v; drawConnections(); });
    U.seg("m3-net-scope", local.scope, (v) => { local.scope = v; drawConnections(); });
    document.getElementById("m3-lift").addEventListener("input", (e) => { local.lift = +e.target.value; drawConnections(); });
    document.getElementById("m3-tree-apply").addEventListener("click", applyBranch);
    window.PlanLinks = { setView(v) { local.view = v; setView(v); drawConnections(); } };
  })();
})();
