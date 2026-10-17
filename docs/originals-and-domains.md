# Original-source and domain follow-up, 17 October 2026

Later status: see [the broader inventory audit](broader-inventory-audit.md), including the obtained DFLLV26 final journal and expanded completion/domain inventory. Pending statements below describe that earlier audit stage.

## Supplied originals

The user supplied Ehrenfeucht–Haussler's *Learning Decision Trees from Random Examples*, Information and Computation 82(3), 231–246 (1989), and Nisan's *CREW PRAMS and Decision Trees*, STOC 1989, 327–335. The latter is the conference predecessor of the still-uninspected SIAM Journal on Computing 20(6), 999–1007 (1991) version. SHA-256 snapshots preserve these identities; neither supplied PDF is redistributed in the archive.

EH89 defines tree rank `r(Q)` on p.234 and function rank `r(f)` on p.241. Lemma 1(i), p.235, uses **total nodes** k. A rank-r tree needs at least `2^(r+1)-1` nodes; the maximum leaf count in a reduced n-variable tree is `sum_{i=0}^r binom(n,i)`. The recurrence splits into ranks r and r-1 after the root query. Convert to leaves via `k=2L-1`. The original now supports the rank/size record previously checked through CDMRS23.

Nis89 Section 2 uses `s_w(f)`, `bs_w(f)` and `C_w(f)` for input-local quantities, and maximizes over w for global measures. Lemma 2.4, p.331, proves `C<=bs^2`: a maximal family of disjoint minimal sensitive blocks covers a certificate, and the altered input is sensitive to every coordinate of each minimal block. Lemma 2.5, p.332, records `C<=D<=C^2` and credits earlier work, perhaps first Blum, citing Blum–Impagliazzo; this should not be attributed as a new Nisan theorem.

Nis89 Section 1.2, p.329, defines cost as worst-case **expected** queries. `R_2` has error at most 1/4; `R_1` always rejects 0-inputs and accepts 1-inputs with probability at least 1/2. These now have separate catalogue IDs. Lemma 4.2, p.334, proves `bs<=2R_2`: distinguishing a point from each disjoint sensitive-block neighbor forces query probability at least 1/2 for that block. Lemma 4.1, pp.333–334, gives `D<=2C_1 R_2` by iterative certificate queries and expected-cost reduction. Together they give Theorem 4's `D<=8R_2^3`. Constant-error amplification transfers the exponent to the default capped randomized measure, but not the constant 8 unchanged.

There is a remaining normalization issue in Theorem 3's printed `D<=2R_1^2`. Under the literal expected-cost definition, the one-bit identity can reject immediately with probability 1/2 and query otherwise, giving expected cost 1/2 and meeting the one-sided requirement. The printed inequality would give `1<=1/2`. Its source statement is recorded historically, with the exact constant blocked from inference until reconciled. This does not refute the asymptotic quadratic relation.

## Search inventory

Added elementary records for exact bounded relation degree versus exact quantum cost, approximate versus exact degree, promise-only versus globally bounded relation approximation, conical junta degree versus randomized cost, and solver-model containments. On total relations the bounded and promise-only approximate systems coincide. For promises only the relaxation direction is entered. Exact quantum cost now appears explicitly in the search matrices.

For the conical upper bound, each capped classical computation leaf contributes a nonnegative weighted conjunction of at most R literals. For exact quantum degree, use output-probability polynomials of degree at most twice the number of queries; positivity and normalization hold on the entire cube, including off-promise inputs.

A purported ECCC revision search hit was inspected and rejected: TR24-172 is *Quantum Communication Advantage in TFNP*, not a revision of BK24. BK24's arXiv record still lists only v1. No resolving primary source for its three open questions was found; their current status remains unverified.

## Relevant variables

The existing relevant-coordinate count now has the historical alias `R(f)` from Chiarelli–Hatami–Saks, which clashes with randomized query complexity. The source proves an `O(2^degree)` upper bound using coordinate-local degree weights and restrictions to maxonomial hitting sets. Its bound `6.614*2^degree` is historical; Wellens' 2022 theorem improves the constant to `4.394`. The catalogue also includes Wellens' certificate bound `4^C/2` and the stronger monotone degree, sensitivity and depth bounds, with proof summaries.

No finite pure power of degree bounds relevant-variable count: a read-once complete depth-d decision tree with distinct variables at internal nodes can depend on `2^d-1` variables. Consequently, this strand needs exponential relationships in addition to exponent tables. Current-best constant certification and the full history remain incomplete.

## Other domains

Dafni–Filmus–Lifshitz–Lindzey–Vinyals develops complexity measures on the symmetric group, perfect matching schemes, slices and multislices in a common set-system framework. The full 2020 preprint and ITCS 2021 extended abstract are distinguished from the 2026 Combinatorial Theory journal metadata. Journal proof text remains unchecked.

For S_n, queries ask `pi(i)=?` or `pi^{-1}(j)=?`, returning a symbol in [n]. Degree is degree in permutation-matrix indicators. Sensitivity is the maximum size of a family of **disjoint sensitive transpositions**, whereas edge sensitivity t counts **all** sensitive transpositions. Block sensitivity allows disjoint moved-point supports of arbitrary permutations. Separate measure IDs and permutation-domain scopes prevent Boolean-cube inference.

Corollary 5.6 gives `degree<=2*s^2`: tableau pseudo-characters witness degree and induce a Boolean cube of dimension at least degree/2; apply Huang's sensitivity theorem there. Theorem 3.1 gives `bs<=6*approx_degree^2` by restricting to independent sensitive blocks and using the polynomial method. The complete non-cube pair matrix, general-domain parameters, perfect-matching definitions and multislice refinements remain extraction gaps.

The new HKMP26 full preprint and MFCS 2026 proceedings are bibliographically indexed, including their title change. Their promise-aware and minimum-over-completions measures, conjectures and all parameterized bounds remain on the extraction queue. The 2025/2026 Hamming-graph relevant-variable results are additional leads; they have not been promoted from search snippets into verified claims.


## Subsequent constant and completion update

The earlier unresolved one-sided constant issue has now been resolved under the literal expected-cost convention: factor 2 is false and the certificate method gives sharp factor 4, recorded as a repository derivation. The journal Nis91 text is still unchecked. Completion and symmetric-group matrices, relevance comparisons and current residual gaps are described in [the latest follow-up](completion-and-symmetric-audit.md).
