# Independent mathematical audit of the lambda-partite lift

**23 October source-audit update.** The imported cube construction needs output-value transpositions from columns of B; the printed input/A-column construction fails in S_3. The corrected proof preserves the old query bound. The new [complete proof](hypermatching-proof.md) additionally establishes quadratic intrinsic degree. The [fresh source audit](hypermatching-full-source-audit.md) supersedes earlier acceptance of the uncorrected imported orientation.

Audit date: 2026-10-17. Scope: the complete argument in `docs/lambda-partite-lift.md` and claim `lambda-partite-D-sensitivity-product-lift`. This is a separate-agent mathematical check of the argument, not a priority or optimality certification. The inspected original is the final DFLLV26 journal, `work/sources/DFLLV26journal.txt`, including its actual lemma proofs, Section 2.3 parameter definitions, Section 5.3 pseudo-characters and Theorem 5.5. No authoritative file was edited.

## Verdict

The displayed bound is valid for the stated full lambda-partite domain and vertex-to-entire-hyperedge query model. There is one false sentence in its simulation proof that should be replaced, but the corrected simulation is valid. The domain parameters admit a stronger conflict bound, removing the factor depending on the ratio of color multiplicities. Specifically, the same proof establishes

\[
D(f)\le 10368(2k-1)^{10}s(f)^{10}.
\]

This is uniform in the multiplicities for fixed total edge size k. It does not establish quadratic intrinsic degree versus sensitivity on hypermatchings. Priority and stronger exponents have not been checked.

## 1. Product degree and witnessing: pass

Give the product uniform measure and let E^i_j be the direct sum of the isotypic components of S_(N_i) of depth exactly j. By final-journal Theorem 5.5 (article p.32, PDF p.33) and the isotypic decomposition, V^i_d is the orthogonal sum of E^i_j for j≤d. Indicator monomials on the product factor into component monomials, so the degree-at-most-d space is exactly the orthogonal sum of tensor products E^1_(j_1) tensor ... tensor E^r_(j_r) with sum j_i≤d. Both inclusions hold: factor monomials generate the filtered space, and the individual E^i_j lie in V^i_j.

For a nonzero degree-d function F, its exact-degree-d projection is nonzero. A tensor product of spanning pseudo-characters from those E^i_(j_i) therefore has nonzero inner product with F, for some sum j_i=d. This last statement uses the orthogonality of the filtration layers and does not assume that an arbitrary nonorthogonal spanning family detects the top degree.

Section 5.3 (article pp.33–34) constructs each factor pseudo-character with values in {-1,0,1}, with support partitioned into parity cubes of dimension D_i≥j_i/2. Their products partition the product support into cubes of dimension sum D_i≥d/2. At each vertex, changes in different factors concern disjoint tagged permutation entries; within each factor the original disjointness property holds. Every change removes exactly two entries, equal to the chunk size of the product. Thus the precise hypotheses of Lemma 5.2 hold. Consequently s_Z(F)≥sqrt(d/2), or deg_Z(F)≤2s_Z(F)^2. The constant-function case is immediate.

## 2. Product parameters and certificate chain: pass, with improvement

Encode the product as sets of tagged permutation entries. Each input has N_total=sum_i N_i entries. It is composable componentwise. Every entry lies in exactly two queries, its forward and inverse query, so Delta=2. Minimum changes are single transpositions in one factor, of chunk size two (N_i≥2 follows from n≥2 and lambda_i≥1).

For beta_c≥1/3, apply the cycle-shortcut construction in the source Section 2.3.2 (article p.17) separately in every differing factor and leave all other factors equal to y. The shortening sets y\z are disjoint both inside a factor and between factors. The number of shortenings is at least one third of the sum of the factor disagreements. Every shortening removes two entries. This proves the exact product parameter required by Lemma 3.5.

The stated lower bound M≥min_i N_i is conservative and valid. In fact M=N_total is permitted: two partial inputs not separated by any forward or inverse query have a union which is a partial bijection in every factor. Each partial bijection extends to a full permutation, and their product extends the union. Hence incompatible partial inputs always have a separating query, regardless of their sizes. This is the same extension argument printed for one symmetric group in Section 2.3.2, applied componentwise. In the source convention that M is capped by input size, choose M=N_total.

Lemma 3.5, then Lemma 3.6, and exact degree ≥ approximate degree yield

C_Z≤3s_Z bs_Z≤18s_Z deg_Z²≤72s_Z^5.

Lemma 3.3 now gives D_Z≤2 C_0 C_1≤2 C_Z²≤10368s_Z^10. There is no requirement that the lifted Boolean function be invariant under component relabeling for these inequalities.

## 3. Oracle simulation: pass after correcting one sentence

Fix a hypermatching H. Maintain partial bijections whose assigned groups are complete hyperedges of H; whenever a group is assigned, fill every color's positions in that group. Every assigned vertex is thereby known, and every unassigned vertex belongs to an undiscovered hyperedge.

A forward query into a free group can choose any unassigned vertex of the queried color. Querying that vertex reveals an undiscovered hyperedge, which may consistently be placed in the requested group. An inverse query about an unassigned vertex similarly reveals an undiscovered hyperedge which can be placed in any free group. Positive lambda_i ensures every free group has positions in every color. Known queries require no oracle call. The rules handle either convention for which side of a permutation is called forward.

At every stage, the resulting transcript has at least one complete representation whose projection is H: assign the remaining hyperedges bijectively to the remaining labels and order each color within its group arbitrarily. If the F-tree reaches a leaf, this complete representation follows the same transcript, and its F-value is f(H). Thus the simulated output is correct and each permutation query costs at most one hyperedge query.

The current sentence 'every completion of the stored representation projects to that same hypermatching' is false until all groups have been filled. Arbitrary completions may regroup the undiscovered vertices into other hypermatchings. Only existence of a completion representing the fixed H is needed. Replace that sentence by the preceding extension invariant. This repair changes no bound.

## 4. Sensitivity transfer: pass

At a fixed product representation, disjoint sensitive chunk-two changes are transpositions in individual factors. Disjointness of old permutation entries implies that no position is involved in two changes. A same-group transposition leaves the projected hypermatching unchanged and cannot be sensitive. Every sensitive transposition therefore produces a multigraph edge joining two distinct original hyperedges.

Every original hyperedge contains exactly k positions across all factors. Hence its multigraph degree, with parallel edges counted, is at most k. Greedy matching deletes at most 2k−1 edges at each step, including parallel edges; therefore it selects at least t/(2k−1) edges from t transpositions.

Every selected transposition swaps vertices of one color between two hyperedges. Each resulting edge differs from both original edges (even when the relevant color has only one vertex per edge), so the change removes exactly two old hyperedges. These are minimum nonzero changes: changing only one hyperedge is impossible because all remaining vertex usages force that edge. Selected multigraph edges are disjoint, hence the removed old hyperedge pairs are disjoint. Each selected change is sensitive by definition of F. Therefore s_Z(F)≤(2k−1)s(H-domain f), pointwise and then maximized.

## 5. Source scope and remaining limits

All imported constants and hypotheses match the inspected final journal: Lemma 3.3, Lemma 3.5, Lemma 3.6, Lemma 5.2 and Theorem 5.5. The tensor assembly, hypermatching projection, simulation and matching argument are repository derivations, not printed DFLLV26 theorems. No assertion is made that the journal's hypermatching representation-theoretic obstruction is solved: witnessing was proved only for the permutation product. Neither this independent audit nor the final journal determines priority, sharp exponents, or applicability to promises restricting the allowed hypermatchings. Full-domain availability is essential to the stated source framework and extension arguments.

## Incorporation status

The simulation invariant has been corrected in the main proof and earlier uniform-lift summary. The full conflict bound and improved coefficient have been incorporated into the claim and generated profiles. The original audited text hash, original claim and corrected text hash are retained in data/lambda-lift-independent-audit.json. This review is not formal verification or human peer review.
