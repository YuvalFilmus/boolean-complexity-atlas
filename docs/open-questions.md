# Open Questions tab

Added 23 October 2026. The tab is a view of the existing catalogue audit, not a new certification that every included question remains open. Its default view shows published formulations that are not recorded resolved or refuted. Formulation ambiguities and status checks still due are labelled explicitly. Resolved/refuted records remain in the archive and in the existing conjecture registry.

## Editable sources and generation

- `data/catalog.json`: original question formulations, source locators, status and implications.
- `data/question-annotations.json`: curated measure mappings, domain, and exact passages discussing the same question. A bound citation is not automatically a question mention.
- `tools/open_questions.py`: work deduplication, centrality, inferred gaps and conditional implication calculations.
- `data/open-questions.json`: generated data with evidence for every score and null for unassessed quantities.
- `site/questions-model.mjs`: sorting, filtering and shareable URLs. Missing values sort last, including when sorting by historical longevity. Ties use stable IDs.

Run `python3 tools/open_questions.py` after research or annotation changes. The site build also regenerates its payload and downloadable question data directly from the source files, so it does not depend on a stale cached ranking.

## Ranking orders

**Measure centrality:** geometric mean of distinct indexed scholarly-work counts for the mapped measures. The corpus now has 104 deduplicated scholarly works. Definition references, checked notation records, direct checked comparisons and explicitly annotated measure mentions in question passages supply the evidence. Surveys count; online missions, notes, repository derivations and citation-only proof references do not. Exact normalized titles and the journal-version audit merge versions of a work. The work index and every evidence record are inspectable. These are corpus counts, not a full-text census or a measure of mathematical importance.

**Question recurrence:** number of distinct works with curated passages about the same formulation. Research and survey counts are separate. The average-case simulation question now has five verified work-level sightings (AA14, BSW22, GMNR26, HKMP26, LMparallel26), including its equivalent dense-promise formulation. The bounded-polynomial influence conjecture also has five (AA14, BSW22, Bha26, GMNR26, LMparallel26). These are different questions. Preprint and journal versions do not count twice. Recurrence is not assessed for an inferred table gap merely because its bounds have citations.

**Implication reach:** add the displayed hypothetical pure upper bound to the restricted, scope-compatible total-function upper closure and list the changed ordered pairs among the twelve core measures. Endpoint-loss improvements count alongside exponent improvements. The original pair is included. This is conditional mathematics, not a theorem or a difficulty estimate. It is not assessed for unsupported models, ambiguous formulations, or transcendental endpoints that the rational closure does not support. In particular, no truncated sensitivity exponent is inserted as an exact hypothetical endpoint.

**Exponent gap:** finite upper exponent minus finite lower exponent. It is a feature of the recorded interval, not a judgement of importance. An endpoint-only logarithmic loss has no exponent-gap score. The original lower expression and all endpoint qualifications remain available. No gap score is invented for missing or unbounded endpoints.

**Recent activity:** latest year of a recorded substantive formulation, result or status source associated with the entry. Fetch dates are excluded. This is not an exhaustive measure of research attention.

**Historical longevity:** earliest formulation year verified in the listed question passages. This is not certified first-discovery priority. Inferred gaps have no historical origin assigned.

## Views and qualifications

Filters cover domain, measure group, question type, text and discussion in multiple papers. The default published view retains current-status warnings. The all-active view combines published formulations and inferred gaps; a published pair with a comparison is not duplicated as a second gap entry. The table-gap filter also includes a published formulation when it has a recorded finite exponent gap. The archive excludes active candidates and vice versa.

All unmatched finite core and completion intervals and upper endpoint losses are represented. The 176 unmatched completion intervals remain audit gaps rather than 176 certified open problems. Bounds and witness links retain their own total-function or completion context.

The polynomial influence conjecture is deliberately not ranked using Boolean approximate degree: it concerns real bounded polynomials, variance and coordinate influences. Its complete parameter-to-centrality mapping is not assessed. Likewise, q-analog questions do not borrow symmetric-group measure counts for as-yet unspecified models.

## Maintenance checks

Tests check work-level deduplication, exclusion of derived records and web missions, archive classification, explicit recurrence evidence, conditional core implications, null sorting, URL round trips, scope-safe comparison links, mathematical rendering and reference integrity. A newly reported resolution must be recorded in the catalogue before it changes the active/archive classification. Adding citations without passage-level evidence must not increase the recurrence score.


## Literature-status check

The [23 October 2026 audit](question-status-audit-2026-10-23.md) distinguishes recent primary sources explicitly preserving an open question, searches finding no resolution, and unresolved formulations. Each question card exposes its own summary, exact locators, queries and limits. A date update never changes a negative search into a proof of openness. Five questions now have multiple distinct-work sightings; proceedings and manuscript versions still count once.
