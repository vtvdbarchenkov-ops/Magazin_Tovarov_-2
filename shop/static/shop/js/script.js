document.addEventListener("DOMContentLoaded", function () {
  const links = document.querySelectorAll("nav a");

  links.forEach(function (link) {
    if (link.getAttribute("href") === window.location.pathname) {
      link.classList.add("active");
    }
  });
});
