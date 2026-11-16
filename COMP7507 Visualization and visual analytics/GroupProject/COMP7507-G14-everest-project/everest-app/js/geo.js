/* Module 02 — geographic view: 2D hillshade map + 3D terrain (three.js). */
(function () {
  "use strict";

  const D = window.EVEREST_DATA;
  const T = window.TERRAIN;
  const F = window.TERRAIN_FEATURES;
  const { fmt, COLORS, withTip } = U;

  const SIDE = { south: COLORS.south, north: COLORS.north };
  // Filter-driven view state: reach(side, elevation) gives the share of filtered
  // expeditions that got that high, so the map and 3D view follow the charts.
  const view = { reach: null, alt: null, contours: true };
  const shareOf = (c) => (view.reach ? view.reach(c.side, c.elev) : null);
  const META = T.meta;
  const BBOX = META.bbox;
  const MESH = META.mesh;

  // ---------------------------------------------------------------- data
  function decodeInt16(b64) {
    const bin = atob(b64);
    const buf = new ArrayBuffer(bin.length);
    const view = new Uint8Array(buf);
    for (let i = 0; i < bin.length; i++) view[i] = bin.charCodeAt(i);
    return new Int16Array(buf);
  }
  const ELEV = decodeInt16(T.elev);

  function heightAt(lon, lat) {
    const fx = ((lon - BBOX.west) / (BBOX.east - BBOX.west)) * (MESH.nx - 1);
    const fy = ((BBOX.north - lat) / (BBOX.north - BBOX.south)) * (MESH.ny - 1);
    const x0 = Math.max(0, Math.min(MESH.nx - 2, Math.floor(fx)));
    const y0 = Math.max(0, Math.min(MESH.ny - 2, Math.floor(fy)));
    const tx = Math.max(0, Math.min(1, fx - x0));
    const ty = Math.max(0, Math.min(1, fy - y0));
    const i = y0 * MESH.nx + x0;
    const v00 = ELEV[i], v10 = ELEV[i + 1];
    const v01 = ELEV[i + MESH.nx], v11 = ELEV[i + MESH.nx + 1];
    return (v00 * (1 - tx) + v10 * tx) * (1 - ty) + (v01 * (1 - tx) + v11 * tx) * ty;
  }

  const RECORD_MEDIAN = {};
  ["south", "north"].forEach((side) => {
    (D.camps[side] || []).forEach((c) => {
      const key = c.label === "Smt" ? "Summit" : c.label;
      RECORD_MEDIAN[side + "|" + key] = c;
    });
  });

  const DATA_CAMP_LABEL = { BC: "BC", C1: "C1", C2: "C2", C3: "C3", C4: "C4", ABC: "ABC", Summit: "Summit" };

  function recordFor(camp) {
    const key = camp.id === "SUM" ? "Summit" : camp.short;
    return RECORD_MEDIAN[camp.side + "|" + DATA_CAMP_LABEL[key]];
  }

  function campTip(camp) {
    const rec = recordFor(camp);
    const sideName = camp.side === "south" ? "South" : "North";
    let html = `<strong>${sideName} · ${camp.label}</strong><br>${fmt.int(camp.elev)} m (OSM)`;
    if (rec && rec.elev) {
      html += `<br><span class="tt-muted">records median ${fmt.int(rec.elev)} m`;
      if (rec.share != null) html += ` · listed by ${fmt.pct(rec.share, 0)}`;
      html += "</span>";
    }
    if (camp.id === "SUM" && view.reach) {
      const s = view.reach("south", camp.elev), n = view.reach("north", camp.elev);
      html += `<br>Reached under these filters: south ${s == null ? "–" : fmt.pct(s, 0)}, north ${n == null ? "–" : fmt.pct(n, 0)}`;
    } else {
      const share = shareOf(camp);
      if (share != null) html += `<br>${fmt.pct(share, 0)} of filtered ${sideName.toLowerCase()} expeditions got this high`;
    }
    return html;
  }

  // ------------------------------------------------------------- 2D map
  const bboxPoly = {
    type: "Polygon",
    coordinates: [[
      [BBOX.west, BBOX.south], [BBOX.east, BBOX.south],
      [BBOX.east, BBOX.north], [BBOX.west, BBOX.north], [BBOX.west, BBOX.south],
    ]],
  };

  let mapProj = null;
  // Ring the camps nearest a hovered altitude (linked with the funnel and profile).
  function highlightMap() {
    const svg = d3.select("#geo-map svg");
    if (svg.empty() || !mapProj) return;
    svg.selectAll("g.geo-hl").remove();
    if (view.alt == null) return;
    const layer = svg.append("g").attr("class", "geo-hl").attr("pointer-events", "none");
    Object.values(F.camps).forEach((list) => {
      const near = d3.least(list, (c) => Math.abs(c.elev - view.alt));
      if (!near || Math.abs(near.elev - view.alt) > 350) return;
      const [x, y] = mapProj([near.lon, near.lat]);
      layer.append("circle").attr("cx", x).attr("cy", y).attr("r", 13).attr("fill", "none")
        .attr("stroke", COLORS.plan).attr("stroke-width", 3);
    });
  }

  function drawMap() {
    const el = document.getElementById("geo-map");
    if (!el || !el.clientWidth) return;
    const w = el.clientWidth;
    const h = el.clientHeight;
    d3.select(el).selectAll("*").remove();
    const svg = d3.select(el).append("svg").attr("width", w).attr("height", h);

    const pad = 14;
    const unit = d3.geoMercator().scale(1).translate([0, 0]);
    const uNW = unit([BBOX.west, BBOX.north]);
    const uSE = unit([BBOX.east, BBOX.south]);
    const spanX = Math.abs(uSE[0] - uNW[0]);
    const spanY = Math.abs(uSE[1] - uNW[1]);
    const scale = Math.min((w - 2 * pad) / spanX, (h - 2 * pad) / spanY);
    const proj = d3.geoMercator()
      .scale(scale)
      .translate([w / 2 - ((uNW[0] + uSE[0]) / 2) * scale,
                  h / 2 - ((uNW[1] + uSE[1]) / 2) * scale]);
    const nw = proj([BBOX.west, BBOX.north]);
    const se = proj([BBOX.east, BBOX.south]);

    const defs = svg.append("defs");
    defs.append("clipPath").attr("id", "geo-clip")
      .append("rect").attr("x", nw[0]).attr("y", nw[1])
      .attr("width", se[0] - nw[0]).attr("height", se[1] - nw[1]);

    svg.append("image")
      .attr("href", "data/terrain/terrain-shade.jpg")
      .attr("x", nw[0]).attr("y", nw[1])
      .attr("width", se[0] - nw[0]).attr("height", se[1] - nw[1])
      .attr("preserveAspectRatio", "none");

    const g = svg.append("g").attr("clip-path", "url(#geo-clip)");

    // graticule
    const grat = g.append("g").attr("opacity", 0.42);
    for (let lon = 86.8; lon <= 86.96; lon += 0.05) {
      const a = proj([lon, BBOX.south]), b = proj([lon, BBOX.north]);
      grat.append("line").attr("x1", a[0]).attr("y1", a[1]).attr("x2", b[0]).attr("y2", b[1])
        .attr("stroke", "#fff").attr("stroke-width", 0.8).attr("stroke-dasharray", "3 4");
    }
    for (let lat = 28.0; lat <= 28.14; lat += 0.05) {
      const a = proj([BBOX.west, lat]), b = proj([BBOX.east, lat]);
      grat.append("line").attr("x1", a[0]).attr("y1", a[1]).attr("x2", b[0]).attr("y2", b[1])
        .attr("stroke", "#fff").attr("stroke-width", 0.8).attr("stroke-dasharray", "3 4");
    }

    // contour plot from the same elevation grid as the 3D mesh
    if (view.contours) {
      const toLonLat = d3.geoTransform({
        point(px, py) {
          const lon = BBOX.west + (px / (MESH.nx - 1)) * (BBOX.east - BBOX.west);
          const lat = BBOX.north - (py / (MESH.ny - 1)) * (BBOX.north - BBOX.south);
          const p = proj([lon, lat]);
          this.stream.point(p[0], p[1]);
        },
      });
      const path = d3.geoPath(toLonLat);
      const levels = d3.contours().size([MESH.nx, MESH.ny]).thresholds(d3.range(5000, 8600, 500))(Array.from(ELEV));
      const cg = g.append("g").attr("fill", "none");
      levels.forEach((c) => {
        cg.append("path").attr("d", path(c)).attr("stroke", "#fff")
          .attr("stroke-width", c.value % 1000 === 0 ? 1.1 : .6).attr("stroke-opacity", c.value % 1000 === 0 ? .8 : .55);
      });
    }

    // routes: one segment per camp pair; width shows the share that got to the upper camp
    Object.entries(F.routes).forEach(([side, ids]) => {
      // the north approach starts at ABC: BC-N -> ABC crosses half the massif
      const chain = side === "north" ? ids.slice(1) : ids;
      const camps = chain.map((id) => F.camps[side].find((x) => x.id === id));
      camps.slice(1).forEach((c, i) => {
        const a = proj([camps[i].lon, camps[i].lat]), b = proj([c.lon, c.lat]);
        const s = view.reach ? view.reach(side, c.elev) : null;
        const width = s == null ? 2.2 : 1.5 + s * 7;
        g.append("line").attr("x1", a[0]).attr("y1", a[1]).attr("x2", b[0]).attr("y2", b[1])
          .attr("stroke", "#fff").attr("stroke-width", width + 2.4).attr("stroke-opacity", .85).attr("stroke-linecap", "round");
        g.append("line").attr("x1", a[0]).attr("y1", a[1]).attr("x2", b[0]).attr("y2", b[1])
          .attr("stroke", SIDE[side]).attr("stroke-width", width).attr("stroke-linecap", "round");
      });
    });
    mapProj = proj;
    highlightMap();

    // ---- label placement with simple collision avoidance
    const placed = [];
    const overlap = (a, b) => !(a.x + a.w < b.x || b.x + b.w < a.x || a.y + a.h < b.y || b.y + b.h < a.y);
    const measure = (txt, size) => Math.max(24, txt.length * size * 0.6);
    function placeLabel(px, py, lines, opts = {}) {
      const size = opts.size || 11;
      const width = Math.max(...lines.map((l) => measure(l.text, l.size || size))) + 14;
      const height = lines.length > 1 ? size + 16 : size + 8;
      const prefer = opts.anchor || "start";
      const cands = [];
      for (const dy of [0, -15, 15, -30, 30, -45, 45]) {
        const box = {
          x: prefer === "start" ? px + 9 : prefer === "end" ? px - 9 - width : px - width / 2,
          y: py - height + dy,
          w: width, h: height,
        };
        if (!placed.some((p) => overlap(p, box))) {
          placed.push(box);
          return box;
        }
        cands.push(box);
      }
      return null;
    }

    const labelLayer = svg.append("g");
    function drawLabel(box, px, py, lines, opts = {}) {
      if (!box) return;
      if (Math.abs(box.x + 4 - px) > 14 || Math.abs(box.y + 8 - py) > 16) {
        labelLayer.append("line")
          .attr("x1", px).attr("y1", py)
          .attr("x2", box.x + (box.x > px ? 2 : box.w - 2)).attr("y2", box.y + box.h / 2)
          .attr("stroke", "rgba(255,255,255,.9)").attr("stroke-width", 1.4);
      }
      const t = labelLayer.append("text")
        .attr("x", box.x + 5).attr("y", box.y + (lines.length > 1 ? 11 : box.h - 6))
        .attr("font-size", opts.size || 11)
        .attr("font-weight", opts.weight || 550)
        .attr("fill", opts.fill || "#1b1e22")
        .attr("stroke", "rgba(255,255,255,.92)")
        .attr("stroke-width", 3.2)
        .attr("paint-order", "stroke");
      lines.forEach((l, i) => {
        t.append("tspan")
          .attr("x", box.x + 5)
          .attr("dy", i === 0 ? 0 : (l.size || 9.5) + 2)
          .attr("font-size", l.size || (opts.size || 11))
          .attr("font-weight", l.weight || 400)
          .attr("fill", l.fill || opts.fill || "#1b1e22")
          .text(l.text);
      });
    }

    // peaks first (context), then camps, then summit
    F.peaks.forEach((p) => {
      const [x, y] = proj([p.lon, p.lat]);
      g.append("path")
        .attr("d", `M${x},${y - 4} L${x + 4},${y + 3} L${x - 4},${y + 3} Z`)
        .attr("fill", "rgba(255,255,255,.75)").attr("stroke", "#4a463f").attr("stroke-width", 1);
      if (!p.hideLabel) {
        const box = placeLabel(x, y, [{ text: p.label }], { size: 10.5, anchor: p.anchor, fill: "#4a463f" });
        drawLabel(box, x, y, [{ text: p.label }], { size: 10.5, fill: "#4a463f", weight: 400 });
      }
      g.append("circle").attr("cx", x).attr("cy", y).attr("r", 10).attr("fill", "transparent")
        .call((sel) => withTip(sel, `<strong>${p.label}</strong><br>context peak`));
    });

    const seen = new Set();
    const camps = [];
    Object.entries(F.camps).forEach(([side, list]) => {
      list.forEach((c) => {
        if (c.id === "SUM" && seen.has("SUM")) return;
        seen.add(c.id);
        camps.push(c);
      });
    });
    camps.sort((a, b) => (a.id === "SUM" ? 1 : b.id === "SUM" ? -1 : 0));

    camps.forEach((c) => {
      const [x, y] = proj([c.lon, c.lat]);
      const isSummit = c.id === "SUM";
      const isBC = c.kind === "bc";
      if (isSummit) {
        g.append("path")
          .attr("d", `M${x},${y - 7} L${x + 6.5},${y + 4} L${x - 6.5},${y + 4} Z`)
          .attr("fill", "#fff").attr("stroke", "#1b1e22").attr("stroke-width", 1.8);
      } else {
        g.append("circle").attr("cx", x).attr("cy", y).attr("r", isBC ? 6.5 : 5.2)
          .attr("fill", SIDE[c.side]).attr("stroke", "#fff").attr("stroke-width", 1.8);
      }
      const name = isSummit ? "Summit" : (isBC ? c.label : c.short);
      const share = isSummit ? null : shareOf(c);
      const lines = [{ text: name, weight: isSummit ? 650 : 600 },
                     { text: fmt.int(c.elev) + " m" + (share == null ? "" : " · " + fmt.pct(share, 0)), size: 10, weight: 400, fill: "#3c4046" }];
      const box = placeLabel(x, y, lines, { size: 12, anchor: c.dx < 0 ? "end" : "start" });
      drawLabel(box, x, y, lines, { size: 12 });
      g.append("circle").attr("cx", x).attr("cy", y).attr("r", 13).attr("fill", "transparent")
        .call((sel) => withTip(sel, () => campTip(c)));
    });

    // scale bar
    const midLat = (BBOX.north + BBOX.south) / 2;
    const a = proj([BBOX.west, midLat]), b = proj([BBOX.east, midLat]);
    const mPerPx = (d3.geoDistance([BBOX.west, midLat], [BBOX.east, midLat]) * 6371 * 1000) / (b[0] - a[0]);
    let barKm = 2, barPx = (barKm * 1000) / mPerPx;
    if (barPx > 170) { barKm = 1; barPx = (1000) / mPerPx; }
    if (barPx < 55) { barKm = 5; barPx = 5000 / mPerPx; }
    const sb = svg.append("g").attr("transform", `translate(${nw[0] + 10},${se[1] - 14})`);
    sb.append("line").attr("x1", 0).attr("x2", barPx).attr("y1", 0).attr("y2", 0)
      .attr("stroke", "#1b1e22").attr("stroke-width", 2);
    sb.append("line").attr("x1", 0).attr("x2", 0).attr("y1", -4).attr("y2", 4).attr("stroke", "#1b1e22").attr("stroke-width", 2);
    sb.append("line").attr("x1", barPx).attr("x2", barPx).attr("y1", -4).attr("y2", 4).attr("stroke", "#1b1e22").attr("stroke-width", 2);
    sb.append("text").attr("x", barPx / 2).attr("y", -6).attr("text-anchor", "middle")
      .attr("font-size", 10).attr("fill", "#1b1e22").text(barKm + " km");

    // north arrow
    const na = svg.append("g").attr("transform", `translate(${w - 26},${nw[1] + 26})`);
    na.append("path").attr("d", "M0,-9 L4,5 L0,2 L-4,5 Z").attr("fill", "#1b1e22");
    na.append("text").attr("x", 0).attr("y", 17).attr("text-anchor", "middle")
      .attr("font-size", 10).attr("fill", "#1b1e22").text("N");
  }

  // ----------------------------------------------------------- 3D terrain
  let three = null;

  function webglSupported() {
    try {
      const c = document.createElement("canvas");
      return !!(window.WebGLRenderingContext &&
        (c.getContext("webgl") || c.getContext("experimental-webgl")));
    } catch (e) { return false; }
  }

  function init3D() {
    if (three) return three;
    const host = document.getElementById("geo-3d");
    if (!host) return null;
    if (!window.THREE || !webglSupported()) {
      host.innerHTML = `<div class="geo-fallback">3D needs WebGL, which this browser has disabled.
        The map on the left shows the same terrain.</div>`;
      return null;
    }
    const w = Math.max(320, host.clientWidth);
    const h = Math.max(320, host.clientHeight);

    let renderer;
    try {
      renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    } catch (err) {
      host.innerHTML = `<div class="geo-fallback">3D could not start in this browser (WebGL).
        The map on the left shows the same terrain.</div>`;
      return null;
    }
    renderer.setPixelRatio(Math.min(2, window.devicePixelRatio || 1));
    renderer.setSize(w, h, false);
    if ("outputEncoding" in renderer) renderer.outputEncoding = THREE.sRGBEncoding;
    host.appendChild(renderer.domElement);

    const scene = new THREE.Scene();
    scene.fog = new THREE.Fog(0xeef2f5, 42, 88);
    const camera = new THREE.PerspectiveCamera(40, w / h, 0.1, 400);
    const { widthKm, heightKm } = META;
    const EX = 1.7;
    const vs = 0.001 * EX;
    const base = META.elevation.min;

    // --- terrain mesh
    const pos = new Float32Array(MESH.nx * MESH.ny * 3);
    const uv = new Float32Array(MESH.nx * MESH.ny * 2);
    for (let j = 0; j < MESH.ny; j++) {
      for (let i = 0; i < MESH.nx; i++) {
        const k = j * MESH.nx + i;
        pos[k * 3] = (i / (MESH.nx - 1) - 0.5) * widthKm;
        pos[k * 3 + 1] = (ELEV[k] - base) * vs;
        pos[k * 3 + 2] = (j / (MESH.ny - 1) - 0.5) * heightKm;
        uv[k * 2] = i / (MESH.nx - 1);
        uv[k * 2 + 1] = 1 - j / (MESH.ny - 1);
      }
    }
    const idx = [];
    for (let j = 0; j < MESH.ny - 1; j++) {
      for (let i = 0; i < MESH.nx - 1; i++) {
        const a = j * MESH.nx + i;
        const b = a + 1;
        const c = a + MESH.nx;
        const d = c + 1;
        idx.push(a, c, b, b, c, d);
      }
    }
    const geo = new THREE.BufferGeometry();
    geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
    geo.setAttribute("uv", new THREE.BufferAttribute(uv, 2));
    geo.setIndex(idx);
    geo.computeVertexNormals();

    // Embedded as a data URL: WebGL can't read image files when the page is opened by double-click.
    const tex = new THREE.TextureLoader().load(window.TERRAIN_TEXTURE);
    if ("encoding" in tex) tex.encoding = THREE.sRGBEncoding;
    tex.anisotropy = renderer.capabilities.getMaxAnisotropy();
    const surface = new THREE.Mesh(geo, new THREE.MeshLambertMaterial({ map: tex, color: 0xe9e9e9 }));
    scene.add(surface);

    scene.add(new THREE.HemisphereLight(0xffffff, 0x46525c, 0.72));
    const sun = new THREE.DirectionalLight(0xfff3e3, 0.9);
    sun.position.set(-widthKm * 0.6, 18, -heightKm * 0.5);
    scene.add(sun);

    // --- markers
    const markers = [];
    const markerGeo = new THREE.SphereGeometry(0.13, 14, 14);
    const summitGeo = new THREE.SphereGeometry(0.2, 16, 16);
    const seen = new Set();
    Object.entries(F.camps).forEach(([side, list]) => {
      list.forEach((c) => {
        if (c.id === "SUM" && seen.has("SUM")) return;
        seen.add(c.id);
        const x = (c.lon - BBOX.west) / (BBOX.east - BBOX.west) * widthKm - widthKm / 2;
        const z = (BBOX.north - c.lat) / (BBOX.north - BBOX.south) * heightKm - heightKm / 2;
        const y = (heightAt(c.lon, c.lat) - base) * vs + 0.12;
        const isSummit = c.id === "SUM";
        const m = new THREE.Mesh(
          isSummit ? summitGeo : markerGeo,
          new THREE.MeshBasicMaterial({ color: isSummit ? 0xffffff : (side === "south" ? 0xeb6834 : 0x2a78d6) })
        );
        m.position.set(x, y, z);
        scene.add(m);
        markers.push({ c, x, y, z, isSummit, mesh: m });
      });
    });

    // --- route lines
    Object.entries(F.routes).forEach(([side, ids]) => {
      // in 3D the north approach starts at ABC: BC-N -> ABC crosses half the massif
      const chain = side === "north" ? ids.slice(1) : ids;
      const pts = chain.map((id) => {
        const c = F.camps[side].find((x) => x.id === id);
        return new THREE.Vector3(
          (c.lon - BBOX.west) / (BBOX.east - BBOX.west) * widthKm - widthKm / 2,
          (heightAt(c.lon, c.lat) - base) * vs + 0.06,
          (BBOX.north - c.lat) / (BBOX.north - BBOX.south) * heightKm - heightKm / 2
        );
      });
      const casing = new THREE.Line(
        new THREE.BufferGeometry().setFromPoints(pts),
        new THREE.LineBasicMaterial({ color: 0x2c241c, transparent: true, opacity: 0.5 })
      );
      scene.add(casing);
      const raised = pts.map((q) => new THREE.Vector3(q.x, q.y + 0.05, q.z));
      const line = new THREE.Line(
        new THREE.BufferGeometry().setFromPoints(raised),
        new THREE.LineDashedMaterial({
          color: side === "south" ? 0xffffff : 0xd7edf7,
          dashSize: 0.34, gapSize: 0.2,
        })
      );
      line.computeLineDistances();
      scene.add(line);
    });

    // --- HTML labels
    const overlay = document.createElement("div");
    overlay.className = "geo-overlay";
    host.appendChild(overlay);
    markers.forEach((m) => {
      const d = document.createElement("div");
      d.className = "geo-label" + (m.isSummit ? " is-summit" : "");
      const room = m.c.name || m.c.short;
      d.textContent = m.isSummit ? "Summit"
        : (m.c.kind === "bc" ? (m.c.side === "south" ? "S BC" : "N BC")
                             : (m.c.side === "south" ? "S·" : "N·") + m.c.short);
      m.priority = m.isSummit ? 0 : (m.c.kind === "bc" ? 1 : 2);
      d.style.color = m.isSummit ? "#111" : (m.c.side === "south" ? "#8a3f1f" : "#16394a");
      d.dataset.side = m.c.side;
      overlay.appendChild(d);
      m.el = d;
      m.baseLabel = d.textContent;
    });

    // --- orbit
    const tx = ((86.906 - BBOX.west) / (BBOX.east - BBOX.west)) * widthKm - widthKm / 2;
    const tz = ((BBOX.north - 28.012) / (BBOX.north - BBOX.south)) * heightKm - heightKm / 2;
    const target = new THREE.Vector3(tx, 2.8, tz);
    const state = { theta: -0.5, phi: 0.9, radius: 24 };
    const goal = { ...state };
    let dragging = false;
    let moved = false;

    function reset() {
      goal.theta = -0.5; goal.phi = 0.9; goal.radius = 24;
    }
    function onPointerDown(e) {
      dragging = true; moved = false;
      renderer.domElement.setPointerCapture(e.pointerId);
      renderer.domElement.dataset.px = e.clientX;
      renderer.domElement.dataset.py = e.clientY;
    }
    function onPointerMove(e) {
      if (!dragging) return;
      const px = +renderer.domElement.dataset.px || e.clientX;
      const py = +renderer.domElement.dataset.py || e.clientY;
      const dx = e.clientX - px;
      const dy = e.clientY - py;
      if (Math.abs(dx) + Math.abs(dy) > 2) moved = true;
      goal.theta -= dx * 0.006;
      goal.phi = Math.max(0.18, Math.min(1.42, goal.phi - dy * 0.004));
      renderer.domElement.dataset.px = e.clientX;
      renderer.domElement.dataset.py = e.clientY;
    }
    function onPointerUp() { dragging = false; }
    renderer.domElement.addEventListener("pointerdown", onPointerDown);
    renderer.domElement.addEventListener("pointermove", onPointerMove);
    renderer.domElement.addEventListener("pointerup", onPointerUp);
    renderer.domElement.addEventListener("pointercancel", onPointerUp);
    renderer.domElement.addEventListener("wheel", (e) => {
      e.preventDefault();
      goal.radius = Math.max(9, Math.min(60, goal.radius * (1 + e.deltaY * 0.0012)));
    }, { passive: false });
    renderer.domElement.addEventListener("dblclick", reset);

    // --- resize
    const ro = new ResizeObserver(() => {
      const ww = Math.max(1, host.clientWidth);
      const hh = Math.max(1, host.clientHeight);
      renderer.setSize(ww, hh, false);
      camera.aspect = ww / hh;
      camera.updateProjectionMatrix();
    });
    ro.observe(host);

    const v3 = new THREE.Vector3();
    function frame() {
      state.theta += (goal.theta - state.theta) * 0.12;
      state.phi += (goal.phi - state.phi) * 0.12;
      state.radius += (goal.radius - state.radius) * 0.12;
      const r = state.radius;
      camera.position.set(
        target.x + r * Math.sin(state.phi) * Math.sin(state.theta),
        target.y + r * Math.cos(state.phi),
        target.z + r * Math.sin(state.phi) * Math.cos(state.theta)
      );
      camera.lookAt(target);
      renderer.render(scene, camera);

      const ww = host.clientWidth;
      const hh = host.clientHeight;
      const boxes = [];
      const ordered = [...markers].sort((a, b) => a.priority - b.priority);
      ordered.forEach((m) => {
        v3.set(m.x, m.y + 0.35, m.z).project(camera);
        const onScreen = v3.z < 1 && Math.abs(v3.x) < 1.02 && Math.abs(v3.y) < 1.02;
        if (!onScreen) { m.el.style.display = "none"; return; }
        const sx = (v3.x * 0.5 + 0.5) * ww;
        const sy = (-v3.y * 0.5 + 0.5) * hh;
        const label = m.el.textContent;
        const bw = label.length * 6.2 + 10;
        const bh = 15;
        const box = { x: sx - bw / 2, y: sy - bh - 8, w: bw, h: bh };
        const clash = boxes.some((b) => !(b.x + b.w < box.x || box.x + box.w < b.x ||
                                           b.y + b.h < box.y || box.y + box.h < b.y));
        if (clash) { m.el.style.display = "none"; return; }
        boxes.push(box);
        m.el.style.display = "block";
        m.el.style.left = sx + "px";
        m.el.style.top = (sy - 8) + "px";
      });
      requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);

    three = { renderer, host, reset, markers };
    apply3D();
    return three;
  }

  // Same filter state on the 3D markers: label shows the share, size follows it.
  function apply3D() {
    if (!three) return;
    three.markers.forEach((m) => {
      const s = m.isSummit ? null : shareOf(m.c);
      m.el.textContent = m.baseLabel + (s == null ? "" : " " + fmt.pct(s, 0));
      const near = view.alt != null && Math.abs(m.c.elev - view.alt) <= 350;
      m.mesh.scale.setScalar((s == null ? 1 : .6 + s * 1.1) * (near ? 1.9 : 1));
    });
  }

  function update(reach) {
    view.reach = reach;
    drawMap();
    apply3D();
  }
  function highlight(alt) {
    view.alt = alt;
    highlightMap();
    apply3D();
  }

  // ------------------------------------------------------------- mount
  function setMode(mode) {
    const grid = document.getElementById("geo-grid");
    grid.className = "geo-grid mode-" + mode;
    if (mode !== "map") init3D();
    setTimeout(() => { drawMap(); if (three) window.dispatchEvent(new Event("resize")); }, 60);
  }

  function init() {
    const foot = document.getElementById("geo-foot");
    if (foot) {
      foot.innerHTML = `Terrain: SRTM 30 m via <a href="https://registry.opendata.aws/terrain-tiles/" target="_blank" rel="noopener">Mapzen / AWS Terrain Tiles</a>
        (vertical exaggeration ×1.7 in 3D). Camps, cols and peaks: <a href="https://www.openstreetmap.org/" target="_blank" rel="noopener">© OpenStreetMap contributors</a> (ODbL).
        Elevations are OSM tags, cross-checked against the database medians shown on hover.
        The connecting line is a schematic route, not a surveyed track. Contours every 500 m, heavier at each 1,000 m.`;
    }
    const note = document.getElementById("geo-map-note");
    if (note) note.textContent = "north up";
    U.seg("geo-contour", "on", (v) => { view.contours = v === "on"; drawMap(); });

    drawMap();
    const ro = new ResizeObserver(() => {
      clearTimeout(drawMap._t);
      drawMap._t = setTimeout(drawMap, 120);
    });
    const mapEl = document.getElementById("geo-map");
    if (mapEl) ro.observe(mapEl);

    document.querySelectorAll("#geo-mode button").forEach((b) => {
      b.addEventListener("click", () => {
        document.querySelectorAll("#geo-mode button").forEach((x) => x.classList.remove("is-active"));
        b.classList.add("is-active");
        setMode(b.dataset.mode);
      });
    });
    init3D();
    const rb = document.getElementById("geo-reset");
    if (rb) rb.addEventListener("click", () => { if (three) three.reset(); });
  }

  window.GEO = { init, update, highlight };
})();
