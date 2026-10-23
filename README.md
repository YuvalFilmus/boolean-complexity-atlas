# Boolean Complexity Atlas

**[Open the website](https://yuvalfilmus.github.io/boolean-complexity-atlas/)** · [Website maintenance guide](docs/website-guide.md)

A source-linked repository for query, sensitivity, certificate and polynomial complexity measures, with separate scopes for promises, search relations and restricted classes. Broad catalogue audit: 17 October 2026. Sensitivity-campaign update: 22 October 2026.

**Current coverage: 249 defined measures, 782 claim records, 135 references and 9 surveys.** Both twelve-measure total and promise core grids have evidence for all 132 off-diagonal pairs. The promise grid has 49 matched finite exponents and 83 pairs with no finite polynomial bound. Search and extended-measure coverage, historical notation and source-priority audits remain incomplete. Many claim records are consequences of shared witnesses. No claim is globally certified current-best. See [the audit report](docs/source-audit.md).

The [Open Questions tab](https://yuvalfilmus.github.io/boolean-complexity-atlas/#questions) offers six transparent ranking orders, passage-level repeated-question highlights, scoped gap views and a resolved/refuted archive. Counts reflect indexed literature; unknown scores and unverified current status are marked. See [ranking methods and maintenance](docs/open-questions.md).

## Website

The [separation-witness gallery](https://yuvalfilmus.github.io/boolean-complexity-atlas/#witnesses) connects 136 construction records to all indexed separation/no-finite-power claims. See [the sensitivity campaign and gallery audit](docs/sensitivity-campaign-and-gallery.md) for the new OpenAI construction, dated improvements, and explicit proof-access limits.

The site includes selectable exponent tables, amber gap highlighting, clickable historical dossiers with proof summaries, an annotated bibliography, a notation dictionary and a conjecture index. Domains and query conventions have separate views. Tables and dossiers have shareable links; exports include CSV, LaTeX, JSON and BibTeX. Notations and inequalities use locally bundled KaTeX.

Build with `python3 tools/build_site.py`; run the website tests with `node --test tests/site-model.test.mjs`. GitHub Actions publishes the static build to GitHub Pages on changes to `main`. See [the website guide](docs/website-guide.md).

## Files

- `docs/independent-checks-and-source-versions.md`: independent review of four derivations, corrected Aaronson proof, recovered mixed constant bound and remaining gaps.
- `docs/new-derivations-independent-audit.md`, `data/new-derivations-independent-audit.json`: complete separate-agent review and exact reviewed records.

- `docs/independent-audit-and-quantum-endpoints.md`: independent lift repairs, fifteen tighter lower bounds, source/priority and normalization status.
- `docs/lambda-lift-independent-audit.md`, `data/lambda-lift-independent-audit.json`: separate-agent review and hash-bound incorporation record.

- `docs/unmatched-and-kernel-line-audit.md`: latest unmatched-interval tightening, sharp verification constants and quantitative kernel-line conditions.
- `docs/lambda-partite-lift.md`: full product-permutation sensitivity proof with explicit lambda dependence.
- `data/completion-unmatched-queue.json`: remaining recorded exponent gaps with witnesses and provenance; not certified open problems.

- `docs/dependent-support-and-exponent-audit.md`: dependent-support LP diagnostic, capped one-sided quadratic bound, and uniform hypermatching lift.
- `docs/extended-completion-exponents.md`, `data/extended-completion-exponents.json`: all 506 completion directions, with lower/upper evidence and endpoint caveats.

- `docs/higher-support-and-profile-audit.md`: higher-degree sufficient kernel conditions, 61 tighter completion chains and explicit conjecture quantifiers.
- `docs/profile-matrices.md`, `data/profile-matrices.json`: six domain-profile matrices with symbolic prefactors and guards.

- `docs/coverage-guide.md`: grouped overview and complete index of the 249 measure entries.
- `docs/tightening-and-linear-normalization.md`: 22 tighter completion chains, original UC bound and degree-one kernel proof.

- `docs/completion-closure-and-formulations.md`: complete 506-cell completion coverage, one-sided and address witnesses, and the enlarged-basis normalization obstruction.

- `docs/normalization-and-inventory-followup.md`: sparse-coefficient sufficient repair, conjecture quantifiers and newly indexed completion paths.
- `docs/domain-matrix.md`, `data/domain-matrix.json`: conservative common-oracle general-domain comparison inventory.

- `docs/broader-inventory-audit.md`: extended completions, query-domain profiles, conjecture formulations and final-journal checks.
- `docs/extended-completion-inventory.md`, `data/extended-completion-inventory.json`: 23 completion measures and 506 ordered comparisons.
- `docs/general-domains.md`, `data/general-domains.json`: six parameterized domain families with oracle conventions.
- `data/journal-version-audit.json`: explicit manuscript/journal verification statuses.

- `data/catalog.json`: authoritative UTF-8 plaintext definitions, aliases, claims, constants, domains, conjectures and bibliographic information.
- `docs/core-matrix.md` and `data/core-matrix.json`: complete twelve-measure core grid, exact exponent expressions and per-cell provenance.
- `docs/partial-matrix.md` and `data/partial-matrix.json`: separate complete promise core, with witness and finite-bound provenance.
- `docs/partial-functions.md`, `docs/search-problems.md`: model conventions, proof summaries and source/priority findings.
- `docs/search-matrices.md` and `data/search-matrices.json`: eight direct-evidence inventories for total/promise search and other query models.
- `docs/completion-and-symmetric-audit.md`: completion measures, Nisan’s expected-cost constant repair, relevant-variable comparisons and symmetric-group distinctions.
- `docs/completion-matrix.md`, `data/completion-matrix.json`: all 132 core minimum-completion exponent comparisons, with total-witness lower bounds and preserved endpoint losses.
- `docs/permutation-matrix.md`, `data/permutation-matrix.json`: 132 derived upper comparisons on the symmetric group, without optimality certification.
- `docs/originals-and-domains.md`: supplied originals, expected-cost constants, relevant variables and symmetric-group measures.
- `docs/conjecture-status-audit.md`: literal sparsity conjecture correction, Forrelation revision, journal comparisons and original-source access gaps.
- `data/source-access-audit.json`: failed original full-text requests, distinct from inspected snapshots.
- `docs/priority-audit.md`: source versions, priorities, constants and targeted literature-search status.
- `docs/search-size-audit.md`, `docs/average-cost.md`: new original-source checks and model distinctions.
- `docs/model-transformations.md`: typed search-to-decision, coupled-tree bounds and query-class definitions.
- `data/historical-matrix-2021.json`: dated transcription of ABKBRT21 Table 1, kept separate from checked current evidence.
- `data/pair-index.json`: all-measure syntactic pair register with separate scope groups. Unindexed does not mean unknown in the literature; cross-model comparisons need a common domain.
- `docs/measures.md`: definitions and source-dependent normalizations.
- `docs/historical-notation.md`, `docs/notation-collisions.md`, `data/notation-register.json`: notation occurrences, names, clashes and repair history.
- `docs/claims.md`: statements, theorem locators, proof summaries, constants and caveats.
- `docs/exponents.md`: selected manually curated pair summaries; the complete core grid is in `docs/core-matrix.md`.
- `docs/surveys.md`: annotated survey entry points.
- `docs/research-queue.md`: conjectures, dated resolutions and extraction queue.
- `docs/source-audit.md`, `data/source-snapshots.json`: audit progress and source hashes.
- `docs/data-model.md`: mathematical and data conventions.
- `bibliography.bib`: generated version-aware bibliography.

## Reproduce and query

Python 3, standard library only. From this directory:

```sh
python3 tools/catalog.py validate
python3 tools/catalog.py export
python3 tools/matrix.py
python3 tools/partial_matrix.py
python3 tools/search_matrices.py
python3 tools/audit_reports.py
python3 tools/completion_matrix.py
python3 tools/permutation_matrix.py
python3 tools/extended_completions.py
python3 tools/completion_lower.py
python3 tools/general_domains.py
python3 tools/domain_matrix.py
python3 tools/profile_matrices.py
python3 tools/pair_index.py
python3 -m unittest discover -s tests -v
python3 tools/matrix.py --pair C s
python3 tools/catalog.py pair D Q --kind decision_function --totality total --class unrestricted
python3 tools/catalog.py list --kind search_relation --totality total
```

The matrix is a restricted exponent calculation on explicitly eligible total-function evidence. It is not a general inference engine: no historical table value, input-length factor, promise theorem, local bound or restricted-class upper bound is silently inserted. All derivations keep their claim IDs. Matching endpoint exponents do not imply constant-factor tightness or eliminate logarithmic endpoint losses.

The claim CLI performs direct scope filtering. General upper bounds apply to subclasses; witnesses apply only to supported superclasses. Without filters, the CLI displays each scope explicitly and those results must not be merged into one interval. Use stable measure IDs because printed symbols are deliberately non-unique.

No HTML has been generated, and the repository has not been published. Downloaded papers are excluded from the distributable archive.

The [23 October question-status audit](docs/question-status-audit-2026-10-23.md) checks all 15 active published candidates: six are reaffirmed in recent primary sources, seven have no resolution found in the recorded search, and two retain formulation issues. Repeated-question references now cover five questions.
