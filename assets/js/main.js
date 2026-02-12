(function () {
  const path = (location.pathname || "").toLowerCase();

  const pick = () => {
    if (path.endsWith("/listen/")) return "listen";
    if (path.endsWith("/events/")) return "events";
    if (path.endsWith("/gallery/")) return "gallery";
    if (path.includes("/posts/")) return "posts";
    if (path.endsWith("/contact/")) return "contact";
    return "home";
  };

  const key = pick();
  document.querySelectorAll(".nav a").forEach(a => {
    if ((a.getAttribute("data-nav") || "") === key) a.classList.add("active");
  });
})();
