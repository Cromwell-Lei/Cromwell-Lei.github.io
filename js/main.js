/* Progressive enhancements: all navigation and text work without JavaScript. */
(() => {
  'use strict';
  document.querySelectorAll('[data-year]').forEach(el => { el.textContent = String(new Date().getFullYear()); });
  const legacy = { '#work': '#lei-projects', '#photography': '#lei-outside', '#about': '#lei-experience', '#contact': '#lei-contact', '#research': '#lei-research', '#projects': '#lei-projects', '#experience': '#lei-experience' };
  const destination = legacy[location.hash];
  if (destination && document.querySelector(destination)) {
    history.replaceState(null, '', destination);
    document.querySelector(destination).scrollIntoView();
  }
  const links = [...document.querySelectorAll('header nav a[href^="#"]')];
  if ('IntersectionObserver' in window && links.length) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        const link = links.find(item => item.hash === '#' + entry.target.id);
        if (!link) return;
        if (entry.isIntersecting) {
          links.forEach(item => item.removeAttribute('aria-current'));
          link.setAttribute('aria-current', 'location');
        } else if (link.getAttribute('aria-current') === 'location') link.removeAttribute('aria-current');
      });
    }, { rootMargin: '-10% 0px -55% 0px', threshold: 0 });
    links.forEach(link => { const target = document.querySelector(link.hash); if (target) observer.observe(target); });
  }
  // Opt in only real photographs. Placeholders are never links.
  const photos = [...document.querySelectorAll('a[data-lightbox]')];
  if (!photos.length || typeof HTMLDialogElement === 'undefined') return;
  const dialog = document.createElement('dialog');
  if (typeof dialog.showModal !== 'function') return;
  dialog.className = 'lightbox';
  dialog.setAttribute('aria-label', 'Photograph viewer');
  dialog.innerHTML = '<div class="lightbox-bar"><p class="kicker" data-count></p><div class="lightbox-controls"><button type="button" data-prev aria-label="Previous photograph">←</button><button type="button" data-next aria-label="Next photograph">→</button><button type="button" data-close>Close</button></div></div><img alt=""><p class="lightbox-error" hidden>Unable to load this photograph.</p><p class="lightbox-caption" aria-live="polite"></p>';
  document.body.append(dialog);
  const image = dialog.querySelector('img');
  const error = dialog.querySelector('.lightbox-error');
  let current = 0;
  let trigger;
  const render = () => {
    const photo = photos[current];
    error.hidden = true;
    image.hidden = false;
    image.alt = photo.querySelector('img')?.alt || 'Photograph';
    image.src = photo.href;
    dialog.querySelector('.lightbox-caption').textContent = photo.closest('figure')?.querySelector('figcaption')?.textContent.trim() || image.alt;
    dialog.querySelector('[data-count]').textContent = (current + 1) + ' / ' + photos.length;
  };
  const move = delta => { current = (current + delta + photos.length) % photos.length; render(); };
  image.addEventListener('error', () => { image.hidden = true; error.hidden = false; });
  photos.forEach((photo, index) => photo.addEventListener('click', event => {
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault(); trigger = photo; current = index; render();
    dialog.showModal(); document.body.classList.add('has-lightbox');
    dialog.querySelector('[data-close]').focus();
  }));
  dialog.querySelector('[data-prev]').addEventListener('click', () => move(-1));
  dialog.querySelector('[data-next]').addEventListener('click', () => move(1));
  dialog.querySelector('[data-close]').addEventListener('click', () => dialog.close());
  if (photos.length < 2) { dialog.querySelector('[data-prev]').hidden = true; dialog.querySelector('[data-next]').hidden = true; }
  dialog.addEventListener('keydown', event => {
    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') { event.preventDefault(); move(event.key === 'ArrowLeft' ? -1 : 1); }
  });
  dialog.addEventListener('click', event => {
    const rect = dialog.getBoundingClientRect();
    if (event.target === dialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) dialog.close();
  });
  dialog.addEventListener('close', () => { document.body.classList.remove('has-lightbox'); trigger?.focus(); });
})();
