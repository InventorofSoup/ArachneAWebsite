(function () {
  document.querySelectorAll(".archive-section").forEach(function (section) {
    var filterGroups = Array.prototype.slice.call(section.querySelectorAll("[data-archive-filters]"));
    var items = Array.prototype.slice.call(section.querySelectorAll("[data-archive-item]"));
    var status = section.querySelector("[data-archive-status]");
    var activeFilters = {};

    if (!filterGroups.length || !items.length) return;

    filterGroups.forEach(function (filterGroup) {
      var groupName = filterGroup.getAttribute("data-filter-group") || "category";
      var activeButton = filterGroup.querySelector("[data-filter].active");
      activeFilters[groupName] = activeButton ? activeButton.getAttribute("data-filter") : "all";
    });

    function applyFilters() {
      var visible = 0;

      items.forEach(function (item) {
        var matches = Object.keys(activeFilters).every(function (groupName) {
          var filter = activeFilters[groupName];
          return filter === "all" || item.getAttribute("data-filter-" + groupName) === filter;
        });
        item.hidden = !matches;
        if (matches) visible += 1;
      });

      filterGroups.forEach(function (filterGroup) {
        var groupName = filterGroup.getAttribute("data-filter-group") || "category";
        filterGroup.querySelectorAll("[data-filter]").forEach(function (button) {
          var active = button.getAttribute("data-filter") === activeFilters[groupName];
          button.classList.toggle("active", active);
          button.setAttribute("aria-pressed", String(active));
        });
      });

      if (status) {
        var itemName = status.getAttribute("data-item-name") || "item";
        status.textContent = visible + " " + itemName + (visible === 1 ? " shown" : "s shown");
      }
    }

    filterGroups.forEach(function (filterGroup) {
      filterGroup.addEventListener("click", function (event) {
        var button = event.target.closest("[data-filter]");
        if (!button) return;
        var groupName = filterGroup.getAttribute("data-filter-group") || "category";
        activeFilters[groupName] = button.getAttribute("data-filter") || "all";
        applyFilters();
      });
    });

    applyFilters();
  });
})();
