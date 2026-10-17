# Independent mathematical audit of four repository derivations

Audit date: 2026-10-17. I read the four catalogue records directly and independently reconstructed their arguments. I checked the RC convention against Aar02 Definition 3, the R1 definition against the catalogue's AIK26 convention, and the fixed-support interpretation against HKMP26 Definition 68 and Lemma 71. This is a mathematical and convention audit, not priority certification or an independent line-by-line verification of all cited papers. None of the arguments below uses Aar02's old Theorem 10.

## 1. Sharp verification constants: passes under the stored convention

For each fixed claimed input x, let q_i be the probability that a verifier queries i when its actual input is x. Repeated queries can be omitted. Coupling the verifier on x and an opposite-output y, the executions agree until the first query in their disagreement set B. Acceptance on x is certain, so rejection on y with probability at least 1/2 implies sum_{i in B} q_i >= 1/2. Thus w_i=2q_i is a fractional certificate and FC(x)<=2 E[cost on x]<=2 RC(x). This proof uses expected cost, and the final inequality is valid for either cost measured at x or worst-case expected cost.

Conversely, for fractional weights w_i, independently preselect i with probability 1-exp(-(ln 2)w_i), query the selected coordinates, and reject exactly upon disagreement with x. Every opposite y is missed with probability exp(-(ln 2)sum_{i in B}w_i)<=1/2. The expected number selected is at most (ln 2)sum_i w_i, uniformly on all actual inputs. This proves the stated upper bound even with worst-case expected cost.

For the promise {0^N} union {weight-k strings}, symmetry and summing all k-subset constraints give FC(0)=N/k; each positive claim has FC=1. On the zero execution let T be the number of distinct queried coordinates. For a uniformly random k-subset y, the probability of missing y is E[g(T)] with g(t)=binom(N-t,k)/binom(N,k), interpreting binomial coefficients as zero past their valid range. Any rejection on y requires a query hit, so E[g(T)]<=1/2. The integer sequence has second differences binom(N-t-2,k-2)/binom(N,k)>=0 (with endpoint conventions); its linear interpolation is decreasing and convex. Jensen therefore forces E[T] to exceed the interpolated half-threshold. Selecting a uniform subset of one of the two adjacent integer sizes attains the threshold and has uniform expected query cost. For N=k^3 the threshold is (ln 2+o(1))N/k: for t=Theta(N/k), log g(t)=sum_{j<k}log(1-t/(N-j))=-kt/N+o(1). Positive claims need only query one known 1 with probability 1/2. The single-bit function attains the lower coefficient 1/2.

No error found. Explicit limitations: partial-promise upper-coefficient sharpness does not establish total-function or completion sharpness; the coefficients are specific to rejecting error 1/2 and expected query cost. They should not be attributed as a printed theorem to Aar02.

## 2. Capped one-sided quadratic bound: passes

Let T be a worst-execution cap and p the minimum positive acceptance probability; no false positives are permitted. Any positive accepting transcript is a 1-certificate: otherwise a zero input consistent with the transcript would be accepted by that deterministic random seed, contradicting one-sided correctness (up to the usual removal of a null set of seeds, valid because the input set is finite). Thus C1<=T.

In the deterministic certificate-query algorithm, select a positive input consistent with the current restriction and query a positive certificate for it, omitting already queried coordinates. At any surviving zero input x, the newly queried certificate disagrees with x on a nonempty block B_j. Changing exactly that block produces a positive input y_j satisfying the full certificate. The B_j are disjoint across rounds. Under identical randomness, acceptance on y_j entails hitting B_j on x, since otherwise the executions agree. Consequently Pr_x[hit B_j]>=p and kp<=E_x[number of distinct queries]<=T.

After floor(T/p) rounds, a remaining nonconstant restriction would contain a zero x and a positive certificate yielding one further disjoint block, contradicting (floor(T/p)+1)p>T. Hence D<=floor(T/p) C1<=T^2/p. Constants and constant-function edge cases agree with the record. This proof does not justify transferring the coefficient to Nisan's expected-cost convention.

## 3. Quantitative kernel-line slab avoidance: passes as a conditional result

For every nonzero slope h(x), the forbidden set |p(x)+t h(x)|<gamma is an open interval of length 2gamma/|h(x)|. Representatives of identical affine pairs suffice. Their total length is at most 2gamma S<2R, so they cannot cover [-R,R]. Constraints with zero slope are safe by the stated hypothesis. Choosing an uncovered t yields margin >=gamma and norm <=1+R||h||_infinity. Standard constant-error polynomial approximation to sign on [-K,-gamma] union [gamma,K], with K=1+R||h||_infinity, has degree O(K/gamma). Composition gives O(dK/gamma), where d bounds both p and h; this follows from h using the fixed support of p. Exact promise values are preserved because h vanishes there.

No unconditional normalization conclusion follows: S, the minimum nonzero slope, and ||h||_infinity can depend badly on the input dimension and chosen kernel direction. The statement correctly retains these parameters.

## 4. Minimal-support bounded-interpolation vertices: passes

The fixed-support full-cube evaluation matrix H is injective because its columns are distinct Fourier characters. The constraints |Ha|<=1 imply each Fourier coefficient has magnitude <=1 by Fourier inversion. The feasible set is therefore closed and bounded, hence compact, and contains the original coefficient vector. Every feasible vector has exactly the same promised values and degree at most d. A zero coordinate would contradict support minimality in the stated bounded approximant class.

At a vertex, if a nonzero vector annihilated both the domain equalities and all active cube-bound rows, then sufficiently small moves in both directions would preserve the inactive inequalities (there are finitely many) and all active equalities, contradicting extremality. Hence the augmented row matrix has full column rank.

This says nothing by itself about rank of the domain matrix alone. Saturated full-cube bounds may provide the missing rank. Thus it neither resolves unrestricted normalization nor furnishes a counterexample satisfying the source's support-minimal hypotheses.

## Conclusion

All four arguments pass this independent mathematical audit under the explicit stored conventions. No new derivation should be advertised as a priority result or as a proof of HKMP26 Lemma 71 in unrestricted form. Source-version verification, particularly the later Aar02 manuscript's corrections, remains a separate task for the integrating agent.
