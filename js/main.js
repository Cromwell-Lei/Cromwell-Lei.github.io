(() => {
  const year = document.querySelector('[data-year]');
  if (year) year.textContent = String(new Date().getFullYear());

  const links = [...document.querySelectorAll('.nav-list a[href^="#"]')];
  if (!('IntersectionObserver' in window) || !links.length) return;

  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      for (const link of links) {
        if (link.getAttribute('href') === `#${entry.target.id}`) {
          link.setAttribute('aria-current', 'location');
        } else {
          link.removeAttribute('aria-current');
        }
      }
    }
  }, { rootMargin: '-20% 0px -65% 0px' });

  for (const link of links) {
    const section = document.querySelector(link.getAttribute('href'));
    if (section) observer.observe(section);
  }
})();
