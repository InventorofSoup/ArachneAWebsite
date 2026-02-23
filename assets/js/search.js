(function () {
  const posts = (window.__POSTS__ || []).map(p => ({
    ...p,
    _haystack: (p.title + " " + p.excerpt + " " + p.content).toLowerCase()
  }));

  const box = document.getElementById("searchBox");
  const resultsEl = document.getElementById("results");
  const metaEl = document.getElementById("searchMeta");

  function escapeHtml(str) {
    return String(str)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function render(items, q) {
    if (!q) {
      metaEl.textContent = `Type to search across ${posts.length} posts.`;
      resultsEl.innerHTML = "";
      return;
    }

    metaEl.textContent = `${items.length} result(s) for "${q}"`;

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

    // very simple contains matching
    const hits = posts.filter(p => p._haystack.includes(query));

    // newest first
    return hits;
  }

  // initial
  render([], "");

  box.addEventListener("input", () => {
    const q = box.value;
    const hits = search(q);
    render(hits, q);
  });
})();
