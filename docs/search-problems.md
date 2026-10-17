# Search relations: models, results and unresolved audit cells

Use the [search pair inventories](search-matrices.md) for separate full-cube and promised relations. They include bit queries, polynomial systems, adversary/sensitivity measures, tree size, distributional depth and restricted query oracles. These inventories expose unindexed pairs; they do not assert that each pair's optimal exponent or current literature status has been settled.

## Domain and output requirements

A relation S assigns a nonempty set S(x) of valid answers to each promised input. A total relation in this catalogue has a solution on every input of the entire Boolean cube. A solver can output different valid answers on different runs. A pseudo-deterministic solver must, for each input, return one fixed valid selector g(x) with probability at least 2/3. Its canonical selector may depend on the algorithm but not on that run's coins or measurements.

An arbitrary total relation need not have short locally checkable answers. Query-TFNP requires a polylogarithmic verification bound, and is a more restricted class. The verification measure V charges input queries needed to test a supplied candidate answer. AOES and approximate Hamming-weight search must not be promoted to short-verification query-TFNP examples.

A single-valued multi-output function is also distinct from a relation. Sensitivity for that function means its output label changes; it is not an existential choice between overlapping answer sets.

## Polynomial systems and adversary measures

BK24 Definition 10 uses nonnegative polynomials p_c, with total mass at most one **on the whole cube**, and mass at least 1-epsilon on valid answers at each promised input. Relation approximate degree minimizes their maximum degree. Exact relation degree is the error-zero case. The unbounded-off-promise version has its own ID. Conical degree replaces each p_c by a nonnegative combination of literal conjunctions. Conjunction width and source degree conventions should be checked before reusing a normalization.

Positive and classical relation adversaries constrain only input pairs with disjoint valid-output sets. Relation block sensitivity likewise requires disjoint valid-output sets after a block flip. Critical block sensitivity instead minimizes over valid selectors and takes its local maximum only on inputs having exactly one valid answer. These are different constructions. If there are no critical inputs, the critical maximum is zero.

[ABK21](https://doi.org/10.4230/LIPIcs.CCC.2021.30) and [BK24](https://arxiv.org/abs/2410.16245), Section 5, give the following source-checked comparison routes:

- Adv<=CAdv<=2 Adv², including relations.
- bs<=fbs<=CAdv and fcbs<=2 CAdv.
- fbs and fcbs are O(rel_adeg²) at fixed error below one half.
- Adv lower-bounds Q; CAdv lower-bounds R.

Do not reverse a comparison, or extend CAdv<=cfbs from partial decision functions to relations automatically. BK24 explicitly asks whether the decision-function bound Adv=O(approximate-degree²) extends to total search; that 2024 question remains marked current-status-unverified here.

## Main separations and their proofs

**Quantum queries versus polynomial and conical degree.** BK24 Corollary 40 constructs total query-TFNP relations on poly(n) bits with bounded polynomial and two-sided conical degree O(polylog n), but Q=tildeOmega(sqrt(n)). Repeated AND-OR search admits short polynomial/conical descriptions after a small family of XOR shifts. A quantum direct-product lower bound followed by a union bound over shifts proves query hardness. The construction parameter n is recorded separately from input length.

**Polynomial degree versus positive/classical adversaries.** BK24 Definition 44, Lemma 45 and Theorem 46 use pigeonhole search: find two identical input blocks and supply their common value. Disjoint valid-certificate sets force inputs to be far apart, so uniform adversary weights give CAdv<=2 log(n/2). Symmetrizing any output-polynomial system and reducing to collision gives rel_adeg=tildeOmega(n^(1/3)). The same family separates Q and R from both adversaries. Storing the shared value in the output matters to the disjoint-output argument.

**Search-to-decision transfer.** BK24 Definition 18 adds a bit y_c for every certificate c and promises that all bits indexed by valid certificates agree; the decision task asks for their common value. Polynomials transfer as sum_c p_c(x)y_c. Measuring a decision algorithm's query register and checking the sampled certificates gives a reverse query reduction. Theorem 19 guarantees a cube-root quantum lower-bound transfer, with polylogarithmic losses, not a cost-preserving reduction. The construction, eight measure-transfer statements and proof route are stored in the catalogue's `reductions` records. Corollary 41 gives partial decision functions with low bounded approximate and conical degrees but quantum query complexity tildeOmega(n^(1/6)).

**Pseudo-deterministic hardness with easy randomized solving.** [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36) proves Find1 on the dense-input promise has R=O(1), psQ=Omega(sqrt(n)), and establishes a completeness reduction from efficiently verifiable search. It also gives total query-TFNP examples from expanding unsatisfiable constraint systems. [AGL26](https://doi.org/10.4230/LIPIcs.ICALP.2026.3), Theorem 1, strengthens the gap to R=O(1), psQ=Omega(N) for the arbitrary total relation AOES. Its XOR blocks hide a string; blind random output usually avoids it, while a stable valid output yields information needed to solve XOR. This stronger example has expensive verification.

**Quantum canonicalization advantage.** AGL26 Definition 36 and Theorem 37 use a Simon instance as a key to a canonical approximate Hamming weight. The promised QL-Estimation problem has psQ=O(log N), psR=Omega(sqrt(N)), and R=O(1). The randomized algorithm whose output is canonized uses O(log N) queries. A query to the Simon oracle returns an n-bit symbol, whereas a query to the weight string returns one bit; N=2^n is a parameter. This model is recorded explicitly and excluded from bit-query inference.

**Restricted query oracles.** [CDM23](https://doi.org/10.4230/LIPIcs.MFCS.2023.34), with full proofs in its [ECCC report](https://eccc.weizmann.ac.il/report/2023/039/), treats conjunction and parity queries. Positive-conjunction queries contain no negated literals; their measures are separate from literal-conjunction depth. Approximate Hamming-weight search has constant randomized positive-conjunction complexity but linear canonical complexity. For total SearchOR, deterministic parity depth is n, yet canonical randomized parity depth is O(log n log log n): binary search using random parity tests finds the first marked bit. The deterministic lower bound is the affine-subspace dimension argument. This does not contradict cubic derandomization for bit-query search.

## Derandomization, constants and priority

[CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Theorems 3.1–3.2, proves for total multi-output functions C<=s bs, s<=bs<=3R, D<=2 C bs and D<=C². Consequently D<=54 R³. Choosing the canonical selector gives **D(S)<=54 psR(S)³** for every total bit-query search relation. The constant 54 is the direct combination of those inequalities, not a claim of optimality.

[GGR13](https://www.wisdom.weizmann.ac.il/~oded/p_balg.html), full-report Theorem 4.1(3), previously proved a quartic bound, without an input-length logarithm, and an additional output-range-dependent bound. Its nonadaptive result, Theorem 4.1(2), gives deterministic nonadaptive complexity at most three times canonical randomized nonadaptive complexity. Its Corollary 4.2 supplies the original constant-randomized versus linear-canonical approximate Hamming-weight example. These original statements have now been inspected directly rather than inferred solely from later citations.

AGL26's comparison to an older quartic classical bound must therefore not be read as the classical frontier. Its separate quantum theorem, D(S)=O(psQ(S)^5 log N), retains the input-length logarithm; it is not a pure fifth-power inequality. The same paper proves psQ(S)=O((R(S)+V(S))*sqrt(N)), retaining verification and input-length factors.

For leaf size, CDM23full Corollary 5.3 bounds log DSize in terms of log psDSize, log input length and log output-range size. These logarithms are preserved. Randomized size means the maximum size among trees in the support, not its expectation; distributional size and depth have explicit input distribution and error parameters.

## Reading routes and remaining work

The general survey entry points remain [the annotated surveys](surveys.md): Buhrman–de Wolf for the classical framework, Ambainis and Aaronson for quantum promises, Bun–Thaler for approximation, and the sensitivity surveys for the full-cube combinatorics. For search specifically, read the introductory comparisons and definitions in BK24, GIPS21, CDM23 and AGL26; these are research papers with useful overview material, not relabelled as surveys.

The all-pair search inventory still has unindexed cells. Complete extraction of size separations, distributional and expected-cost canonicalization, AND/OR models, error-dependent constants, historical source typography and first-attribution chains remains necessary. BK24's 2024 questions on exact quantum/randomized search and polynomial-system degree are preserved as dated questions; their present status has not been certified. No HTML has been started.
