# Unmatched completion intervals, kernel lines and lambda-partite sensitivity

Later status: see [independent audit and quantum endpoints](independent-audit-and-quantum-endpoints.md), including the corrected simulation invariant and improved lift coefficient.

The completion inventory remains 506 ordered directions: 442 finite intervals and 64 directions excluding every finite power. After this round, 266 finite intervals have matching recorded exponents and 176 remain unmatched. Unmatched means a gap in this catalogue's recorded interval, not a certified open problem. `data/completion-unmatched-queue.json` ranks these intervals and retains their witnesses and upper-bound paths.

## Tightening the recorded intervals

A directed extraction of FC=Theta(RC) was missing. It improves nine pure upper bounds, including fractional-certificate/packing and quantum-certificate comparisons with RC and its upper simulators. For example, completion_FC versus completion_RC changes from exponent two to one, and completion_QC versus completion_RC becomes exponent one half.

Ten recorded lower bounds improve by transferring a witness first to C and then to either prescribed output side. If X<=O(C^u) and a witness has X>=Y^ell, it gives C>=Y^(ell/u). When Y is complement invariant, choose an infinite subsequence with a fixed large side of C=max(C0,C1), and complement if needed. This supplies side-specific witnesses without asserting the original numerator is itself invariant or silently complementing oriented R1. AIK26's actual C0-versus-R1 lower bound was also checked directly through Lemma 3.4, Theorem 2.2 and the definition of the underlying DNF.

Two more upper directions improve from a pure cubic bound to a quadratic-log bound: completion_Q0 and completion_R1 versus completion_R. KT13 Theorem 5.3 explicitly gives R0=O(R^2 log(2+R)); compose with Q0=O(R0) or R1=O(R0). The original theorem and proof were revisited. The extended closure now retains logarithmic powers separately: composing x^a log(2+x)^b with x^c log(2+x)^d gives powers ac and ad+b. The pure cubic alternative remains recorded. No pure quadratic endpoint is claimed. This also yields a matching infimum exponent for R1 versus R with the lower witness's losses still retained.

The result is 266 matching recorded exponent intervals, not 266 independently discovered or globally certified optimal comparisons. Existing core lower evidence and exact logarithmic exponent expressions are retained.

## Verification constants

Under the stored expected-query verification convention (accept the claimed input certainly; reject every opposite-output input with probability at least one half), the directed fractional comparisons can be made explicit:

`FC/2 <= RC <= (ln 2)*FC`.

For the first inequality, let q_i be the probability of querying coordinate i on the claimed input. Coupling to an opposite-output input forces a query to their disagreement set with probability at least one half. Thus weights 2q_i are a fractional certificate and their total is at most twice the expected cost.

For the second, fix a fractional certificate w. Independently query i with probability `1-2^(-w_i)`, rejecting on disagreement. For any opposite-output input, the probability of missing every disagreement is `2^(-sum_disagreement w_i)<=1/2`. The expected cost is at most `(ln 2)*sum_i w_i`. The verifier always accepts its claimed input.

The coefficient one half is attained by a single bit queried with probability one half. The coefficient ln 2 is asymptotically necessary over partial functions: take the promise consisting of zero and all weight-k inputs in N=k^3 bits. At zero, FC=N/k; at each positive input FC=1. For a verifier at zero, let T be the size of its random query set along that input. Averaging over a uniform weight-k opposite input gives miss probability `g(T)=binom(N-T,k)/binom(N,k)`. The piecewise-linear extension of g is convex by its nonnegative second finite differences, so Jensen's inequality bounds expected T below by the interpolated half-threshold. Querying uniform subsets of the two adjacent sizes attains that threshold. It is `(ln 2+o(1))*N/k`. Positive claims cost at most one half by sampling a known positive bit.

These constants are repository refinements of the source verification/LP characterizations, not quoted source constants or a priority claim. The partial-promise sharpness does not establish optimality of ln 2 on total functions or on minimum-completion measures. The inequalities themselves do lift to minimum completions.

## Quantitative slab avoidance in a kernel direction

The source's Lemma 70 is qualitative: finitely many nontrivial slabs do not cover an unbounded vector space. It explicitly distinguishes arbitrarily stretching a direction from obtaining a polynomial-radius perturbation. It must not be read as proving such a radius.

Here is a bounded-radius sufficient condition. Let u be a fixed original-support domain-kernel vector and h its Fourier polynomial, so h=0 on the promise. Fix gamma>0 and suppose `|p(x)|>=gamma` at every cube point where h(x)=0. Take one representative for each distinct affine pair `(p(x),h(x))` with nonzero second coordinate, and put

`S = sum_representatives 1/|h(x)|`.

For every `R>gamma*S`, there exists t in [-R,R] with `|p(x)+t*h(x)|>=gamma` on the entire cube. Each forbidden interval `|p(x)+t*h(x)|<gamma` has length `2gamma/|h(x)|`; their total length is smaller than 2R, so they cannot cover the whole parameter interval. Zero-slope constraints are safe by assumption. The coefficient displacement is bounded by `R*||u||_infinity`, and the function norm by `1+R*||h||_infinity`. Sign approximation gives degree `O(d*(1+R*||h||_infinity)/gamma)`.

This works for dependent supports, but is not an unconditional repair. The number of distinct constraints can be exponential, and a tiny nonzero slope can force a huge R. Even one slab `|epsilon*t|<=gamma` requires radius at least gamma/epsilon to escape. That elementary observation is about the radius inference, not a counterexample satisfying all support-minimality hypotheses of Lemma 71.

The earlier kernel-amplification LP diagnostic, coefficient-l1 sufficient case, independent-character case and logarithmic-character-rank case remain separate valid sufficient conditions. Support minimality alone still has not supplied polynomial bounds on the required radius, amplification or margin. The unrestricted dependent-support conclusion is therefore still proof-pending.

## General lambda-partite hypermatchings

The [complete product-lift proof](lambda-partite-lift.md) now extends the uniform-hypermatching reduction to every positive lambda vector. It yields

`D <= 5184*max(2,k/m)*(2k-1)^10*s^10`,

where k=sum(lambda_i) and m=min(lambda_i). The proof establishes a sensitivity theorem on a product of permutation domains by tensoring the original pure-degree pseudo-characters, simulates its queries through a lazy common hyperedge labeling, and extracts disjoint hyperedge changes from a bounded-degree multigraph of sensitive transpositions.

All source inputs were checked against the final DFLLV26 journal: the permutation degree decomposition and spanning pseudo-characters, cube induction, shortening/certificate bounds and conflict-threshold algorithm. The tensor assembly and query reduction are repository derivations, not claimed printed theorems or independently reviewed literature results.

This supplies the eleven previously missing parameterized reverse-sensitivity chains. All seven profile grids now contain 132 upper chains each, 924 in total. It does not construct an alpha-witnessing system for hypermatchings or prove a quadratic degree/sensitivity bound there. Block-size and M>0 guards remain explicit, and no optimality or priority is certified.

## Conjectures and remaining work

The dependent-support and natural-completion formulations still require a fixed target, allowed Fourier support, exact interpolation versus label approximation, and uniform family-polynomial quantifiers. The quantitative kernel-line lemma is sufficient only with its explicit geometric parameters; neither it nor the lambda-partite query lift resolves the natural-completion characterization. No new primary-source correction of the original normalization step was found in the limited follow-up search.

Remaining work includes the 176 unmatched completion intervals, current-best/priority checks, stronger hypermatching sensitivity bounds and independent review of the repository reductions. Nis91 and AB25 journal proofs remain uninspected. No HTML has been generated.
