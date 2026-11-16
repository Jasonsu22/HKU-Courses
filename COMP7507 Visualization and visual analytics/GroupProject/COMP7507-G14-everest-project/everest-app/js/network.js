/* Page 1 · Network of expedition nations and trekking agencies. */
(function () {
  "use strict";

  const { fmt, COLORS, mount, withTip } = U;
  const local = { min: 4, size: "expeditions", pinned: null };

  function build(rows, min) {
    const pairs = d3.rollups(rows.filter((r) => r.agency && r.nation),
      (v) => ({ n: v.length, k: v.filter((r) => r.success).length }),
      (r) => "N:" + r.nation, (r) => "A:" + r.agency);
    const links = [];
    pairs.forEach(([nation, list]) => list.forEach(([agency, s]) => {
      if (s.n >= min) links.push({ source: nation, target: agency, ...s });
    }));
    const map = new Map();
    const touch = (id) => {
      if (!map.has(id)) map.set(id, { id, label: id.slice(2), type: id[0] === "N" ? "nation" : "agency", n: 0, k: 0, degree: 0 });
      return map.get(id);
    };
    links.forEach((l) => {
      [l.source, l.target].forEach((id) => { const d = touch(id); d.n += l.n; d.k += l.k; d.degree += 1; });
    });
    return { nodes: [...map.values()].sort((a, b) => d3.ascending(a.id, b.id)), links };
  }

  // Brandes' algorithm for an unweighted graph (slides: betweenness centrality).
  function betweenness(nodes, links) {
    const adj = new Map(nodes.map((n) => [n.id, []]));
    links.forEach((l) => {
      const s = l.source.id || l.source, t = l.target.id || l.target;
      adj.get(s).push(t); adj.get(t).push(s);
    });
    const score = new Map(nodes.map((n) => [n.id, 0]));
    nodes.forEach(({ id: s }) => {
      const stack = [], pred = new Map(), sigma = new Map(), dist = new Map();
      nodes.forEach((n) => { pred.set(n.id, []); sigma.set(n.id, 0); dist.set(n.id, -1); });
      sigma.set(s, 1); dist.set(s, 0);
      const q = [s];
      for (let i = 0; i < q.length; i++) {
        const v = q[i];
        stack.push(v);
        adj.get(v).forEach((w) => {
          if (dist.get(w) < 0) { q.push(w); dist.set(w, dist.get(v) + 1); }
          if (dist.get(w) === dist.get(v) + 1) { sigma.set(w, sigma.get(w) + sigma.get(v)); pred.get(w).push(v); }
        });
      }
      const delta = new Map(nodes.map((n) => [n.id, 0]));
      while (stack.length) {
        const w = stack.pop();
        pred.get(w).forEach((v) => delta.set(v, delta.get(v) + (sigma.get(v) / sigma.get(w)) * (1 + delta.get(w))));
        if (w !== s) score.set(w, score.get(w) + delta.get(w));
      }
    });
    nodes.forEach((n) => { n.between = score.get(n.id) / 2; });
  }

  function draw(rows, rangeLabel) {
    document.getElementById("m1-net-out").textContent = local.min;
    const { nodes, links } = build(rows, local.min);
    const withAgency = rows.filter((r) => r.agency && r.nation).length;
    const base = rows.length ? rows.filter((r) => r.success).length / rows.length : 0;
    document.getElementById("m1-net-hint").innerHTML =
      `${rangeLabel}: ${fmt.int(nodes.length)} nodes and ${fmt.int(links.length)} connections, from ${fmt.int(withAgency)} expeditions with a recorded agency. Circles are nations, squares are agencies. Colour shows success against the ${fmt.pct(base, 0)} average for the period. Click a node to isolate it. These are associations, not a ranking of quality.`;
    betweenness(nodes, links);
    const color = U.diverging(.35);

    mount(document.getElementById("m1-net"), 620, (svg, w, h) => {
      if (nodes.length < 2) { U.emptyNote(svg, w, h, "No connections at this threshold. Lower it or widen the period."); document.getElementById("m1-net-side").innerHTML = ""; return; }
      const metric = (n) => (local.size === "expeditions" ? n.n : n.between);
      const r = d3.scaleSqrt().domain([0, d3.max(nodes, metric) || 1]).range([4, 26]);
      // Deterministic start + fixed tick count: the same data draws the same picture.
      nodes.forEach((n, i) => {
        const t = (i / nodes.length) * 2 * Math.PI;
        n.x = w / 2 + (w / 3) * Math.cos(t); n.y = h / 2 + (h / 3) * Math.sin(t);
      });
      const sim = d3.forceSimulation(nodes)
        .force("link", d3.forceLink(links).id((d) => d.id).distance(70).strength(.45))
        .force("charge", d3.forceManyBody().strength(-300))
        .force("x", d3.forceX(w / 2).strength(.07)).force("y", d3.forceY(h / 2).strength(.11))
        .force("collide", d3.forceCollide((d) => r(metric(d)) + 5))
        .stop();
      sim.tick(300);
      nodes.forEach((n) => {
        n.x = Math.max(34, Math.min(w - 34, n.x));
        n.y = Math.max(32, Math.min(h - 18, n.y));
      });

      U.gradientLegend(svg, 4, 0, 170, color, [-.35, .35], [[0, "−35 pts"], [.5, "average"], [1, "+35 pts"]]);
      const edge = svg.append("g").selectAll("line").data(links).join("line")
        .attr("x1", (d) => d.source.x).attr("y1", (d) => d.source.y)
        .attr("x2", (d) => d.target.x).attr("y2", (d) => d.target.y)
        .attr("stroke", "#8d877c").attr("stroke-width", (d) => Math.min(6, .7 + d.n / 6))
        .call((s) => withTip(s, (d) => `<strong>${d.source.label} × ${d.target.label}</strong><br>${fmt.int(d.k)} of ${fmt.int(d.n)} expeditions reached the summit`));
      const node = svg.append("g").selectAll("g").data(nodes).join("g")
        .attr("transform", (d) => `translate(${d.x},${d.y})`).style("cursor", "pointer");
      const fill = (d) => (d.n >= 5 ? color(d.k / d.n - base) : "#efeae2");
      node.filter((d) => d.type === "nation").append("circle").attr("r", (d) => r(metric(d)));
      node.filter((d) => d.type === "agency").append("rect")
        .attr("x", (d) => -r(metric(d)) * .88).attr("y", (d) => -r(metric(d)) * .88)
        .attr("width", (d) => r(metric(d)) * 1.76).attr("height", (d) => r(metric(d)) * 1.76).attr("rx", 3);
      node.selectAll("circle,rect").attr("fill", fill).attr("stroke", COLORS.ink).attr("stroke-width", .9);
      const labelled = new Set([...nodes].sort((a, b) => metric(b) - metric(a)).slice(0, w < 620 ? 8 : 16).map((d) => d.id));
      node.filter((d) => labelled.has(d.id)).append("text").attr("y", (d) => r(metric(d)) + 13).attr("text-anchor", "middle")
        .attr("font-size", 11).attr("fill", COLORS.ink).attr("paint-order", "stroke").attr("stroke", "#fff").attr("stroke-width", 3)
        .text((d) => (d.label.length > 20 ? d.label.slice(0, 19) + "…" : d.label));
      withTip(node, (d) => `<strong>${d.label}</strong> (${d.type})<br>${fmt.int(d.k)} of ${fmt.int(d.n)} shown expeditions reached the summit (${fmt.pct(d.k / d.n, 0)})<br><span class="tt-muted">Degree ${d.degree} · betweenness ${d3.format(".0f")(d.between)}</span>`);

      const focus = (id) => {
        const near = new Set(id ? [id] : []);
        links.forEach((l) => { if (l.source.id === id) near.add(l.target.id); if (l.target.id === id) near.add(l.source.id); });
        node.attr("opacity", (d) => (!id || near.has(d.id) ? 1 : .15));
        edge.attr("stroke-opacity", (d) => (!id ? .5 : d.source.id === id || d.target.id === id ? .95 : .04));
      };
      node.on("mouseenter", (e, d) => focus(d.id)).on("mouseleave", () => focus(local.pinned))
        .on("click", (e, d) => { local.pinned = local.pinned === d.id ? null : d.id; focus(local.pinned); });
      focus(nodes.some((n) => n.id === local.pinned) ? local.pinned : null);

      const top = (key, fmtV) => [...nodes].sort((a, b) => b[key] - a[key]).slice(0, 6)
        .map((n) => `<tr><td>${n.label}</td><td>${fmtV(n[key])}</td></tr>`).join("");
      document.getElementById("m1-net-side").innerHTML = `
        <h3>Most connected (degree)</h3><table>${top("degree", (v) => v)}</table>
        <h3>Bridges between groups (betweenness)</h3><table>${top("between", d3.format(".0f"))}</table>
        <p>Betweenness counts how often a node sits on the shortest path between two others, so a high value marks a bridge between communities.</p>`;
    });
  }

  window.OperatorNet = {
    draw,
    setup(redraw) {
      U.seg("m1-net-size", local.size, (v) => { local.size = v; redraw(); });
      document.getElementById("m1-net-min").addEventListener("input", (e) => { local.min = +e.target.value; redraw(); });
    },
  };
})();
