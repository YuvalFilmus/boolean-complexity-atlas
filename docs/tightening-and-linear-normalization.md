# Exponent tightening and original-support normalization

Later developments: see [higher-support and profile audit](higher-support-and-profile-audit.md) for the current sufficient normalization cases, tighter chains and domain-profile inventories.

The original ECCC report by Mika Göös, *Lower Bounds for Clique vs. Independent Set*, TR15-012 (24 January 2015), Proposition 5, p.4, gives `D<=UC1^2`. Complementing the output gives the UC0 version. This original report is now a separate bibliography record; the FOCS DOI is recorded as related publication metadata, not an inspected final version.

The certificate-query proof also yields a repository constant refinement: if k=UC_b, each failed round reduces every surviving certificate’s width, giving `D<=k+(k-1)+...+1=k(k+1)/2`. No optimal leading constant is claimed. The same bound applies to UCmin by choosing the cheaper output side. It lifts to minimum-completion measures by choosing a completion optimal for the right-hand measure.

This improves 22 upper chains in the extended completion inventory. In particular, the previous conservative exponent 6 for D, R and R0 versus either completion_UC0 or completion_UC1 becomes 2. The machine-readable before/after list is `data/completion-exponent-improvements.json`. Direct total-function lower witnesses are now attached to 35 cells, including complement-transferred witnesses for UC0. They retain their logarithmic losses; an exponent match does not mean an attained constant-factor separation.

## Degree-one original-support case

Let p be a bounded degree-at-most-one approximant, with minimal nonzero Fourier support among such approximants under the fixed promise-error convention. Write its coefficient vector as a, including the constant coefficient when nonzero. Then the evaluation matrix on that support has trivial kernel.

Indeed, a linear polynomial has function sup norm exactly `||a||_1`. Suppose a nonzero Delta is in the evaluation kernel. Choose its orientation so `sum_j sign(a_j) Delta_j<=0`. Move along `a+t Delta` until the first coefficient becomes zero. Such a coefficient exists: otherwise all nonzero coordinate changes increase absolute values, contradicting the chosen nonpositive slope. Up to that first zero the l1 norm is affine and nonincreasing. The resulting polynomial remains bounded, has unchanged promised values and no higher degree, but has smaller support. This contradicts minimality.

Consequently the original-support kernel perturbation is necessarily zero in degree one. If p already has the required full-cube margin, use its function bound directly to construct its sign approximant; do not divide by `||Delta||_infinity=0`. If p has no such margin, the hypothesized perturbation cannot supply one in this case.

This argument also covers the degree-optimal, then support-minimal convention when the optimal degree is one: dropping the degree to zero would contradict degree optimality. It does not cover arbitrary nonminimal linear approximants or degree two and above. For example, `(1+x+y-xy)/2` has function sup norm one but coefficient l1 norm two, illustrating the failure of the norm identity beyond the linear case.

The original-support higher-degree lemma remains proof-pending. The polynomial-support repair and the enlarged-basis majority obstruction remain separate records. Neither the existence of some easy completion nor equality on the promise establishes that a fixed off-promise sign completion is easy. Conjecture 72 therefore still needs its target-completion and allowed-perturbation quantifiers fixed before a nontrivial restricted resolution can be claimed.

No further journal access was obtained this round. Nis91 and AB25 proof comparisons remain uninspected. All 506 completion cells have evidence, but extended sharp exponents and most general-domain reverse comparisons remain under audit. No HTML generated.

## Product-domain profile

Certificate querying also gives D<=C^2 and D<=UC^2 on full Cartesian products with symbol-coordinate queries, uniformly over the alphabet. These two profile-specific claims are now indexed. Their proofs use the fact that compatible partial assignments have a common valid extension. This fails for permutations and general multislices, so they are excluded from the common composable-domain closure. The existing forward-only permutation witness rules out extending either comparison uniformly to all such domains.
