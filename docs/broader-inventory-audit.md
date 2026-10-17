# Broader completion, domain and version audit

This round adds source-linked definitions and proof routes. An inspected theorem statement or proof outline is not an independent full-proof certification. HTML remains deferred.

## Completion inventory

There are now 23 explicit minimum-completion measures, including one-sided certificates, unambiguous certificates, fractional and quantum certificates, one-sided randomized cost and detectable-failure quantum cost. The [extended inventory](extended-completion-inventory.md) contains all 506 ordered off-diagonal cells; 181 have indexed evidence. The remaining cells are extraction gaps, not assertions of open problems. The complete twelve-measure core remains separately available with its lower witnesses and logarithmic endpoints.

The extension uses only eligible single-measure power inequalities on total Boolean functions. It does not transform `A<=B*C` into `min A<=min B*min C`, since the minima may have different optimizers. Likewise, `min_F max_b C_b(F)` is not replaced by `max_b min_F C_b(F)`. Only the safe componentwise inequalities are entered. One-sided certificate measures need not be polynomially equivalent to deterministic depth on total functions, so membership in the generic completion template does not imply that equivalence.

The constructions and their notation are also registered in `data/completion-constructions.json`: fixed-output completions, sign completions of a fixed approximant, the domain evaluation matrix and coefficient perturbations. These are distinct from the unrestricted minimum over all completions.

HKMP26 Definition 29 introduces another important constraint: its exact and approximate Fourier sparsities for partial functions minimize support **among degree-optimal bounded polynomials**. These have separate IDs from ordinary approximate sparsity, full-function Fourier sparsity and 0/1 monomial sparsity. The bias convention, coefficient influence and all factors in the biased Lipschitz criterion are explicit.

## General query domains

The [domain register](general-domains.md) gives the input sets, allowed queries and parameters for product domains, permutations, perfect matchings, hypermatchings, multislices and slices. Twelve generic measures are defined on these query domains. The parameterized theorem is

`D <= beta^(-2) * max(Delta,n/M) * bs^4`,

with the source's additional conditions for replacing the prefactor by `beta^(-2)*Delta`. The register preserves chunk size, conflict bound, query overlap and sensitivity ratios. Composability and the pseudo-character witnessing property are separate hypotheses. For multislices, `floor(min(lambda)/2)` can be zero; the formula involving `n/M` is not applied then.

The same input set with a different oracle can have different comparisons. For an even-sized permutation, consider whether the position of value 1 lies in the first half. One inverse query solves it, and a sum of permutation-entry indicators represents it with degree one. Under **forward-only** queries it needs n/2 queries: before then an adversary can return distinct values other than 1, leaving both output possibilities. Thus the all-distinct multislice must not be identified with the forward-and-inverse permutation query model.

Ben-David’s original TQC 2016 paper supplies uniform comparisons on a single multislice with forward-only coordinate queries: `D=O(Q^18)` and `D=O(R^9)` (Theorems 5/12), and `C<=3*bs*s_2<=3*bs^2` (Theorem 8). Its proof splits according to certificate size; the small-certificate case isolates a restricted alphabet and reduces to a permutation-inversion adversary problem. These are source-verified bounds, not claims that the exponent 18 is optimal. For a union of orbits over a fixed alphabet of size M, Theorem 6 gives `R=O(Q^(18(M-1)))`; the promise is invariant but the function need not be.

The general-domain proof routes are certificate querying, shortening disjoint sensitive changes, LP duality, acceptance polynomials and Boolean subcube reductions. The sensitivity theorem additionally uses degree-witnessing pseudo-characters and Huang's theorem. No uniform pure-power comparison is inferred after dropping the domain parameters.

## A blocked perturbation proof step

HKMP26 Lemma 71 rescales a perturbed polynomial by the infinity norm of its **coefficient vector**, then uses a uniform bound on its **function values**. That bound is not supplied by the coefficient norm. In general,

`||p_Delta||_infinity <= ||p||_infinity + ||Delta||_1 <= 1+s*||Delta||_infinity`,

where s is the Fourier support size.

An exact small example checks the disputed step. Let `p=(x1+x2+x3+x4)/4`, with promised inputs the all-plus and all-minus vectors, and perturb its linear coefficients by `(1,9/10,-4/5,-11/10)`. The perturbation preserves values on those promised inputs. Its coefficient infinity norm is `11/10`; the perturbed polynomial has full-cube minimum absolute value `1/5` and maximum absolute value `19/5`. Consequently the displayed range bound `|p_Delta|/M<=2` fails. This illustrates the specific norm step; it is **not** presented as a counterexample to the lemma's final conclusion or to every possible additional restriction in the surrounding setup.

The record therefore remains proof-pending. A separately proved sufficient condition normalizes by the actual function bound K and uses a full-cube margin gamma; sign approximation then has degree `O(d*K/gamma)` at fixed error. Kernel membership preserves values on the promise only, and does not by itself preserve the original polynomial's sign off-promise.

Conjecture 72 also needs its perturbation class stated precisely. If arbitrary coefficients on all characters up to the permitted degree are allowed, any target polynomial in that space is already a coefficient perturbation. The catalogue records this formulation issue rather than declaring the intended conjecture proved or open.

## Conjecture status and distributional variants

The original AA14 journal paper distinguishes its folklore almost-everywhere quantum/classical simulation conjecture from its stronger bounded-polynomial influential-coordinate conjecture. The latter implies the former; no converse is asserted. Its appendix relates the folklore statement to dense promises. This repairs the attribution chain behind HKMP26 Conjecture 77.

GMNR26, arXiv v1 of 28 September 2026, proves equivalences of both types of conjecture across the uniform cube, fixed-bias products and fixed-density slices. It does **not** prove their truth. The proof uses small bias-conversion gadgets, coherent uncomputation, product/slice couplings and hybrid bounds; corresponding variance and influence comparisons handle the polynomial conjecture. Bias dependence is retained. These equivalences do not resolve the separate almost-completion conjecture HKMP26 78.

Influence has normalization and carrier differences. AA14/GMNR26 use an unnormalized squared bit-flip difference. On the uniform cube this is four times the derivative-normalized HKMP26 influence. On slices, bit-flip influence uses values outside the slice; swap influence does not. The source proves `swInf_(i,j)<=2*(Inf_i+Inf_j)`. Neither is the maximum packing sensitivity used in the domain theorems.

Targeted searches identified no resolving primary source for HKMP26 72/78, robust low degree on permutations or perfect matchings, or the general q-analog framework. Their current resolution remains unverified. The robust question's error modulus and the q-analog query models remain part of the formulation audit.

## Version checks and bibliography

The May 2022 author-hosted domain manuscript has 62 pages, compared with 59 in the 2020 arXiv source. Its main indexed bounds and domain parameters were checked, including visually reading key formulas. Its added Circuits section moves the open questions to Section 9. The final 2026 journal PDF has now also been obtained: 60 article pages plus a repository cover. Selected statements and proof routes, including Theorem 3.1, the domain parameters and randomized failure conventions, agree with the indexed bounds. The journal omits the author manuscript’s Circuits section and places open questions in Section 8. The robust low-degree and q-analogue questions are still proposed there; a later resolution has not been verified.

The Ambainis–Belovs journal publication is now bibliographically recorded: computational complexity 34(2), article 14, 1–25 (2025), DOI 10.1007/s00037-025-00277-4; online publication was 3 October, with a December print issue. Its proof remains checked through the original CCC 2023 paper, not the subscription journal text. The supplied Nisan conference original remains separate from the uninspected Nis91 journal version. A normal browser visit to the SIAM publisher page confirmed that full text requires subscriber or paid access; no purchase was made. See `data/journal-version-audit.json` for explicit version statuses.

Remaining work includes the Nisan and Ambainis–Belovs journal proof comparisons, the unindexed extended-completion cells, complete profiles beyond the current domain families, independent computation/proof checks and remaining conjecture formulations. The survey is not yet certified exhaustive or ready for HTML.
