# Completion and general-domain audit follow-up

Later developments: see [higher-support and profile audit](higher-support-and-profile-audit.md) for the current sufficient normalization cases, tighter chains and domain-profile inventories.

This round fills indexing gaps and gives a sufficient repair of a disputed proof step. It does not establish the unrestricted source lemma or certify an exhaustive literature survey.

## Completion inventory

The extended inventory now indexes evidence in 255 of 506 ordered cells, up from 181. The new paths use elementary comparisons already in the catalogue: a certificate dominates its fractional relaxation, an unambiguous certificate is a certificate, disjoint sensitive blocks give a feasible fractional packing, and deterministic/exact algorithms satisfy the corresponding randomized/zero-error requirements. Expected zero-error classical algorithms can be truncated at a constant multiple of their worst-input expectation before quantum simulation. These comparisons preserve exponents; truncation constants are not silently identified.

The generator now admits checked definition proofs and five explicitly reviewed simulation records. It still excludes historical bounds, input-size factors, mixed products, restricted-class bounds and arbitrary records marked merely “derived”. For each completion upper chain, choose a total completion minimizing the right-hand measure and apply the total-function comparison there. Different factors cannot be minimized independently. The remaining 251 cells are unindexed, not asserted open.

## General-domain inventory

The new twelve-measure [general-domain matrix](domain-matrix.md) has 132 ordered cells and 38 parameter-free upper chains. It lists the two direct parameterized bounds separately. Its paths use only the composable-domain scope of the original source; each path retains its claim IDs and error conventions.

Neither `D <= beta^(-2) max(Delta,n/M) bs^4` nor `C <= beta^(-1) bs^2` is a uniform edge when the domain varies. M must be positive for the first formula. Sensitivity-to-degree arguments need the separate pseudo-character witnessing hypothesis. The forward-only multislice theorems of Ben-David and the inverse-query permutation model are kept outside this common-oracle closure. The matrix deliberately leaves unsupported reverse directions blank rather than importing Boolean-cube inequalities.

Original source verification uses DFLLV26 Theorem 3.1 and its model definitions, together with the previously inspected DFLLV22 author manuscript. The indexed elementary comparisons follow certificate/LP relaxation, acceptance-polynomial and simulation arguments. This matrix is conservative coverage, not an optimal exponent table for every domain profile.

## The normalization step

HKMP26 v3 Lemma 71 (article pp.33–34) takes `M=||Delta||_infinity`, a coefficient norm, and asserts `|p_Delta(x)|/M <= 2` throughout the cube. A bound on individual Fourier coefficients does not imply this. The exact counterexample to that particular inference is recorded in the earlier audit. In addition, M can be zero, so this denominator cannot be used without a case split.

A rigorous sufficient repair is as follows. Suppose p has degree at most d and full-cube absolute value at most one. Let q be its degree-at-most-d perturbation, with s perturbed Fourier coefficients, each at most M in absolute value. Suppose q has the correct sign on the promise and `|q(x)| >= gamma > 0` everywhere. Then

`|q(x)| <= 1 + ||Delta||_1 <= 1+sM = K`.

Normalize q by K, which is always positive. Lemma 27's univariate sign approximant, composed with q/K, gives a bounded approximating polynomial for `F=sign(q)` of degree `O(d*K/gamma)` at fixed error. Thus polynomial s, M and inverse margin suffice for polynomial completion approximate degree. This proof works for M=0 as well.

To infer `D(f)=poly(Q(f))`, d must also be polynomially controlled by the native approximate degree of f (which is O(Q(f))). The total completion has polynomial approximate degree, the total-function deterministic upper bound applies to it, and restricting its decision tree to the promise solves f. An arbitrary high-degree starting approximant does not supply that final comparison.

This is a repository sufficient condition with additional hypotheses. Low degree alone does not bound s polynomially in d: there can be `sum_{j<=d} binomial(n,j)` Fourier coordinates. No unrestricted coefficient-only repair, nor a counterexample to the final lemma under all its intended restrictions, is claimed.

## Conjecture 72: quantifiers matter

The source's discussion allows enlarging the Fourier basis through a polynomial degree cutoff. For a fixed target completion F and a full degree-t basis, existence of a degree-t approximant q for F is equivalent to existence of a coefficient perturbation with `Delta=coeff(q)-coeff(p)` and `p_Delta=q`. Under that unrestricted interpretation the equivalence is an algebraic representation identity.

A substantive restricted formulation must specify support, norm, margin and the quantifier fixing F. In particular, if F must be the original `sign(p)` on the entire cube, finding a different low-degree completion does not suffice. Kernel membership preserves values on the promise, not signs everywhere. The catalogue now records these distinctions explicitly. It does not label an unspecified restricted formulation resolved.

Targeted searches did not provide a primary-source correction of the normalization argument. Absence of a hit is not evidence that none exists. Nis91 and AB25 journal-text comparisons, the remaining completion cells, domain-profile reverse comparisons and other conjecture formulations remain unfinished. No HTML has been generated.
