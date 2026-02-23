(function () {
  const posts = (window.__POSTS__ || []).map(p => ({
    ...p,
    type: (p.type || "post").toLowerCase(),
    _haystack: (p.title + " " + p.excerpt + " " + p.content).toLowerCase()
  }));

  const box = document.getElementById("searchBox");
  const resultsEl = document.getElementById("results");
  const metaEl = document.getElementById("searchMeta");
  const filtersEl = document.getElementById("filters");

  let activeFilter = "all";

  function escapeHtml(str) {
    return String(str)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function isMatchFilter(p) {
    if (activeFilter === "all") return true;
    if (activeFilter === "post") {
      // "post" filter means: anything not explicitly episode/event/youtube
      return !["episode", "event", "youtube"].includes(p.type);
    }
    return p.type === activeFilter;
  }

  function render(items, q) {
    if (!q) {
      metaEl.textContent = `Type to search across ${posts.length} posts.`;
      resultsEl.innerHTML = "";
      return;
    }

    const label = activeFilter === "all" ? "All" : activeFilter.toUpperCase();
    metaEl.textContent = `${items.length} result(s) for "${q}" in ${label}`;

    resultsEl.innerHTML = items.map(p => `
      <div class="post-row">
        <div class="tag">${escapeHtml(String(p.type || "post").toUpperCase())}</div>
        <h3 class="hline"><a href="${escapeHtml(p.url)}">${escapeHtml(p.title)}</a></h3>
        <p class="excerpt">${escapeHtml(p.excerpt || "")}</p>
        <div class="meta">${escapeHtml(p.date || "")}</div>
      </div>
      <hr class="divider">
    `).join("");
  }

  function search(q) {
    const query = q.trim().toLowerCase();
    if (!query) return [];

    // contains match + filter
    return posts
      .filter(p => p._haystack.includes(query))
      .filter(isMatchFilter);
  }

  function setActiveButton() {
    if (!filtersEl) return;
    const btns = filtersEl.querySelectorAll("button[data-filter]");
    btns.forEach(b => {
      const isOn = b.getAttribute("data-filter") === activeFilter;
      b.style.borderColor = isOn ? "rgba(255,212,71,0.55)" : "rgba(255,212,71,0.25)";
      b.style.boxShadow = isOn ? "0 0 0 1px rgba(255,212,71,0.10) inset" : "none";
    });
  }

  function run() {
    const q = box.value || "";
    const hits = search(q);
    render(hits, q);
  }

  // Initial state
  setActiveButton();
  render([], "");

  // Filter clicks
  if (filtersEl) {
    filtersEl.addEventListener("click", (e) => {
      const btn = e.target.closest("button[data-filter]");
      if (!btn) return;
      activeFilter = btn.getAttribute("data-filter") || "all";
      setActiveButton();
      run();
    });
  }

  // Search input
  box.addEventListener("input", run);
})();
