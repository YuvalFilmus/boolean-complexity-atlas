# Completion closure and formulation audit

Later developments: see [higher-support and profile audit](higher-support-and-profile-audit.md) for the current sufficient normalization cases, tighter chains and domain-profile inventories.

All 506 ordered comparisons in the fixed 23-measure completion inventory now have an indexed upper chain or a no-finite-power witness. This is a coverage milestone for that inventory, not a claim of sharp exponents, optimal constants or exhaustive measure coverage. The 132 core cells retain their separate lower evidence and endpoint losses.

## Newly indexed elementary proofs

AIK26's preliminary definitions (article p.3) fix C_b, UC_b, UC, and the orientation and query cap of R_1. Restricting a maximum gives C_b<=C and UC_b<=UC. Dropping unambiguity gives C_b<=UC_b. The leaves labeled b in a deterministic tree give disjoint certificates of width at most D, so UC_b<=D and UC<=D. On a total function, summing the indicators of an unambiguous b-certificate partition is exactly f or 1-f; hence degree<=UC_b for either b.

A one-sided algorithm is a bounded-error algorithm, so R<=R_1. For every positive input, a positive-probability accepting transcript gives a positive certificate: any compatible negative input would also have that accepting transcript, contradicting no false positives. Thus C_1<=R_1 under the capped convention. A deterministic tree is one-sided. Truncating an expected zero-error tree at a constant multiple of its worst-input expectation and returning zero on timeout also gives R_1=O(R_0). This last argument uses the repository's expected R_0, not an identification with AIK26's capped inconclusive convention.

The fractional covering and sensitive-block packing LPs are dual at each input, giving FC=fbs. Aaronson's original Theorem 7 gives QC=Theta(sqrt(RC)); Lemma 5 identifies randomized verification with a nonadaptive fractional sampling problem. Combining it with the fractional-cover formulation gives QC=Theta(sqrt(FC)). Directed copies of these comparisons now supply completion chains. Repetition also gives Q=O(Q_0). A minimum-completion upper chain always chooses a completion optimal for its right-hand measure; no independently minimized product is used.

## Total witnesses and completion lower obstructions

OR_n has C_1=1; AND_n has C_0=1. Each has n singleton sensitive blocks at its unique extreme input, exact degree n and approximate degree Omega(sqrt(n)). Their fractional certificate/packing cost is n, randomized verification is Theta(n), and quantum verification is Theta(sqrt(n)). The indexed simulations and relaxations show that every other measure in this 23-measure inventory diverges on these witnesses. Consequently no finite power of the constant one-sided certificate measure bounds those measures.

For the relevant-variable directions, use the address function with k address bits and 2^k data bits. Every bit is relevant, but a deterministic algorithm reads k+1 bits. Its leaf partitions and simulations bound UC, UC_b, fbs, FC, QC, Q_0 and R_1 by O(k+1). Relevance is therefore not bounded by any fixed power of those measures. These witnesses are total functions and have unique completions, so the same obstructions apply to minimum-completion measures.

The generated inventory has 310 pure upper-chain cells, 132 core evidence cells and 64 no-finite-power cells. Upper chains can be weak. A cell with an upper chain is not thereby furnished with a matching separation or optimality proof.

## General domains: uniformity fails in seven more explicit directions

The common-oracle twelve-measure inventory now has 43 parameter-free upper chains and seven no-uniform-power cells, out of 132 ordered cells. Domain-dependent bounds remain separate. The exact-query degree comparison is explicitly DFLLV26 Lemma 2.2(l), article p.13: degree<=2Q_E. Classical randomized queries can also be simulated quantumly.

On the all-distinct multislice with forward-only coordinate queries, take f(pi) to indicate whether the position of 1 lies in the first half. Observing the coordinate containing 1 is a one-coordinate certificate. The certificates for the distinct possible positions partition both output classes, so C=UC=1. The sum of the entry indicators in the first half represents f with degree one. Every sensitive change includes the original position of 1, so bs=fbs=s=1; a sensitive swap exists. D=n/2, since before n/2 queries an adversary can avoid returning 1 and leave positions in both halves.

Thus none of degree, approximate degree, C, UC, bs, fbs or s gives a uniform polynomial upper bound on forward deterministic cost over all these domains. This also obstructs a universal bound over the larger class of composable domains. It does not contradict the parameterized theorem: the overlap parameter for this multislice is zero. Nor does it contradict the forward-and-inverse permutation results, since an inverse query locates 1 immediately. The other 82 cells remain without a uniform upper chain or this kind of obstruction in the inventory; two of them have direct parameterized bounds.

## What the normalization assumptions can and cannot yield

The earlier sufficient repair remains valid: if a degree-d perturbed polynomial q has full-cube margin gamma and range bounded by K, composing q/K with a sign approximant gives approximate degree O(dK/gamma). A coefficient perturbation of s coordinates gives only K<=1+sM when the original polynomial is bounded by one. This proves the polynomial-support sufficient condition, and handles M=0.

There is now a stronger explicit obstruction to dropping that support dependence in the enlarged-basis setting discussed after HKMP26 Lemma 71. For odd n, set p=x_1 and q=sum_i x_i. On the nonempty promise sum_{i=2}^n x_i=0, both equal the promised function f=x_1. The added coefficients have infinity norm one, q has degree one and full-cube margin one, yet sign(q) is majority. At a majority boundary it has (n+1)/2 singleton sensitive blocks, so its approximate degree is at least Omega(sqrt(n)). In particular, this specific sign completion does not have degree polynomial in the constant starting degree.

This example applies to the enlarged basis. It does **not** meet a restriction to perturbing only the original sparsest support: p=x_1 has support one. It also does **not** refute D(f)=poly(Q(f)), since one query solves this promised f and sign(p) is an easy completion. It shows why three claims must stay separate: a particular perturbed sign completion is easy; some completion is easy; and the partial function has no superpolynomial speedup. The fixed-support unrestricted lemma's final decision-complexity implication remains unverified here, rather than declared false.

For Conjecture 72, unrestricted coefficients on a full degree-t basis give an exact representation identity: any degree-t target approximant q equals p+Delta with Delta its coefficient difference. A nontrivial formulation must fix the target completion and state support, norm and margin restrictions. Kernel preservation establishes equality on the promise only. Existence of a different easy completion does not establish that the original sign(p) is easy. The catalogue retains these formulation distinctions rather than claiming a resolution of an unspecified restricted conjecture.

No new primary-source correction of Lemma 71 has been verified. Nis91 and AB25 journal proof comparisons remain inaccessible/uninspected. Independent source-proof audits, optimality of extended exponents, broader domain profiles and the remaining conjecture formulations still require work. No HTML has been started.
