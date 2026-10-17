# Size, restricted queries and original attribution

This audit supplements [the search overview](search-problems.md), [the priority report](priority-audit.md) and the [average-cost audit](average-cost.md). The final MFCS version of CDM23 is essential: its earlier ECCC report lacks several of the results below.

## Final-version additions

CDM23 Theorem 4.5 proves that **every total completion** of the promise ApproxMaj (weight<=n/2 versus weight>=3n/4) has randomized leaf size exp(Omega(n)). The proof uses a corruption distribution built from extreme upward neighbors: small leaves cannot collect enough zero-side mass without incurring too much one-side error. The paper explicitly credits this corruption argument to Swagato Sanyal.

Thresholding the answer of any approximate-Hamming-weight selector produces such a completion. Consequently Theorem 4.6 gives a total relation with ordinary randomized leaf size O(1) but canonical randomized leaf size exp(Omega(n)). This is stronger than the earlier lifted exp(Omega(sqrt(n))) size family of GIPS21. The earlier family remains distinct; the input and gadget conventions must not be combined.

For dense random unsatisfiable 3-CNFs without lifting, Corollary 4.4 gives canonical size exp(Omega(n^(1/4)/log n)), versus constant ordinary randomized size. The exponent and logarithmic loss are retained. It follows by combining deterministic size lower bounds and the logarithmic-size derandomization theorem, not by importing the lifted-family lower bound.

The final paper's Section 5 adds positive AND/OR trees. Lemma 5.5 compares their canonical depth with log canonical leaf size within a log n factor. Approximate Hamming weight therefore has constant randomized AND/OR cost but canonical cost Omega(n/log n). Theorems 5.4 and 5.7 give canonical-to-deterministic simulations for positive AND and AND/OR queries, with input-length logarithms and output-range factors explicit. A query can read an entire subset conjunction/disjunction for cost one; these are not bit-query bounds.

## The original size derandomization source

[CDMRS23](https://doi.org/10.1145/3564246.3585199), Theorem 3.1, proves

    log coverN = O((log RSize)^2 log n),
    log DTSize = O((log RSize)^4 log^3 n).

It uses block number—the number of minimal sensitive blocks, rather than their maximum disjoint packing—to obtain the cover bound. The source traces that counting measure to Kulkarni–Tal. Tree balancing converts log size to AND/OR depth, giving fourth-power derandomization with log^7 n. A separate fractional hitting-set and zero-answer-depth argument gives positive AND derandomization with third power and log^4 n.

Deterministic rank/size is attributed there to Ehrenfeucht–Haussler 1989. That bibliography entry is now complete, but the original full text has not been inspected; the checked proof route is the reproduced relationship in CDMRS23. Randomized rank takes the worst rank in the support, and the same tree transformation gives its logarithmic-size counterpart. Rank and depth bounds referring to one tree must not be combined using separately optimal trees.

## Names and symbols that collide

- `R^{0-dt}` counts **zero answers** along a path. It is not the expected zero-error cost `R0`.
- Loff–Mukhopadhyay 2019 uses `D^{dt}_0`; KLMY21 uses `P^{0-dt}` for this zero-answer measure. The original Definitions 9–10 and Lemma 11 are now checked, and the short proof is reproduced in KLMY21 Claim 4.4.
- KLMY21 uses bare `HSC` and `FHSC` for input-directed hitting-set quantities (`MCC` and `fmbs`). CDMRS23 uses bare `HSC` for ordinary certificate complexity and adds a zero subscript for the directed quantities. The source and direction are part of the alias.
- KLMY21 `spar` counts coefficients in the **0/1 monomial basis**. It differs from Walsh Fourier sparsity. AND_n has one 0/1 monomial but 2^n nonzero Fourier coefficients. Its logarithmic sparsity theorems are stored under a new monomial-sparsity ID.
- CDM23 and CDMRS23 size counts leaves. CMP22 `DTSize`/`RDTSize` count **all nodes**. For full binary trees, nodes=2 leaves-1; the count variants remain separate IDs.

KLMY21's fractional-hitting-set definition prints “smallest” feasible p where its LP and subsequent arguments require the largest feasible p. The catalogue uses the explicit LP normalization and retains the textual discrepancy.

## Quantum size simulation and its error parameter

[CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Corollary 9, gives quantum cost O(sqrt(s)) to identify the reached leaf of a correct deterministic tree with s nodes. This computes a unique leaf, so its error can be reduced before mapping the leaf to a relation answer.

For a **randomized** classical tree, Corollary 27 gives Q_{2/5}=O(sqrt(RDTSize)), not the catalogue's default Q_{1/3}. Sampling a classically successful tree and identifying its leaf with probability 9/10 gives success (2/3)(9/10)=3/5. For a Boolean decision function, majority voting converts this to the usual fixed-error Q. For arbitrary relations, different successful runs can return different valid answers, so majority error reduction must not be assumed. The error-parameter relation measure is separate, and this guard also applies to the randomized rank-depth simulation.

The original O(sqrt(TG)) guessing-algorithm route is [LL16](https://theoryofcomputing.org/articles/v012a018/), Theorems 5.4–5.5. Its bomb-query model satisfies B=Theta(Q²) at fixed error; Theorem 4.1 retains an inverse explosion-budget factor when that parameter varies. [BT20](https://doi.org/10.22331/q-2020-03-02-241) supplies span-program/adversary proofs, nonbinary alphabets and expected parameters for a single randomized algorithm. CMP22 proves guessing complexity equals Strahler rank and optimizes edge weights to get the node-size bound. Each step now has its own bibliographic and proof record.

## Conjectures and input-length dependence

KLMY21survey Conjecture 3.16 asks for DandPos<=poly(RandPos,log n). CDMRS23 resolves it as stated. This is not a pure power relationship: the threshold weight>=n-1 has constant randomized AND-query complexity and deterministic complexity Omega(log n). Its randomized algorithm tests conjunctions of random complementary subsets; its deterministic lower bound follows from the monomial count of a shallow conjunction tree.

The survey's stronger exact/approximate monomial-sparsity conjecture and the earlier conjecture eliminating input-length dependence from the sparsity/AND bound are retained separately, with present status unverified. Resolving a consequence of either conjecture does not resolve the stronger conjecture. Targeted searches did not identify resolutions of BK24's exact-query and relation-degree questions; that search outcome is recorded without declaring them open today.
