# Higher-support normalization and domain-profile audit

Later status: see [unmatched intervals and kernel-line audit](unmatched-and-kernel-line-audit.md), including the general lambda-partite product lift.

Later developments: see [dependent-support and exponent audit](dependent-support-and-exponent-audit.md), including full lower-exponent intervals and the uniform-hypermatching subprofile.

This round tightens another 61 completion upper chains, extends a proved original-support normalization case to arbitrary degree, and generates parameterized comparisons for six domain profiles. None of these changes certifies every exponent as best known.

## Completion upper chains

The extended inventory was not seeding its closure with all previously checked pure core upper chains. It now does so, admitting only chains whose recorded endpoint has no logarithmic loss. Every new path retains its original claim IDs. For example, completion_D versus completion_Q0 improves from exponent 6 to 4 by combining the total-function quartic quantum bound with Q=O(Q0). The same improvement holds for completion_R and completion_R0 versus completion_Q0. Several degree, sensitivity and certificate chains also improve. The 61 before/after records are in `data/completion-core-extension-improvements.json`.

This is a correction to conservative indexing, not a claim of new mathematical bounds. The inventory remains 506/506 covered; lower witnesses, logarithmic losses and lack of best-known certification remain explicit. A logarithmic endpoint is not silently promoted to a pure-power seed.

## Original-support normalization in higher degree

Let p be a support-minimal globally bounded approximant among degree-at-most-d polynomials satisfying the fixed promise-error requirement. If the Fourier coefficient l1 norm of p is at most one, its promise evaluation matrix on its nonzero Fourier support has trivial kernel.

Here is a complete proof. Suppose a nonzero Delta preserves all promised values. Orient it so `sum_S sign(p_hat(S))*Delta_S<=0`. Move in this direction until the first coefficient becomes zero. Such a coefficient must exist: otherwise every nonzero coordinate change would increase its coefficient's absolute value, giving positive slope. Before the first zero no coefficient changes sign, so the coefficient l1 norm is affine and nonincreasing. At the zero the new polynomial is still globally bounded by its coefficient l1 norm, agrees with p on the promise and has no higher degree, but uses fewer characters. This contradicts support minimality.

Thus a nontrivial original-support kernel for such a minimizer requires coefficient l1 norm greater than one. This theorem works in every degree. In particular, if the incidence vectors of the supported nonconstant characters are independent over F2, their values realize every possible sign pattern. The function sup norm then equals the coefficient l1 norm (also with a constant term). Global boundedness implies the needed l1 bound, so the kernel is trivial in this higher-degree case too. Degree one is a special case.

The result concerns the source's bounded, degree-optimal-then-support-minimal setup. It does not assert that all bounded polynomials have l1 norm at most one. Dependent Fourier supports with larger l1 norm remain outside this argument. A trivial kernel means only Delta=0 is available; if p already has a global margin, normalize p by its function bound. If it lacks the margin, that kernel cannot repair it.

A second sufficient condition controls support dependence. If the supported characters span F2-rank r, there are at most 2^r possible characters in their span. Consequently the earlier coefficient repair gives `K<=1+2^r M` and completion approximate degree `O(d*(1+2^r M)/gamma)`. For r=O(log d), polynomial coefficient bound and inverse margin suffice for polynomial overhead. Rank of character incidence vectors and rank of the promise evaluation matrix are different quantities; low polynomial degree does not imply logarithmic character rank.

The unrestricted higher-degree original-support conclusion remains unverified. The fixed-basis statement, enlarged-basis majority obstruction and sufficient function-norm repairs remain distinct records. No primary-source correction was found in the narrow follow-up searches; this does not establish that none exists.

## Domain-profile comparison grids

The new `data/profile-matrices.json` contains six twelve-measure grids: 132 upper chains each for products, permutations, perfect matchings, multislices and slices, and 121 for hypermatchings. Hypermatchings lack the eleven reverse comparisons with sensitivity on the right because the source supplies no witnessing parameter there. The total is 781 parameterized upper chains across 792 ordered profile cells.

Each chain records a symbolic prefactor, its claim IDs and its guards. In particular,

- `K_D=beta^(-2)*max(Delta,n/M)` for D versus bs^4;
- `K_P=max(Delta,n/M)` for D versus C^2;
- `K_C=beta^(-1)` for C versus bs^2;
- `K_S=alpha^(-1)` for degree versus s^2;
- `K_T=6*beta_c^(-1)*alpha^(-2)` for C versus s^5.

The certificate bound was rechecked directly in the final DFLLV26 journal: Lemma 3.3, article pp.19–20, proves `D<=max(Delta,n/M)*C0*C1`, improving to `Delta*C0*C1` when C<=M. The algorithm queries a consistent positive certificate and all queries mentioning its elements; each round discovers a new element of every surviving negative certificate. The global fallback uses D<=n. This supplies a previously unindexed parameterized D-versus-C comparison.

The sensitivity composition uses Lemmas 3.5–3.6 and Theorem 5.3 (article p.31): `C<=beta_c^(-1)*s*bs`, `bs<=6*adeg^2<=6*degree^2`, and `degree<=alpha^(-1)*s^2`. Together they give the displayed C-versus-s^5 bound. Combining with D-versus-C^2 yields a parameterized exponent 10 for D versus sensitivity in the witnessed profiles, including the forward-and-inverse permutation model. These are checked chains, not certified optimal exponents.

For multislices and slices, every use of n/M retains M>0. When the minimum multiplicity is one, the n/M theorem is inapplicable; those conditional cells cannot be read as unconditional bounds. Even when M>0, n/M may grow with n. Balanced profiles keep it bounded; general profiles need their recorded factors. Hypermatching constants can depend on block size. Full-product certificate bounds are profile-specific and do not transfer to other oracles.

## Conjecture formulations

The Conjecture 72 audit now spells out uniform family quantifiers: polynomial overhead must have constants independent of input size and the particular function in the family. A separate constant for every finite function would make the assertion vacuous.

For a fixed completion F and a full permitted Fourier basis, existence of a low-degree approximant q to F is equivalent to existence of an unrestricted perturbation giving q, simply by coefficient subtraction. Moreover, if both p and q are globally bounded by one, every Fourier coefficient has magnitude at most one, and the coefficient difference has infinity norm at most two. That coefficient bound alone adds no restriction to this representation.

Requiring Delta in the promise evaluation kernel is different: it enforces exact equality q=p on the promise, not merely approximation of the same labels. Requiring F=sign(p) off the promise is also different from allowing any completion. Support, degree, margin, exact interpolation and fixed-target quantifiers must therefore be stated before a nontrivial restricted characterization can be assessed. No resolution of an unspecified intended formulation is asserted.

Nis91 and AB25 journal-text comparisons remain uninspected; other conjecture formulations and optimality audits remain unfinished. No HTML has been generated.
