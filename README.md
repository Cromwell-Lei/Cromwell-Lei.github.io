# Chenjun Lei — The Considered Archive

Live: https://cromwell-lei.github.io/ · 中文：https://cromwell-lei.github.io/zh/

Static HTML, CSS and vanilla JavaScript, published by GitHub Pages from `main` / root. No build service, third-party fonts, tracking or runtime dependencies.

## Content & editing

`python3 scripts/build.py` generates all five English pages and their Chinese counterparts, the sitemap and two BibTeX files. Edit the paired English/Chinese content in `scripts/build.py`, then regenerate. Do not edit generated pages in isolation. CSS and JS are shared across languages. Dates and metrics are from the CV supplied on 27 September 2026 (Sydney time).

- `index.html` — introduction, research, projects, experience, education, interests and contact.
- `research.html` — three manuscripts/papers and one research report, authorship, status, summaries and source links.
- `projects.html` — four project descriptions with individual contributions.
- `experience.html` — complete work history, education, awards, skills, campus activities; print / save as PDF.
- `photography.html` — photography, music, motorsport and the photobook in preparation.
- `zh/` — complete Chinese versions of all five pages.
- `assets/citations/` — citations to the two arXiv preprints, not invented proceedings records.

## Sources and factual boundaries

- CV: three user-supplied screenshots. Current CV supersedes older placeholder roles, dates and metrics. Survey response rate is **at 30%**, not a 30% increase; labour dataset is **160,000+** records; bond issuance is **RMB 150 million**.
- Safe Remediation: https://arxiv.org/abs/2607.20005
- Coordinating from Memory: https://arxiv.org/abs/2607.19985
- Conference acceptance: current CV, corroborated by coauthor's publication list https://erikdai.github.io/publications/ . Both are labelled accepted, with links explicitly pointing to preprints.
- Scientific Data manuscript remains **submitted**. No verified public manuscript link was found. The related code repository is private and is not presented as publicly available code.
- Research summaries paraphrase the source papers; reported benchmark results are attributed to the papers, not presented as personal achievements or deployment outcomes.
- Google Scholar and ORCID logos in the screenshots do not expose their underlying URLs. No profile identifiers are guessed. No LinkedIn or fake CV download links are added.
- Portfolio photography is still being curated. Decorative artwork is original CSS; it is not represented as a photograph. Screenshots of the CV are not published.
- The commercial annotation platform is described by function; unverified market-first claims are omitted.

Publication presentation references reviewed: Jon Barron (https://jonbarron.info/), Deepak Pathak (https://www.cs.cmu.edu/~dpathak/) and Chengxiao Dai (https://erikdai.github.io/publications/). The existing visual identity is retained.

## Languages and accessibility

The language link opens the equivalent page, retaining its section anchor with JavaScript. Both languages are fully readable with JavaScript disabled. URLs, document language, descriptions, canonical URLs and hreflang metadata are language-specific. Original English publication titles and author names are preserved in Chinese pages.

Semantic headings, keyboard focus, skip links, native details/summary and reduced-motion support are retained. Phones are in an expandable contact section. The experience page has print styles. Old home and project anchors are redirected in `js/main.js`.

## Preview, check and publish

```sh
python3 scripts/build.py
python3 -m http.server 8000
```

Check all ten pages at desktop and mobile widths, switch languages on each page, expand research summaries, verify anchors and paper links, and inspect printed experience. Check `node --check js/main.js`. Deploy by committing and pushing to `main`, then verify the GitHub Pages workflow and live URLs. Update the CSS/JS version query when changing shared assets. Revert a commit for rollback; do not force-push.
