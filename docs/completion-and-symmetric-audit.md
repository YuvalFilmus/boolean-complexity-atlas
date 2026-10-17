# Completion, relevance and symmetric-group audit

Later status: see [the broader inventory audit](broader-inventory-audit.md), including the obtained DFLLV26 final journal and expanded completion/domain inventory. Pending statements below describe that earlier audit stage.

This round checks source statements, conventions and proof routes. It does not certify every proof step or complete the full citation literature. No HTML has been started.

## Minimum over completions

HKMP26 is now pinned as arXiv:2603.29256v3, 30 September 2026. Definition 45 uses an **overline**, visually checked in the PDF. Thirteen explicit instantiations are defined: the twelve core measures and relevant-variable count. Instantiated display symbols are marked as repository notation; the original defines the generic overline-M template.

For any total-function upper bound `A<=g(B)`, choose a completion F_B minimizing B. Then

`min_F A(F) <= A(F_B) <= g(B(F_B)) = g(min_F B(F))`.

This supplies all 132 off-diagonal upper comparisons in [the completion matrix](completion-matrix.md). All 132 total-function lower witnesses also transfer: on a total function there is only one completion, itself. Logarithmic endpoint losses are preserved; the matrix is not claiming a log-free quadratic where the original bound has a logarithm. Native promise measures are not replaced by minimum-completion measures.

Observation 49 proves `minimum-completion D=D`: any partial deterministic tree defines an output off-promise and hence a total completion. Lemma 48 compares measures evaluated on completions optimizing members of a uniformly polynomially equivalent set; it does **not** compare arbitrary completions. Lemma 50 therefore characterizes absence of a speedup by polynomial growth under completion. These are recorded as conditional family statements.

The domain-indicator construction in Lemma 51 multiplies a globally bounded approximant by a globally bounded approximant to promise membership. For fixed error margins its displayed proof gives additive degree `O(d+q)`; the source states the weaker `poly(d,q)`. Global boundedness is necessary. The slice completion statement in Theorem 56 is recorded with its complete-slice domain and mixed parameters explicit.

Four further definitions distinguish exit-sensitive sensitivity/block sensitivity, completion-critical block sensitivity and critical certificates. The last minimizes certificates **only among completions already optimal for critical block sensitivity**. It is not an unconstrained minimum of certificate complexity. This critical block measure maximizes only over promised points, whereas minimum-completion block sensitivity maximizes over the entire cube. The relation critical measures are separate definitions.

A useful additional identity is `minimum-completion nRelevant = Dna` for partial decision functions. A fixed coordinate set S solves the promise exactly iff no opposite-output pair agrees on S. Its observed patterns define a total completion depending only on S. Conversely, the relevant coordinates of any completion give a nonadaptive solver. In particular this quantity is at most `2^D-1`, but it need not be polynomial in D.

## Nisan's expected-cost constant

The supplied STOC 1989 original defines R_1 using worst-case **expected** query cost, no false positives and acceptance at least 1/2 on positive inputs. Theorem 3 prints `D<=2R_1^2`. Under these literal conventions the one-bit identity refutes that constant: reject immediately with probability 1/2 and query otherwise. Expected cost is 1/2, and the printed bound would say `1<=1/2`.

A direct repair of the certificate-query argument gives the sharp universal constant **4** for this convention. If T is the expected cost, an accepting transcript is a 1-certificate, so `C1<=2T`. Query a consistent 1-certificate each round. At any surviving zero input, coupling with a positive input satisfying the certificate forces probability at least 1/2 of probing the new disagreement block. The blocks from different rounds are disjoint, so at most `floor(2T)` rounds are possible. Thus `D<=2T*C1<=4T^2`. The one-bit identity attains equality, since acceptance requires making a query.

The corrected factor 4 is a **repository derivation**, not an attributed Nisan theorem or a claimed published erratum. The printed factor 2 remains a historical record excluded from inference. This does not affect the cubic exponent or the asymptotic quadratic relation. Nis91's journal full text is still unavailable here; whether it changes the definition or statement remains unchecked.

## Relevant variables

Theorem 3.13 of Wel22, visually checked on p.10, gives `nRelevant<=4.3935*2^degree`, sharper than the introductory 4.394. Its proof uses coordinate-local restriction potentials, exact-rational LP bounds for low degrees and the general block-sensitivity improvement. The source's Maple computation has not been independently reproduced.

The record set now compares relevance to every core measure in both directions: each core measure is `O(nRelevant)`, but no finite pure power of any one bounds nRelevant. For the lower direction use `f_1=x` and `f_d=(1-z)f_{d-1}(L)+z f_{d-1}(R)` on fresh disjoint variables. It has depth and degree d and `2^d-1` relevant variables; every core measure is O(d). The exact depth upper bound `nRelevant<=2^D-1` is also indexed.

Wellens' hybrid degree/sensitivity and certificate/sensitivity bounds from Theorem 3.18 are included with a weaker proof status: the author gives the convex-potential idea but explicitly omits the technical proof. Conjecture 3.17, removing the sensitivity prefactor from Simon's relevance bound, remains current-status-unverified after targeted searches; it is not certified open.

## Symmetric group

The expanded S_n family includes certificates, unambiguous certificates, fractional block sensitivity, capped randomized queries, detectable failure and quantum variants. The [132-pair upper matrix](permutation-matrix.md) uses only permutation-qualified edges. It gives derived upper bounds, not optimal exponents or a lower-bound classification.

Queries reveal pi(i) or inverse-pi(j). The source's R_0 is capped failure probability at most 2/3, distinct from expected Las Vegas cost. Because outputs are Boolean, guessing a fresh fair bit on failure converts it to error at most 1/3 **without increasing the cap**. Certificate partitions, LP duality, polynomial acceptance probabilities and the domain parameters give the remaining chains. Parameters Delta=2, M=n and beta>=1/3 yield the conservative derived bound `D<=18*bs^4`.

Sensitivity s packs disjoint sensitive transpositions; edge sensitivity t counts all of them. For `f(pi)=[pi(1)=1]`, all twelve core permutation measures are bounded by one, while `t=n-1`. At a positive input all sensitive swaps involve position 1. This explicitly rules out a finite-power upper bound on t by any core permutation measure, and explains its exclusion from the polynomial-equivalence matrix.

Remaining source work includes the final Combinatorial Theory journal proof (a direct PDF request did not return a PDF), Nis91 journal text, all general-domain and multislice parameters, the remaining completion constructions/conjectures, and full proofs omitted by authors. The bibliography distinguishes inspected full preprints from final-publication metadata.
