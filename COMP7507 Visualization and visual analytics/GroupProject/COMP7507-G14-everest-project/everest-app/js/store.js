/* Shared navigation and URL state, so views can be linked and scenarios shared. */
(function () {
  "use strict";

  function readParams() {
    return new URLSearchParams(location.search);
  }
  // Merge values into the query string without reloading the page.
  function writeParams(values) {
    const q = readParams();
    Object.entries(values).forEach(([k, v]) => {
      if (v == null || v === "") q.delete(k); else q.set(k, v);
    });
    const s = q.toString();
    history.replaceState(null, "", location.pathname + (s ? "?" + s : "") + location.hash);
  }
  const Store = {
    readParams,
    writeParams,
    go(view) { window.APP.show(view, true); },
  };
  window.Store = Store;
})();
