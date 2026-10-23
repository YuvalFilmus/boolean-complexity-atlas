# Typed algorithmic bounds, reductions and problem classes

These statements have parameters or change objects/models; they are not silently entered as scalar function-measure inequalities.

## BK24-search-to-partial-decision

For relation S(x), auxiliary string y indexed by all certificate outputs. Promise all y_c for c in S(x) agree; the decision value is that common bit.

Index an auxiliary bit y_c by every solution certificate c. Promise that all bits y_c for certificates valid on x have the same value, and ask for that value. Polynomial systems transfer via sum_c p_c(x)y_c. In the reverse direction, measure a decision algorithm’s query register on auxiliary input all zero and verify sampled certificates. The quantum hybrid argument gives Q(search)<=tildeO(Q(decision)^3), hence the cube-root lower-bound transfer.

- D(decision)=tildeTheta(D(search))
- R(decision)=tildeTheta(R(search))
- Q(decision)<=O(Q(search))
- Q(decision)>=tildeOmega(Q(search)^(1/3))
- cubeBoundedAdeg(decision)<=O(rel_adeg(search))
- conical(decision)<=O(rel_conical(search))
- CAdv(decision)>=tildeOmega(rel_CAdv(search))
- AdvPlus(decision)>=tildeOmega(rel_Adv(search))

Input length may grow with the number of certificates. Theorem 19 explicitly gives the cube-root quantum lower transfer; the stronger-looking quantum statement printed in Lemma 21 is not used in this catalogue.

Source: [BK24](https://arxiv.org/abs/2410.16245), Definition 18 and Theorem 19; Lemmas 20–22.

## CMP22-tree-rank-depth

Given one correct tree T, Q(S)=O(sqrt(rank(T)*depth(T))).

Identify rank(T) with optimal guessing mistakes and apply the Lin–Lin simulation, or the optimized weighted span-program construction.

Both factors belong to the SAME tree. This does not justify replacing them by separately minimized rank(f) and D(f). Original guessing-algorithm simulation is LL16 Theorems 5.4–5.5; BT20 Theorem 4 generalizes alphabets and uses span programs/adversary SDPs. CMP22 proves the guessing-rank identity.

Source: [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Theorem 4 and Corollary 9(1).

## CMP22-random-tree-rank-depth

Given one randomized tree family T, Q_{2/5}(S)=O(sqrt(rrank(T)*depth(T))).

Sample a support tree, then run a high-success quantum reached-leaf algorithm. Multiply the two pointwise success guarantees.

Depth and worst-support rank belong to the same algorithm. Preserve epsilon=2/5 for general relations.

Source: [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Theorem 5 and Corollary 27.

## BT20-expected-guessing

For a single randomized algorithm computing a function f:D subset [ell]^n -> [m], let T=max_x E[depth on x], G=max_x E[red mistakes on x]. Then Q(f)=O(sqrt(TG)).

Construct a feasible dual adversary solution from the colored query algorithm; average its contributions over the classical random choices. Nonbinary span programs provide the deterministic counterpart.

The bounds are expectations for the SAME algorithm and a single-valued function. Do not replace them by independently optimal measures or import them as a general multivalued-relation amplification theorem.

Source: [BT20](https://doi.org/10.22331/q-2020-03-02-241), Theorem 4(ii).

## completion-optimal-cross-evaluation

If a fixed set of measures is uniformly polynomially equivalent on total functions, then their evaluations on any completions optimizing any measure in that set remain uniformly polynomially equivalent.

Compare M_i(F_k) to M_k(F_k), use optimality to compare with M_k(F_l), and apply total-function polynomial bounds again.

The completions must optimize a member of the stated set; this is not a claim about arbitrary completions. Uniform families and constants are required.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Lemma 48.

## completion-speedup-equivalence

For a family of partial functions and a measure M uniformly polynomially equivalent to D on total functions: D(f) and native M(f) are polynomially equivalent iff minimum-completion M(f) and native M(f) are polynomially equivalent.

Observation 49 gives minimum-completion D=D; Observation 47 relates minimum-completion M to minimum-completion D. Substitute this equivalence on either side.

This is a conditional family-level equivalence, not an unconditional bound D<=poly(native M) for partial functions.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Lemma 50.

## completion-domain-indicator

If p is a globally [0,1]-bounded degree-d approximant to f on its promise and membership in the promise has a q-query Boolean algorithm, the zero-outside completion admits approximate degree O(d+q), with constants depending on the fixed error margins.

Construct a globally bounded constant-error acceptance polynomial a for the domain indicator. Multiply p*a. On the promise its error is at most epsilon+epsilon_prime; outside it is at most epsilon_prime. Degree is additive.

The source states poly(d,q); its displayed product proof gives O(d+q) for fixed margins. Global boundedness of p is essential. An off-promise unbounded approximant cannot be substituted.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Lemma 51.

## completion-slice-degree

For a function defined on the entire k-slice, a total completion has degree O(cubeBoundedAdeg(f)^2*bs(f)^4). In particular D(f)=O(Q(f)^10).

For a sufficiently balanced slice use the existing slice decision-tree theorem. Otherwise use the low-weight-domain certificate-query construction (Lemma 55); substitute k=O(bs^2).

Domain is the entire slice, not an arbitrary subpromise inside it. Approximation is globally bounded. The native partial-function degree convention is not interchangeable.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Theorem 56.

## domain-D-bs-parameters

D(f)<=beta^(-2)*max(Delta,n/M)*bs(f)^4.

Generalize the certificate-query procedure: shortening blocks gives small certificates, and query conflicts bound the number of certificate stages.

Require M>0. If C<=M, or bs<=sqrt(beta*M), or approx_degree<=(beta*M/36)^(1/4), the source strengthens the prefactor to beta^(-2)*Delta. Parameter assumptions are explicit, not a uniform bs^4 theorem.

Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Theorem 3.1.

## domain-certificate-sensitivity

C(f)<=min(beta_c^(-1)*s(f)*bs(f),beta^(-1)*bs(f)^2).

Choose maximal disjoint opposite-output changes and shorten them using the domain sensitivity ratios; their union is a certificate.

The parameters beta and beta_c belong to the query domain; they are not functions of f.

Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Lemma 3.5.

## domain-witnessing-sensitivity

degree(f)<=s(f)^2/alpha for an alpha-witnessing domain.

A nonzero top-degree pseudo-character coefficient yields an induced Boolean cube of dimension at least alpha*degree; Huang gives the square-root sensitivity lower bound.

Alpha-witnessing is an additional representation-theoretic property. It is not implied by composability alone.

Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Theorem 5.3.

## natural-completion-Lipschitz

For a fixed globally bounded approximant p of degree d, a positive margin gamma on the entire cube gives approximate degree of sign(p) at most O(d/gamma) at fixed error. In HKMP26 Lemma 60 gamma=d^(-c), giving O(d^(c+1)).

If every off-promise point is within r of a promised point and |p(x)-p(y)|<=L*r with L*r<=2/3-gamma, reverse triangle inequality gives the margin. Compose p with a univariate sign approximant.

The completion is fixed by p, with sign(0)=+1. Require 0<gamma<=2/3 and global boundedness. Constant or total-domain boundary cases are separate. This is not a statement for an arbitrary unbounded promise approximant.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Lemma 60 and Definition 59.

## natural-completion-influence

HKMP26 Lemma 63: if an optimal-degree globally bounded approximant p has max_i sqrt(spar_i(p)*Inf_i(p)) <= eta(f,c)/2, its sign completion has approximate degree O(d^(c+1)).

Cauchy–Schwarz gives ||D_i p||_infinity<=sqrt(spar_i(p)*Inf_i(p)); convert to a Hamming Lipschitz bound and apply the margin construction.

Here eta=(2/3-d^(-c))/r_C(Dom f), with positive numerator and nonzero covering radius. p is fixed on the full cube; a partial function has no unique Fourier expansion.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Lemma 63.

## exact-degree-completion-Mobius

A Boolean completion F has degree <=d iff its 1-inputs supported inside each S with |S|>d have equal even- and odd-weight counts.

The parity difference is exactly the high-degree multilinear coefficient up to sign by Mobius inversion. All coefficients above d vanish iff degree<=d.

The source writes degree=d using minimality of the starting exact degree to force the reverse inequality; without that premise the conclusion is only <=d.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Lemma 67.

## perturbation-Lemma71-audit

The source claims polynomial-cost completion from a domain-preserving Fourier coefficient perturbation with polynomial coefficient infinity norm and a full-cube inverse-polynomial margin.

It rescales p_Delta by M=||Delta||_infinity and applies a sign approximant. The displayed assertion |p_Delta(x)|/M<=2 is not justified by a bound on individual Fourier coefficients. Generally ||p_Delta||_infinity<=||p||_infinity+||Delta||_1<=1+s*||Delta||_infinity, introducing the support size s.

Statement/proof pending. This identifies an unsupported proof step, not a counterexample to the final lemma. A sufficient repair is a polynomial bound on the FUNCTION sup norm relative to the margin; bounded coefficient infinity norm alone is not that bound. Kernel preservation holds only on the promised domain. Further issues to keep explicit: M may be zero; a polynomial degree of an arbitrary chosen approximant is not automatically polynomial in native approximate degree. The sparse-coefficient sufficient repair addresses these with explicit hypotheses.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Lemma 71, pp.33–34.

## distributional-simulation-equivalence

For fixed p,q in (0,1), polynomial-overhead classical average-L1 simulation of quantum acceptance probabilities under product bias p is equivalent to simulation under the uniform q-density slice, and hence the uniform cube.

A short biased-input gadget simulates another bias; compose and coherently uncompute the gadget. Product/slice couplings, padding and quantum hybrid bounds control average error; fixing simulator randomness gives deterministic trees.

A theorem equating conjectures, not a proof of simulation. Overheads depend on the biases; the theorem must not be specialized to arbitrarily vanishing bias without tracking those factors. Average L1 error is related to high-probability error by Markov and the bounded range.

Source: [GMNR26](https://arxiv.org/abs/2609.35327), Theorem 3.3; Propositions 3.6 and 3.10.

## distributional-influence-equivalence

For fixed p,q in (0,1), the bounded-polynomial influential-coordinate criterion AA(mu_p) is equivalent to AA(nu_q).

Use the bias-conversion gadget and transfer variance/influence inequalities. Compare product and slice expectations for bounded low-degree polynomials and reduce each criterion to the other.

The slice influence is distribution-specific; it is not the disjoint-transposition sensitivity in the general-domain catalogue. This equivalence does not resolve the conjecture or establish HKMP26 Conjecture 78.

Source: [GMNR26](https://arxiv.org/abs/2609.35327), Theorem 4.3; Corollary 4.8 and Proposition 4.12.

## influence-normalization-and-slice-comparison

Under uniform measure, AA14/GMNR26 flip influence equals 4 times the HKMP26 E[(D_i p)^2] normalization. On the uniform slice, swInf_(i,j)<=2*(Inf_i+Inf_j)<=4*max_i Inf_i.

The derivative normalization divides a flip difference by two. For a swap, insert the common intermediate off-slice neighbor and apply (a+b)^2<=2a^2+2b^2; swap invariance preserves the slice expectation.

Bit flips can leave the slice. Changing off-slice values can change flip influence while preserving all slice values and swap influences. The new distributional equivalences use full-cube bounded polynomials, not arbitrary intrinsic slice extensions.

Source: [GMNR26](https://arxiv.org/abs/2609.35327), Definition 2.5 and Lemma 2.6; AA14 before Conjecture 1.7; HKMP26 Definitions 21–22.

## perturbation-function-norm-repair

If q is a degree-d polynomial with gamma<=|q(x)|<=K on the entire cube, and sign(q) agrees with f on its promise, its sign completion has bounded approximate degree O(d*K/gamma) at fixed error.

Normalize by the FUNCTION bound K, then compose q/K with a univariate sign approximant on [-1,-gamma/K] union [gamma/K,1]. The degree multiplies by O(K/gamma), and the sign agrees with f on the promise.

This is a repository sufficient condition, not a correction asserted by the authors. A coefficient bound gives only K<=||p||_infinity+||Delta||_1, so support dependence cannot be discarded without another argument.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Repository sufficient-condition repair of Lemma 71, using Lemma 27.

## biased-natural-completion

Let beta=max(sqrt(p/(1-p)),sqrt((1-p)/p)), sigma=2*sqrt(p*(1-p)), and K=sum_{l=0}^{d-1} binom(n-1,l)*beta^(2l). If a degree-optimal bounded approximant has max_i sqrt(biasedCoordInfluence_i)<=sigma*eta/(2*sqrt(K)), its sign completion has approximate degree O(d^(c+1)).

In the biased orthonormal expansion, flipping coordinate i changes its basis factor by 2/sigma. Cauchy–Schwarz bounds the sum by sqrt(influence)*sqrt(K), yielding the Lipschitz bound eta; apply the global-margin sign construction.

The influence here is the coefficient-squared normalization, not unscaled E_p[(D_i f)^2]. All n,d,p factors remain explicit. eta=(2/3-d^(-c))/r_C(Dom f), with positive numerator and nonzero radius.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Lemma 66, pp.29–30.

## BD16-union-of-multislices

For fixed alphabet size M and a coordinate-permutation-invariant promise X subseteq [M]^n, R(f)=O(Q(f)^(18*(M-1))). The function itself need not be permutation-invariant.

Control how the function behaves inside each orbit, then organize the orbits by their multiplicities. Distinguishing nearby orbit types is reduced to permutation inversion or counting and bounded using adversary arguments.

The promise can be a union of multislices. M is a fixed alphabet parameter; this is not one universal exponent for growing M. Deterministic cost need not replace randomized cost for unions.

Source: [BD16](https://doi.org/10.4230/LIPIcs.TQC.2016.7), Theorem 6.

## perturbation-sparse-coefficient-repair

Let p be full-cube bounded by 1, of degree at most d. Let q=p+sum_S Delta_S chi_S have degree at most d, s perturbed Fourier coordinates, coefficient bound M=max_S |Delta_S|, full-cube margin gamma>0, and correct sign on the promise. Then the sign completion has bounded approximate degree O(d*(1+s*M)/gamma) at fixed error.

Each character has absolute value one, so |q|<=1+sum_S |Delta_S|<=1+s*M. Normalize by K=1+s*M and compose with the sign approximant of Lemma 27. The margin becomes gamma/K and degrees multiply. This also handles M=0 without division by zero. If s,M,1/gamma are polynomial in d, completion approximate degree is polynomial in d.

A sufficient repair, not an author correction. To conclude D(f)=poly(Q(f)), additionally require d polynomially bounded in the native approximate degree (hence in Q). Restrict a total completion decision tree to the promise and use the total-function D versus approximate-degree bound. No bound on s polynomial in d follows just from low degree: s can be sum_{j<=d} binomial(n,j). The kernel condition alone preserves only promised values.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Repository sufficient-condition derivation from Lemma 27; audit of Lemma 71.

## expanded-basis-majority-normalization-obstruction

For odd n>=3, p=x_1 and q=sum_{i=1}^n x_i have degree 1. On the nonempty promise sum_{i=2}^n x_i=0, both equal f=x_1. The added coefficient perturbation has infinity norm 1 and q has full-cube margin 1, yet sign(q) has unbounded approximate degree as n grows.

All n signs sum to an odd integer, so |q|>=1 and ||q||_infinity=n. On the promise the added even-coordinate sum is zero. At a majority boundary, (n+1)/2 singleton flips change the output, so block sensitivity is at least (n+1)/2; the total-function approximate-degree lower bound gives Omega(sqrt(n)). Thus polynomial degree, coefficient norm and inverse margin alone do not force the particular sign completion to have polynomial approximate degree in d.

This uses the enlarged degree-one basis discussed after Lemma 71. It does not obey the lemma’s original restriction to perturbing only the sparsest approximant’s existing support: p=x_1 has support one. Nor does it refute D(f)=poly(Q(f)): on this promise f is computable with one query, and sign(p)=x_1 is an easy completion. It rigorously separates the sign-completion inference from the decision-complexity conclusion and from the fixed-support setting.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Repository example for the enlarged-basis discussion after Lemma 71.

## linear-minimal-support-kernel-trivial

Let p=a_empty+sum_i a_i x_i be full-cube bounded by one and support-minimal among bounded degree-at-most-one approximants to f with the fixed promise-error convention. On its nonzero Fourier support S, the evaluation matrix A_D(p) has trivial kernel.

For linear p, ||p||_infinity=|a_empty|+sum_i |a_i|. If nonzero Delta lies in the evaluation kernel, orient it so sum_{j in S} sign(a_j) Delta_j<=0. Before the first coefficient reaches zero, the l1 norm changes linearly with that nonpositive slope. At the first zero the polynomial remains bounded, has identical promised values and degree at most one, but smaller support: contradiction. Such a zero exists because some oriented coefficient moves toward zero; otherwise every sign(a_j)Delta_j would be nonnegative and at least one positive.

Also applies when degree one is the optimal exact degree of the starting approximation problem; dropping to degree zero would contradict that optimality. Delta=0 must be treated without dividing by its norm. If p itself has full-cube positive margin, normalize by its function bound and apply sign approximation. This resolves the kernel issue for degree one, not for degree>=2. For higher degree the Fourier l1 norm need not equal the function sup norm, so this proof does not extend automatically.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Repository degree-one special case of the original-support setting of Definitions 68–69/Lemma 71.

## minimal-support-l1-kernel-trivial

If a support-minimal bounded degree-at-most-d approximant p has Fourier coefficient l1 norm at most one, its domain evaluation matrix on its nonzero support has trivial kernel. In particular this holds in any degree when the nonconstant Fourier characters in its support have F2-linearly independent incidence vectors.

A nonzero domain-kernel vector can be oriented to make the directional l1 slope nonpositive. Move to the first coefficient zero; up to that point signs stay fixed and l1 does not increase. The resulting polynomial stays globally bounded by its coefficient l1 norm, preserves all promised values and has no higher degree, but smaller support. This contradicts support minimality. For F2-independent character supports, every sign pattern of character values is attained on the cube; hence the function sup norm equals the coefficient l1 norm, including an optional constant term.

This extends the degree-one argument without assuming degree one. Support minimality is essential. It gives a sufficient original-support case, not a solution when coefficient l1 norm exceeds one and Fourier supports have dependencies. A necessary condition for a nontrivial kernel in the support-minimal bounded setting is therefore l1 norm>1. A positive full-cube margin with Delta=0 is handled by normalizing the function bound, never by dividing by zero.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Repository arbitrary-degree sufficient condition for Definition 68 and Lemma 71.

## fourier-closure-support-repair

If the supported nonconstant Fourier characters span F2-rank r, then at most 2^r distinct Fourier characters occur. Thus the coefficient repair has K<=1+2^r M, and approximate completion degree O(d*(1+2^r M)/gamma). In particular r=O(log d) suffices for polynomial overhead when M and 1/gamma are polynomial in d.

All characters in the support belong to the F2-span of r incidence vectors, which has exactly 2^r elements including zero. Sum their absolute coefficient perturbations to bound the function norm, then apply the indexed function-norm sign-approximation argument.

This is a sufficient condition. A degree bound d does not itself bound r by O(log d), and support rank is distinct from the rank of the promise evaluation matrix. No necessity or full characterization is asserted.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Repository character-rank sufficient condition for normalization repair.

## kernel-amplification-duality

For supported characters S, promise evaluation matrix A and full-cube evaluation vector v_x, define kappa=max_x max_{A Delta=0, ||Delta||_infinity<=1}|v_x^T Delta|. Then kappa=max_x min_y ||v_x-A^T y||_1. If ||p||_infinity<=1 and ||Delta||_infinity<=M, the perturbed function is bounded by 1+kappa*M.

The kernel-box feasible set is symmetric, so maximizing the absolute linear functional equals maximizing the positive functional. The LP dual of max{v_x^T Delta:A Delta=0,-1<=Delta<=1} minimizes ||v_x-A^T y||_1. Finite feasible bounded LP strong duality gives equality. Scale an actual kernel perturbation by M and apply the triangle inequality; M=0 is immediate. With margin gamma, sign composition gives degree O(d*(1+kappa*M)/gamma).

kappa is a repository diagnostic, not a source-introduced complexity measure or a claimed polynomial bound. It obeys 0<=kappa<=|S| and kappa=0 iff ker A is trivial, since full-cube characters are linearly independent. The source assumptions do not presently give a verified polynomial bound on kappa for dependent supports. This isolates the missing normalization control without asserting the unrestricted lemma false. The kappa<=|S| bound assumes the uniform Walsh characters with values +/-1; it is not asserted unchanged for an unbounded biased orthonormal basis. A large kappa alone does not refute the lemma’s existential or query-complexity conclusion.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Repository diagnostic for fixed-support Lemma 71; finite LP duality.

## support-elimination-boundary-obstruction

For a support-minimal bounded approximant, any nonzero domain-kernel direction with finite first coefficient-zero time t_zero has maximal feasible segment endpoint t_feas<t_zero, where feasibility means |p+t h|<=1 on the full cube.

The feasible t interval is determined exactly by all inequalities -1<=p(x)+t h(x)<=1. Its upper endpoint is the minimum of (1-p(x))/h(x) for h(x)>0 and (-1-p(x))/h(x) for h(x)<0. If t_zero were in that feasible interval, promised values and degree would be preserved while a supported coefficient vanished, contradicting minimality. Immediate infeasibility at an already saturated point gives t_feas=0.

A necessary obstruction, not a sufficient test of global support minimality. Directions need not have a finite coefficient-zero time in both orientations; the statement concerns orientations with finite such time. Hitting a boundary is not by itself proof that the segment cannot continue (a zero directional value there is irrelevant). The feasible interval must be used. No deduction that all dependent-support kernels vanish is made.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Repository necessary condition for bounded support minimality.

## permutation-product-witnessing

For a finite product of permutation domains with forward and inverse coordinate queries, the product spatial-degree filtration is 1/2-witnessing for disjoint-transposition sensitivity.

Each coordinate indicator monomial factors across permutation components, so V_d(product)=sum_{sum d_i<=d} tensor_i V_{d_i}. The source irreducible decomposition assigns each permutation isotypic component a degree depth and supplies pure-degree pseudo-characters spanning it. Products of those pseudo-characters span the product graded components. A product of degree depths summing to d induces a cube whose dimension is the sum of the factor dimensions, at least d/2. Neighbor changes from separate factors have disjoint supports. A Boolean function with nonzero top graded component correlates with one such product; source Lemma 5.2 then yields s>=sqrt(d/2). Fresh 23 October audit rechecks the homogeneous decomposition and uses output-value transpositions in B columns; the printed input/A-column orientation fails, with an explicit S_3 counterexample.

Uses the source permutation isotypic grading, not an unproved plethysm assertion for hypermatchings. Cube dimensions add and the parity signs multiply. This is a repository tensor argument, not a claim that the source explicitly states the product lemma.

Source: [DFLLV26](https://doi.org/10.5070/C6.68665), Repository tensor-product lemma from Theorem 5.5 and Section 5.3.

## quantitative-kernel-line-slab-avoidance

Let h be a nonzero polynomial from a fixed-support domain-kernel vector u. Fix gamma>0. Suppose |p(x)|>=gamma whenever h(x)=0. Choose representatives I of distinct nonconstant affine pairs (p(x),h(x)), h(x)!=0, and S=sum_{x in I} 1/|h(x)|. For any R>gamma*S there is t in [-R,R] with |p(x)+t*h(x)|>=gamma everywhere. If ||p||_infinity<=1, the resulting sign completion has approximate degree O(d*(1+R*||h||_infinity)/gamma).

For each representative, the forbidden t interval |p(x)+t*h(x)|<gamma has length 2gamma/|h(x)|. Their total length is at most 2gamma*S<2R, so they cannot cover [-R,R]. Zero-slope constraints are safe by hypothesis. Choose an uncovered t, use ||p+t h||_infinity<=1+R||h||_infinity and compose a sign approximant. The coefficient displacement obeys ||Delta||_infinity<=R||u||_infinity. Exact promise values remain unchanged because u is in the domain kernel.

A sufficient quantitative condition in one chosen kernel direction, not a uniform polynomial bound implied by support minimality. The number of distinct constraints and small nonzero |h(x)| may force enormous R. This distinguishes the source qualitative finite-slab escape lemma from the polynomial-radius requirement. The degree d must be controlled by the native approximate degree for a D-versus-Q conclusion.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Repository bounded-radius refinement of Lemma 70.

## qualitative-slabs-no-polynomial-radius

Qualitative avoidance of finitely many slabs does not by itself bound the required radius: already the one-dimensional slab |epsilon*t|<=gamma requires |t|>gamma/epsilon to escape.

The slab is exactly [-gamma/epsilon,gamma/epsilon] when epsilon>0. The ratio can be arbitrarily large independently of the number or dimension of the slabs.

An elementary obstruction to an inference, not a counterexample satisfying all original-support/minimality hypotheses of Lemma 71. No failure of the lemma’s final existential decision-complexity implication is claimed.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Repository audit of Lemma 70 versus Lemma 71 hypotheses.

## verification-fractional-sharp-constants

Under expected-cost, rejecting-error-1/2 verification, FC/2<=RC<=(ln 2)*FC. The lower coefficient 1/2 is attained by a single bit. The upper coefficient ln 2 is asymptotically necessary over partial functions, using the promise {0^N} union {x:|x|=k}, with k->infinity and N=k^3.

For the upper bound independently query i with probability 1-2^(-w_i) from a fractional certificate. Missing disagreement probability is at most 1/2, and expected cost is at most (ln 2)FC. The lower bound uses query probabilities on the claimed input: twice those probabilities form a fractional certificate. For sharpness on the zero-or-weight-k promise, FC=N/k at zero and FC=1 at positive inputs. A verifier on zero has a random query set of size T; averaging a positive uniform k-subset gives miss probability g(T)=binom(N-T,k)/binom(N,k). Its piecewise-linear extension is convex, since the second finite differences are nonnegative, so Jensen and miss probability<=1/2 imply expected T at least the interpolated half-threshold. Uniform random query sets of the two adjacent sizes attain it. That threshold is (ln 2+o(1))*N/k when N=k^3. Positive claims cost at most 1/2 by querying one known 1 with probability 1/2.

Constants are specific to the stored expected-query verification convention. This is a repository argument, not a printed sharp-constant theorem attributed to the source. The partial-promise sharpness does not establish sharpness of the upper coefficient on total functions or minimum completions. The linear upper inequalities themselves lift to minimum completions by choosing the right-hand minimizing completion.

Source: [Aar02](https://arxiv.org/abs/quant-ph/0210020), Repository refinement of Definition 3/Lemma 5 sampling characterization.

## minimal-support-bounded-interpolation-vertex

On the support S of a support-minimal bounded degree-at-most-d approximant p, the bounded exact-interpolation polytope P={a:A_D a=A_D a_p, |H a|<=1} is compact. Every vertex retains all S coordinates nonzero, and its active constraint matrix [A_D; H_T] has full column rank, where H_T are the saturated full-cube evaluations.

H is the full-cube evaluation matrix of distinct supported characters. Bounded function values bound every Fourier coefficient by one, so P is a compact nonempty polytope. A zero coefficient at any feasible point would produce a smaller-support bounded approximant with identical promised values and no higher degree, contradicting minimality. At a vertex, if the stacked domain and active-cube rows had a common nonzero null vector, sufficiently small positive and negative movements along it would preserve equality and all cube bounds; that would contradict extremality. Thus the stacked matrix has full column rank.

This supplies only an augmented rank certificate, not a proof that A_D alone has full rank or that its kernel amplification is polynomially bounded. It explains the role of saturated off-promise constraints. It is not a constructed support-minimal counterexample to the unrestricted lemma. If p is degree-optimal and then support-minimal, a lower-degree feasible point would itself contradict optimality, so the same argument applies.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Repository polyhedral analysis of fixed-support Definition 68/Lemma 71.

## Aaronson-R0-RC-ndeg-logn-corrected-proof

For total n-bit f, R0(f)=O(RC(f)*ndeg(f)*log(2+n)), with expected classical query costs and the source one-sided nondeterministic polynomial degree.

At each restriction choose a consistent zero input and query its randomized certificate. Every maxonomial of a nondeterministic representative contains a block whose flip changes that zero input to a one input. Coupling forces the verifier to hit that block with probability at least one half. The shrinking-monomial potential of Lemma 9 bounds the expected number of rounds by O(ndeg(f) log(2+n)); each round costs O(RC(f)) in expectation. Stop when the restricted function is constant.

Use the later proof, not the old auxiliary assertion that resetting a sampled coordinate set toward a zero input makes every other input zero with probability at least one half. The source expressly calls a previous claim false and superfluous, without identifying that claim in the correction footnote; the reset assertion is isolated here by direct comparison. Retain n and the mixed product. Minimizing the factors over unrelated completions is invalid. Does not produce a new parameter-free completion exponent.

Source: [Aar02](https://arxiv.org/abs/quant-ph/0210020), Later 12-page author manuscript, Theorem 10 pp. 6–7, footnote 3 p. 6; old preprint pp. 5–6.

## Tal-fbs-bs-sensitivity-fractional-packing-constant

For every nonconstant total Boolean function, fbs(f)<=bs(f)*(s(f)-1+1/s(f)). The constant function case has all three measures zero and is handled separately.

At a fixed input x retain the inclusion-minimal sensitive blocks. Their fractional matching number is fbs_x and integral matching number is bs_x. Every block B has size at most s(f), because at x^B each coordinate in B is sensitive by minimality. Pad shorter edges with fresh private vertices to uniform size s(f); neither matching optimum changes. Apply the uniform-hypergraph fractional matching bound nu*<=(s-1+1/s)nu and maximize over x. Tal prints the resulting Boolean-function inequality.

Tal cites Chan–Lau for the packing bound; the later Chan–Lau journal-layout manuscript explicitly credits the older unweighted theorem to Zoltán Füredi, Maximum degree and fractional matchings in uniform hypergraphs, Combinatorica 1(2):155–162 (1981), and the weighted extension to Füredi, Kahn and Seymour, On the fractional matching polytope of a hypergraph, Combinatorica 13(2):167–180 (1993). Those older original texts have not been inspected here. This improves the mixed-product constant, not a recorded single-parameter exponent. Do not minimize bs and s separately across completions. Projective-plane sharpness at a single input does not establish global Boolean-function sharpness.

Source: [Tal13](https://eccc.weizmann.ac.il/report/2012/163/), Original ECCC TR12-163, Section 5.1.2 pp. 13–14; CL12 introduction and related work pp. 2–5.

## fractional-bs-quadratic-subtractive-completion

Put g(0)=0 and g(b)=b^2-b+1 for integers b>=1. For total f, fbs(f)=FC(f)<=g(bs(f)); for arbitrary partial f, completion_fbs(f)=completion_FC(f)<=g(completion_bs(f)).

For nonconstant total f, 1<=s<=b=bs and t-1+1/t is increasing on [1,infinity), so the original mixed packing bound gives fbs<=b*(b-1+1/b)=b^2-b+1. Fractional packing/covering LP duality gives FC=fbs. For completions choose a single total extension F minimizing bs. Minimum fbs is at most fbs(F), and apply the total bound to F. When b=0, this extension is constant and both minima are zero.

This retains lower-order terms beyond the quadratic upper exponent. It does not change the count of matching completion exponents. Separate minima are never multiplied. A separate agent checked the original Tal statement as well as the deduction; this is not an independent proof audit of the earlier hypergraph theorem. No optimality or novelty claim.

Source: [Tal13](https://eccc.weizmann.ac.il/report/2012/163/), Repository consequence of original Section 5.1.2 and LP duality; minimum-completion lifting.

## hypermatching-degree-comparison

For every real f on full lambda-partite hypermatchings, 2degree_H(f)<=degree_Z(f composed with pi)<=k degree_H(f); the same inequalities hold for epsilon-approximate degree on the two native domains.

Uniform representation fibers have n! product_i(lambda_i!)^n elements. An entry monomial of degree t specifies t distinct vertices. Mobius inversion on touched group labels expresses its fiber average by products of containment indicators J_U; singleton U factors equal one and each remaining factor consumes at least two vertices. This yields degree<=floor(t/2). Pulling back each hyperedge indicator costs degree at most k. Conditional averaging preserves uniform approximation error.

The averaging/degree comparison is a repository derivation, not a printed theorem attributed to DFLLV26. The purely algebraic comparison holds for real f; the sensitivity consequence requires Boolean f.

Source: [DFLLV26](https://doi.org/10.5070/C6.68665), Repository uniform-fiber averaging and partition-lattice derivation; separate full proof.

## rooted-path-nonadaptive-approximation

For [0,1]-valued rooted-path polynomials in the stated support class, at most d*ceil(2d/(delta*epsilon^2)) original nonadaptive queries give additive error epsilon with uniform-input failure probability at most delta; the self-contained version uses 3d in the ceiling.

Keep the m largest nonconstant Fourier terms and query their native supports. Squared tail energy is at most A^2/(4m), at most 2d/m by sharp Khintchine or 3d/m by the fourth moment. Parseval and Markov give the error; clipping preserves the estimate.

Derived repository corollary; Sz76 supplies only the sharp Khintchine input, not the tree/query theorem. Fourier representation available; no efficient recovery algorithm, promise extension or arbitrary-distribution claim.

Source: [Sz76](https://doi.org/10.4064/sm-58-2-197-208), Derived proof, docs/rooted-paths-proof.md, nonadaptive approximation and sharp Khintchine variant.

## quadratic-character-nonadaptive-approximation

For [0,1]-valued polynomials in the invertibly quadratic-character support class with original support size at most d, d*ceil(8/(3 delta^2 epsilon^4)) representation-available nonadaptive native queries suffice for uniform-input epsilon approximation with failure probability at most delta.

Symmetric mixed-norm Holder yields 2sum|a|^(4/3)<=R^(4/3), and moment polarization gives R<=2sqrt(3)W. Keeping m largest coefficients leaves squared error at most sqrt(8/3)W^2/sqrt(m). Parseval, Markov and clipping give the error guarantee; evaluate each selected monomial using at most d original queries.

This classical coefficient consequence is separate from the stronger weighted-cut influence bound. AL25 supplies analytic context; the native query consequence is a derived repository result. No coefficient recovery or nonuniform-distribution claim.

Source: [AL25](https://doi.org/10.1007/s00208-025-03257-9), Derived mixed-norm calculation in docs/graphic-influence-proof.md; not a query theorem quoted from AL25.

## query_TFZPP

Total relations with polylogarithmic certificate verification and a polylog-depth randomized decision tree that returns only valid answers or bottom, succeeding with probability at least 2/3 on each input.

Rfail=polylog(n) and efficient certificate verification; equivalently expected zero-error cost polylog(n) after independent repetition.

Class membership also includes the verification restriction; small R0 alone does not place an arbitrary relation in query-TFNP. Theorem 23 uses explicit 3-XOR instances to separate this class from PLSdt and PPPdt via SoS lower bounds. No scalar query exponent is inferred from these reduction-class separations.

Source: [ZPP26](https://doi.org/10.4230/LIPIcs.ITCS.2026.60), Definition 14.

