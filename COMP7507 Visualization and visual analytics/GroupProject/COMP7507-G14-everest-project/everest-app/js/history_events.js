/* Module 01 event explorer: historical context plus descriptive fixed-window comparisons. */
(function () {
  "use strict";

  const D = window.EVEREST_DATA;
  const EVENTS = window.EVEREST_EVENTS || [];
  const { fmt, wilson } = U;
  let selected = null;

  function summary(range) {
    const rows = D.expeditions.filter((r) => r.year >= range[0] && r.year <= range[1]);
    return {
      n: rows.length,
      k: rows.filter((r) => r.success).length,
      members: d3.sum(rows, (r) => r.members),
      hired: d3.sum(rows, (r) => r.hired),
    };
  }

  function comparisonTable(event) {
    return `<table class="event-table">
      <thead><tr><th>Fixed comparison window</th><th>Expeditions</th><th>With a summit</th><th>Hired / member</th></tr></thead>
      <tbody>${event.windows.map((w) => {
        const s = summary(w.range);
        const ci = wilson(s.k, s.n);
        const rate = s.n ? `${fmt.int(s.k)} of ${fmt.int(s.n)} · ${fmt.pct(s.k / s.n, 1)}` : "No records";
        const interval = s.n ? `95% CI ${fmt.pct(ci[0])}–${fmt.pct(ci[1])}` : "–";
        const small = s.n < 5 ? `<span class="event-small">Very small sample</span>` : "";
        return `<tr><th>${w.label}${small}</th><td>${fmt.int(s.n)}</td><td>${rate}<small>${interval}</small></td><td>${s.members ? fmt.dec2(s.hired / s.members) : "–"}<small>${fmt.int(s.hired)} hired · ${fmt.int(s.members)} members</small></td></tr>`;
      }).join("")}</tbody>
    </table>`;
  }

  function paintChoices() {
    document.querySelectorAll(".event-choice").forEach((b) => {
      const on = b.dataset.event === selected;
      b.classList.toggle("is-active", on);
      b.setAttribute("aria-pressed", on ? "true" : "false");
    });
  }

  function renderIntro() {
    selected = null;
    paintChoices();
    document.getElementById("m1-event-detail").innerHTML = `
      <div class="event-kicker">Events and turning points</div>
      <h3>The long-term rise was not a smooth, single-cause story</h3>
      <p>Select an event to read its context and compare fixed periods before, during and after it. The timeline will zoom to the surrounding years.</p>
      <p class="event-caveat">These are descriptive comparisons, not causal estimates. External sources explain the events; the table is recomputed from the Everest expedition records.</p>`;
  }

  function select(id, zoom = true) {
    const event = EVENTS.find((e) => e.id === id);
    if (!event) return;
    selected = id;
    document.getElementById("m1-events-details").open = true;
    paintChoices();
    const detail = document.getElementById("m1-event-detail");
    detail.innerHTML = `
      <div class="event-kicker">${event.label} · ${event.type}</div>
      <h3>${event.title}</h3>
      <p>${event.summary}</p>
      <p class="event-prompt"><strong>What to inspect:</strong> ${event.prompt}</p>
      ${comparisonTable(event)}
      <p class="event-caveat">Fixed windows keep this comparison reproducible. They describe what was recorded, not what the event caused.${event.dataNote ? ` ${event.dataNote}` : ""}</p>
      <div class="event-actions">
        <button type="button" class="finding-go" id="m1-event-evidence">${event.targetLabel}</button>
        <a href="${event.source.url}" target="_blank" rel="noopener">Source: ${event.source.label}</a>
      </div>`;
    document.getElementById("m1-event-evidence").addEventListener("click", () => U.spotlight(event.target));
    if (zoom) window.M1.showPeriod(event.range.slice());
    Store.writeParams({ event: id });
  }

  function init() {
    const list = document.getElementById("m1-event-list");
    if (!list) return;
    EVENTS.forEach((event) => {
      const b = U.el("button", {
        type: "button",
        class: "event-choice",
        "data-event": event.id,
        "aria-pressed": "false",
        html: `<span class="event-year">${event.label}</span><span>${event.title}</span><small>${event.type}</small>`,
      });
      b.addEventListener("click", () => select(event.id));
      list.appendChild(b);
    });
    document.getElementById("m1-event-clear").addEventListener("click", () => {
      renderIntro();
      Store.writeParams({ event: null });
    });
    const wanted = Store.readParams().get("event");
    if (EVENTS.some((e) => e.id === wanted)) select(wanted);
    else renderIntro();
  }

  window.HistoryEvents = { init, _test: { summary } };
})();
