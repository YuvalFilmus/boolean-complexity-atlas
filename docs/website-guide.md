# Website and maintenance guide

The website is published from this repository by GitHub Pages. The static website source is in `site/`. Its mathematical source of truth remains `data/catalog.json`, the generated evidence matrices and the Markdown audit notes.

## Views

- **Explorer:** choose a scope and measures, grouped by subject. Each cell uses row A and column B for a bound of A in terms of B. Amber cells have distinct recorded lower and upper exponents; green cells have matching exponents. A dagger retains upper endpoint losses; infinity indicates a scoped no-finite-power witness. Unindexed cells remain neutral. The gap-emphasis toggle dims the rest of the table.
- **Comparison dossier:** definitions, supporting claim IDs, direct historical results, proof summaries, source locators, mixed/conditional comparisons and full provenance. Copy a permanent comparison URL or download its JSON. Generated transfer chains and direct results are distinguished.
- **Witness gallery:** searchable construction cards with separated pairs, proof summaries, references, source-access qualifications and links back to scoped comparisons. Table arrows and dossiers link directly to the supporting constructions. A dated campaign panel distinguishes completed sensitivity exponents from open targets.
- **Bibliography:** all source records, original annotations where available, summaries of indexed contributions otherwise, expandable result/proof lists, publication versions and source-inspection information. Search authors, titles, years, keys or statements; filter surveys; download individual or complete BibTeX.
- **Measures and notation:** all definitions, grouped families, source-specific aliases and clashes. Canonical symbols are rendered with KaTeX; the original strings remain in the underlying records.
- **Conjectures:** source formulations, recorded status, implications and exact status evidence.
- **About and audit:** mathematical conventions, coverage limits, downloads and research notes.

The table only summarizes evidence under the selected scope. Noncore direct comparisons do not run a general inference engine. General-domain entries retain coefficients and guards. Neither missing entries nor unmatched exponents are certified open problems. Current-best completeness is not claimed.

## Local development

Python 3.12 and Node 22 suffice; no package installation is needed. KaTeX 0.19.0 and its MIT license are bundled under `site/vendor/katex/`, with the npm integrity recorded in `VERSION.txt`.

```sh
python3 tools/catalog.py validate
python3 tools/catalog.py export
python3 -m unittest discover -s tests
python3 tools/witness_gallery.py
python3 tools/build_site.py
node --test tests/site-model.test.mjs
python3 -m http.server 8765 --directory _site
```

Open `http://localhost:8765`. The build recreates the ignored `_site/` directory. Paths are relative, so the same build works under the GitHub Pages repository subpath. Source PDFs, local source-file paths and credentials are not published. User-supplied source filenames are retained without their machine directories.

When changing mathematical data, run the relevant evidence generators documented in the main README before rebuilding. The website builder deliberately does not recompute or silently alter the research matrices. It copies their audited evidence and adds presentation-only expression labels.

## Publishing

The workflow `.github/workflows/pages.yml` validates the catalogue, runs the research and website model tests, builds `_site/`, uploads the Pages artifact and deploys on `main`. Pull requests run the checks without publishing. GitHub Pages must use **GitHub Actions** as its build source.

The code does not use analytics, third-party font services, a remote math-rendering CDN or a server database. The static research data is public. Source inspection statuses and independent-assistant audit records describe their actual scope; they are not formal proofs or human peer review.

Presentation-only TeX transcriptions live in `data/statement-latex.json`; mathematical statement strings remain authoritative. New scalar bounds must update the relevant matrices before publishing. The dated sensitivity campaign snapshot and its attestation limits are documented in `docs/sensitivity-campaign-and-gallery.md`.


## Sensitivity-campaign updates

The campaign panel reads its date and exact leading exponent from data/sensitivity-campaign.json. Keep exact logarithmic endpoints in exponent_expression; a tracker decimal is only a display approximation when the theorem is logarithmic. Record completed checkpoints, goal URLs, page hashes and solve timestamps, while retaining open targets outside the claim registry. Distinguish public construction summaries, accepted-proof access and independent kernel replay. Rebuild all dependent matrices and the gallery after changing lower-bound claims. See the dated campaign audit for current details and remaining proof-access gaps.
