# Conjecture and publication audit, 17 October 2026

Later status: see [the broader inventory audit](broader-inventory-audit.md), including the obtained DFLLV26 final journal and expanded completion/domain inventory. Pending statements below describe that earlier audit stage.

This round checked statements and proof routes, not all proof steps or the entire forward-citation literature.

## Absolute sparsity versus logarithmic sparsity

KLMY21survey Conjecture 3.19 literally asserts `spar(f)<=poly(approx_spar(f))`. This is false. Sparse25 Remark 1.2 gives OR, and Claim 4.15 gives the stronger near-top threshold example: for `f(x)=1 iff |x|>=n-1`, exact monomial sparsity is `n+1`, while approximate sparsity is `O(log n)`. Its exact coefficient weight is `2n-1`, while approximate weight is `O(1)`.

The exact polynomial is `sum_i product_{j!=i}x_j -(n-1)product_j x_j`. For approximation, take a collection of `O(log n)` pairs of partitions such that every pair of coordinates is separated in at least a two-thirds fraction of the pairs. For each pair of partitions, a constant-size polynomial tests that all zero coordinates lie on one side of both partitions. Average these polynomials. Inputs with at most one zero always pass; any input with at least two zeros passes at most one-third of the tests. Random pairs of partitions, Chernoff bounds and a union bound construct the separating collection.

The positive result is instead `log(2+spar)=O(log(2+approx_spar)^2 log(2n))`. DMbasis25 proves the ordinary monomial result; Sparse25 extends this to coefficient weight, signed generalized monomial sparsity and signed generalized weight. The catalogue records all eight exact/approximate cross comparisons on this logarithmic scale, with the input factor explicit. A deep max-degree restriction tree retains large exact degree at typical leaves but eliminates high-degree terms of a putative sparse approximant; the quadratic exact/approximate degree theorem gives the contradiction. Two-sided restriction trees handle generalized monomials.

Do not identify this with a proof of the literal 2021 conjecture, even where the later abstract describes its result as confirming the conjecture. Also do not infer resolution of KLMY21 Conjecture 6.1, the pure input-independent deterministic AND-query bound.

A further extraction gap remains in Sparse25 Section 4.4: the printed AND-query/log-approximate-sparsity bound and the intervening displayed bounds need a formula-level check against the final proceedings version. This audit has not entered that bound as verified. The earlier ECCC report and later report remain distinct bibliography entries.

## Extremal Forrelation: revision changes the model

CCM26 v2, dated 1 October 2026, proves `Rna=Omega(2^((1/2-o(1))*n))`, while exact quantum query complexity is one. Here `n` is oracle address length and the Boolean input length is `2^(n+1)`. This is a nonadaptive classical lower bound. It does not replace GS26's adaptive lower bound or resolve its Conjectures 6 or 7.

The proof generalizes a bent-function hidden-subspace construction and controls nonadaptive transcript total variation by counting dependent query configurations. Appendix D explicitly identifies a gap in the v1 partial-spread construction and replaces that argument. Searching by the original abstract alone would incorrectly mark the adaptive conjecture resolved.

## Search comparisons and journal versions

CDM25 is the 57-page journal version, computational complexity 34, article 20, published 8 November 2025. Journal locators have been added to twelve existing records, preserving their earlier priority sources. New records index both directions of deterministic, randomized and pseudo-deterministic size versus positive AND/OR query conversions, and the multi-output inequalities `C<=s*bs` and `D<=2*C*bs`.

CDM25 Proposition 6.6 gives `log size/(2 log n)<=AND/OR queries<=4 log size`. Its syntactic tree expansions and balancing preserve labels and work for relations, while Lemma 6.9 minimizes over canonical selectors. The reverse conversion is exponential, not a finite power of query cost. Sizes here count leaves.

The publisher HTML abstract names CONJ and ApproxHW, whereas the downloaded PDF uses positive AND/OR queries and ApproxHamWt. The pinned PDF definitions govern these records; the HTML wording is not evidence for silently transferring the theorem to signed conjunction queries.

CMP25 is the Quantum 9, 1777 journal version of CMP22. Theorem 1.3 and Corollary 5.5 retain error `2/5` for randomized relation simulations. The proof samples a classical tree, computes its deterministic output with sufficiently small quantum error, and adds the two failure contributions. Node size and coupled rank/depth conventions remain explicit.

## Original historical sources and remaining status gaps

The EH89 and Nis91 publisher full-text requests, and the Nis89 conference PDF request, failed. See `data/source-access-audit.json`. Bibliographic metadata and the Nis91 abstract are available, but these are not original proof access. Original theorem locators, constants and first-publication proof priority therefore remain pending. Existing later-source proof summaries retain their weaker audit status.

Targeted searches found no resolving primary source for BK24's three search questions, the quadratic deterministic/block-sensitivity conjecture, or the pure monomial AND-query conjecture. Their status remains unverified; failure to find a resolution does not establish that a question is currently open. Unindexed search cells likewise remain extraction gaps, not claims of unknown mathematics.


## Update after user-supplied originals

The user subsequently supplied the original EH89 journal PDF and Nis89 STOC PDF. Their relevant statements and proof routes are now checked; the earlier failed-access entries above are historical. Nis91 journal full text remains uninspected. See [the original-source follow-up](originals-and-domains.md) for node-size conventions, randomized expected-cost normalization and an unresolved literal-constant discrepancy in the one-sided theorem.


## Subsequent constant and completion update

The earlier unresolved one-sided constant issue has now been resolved under the literal expected-cost convention: factor 2 is false and the certificate method gives sharp factor 4, recorded as a repository derivation. The journal Nis91 text is still unchecked. Completion and symmetric-group matrices, relevance comparisons and current residual gaps are described in [the latest follow-up](completion-and-symmetric-audit.md).
