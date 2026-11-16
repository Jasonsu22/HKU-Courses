/* Runs inside each snapshot: draws difference banners and takes commands from compare.html. */
(function () {
  "use strict";
  const side = window.SNAPSHOT_SIDE;
  const style = document.createElement("style");
  style.textContent = `
    .chg-banner{display:flex;gap:9px;align-items:baseline;margin:-4px 0 10px;padding:7px 11px;border-radius:7px;font:12.5px/1.4 -apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif;color:#1b1e22;}
    .chg-banner b{flex:none;font-size:10.5px;letter-spacing:.07em;padding:2px 7px;border-radius:4px;color:#fff;}
    .chg-NEW{background:#e4f3e6;} .chg-NEW b{background:#1b7837;}
    .chg-UPGRADED{background:#e3edfb;} .chg-UPGRADED b{background:#1c5cab;}
    .chg-FIXED{background:#fde9df;} .chg-FIXED b{background:#b8430f;}
    .chg-CHANGED{background:#fbf1d8;} .chg-CHANGED b{background:#7a5b12;}
    .chg-t-NEW{outline:3px solid #1b7837;outline-offset:2px;}
    .chg-t-UPGRADED{outline:3px solid #1c5cab;outline-offset:2px;}
    .chg-t-FIXED{outline:3px solid #b8430f;outline-offset:2px;}
    .chg-t-CHANGED{outline:3px solid #7a5b12;outline-offset:2px;}
    body.chg-off .chg-banner{display:none;}
    body.chg-off [class*="chg-t-"]{outline:none;}
    .chg-focus{animation:chgf 1.6s ease;}
    @keyframes chgf{0%,50%{box-shadow:0 0 0 7px rgba(216,27,96,.55);}100%{box-shadow:none;}}`;
  document.head.appendChild(style);

  const targetFor = (sel) => {
    const n = document.querySelector(sel);
    return n ? (n.closest(".card") || n.closest(".findings") || n) : null;
  };
  function mark(c) {
    const sel = side === "before" ? c.before : c.after;
    if (!sel) return;
    const el = targetFor(sel);
    if (!el) return;
    const type = side === "before" ? (c.type === "FIXED" ? "FIXED" : "CHANGED") : c.type;
    const label = side === "before" && c.type === "FIXED" ? "ISSUE" : type;
    const note = side === "before" ? (c.beforeNote || `Changed in the new version: ${c.title}.`) : c.note;
    const banner = document.createElement("div");
    banner.className = `chg-banner chg-${type}`;
    banner.innerHTML = `<b>${label}</b><span>${note}</span>`;
    el.classList.add(`chg-t-${type}`);
    const ensure = () => { if (banner.parentNode !== el || el.firstChild !== banner) el.prepend(banner); };
    ensure();
    // some cards rewrite their own content when they redraw
    new MutationObserver(ensure).observe(el, { childList: true });
  }

  function setView(view, tab) {
    if (location.hash !== "#" + view) location.hash = "#" + view;
    if (tab && side === "after") {
      setTimeout(() => { if (window.M3 && M3.setTab) M3.setTab(tab); }, 60);
    }
  }
  function goto(c) {
    setView(c.view, c.tab);
    const sel = side === "before" ? c.before : c.after;
    if (!sel) return;
    setTimeout(() => {
      const el = targetFor(sel);
      if (!el) return;
      el.scrollIntoView({ behavior: "smooth", block: "start" });
      setTimeout(() => window.scrollBy(0, -80), 450);
      el.classList.remove("chg-focus"); void el.offsetWidth; el.classList.add("chg-focus");
    }, 180);
  }

  window.addEventListener("message", (e) => {
    const m = e.data || {};
    if (m.cmd === "view") setView(m.view, m.tab);
    if (m.cmd === "highlight") document.body.classList.toggle("chg-off", !m.on);
    if (m.cmd === "goto") goto(window.CHANGES[m.index]);
  });

  function boot() {
    window.CHANGES.forEach(mark);
    const q = new URLSearchParams(location.search);
    if (q.get("highlight") === "0") document.body.classList.add("chg-off");
    if (window.parent !== window) window.parent.postMessage({ ready: side }, "*");
  }
  if (document.readyState === "complete") boot(); else window.addEventListener("load", boot);
})();
