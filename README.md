# CHENJUN LEI — Personal Portfolio

A small, dependency-free personal archive for photography, research, projects, and notes. The first version uses text and CSS placeholders rather than stock imagery or invented biographical details.

**Website:** https://cromwell-lei.github.io/  
**Repository:** https://github.com/Cromwell-Lei/Cromwell-Lei.github.io

## Files

| Path | Purpose |
| --- | --- |
| `index.html` | Home page content, section order, metadata, navigation |
| `css/style.css` | Typography, layout, colours, gallery, responsive rules |
| `js/main.js` | Automatic footer year and current navigation state |
| `assets/images/` | Your future photographs (currently empty) |
| `assets/icons/favicon.svg` | Minimal browser icon |
| `404.html` | Custom missing-page screen |
| `robots.txt`, `sitemap.xml` | Basic crawler information |
| `.nojekyll` | Serve the static files directly without Jekyll processing |

## Preview locally

Clone the repository, then from its root run:

```sh
python3 -m http.server 8000
```

Visit `http://localhost:8000/`. Stop with `Ctrl+C`. You can also open `index.html` directly, but root-relative asset paths (`/css/...`) work properly through the local server.

## Edit the site

- **Introduction / About:** In `index.html`, edit the text in `<section id="about">`. The top introduction is in `<section class="hero">`.
- **Projects / Research:** Edit or duplicate an `<article class="work-item">` inside `<section id="work">`. Once you have a real project page, wrap its title in an `<a href="...">`; these initial rows are deliberately not clickable.
- **Photography:** Put optimised `.jpg`, `.webp`, or `.avif` files in `assets/images/`. For each `<figure class="photo">` in `<section id="photography">`, replace its `.photo-placeholder` span with an image, for example:

  ```html
  <div class="photo-media">
    <img src="/assets/images/my-photo.webp" alt="A specific description of the photograph" loading="lazy">
  </div>
  ```

  Update the corresponding `<figcaption>`. The existing `.photo-media img` CSS already applies `object-fit: cover`; to preserve the full original crop, change it to `contain` or adjust `object-position` for an individual photo. Aim for consistent aspect ratios and sensible file sizes before uploading.
- **Contact:** Edit `<section id="contact">`. Replace `Coming soon` with a real `mailto:` link or a verified LinkedIn URL when ready. The GitHub link already points to the confirmed account.
- **Design:** Change the colour variables at the top of `css/style.css`. Responsive rules are at the bottom of that file.
- **SEO:** If the name, domain, or description changes, update `index.html`, `robots.txt`, and `sitemap.xml` together.

## Publish changes

GitHub Pages serves the **`main` branch, root (`/`)**. Commit and push to `main`; GitHub republishes the site automatically. Changes usually appear after the Pages deployment completes. You can check **Repository → Actions** for the Pages build and **Settings → Pages** for the live URL and source. No Node.js, npm, build command, secrets, or third-party services are required.

The custom `404.html` is used for unknown URLs on GitHub Pages. A plain local Python server may show its own generic 404 instead.
