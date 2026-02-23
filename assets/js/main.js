(function () {
  const base = "{{ site.baseurl }}";
  const currentPath = window.location.pathname.replace(base, "");

  const links = document.querySelectorAll(".nav a[data-path]");

  links.forEach(link => {
    const linkPath = link.getAttribute("data-path");

    if (currentPath === linkPath || currentPath.startsWith(linkPath)) {
      link.classList.add("active");
    }
  });
})();
