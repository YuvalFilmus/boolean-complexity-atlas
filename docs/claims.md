# Source-linked claims

Generated from data/catalog.json. This is an expanding, incomplete catalogue. Status labels describe the evidence inspected; none of these entries is certified globally best-known.

## s-bs

s(f) <= bs(f)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: definition_proof; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Singleton blocks are disjoint sensitive blocks.

## bs-C

bs(f) <= C(f)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: definition_proof; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Every certificate intersects every sensitive block.

## C-D

C(f) <= D(f)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: definition_proof; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: A deterministic transcript fixes the output.

## adeg-deg

adeg(f) <= deg(f)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: definition_proof; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: An exact polynomial is an approximant.

## R-D

R(f) <= D(f)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: definition_proof; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Simulate a deterministic algorithm.

## Q-R

Q(f) <= R(f)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: definition_proof; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Simulate randomized queries coherently or with mixed states.

## QE-D

QE(f) <= D(f)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: definition_proof; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Simulate deterministic queries exactly.

## Q-QE

Q(f) <= QE(f)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: definition_proof; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: An exact answer meets the error requirement.

## C-UC

C(f) <= UC(f)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: definition_proof; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: An unambiguous certificate is a certificate.

## bs-fbs

bs(f) <= fbs(f)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: definition_proof; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Put unit weight on disjoint blocks.

## FC-C

FC(f) <= C(f)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: definition_proof; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Use an integral certificate as an LP cover.

## FC-fbs

FC(f) = fbs(f)

- Kind: identity; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: definition_proof; loss: none.
- Source: Repository proof, LP primal/dual.
- Proof: Finite LP duality.

## C-C0C1

D(f) <= C_0(f) C_1(f)

- Kind: multivariate_upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: survey_checked; loss: none.
- Source: [BdW02](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf), Certificate/decision-tree relations.
- Proof: Query compatible certificates; each failed round reduces the opposite certificate budget.

## C-bs2

C(f) <= bs(f)^2

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BBCMW01](https://arxiv.org/abs/quant-ph/9802049), Lemma 5.2 (Nisan), PDF pp.7–8.
- Proof: At x, take a maximal disjoint family of minimal sensitive blocks. Its union is a certificate; each block has size at most bs at the flipped input. The original proof is reproduced here.

## D-Cbs

D(f) <= C(f) bs(f)

- Kind: multivariate_upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BBCMW01](https://arxiv.org/abs/quant-ph/9802049), Lemma 5.3, PDF p.8.
- Proof: Query a consistent 1-certificate per round. If more than bs rounds were needed, the failures would yield too many disjoint sensitive blocks; each round costs at most C_1.

## D-deg-bs

D(f) <= deg(f) bs(f)

- Kind: multivariate_upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: source_checked; loss: none.
- Source: [Mid04](https://arxiv.org/abs/quant-ph/0403168), Proof of Theorem 4, final paragraph.
- Proof: Query a maxonomial repeatedly; each round supplies a disjoint sensitive block.

## D-deg3

D(f) <= 2 deg(f)^3

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: source_checked; loss: none.
- Source: [Mid04](https://arxiv.org/abs/quant-ph/0403168), Theorem 4.
- Proof: Combine the maxonomial algorithm with bs <= 2 deg^2.

## deg-QE

deg(f) <= 2 Q_E(f)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: source_checked; loss: none.
- Source: [BBCMW01](https://arxiv.org/abs/quant-ph/9802049), Polynomial-method lemma.
- Proof: T quantum queries give amplitudes of degree T and probabilities of degree at most 2T.

## adeg-Q

adeg(f) <= 2 Q(f)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: source_checked; loss: none.
- Source: [BBCMW01](https://arxiv.org/abs/quant-ph/9802049), Polynomial-method lemma.
- Proof: The acceptance polynomial approximates f.

## D-Q6-history

D(f) = O(Q(f)^6)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: source_checked; loss: none.
- Source: [BBCMW01](https://arxiv.org/abs/quant-ph/9802049), Main classical simulation bound.
- Proof: Polynomial method plus classical degree and block-sensitivity inequalities.

Historical result; inspect superseding records before selecting a frontier.

## deg-s2

deg(f) <= s(f)^2

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: source_checked; loss: none.
- Source: [Hua19](https://arxiv.org/abs/1907.00847), Sensitivity-conjecture consequence.
- Proof: Signed hypercube adjacency and eigenvalue interlacing.

## deg-lambda2

deg(f) <= lambda(f)^2

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: source_checked; loss: none.
- Source: [ABKBRT21](https://arxiv.org/abs/2010.12629), Theorem 1.
- Proof: Huang spectral argument.

## lambda-s

lambda(f) <= s(f)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: definition_proof; loss: none.
- Source: Repository proof, Adjacency norm.
- Proof: Spectral radius is at most maximum degree.

## s-lambda2

s(f) <= lambda(f)^2

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: definition_proof; loss: none.
- Source: Repository proof, Star subgraph.
- Proof: A vertex of degree s induces a star with norm sqrt(s).

## lambda-deg

lambda(f) <= deg(f)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: source_checked; loss: none.
- Source: [ABKBRT21](https://arxiv.org/abs/2010.12629), Theorem 10.
- Proof: Fourier matrix norm estimate.

## lambda-adeg

lambda(f) = O(adeg(f))

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: source_checked; loss: none.
- Source: [ABKBRT21](https://arxiv.org/abs/2010.12629), Theorem 17.
- Proof: Composition and tensor powers.

## lambda-adeg-constant

lambda(f) <= adeg_bounded_epsilon(f)/(1-2epsilon)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: source_checked; loss: none.
- Source: [ABKBRT21](https://arxiv.org/abs/2010.12629), Theorem 18.
- Proof: Polynomial difference matrix.

## deg-adeg2

deg(f) = O(adeg(f)^2)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: source_checked; loss: none.
- Source: [ABKBRT21](https://arxiv.org/abs/2010.12629), Theorem 4.
- Proof: Huang’s signed-hypercube argument gives deg<=lambda^2. A spectral bound proved using approximating polynomials gives lambda=O(adeg); composing them yields the quadratic relation.

## deg-Q2

deg(f) = O(Q(f)^2)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: source_checked; loss: none.
- Source: [ABKBRT21](https://arxiv.org/abs/2010.12629), Theorem 3.
- Proof: Huang plus spectral adversary.

## D-Q4

D(f) = O(Q(f)^4)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: source_checked; loss: none.
- Source: [ABKBRT21](https://arxiv.org/abs/2010.12629), Theorem 2.
- Proof: Combine Midrijanis D<=deg*bs with the spectral-sensitivity bound deg=O(Q^2) and the polynomial-method bound bs=O(Q^2). Both factors are essential to the quartic exponent.

## RC-adeg2

RC(f) = O(adeg(f)^2)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Theorem 3.4 and Corollary 1.2, PDF pp.7–8.
- Proof: Amplify a hypothetical counterexample by repeated composition; composition limits make integral and fractional block sensitivity comparable, while approximate degree grows multiplicatively up to constants.

## R0-R2

R_0(f) = O(R(f)^2 log(2+R(f)))

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_log.
- Source: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Theorem 5.3, PDF p.10.
- Proof: Bound the number of minimal flipping blocks by 2 fbs(f)^s(f), substitute into Midrijanis R_0=O(R log nbs), and use s<=fbs=O(R).

## QC-RC

QC(f) = Theta(sqrt(RC(f)))

- Kind: theta_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: source_checked; loss: none.
- Source: [Aar02](https://arxiv.org/abs/quant-ph/0210020), Main characterization.
- Proof: An optimal fractional query distribution gives a quantum verifier by amplitude amplification, costing the square root of classical verification. A positive-weight adversary argument supplies the matching lower bound.

## fbs-RC

fbs(f) = Theta(RC(f))

- Kind: theta_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 2.1, Definition 2.2, and Section 1 related work.
- Proof: A fractional cover gives a nonadaptive verifier by sampling coordinates proportional to their weights; a verifier induces cover weights via its coordinate-query probabilities.

## C-R2

C(f) = O(R(f)^2)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: derived; loss: none.
- Source: Repository proof, BBCMW01 Lemma 5.2 plus coupling.
- Proof: C<=bs^2 and bs<=3R imply C<=9R^2. This verifies the exponent without relying on the later paper’s attribution.

Dependencies: C-bs2, bs-R.

## C-Q4

C(f) = O(Q(f)^4)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: derived; loss: none.
- Source: [BK26](https://arxiv.org/abs/2609.15063), Introduction, paragraph following Theorem 1.
- Proof: Use C <= D and the quartic simulation.

Dependencies: C-D, D-Q4.

## Q-C2-sep

There is a total family with Q(f) = Omega_tilde(C(f)^2)

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: source_checked; loss: polylog.
- Source: [ABK16](https://arxiv.org/abs/1511.01937), Theorem 3.
- Proof: BKK construction and cheat sheets.

## Q-adeg4-sep

There is a total family with Q(f) >= adeg(f)^(4-o(1))

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: source_checked; loss: subpolynomial.
- Source: [ABK16](https://arxiv.org/abs/1511.01937), Theorem 2.
- Proof: Recursive BKK with cheat sheets.

## D-Q4-sep

There is a total family with D(f) = Omega_tilde(Q(f)^4)

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylog.
- Source: [ABBLS17](https://arxiv.org/abs/1506.04719), Corollary 7, from Theorems 2, 4, 5.
- Proof: A unique all-one column carries pointers certifying zeros elsewhere. An adversary forces deterministic nm queries, while quantum search finds and verifies the candidate in O_tilde(sqrt(n)+sqrt(m)); take n=2m.

## C-R2-sep-BK

C(f_n)=Omega(n^2), R(f_n)=O(n log n)

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: source_checked; loss: polylog.
- Source: [BK26](https://arxiv.org/abs/2609.15063), Theorem 1; Lemmas 3 and 4.
- Proof: Sample race winners, eliminate candidates, verify; untouched cards force large 0-certificates.

## C-Q4-sep-BK

C(f_n)=Omega(n^2), Q(f_n)=O_tilde(sqrt(n))

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: source_checked; loss: polylog.
- Source: [BK26](https://arxiv.org/abs/2609.15063), Theorem 1; Lemma 5.
- Proof: Virtual candidates, quantum tournament sink finding, and Grover verification.

## C-Q4-sep-AIK

C(F_n)>=n(ceil(n/2)+1), Q(F_n)=O(sqrt(n) log(n)^3)

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: source_checked; loss: explicit_log.
- Source: [AIK26](https://arxiv.org/abs/2609.11664), v3 Theorem 2.1.
- Proof: DNF, position lists, cheat-sheet totalization, and source finding.

## C-R1-2-sep-AIK

C(f_n)=Theta(n^2), R_1(f_n)=O(n)

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: source_checked; loss: none.
- Source: [AIK26](https://arxiv.org/abs/2609.11664), v3 Theorem 2.2.
- Proof: Unambiguous DNF with randomized elimination.

## C-R2-sep-AIK

C(f_n)=Theta(n^2), R(f_n)=O(n)

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: derived; loss: none.
- Source: [AIK26](https://arxiv.org/abs/2609.11664), v3 Theorem 2.2.
- Proof: One-sided algorithm is also two-sided.

Dependencies: C-R1-2-sep-AIK.

## sym-D-Q2

D(f) = O(Q(f)^2) for symmetric total Boolean f

- Kind: upper_bound; domain: total decision_function; classes: symmetric.
- Evidence: source_checked; loss: none.
- Source: [BBCMW01](https://arxiv.org/abs/quant-ph/9802049), Symmetric-function characterization.
- Proof: Symmetrization plus polynomial lower bounds.

## sym-deg-rdeg

deg(f)+1 <= 3 rdeg(f) for nonconstant symmetric total f

- Kind: upper_bound; domain: total decision_function; classes: symmetric.
- Evidence: source_checked; loss: none.
- Source: [IJKKSWW23](https://arxiv.org/abs/2310.08004), 2310.08004v2 Proposition 6.
- Proof: Symmetrize the rational representation and count roots.

Abstract search metadata says deg/2; v2 Proposition 6 states (deg+1)/3. Use the versioned main text, pending latest-version reconciliation.

## mono-deg-rdeg

deg(f) <= rdeg(f)^2 for monotone total f

- Kind: upper_bound; domain: total decision_function; classes: monotone.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [IJKKSWW23](https://arxiv.org/abs/2310.08004), v2 Section 3.2, Corollary 14.
- Proof: For unate functions, rational degree equals sensitivity: monotone local changes force a nondeterministic-degree lower bound, and certificates supply the converse. Combine with Huang degree<=sensitivity squared.

## partial-R-Q

For each integer k>=1: Q(f_n)<=k, R(f_n)=Omega_tilde(n^(1-1/(2k)))

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: source_checked; loss: polylog.
- Source: [SSW20](https://arxiv.org/abs/2008.10223), Abstract / main application.
- Proof: Decision-tree Fourier-growth bounds applied to forrelation.

## partial-Q-rdeg

Imbalance_n: rdeg=O(1), adeg=Omega(n), hence Q=Omega(n)

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [IJKKSWW23](https://arxiv.org/abs/2310.08004), v2 Section 6.2 (Imbalance).
- Proof: The promise makes an exact rational representation low-degree, while symmetrization and the univariate approximation bound force linear approximate degree, and hence linear quantum complexity.

## search-Q-adeg

There are total query-TFNP relations on poly(n) input bits with rel_adeg and rel_conical both O(polylog n), while Q=tildeOmega(sqrt(n)).

- Kind: no_polynomial_bound; domain: total search_relation; classes: query_TFNP.
- Evidence: primary_statement_and_proof_route_checked; loss: see_source.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Corollary 40, from Theorem 39, Theorem 31 and Corollary 32.
- Proof: Construct repeated AND-OR search with a small family of XOR shifts: conical polynomials describe short witnesses, but a quantum direct-product lower bound and union bound over shifts give Q=Omega_tilde(sqrt(n)).

Here n is the construction parameter, not necessarily the input length. These are bounded polynomial systems and two-sided bounded conical systems.

## search-Q-conical

There are total query-TFNP relations on poly(n) input bits with rel_adeg and rel_conical both O(polylog n), while Q=tildeOmega(sqrt(n)).

- Kind: no_polynomial_bound; domain: total search_relation; classes: query_TFNP.
- Evidence: primary_statement_and_proof_route_checked; loss: see_source.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Corollary 40, from Theorem 39, Theorem 31 and Corollary 32.
- Proof: The low-degree witness polynomials remain conical juntas under the total-search transformation; the shifted repeated-search quantum lower bound is unchanged.

Here n is the construction parameter, not necessarily the input length. These are bounded polynomial systems and two-sided bounded conical systems.

## search-D-psQ

D(S)=O(psQ(S)^5 log N) for total search S

- Kind: upper_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_log.
- Source: [AGL26](https://doi.org/10.4230/LIPIcs.ICALP.2026.3), Preprint Theorem 1.4; ICALP Theorem 4.
- Proof: Use pseudo-determinism to bound how many canonical outputs can arise; binary search for the canonical output reduces to total Boolean predicates, each simulated deterministically using the quartic D/Q relation.

## bs-R

bs(f) <= 3 R(f)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: definition_proof; loss: none.
- Source: Repository proof, Coupling argument.
- Proof: For each disjoint sensitive block, correctness on the base input and its flip forces query probability at least 1/3; sum over blocks.

## bs-adeg2

bs(f) <= 6 adeg(f)^2

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [NS94](https://web.vu.lt/mif/s.jukna/boolean/Nisan-Szegedy.pdf), Lemma 3.8, combined with Lemma 3.5.
- Proof: Map one new variable to each disjoint sensitive block, fixing the rest. Symmetrize the resulting polynomial, then use a univariate derivative inequality to force quadratic degree.

## bs-deg2

bs(f) <= 2 deg(f)^2

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: secondary_checked; loss: none.
- Source: [Mid04](https://arxiv.org/abs/quant-ph/0403168), Theorem 2, attributed to Nisan–Szegedy.
- Proof: Degree lower bound from disjoint sensitive blocks.

## bs-s4

bs(f) <= 2 s(f)^4

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: derived; loss: none.
- Source: Repository proof, Composition of inequalities.
- Proof: Substitute deg <= s^2 into bs <= 2 deg^2.

Dependencies: bs-deg2, deg-s2.

## D-R3

D(f) = O(R(f)^3)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: derived; loss: none.
- Source: Repository proof, Composition of inequalities.
- Proof: Use D <= C bs, C=O(R^2), and bs=O(R).

Dependencies: D-Cbs, C-R2, bs-R.

## D-adeg4

D(f) = O(adeg(f)^4)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: derived; loss: none.
- Source: Repository proof, Composition of inequalities.
- Proof: Use D <= deg bs and the two quadratic degree bounds.

Dependencies: D-deg-bs, deg-adeg2, bs-adeg2.

## Q-adeg4-upper

Q(f) = O(adeg(f)^4)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: derived; loss: none.
- Source: Repository proof, Classical simulation.
- Proof: Q <= D <= O(adeg^4).

Dependencies: D-adeg4, Q-QE, QE-D.

## R-Q4

R(f) = O(Q(f)^4)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: derived; loss: none.
- Source: Repository proof, Classical simulation.
- Proof: R <= D <= O(Q^4).

Dependencies: R-D, D-Q4.

## search-D-psR3

For every total search relation S, D(S)<=54 psR(S)^3 under the CDM23 error-1/3 convention.

- Kind: upper_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), CDM23 Theorem 3.2; full report Theorem 3.2(2) and proof.
- Proof: Choose the canonical multi-output function computed by the pseudo-deterministic algorithm, then apply the cubic deterministic/randomized relation for multi-output functions.

The complete proof of the multi-output bound is in the ECCC report; the proceedings omits some proofs. This cubic 2023 bound predates AGL26’s discussion of an older quartic classical bound.

## D-Rank-no-bound

OR_n has Rank=1 and D=n, so no bound on D in terms of Rank alone

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 1; Section 5 depth/rank discussion.
- Proof: A chain computes OR with rank one, while the zero input forces n queries. Thus even a general function of rank alone cannot upper-bound deterministic depth.

## partial-rdeg-Q

MajOrNone_n has Q=O(1) and rdeg=Omega(n)

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: source_checked; loss: none.
- Source: [IJKKSWW23](https://arxiv.org/abs/2310.08004), v2 Section 6.1.
- Proof: Hamming-slice promise and rational-polynomial root counting.

## D-C2

D(f) <= C(f)^2

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: definition_proof; loss: none.
- Source: Repository proof, Repository derivation / explicit family.
- Proof: Use D <= C_0 C_1 and C_b <= C.

Dependencies: C-C0C1.

## Q-C2-upper

Q(f) <= C(f)^2

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: definition_proof; loss: none.
- Source: Repository proof, Repository derivation / explicit family.
- Proof: Q <= Q_E <= D <= C^2.

Dependencies: Q-QE, QE-D, D-C2.

## D-bs3

D(f) <= bs(f)^3

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: definition_proof; loss: none.
- Source: Repository proof, Repository derivation / explicit family.
- Proof: Use D <= C bs and C <= bs^2.

Dependencies: D-Cbs, C-bs2.

## OR-D-Q

OR_n witnesses D(OR_n)=Theta(Q(OR_n)^2)

- Kind: separation; domain: total decision_function; classes: symmetric, monotone.
- Evidence: source_checked; loss: none.
- Source: [BBCMW01](https://arxiv.org/abs/quant-ph/9802049), AND/OR query characterization; approximate-degree lower bound via polynomial method.
- Proof: OR needs n classical queries or exact degree; Grover gives O(sqrt(n)), and polynomial lower bounds give Omega(sqrt(n)).

## OR-R-Q

OR_n witnesses R(OR_n)=Theta(Q(OR_n)^2)

- Kind: separation; domain: total decision_function; classes: symmetric, monotone.
- Evidence: source_checked; loss: none.
- Source: [BBCMW01](https://arxiv.org/abs/quant-ph/9802049), AND/OR query characterization; approximate-degree lower bound via polynomial method.
- Proof: OR needs n classical queries or exact degree; Grover gives O(sqrt(n)), and polynomial lower bounds give Omega(sqrt(n)).

## OR-deg-Q

OR_n witnesses deg(OR_n)=Theta(Q(OR_n)^2)

- Kind: separation; domain: total decision_function; classes: symmetric, monotone.
- Evidence: source_checked; loss: none.
- Source: [BBCMW01](https://arxiv.org/abs/quant-ph/9802049), AND/OR query characterization; approximate-degree lower bound via polynomial method.
- Proof: OR needs n classical queries or exact degree; Grover gives O(sqrt(n)), and polynomial lower bounds give Omega(sqrt(n)).

## OR-deg-adeg

OR_n witnesses deg(OR_n)=Theta(adeg(OR_n)^2)

- Kind: separation; domain: total decision_function; classes: symmetric, monotone.
- Evidence: source_checked; loss: none.
- Source: [BBCMW01](https://arxiv.org/abs/quant-ph/9802049), AND/OR query characterization; approximate-degree lower bound via polynomial method.
- Proof: OR needs n classical queries or exact degree; Grover gives O(sqrt(n)), and polynomial lower bounds give Omega(sqrt(n)).

## bs-deg2-Tal

bs(f) <= deg(f)^2

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Tal13](https://eccc.weizmann.ac.il/report/2012/163/), Theorem 4; Section 6.
- Proof: Apply a fractional-block-sensitive LP argument and polynomial composition to remove the factor two in the Nisan–Szegedy inequality.

Historical result; inspect superseding records before selecting a frontier.

## bs-deg2-Pro

bs(f) <= deg(f)^2/(sqrt(10)-2)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Pro21](https://arxiv.org/abs/2101.08600), Theorem 1.
- Proof: A sharper analysis of the symmetrized univariate polynomial improves the derivative estimate.

## bs-adeg2-Pro

bs(f) <= sqrt(101/6) adeg(f)^2

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Pro21](https://arxiv.org/abs/2101.08600), Theorem 2.
- Proof: Analyze the symmetrized approximating polynomial more precisely than the original Markov bound.

## bs-s4-Pro

bs(f) <= s(f)^4/(sqrt(10)-2)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Pro21](https://arxiv.org/abs/2101.08600), Corollary following Theorem 1.
- Proof: Substitute Huang deg<=s^2 into the improved block/degree inequality.

## fbs-deg2

fbs(f) <= deg(f)^2

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Corollary 3.2(1).
- Proof: The composition-limit transfer lemma upgrades a block-sensitivity/degree bound to fractional block sensitivity with the same constant.

## fbs-adeg2

fbs(f) = O(adeg(f)^2)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Theorem 3.4.
- Proof: Composition amplification transfers the quadratic integral block bound to the fractional relaxation.

## QC-adeg

QC(f) = O(adeg(f))

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Corollary 1.3.
- Proof: Combine fbs=Theta(RC), fbs=O(adeg^2), and QC=Theta(sqrt(RC)).

## R0-R-s-RC

R_0(f)=O(R(f) s(f) log(2+RC(f)))

- Kind: multivariate_upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_log.
- Source: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Proof of Theorem 5.3.
- Proof: Count minimal blocks by fractional block sensitivity, then use Midrijanis block-number derandomization.

## C-bs-s

C(f) <= bs(f) s(f)

- Kind: multivariate_upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BBCMW01](https://arxiv.org/abs/quant-ph/9802049), Lemma 5.2 proof, with singleton sensitivity retained.
- Proof: The union of a maximal disjoint family of minimal sensitive blocks is a certificate; each minimal block has size at most sensitivity at its flip.

## R-Q4-sep-2026

For each fixed k>=2: Q(F_{k,m})<=C_k sqrt(m) log(m)^{b_k}, R(F_{k,m})>=c_k m^{2-1/k}/log(m)^2. Thus every exponent below 4 is excluded.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: arbitrarily_small_power_and_polylog.
- Source: [OAI26](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf), Theorem 1.1 and Sections 2–5.
- Proof: Addressed cheat sheets with outward pointers give a unique winner. A quantum tournament handles unreliable off-promise competitors; a planted hidden-zero argument and adaptive direct product force randomized address cost.

Publication status: repository_preprint.

## bs-lambda-sep-2026

A total family satisfies bs(f_t)=Omega(lambda(f_t)^2.127)

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Mei26](https://arxiv.org/abs/2608.00851), Theorem 6.1 and its composition corollary.
- Proof: Take a union of subcubes indexed by a doubly regular tournament, use the Lovasz local lemma to control spectral sensitivity, and amplify the finite example by composition.

The certified finite example has 2017584 variables, bs>=14011, lambda<=89.0162. The numerical exponent near 2.20 elsewhere in the paper is not recorded as a proved lower bound.

## QD-Q

QD(f) <= Q(f)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BK19](https://arxiv.org/abs/1902.03660), Proposition 6.
- Proof: Retain the output state of a bounded-error algorithm; opposite outputs have separated measurement distributions.

## QD-QSZK

QD(f) <= QSZK(f)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BK19](https://arxiv.org/abs/1902.03660), Theorem 2.
- Proof: Run both state-preparation procedures and use the near/far trace-distance promise to separate opposite inputs.

## QSZK-Q

QSZK(f) <= Q(f)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BK19](https://arxiv.org/abs/1902.03660), Proposition 15.
- Proof: Compare the output-bit state of the quantum algorithm with the constant zero state.

## QC-QD

QC(f) = O(QD(f))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BK19](https://arxiv.org/abs/1902.03660), Proposition 8.
- Proof: Fix an input and distinguish its output state from all opposite-output states.

## AdvPlus-QD

AdvPlus(f) = O(QD(f))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BK19](https://arxiv.org/abs/1902.03660), Section 3.2, equation (7).
- Proof: The adversary progress proof only needs separated final states, not a common output measurement.

## Q0-QD5-history

Q_0(f)=O(QD(f)^5 log(2+QD(f)))

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_log.
- Source: [BK19](https://arxiv.org/abs/1902.03660), Theorem 1; Section 4.
- Proof: Hybrid query probabilities yield fractional certificates; repeatedly sample them to find a verified certificate.

The later quartic D/Q bound supersedes the corresponding Q_0/Q consequence, not automatically the Q_0/QD statement.

## fbs-QS2

fbs(f)=O(QS_weak(f)^2)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CMP24](https://arxiv.org/abs/2408.12595), Theorem 5.
- Proof: Apply a hybrid argument against a fractional packing of differing blocks.

## QSstrong-Q

QS_str(f)=O(min(Q(f),sqrt(n)))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CMP24](https://arxiv.org/abs/2408.12595), Main results / strong-input distinguishing algorithm.
- Proof: Run a quantum algorithm with access to both underlying inputs, or search directly for a differing coordinate.

## QSstrongIndex-Q

QS_str^ind(f)=O(min(Q(f)^(3/2),sqrt(n)))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CMP24](https://arxiv.org/abs/2408.12595), Main results / index-output algorithm.
- Proof: Convert distinguishing progress into finding a differing index via search.

## CGns-CGent

CGns(f)=O(CGent(f))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CG22](https://arxiv.org/abs/2211.03396), Proposition 2.7.
- Proof: Entangled strategies are nonsignaling.

## CGent-CGpub

CGent(f)=O(CGpub(f))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CG22](https://arxiv.org/abs/2211.03396), Proposition 2.7.
- Proof: Shared entanglement can realize shared random bits.

## CGpub-CGpriv

CGpub(f)=O(CGpriv(f))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CG22](https://arxiv.org/abs/2211.03396), Proposition 2.7.
- Proof: A public source can supply independent random seeds.

## CAdv-CGns

CAdv(f)=O(CGns(f))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CG22](https://arxiv.org/abs/2211.03396), Theorem 6.2.
- Proof: Nonsignaling output marginals supply a feasible classical-adversary solution.

## CGpub-CAdv

CGpub(f)=O(CAdv(f))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CG22](https://arxiv.org/abs/2211.03396), Theorem 7.1.
- Proof: Correlated sampling of input-index distributions attains the minimax adversary overlap.

## CGpub-R

CGpub(f)=O(R(f))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CG22](https://arxiv.org/abs/2211.03396), Theorem 5.7.
- Proof: Use shared coins to simulate a randomized tree, then sample a common query position.

## CGpub-EC

CGpub(f)=O(EC(f))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CG22](https://arxiv.org/abs/2211.03396), Theorem 5.5.
- Proof: Sample weighted certificates with public hashing to coordinate an intersecting index.

## CGpub-C

CGpub(f)=O(C(f))

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CG22](https://arxiv.org/abs/2211.03396), Theorem 5.4.
- Proof: Public hashing coordinates the two short opposite certificates.

## R0-CGpriv

R_0(f) <= CGpriv(f)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CG22](https://arxiv.org/abs/2211.03396), Theorem 5.10(2).
- Proof: Private strategies induce randomized certificate queries; verify their intersection progress to obtain a zero-error algorithm.

## CGpriv-EC2

CGpriv(f)=O(EC(f)^2)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CG22](https://arxiv.org/abs/2211.03396), Theorem 5.10(2).
- Proof: Normalize expectational certificate weights to independent output distributions; their winning overlap is inverse-quadratic.

## CGpriv-C0C1

CGpriv(f) <= C_0(f) C_1(f)

- Kind: multivariate_upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CG22](https://arxiv.org/abs/2211.03396), Theorem 5.10(4).
- Proof: Each player samples uniformly from a shortest certificate; opposite certificates share a differing index.

Total-function scope entered conservatively. Partial-function certificate conventions in CG22 Section 4.4 need separate records before extending the scope.

## AdvPlus-CGpriv

AdvPlus(f)^2 <= CGpriv(f)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CG22](https://arxiv.org/abs/2211.03396), Theorem 5.10(1).
- Proof: Use the private strategy distributions in the minimax quantum adversary bound and compare squared sum of square roots with sum of products.

## CGpubSingle-s

CGpub_{[1]}(f)=Theta(s(f))

- Kind: theta_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CG22](https://arxiv.org/abs/2211.03396), Theorem 8.4.
- Proof: A public strategy coordinates a sensitive neighbor index; the degree of the sensitivity graph bounds the achievable success probability.

## CGprivSingle-lambda

CGpriv_{[1]}(f)=lambda(f)^2

- Kind: identity; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CG22](https://arxiv.org/abs/2211.03396), Theorem 8.8.
- Proof: The private single-bit game is a matrix scaling/spectral optimization on the sensitivity graph.

## Rexp-literaldeg

RE(f)=ldeg_+(f)

- Kind: identity; domain: total real_valued_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLW14](https://arxiv.org/abs/1411.7280), Theorem 9.
- Proof: Tree leaves give nonnegative literal monomials; conversely sample a conjunction and scale its nonnegative contribution.

## Qexp-sosdeg

QE_in_expectation(f)=deg_sos(f)

- Kind: identity; domain: total real_valued_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLW14](https://arxiv.org/abs/1411.7280), Theorem 12.
- Proof: Quantum output probabilities are sums of squared low-degree amplitudes; a sum-of-squares representation can be implemented as a quantum expectation algorithm.

## Rexp-Qexp-no-bound

f(x)=(sum_i x_i-1)^2 has RE(f)=n and QE_in_expectation(f)=1

- Kind: no_polynomial_bound; domain: total real_valued_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLW14](https://arxiv.org/abs/1411.7280), Section 5.
- Proof: A single square has SOS degree one, while the zero set forces degree n in every nonnegative literal representation.

## hazardD-R2

D_u(f)=O(R_u(f)^2)

- Kind: upper_bound; domain: total hazard_free_extension; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BKMNSS25](https://arxiv.org/abs/2507.00148), Theorem 4.4.
- Proof: Prime implicants/implicates make u-sensitivity, u-block sensitivity and u-certificates linearly equivalent; certificate rounds give quadratic deterministic simulation.

## hazardD-Q4

D_u(f)=O(Q_u(f)^4)

- Kind: upper_bound; domain: total hazard_free_extension; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BKMNSS25](https://arxiv.org/abs/2507.00148), Theorem 4.4.
- Proof: Use the same certificate-round algorithm and the quantum square-root block-sensitivity lower bound.

## hazardC-hazardS

cc_u(f) <= 2 s_u(f)-1 for nonconstant f

- Kind: upper_bound; domain: total hazard_free_extension; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BKMNSS25](https://arxiv.org/abs/2507.00148), Theorem 3.1.
- Proof: A prime implicant and prime implicate certify an unknown output; they intersect, so at most k_1+k_2-1 positions suffice.

## brick-s-exp

N_br^ell(f) <= (6 s(f))^ell

- Kind: parameterized_upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CG26](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.61), Theorem 9.
- Proof: A weighted double-count over coordinate flips bounds bricks by induction on block size.

## block-s-exp

N_bs^ell(f) <= (6 s(f))^ell

- Kind: parameterized_upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CG26](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.61), Theorem 5.
- Proof: Every minimal sensitive block is a brick, so apply the brick-count theorem.

## block-brick

N_bs(f) <= N_br(f)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CG26](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.61), Definitions 3,7.
- Proof: Every coordinate in a minimal sensitive block flips the value back at the block-flipped input.

## fbs-Qdeph

Q_deph_{p,epsilon}(f)=Omega_epsilon(p fbs(f))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [ARS26](https://arxiv.org/abs/2610.00506), Theorem 1.3; Theorem 5.1.
- Proof: Track a fractional-block-sensitive progress measure and bound its expected growth under independent index dephasing.

Equivalently fbs=O_epsilon(Q_deph/p); no constant uniform in p is claimed.

## fbs0-Qneg

Q_neg_{p,epsilon}(f)=Omega_epsilon((p/(1-p)) fbs(f,0^n))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [ARS26](https://arxiv.org/abs/2610.00506), Theorem 1.1.
- Proof: A fractional packing of sensitive blocks at 0^n drives the negligent-oracle progress lower bound.

Left scalar A is displayed only for indexing; the actual lower bound is local fbs(f,0^n), not global fbs. Excluded from scalar inference.

## deg-rdeg3

deg(f)=O(rdeg(f)^3 log(2+rdeg(f)))

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_log.
- Source: [KKWY26](https://arxiv.org/abs/2601.08727v3), Theorem 8; Corollary 4.
- Proof: A deterministic algorithm queries randomized certificate sets hitting maximal monomials of two nondeterministic representations. A fractional-block lower bound on sign degree controls the cost; restricting to a full-degree monomial removes input-length dependence.

Publication status: FOCS_2026_to_appear_as_reported_by_authors.

## deg-sign2-rdeg

deg(f)=O(rdeg(f) signDeg(f)^2 log(2+rdeg(f)))

- Kind: multivariate_upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_log.
- Source: [KKWY26](https://arxiv.org/abs/2601.08727v3), Corollary 4, equation (53).
- Proof: Track a decreasing maximal-monomial potential while using the best randomized certificate on every restriction; bound its cost by minimum fractional block sensitivity and sign degree.

Publication status: FOCS_2026_to_appear_as_reported_by_authors.

## rdeg-deg

rdeg(f) <= deg(f)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KKWY26](https://arxiv.org/abs/2601.08727v3), Introduction.
- Proof: Use denominator one.

Publication status: FOCS_2026_to_appear_as_reported_by_authors.

## sign-rdeg

signDeg(f) <= 2 rdeg(f)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KKWY26](https://arxiv.org/abs/2601.08727v3), Fact 2.
- Proof: Square a nondeterministic numerator and shift by a sufficiently small positive constant.

Publication status: FOCS_2026_to_appear_as_reported_by_authors.

## PostQE-rdeg

PostQ_0(f)=rdeg(f)

- Kind: identity; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KKWY26](https://arxiv.org/abs/2601.08727v3), Fact 4 and Appendix A.
- Proof: Amplitude preparation and exact postselection realize the rational representation; conversely postselected acceptance probabilities yield a rational representation.

Publication status: FOCS_2026_to_appear_as_reported_by_authors.

## D-rdeg3-n

D(f)=O(rdeg(f)^3 log n)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_log.
- Source: [KKWY26](https://arxiv.org/abs/2601.08727v3), Theorem 8.
- Proof: The maximal-monomial potential shrinks geometrically under certificate-set queries.

Publication status: FOCS_2026_to_appear_as_reported_by_authors.

The logarithm depends on input length; this does not by itself give a pure pairwise exponent bound on D in terms of rdeg.

## bs-rdeg3

bs(f)=O(rdeg(f)^3 log(2+rdeg(f)))

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_log.
- Source: [KKWY26](https://arxiv.org/abs/2601.08727v3), Corollary 4, equation (54).
- Proof: Restrict to the union of minimal disjoint sensitive blocks, whose total size is at most bs^2, then apply the deterministic simulation and eliminate the remaining logarithm.

Publication status: FOCS_2026_to_appear_as_reported_by_authors.

## D-rdeg-RCmin

D(f)=O(rdeg(f) RC_min^downarrow(f) log n)

- Kind: multivariate_upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_log.
- Source: [KKWY26](https://arxiv.org/abs/2601.08727v3), Theorem 6.
- Proof: Query a certificate set hitting a constant fraction of maximal monomials; its potential starts at n^O(rdeg) and decreases geometrically.

Publication status: FOCS_2026_to_appear_as_reported_by_authors.

## bs-deg2-Wellens

bs(f) <= sqrt(2/3) deg(f)^2 + 1

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Theorem 1.2.
- Proof: Use a noise-operator polynomial bounded on the whole interval and a second-derivative Markov-brothers inequality.

## nRelevant-deg-exp

nRelevant(f) <= 4.394 * 2^deg(f)

- Kind: nonpolynomial_upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Theorem 1.1, equation (1.3).
- Proof: A coordinate-local degree potential bounds how many variables survive restrictions; small-degree LP bounds sharpen the constant.

Rounded introductory form; Theorem 3.13 in the same paper gives 4.3935.

## fbs-bs-sep-constant

There is a family with fbs(f)=(1/sqrt(6)-o(1)) bs(f)^(3/2)

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [APV18](https://arxiv.org/abs/1810.02393), Theorem 1.
- Proof: Compose OR with a graph-property gadget chosen to improve the fractional packing/integral packing ratio.

## bs-s2-sep-AS

There is a family with bs(f)=(2/3)s(f)^2-(1/3)s(f)

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [AS11](https://eccc.weizmann.ac.il/report/2011/116/), Main construction, Section 4.
- Proof: OR together carefully spaced subcube patterns so many disjoint blocks coexist while one-sided sensitivity stays small.

## C1-bs0-s0

C_1(f) >= 3 bs_0(f)/(2 s_0(f))

- Kind: multivariate_lower_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [AP14](https://arxiv.org/abs/1402.5078), Main theorem.
- Proof: Analyze pairwise intersections of minimal sensitive blocks and charge the conflicts to 0-sensitivity.

## sym-C-s-constant

C(f) <= 2 s(f); a family has C(f)=2s(f)-4

- Kind: upper_bound; domain: total decision_function; classes: symmetric.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [MNP24](https://arxiv.org/abs/2110.12616v5), Theorems 4(1),8; Lemma 7.
- Proof: Certify a Hamming-weight interval by its boundary ones and zeros; the boundary sensitivities pay for both ends.

## sym-bs-s-constant

bs(f) <= (3/2) s(f), with asymptotically matching families

- Kind: upper_bound; domain: total decision_function; classes: symmetric.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [MNP24](https://arxiv.org/abs/2110.12616v5), Theorems 4(2),9.
- Proof: Compute local block sensitivity from the two endpoints of a constant Hamming interval, then optimize their ratio to sensitivity.

## sym-Q-lambda

Q(f)=Theta(lambda(f))

- Kind: theta_bound; domain: total decision_function; classes: symmetric.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [MNP24](https://arxiv.org/abs/2110.12616v5), Theorems 1–2; Section 1.1.
- Proof: Analyze adjacent Hamming layers for spectral sensitivity and construct explicit minimax weights; compare with the known quantum and approximation characterization.

## sym-lambda-adeg

lambda(f)=Theta(adeg(f))

- Kind: theta_bound; domain: total decision_function; classes: symmetric.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [MNP24](https://arxiv.org/abs/2110.12616v5), Theorems 1–2; Section 1.1.
- Proof: Analyze adjacent Hamming layers for spectral sensitivity and construct explicit minimax weights; compare with the known quantum and approximation characterization.

## sym-Adv-lambda

AdvPlus(f)=Theta(lambda(f))

- Kind: theta_bound; domain: total decision_function; classes: symmetric.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [MNP24](https://arxiv.org/abs/2110.12616v5), Theorems 1–2; Section 1.1.
- Proof: Analyze adjacent Hamming layers for spectral sensitivity and construct explicit minimax weights; compare with the known quantum and approximation characterization.

## sym-CGpriv-Adv2

CGpriv(f)=Theta(AdvPlus(f)^2)

- Kind: theta_bound; domain: total decision_function; classes: symmetric.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [MNP24](https://arxiv.org/abs/2110.12616v5), Theorem 1.
- Proof: The explicit minimax adversary weights also solve the square-root private certificate-game optimization.

## graph_property-D-bs2

D(f)=O(bs(f)^2)

- Kind: upper_bound; domain: total decision_function; classes: graph_property.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CPS22](https://arxiv.org/abs/2209.08042), Theorem 1.1(1).
- Proof: For graph properties, bs is Omega(number of vertices), while D is at most the number of edges; for zebra functions, monochromatic stripe structure bounds certificate-query progress.

## zebra-D-bs2

D(f)=O(bs(f)^2)

- Kind: upper_bound; domain: total decision_function; classes: zebra.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CPS22](https://arxiv.org/abs/2209.08042), Theorem 1.3(1).
- Proof: For graph properties, bs is Omega(number of vertices), while D is at most the number of edges; for zebra functions, monochromatic stripe structure bounds certificate-query progress.

## graph-D-deg2

D(f)=O(deg(f)^2) for graph properties

- Kind: upper_bound; domain: total decision_function; classes: graph_property.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CPS22](https://arxiv.org/abs/2209.08042), Theorem 1.1(2).
- Proof: Graph invariance forces real degree Omega(number of vertices); query every possible edge.

## Dcert-C

D^cert(f)=C(f)

- Kind: identity; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLLPV26](https://arxiv.org/abs/2609.26757), Theorem 3(1).
- Proof: Certification restricts to one accepting input against all opposite-value inputs; deterministic certificates characterize the task, and the certification sandwich lemma gives the other equalities.

## R0cert-C

R0^cert(f)=C(f)

- Kind: identity; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLLPV26](https://arxiv.org/abs/2609.26757), Theorem 3(1).
- Proof: Certification restricts to one accepting input against all opposite-value inputs; deterministic certificates characterize the task, and the certification sandwich lemma gives the other equalities.

## UCcert-C

UC^cert(f)=C(f)

- Kind: identity; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLLPV26](https://arxiv.org/abs/2609.26757), Theorem 3(1).
- Proof: Certification restricts to one accepting input against all opposite-value inputs; deterministic certificates characterize the task, and the certification sandwich lemma gives the other equalities.

## Rcert-RC

R^cert(f)=Theta(RC(f))

- Kind: theta_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLLPV26](https://arxiv.org/abs/2609.26757), Theorem 3(2).
- Proof: Use stability and idempotence of certification to sandwich the transformed measure between randomized certification and fractional certificates.

## RScert-RC

RS^cert(f)=Theta(RC(f))

- Kind: theta_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLLPV26](https://arxiv.org/abs/2609.26757), Theorem 3(2).
- Proof: Use stability and idempotence of certification to sandwich the transformed measure between randomized certification and fractional certificates.

## ECcert-RC

EC^cert(f)=Theta(RC(f))

- Kind: theta_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLLPV26](https://arxiv.org/abs/2609.26757), Theorem 3(2).
- Proof: Use stability and idempotence of certification to sandwich the transformed measure between randomized certification and fractional certificates.

## CAdvcert-RC

CAdv^cert(f)=Theta(RC(f))

- Kind: theta_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLLPV26](https://arxiv.org/abs/2609.26757), Theorem 3(2).
- Proof: Use stability and idempotence of certification to sandwich the transformed measure between randomized certification and fractional certificates.

## Qcert-QC

Q^cert(f)=Theta(QC(f))

- Kind: theta_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLLPV26](https://arxiv.org/abs/2609.26757), Theorems 4 and 6.
- Proof: Apply the certification sandwich lemma between quantum certification and a lower bound that already captures quantum certificates.

## QDcert-QC

QD^cert(f)=Theta(QC(f))

- Kind: theta_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLLPV26](https://arxiv.org/abs/2609.26757), Theorems 4 and 6.
- Proof: Apply the certification sandwich lemma between quantum certification and a lower bound that already captures quantum certificates.

## AdvPluscert-QC

AdvPlus^cert(f)=Theta(QC(f))

- Kind: theta_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLLPV26](https://arxiv.org/abs/2609.26757), Theorems 4 and 6.
- Proof: Apply the certification sandwich lemma between quantum certification and a lower bound that already captures quantum certificates.

## QScert-QC

QS^cert(f)=Theta(QC(f))

- Kind: theta_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLLPV26](https://arxiv.org/abs/2609.26757), Theorems 4 and 6.
- Proof: Apply the certification sandwich lemma between quantum certification and a lower bound that already captures quantum certificates.

## cubeBoundedAdegcert-QC

cubeBoundedAdeg^cert(f)=Theta(QC(f))

- Kind: theta_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLLPV26](https://arxiv.org/abs/2609.26757), Theorems 4 and 6.
- Proof: Apply the certification sandwich lemma between quantum certification and a lower bound that already captures quantum certificates.

## QEcert-Q0cert

Q_E^cert(f)=Theta(Q_0^cert(f))

- Kind: theta_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLLPV26](https://arxiv.org/abs/2609.26757), Theorem 5.
- Proof: Exact amplitude amplification on an input-fixed certification problem removes the inconclusive outcome with constant-factor query overhead.

## lambdaCert-s

lambda^cert(f)=sqrt(s(f))

- Kind: identity; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLLPV26](https://arxiv.org/abs/2609.26757), Theorem 11(1); Theorem 42.
- Proof: Every input-fixed certification sensitivity graph is a star with s_x(f) leaves, whose adjacency norm is sqrt(s_x(f)).

## osdeg-Q0

osdeg(f)=O_epsilon(Q_0(f))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLLPV26](https://arxiv.org/abs/2609.26757), Theorem 8.
- Proof: The no-error acceptance probabilities yield globally bounded one-sided approximants after adjusting inconclusive mass.

## rdegCert-rdeg

rdeg^cert(f)=rdeg(f)

- Kind: identity; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLLPV26](https://arxiv.org/abs/2609.26757), Theorem 11(2); Lemma 50.
- Proof: Restrict nondeterministic representations to an input-fixed certification task and use rdeg=max(ndeg(f),ndeg(not f)).

## bs-boundedDegCert2

bs(f)=O((globally-bounded-deg^cert(f))^2)

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLLPV26](https://arxiv.org/abs/2609.26757), Theorem 12(1).
- Proof: The globally bounded degree/block-sensitivity inequality survives the certification transform; block sensitivity is certification-invariant.

## C-boundedDegCert3

C(f)=O((globally-bounded-deg^cert(f))^3)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLLPV26](https://arxiv.org/abs/2609.26757), Theorem 12(2).
- Proof: The maxonomial algorithm still works on certification promises inherited from total f, then combine the certified block-degree bound.

## RC-C

RC(f)=O(C(f))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: derived; loss: none.
- Source: Repository proof, Direct model simulation.
- Proof: Read a shortest fixed-input certificate.

## RC-R

RC(f)=O(R(f))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: derived; loss: none.
- Source: Repository proof, Direct model simulation.
- Proof: Restrict the decision algorithm to its input-fixed certification promise.

## C-R0

C(f)=O(R0(f))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: derived; loss: none.
- Source: Repository proof, Direct model simulation.
- Proof: Every terminating zero-error computation path is a certificate for its input.

## R0-D

R0(f)=O(D(f))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: derived; loss: none.
- Source: Repository proof, Direct model simulation.
- Proof: A deterministic tree is a zero-error randomized tree.

## R-R0

R(f)=O(R0(f))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: derived; loss: none.
- Source: Repository proof, Direct model simulation.
- Proof: Truncate an expected-time zero-error tree at a constant multiple of its worst-input expectation.

## Q0-QE

Q0(f)=O(QE(f))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: derived; loss: none.
- Source: Repository proof, Direct model simulation.
- Proof: An exact fixed-cap algorithm satisfies zero-error requirements.

## Q0-R0

Q0(f)=O(R0(f))

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: derived; loss: none.
- Source: Repository proof, Direct model simulation.
- Proof: Truncate a randomized zero-error algorithm and simulate it quantumly.

## C-adeg4-upper

C(f)=O(adeg(f)^4)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: derived; loss: none.
- Source: Repository proof, Composition of recorded claims: C-bs2, bs-adeg2-Pro.
- Proof: Combine C<=bs^2 with the source-checked quadratic upper bound on bs in terms of approximate degree.

Dependencies: C-bs2, bs-adeg2-Pro.

## C-adeg4-sep

For the AIK26 family F_n, C(F_n)>=n(ceil(n/2)+1), adeg(F_n)=O(sqrt(n) log(n)^3); this excludes every exponent below 4.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: derived; loss: polylog.
- Source: Repository proof, Composition of recorded claims: C-Q4-sep-AIK, adeg-Q.
- Proof: Use adeg<=2Q on the original AIK26 witness. If C<=O(adeg^p) held universally for p<4, the parameterized bounds would imply n^2<=O(n^(p/2) log(n)^(3p)), a contradiction. No conversion of log(n) into log(adeg) is needed.

Dependencies: C-Q4-sep-AIK, adeg-Q.

## R0-Q4-upper

R0(f)=O(Q(f)^4)

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: derived; loss: none.
- Source: Repository proof, Composition of recorded claims: R0-D, D-Q4.
- Proof: A deterministic algorithm is an always-correct randomized algorithm; apply the quartic deterministic-versus-quantum upper bound.

Dependencies: R0-D, D-Q4.

## R0-Q4-sep

For the AIK26 family F_n, R0(F_n)=Omega(n^2), Q(F_n)=O(sqrt(n) log(n)^3); every exponent below 4 is impossible.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: derived; loss: polylog.
- Source: Repository proof, Composition of recorded claims: C-R0, C-Q4-sep-AIK.
- Proof: Certificate complexity lower bounds zero-error randomized complexity up to a constant. Apply this to the AIK26 witness, retaining its parameterized quantum upper bound.

Dependencies: C-R0, C-Q4-sep-AIK.

## Q-s3-sep-BHT

A total family has Q(f)=Omega_tilde(s(f)^3).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylog.
- Source: [BHT17](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2017.28), Theorem 1 and Corollary 2.
- Proof: Make one side of the sensitivity constant using unambiguous certificates, then compose with an AND/OR gadget to balance the sensitivities while preserving the cheat-sheet quantum lower bound.

## C-UCmin-BHT

A total family has C(f)>=UCmin(f)^(log(38/3)/log(8)-o(1)); in particular exponent 1.22 is excluded.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: subpolynomial.
- Source: [BHT17](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2017.28), Theorem 4.
- Proof: Compose weighted projective-plane gadgets with fractional intermediate weights, then round and encode them into Boolean variables.

Historical result; inspect superseding records before selecting a frontier.

## C-s-BHT

A total family excludes every exponent below 1+log(38/3)/log(8) for C versus s.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: subpolynomial.
- Source: [BHT17](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2017.28), Theorem 1 applied to Theorem 4; Corollary 3.
- Proof: Apply the sensitivity transformation to the fractional-weight unambiguous-certificate separation.

Historical result; inspect superseding records before selecting a frontier.

## s-QE-Amb13

For iterated ternary non-equality NE_d, s=3^d and QE=O(2048^(d/8)); the excluded exponent is 8 log(3)/log(2048), not merely the rounded 1.15.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Amb13](https://arxiv.org/abs/1211.0721v6), Theorem 1; Section 3.4, eight-level construction.
- Proof: Design an exact quantum subroutine whose amplitude is transformed under composition; an eight-level algorithm uses 2048 queries and composes recursively.

## adeg-C2-BT17

A total family has adeg(F)>=C(F)^(2-o(1)).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: subpolynomial.
- Source: [BT17](https://arxiv.org/abs/1703.05784), Theorem 38; Section 5.2.2, equations (63)–(65).
- Proof: Use dual block composition and hardness amplification, then a balanced-pair encoding that supplies cheap certificates.

## C-fbs2-GSS

There are total functions on n^2 bits with C=Omega(n^2) and fbs=O(n).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [GSS13](https://arxiv.org/abs/1306.0630), Theorem 32; Section 5.1.1.
- Proof: Choose sparse random codewords far apart but hitting large subcubes, then OR-compose n copies. Distance bounds fractional block packing; subcube hitting forces large certificates.

## D-UC1-GPW

A total family has D=Omega_tilde(UC1^2).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylog.
- Source: [GPW18](https://eccc.weizmann.ac.il/report/2015/050/revision/1/), Theorem 5; Section 2.1.
- Proof: A marked all-one column contains a pointer chain certifying zeros in all other columns. An adaptive adversary forces inspection of the whole matrix.

## R-deg2-GJPW

A total family has R(f)=Omega_tilde(deg(f)^2).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylog.
- Source: [GJPW18](https://eccc.weizmann.ac.il/report/2015/169/), Lemma 7 (coWAPPdt versus UPdt); Section 4.
- Proof: A two-level pointer function has cheap unambiguous positive certificates, hence low exact degree. A distributional conical-junta argument forces quadratic randomized cost.

## D-UC-sep-AKK

D(f)>=UC(f)^(2-o(1)) for a total family.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: subpolynomial.
- Source: [AKK16](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2016.4), Theorem 1.2; Section 2 and recursive construction.
- Proof: Alternate AND/OR composition with cheat-sheet totalization, controlling unambiguous certificates while retaining query lower bounds.

## R-UC-sep-AKK

R(f)>=UC(f)^(2-o(1)) for a total family.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: subpolynomial.
- Source: [AKK16](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2016.4), Theorem 1.3; Section 2 and recursive construction.
- Proof: Alternate AND/OR composition with cheat-sheet totalization, controlling unambiguous certificates while retaining query lower bounds.

## Q-UC-sep-AKK

Q(f)>=UC(f)^(3/2-o(1)) for a total family.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: subpolynomial.
- Source: [AKK16](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2016.4), Theorem 1.4; Section 2 and recursive construction.
- Proof: Alternate AND/OR composition with cheat-sheet totalization, controlling unambiguous certificates while retaining query lower bounds.

## Q-UC1-sep-AKK

A total family has Q(f)=Omega_tilde(UC1(f)^2).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylog.
- Source: [AKK16](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2016.4), Theorem 1.5.
- Proof: Use a cheat sheet to make the accepting certificate unique while preserving quantum hardness.

## deg-UC1

deg(f)<=UC1(f) for total f.

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [GPW18](https://eccc.weizmann.ac.il/report/2015/050/revision/1/), Discussion after Theorems 4–5.
- Proof: Sum the monomial indicators of an unambiguous 1-certificate partition; the sum equals f exactly.

## C-UC1-2-BBGJK

A total family satisfies C0(f)>=Omega_tilde(UC1(f)^2).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylog.
- Source: [BBGJK21](https://arxiv.org/abs/2102.08348v2), Theorems 1–2; Section 3 and Section 5.1.
- Proof: Random row-association functions create a partial-function certificate gap; a cheat-sheet reduction turns it into a total function with cheap unambiguous positive certificates.

Historical result; inspect superseding records before selecting a frontier.

## C-deg2-BBGJK

A total family has C(f)>=Omega_tilde(deg(f)^2).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylog.
- Source: [BBGJK21](https://arxiv.org/abs/2102.08348v2), Corollary 4; also Bal21 Corollary 6.
- Proof: The total unambiguous-DNF witness has C0 large while deg<=UC1, by summing its disjoint accepting-certificate indicators.

Historical result; inspect superseding records before selecting a frontier.

## C-s3-BBGJK

A total family has C(f)>=Omega_tilde(s(f)^3).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylog.
- Source: [BBGJK21](https://arxiv.org/abs/2102.08348v2), Corollary 5; BHT17 Theorem 1; also Bal21 Corollary 5.
- Proof: Apply the BHT sensitivity transformation to the quadratic certificate/unambiguous-certificate gap.

Historical result; inspect superseding records before selecting a frontier.

## C-adeg3-BBGJK-history

A total family has C(f)>=Omega_tilde(adeg(f)^3).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylog.
- Source: [BBGJK21](https://arxiv.org/abs/2102.08348v2), Corollary 6; Section 6.1.
- Proof: Use the Hex partial function, cheat-sheet encoding of paths, and low-degree AND approximations for checking a selected certificate cell.

Historical result; inspect superseding records before selecting a frontier.

## C-lambda4-BBGJK

A total family excludes every exponent below 4 for C versus lambda.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: derived; loss: polylog.
- Source: Repository proof, BBGJK21 Theorem 1; BHT17 sensitivity transformation; ABKBRT21 Appendix A.1.
- Proof: The intermediate BHT transformation preserves C and has s1=O(1), s0=O(UC1), so lambda<=sqrt(s0*s1)=O(sqrt(UC1)). Apply the quadratic C/UC1 gap.

Dependencies: C-UC1-2-BBGJK.

## Q-deg2-ABK

A total family has Q(f)=Omega_tilde(deg(f)^2).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylog.
- Source: [ABK16](https://arxiv.org/abs/1511.01937), Theorem 4; Section 4.2.
- Proof: Apply a cheat sheet to a quantum-hard low-certificate function. The correct cheat-sheet cell is unique, so summing its exact checking polynomials gives small degree.

## D-R0-sep-ABB

A total family has D(f)=Omega_tilde(R0(f)^2).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylog.
- Source: [ABBLS17](https://arxiv.org/abs/1506.04719), Corollary 7.
- Proof: A pointer matrix has an adversarially hidden all-one column; random sampling and back pointers find its certificate quickly.

## R0-R-sep-ABB

A total family has R0(f)=Omega_tilde(R(f)^2).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylog.
- Source: [ABBLS17](https://arxiv.org/abs/1506.04719), Corollary 14.
- Proof: A back-pointer variant makes one-sided randomized evaluation cheap while zero-error evaluation must locate a full certificate.

## R0-QE-sep-ABB

A total family has R0(f)=Omega_tilde(QE(f)^2).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylog.
- Source: [ABBLS17](https://arxiv.org/abs/1506.04719), Corollary 14.
- Proof: Use exact quantum search in the same pointer construction with a zero-error randomized lower bound.

## R-QE-sep-ABB

A total family has R(f)=Omega_tilde(QE(f)^(3/2)).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylog.
- Source: [ABBLS17](https://arxiv.org/abs/1506.04719), Corollary 21.
- Proof: Several marked columns permit exact quantum search while planted distributions force many classical queries.

## R-adeg-sep-ABB

A total family has R(f)=Omega_tilde(adeg(f)^4).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylog.
- Source: [ABBLS17](https://arxiv.org/abs/1506.04719), Corollary 23.
- Proof: Represent the pointer verification by low-degree polynomials while retaining the randomized lower bound.

## deg-C2-ANDOR

For AND_m composed with OR_m, deg=m^2 and C=m; hence deg=C^2.

- Kind: separation; domain: total decision_function; classes: monotone, read_once.
- Evidence: derived; loss: none.
- Source: Repository proof, Elementary polynomial and certificate calculation.
- Proof: The exact polynomial has a nonzero full-degree monomial. Certificates are one zero row or one selected 1 in each row, of maximum size m.

## s-deg-Kushilevitz

For the iterated six-variable Kushilevitz gadget, s(f_k)=6^k and deg(f_k)=3^k, giving exact exponent log(6)/log(3).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [NW95](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/NOAM/RANK/journal.pdf), Footnote 1, manuscript p.5 (journal p.560).
- Proof: The footnote gives an explicit degree-3 polynomial on six variables. Its value is 0 at zero and 1 at every unit vector. Disjoint recursive composition preserves full sensitivity and multiplies degree.

## OR-s-Q

For OR_n, s=n and Q=Theta(sqrt(n)), so the exponent is 2.

- Kind: separation; domain: total decision_function; classes: symmetric, monotone.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BBCMW01](https://arxiv.org/abs/quant-ph/9802049), OR bounds in Section 6.1.
- Proof: OR has n sensitive bits at zero. Quantum search and approximate-degree bounds give square-root complexity; the star adjacency matrix has norm sqrt(n).

## OR-s-adeg

For OR_n, s=n and adeg=Theta(sqrt(n)), so the exponent is 2.

- Kind: separation; domain: total decision_function; classes: symmetric, monotone.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [NS94](https://web.vu.lt/mif/s.jukna/boolean/Nisan-Szegedy.pdf), Example 3.11 and Lemma 3.8.
- Proof: OR has n sensitive bits at zero. Quantum search and approximate-degree bounds give square-root complexity; the star adjacency matrix has norm sqrt(n).

## OR-s-lambda

For OR_n, s=n and lambda=Theta(sqrt(n)), so the exponent is 2.

- Kind: separation; domain: total decision_function; classes: symmetric, monotone.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: Repository proof, Sensitivity graph of OR is a star.
- Proof: OR has n sensitive bits at zero. Quantum search and approximate-degree bounds give square-root complexity; the star adjacency matrix has norm sqrt(n).

## C0-UC1-exact2-Pab

There are total functions with UC1=O(n) and C0=Omega(n^2).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Pab26](https://arxiv.org/abs/2608.02533v2), Theorem 1; Section 2.
- Proof: Construct pairwise-incompatible signed set pairs using a fixed-size subset in each block. Their associated terms are unambiguous, while a 0-certificate must hit many coordinates.

Publication status: SODA_2027_camera_ready_as_reported_by_author.

## C-deg2-Pab

A total family satisfies C(f)=Omega(deg(f)^2), without a polylogarithmic lower loss.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Pab26](https://arxiv.org/abs/2608.02533v2), Corollary 1.2.
- Proof: The log-free C0/UC1 witness has deg<=UC1, giving the quadratic separation.

Publication status: SODA_2027_camera_ready_as_reported_by_author.

## C-s3-Pab

A total family satisfies C(f)=Omega(s(f)^3), without a polylogarithmic lower loss.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Pab26](https://arxiv.org/abs/2608.02533v2), Corollary 1.3; Appendix C.
- Proof: Apply the BHT desensitization and balancing transformation to the log-free C0/UC1 witness.

Publication status: SODA_2027_camera_ready_as_reported_by_author.

## C-adeg4-Bal26

A total family Gn has C(Gn)=Omega(n^2), adeg(Gn)=Theta_tilde(sqrt(n)), on Theta_tilde(n^3) input bits.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylog.
- Source: [Bal26](https://arxiv.org/abs/2608.30351v1), Theorem 1.1; Sections 3–5.
- Proof: Restrict the ambiguous negative certificates to a structured family. Verify their validity using a low-degree count of compatible positive certificates, then apply the cheat-sheet transform.

Publication status: arxiv_preprint.

## C-adeg4-Pab

A total family on O(n^3 log n) bits satisfies C(f)>=Omega(adeg(f)^4/log(n)^6).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylog.
- Source: [Pab26](https://arxiv.org/abs/2608.02533v2), Theorem 4; Appendix D.
- Proof: Attach pointers and certificate cells to the unambiguous-DNF construction. Check each selected certificate with O(n) low-degree consistency tests, then combine their approximants.

Publication status: SODA_2027_camera_ready_as_reported_by_author.

The Appendix D construction also has C(G)=Omega(n^2) and adeg(G)=O_tilde(sqrt(n)); these parameterized bounds, not erasing log(input length) in isolation, justify the excluded exponent 4.

## deg-R0-NAND-SW

On the complete binary NAND tree of height h, deg=2^h, QE>=2^(h-1), and R0=O(((1+sqrt(33))/4)^h). The lower exponent is log(2)/log((1+sqrt(33))/4), approximately 1.32674.

- Kind: separation; domain: total decision_function; classes: read_once.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [SW86](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/SW86/SW86.pdf), Example 1.1, p.30; Theorem 1.5, p.31; polynomial/query translation is elementary.
- Proof: Choose the first child uniformly and stop whenever its value determines the parent. The two output-conditioned costs satisfy a 2-by-2 linear recurrence with dominant root (1+sqrt(33))/4. Exact degree doubles at each NAND level; the polynomial method bounds exact quantum queries.

## QE-R0-NAND-SW

On the complete binary NAND tree of height h, deg=2^h, QE>=2^(h-1), and R0=O(((1+sqrt(33))/4)^h). The lower exponent is log(2)/log((1+sqrt(33))/4), approximately 1.32674.

- Kind: separation; domain: total decision_function; classes: read_once.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [SW86](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/SW86/SW86.pdf), Example 1.1, p.30; Theorem 1.5, p.31; polynomial/query translation is elementary.
- Proof: Choose the first child uniformly and stop whenever its value determines the parent. The two output-conditioned costs satisfy a 2-by-2 linear recurrence with dominant root (1+sqrt(33))/4. Exact degree doubles at each NAND level; the polynomial method bounds exact quantum queries.

## Q-AdvGeneral

Q(f)=Theta(AdvGeneral(f)) for every partial or total Boolean function.

- Kind: theta_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [LMRSS11](https://arxiv.org/abs/1011.3020v2), Theorem 1.1; Definition 3.3; Theorems 3.4 and 4.1.
- Proof: The filtered gamma_2 norm of the state-conversion task is comparable to the general adversary bound. A query algorithm built from its factorization supplies the upper bound; the adversary progress argument supplies the lower bound.

## AdvPlus-AdvGeneral

AdvPlus(f)<=AdvGeneral(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [HLS07](https://arxiv.org/abs/quant-ph/0611054), Definitions 1–2.
- Proof: Every nonnegative adversary matrix is feasible in the signed optimization.

## AdvGeneral-Qeps-constant

AdvGeneral(f)<=2 Q_epsilon(f)/(1-2 sqrt(epsilon(1-epsilon))) for Boolean output and 0<=epsilon<1/2.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [HLS07](https://arxiv.org/abs/quant-ph/0611054), Theorem 2, Boolean-output case; Section 3.
- Proof: Track a weighted progress quantity across oracle queries, and use the final measurement’s output correctness to bound it, including signed adversary weights.

## partial-R0-D

R0(f)<=D(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Promise-valid elementary derivation; docs/partial-functions.md.
- Proof: Run an optimal deterministic tree.

Applies to weak promise certificates and unrestricted promise degree; it does not import a total-function certificate-product bound.

## partial-R-R0

R(f)=O(R0(f)) for worst-case expected Las Vegas cost.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Promise-valid elementary derivation; docs/partial-functions.md.
- Proof: Truncate after three times the maximum expected cost; Markov bounds the failure probability.

Applies to weak promise certificates and unrestricted promise degree; it does not import a total-function certificate-product bound.

## partial-Q-R

Q(f)<=R(f) in the standard bit-query model.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Promise-valid elementary derivation; docs/partial-functions.md.
- Proof: A quantum algorithm can simulate classical randomness and queries.

Applies to weak promise certificates and unrestricted promise degree; it does not import a total-function certificate-product bound.

## partial-Q-QE

Q(f)<=QE(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Promise-valid elementary derivation; docs/partial-functions.md.
- Proof: An exact algorithm is a bounded-error algorithm.

Applies to weak promise certificates and unrestricted promise degree; it does not import a total-function certificate-product bound.

## partial-QE-D

QE(f)<=D(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Promise-valid elementary derivation; docs/partial-functions.md.
- Proof: Simulate the deterministic tree reversibly.

Applies to weak promise certificates and unrestricted promise degree; it does not import a total-function certificate-product bound.

## partial-C-R0

C(f)<=R0(f) for weak promise certificates.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Promise-valid elementary derivation; docs/partial-functions.md.
- Proof: Every terminating zero-error path identifies the output on the promise, hence contains a weak certificate; its length is at least C(f,x) at each x.

Applies to weak promise certificates and unrestricted promise degree; it does not import a total-function certificate-product bound.

## partial-RC-C

RC(f)<=C(f), under the stated verification convention.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Promise-valid elementary derivation; docs/partial-functions.md.
- Proof: Read a smallest certificate for the fixed target input and reject a mismatch.

Applies to weak promise certificates and unrestricted promise degree; it does not import a total-function certificate-product bound.

## partial-bs-RC

bs(f)=O(RC(f)).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Promise-valid elementary derivation; docs/partial-functions.md.
- Proof: A successful verifier must hit each sensitive disjoint block with constant probability; sum the expected query indicators.

Applies to weak promise certificates and unrestricted promise degree; it does not import a total-function certificate-product bound.

## partial-s-bs

s(f)<=bs(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Promise-valid elementary derivation; docs/partial-functions.md.
- Proof: Each sensitive bit is a disjoint sensitive singleton block.

Applies to weak promise certificates and unrestricted promise degree; it does not import a total-function certificate-product bound.

## partial-lambda-s

lambda(f)<=s(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Promise-valid elementary derivation; docs/partial-functions.md.
- Proof: The promised sensitivity graph has maximum degree s; its adjacency norm is at most its maximum degree.

Applies to weak promise certificates and unrestricted promise degree; it does not import a total-function certificate-product bound.

## partial-s-lambda2

s(f)<=lambda(f)^2.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Promise-valid elementary derivation; docs/partial-functions.md.
- Proof: A vertex with s sensitive neighbors gives a star subgraph with adjacency norm sqrt(s).

Applies to weak promise certificates and unrestricted promise degree; it does not import a total-function certificate-product bound.

## partial-adeg-deg

adeg(f)<=deg(f) for unrestricted promise polynomials.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Promise-valid elementary derivation; docs/partial-functions.md.
- Proof: An exact interpolant is also an approximant.

Applies to weak promise certificates and unrestricted promise degree; it does not import a total-function certificate-product bound.

## partial-adeg-R

adeg(f)<=R(f) for fixed worst-case query cap.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Promise-valid elementary derivation; docs/partial-functions.md.
- Proof: The acceptance probability of a randomized depth-T decision tree is a polynomial of degree at most T; average its leaf conjunctions.

Applies to weak promise certificates and unrestricted promise degree; it does not import a total-function certificate-product bound.

## partial-deg-QE

deg(f)<=2 QE(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Promise-valid elementary derivation; docs/partial-functions.md.
- Proof: The acceptance probability of a T-query exact quantum algorithm is degree at most 2T and equals f on its promise.

Applies to weak promise certificates and unrestricted promise degree; it does not import a total-function certificate-product bound.

## partial-adeg-Q

adeg(f)<=2 Q(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Promise-valid elementary derivation; docs/partial-functions.md.
- Proof: The same acceptance polynomial approximates f on the promise.

Applies to weak promise certificates and unrestricted promise degree; it does not import a total-function certificate-product bound.

## partial-RC-R

RC(f)=O(R(f)).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Promise-valid elementary derivation; docs/partial-functions.md.
- Proof: For a fixed target x, repeat a bounded-error decision algorithm a constant number of times, replay its paths using x, and reject when an actual queried bit disagrees. Distinguishability of opposite outputs forces constant probability of finding a mismatch; accept x with certainty.

Applies to weak promise certificates and unrestricted promise degree; it does not import a total-function certificate-product bound.

## partial-RC-Q2

RC(f)=O(Q(f)^2).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Promise-valid elementary derivation; docs/partial-functions.md.
- Proof: At a fixed target x, the quantum hybrid argument gives a fractional certificate of weight O(T^2). Sampling that fractional certificate a constant number of times yields a target verifier.

Applies to weak promise certificates and unrestricted promise degree; it does not import a total-function certificate-product bound.

## partial-lambda-Q

lambda(f)=O(Q(f)).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Promise-valid elementary derivation; docs/partial-functions.md.
- Proof: Use the promised sensitivity adjacency matrix as a positive adversary matrix; each coordinate-filtered matrix is a matching with norm at most one.

Applies to weak promise certificates and unrestricted promise degree; it does not import a total-function certificate-product bound.

## partial-fbs-bs-n

For an n-bit partial function, fbs(f)<=sqrt(n bs(f)); the bound is asymptotically tight, with constant approaching 1.

- Kind: upper_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorems 15 and 17.
- Proof: For the upper bound, split sensitive blocks by size and construct a fractional certificate. For tightness, use lines of a finite projective plane (pairwise intersecting, uniformly incident) and OR composition.

An input-length factor is retained; this is not a pure power bound in bs.

## partial-fbs-bs-unbounded

There are partial Boolean functions with bs=1 and fbs unbounded; consequently no finite power of max(1,bs) bounds fbs.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17, take k=1.
- Proof: Use the promise consisting of the zero string and incidence vectors of lines of a finite projective plane. Two lines intersect, so bs=1. Give every line fractional weight 1/(t+1), obtaining fbs=Theta(t).

## partial-CAdv-fbs-unbounded

There are partial Boolean functions with fbs=O(1) but CAdv=Omega(n).

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorems 2 and 9.
- Proof: Promise a unique 1 and ask which half contains it. A 1-query weak certificate gives fbs<=1, whereas the complete bipartite relation between the two halves yields a linear classical adversary.

## partial-CAdv-AdvPlus2

CAdv(f)<=2 AdvPlus(f)^2 for partial Boolean functions.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [ABK21](https://doi.org/10.4230/LIPIcs.CCC.2021.30), Theorem 30.
- Proof: Apply Cauchy–Schwarz to the positive-adversary weight constraints, split each product into minimum and maximum, and bound the latter sum by twice the objective.

## partial-AdvPlus-CAdv

AdvPlus(f)<=CAdv(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [ABK21](https://doi.org/10.4230/LIPIcs.CCC.2021.30), Section 6; definitions of the two optimization problems.
- Proof: The geometric mean dominates the minimum, so every classical-adversary feasible weight scheme is positive-adversary feasible.

## partial-AdvPlus-boundedadeg2

AdvPlus(f)=O(cubeBoundedAdeg(f)^2) at fixed error below 1/2, even for partial Boolean functions.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [ABK21](https://doi.org/10.4230/LIPIcs.CCC.2021.30), Final Theorem 7; Section 6, Theorem 29 and Lemmas 26–27.
- Proof: Use a globally bounded approximant to choose a total completion; its critical fractional block sensitivity is O(degree^2). Compare that completion measure with CAdv and then positive Adv.

Global boundedness is essential. The final version repairs the Lemma 27 weight-construction typo in the inspected v1 preprint.

## partial-Q-boundeddeg-AB23

For partial Boolean functions, cubeBoundedDeg=O(log N) while Q=tildeOmega(N^(1/3)); no finite polynomial in cubeBoundedDeg upper-bounds Q.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylogarithmic.
- Source: [AB23](https://doi.org/10.4230/LIPIcs.CCC.2023.24), Corollary 2, Theorems 1, 6 and 8; definition in Section 2.1.
- Proof: Construct threshold satisfiability with a degree-nine globally bounded representing polynomial over a large alphabet. Prove a quantum lower bound for the contained tripartite shift problem using a negative-weight adversary; encode alphabet symbols in O(log N) bits.

## partial-R-QE-GS26

Extremal Forrelation has QE=1 in the paper’s joint phase-oracle convention and R=tildeOmega(N^(1/4)), for truth-table input length N=2^(n+1). A standard bit-oracle convention changes the quantum cost by at most a constant.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylogarithmic.
- Source: [GS26](https://doi.org/10.4230/LIPIcs.ITCS.2026.72), Theorem 4; Definition 3 and Section 3.2.
- Proof: One interference experiment determines the sign when the forrelation is promised to be exactly plus or minus one. For the classical lower bound, construct bent-function instances and use a linear-algebraic analysis of limited transcripts.

## relation-Adv-CAdv

Adv(S)<=CAdv(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Section 5.1, before Theorem 42.
- Proof: Use sqrt(ab)>=min(a,b) in each disjoint-valid-output constraint.

## relation-fbs-CAdv

fbs(S)<=CAdv(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Section 5.1, before Theorem 42.
- Proof: For a fixed input, the classical-adversary weights form a feasible fractional certificate against inputs with disjoint valid-output sets.

## relation-bs-fbs

bs(S)<=fbs(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Section 5.1.
- Proof: Assign unit weight to a packing of pairwise disjoint sensitive blocks.

## relation-fcbs-CAdv

fcbs(S)<=2 CAdv(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Theorem 42.
- Proof: Choose a valid-output selector using a weighted nearest critical input, then double the critical input weights to construct its fractional certificate.

## relation-CAdv-Adv2

CAdv(S)<=2 Adv(S)^2.

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Section 5.1, paragraph after Theorem 42.
- Proof: The partial-function Cauchy–Schwarz proof of ABK21 Theorem 30 uses only constrained pairs, so it extends to disjoint valid-output sets.

## relation-fcbs-adeg2

fcbs(S)=O(rel_adeg(S)^2) at fixed error below 1/2.

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Theorem 43.
- Proof: Choose the largest valid-output polynomial as selector. At a critical input its polynomial exceeds one half; reduce to the partial one-versus-rest problem and apply the bounded-polynomial fractional-sensitivity bound.

## relation-fbs-adeg2

fbs(S)=O(rel_adeg(S)^2) at fixed error below 1/2.

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Theorem 43.
- Proof: At a fixed input, sum the polynomial mass over its valid outputs. On every disjoint-output input the mass is small, yielding a bounded polynomial for a partial decision problem.

## relation-Adv-Q

Adv(S)=O(Q(S)).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Section 5.1.
- Proof: Apply the positive adversary progress argument only to inputs whose valid-output sets are disjoint.

## relation-CAdv-R

CAdv(S)=O(R(S)).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Section 5.1.
- Proof: A randomized solver distinguishes inputs with disjoint valid-output sets; its query weights satisfy the adversary constraints after constant rescaling.

## relation-adeg-CAdv-unbounded

For the total pigeonhole search problem PH_n, CAdv<=2 log(n/2) but rel_adeg=tildeOmega(n^(1/3)). Thus no finite power of CAdv, or of positive Adv, upper-bounds relation approximate degree.

- Kind: no_polynomial_bound; domain: total search_relation; classes: query_TFNP.
- Evidence: primary_statement_and_proof_route_checked; loss: polylogarithmic.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Definition 44, Lemma 45 and Theorem 46.
- Proof: Any two inputs with disjoint collision certificates differ in at least n/2 bits, so uniform weights give a logarithmic classical adversary. Symmetrize the output-polynomial system and reduce to the collision lower bound.

Collision certificates include both colliding indices and their shared values. Do not apply the decision-function inequality Adv=O(approximate-degree^2) in the reverse direction, or confuse relation polynomial systems with a single polynomial.

## partial-search-conversion-cubeBoundedAdeg

BK24 constructs partial decision functions with bounded approximate degree and two-sided conical degree O(polylog n), but Q=tildeOmega(n^(1/6)); input length is at most 2^polylog(n).

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylogarithmic.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Corollary 41 and Theorem 19.
- Proof: Index an auxiliary bit y_c by every solution certificate c. Promise that all bits y_c for certificates valid on x have the same value, and ask for that value. Polynomial systems transfer via sum_c p_c(x)y_c. In the reverse direction, measure a decision algorithm’s query register on auxiliary input all zero and verify sampled certificates. The quantum hybrid argument gives Q(search)<=tildeO(Q(decision)^3), hence the cube-root lower-bound transfer.

## partial-search-conversion-conical

BK24 constructs partial decision functions with bounded approximate degree and two-sided conical degree O(polylog n), but Q=tildeOmega(n^(1/6)); input length is at most 2^polylog(n).

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylogarithmic.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Corollary 41 and Theorem 19.
- Proof: Index an auxiliary bit y_c by every solution certificate c. Promise that all bits y_c for certificates valid on x have the same value, and ask for that value. Polynomial systems transfer via sum_c p_c(x)y_c. In the reverse direction, measure a decision algorithm’s query register on auxiliary input all zero and verify sampled certificates. The quantum hybrid argument gives Q(search)<=tildeO(Q(decision)^3), hence the cube-root lower-bound transfer.

## search-psQ-R-V

For every N-bit search relation S, psQ(S)=O((R(S)+V(S))*sqrt(N)).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [AGL26](https://doi.org/10.4230/LIPIcs.ICALP.2026.3), ICALP Theorem 5.
- Proof: Use the completeness reduction to Find1 with randomized generation and deterministic verification, then apply the O(sqrt(N)) pseudo-deterministic quantum Find1 algorithm.

This is multivariate and input-length dependent; it is excluded from scalar exponent closure. Verification cost V can be large even for a total relation.

## search-psQ-R-unbounded

AOES is a total N-bit search relation with R=O(1) and psQ=Omega(N).

- Kind: no_polynomial_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [AGL26](https://doi.org/10.4230/LIPIcs.ICALP.2026.3), ICALP Theorem 1 and Definition 22.
- Proof: The input hides a string through XOR blocks; any other string is a valid answer, so blind random output succeeds. A canonical solver can be amplified and converted into solving an XOR instance, giving the linear lower bound.

Arbitrary total relation, not a claim of a short-verification query-TFNP separation.

## search-psR-psQ-QL

QL-Estimation has R=O(1), psQ=O(log N), and psR=Omega(sqrt(N)) in its stated mixed-oracle model. The classical algorithm that is canonized uses O(log N) queries.

- Kind: no_polynomial_bound; domain: partial search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [AGL26](https://doi.org/10.4230/LIPIcs.ICALP.2026.3), ICALP Definition 36 and Theorem 37; introduction Theorem 3.
- Proof: Use Simon’s hidden period as a key selecting a canonical approximate Hamming weight. The quantum algorithm learns the key, whereas a classical canonical solver either solves Simon or stabilizes Hamming-weight estimation.

This is a promised relation with mixed alphabet queries. Bit-expanding the f oracle changes costs and must be stated explicitly.

## search-Find1-psQ

On the promise |x|>=n/2, Find1 has R=O(1) and psQ=Omega(sqrt(n)); hence it separates randomized solving from quantum canonical solving.

- Kind: no_polynomial_bound; domain: partial search_relation; classes: Find1.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36), Theorems 3, 4 and 7.
- Proof: Show any low-query quantum canonical solver for Find1 would violate a hybrid distinguishability bound; the paper also establishes completeness for search with efficient verification.

## partial-fbs-RC

For weak promise certificates, fbs(f)=FC(f)=Theta(RC(f)), including partial Boolean functions.

- Kind: theta_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, LP duality and fixed-target verifier sampling; docs/partial-functions.md.
- Proof: Fractional packing/cover LP duality gives fbs=FC. Replay a verifier on the fixed target x: its probabilities of querying coordinates, doubled, cover every opposite input because rejection requires a mismatch. Conversely, sample from a fractional certificate with a constant expected number of queries per unit total weight; every opposite input is rejected with constant probability.

This equivalence concerns fractional weak certificates, not classical CAdv. CAdv can be much larger on promises.

## promise-unbounded-D-deg-promise-unit-OR

On promise-unit-OR, D is unbounded while deg=O(1). Thus D is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-adeg-promise-unit-OR

On promise-unit-OR, D is unbounded while adeg=O(1). Thus D is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R0-deg-promise-unit-OR

On promise-unit-OR, R0 is unbounded while deg=O(1). Thus R0 is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R0-adeg-promise-unit-OR

On promise-unit-OR, R0 is unbounded while adeg=O(1). Thus R0 is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R-deg-promise-unit-OR

On promise-unit-OR, R is unbounded while deg=O(1). Thus R is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R-adeg-promise-unit-OR

On promise-unit-OR, R is unbounded while adeg=O(1). Thus R is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-C-deg-promise-unit-OR

On promise-unit-OR, C is unbounded while deg=O(1). Thus C is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-C-adeg-promise-unit-OR

On promise-unit-OR, C is unbounded while adeg=O(1). Thus C is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-RC-deg-promise-unit-OR

On promise-unit-OR, RC is unbounded while deg=O(1). Thus RC is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-RC-adeg-promise-unit-OR

On promise-unit-OR, RC is unbounded while adeg=O(1). Thus RC is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-bs-deg-promise-unit-OR

On promise-unit-OR, bs is unbounded while deg=O(1). Thus bs is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-bs-adeg-promise-unit-OR

On promise-unit-OR, bs is unbounded while adeg=O(1). Thus bs is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-s-deg-promise-unit-OR

On promise-unit-OR, s is unbounded while deg=O(1). Thus s is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-s-adeg-promise-unit-OR

On promise-unit-OR, s is unbounded while adeg=O(1). Thus s is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-lambda-deg-promise-unit-OR

On promise-unit-OR, lambda is unbounded while deg=O(1). Thus lambda is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-lambda-adeg-promise-unit-OR

On promise-unit-OR, lambda is unbounded while adeg=O(1). Thus lambda is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-Q-deg-promise-unit-OR

On promise-unit-OR, Q is unbounded while deg=O(1). Thus Q is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-Q-adeg-promise-unit-OR

On promise-unit-OR, Q is unbounded while adeg=O(1). Thus Q is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-QE-deg-promise-unit-OR

On promise-unit-OR, QE is unbounded while deg=O(1). Thus QE is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-QE-adeg-promise-unit-OR

On promise-unit-OR, QE is unbounded while adeg=O(1). Thus QE is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-s-promise-doubled-parity

On promise-doubled-parity, D is unbounded while s=O(1). Thus D is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: There are no promised pairs at Hamming distance one, hence s=lambda=0. Substitution x_(2i-1)=x_(2i)=z_i converts any interpolating/approximating polynomial to parity on m bits, giving degree m. Flip whole pairs for bs=m. One representative bit per pair supplies the classical upper bound; standard parity lower bounds and verification give linear remaining measures.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-lambda-promise-doubled-parity

On promise-doubled-parity, D is unbounded while lambda=O(1). Thus D is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: There are no promised pairs at Hamming distance one, hence s=lambda=0. Substitution x_(2i-1)=x_(2i)=z_i converts any interpolating/approximating polynomial to parity on m bits, giving degree m. Flip whole pairs for bs=m. One representative bit per pair supplies the classical upper bound; standard parity lower bounds and verification give linear remaining measures.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R0-s-promise-doubled-parity

On promise-doubled-parity, R0 is unbounded while s=O(1). Thus R0 is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: There are no promised pairs at Hamming distance one, hence s=lambda=0. Substitution x_(2i-1)=x_(2i)=z_i converts any interpolating/approximating polynomial to parity on m bits, giving degree m. Flip whole pairs for bs=m. One representative bit per pair supplies the classical upper bound; standard parity lower bounds and verification give linear remaining measures.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R0-lambda-promise-doubled-parity

On promise-doubled-parity, R0 is unbounded while lambda=O(1). Thus R0 is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: There are no promised pairs at Hamming distance one, hence s=lambda=0. Substitution x_(2i-1)=x_(2i)=z_i converts any interpolating/approximating polynomial to parity on m bits, giving degree m. Flip whole pairs for bs=m. One representative bit per pair supplies the classical upper bound; standard parity lower bounds and verification give linear remaining measures.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R-s-promise-doubled-parity

On promise-doubled-parity, R is unbounded while s=O(1). Thus R is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: There are no promised pairs at Hamming distance one, hence s=lambda=0. Substitution x_(2i-1)=x_(2i)=z_i converts any interpolating/approximating polynomial to parity on m bits, giving degree m. Flip whole pairs for bs=m. One representative bit per pair supplies the classical upper bound; standard parity lower bounds and verification give linear remaining measures.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R-lambda-promise-doubled-parity

On promise-doubled-parity, R is unbounded while lambda=O(1). Thus R is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: There are no promised pairs at Hamming distance one, hence s=lambda=0. Substitution x_(2i-1)=x_(2i)=z_i converts any interpolating/approximating polynomial to parity on m bits, giving degree m. Flip whole pairs for bs=m. One representative bit per pair supplies the classical upper bound; standard parity lower bounds and verification give linear remaining measures.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-C-s-promise-doubled-parity

On promise-doubled-parity, C is unbounded while s=O(1). Thus C is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: There are no promised pairs at Hamming distance one, hence s=lambda=0. Substitution x_(2i-1)=x_(2i)=z_i converts any interpolating/approximating polynomial to parity on m bits, giving degree m. Flip whole pairs for bs=m. One representative bit per pair supplies the classical upper bound; standard parity lower bounds and verification give linear remaining measures.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-C-lambda-promise-doubled-parity

On promise-doubled-parity, C is unbounded while lambda=O(1). Thus C is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: There are no promised pairs at Hamming distance one, hence s=lambda=0. Substitution x_(2i-1)=x_(2i)=z_i converts any interpolating/approximating polynomial to parity on m bits, giving degree m. Flip whole pairs for bs=m. One representative bit per pair supplies the classical upper bound; standard parity lower bounds and verification give linear remaining measures.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-RC-s-promise-doubled-parity

On promise-doubled-parity, RC is unbounded while s=O(1). Thus RC is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: There are no promised pairs at Hamming distance one, hence s=lambda=0. Substitution x_(2i-1)=x_(2i)=z_i converts any interpolating/approximating polynomial to parity on m bits, giving degree m. Flip whole pairs for bs=m. One representative bit per pair supplies the classical upper bound; standard parity lower bounds and verification give linear remaining measures.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-RC-lambda-promise-doubled-parity

On promise-doubled-parity, RC is unbounded while lambda=O(1). Thus RC is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: There are no promised pairs at Hamming distance one, hence s=lambda=0. Substitution x_(2i-1)=x_(2i)=z_i converts any interpolating/approximating polynomial to parity on m bits, giving degree m. Flip whole pairs for bs=m. One representative bit per pair supplies the classical upper bound; standard parity lower bounds and verification give linear remaining measures.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-bs-s-promise-doubled-parity

On promise-doubled-parity, bs is unbounded while s=O(1). Thus bs is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: There are no promised pairs at Hamming distance one, hence s=lambda=0. Substitution x_(2i-1)=x_(2i)=z_i converts any interpolating/approximating polynomial to parity on m bits, giving degree m. Flip whole pairs for bs=m. One representative bit per pair supplies the classical upper bound; standard parity lower bounds and verification give linear remaining measures.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-bs-lambda-promise-doubled-parity

On promise-doubled-parity, bs is unbounded while lambda=O(1). Thus bs is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: There are no promised pairs at Hamming distance one, hence s=lambda=0. Substitution x_(2i-1)=x_(2i)=z_i converts any interpolating/approximating polynomial to parity on m bits, giving degree m. Flip whole pairs for bs=m. One representative bit per pair supplies the classical upper bound; standard parity lower bounds and verification give linear remaining measures.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-QE-s-promise-doubled-parity

On promise-doubled-parity, QE is unbounded while s=O(1). Thus QE is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: There are no promised pairs at Hamming distance one, hence s=lambda=0. Substitution x_(2i-1)=x_(2i)=z_i converts any interpolating/approximating polynomial to parity on m bits, giving degree m. Flip whole pairs for bs=m. One representative bit per pair supplies the classical upper bound; standard parity lower bounds and verification give linear remaining measures.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-QE-lambda-promise-doubled-parity

On promise-doubled-parity, QE is unbounded while lambda=O(1). Thus QE is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: There are no promised pairs at Hamming distance one, hence s=lambda=0. Substitution x_(2i-1)=x_(2i)=z_i converts any interpolating/approximating polynomial to parity on m bits, giving degree m. Flip whole pairs for bs=m. One representative bit per pair supplies the classical upper bound; standard parity lower bounds and verification give linear remaining measures.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-deg-s-promise-doubled-parity

On promise-doubled-parity, deg is unbounded while s=O(1). Thus deg is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: There are no promised pairs at Hamming distance one, hence s=lambda=0. Substitution x_(2i-1)=x_(2i)=z_i converts any interpolating/approximating polynomial to parity on m bits, giving degree m. Flip whole pairs for bs=m. One representative bit per pair supplies the classical upper bound; standard parity lower bounds and verification give linear remaining measures.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-deg-lambda-promise-doubled-parity

On promise-doubled-parity, deg is unbounded while lambda=O(1). Thus deg is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: There are no promised pairs at Hamming distance one, hence s=lambda=0. Substitution x_(2i-1)=x_(2i)=z_i converts any interpolating/approximating polynomial to parity on m bits, giving degree m. Flip whole pairs for bs=m. One representative bit per pair supplies the classical upper bound; standard parity lower bounds and verification give linear remaining measures.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-Q-s-promise-doubled-parity

On promise-doubled-parity, Q is unbounded while s=O(1). Thus Q is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: There are no promised pairs at Hamming distance one, hence s=lambda=0. Substitution x_(2i-1)=x_(2i)=z_i converts any interpolating/approximating polynomial to parity on m bits, giving degree m. Flip whole pairs for bs=m. One representative bit per pair supplies the classical upper bound; standard parity lower bounds and verification give linear remaining measures.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-Q-lambda-promise-doubled-parity

On promise-doubled-parity, Q is unbounded while lambda=O(1). Thus Q is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: There are no promised pairs at Hamming distance one, hence s=lambda=0. Substitution x_(2i-1)=x_(2i)=z_i converts any interpolating/approximating polynomial to parity on m bits, giving degree m. Flip whole pairs for bs=m. One representative bit per pair supplies the classical upper bound; standard parity lower bounds and verification give linear remaining measures.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-adeg-s-promise-doubled-parity

On promise-doubled-parity, adeg is unbounded while s=O(1). Thus adeg is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: There are no promised pairs at Hamming distance one, hence s=lambda=0. Substitution x_(2i-1)=x_(2i)=z_i converts any interpolating/approximating polynomial to parity on m bits, giving degree m. Flip whole pairs for bs=m. One representative bit per pair supplies the classical upper bound; standard parity lower bounds and verification give linear remaining measures.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-adeg-lambda-promise-doubled-parity

On promise-doubled-parity, adeg is unbounded while lambda=O(1). Thus adeg is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: There are no promised pairs at Hamming distance one, hence s=lambda=0. Substitution x_(2i-1)=x_(2i)=z_i converts any interpolating/approximating polynomial to parity on m bits, giving degree m. Flip whole pairs for bs=m. One representative bit per pair supplies the classical upper bound; standard parity lower bounds and verification give linear remaining measures.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-R0-promise-dense-two-axes

On promise-dense-two-axes, D is unbounded while R0=O(1). Thus D is not O(max(1,R0)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-R-promise-dense-two-axes

On promise-dense-two-axes, D is unbounded while R=O(1). Thus D is not O(max(1,R)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-C-promise-dense-two-axes

On promise-dense-two-axes, D is unbounded while C=O(1). Thus D is not O(max(1,C)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-RC-promise-dense-two-axes

On promise-dense-two-axes, D is unbounded while RC=O(1). Thus D is not O(max(1,RC)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-bs-promise-dense-two-axes

On promise-dense-two-axes, D is unbounded while bs=O(1). Thus D is not O(max(1,bs)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-s-promise-dense-two-axes

On promise-dense-two-axes, D is unbounded while s=O(1). Thus D is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-lambda-promise-dense-two-axes

On promise-dense-two-axes, D is unbounded while lambda=O(1). Thus D is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-Q-promise-dense-two-axes

On promise-dense-two-axes, D is unbounded while Q=O(1). Thus D is not O(max(1,Q)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-adeg-promise-dense-two-axes

On promise-dense-two-axes, D is unbounded while adeg=O(1). Thus D is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-QE-R0-promise-dense-two-axes

On promise-dense-two-axes, QE is unbounded while R0=O(1). Thus QE is not O(max(1,R0)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-QE-R-promise-dense-two-axes

On promise-dense-two-axes, QE is unbounded while R=O(1). Thus QE is not O(max(1,R)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-QE-C-promise-dense-two-axes

On promise-dense-two-axes, QE is unbounded while C=O(1). Thus QE is not O(max(1,C)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-QE-RC-promise-dense-two-axes

On promise-dense-two-axes, QE is unbounded while RC=O(1). Thus QE is not O(max(1,RC)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-QE-bs-promise-dense-two-axes

On promise-dense-two-axes, QE is unbounded while bs=O(1). Thus QE is not O(max(1,bs)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-QE-s-promise-dense-two-axes

On promise-dense-two-axes, QE is unbounded while s=O(1). Thus QE is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-QE-lambda-promise-dense-two-axes

On promise-dense-two-axes, QE is unbounded while lambda=O(1). Thus QE is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-QE-Q-promise-dense-two-axes

On promise-dense-two-axes, QE is unbounded while Q=O(1). Thus QE is not O(max(1,Q)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-QE-adeg-promise-dense-two-axes

On promise-dense-two-axes, QE is unbounded while adeg=O(1). Thus QE is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-deg-R0-promise-dense-two-axes

On promise-dense-two-axes, deg is unbounded while R0=O(1). Thus deg is not O(max(1,R0)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-deg-R-promise-dense-two-axes

On promise-dense-two-axes, deg is unbounded while R=O(1). Thus deg is not O(max(1,R)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-deg-C-promise-dense-two-axes

On promise-dense-two-axes, deg is unbounded while C=O(1). Thus deg is not O(max(1,C)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-deg-RC-promise-dense-two-axes

On promise-dense-two-axes, deg is unbounded while RC=O(1). Thus deg is not O(max(1,RC)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-deg-bs-promise-dense-two-axes

On promise-dense-two-axes, deg is unbounded while bs=O(1). Thus deg is not O(max(1,bs)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-deg-s-promise-dense-two-axes

On promise-dense-two-axes, deg is unbounded while s=O(1). Thus deg is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-deg-lambda-promise-dense-two-axes

On promise-dense-two-axes, deg is unbounded while lambda=O(1). Thus deg is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-deg-Q-promise-dense-two-axes

On promise-dense-two-axes, deg is unbounded while Q=O(1). Thus deg is not O(max(1,Q)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-deg-adeg-promise-dense-two-axes

On promise-dense-two-axes, deg is unbounded while adeg=O(1). Thus deg is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Each promised input has a one-bit weak certificate: any of its 1 positions identifies the half. Sampling uniformly until a 1 is found is zero-error and uses at most four queries in expectation, so R0,R,Q,RC,bs are O(1). There are no opposite-output adjacent inputs. To lower-bound exact degree, symmetrize p(a,0) and p(0,b) separately. If degree is less than floor(m/2)+1, the first univariate polynomial is identically its required constant and the second is identically the other constant, because both agree at at least floor(m/2)+1 consecutive weights. Their values at zero must agree, a contradiction. Thus deg=Omega(m), QE>=deg/2, and D>=deg. Deterministic evaluation gives O(m) upper bounds.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-C-promise-nonempty-two-axes

On promise-nonempty-two-axes, D is unbounded while C=O(1). Thus D is not O(max(1,C)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-RC-promise-nonempty-two-axes

On promise-nonempty-two-axes, D is unbounded while RC=O(1). Thus D is not O(max(1,RC)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-bs-promise-nonempty-two-axes

On promise-nonempty-two-axes, D is unbounded while bs=O(1). Thus D is not O(max(1,bs)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-s-promise-nonempty-two-axes

On promise-nonempty-two-axes, D is unbounded while s=O(1). Thus D is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-lambda-promise-nonempty-two-axes

On promise-nonempty-two-axes, D is unbounded while lambda=O(1). Thus D is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-QE-C-promise-nonempty-two-axes

On promise-nonempty-two-axes, QE is unbounded while C=O(1). Thus QE is not O(max(1,C)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-QE-RC-promise-nonempty-two-axes

On promise-nonempty-two-axes, QE is unbounded while RC=O(1). Thus QE is not O(max(1,RC)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-QE-bs-promise-nonempty-two-axes

On promise-nonempty-two-axes, QE is unbounded while bs=O(1). Thus QE is not O(max(1,bs)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-QE-s-promise-nonempty-two-axes

On promise-nonempty-two-axes, QE is unbounded while s=O(1). Thus QE is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-QE-lambda-promise-nonempty-two-axes

On promise-nonempty-two-axes, QE is unbounded while lambda=O(1). Thus QE is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-deg-C-promise-nonempty-two-axes

On promise-nonempty-two-axes, deg is unbounded while C=O(1). Thus deg is not O(max(1,C)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-deg-RC-promise-nonempty-two-axes

On promise-nonempty-two-axes, deg is unbounded while RC=O(1). Thus deg is not O(max(1,RC)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-deg-bs-promise-nonempty-two-axes

On promise-nonempty-two-axes, deg is unbounded while bs=O(1). Thus deg is not O(max(1,bs)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-deg-s-promise-nonempty-two-axes

On promise-nonempty-two-axes, deg is unbounded while s=O(1). Thus deg is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-deg-lambda-promise-nonempty-two-axes

On promise-nonempty-two-axes, deg is unbounded while lambda=O(1). Thus deg is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-Q-C-promise-nonempty-two-axes

On promise-nonempty-two-axes, Q is unbounded while C=O(1). Thus Q is not O(max(1,C)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-Q-RC-promise-nonempty-two-axes

On promise-nonempty-two-axes, Q is unbounded while RC=O(1). Thus Q is not O(max(1,RC)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-Q-bs-promise-nonempty-two-axes

On promise-nonempty-two-axes, Q is unbounded while bs=O(1). Thus Q is not O(max(1,bs)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-Q-s-promise-nonempty-two-axes

On promise-nonempty-two-axes, Q is unbounded while s=O(1). Thus Q is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-Q-lambda-promise-nonempty-two-axes

On promise-nonempty-two-axes, Q is unbounded while lambda=O(1). Thus Q is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-adeg-C-promise-nonempty-two-axes

On promise-nonempty-two-axes, adeg is unbounded while C=O(1). Thus adeg is not O(max(1,C)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-adeg-RC-promise-nonempty-two-axes

On promise-nonempty-two-axes, adeg is unbounded while RC=O(1). Thus adeg is not O(max(1,RC)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-adeg-bs-promise-nonempty-two-axes

On promise-nonempty-two-axes, adeg is unbounded while bs=O(1). Thus adeg is not O(max(1,bs)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-adeg-s-promise-nonempty-two-axes

On promise-nonempty-two-axes, adeg is unbounded while s=O(1). Thus adeg is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-adeg-lambda-promise-nonempty-two-axes

On promise-nonempty-two-axes, adeg is unbounded while lambda=O(1). Thus adeg is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: Again C=RC=fbs=bs=1 and s=lambda=0. If p approximates the side label on the promise, amplify it on its two promised ranges to error 1/12 using a constant-degree polynomial. Then q(z)=p(0,z)-p(z,0), with sign chosen for the label convention, is zero at z=0 and within 1/6 of 1 for every nonzero z. It approximates total OR, so degree(p)=Omega(sqrt(m)). A bounded-error algorithm searches for a marked bit; the lower bound follows from this degree argument. Linear exact degree follows because the restrictions p(a,0) and p(0,b) would otherwise force incompatible values at their common origin.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-bs-promise-projective-plane

On promise-projective-plane, D is unbounded while bs=O(1). Thus D is not O(max(1,bs)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-s-promise-projective-plane

On promise-projective-plane, D is unbounded while s=O(1). Thus D is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-lambda-promise-projective-plane

On promise-projective-plane, D is unbounded while lambda=O(1). Thus D is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-deg-promise-projective-plane

On promise-projective-plane, D is unbounded while deg=O(1). Thus D is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-adeg-promise-projective-plane

On promise-projective-plane, D is unbounded while adeg=O(1). Thus D is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R0-bs-promise-projective-plane

On promise-projective-plane, R0 is unbounded while bs=O(1). Thus R0 is not O(max(1,bs)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R0-s-promise-projective-plane

On promise-projective-plane, R0 is unbounded while s=O(1). Thus R0 is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R0-lambda-promise-projective-plane

On promise-projective-plane, R0 is unbounded while lambda=O(1). Thus R0 is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R0-deg-promise-projective-plane

On promise-projective-plane, R0 is unbounded while deg=O(1). Thus R0 is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R0-adeg-promise-projective-plane

On promise-projective-plane, R0 is unbounded while adeg=O(1). Thus R0 is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R-bs-promise-projective-plane

On promise-projective-plane, R is unbounded while bs=O(1). Thus R is not O(max(1,bs)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R-s-promise-projective-plane

On promise-projective-plane, R is unbounded while s=O(1). Thus R is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R-lambda-promise-projective-plane

On promise-projective-plane, R is unbounded while lambda=O(1). Thus R is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R-deg-promise-projective-plane

On promise-projective-plane, R is unbounded while deg=O(1). Thus R is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R-adeg-promise-projective-plane

On promise-projective-plane, R is unbounded while adeg=O(1). Thus R is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-C-bs-promise-projective-plane

On promise-projective-plane, C is unbounded while bs=O(1). Thus C is not O(max(1,bs)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-C-s-promise-projective-plane

On promise-projective-plane, C is unbounded while s=O(1). Thus C is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-C-lambda-promise-projective-plane

On promise-projective-plane, C is unbounded while lambda=O(1). Thus C is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-C-deg-promise-projective-plane

On promise-projective-plane, C is unbounded while deg=O(1). Thus C is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-C-adeg-promise-projective-plane

On promise-projective-plane, C is unbounded while adeg=O(1). Thus C is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-RC-bs-promise-projective-plane

On promise-projective-plane, RC is unbounded while bs=O(1). Thus RC is not O(max(1,bs)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-RC-s-promise-projective-plane

On promise-projective-plane, RC is unbounded while s=O(1). Thus RC is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-RC-lambda-promise-projective-plane

On promise-projective-plane, RC is unbounded while lambda=O(1). Thus RC is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-RC-deg-promise-projective-plane

On promise-projective-plane, RC is unbounded while deg=O(1). Thus RC is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-RC-adeg-promise-projective-plane

On promise-projective-plane, RC is unbounded while adeg=O(1). Thus RC is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17 with k=1; LP/verifier and fixed-line consequences derived here.
- Proof: Any two lines intersect, so bs=1. Put weight 1/(t+1) on every line to obtain fbs=Theta(t), hence RC=Theta(t). A fixed line meets all lines, so querying its t+1 points decides the problem, and yields C,D,R,R0=O(t); C,RC lower bounds give matching growth. Lines have weight t+1, so unrestricted degree is one. Promised opposite pairs are never adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R-QE-promise-extremal-forrelation

On promise-extremal-forrelation, R is unbounded while QE=O(1). Thus R is not O(max(1,QE)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [GS26](https://doi.org/10.4230/LIPIcs.ITCS.2026.72), Theorem 4.
- Proof: Use GS26 Theorem 4. Exact quantum cost is constant in standard bit-oracle conventions, while R=tildeOmega(m^(1/4)). The logarithmic loss does not affect the unboundedness consequence used here.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R-Q-promise-extremal-forrelation

On promise-extremal-forrelation, R is unbounded while Q=O(1). Thus R is not O(max(1,Q)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [GS26](https://doi.org/10.4230/LIPIcs.ITCS.2026.72), Theorem 4.
- Proof: Use GS26 Theorem 4. Exact quantum cost is constant in standard bit-oracle conventions, while R=tildeOmega(m^(1/4)). The logarithmic loss does not affect the unboundedness consequence used here.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R-deg-promise-extremal-forrelation

On promise-extremal-forrelation, R is unbounded while deg=O(1). Thus R is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [GS26](https://doi.org/10.4230/LIPIcs.ITCS.2026.72), Theorem 4.
- Proof: Use GS26 Theorem 4. Exact quantum cost is constant in standard bit-oracle conventions, while R=tildeOmega(m^(1/4)). The logarithmic loss does not affect the unboundedness consequence used here.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R-adeg-promise-extremal-forrelation

On promise-extremal-forrelation, R is unbounded while adeg=O(1). Thus R is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [GS26](https://doi.org/10.4230/LIPIcs.ITCS.2026.72), Theorem 4.
- Proof: Use GS26 Theorem 4. Exact quantum cost is constant in standard bit-oracle conventions, while R=tildeOmega(m^(1/4)). The logarithmic loss does not affect the unboundedness consequence used here.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R0-QE-promise-extremal-forrelation

On promise-extremal-forrelation, R0 is unbounded while QE=O(1). Thus R0 is not O(max(1,QE)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [GS26](https://doi.org/10.4230/LIPIcs.ITCS.2026.72), Theorem 4.
- Proof: Use GS26 Theorem 4. Exact quantum cost is constant in standard bit-oracle conventions, while R=tildeOmega(m^(1/4)). The logarithmic loss does not affect the unboundedness consequence used here.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R0-Q-promise-extremal-forrelation

On promise-extremal-forrelation, R0 is unbounded while Q=O(1). Thus R0 is not O(max(1,Q)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [GS26](https://doi.org/10.4230/LIPIcs.ITCS.2026.72), Theorem 4.
- Proof: Use GS26 Theorem 4. Exact quantum cost is constant in standard bit-oracle conventions, while R=tildeOmega(m^(1/4)). The logarithmic loss does not affect the unboundedness consequence used here.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R0-deg-promise-extremal-forrelation

On promise-extremal-forrelation, R0 is unbounded while deg=O(1). Thus R0 is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [GS26](https://doi.org/10.4230/LIPIcs.ITCS.2026.72), Theorem 4.
- Proof: Use GS26 Theorem 4. Exact quantum cost is constant in standard bit-oracle conventions, while R=tildeOmega(m^(1/4)). The logarithmic loss does not affect the unboundedness consequence used here.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R0-adeg-promise-extremal-forrelation

On promise-extremal-forrelation, R0 is unbounded while adeg=O(1). Thus R0 is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [GS26](https://doi.org/10.4230/LIPIcs.ITCS.2026.72), Theorem 4.
- Proof: Use GS26 Theorem 4. Exact quantum cost is constant in standard bit-oracle conventions, while R=tildeOmega(m^(1/4)). The logarithmic loss does not affect the unboundedness consequence used here.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-QE-promise-extremal-forrelation

On promise-extremal-forrelation, D is unbounded while QE=O(1). Thus D is not O(max(1,QE)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [GS26](https://doi.org/10.4230/LIPIcs.ITCS.2026.72), Theorem 4.
- Proof: Use GS26 Theorem 4. Exact quantum cost is constant in standard bit-oracle conventions, while R=tildeOmega(m^(1/4)). The logarithmic loss does not affect the unboundedness consequence used here.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-Q-promise-extremal-forrelation

On promise-extremal-forrelation, D is unbounded while Q=O(1). Thus D is not O(max(1,Q)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [GS26](https://doi.org/10.4230/LIPIcs.ITCS.2026.72), Theorem 4.
- Proof: Use GS26 Theorem 4. Exact quantum cost is constant in standard bit-oracle conventions, while R=tildeOmega(m^(1/4)). The logarithmic loss does not affect the unboundedness consequence used here.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-deg-promise-extremal-forrelation

On promise-extremal-forrelation, D is unbounded while deg=O(1). Thus D is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [GS26](https://doi.org/10.4230/LIPIcs.ITCS.2026.72), Theorem 4.
- Proof: Use GS26 Theorem 4. Exact quantum cost is constant in standard bit-oracle conventions, while R=tildeOmega(m^(1/4)). The logarithmic loss does not affect the unboundedness consequence used here.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-adeg-promise-extremal-forrelation

On promise-extremal-forrelation, D is unbounded while adeg=O(1). Thus D is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [GS26](https://doi.org/10.4230/LIPIcs.ITCS.2026.72), Theorem 4.
- Proof: Use GS26 Theorem 4. Exact quantum cost is constant in standard bit-oracle conventions, while R=tildeOmega(m^(1/4)). The logarithmic loss does not affect the unboundedness consequence used here.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-R-promise-restricted-DJ

On promise-restricted-DJ, D is unbounded while R=O(1). Thus D is not O(max(1,R)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-D-RC-promise-restricted-DJ

On promise-restricted-DJ, D is unbounded while RC=O(1). Thus D is not O(max(1,RC)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-D-bs-promise-restricted-DJ

On promise-restricted-DJ, D is unbounded while bs=O(1). Thus D is not O(max(1,bs)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-D-s-promise-restricted-DJ

On promise-restricted-DJ, D is unbounded while s=O(1). Thus D is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-D-lambda-promise-restricted-DJ

On promise-restricted-DJ, D is unbounded while lambda=O(1). Thus D is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-D-Q-promise-restricted-DJ

On promise-restricted-DJ, D is unbounded while Q=O(1). Thus D is not O(max(1,Q)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-D-QE-promise-restricted-DJ

On promise-restricted-DJ, D is unbounded while QE=O(1). Thus D is not O(max(1,QE)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-D-deg-promise-restricted-DJ

On promise-restricted-DJ, D is unbounded while deg=O(1). Thus D is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-D-adeg-promise-restricted-DJ

On promise-restricted-DJ, D is unbounded while adeg=O(1). Thus D is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-R0-R-promise-restricted-DJ

On promise-restricted-DJ, R0 is unbounded while R=O(1). Thus R0 is not O(max(1,R)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-R0-RC-promise-restricted-DJ

On promise-restricted-DJ, R0 is unbounded while RC=O(1). Thus R0 is not O(max(1,RC)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-R0-bs-promise-restricted-DJ

On promise-restricted-DJ, R0 is unbounded while bs=O(1). Thus R0 is not O(max(1,bs)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-R0-s-promise-restricted-DJ

On promise-restricted-DJ, R0 is unbounded while s=O(1). Thus R0 is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-R0-lambda-promise-restricted-DJ

On promise-restricted-DJ, R0 is unbounded while lambda=O(1). Thus R0 is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-R0-Q-promise-restricted-DJ

On promise-restricted-DJ, R0 is unbounded while Q=O(1). Thus R0 is not O(max(1,Q)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-R0-QE-promise-restricted-DJ

On promise-restricted-DJ, R0 is unbounded while QE=O(1). Thus R0 is not O(max(1,QE)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-R0-deg-promise-restricted-DJ

On promise-restricted-DJ, R0 is unbounded while deg=O(1). Thus R0 is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-R0-adeg-promise-restricted-DJ

On promise-restricted-DJ, R0 is unbounded while adeg=O(1). Thus R0 is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-C-R-promise-restricted-DJ

On promise-restricted-DJ, C is unbounded while R=O(1). Thus C is not O(max(1,R)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-C-RC-promise-restricted-DJ

On promise-restricted-DJ, C is unbounded while RC=O(1). Thus C is not O(max(1,RC)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-C-bs-promise-restricted-DJ

On promise-restricted-DJ, C is unbounded while bs=O(1). Thus C is not O(max(1,bs)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-C-s-promise-restricted-DJ

On promise-restricted-DJ, C is unbounded while s=O(1). Thus C is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-C-lambda-promise-restricted-DJ

On promise-restricted-DJ, C is unbounded while lambda=O(1). Thus C is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-C-Q-promise-restricted-DJ

On promise-restricted-DJ, C is unbounded while Q=O(1). Thus C is not O(max(1,Q)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-C-QE-promise-restricted-DJ

On promise-restricted-DJ, C is unbounded while QE=O(1). Thus C is not O(max(1,QE)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-C-deg-promise-restricted-DJ

On promise-restricted-DJ, C is unbounded while deg=O(1). Thus C is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-C-adeg-promise-restricted-DJ

On promise-restricted-DJ, C is unbounded while adeg=O(1). Thus C is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository derivation.
- Proof: The phase-query algorithm prepares the uniform state, applies phases (-1)^x_i and tests overlap with the uniform state. Its amplitude is 1 at zero and 0 on balanced inputs, hence QE=1. A weak certificate for zero needs m/2+1 zero positions, so C,D,R0=Theta(m). Random sampling gives R,RC=O(1); at zero exactly two disjoint half-size sensitive blocks can be packed, so bs=2. The promise has no opposite-output adjacent pair for m>=4. The unrestricted polynomial 2 sum_i x_i/m is exact of degree one.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument. The one-query circuit here is explicitly derived; DJ92 is the historical problem citation, not an audited original one-query attribution.

## promise-unbounded-D-C-promise-unique-mark-color

On promise-unique-mark-color, D is unbounded while C=O(1). Thus D is not O(max(1,C)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-RC-promise-unique-mark-color

On promise-unique-mark-color, D is unbounded while RC=O(1). Thus D is not O(max(1,RC)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-bs-promise-unique-mark-color

On promise-unique-mark-color, D is unbounded while bs=O(1). Thus D is not O(max(1,bs)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-s-promise-unique-mark-color

On promise-unique-mark-color, D is unbounded while s=O(1). Thus D is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-lambda-promise-unique-mark-color

On promise-unique-mark-color, D is unbounded while lambda=O(1). Thus D is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-deg-promise-unique-mark-color

On promise-unique-mark-color, D is unbounded while deg=O(1). Thus D is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-D-adeg-promise-unique-mark-color

On promise-unique-mark-color, D is unbounded while adeg=O(1). Thus D is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R0-C-promise-unique-mark-color

On promise-unique-mark-color, R0 is unbounded while C=O(1). Thus R0 is not O(max(1,C)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R0-RC-promise-unique-mark-color

On promise-unique-mark-color, R0 is unbounded while RC=O(1). Thus R0 is not O(max(1,RC)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R0-bs-promise-unique-mark-color

On promise-unique-mark-color, R0 is unbounded while bs=O(1). Thus R0 is not O(max(1,bs)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R0-s-promise-unique-mark-color

On promise-unique-mark-color, R0 is unbounded while s=O(1). Thus R0 is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R0-lambda-promise-unique-mark-color

On promise-unique-mark-color, R0 is unbounded while lambda=O(1). Thus R0 is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R0-deg-promise-unique-mark-color

On promise-unique-mark-color, R0 is unbounded while deg=O(1). Thus R0 is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R0-adeg-promise-unique-mark-color

On promise-unique-mark-color, R0 is unbounded while adeg=O(1). Thus R0 is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R-C-promise-unique-mark-color

On promise-unique-mark-color, R is unbounded while C=O(1). Thus R is not O(max(1,C)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R-RC-promise-unique-mark-color

On promise-unique-mark-color, R is unbounded while RC=O(1). Thus R is not O(max(1,RC)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R-bs-promise-unique-mark-color

On promise-unique-mark-color, R is unbounded while bs=O(1). Thus R is not O(max(1,bs)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R-s-promise-unique-mark-color

On promise-unique-mark-color, R is unbounded while s=O(1). Thus R is not O(max(1,s)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R-lambda-promise-unique-mark-color

On promise-unique-mark-color, R is unbounded while lambda=O(1). Thus R is not O(max(1,lambda)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R-deg-promise-unique-mark-color

On promise-unique-mark-color, R is unbounded while deg=O(1). Thus R is not O(max(1,deg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## promise-unbounded-R-adeg-promise-unique-mark-color

On promise-unique-mark-color, R is unbounded while adeg=O(1). Thus R is not O(max(1,adeg)^p) for any fixed finite p over partial Boolean functions.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9 and its proof.
- Proof: A one-bit weak certificate reads the marked position, so C=RC=fbs=bs=1. AKPVZ18 Theorem 9 uses the complete bipartite relation between the two halves to prove classical adversary Omega(m), hence R=Omega(m), and R0,D are at least as large. Scanning all coordinates gives matching upper bounds. The sum of the second-half input bits is an exact unrestricted degree-one polynomial. No two promised inputs are adjacent.

This consequence uses weak promise certificates and unrestricted promise degree. It does not extend to globally bounded degree without a separate argument.

## partial-cfbs-CAdv

cfbs(f)<=2 CAdv(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [ABK21](https://doi.org/10.4230/LIPIcs.CCC.2021.30), Final Lemma 26.
- Proof: Choose a total Boolean completion by a weighted nearest original promised input. Doubling the original target weights covers every sensitive block of that completion at the original target.

## partial-CAdv-cfbs

CAdv(f)<=cfbs(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [ABK21](https://doi.org/10.4230/LIPIcs.CCC.2021.30), Final Lemma 27, attributed to Krišjānis Prūsis.
- Proof: Choose a completion attaining critical fractional block sensitivity and feasible fractional certificates at promised inputs. A coordinatewise choice of an intermediate cube input converts their coverage constraints into the classical minimum-weight constraint.

## relation-Q-R

Q(S)<=R(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Definitions of relation solvers and bounded polynomial systems; BK24 Section 2.
- Proof: Simulate a classical randomized solver on a quantum computer.

## relation-R-psR

R(S)<=psR(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Definitions of relation solvers and bounded polynomial systems; BK24 Section 2.
- Proof: A canonical valid answer is in particular a valid answer.

## relation-Q-psQ

Q(S)<=psQ(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Definitions of relation solvers and bounded polynomial systems; BK24 Section 2.
- Proof: A canonical quantum answer is in particular valid.

## relation-psQ-psR

psQ(S)<=psR(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Definitions of relation solvers and bounded polynomial systems; BK24 Section 2.
- Proof: Simulate the classical canonical solver.

## relation-psR-D

psR(S)<=D(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Definitions of relation solvers and bounded polynomial systems; BK24 Section 2.
- Proof: A deterministic solver itself chooses a canonical output.

## relation-psQ-D

psQ(S)<=D(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Definitions of relation solvers and bounded polynomial systems; BK24 Section 2.
- Proof: Simulate the deterministic solver.

## relation-adeg-conical

rel_adeg(S)<=rel_conical(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Definitions of relation solvers and bounded polynomial systems; BK24 Section 2.
- Proof: Expand each nonnegative literal conjunction into a multilinear polynomial. A width-d conical system is a globally bounded valid-output polynomial system of degree at most d.

## relation-adeg-Q

rel_adeg(S)<=2 Q(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Definitions of relation solvers and bounded polynomial systems; BK24 Section 2.
- Proof: For every output label, use its quantum acceptance polynomial. All are nonnegative on the full cube, their sum is at most one, and the valid mass is large on the promise.

## relation-cbs-fcbs

cbs(S)<=fcbs(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Definitions of relation solvers and bounded polynomial systems; BK24 Section 2.
- Proof: For each valid selector its critical block packing is bounded by its critical fractional packing; minimize over selectors.

## multi-s-bs

s(f)<=bs(f).

- Kind: upper_bound; domain: total multi_output_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Theorem 3.1 and Theorem 3.2(1), including the complete proofs.
- Proof: Singleton sensitive blocks are disjoint.

## multi-bs-R

bs(f)<=3 R(f).

- Kind: upper_bound; domain: total multi_output_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Theorem 3.1 and Theorem 3.2(1), including the complete proofs.
- Proof: Against any disjoint sensitive block, a bounded-error solver must distinguish the changed output; sum the probabilities of querying each block.

## multi-D-C2

D(f)<=C(f)^2.

- Kind: upper_bound; domain: total multi_output_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Theorem 3.1 and Theorem 3.2(1), including the complete proofs.
- Proof: Iteratively query a certificate of a consistent alternative output; the multi-output certificate argument bounds the number of stages.

## multi-D-R3

D(f)<=54 R(f)^3.

- Kind: upper_bound; domain: total multi_output_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Theorem 3.1 and Theorem 3.2(1), including the complete proofs.
- Proof: Combine D<=2 C bs, C<=s bs and s<=bs<=3R; all are proved for total multi-output functions in the full report.

## partial-quadratic-RC-Q

On the zero-or-unit-vector promise, RC=Theta(m) and Q=Theta(sqrt(m)), giving a quadratic separation.

- Kind: separation; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, promise-unit-OR; BHMT02 Theorem 4 and the star sensitivity graph.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

## partial-quadratic-RC-QE

On the zero-or-unit-vector promise, RC=Theta(m) and QE=Theta(sqrt(m)), giving a quadratic separation.

- Kind: separation; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, promise-unit-OR; BHMT02 Theorem 4 and the star sensitivity graph.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

## partial-quadratic-bs-Q

On the zero-or-unit-vector promise, bs=Theta(m) and Q=Theta(sqrt(m)), giving a quadratic separation.

- Kind: separation; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, promise-unit-OR; BHMT02 Theorem 4 and the star sensitivity graph.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

## partial-quadratic-bs-QE

On the zero-or-unit-vector promise, bs=Theta(m) and QE=Theta(sqrt(m)), giving a quadratic separation.

- Kind: separation; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, promise-unit-OR; BHMT02 Theorem 4 and the star sensitivity graph.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

## partial-quadratic-s-Q

On the zero-or-unit-vector promise, s=Theta(m) and Q=Theta(sqrt(m)), giving a quadratic separation.

- Kind: separation; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, promise-unit-OR; BHMT02 Theorem 4 and the star sensitivity graph.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

## partial-quadratic-s-QE

On the zero-or-unit-vector promise, s=Theta(m) and QE=Theta(sqrt(m)), giving a quadratic separation.

- Kind: separation; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, promise-unit-OR; BHMT02 Theorem 4 and the star sensitivity graph.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

## partial-quadratic-s-lambda

On the zero-or-unit-vector promise, s=Theta(m) and lambda=Theta(sqrt(m)), giving a quadratic separation.

- Kind: separation; domain: partial decision_function; classes: symmetric.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, promise-unit-OR; BHMT02 Theorem 4 and the star sensitivity graph.
- Proof: Unrestricted polynomial sum_i x_i is exact and has degree one. Zero requires inspecting all coordinates classically; each unit position is a disjoint sensitive singleton at zero. The sensitivity graph is a star with norm sqrt(m). Grover search gives Q=O(sqrt(m)); the star adversary gives the matching lower bound. For exact search, apply BHMT02 Theorem 4 with hypothesized marked fraction 1/m and verify the returned index. When there is one mark it is found with certainty; when there are none verification rejects. This also proves QE=O(sqrt(m)).

## search-PH-rel_adeg-rel_Adv

On total pigeonhole search, rel_adeg is at least tildeOmega(n^(1/3)) while rel_Adv=O(log n), excluding every finite polynomial upper bound.

- Kind: no_polynomial_bound; domain: total search_relation; classes: query_TFNP.
- Evidence: primary_statement_and_proof_route_checked; loss: polylogarithmic.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Definition 44, Lemma 45 and Theorem 46.
- Proof: Any two inputs with disjoint collision certificates differ in at least n/2 bits, so uniform weights give a logarithmic classical adversary. Symmetrize the output-polynomial system and reduce to the collision lower bound. Use rel_adeg<=2Q<=2R for numerator transfer and rel_Adv<=rel_CAdv for denominator transfer.

Dependencies: relation-adeg-CAdv-unbounded, relation-adeg-Q, relation-Q-R, relation-Adv-CAdv.

Collision certificates include both colliding indices and their shared values. Do not apply the decision-function inequality Adv=O(approximate-degree^2) in the reverse direction, or confuse relation polynomial systems with a single polynomial.

## search-PH-Q-rel_Adv

On total pigeonhole search, Q is at least tildeOmega(n^(1/3)) while rel_Adv=O(log n), excluding every finite polynomial upper bound.

- Kind: no_polynomial_bound; domain: total search_relation; classes: query_TFNP.
- Evidence: primary_statement_and_proof_route_checked; loss: polylogarithmic.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Definition 44, Lemma 45 and Theorem 46.
- Proof: Any two inputs with disjoint collision certificates differ in at least n/2 bits, so uniform weights give a logarithmic classical adversary. Symmetrize the output-polynomial system and reduce to the collision lower bound. Use rel_adeg<=2Q<=2R for numerator transfer and rel_Adv<=rel_CAdv for denominator transfer.

Dependencies: relation-adeg-CAdv-unbounded, relation-adeg-Q, relation-Q-R, relation-Adv-CAdv.

Collision certificates include both colliding indices and their shared values. Do not apply the decision-function inequality Adv=O(approximate-degree^2) in the reverse direction, or confuse relation polynomial systems with a single polynomial.

## search-PH-Q-rel_CAdv

On total pigeonhole search, Q is at least tildeOmega(n^(1/3)) while rel_CAdv=O(log n), excluding every finite polynomial upper bound.

- Kind: no_polynomial_bound; domain: total search_relation; classes: query_TFNP.
- Evidence: primary_statement_and_proof_route_checked; loss: polylogarithmic.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Definition 44, Lemma 45 and Theorem 46.
- Proof: Any two inputs with disjoint collision certificates differ in at least n/2 bits, so uniform weights give a logarithmic classical adversary. Symmetrize the output-polynomial system and reduce to the collision lower bound. Use rel_adeg<=2Q<=2R for numerator transfer and rel_Adv<=rel_CAdv for denominator transfer.

Dependencies: relation-adeg-CAdv-unbounded, relation-adeg-Q, relation-Q-R, relation-Adv-CAdv.

Collision certificates include both colliding indices and their shared values. Do not apply the decision-function inequality Adv=O(approximate-degree^2) in the reverse direction, or confuse relation polynomial systems with a single polynomial.

## search-PH-R-rel_Adv

On total pigeonhole search, R is at least tildeOmega(n^(1/3)) while rel_Adv=O(log n), excluding every finite polynomial upper bound.

- Kind: no_polynomial_bound; domain: total search_relation; classes: query_TFNP.
- Evidence: primary_statement_and_proof_route_checked; loss: polylogarithmic.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Definition 44, Lemma 45 and Theorem 46.
- Proof: Any two inputs with disjoint collision certificates differ in at least n/2 bits, so uniform weights give a logarithmic classical adversary. Symmetrize the output-polynomial system and reduce to the collision lower bound. Use rel_adeg<=2Q<=2R for numerator transfer and rel_Adv<=rel_CAdv for denominator transfer.

Dependencies: relation-adeg-CAdv-unbounded, relation-adeg-Q, relation-Q-R, relation-Adv-CAdv.

Collision certificates include both colliding indices and their shared values. Do not apply the decision-function inequality Adv=O(approximate-degree^2) in the reverse direction, or confuse relation polynomial systems with a single polynomial.

## search-PH-R-rel_CAdv

On total pigeonhole search, R is at least tildeOmega(n^(1/3)) while rel_CAdv=O(log n), excluding every finite polynomial upper bound.

- Kind: no_polynomial_bound; domain: total search_relation; classes: query_TFNP.
- Evidence: primary_statement_and_proof_route_checked; loss: polylogarithmic.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Definition 44, Lemma 45 and Theorem 46.
- Proof: Any two inputs with disjoint collision certificates differ in at least n/2 bits, so uniform weights give a logarithmic classical adversary. Symmetrize the output-polynomial system and reduce to the collision lower bound. Use rel_adeg<=2Q<=2R for numerator transfer and rel_Adv<=rel_CAdv for denominator transfer.

Dependencies: relation-adeg-CAdv-unbounded, relation-adeg-Q, relation-Q-R, relation-Adv-CAdv.

Collision certificates include both colliding indices and their shared values. Do not apply the decision-function inequality Adv=O(approximate-degree^2) in the reverse direction, or confuse relation polynomial systems with a single polynomial.

## search-R-conical-unbounded

There are total query-TFNP relations with rel_conical=O(polylog n) but R=tildeOmega(sqrt(n)).

- Kind: no_polynomial_bound; domain: total search_relation; classes: query_TFNP.
- Evidence: primary_statement_and_proof_route_checked; loss: see_source.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Corollaries 6 and 40.
- Proof: The low-degree witness polynomials remain conical juntas under the total-search transformation; the shifted repeated-search quantum lower bound is unchanged. A quantum lower bound also lower-bounds classical randomized query complexity.

Dependencies: search-Q-conical, relation-Q-R.

Here n is the construction parameter, not necessarily the input length. These are bounded polynomial systems and two-sided bounded conical systems.

## search-psR-R-unbounded

AOES has R=O(1) and psR=Omega(N), as psQ<=psR.

- Kind: no_polynomial_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [AGL26](https://doi.org/10.4230/LIPIcs.ICALP.2026.3), ICALP Theorem 1 and Definition 22.
- Proof: The input hides a string through XOR blocks; any other string is a valid answer, so blind random output succeeds. A canonical solver can be amplified and converted into solving an XOR instance, giving the linear lower bound.

Dependencies: search-psQ-R-unbounded, relation-psQ-psR.

Arbitrary total relation, not a claim of a short-verification query-TFNP separation.

## search-nonadaptive-derandomization

For every total search relation, Dna(S)<=3 psRna(S).

- Kind: upper_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [GGR13](https://www.wisdom.weizmann.ac.il/~oded/p_balg.html), Full report Theorem 4.1(2).
- Proof: A coordinate with query probability below one third cannot change the canonical answer. The heavy coordinates, of which there are at most 3q, therefore determine the canonical output. Nonadaptivity makes this heavy set independent of the input.

The complete proof of the multi-output bound is in the ECCC report; the proceedings omits some proofs. This cubic 2023 bound predates AGL26’s discussion of an older quartic classical bound.

## search-D-psR4-historical

The original GGR13 theorem gives D(S)=O(psR(S)^4) for total search, with an additional output-range-sensitive bound.

- Kind: upper_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [GGR13](https://www.wisdom.weizmann.ac.il/~oded/p_balg.html), Full report Theorem 4.1(3).
- Proof: Bound the range of a canonical selector in terms of query cost, encode its outputs by bits, and deterministically compute those total Boolean bits using the classical randomized-to-deterministic simulation.

Historical result; inspect superseding records before selecting a frontier.

The complete proof of the multi-output bound is in the ECCC report; the proceedings omits some proofs. This cubic 2023 bound predates AGL26’s discussion of an older quartic classical bound.

## search-ApproxHamWt-psR

Total approximate Hamming-weight search has R=O(1) and psR=Omega(n).

- Kind: no_polynomial_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [GGR13](https://www.wisdom.weizmann.ac.il/~oded/p_balg.html), Full report Corollary 4.2.
- Proof: Random sampling estimates normalized weight within constant additive error. Any valid selector must change between low and high weights. Follow a Hamming walk through coordinates preserving the canonical answer until this is impossible; the resulting input has linearly many sensitive coordinates, forcing linearly many randomized queries.

An arbitrary total relation; this is not a short-verification query-TFNP claim. GGR13 uses strict error <n/10, whereas CDM23 states the non-strict variant.

## search-log-size-ps-size

For total S subset {0,1}^n times [m], log DTSize(S)=O((log psDTSize(S))^4*(log n)^3*min(log m,log psDTSize(S))).

- Kind: upper_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_input_and_output_parameter_factors.
- Source: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Corollary 5.3, from Claim 5.1 and Theorem 5.2.
- Proof: Encode a canonical selector by output bits, bound its range using tree size, and apply the deterministic/randomized size simulation for each Boolean output bit.

Leaf counts, their logarithms, input length and output-range size are all explicit. This is not a quartic scalar power bound between the unlogged size measures. Final proceedings Theorem 4.3 corresponds to full-report Corollary 5.3.

## search-positive-AND-canonical-gap

For total approximate Hamming-weight search, RandPos=O(1) but psRandPos=Omega(n).

- Kind: no_polynomial_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Theorem 6.3, using Corollary 6.2.
- Proof: Any valid selector has input-zero sensitivity Omega(n), proved by a monotone Hamming walk. The monotone block-sensitivity lower bound for randomized positive-conjunction trees then forces linearly many queries.

Use the Omega(n) statement. The source’s proof line claiming a stronger numerical lower bound omits the factor 1/3 from its cited corollary; no such sharpened constant is imported. Final and full-report theorem numbering differ: Theorem 5.3; full report Theorem 6.3.

## search-parity-canonical-speedup

For the total SearchOR relation, Dpar=n while psRpar=O(log n log log n), excluding every finite power upper bound on Dpar in terms of psRpar.

- Kind: no_polynomial_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Theorem 6.6.
- Proof: On the all-zero answer path, fewer than n parity constraints leave a nonzero input in the same affine subspace as zero; the two inputs have disjoint valid outputs, so a deterministic tree cannot stop. For the canonical upper bound, binary search for the first 1, testing each half with O(log log n) random parity queries.

This is a parity-query separation, not a bit-query counterexample to D=O(psR^3). Final and full-report theorem numbering differ: Theorem 5.8; proof in full report Theorem 6.6.

## multi-mbs-positive-AND-R

For a multi-output function, mbs(f)<=3 RandPos(f) at error 1/3.

- Kind: upper_bound; domain: partial_or_total multi_output_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Theorem 6.1.
- Proof: Put half the input distribution on a target input and distribute half over disjoint sensitive zero-block flips. A positive-conjunction query can eliminate only a controlled number of these alternatives; a tree of depth below mbs/3 has distributional error greater than 1/3.

Here mbs is the input-zero directed block measure; it is not output-zero block sensitivity.

## size-log-derandomization

For total Boolean f on n bits, log DTSize(f)=O((log RSize(f))^4 log^3 n).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_input_length_logs.
- Source: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Theorem 3.1(b).
- Proof: Use randomized leaf size to bound the number of minimal sensitive blocks and then monochromatic cover number. Apply the cover-to-tree size simulation to get the quartic logarithmic bound.

## cover-log-RSize2

log coverN(f)=O((log RSize(f))^2 log n).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_input_length_logs.
- Source: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Theorem 3.1(a).
- Proof: First lower-bound randomized tree size by block number, then construct a small monochromatic cover from small randomized trees and the block-number estimate.

## andor-D-R4

DandOr(f)=O(RandOr(f)^4 log^7 n).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_log.
- Source: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Theorem 4.1.
- Proof: Relate AND/OR depth to log leaf size by tree balancing and expansion of subset queries, then apply logarithmic size derandomization.

## and-D-R3

DandPos(f)=O(RandPos(f)^3 log^4 n).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_log.
- Source: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Theorem 4.5.
- Proof: A small zero-answer randomized tree yields fractional hitting sets for input-zero blocks. A greedy deterministic construction shrinks monochromatic covers; the cover-number bound supplies the remaining powers.

## fmbs-zero-depth

fmbs(f)=O(RzeroDepth(f)).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Lemma 4.6.
- Proof: Turn a small zero-answer randomized tree into coordinate weights hitting every sensitive input-zero block with constant probability.

## zero-depth-D-and

DzeroDepth(f)<=DandPos(f).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Claim 2.16.
- Proof: Simulate each conjunction by querying its variables until a zero is found: each conjunction contributes at most one zero answer.

## zero-depth-R-and

RzeroDepth(f)<=RandPos(f).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Claim 2.16.
- Proof: Apply the deterministic simulation to every tree in the randomized support.

## and-zero-depth-DandPos

DandPos(f)<=DzeroDepth(f)*ceil(log_2(n+1)).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_input_length_log.
- Source: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Claim 2.16.
- Proof: Balance the search for a zero inside suitable queried sets; each zero-answer stage needs at most logarithmically many conjunction queries.

Use ceil(log_2(n+1)) for the exact factor, including n=1. The randomized version applies the deterministic transformation to every support tree.

## and-zero-depth-RandPos

RandPos(f)<=RzeroDepth(f)*ceil(log_2(n+1)).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_input_length_log.
- Source: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Claim 2.16.
- Proof: Balance the search for a zero inside suitable queried sets; each zero-answer stage needs at most logarithmically many conjunction queries.

Use ceil(log_2(n+1)) for the exact factor, including n=1. The randomized version applies the deterministic transformation to every support tree.

## andor-log-size-DandOr

log DTSize(f)/(2 log n)<=DandOr(f)<=4 log DTSize(f).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Lemma 4.2.
- Proof: For the upper bound balance a leaf-labelled tree with AND/OR queries; for the lower bound expand subset queries and count leaves. The randomized version applies the transformations to every support tree.

## andor-log-size-RandOr

log RSize(f)/(2 log n)<=RandOr(f)<=4 log RSize(f).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Lemma 4.2.
- Proof: For the upper bound balance a leaf-labelled tree with AND/OR queries; for the lower bound expand subset queries and count leaves. The randomized version applies the transformations to every support tree.

## rank-log-size-sandwich

rank(f)<=log DTSize(f)<=rank(f)*log(e n/rank(f)) for nonconstant total Boolean f.

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Proposition 2.11, citing Ehrenfeucht–Haussler 1989.
- Proof: A rank-r tree has at least 2^r leaves. Orient light/heavy branches using child ranks; at most r rank-increasing choices on any path allow the binomial leaf-count upper bound.

Original size k counts all nodes. The leaf-count formulation uses k=2L-1. Minimize each applicable bound carefully; no product of separately optimized tree parameters is inferred.

## random-rank-log-size

rrank(f)<=log RSize(f)<=rrank(f)*log(e n/rrank(f)) for nonconstant total Boolean f.

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Proposition 2.11.
- Proof: Apply the deterministic rank/size conversion separately to all trees in the support of the randomized algorithm.

## search-size-Hamming-exponential

Total ApproxHamWt has RSize=O(1) but psDTSize=exp(Omega(n)).

- Kind: no_polynomial_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), Theorem 4.6, using Theorem 4.5.
- Proof: Every canonical approximate-weight selector yields, by thresholding its output, a total completion of ApproxMaj. A corruption bound forces exponential randomized leaf size for every such completion. Constant sampling gives constant randomized solver size.

This theorem is absent from the inspected earlier ECCC report. Theorem 4.5 explicitly credits its corruption argument to Swagato Sanyal.

## search-size-CNF-random

With high probability, sufficiently dense random 3-CNF search has RSize=O(1) and psDTSize=exp(Omega(n^(1/4)/log n)).

- Kind: no_polynomial_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), Corollary 4.4.
- Proof: Combine the exponential deterministic-size lower bound for random unsatisfiable formulas with Theorem 4.3’s deterministic/canonical logarithmic-size simulation. A random clause sample solves the relation with constant depth.

A random formula is fixed to obtain a total relation on assignments. This unlifted construction is distinct from the stronger lifted family of GIPS21.

## search-andor-canonical-Hamming

Total ApproxHamWt has RandOr=O(1), psRandOr=Omega(n/log n).

- Kind: no_polynomial_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), Theorem 5.6, using Lemma 5.5 and Theorem 4.6.
- Proof: Use the syntactic equivalence of AND/OR depth and logarithmic leaf size to transfer the exponential canonical-size lower bound.

## search-derandomization-DandPos

For total S on n bits with output range [m], DandPos(S)=O(psRandPos(S)^3 log^4(n) min(log m,psRandPos(S))).

- Kind: upper_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_input_and_output_parameter_factors.
- Source: [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), Theorem 5.4.
- Proof: Encode the canonical output selector in bits, invoke the corresponding total Boolean restricted-query derandomization theorem, and bound its effective output range by its query cost.

## search-derandomization-DandOr

For total S on n bits with output range [m], DandOr(S)=O(psRandOr(S)^4 log^7(n) min(log m,psRandOr(S))).

- Kind: upper_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_input_and_output_parameter_factors.
- Source: [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), Theorem 5.7.
- Proof: Encode the canonical output selector in bits, invoke the corresponding total Boolean restricted-query derandomization theorem, and bound its effective output range by its query cost.

## search-andor-canonical-log-size

log psDTSize(S)/(2 log n)<=psRandOr(S)<=4 log psDTSize(S).

- Kind: upper_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), Lemma 5.5.
- Proof: The underlying tree transformations are syntactic and preserve output labels. Apply them to the selector attaining each canonical optimum separately.

## average-strict-zero-error-fix-coins

For finite promise domains with nonuniform trees, R0avg_mu(S)=Davg_mu(S)=psR0avg_mu(S).

- Kind: identity; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Finite-domain averaging; docs/average-cost.md.
- Proof: The event that fixed coins give a correct terminating algorithm on every promised input has probability one, because the input domain is finite. Average the mu-cost over those coins and fix a seed with cost at most the randomized average. Prune repeated queries. Deterministic algorithms are a subclass of strict Las Vegas and strict canonical zero-error algorithms.

This is a repository derivation for the explicitly strict model, not an attribution of this sharpened equality to GIPS21 or a claim of first discovery.

## average-published-zero-error-simulation

GIPS21 states deterministic simulation on average with cost O(R0avg_mu log^2 n +1), preserving correctness on the input domain.

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_input_length_logs.
- Source: [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36), Theorem 26 and proof.
- Proof: Select a logarithmic family of deterministic algorithms from the randomized solver, interleave their queries, and sum the input-distribution tail bounds for the first fast successful simulation.

Published weaker bound retained as stated. Under the strict finite-domain Las Vegas definition used here, average-strict-zero-error-fix-coins gives exact equality. The proof of Theorem 26 also discusses solvers succeeding with probability 2/3, so one must not identify abort-allowed and strict conventions without specifying the model.

## average-Find1-published

For every distribution on dense Find1 inputs, GIPS21 gives a correct deterministic solver of average cost at most log n+1.

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36), Proposition 25.
- Proof: Fix a logarithmic set of positions that hits a 1 on all but 1/n of the input distribution, query those first, and scan the remainder on failure.

## average-Find1-constant

For dense Find1 (weight>=ceil(n/2)), Davg_mu<= (n+1)/(ceil(n/2)+1)<2 for every distribution mu, in the nonuniform model.

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Random-permutation averaging; docs/average-cost.md.
- Proof: A uniformly random permutation scans until the first 1; on a fixed weight-k string its expected stopping position is (n+1)/(k+1). Average over mu and then fix a permutation whose mean cost is at most that average. Every fixed permutation is correct on all dense inputs.

Elementary repository observation, with no first-priority claim. It improves the bound recorded in GIPS21 Proposition 25 under the explicitly same average-cost convention.

## average-Hamming-canonical

For every input distribution mu and fixed epsilon>0, epsilon-Hamming-weight estimation has psRavg_mu=O(log n/epsilon^2).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36), Theorem 27.
- Proof: Fix a sample that estimates accurately for most mu-inputs. Cross-check it against an independent random sample; on disagreement read all bits and compute a fixed valid selector. The expensive branch is rare under mu, while canonical correctness holds pointwise.

## average-approximation-canonization

If a q-query randomized algorithm epsilon/4-approximates a function into a metric space, a pseudo-deterministic epsilon-approximator has average query cost O(q log n) for every fixed input distribution.

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_input_length_log.
- Source: [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36), Theorem 28.
- Proof: Generalize the fixed-sample and cross-check proof for Hamming weight; on the exceptional branch read the input and evaluate the canonical approximation.

The numerator and denominator solve different approximation radii of the same metric-valued target. This is a typed approximation transformation, not a same-relation scalar power inequality.

## average-Hamming-zero-error-lower

For a full-support input distribution and 0<epsilon<1/2, strict zero-error epsilon-Hamming-weight estimation needs at least (1-2epsilon)n queries on every terminating path, hence Omega(n) average cost.

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36), Proposition 29.
- Proof: A path leaving more than 2epsilon*n input bits unread contains both all-zero and all-one completions of those coordinates. Their normalized weights differ by more than 2epsilon, so one common answer cannot approximate both.

## failure-cap-Rfail

Rfail(S)=O(R0(S)).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Truncation and independent repetition; ZPP26 Definition 14.
- Proof: Truncate a strict Las Vegas solver after a constant multiple of its maximum expected cost and output bottom if it has not finished; Markov bounds failure.

## failure-cap-R0

R0(S)<=1.5 Rfail(S) when failure probability is at most 1/3.

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Truncation and independent repetition; ZPP26 Definition 14.
- Proof: Repeat independent failure-flagged trials until a valid answer is returned. The number of trials is geometric with mean at most 3/2.

## failure-cap-verification

Rfail(S)<=O(R(S)+V(S)): verify the candidate returned by a bounded-error solver, and output bottom if invalid.

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Candidate checking.
- Proof: Correct candidates pass and occur with probability at least 2/3; invalid candidates are never returned.

## search-D-R0-total-CNF

There are total query-TFNP relations with R0=O(1) but D=Omega(sqrt(n)); no finite power of R0 bounds D for total search.

- Kind: no_polynomial_bound; domain: total search_relation; classes: query_TFNP.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36), Corollary 8 and Theorem 7; derived zero-error consequence.
- Proof: Fix a dense expanding unsatisfiable CNF. Sample clauses and inspect them until finding a violated clause; a constant fraction are violated on every assignment, so the always-valid expected cost is constant. The pseudo-deterministic quantum lower bound is Omega(sqrt(n)), and D>=psQ.

Derived from the published family, not a first-discovery attribution. This concerns relations and does not contradict the total Boolean decision-function bound D=O(R0^2).

## quantum-search-deterministic-node-size

For a relation solved by a deterministic tree with s total nodes, Q(S)=O(sqrt(s)).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Corollary 9(2).
- Proof: Construct an optimal edge weighting for the classical tree and a span-program/dual-adversary quantum algorithm computing its reached leaf. Since that leaf is a unique deterministic function of the input, reduce the quantum leaf-identification error before mapping it to a valid output.

## quantum-search-random-node-size

Q_{2/5}(S)=O(sqrt(RNodes(S))).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Corollary 27.
- Proof: Sample a deterministic tree from the classical randomized support. Compute its reached leaf with high constant success and return the leaf label; the combined success is at least (9/10)*(2/3)=3/5.

Preserve the error margin. Do not relabel this as the default error-1/3 quantum search measure without an additional reduction.

## quantum-Boolean-random-node-size

For partial or total Boolean decision functions, Q(f)=O(sqrt(RNodes(f))).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Corollary 27 and Boolean majority error reduction.
- Proof: Apply the relation result at error 2/5, then majority-amplify its Boolean answer a constant number of times to error 1/3.

## quantum-Boolean-random-leaf-size

For partial or total Boolean decision functions, Q(f)=O(sqrt(RSize(f))).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Corollary 27 and the node/leaf conversion.
- Proof: RNodes=2 RSize-1 for full binary trees, so convert the size bound by a constant factor and apply Boolean error reduction.

## quantum-search-random-leaf-size

Q_{2/5}(S)=O(sqrt(RSize(S))).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Corollary 27, converted from nodes to leaves.
- Proof: Use RNodes=2 RSize-1, retaining the error-2/5 conclusion.

## guessing-rank-identity

Minimum guessing complexity equals minimum Strahler rank, including on a promise domain.

- Kind: identity; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Claim 12 and Definition 3.
- Proof: For a tree, unequal child ranks let the larger-rank child be the guessed edge; equal ranks force a red edge into a child of that same rank. This is exactly the Strahler recurrence. Minimize the identity over correct trees.

## bomb-quantum-square

At fixed constant explosion/total-error budgets, Bbomb(f)=Theta(Q(f)^2), including partial Boolean functions.

- Kind: theta_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [LL16](https://theoryofcomputing.org/articles/v012a018/), Theorem 4.1.
- Proof: For the upper bound simulate each ordinary query by a quantum-Zeno sequence of gentle controlled bomb queries. For the lower bound use the adversary method to bound progress per query in terms of explosion probability. Boolean error reduction changes fixed error constants by constant factors.

## bomb-quantum-explosion-parameter

For 0<epsilon<=0.01, B_{epsilon,0.01}(f)=Theta(Q_{0.01}(f)^2/epsilon).

- Kind: theta_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [LL16](https://theoryofcomputing.org/articles/v012a018/), Theorem 4.1.
- Proof: For the upper bound simulate each ordinary query by a quantum-Zeno sequence of gentle controlled bomb queries. For the lower bound use the adversary method to bound progress per query in terms of explosion probability. Boolean error reduction changes fixed error constants by constant factors.

Do not suppress inverse explosion probability when it varies with input size. The source allows other fixed total-error constants at most 1/10.

## search-zero-depth-and

DzeroDepth(S)<=DandPos(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [LM19](https://doi.org/10.4230/LIPIcs.STACS.2019.50), Definitions 9–10 and Lemma 11; proof reproduced in KLMY21 Claim 4.4.
- Proof: A conjunction query costs at most one zero answer when expanded into bit queries. Conversely, each stretch of one-answers up to a zero can be located by binary search among at most n+1 positions using conjunctions. Apply the same syntactic conversion on all promised paths.

The original proceedings states the theorem and omits its proof; the later primary paper supplies the proof.

## search-and-zero-depth

DandPos(S)<=DzeroDepth(S)*ceil(log_2(n+1)).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_input_length_log.
- Source: [LM19](https://doi.org/10.4230/LIPIcs.STACS.2019.50), Definitions 9–10 and Lemma 11; proof reproduced in KLMY21 Claim 4.4.
- Proof: A conjunction query costs at most one zero answer when expanded into bit queries. Conversely, each stretch of one-answers up to a zero can be located by binary search among at most n+1 positions using conjunctions. Apply the same syntactic conversion on all promised paths.

The original proceedings states the theorem and omits its proof; the later primary paper supplies the proof.

## monotone-fractional-block-square

fmbs(f)=O(mbs(f)^2).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLMY21](https://doi.org/10.1145/3406325.3450999), Lemma 3.2.
- Proof: Sample sensitive upward blocks from an optimal fractional packing. Remove coordinates occurring in multiple samples; with positive probability this leaves many disjoint sensitive blocks at a suitable restricted input.

## monotone-block-log-monomial

mbs(f)=O(log^2(2+monomialSparsity(f))).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_logarithmic_expression.
- Source: [KLMY21](https://doi.org/10.1145/3406325.3450999), Lemma 3.1.
- Proof: Identify each of k disjoint upward sensitive blocks with one new variable, giving full sensitivity at zero without increasing monomial sparsity. Greedily fix k/2 variables to zero to eliminate all monomials above degree O(log r). At least k/2 sensitive coordinates remain; the Nisan–Szegedy sensitivity/degree inequality gives k=O(log^2 r).

## monotone-certificate-fractional-sparsity

MCC(f)=O(fmbs(f)*log(2+monomialSparsity(f))).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_logarithmic_expression.
- Source: [KLMY21](https://doi.org/10.1145/3406325.3450999), Lemma 3.3.
- Proof: An optimal fractional hitting distribution puts substantial weight on an element hitting many monomials. Greedily choose such coordinates until every monomial is hit.

## and-log-monomial-sparsity

DandPos(f)=O(log^5(2+monomialSparsity(f))*log(2n)).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_logarithmic_expression.
- Source: [KLMY21](https://doi.org/10.1145/3406325.3450999), Theorem 1.2, via Theorem 1.1.
- Proof: Bound monotone block sensitivity by squared logarithmic sparsity, fractionalize with a quadratic loss, and round to a hitting set with another logarithmic loss. Use the resulting hitting-set structure to construct a zero-depth tree and simulate it by positive-conjunction queries.

## and-threshold-no-pure-power

The threshold f(x)=1 iff |x|>=n-1 has RandPos=O(1) but DandPos=Omega(log n). Therefore no pure finite power of RandPos bounds DandPos for total Boolean functions.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [KLMY21survey](https://cseweb.ucsd.edu/~shmcguir/papers/KLMYsigact.pdf), Example 3.17; randomized construction in KLMY21 Example 6.3.
- Proof: Split coordinates uniformly into two complementary sets and query their two conjunctions. At most one zero guarantees one conjunction is one; at least two zeros are separated with probability at least one half, so a constant number of independent trials suffices. The deterministic logarithmic lower bound follows from the n+1 nonzero monomials and the monomial-count bound for a depth-d positive-conjunction tree.

This explains why the log n factor in DandPos=O(RandPos^3 log^4 n) cannot simply be suppressed, even when asking only for a finite power relation.

## average-elementary-Ravg-R

Ravg_mu(S)<=R(S) in the stated strong average-cost models, with mu fixed.

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Definitions of worst-case and average cost.
- Proof: Use the same admissible algorithm: averaging cannot increase a worst-case cost bound, and a canonical or zero-error solver also meets the corresponding weaker output requirement. A deterministic solver is canonical.

No average-error budget is introduced. For two averaged measures, both use the same fixed mu.

## average-elementary-R0avg-R0

R0avg_mu(S)<=R0(S) in the stated strong average-cost models, with mu fixed.

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Definitions of worst-case and average cost.
- Proof: Use the same admissible algorithm: averaging cannot increase a worst-case cost bound, and a canonical or zero-error solver also meets the corresponding weaker output requirement. A deterministic solver is canonical.

No average-error budget is introduced. For two averaged measures, both use the same fixed mu.

## average-elementary-Davg-D

Davg_mu(S)<=D(S) in the stated strong average-cost models, with mu fixed.

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Definitions of worst-case and average cost.
- Proof: Use the same admissible algorithm: averaging cannot increase a worst-case cost bound, and a canonical or zero-error solver also meets the corresponding weaker output requirement. A deterministic solver is canonical.

No average-error budget is introduced. For two averaged measures, both use the same fixed mu.

## average-elementary-psRavg-psR

psRavg_mu(S)<=psR(S) in the stated strong average-cost models, with mu fixed.

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Definitions of worst-case and average cost.
- Proof: Use the same admissible algorithm: averaging cannot increase a worst-case cost bound, and a canonical or zero-error solver also meets the corresponding weaker output requirement. A deterministic solver is canonical.

No average-error budget is introduced. For two averaged measures, both use the same fixed mu.

## average-elementary-Ravg-psRavg

Ravg_mu(S)<=psRavg(S) in the stated strong average-cost models, with mu fixed.

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Definitions of worst-case and average cost.
- Proof: Use the same admissible algorithm: averaging cannot increase a worst-case cost bound, and a canonical or zero-error solver also meets the corresponding weaker output requirement. A deterministic solver is canonical.

No average-error budget is introduced. For two averaged measures, both use the same fixed mu.

## average-elementary-Ravg-R0avg

Ravg_mu(S)<=R0avg(S) in the stated strong average-cost models, with mu fixed.

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Definitions of worst-case and average cost.
- Proof: Use the same admissible algorithm: averaging cannot increase a worst-case cost bound, and a canonical or zero-error solver also meets the corresponding weaker output requirement. A deterministic solver is canonical.

No average-error budget is introduced. For two averaged measures, both use the same fixed mu.

## average-elementary-psRavg-Davg

psRavg_mu(S)<=Davg(S) in the stated strong average-cost models, with mu fixed.

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Definitions of worst-case and average cost.
- Proof: Use the same admissible algorithm: averaging cannot increase a worst-case cost bound, and a canonical or zero-error solver also meets the corresponding weaker output requirement. A deterministic solver is canonical.

No average-error budget is introduced. For two averaged measures, both use the same fixed mu.

## average-Hamming-unbounded-Davg

For fixed 0<epsilon<1/2 and full-support mu, approximate normalized Hamming-weight search has Ravg_mu=O(1), but Davg_mu=Omega(n).

- Kind: no_polynomial_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36), Proposition 29; constant-query sampling and strict average-cost specialization.
- Proof: Uniform bit sampling gives a constant-query pointwise bounded-error estimator at fixed additive accuracy. Every strict zero-error terminating path must query at least (1-2epsilon)n bits, because its completions must all admit its output. This also lower-bounds deterministic average cost.

The denominator is bounded-error average cost; it must not be confused with the strict zero-error average in the numerator.

## average-Hamming-unbounded-R0avg

For fixed 0<epsilon<1/2 and full-support mu, approximate normalized Hamming-weight search has Ravg_mu=O(1), but R0avg_mu=Omega(n).

- Kind: no_polynomial_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36), Proposition 29; constant-query sampling and strict average-cost specialization.
- Proof: Uniform bit sampling gives a constant-query pointwise bounded-error estimator at fixed additive accuracy. Every strict zero-error terminating path must query at least (1-2epsilon)n bits, because its completions must all admit its output. This also lower-bounds deterministic average cost.

The denominator is bounded-error average cost; it must not be confused with the strict zero-error average in the numerator.

## restriction-log-monomialSparsity-approxMonomialSparsity

log(2+monomialSparsity(f))=O(log(2+approxMonomialSparsity(f))^2 log(2n)).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_log.
- Source: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Theorems 4.6–4.7.
- Proof: Construct a deep max-degree restriction tree from large exact complexity. A random leaf retains large exact degree while killing high-degree terms (or making their total coefficient weight small) in a putative sparse/light approximant. The quadratic exact-degree versus approximate-degree theorem contradicts this. Use one-sided trees for ordinary monomials and two-sided trees for subcube indicators.

## restriction-log-monomialSparsity-approxMonomialWeight

log(2+monomialSparsity(f))=O(log(2+approxMonomialWeight(f))^2 log(2n)).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_log.
- Source: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Theorems 4.6–4.7.
- Proof: Construct a deep max-degree restriction tree from large exact complexity. A random leaf retains large exact degree while killing high-degree terms (or making their total coefficient weight small) in a putative sparse/light approximant. The quadratic exact-degree versus approximate-degree theorem contradicts this. Use one-sided trees for ordinary monomials and two-sided trees for subcube indicators.

## restriction-log-monomialWeight-approxMonomialSparsity

log(2+monomialWeight(f))=O(log(2+approxMonomialSparsity(f))^2 log(2n)).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_log.
- Source: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Theorems 4.6–4.7.
- Proof: Construct a deep max-degree restriction tree from large exact complexity. A random leaf retains large exact degree while killing high-degree terms (or making their total coefficient weight small) in a putative sparse/light approximant. The quadratic exact-degree versus approximate-degree theorem contradicts this. Use one-sided trees for ordinary monomials and two-sided trees for subcube indicators.

## restriction-log-monomialWeight-approxMonomialWeight

log(2+monomialWeight(f))=O(log(2+approxMonomialWeight(f))^2 log(2n)).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_log.
- Source: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Theorems 4.6–4.7.
- Proof: Construct a deep max-degree restriction tree from large exact complexity. A random leaf retains large exact degree while killing high-degree terms (or making their total coefficient weight small) in a putative sparse/light approximant. The quadratic exact-degree versus approximate-degree theorem contradicts this. Use one-sided trees for ordinary monomials and two-sided trees for subcube indicators.

## restriction-log-generalizedSparsity-approxGeneralizedSparsity

log(2+generalizedSparsity(f))=O(log(2+approxGeneralizedSparsity(f))^2 log(2n)).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_log.
- Source: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Theorems 4.12–4.13.
- Proof: Construct a deep max-degree restriction tree from large exact complexity. A random leaf retains large exact degree while killing high-degree terms (or making their total coefficient weight small) in a putative sparse/light approximant. The quadratic exact-degree versus approximate-degree theorem contradicts this. Use one-sided trees for ordinary monomials and two-sided trees for subcube indicators.

## restriction-log-generalizedSparsity-approxGeneralizedWeight

log(2+generalizedSparsity(f))=O(log(2+approxGeneralizedWeight(f))^2 log(2n)).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_log.
- Source: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Theorems 4.12–4.13.
- Proof: Construct a deep max-degree restriction tree from large exact complexity. A random leaf retains large exact degree while killing high-degree terms (or making their total coefficient weight small) in a putative sparse/light approximant. The quadratic exact-degree versus approximate-degree theorem contradicts this. Use one-sided trees for ordinary monomials and two-sided trees for subcube indicators.

## restriction-log-generalizedWeight-approxGeneralizedSparsity

log(2+generalizedWeight(f))=O(log(2+approxGeneralizedSparsity(f))^2 log(2n)).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_log.
- Source: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Theorems 4.12–4.13.
- Proof: Construct a deep max-degree restriction tree from large exact complexity. A random leaf retains large exact degree while killing high-degree terms (or making their total coefficient weight small) in a putative sparse/light approximant. The quadratic exact-degree versus approximate-degree theorem contradicts this. Use one-sided trees for ordinary monomials and two-sided trees for subcube indicators.

## restriction-log-generalizedWeight-approxGeneralizedWeight

log(2+generalizedWeight(f))=O(log(2+approxGeneralizedWeight(f))^2 log(2n)).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_log.
- Source: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Theorems 4.12–4.13.
- Proof: Construct a deep max-degree restriction tree from large exact complexity. A random leaf retains large exact degree while killing high-degree terms (or making their total coefficient weight small) in a putative sparse/light approximant. The quadratic exact-degree versus approximate-degree theorem contradicts this. Use one-sided trees for ordinary monomials and two-sided trees for subcube indicators.

## monomial-sparsity-no-pure-approx-power

No finite c gives monomialSparsity(f)=O(approxMonomialSparsity(f)^c) for all total Boolean functions: threshold |x|>=n-1 has exact sparsity n+1 and approximate sparsity O(log n).

- Kind: no_polynomial_bound; domain: total decision_function; classes: symmetric, monotone.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Remark 1.2 and Claim 4.15.
- Proof: For threshold f(x)=1 iff |x|>=n-1, the unique exact polynomial is sum_i product_{j!=i}x_j -(n-1)product_j x_j, with n+1 terms. A separating collection of O(log n) pairs of subsets separates each pair of coordinates in at least a 2/3 fraction of its members. Average the constant-size polynomials testing that all zeros lie on one side of both partitions. This is exact on positive inputs and at most 1/3 on negative inputs.

## monomial-weight-no-pure-approx-power

No finite pure polynomial bound: threshold |x|>=n-1 has exact weight 2n-1 and approximate weight O(1).

- Kind: no_polynomial_bound; domain: total decision_function; classes: symmetric, monotone.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Section 4.3 and Claim 4.15.
- Proof: For threshold f(x)=1 iff |x|>=n-1, the unique exact polynomial is sum_i product_{j!=i}x_j -(n-1)product_j x_j, with n+1 terms. A separating collection of O(log n) pairs of subsets separates each pair of coordinates in at least a 2/3 fraction of its members. Average the constant-size polynomials testing that all zeros lie on one side of both partitions. This is exact on positive inputs and at most 1/3 on negative inputs. The average has bounded coefficient weight, whereas the displayed exact polynomial has weight 2n-1.

## extremal-forrelation-nonadaptive-2026

Extremal Forrelation has QE=1 and Rna=Omega(2^((1/2-o(1))*n)); hence no finite Rna versus QE polynomial bound. This is not an adaptive R lower bound.

- Kind: no_polynomial_bound; domain: partial decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CCM26](https://arxiv.org/abs/2602.07503v2), Theorems 1 and 3; Appendix D.
- Proof: Generalize the bent-function hidden-subspace construction and bound total variation between nonadaptive query transcripts by counting dependent query configurations. Optimize the moment parameter. The v1 partial-spread argument is replaced, not reused.

## multi-C-s-bs

C(f)<=s(f)*bs(f) for total multi-output functions.

- Kind: upper_bound; domain: total multi_output_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDM25](https://doi.org/10.1007/s00037-025-00266-7), Theorem 3.1(i).
- Proof: Take a maximal family of disjoint minimal sensitive blocks. Their union is a certificate, and each block has size at most s(f), since flipping back any coordinate from the altered input changes the output.

## multi-D-C-bs

D(f)<=2*C(f)*bs(f) for total multi-output functions.

- Kind: upper_bound; domain: total multi_output_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDM25](https://doi.org/10.1007/s00037-025-00266-7), Theorem 3.1(iv).
- Proof: Query a consistent certificate for up to 2bs(f) stages. If the residual function is not constant, two consistent inputs with different outputs yield enough disjoint sensitive blocks to contradict the block-sensitivity bound.

## search-deterministic-andor-log-size

log DTSize(S)/(2 log n)<=DandOr(S)<=4 log DTSize(S), for total search; sizes count leaves.

- Kind: upper_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDM25](https://doi.org/10.1007/s00037-025-00266-7), Proposition 6.6 and extension paragraph.
- Proof: Expand each AND/OR query into a bit-query tree for one direction; balance a bit-query tree using AND/OR queries for the other. These syntactic transformations preserve output labels and apply to each tree in a randomized distribution.

## search-randomized-andor-log-size

log RSize(S)/(2 log n)<=RandOr(S)<=4 log RSize(S), for total search; sizes count leaves.

- Kind: upper_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDM25](https://doi.org/10.1007/s00037-025-00266-7), Proposition 6.6 and extension paragraph.
- Proof: Expand each AND/OR query into a bit-query tree for one direction; balance a bit-query tree using AND/OR queries for the other. These syntactic transformations preserve output labels and apply to each tree in a randomized distribution.

## search-DTSize-from-DandOr

DTSize(S)<=2^(2*DandOr(S)*log n).

- Kind: upper_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDM25](https://doi.org/10.1007/s00037-025-00266-7), Proposition 6.6; Lemma 6.9 for pseudo-deterministic variant.
- Proof: Expand each positive AND or OR query to bit queries. For the pseudo-deterministic case choose the selector attaining its optimum; the syntactic expansion preserves that selector and its success probability.

Exponential size conversion; not a finite scalar power bound.

## search-RSize-from-RandOr

RSize(S)<=2^(2*RandOr(S)*log n).

- Kind: upper_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDM25](https://doi.org/10.1007/s00037-025-00266-7), Proposition 6.6; Lemma 6.9 for pseudo-deterministic variant.
- Proof: Expand each positive AND or OR query to bit queries. For the pseudo-deterministic case choose the selector attaining its optimum; the syntactic expansion preserves that selector and its success probability.

Exponential size conversion; not a finite scalar power bound.

## search-psDTSize-from-psRandOr

psDTSize(S)<=2^(2*psRandOr(S)*log n).

- Kind: upper_bound; domain: total search_relation; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CDM25](https://doi.org/10.1007/s00037-025-00266-7), Proposition 6.6; Lemma 6.9 for pseudo-deterministic variant.
- Proof: Expand each positive AND or OR query to bit queries. For the pseudo-deterministic case choose the selector attaining its optimum; the syntactic expansion preserves that selector and its success probability.

Exponential size conversion; not a finite scalar power bound.

## EH89-rank-node-count

For a reduced n-variable binary tree of rank r>=1 and k total nodes: 2^(r+1)-1<=k<=2*sum_{i=0}^r binom(n,i)-1<=2*(e*n/r)^r-1. Function optima inherit the corresponding inequalities.

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: explicit_input_and_rank_parameter_factors.
- Source: [EH89](https://doi.org/10.1016/0890-5401(89)90001-1), Lemma 1(i), p.235.
- Proof: The smallest rank-r tree contains a complete rank-r branching skeleton. The maximum leaf count obeys L(n,r)=L(n-1,r)+L(n-1,r-1), with L(n,0)=L(0,r)=1, hence the binomial sum. A full binary tree has k=2L-1.

The displayed r,k statement is about a single tree; not an equality for independently minimizing trees.

## Nis89-D-R2-cubic

D(f)<=8 R_2(f)^3.

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Nis89](https://doi.org/10.1145/73007.73038), Theorem 4, p.334.
- Proof: Combine C<=bs^2, D<=2*C_1*R_2 and bs<=2R_2.

## Nis89-bs-R2

bs(f)<=2 R_2(f).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Nis89](https://doi.org/10.1145/73007.73038), Lemma 4.2, p.334.
- Proof: Couple runs at x and each disjoint sensitive-block neighbor. Correctness with error 1/4 forces probability at least 1/2 of querying each block; sum over disjoint blocks.

## Nis89-D-R1-square

D(f)<=2 R_1(f)^2.

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: source_statement_refuted_under_literal_cost_convention; loss: none.
- Source: [Nis89](https://doi.org/10.1145/73007.73038), Theorem 3, p.333.
- Proof: For one-bit identity, reject immediately with probability 1/2 and otherwise query. Expected cost is 1/2 and acceptance on input 1 is 1/2, so the printed D<=2R_1^2 gives 1<=1/2. The constant cannot hold under the literal source convention.

Historical result; inspect superseding records before selecting a frontier.

Literal normalization discrepancy established. Repository derivation Nis89-expected-one-sided-repair gives the sharp universal factor 4. Nis91 journal text remains uninspected; no claim about a published erratum.

## Nis89-D-C1-R2

D(f)<=2*C1(f)*R_2(f).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Nis89](https://doi.org/10.1145/73007.73038), Lemma 4.1, pp.333–334.
- Proof: Query a consistent 1-certificate each round. Coupling a 0-input with an input satisfying this certificate forces at least half a query of expected cost to be removed each round; after at most 2R_2 rounds the residual function is constant.

## search-elementary-rel_deg-QE

rel_deg(S)<=2 QE(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Section 2, Definitions 10–12 and standard solver definitions.
- Proof: Use all exact quantum output-probability polynomials, of degree at most twice the query count. They form a bounded nonnegative output distribution on the full cube.

## search-elementary-rel_adeg-rel_deg

rel_adeg(S)<=rel_deg(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Section 2, Definitions 10–12 and standard solver definitions.
- Proof: An exact bounded system satisfies the approximate success constraint.

## search-elementary-rel_udeg-rel_adeg

rel_udeg(S)<=rel_adeg(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Section 2, Definitions 10–12 and standard solver definitions.
- Proof: Drop the off-promise positivity and normalization constraints.

## search-elementary-rel_adeg-rel_udeg

rel_adeg(S)=rel_udeg(S) for total relations.

- Kind: upper_bound; domain: total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Section 2, Definitions 10–12 and standard solver definitions.
- Proof: On a total domain there are no off-promise inputs; the two feasible systems coincide.

## search-elementary-rel_conical-R

rel_conical(S)<=R(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Section 2, Definitions 10–12 and standard solver definitions.
- Proof: For every output sum the probabilities of leaves labeled with that output. Each leaf is a conjunction of at most R queried literals with a nonnegative coefficient. The full-cube normalization is at most one.

## search-elementary-Q-QE

Q(S)<=QE(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Section 2, Definitions 10–12 and standard solver definitions.
- Proof: An exact quantum solver is also a bounded-error solver.

## search-elementary-QE-D

QE(S)<=D(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Section 2, Definitions 10–12 and standard solver definitions.
- Proof: Execute the deterministic solver coherently and measure its valid output.

## search-elementary-R-Rfail

R(S)<=Rfail(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Section 2, Definitions 10–12 and standard solver definitions.
- Proof: Replace detectable failure by any fixed label, counting it as error.

## search-elementary-Rfail-D

Rfail(S)<=D(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Section 2, Definitions 10–12 and standard solver definitions.
- Proof: A deterministic solver never fails.

## search-elementary-R0-D

R0(S)<=D(S).

- Kind: upper_bound; domain: partial_or_total search_relation; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [BK24](https://arxiv.org/abs/2410.16245), Section 2, Definitions 10–12 and standard solver definitions.
- Proof: A deterministic solver is an always-correct randomized solver with the same expected cost.

## relevant-certificate-exp

nRelevant(f)<=4^C(f)/2.

- Kind: nonpolynomial_upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Theorem 1.1, equation (1.4).
- Proof: Use the restriction-decreasing coordinate potential built from certificate measures, and induct under restrictions.

## relevant-monotone-degree

nRelevant(f)<=1.325*2^deg(f).

- Kind: nonpolynomial_upper_bound; domain: total decision_function; classes: monotone.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Theorem 1.1.
- Proof: Apply the coordinate-potential restriction argument with stronger monotone local-degree constraints.

## relevant-monotone-sensitivity

nRelevant(f)<=4^s(f)/2.

- Kind: nonpolynomial_upper_bound; domain: total decision_function; classes: monotone.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Theorem 1.1.
- Proof: Specialize the coordinate-measure potential to monotone sensitivity and bound the potential after restrictions.

## relevant-monotone-D

nRelevant(f)<=2^D(f)/4+2.

- Kind: nonpolynomial_upper_bound; domain: total decision_function; classes: monotone.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Theorem 1.1.
- Proof: Use the monotone decision-tree recurrence and restriction-decreasing local depth potential.

## relevant-degree-CHS-historical

nRelevant(f)<=6.614*2^deg(f); later constant improved to 4.394 by Wel22.

- Kind: nonpolynomial_upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CHS20](https://doi.org/10.1007/s00493-019-4136-7), Theorem 1.1 and Section 2.
- Proof: Weight each relevant coordinate by 2^(-local degree). Restrict a maxonomial hitting set and bound the increase in the normalized relevant-variable count; sum the resulting convergent series.

Historical result; inspect superseding records before selecting a frontier.

## relevant-degree-no-power

No fixed polynomial upper bound of nRelevant by degree: read-once complete depth-d decision trees on distinct internal-node variables depend on 2^d-1 variables and have degree d.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [CHS20](https://doi.org/10.1007/s00493-019-4136-7), Introduction, p.1.
- Proof: Use an address-style complete depth-d tree with fresh variables at every internal node and leaf labels chosen so every node query is relevant. Its degree is at most d, and the deepest queries witness degree d.

## permutation-degree-sensitivity

deg(f)<=2*s(f)^2 on S_n, with s the disjoint-transposition packing sensitivity.

- Kind: upper_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Corollary 5.6.
- Proof: Use Young-tableau pseudo-characters to witness a nonzero top-degree component; embed a Boolean cube of dimension at least degree/2 whose neighbors map to disjoint transposition neighbors. Apply Huang’s cube sensitivity theorem.

## permutation-bs-degree

bs(f)<=6*approx_degree(f)^2 on S_n.

- Kind: upper_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Theorem 3.1; Lemma 3.6.
- Proof: Disjoint sensitive permutation blocks generate a Boolean subcube. Restrict the approximating polynomial to this cube and symmetrize; the standard approximate-degree/block-sensitivity argument applies.

## permutation-s-edge

s(f)<=t(f); the packing sensitivity and the total transposition edge count are different measures.

- Kind: upper_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Section 2.2, Notes on sensitivity.
- Proof: Every family of disjoint sensitive transpositions is a subset of all sensitive transpositions.

## completion-D-equals-D

completion_D(f)=D(f) for every partial Boolean function.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Observation 49, p.23.
- Proof: A deterministic decision tree for the partial function outputs some bit off-promise and hence defines a total completion of the same depth. Conversely every completion solver solves the partial function.

## D-equals-completion-D

D(f)=completion_D(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Observation 49, p.23.
- Proof: Restrict an optimal total-completion solver to the promised domain; use the reverse construction for equality.

## native-to-completion-R0

R0(f)<=completion_R0(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45; restriction of a total solver or witness.
- Proof: Every total completion agrees on the promise. Restrict its solver, certificates, sensitive blocks or polynomial to the promised task, then minimize. For degree this is the unrestricted promise degree, a relaxation of the total polynomial.

## native-to-completion-R

R(f)<=completion_R(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45; restriction of a total solver or witness.
- Proof: Every total completion agrees on the promise. Restrict its solver, certificates, sensitive blocks or polynomial to the promised task, then minimize. For degree this is the unrestricted promise degree, a relaxation of the total polynomial.

## native-to-completion-C

C(f)<=completion_C(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45; restriction of a total solver or witness.
- Proof: Every total completion agrees on the promise. Restrict its solver, certificates, sensitive blocks or polynomial to the promised task, then minimize. For degree this is the unrestricted promise degree, a relaxation of the total polynomial.

## native-to-completion-bs

bs(f)<=completion_bs(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45; restriction of a total solver or witness.
- Proof: Every total completion agrees on the promise. Restrict its solver, certificates, sensitive blocks or polynomial to the promised task, then minimize. For degree this is the unrestricted promise degree, a relaxation of the total polynomial.

## native-to-completion-s

s(f)<=completion_s(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45; restriction of a total solver or witness.
- Proof: Every total completion agrees on the promise. Restrict its solver, certificates, sensitive blocks or polynomial to the promised task, then minimize. For degree this is the unrestricted promise degree, a relaxation of the total polynomial.

## native-to-completion-QE

QE(f)<=completion_QE(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45; restriction of a total solver or witness.
- Proof: Every total completion agrees on the promise. Restrict its solver, certificates, sensitive blocks or polynomial to the promised task, then minimize. For degree this is the unrestricted promise degree, a relaxation of the total polynomial.

## native-to-completion-deg

deg(f)<=completion_deg(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45; restriction of a total solver or witness.
- Proof: Every total completion agrees on the promise. Restrict its solver, certificates, sensitive blocks or polynomial to the promised task, then minimize. For degree this is the unrestricted promise degree, a relaxation of the total polynomial.

## native-to-completion-Q

Q(f)<=completion_Q(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45; restriction of a total solver or witness.
- Proof: Every total completion agrees on the promise. Restrict its solver, certificates, sensitive blocks or polynomial to the promised task, then minimize. For degree this is the unrestricted promise degree, a relaxation of the total polynomial.

## native-to-completion-adeg

adeg(f)<=completion_adeg(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45; restriction of a total solver or witness.
- Proof: Every total completion agrees on the promise. Restrict its solver, certificates, sensitive blocks or polynomial to the promised task, then minimize. For degree this is the unrestricted promise degree, a relaxation of the total polynomial.

## promise-s-bs

s prime<=bs prime.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Observation 16.
- Proof: Single-coordinate sensitive exits are disjoint sensitive blocks.

## promise-bs-strongC

bs prime<=Cstrong.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Observation 16.
- Proof: A strong certificate intersects each disjoint block that exits the promise or changes the output.

## critical-bs-exit

cbs<=bs prime.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Lemma 35.
- Proof: At promised inputs every block sensitive in a completion either changes the original output or exits the promise.

## bs-critical-completion

bs<=cbs.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Lemma 35.
- Proof: Every completion retains all promised opposite-output sensitive blocks.

## critical-bs-bounded-adeg

cbs=O(cubeBoundedAdeg^2).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Lemma 20, citing ABK21.
- Proof: Use the completion-critical block-sensitivity versus globally bounded polynomial theorem; off-promise boundedness is essential.

## D-critical-certificate-bs

D<=criticalCertificate*criticalBScompletion.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Lemma 33(3).
- Proof: Choose a completion attaining both nested optima. Query consistent positive certificates; if too many rounds leave conflicting promised outputs, their disjoint disagreement sets contradict the completion-critical block bound.

## promise-C-bs-exitS

C<=bs*promiseS.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Lemma 32.
- Proof: A maximal family of disjoint minimal promised opposite-output blocks covers a weak certificate. At a minimal block endpoint, undoing any one coordinate either changes the output back or exits the promise, bounding block size by exit-sensitive sensitivity.

## promise-D-weak-strong-C

D<=C*Cstrong.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Lemma 34.
- Proof: Query a consistent strong 1-certificate in each round. Against any surviving 0-input, each round reveals a new coordinate of its weak 0-certificate; after C rounds the answer is determined.

## relevant-degree-43935

nRelevant(f)<=4.3935*2^deg(f).

- Kind: nonpolynomial_upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Theorem 3.13, p.10; visually checked.
- Proof: Use exact-rational small-degree LP block-sensitivity bounds through degree 14, the general block-sensitivity improvement and the coordinate-potential recurrence to bound its limiting constant by 4.3935.

Sharper than introductory 4.394, not a new later publication. The reported Maple LP computation was not independently reproduced.

## Nis89-expected-one-sided-repair

D(f)<=4*NisR1expect(f)^2; factor 4 is optimal for this exact expected-cost, success-1/2 convention.

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Nis89](https://doi.org/10.1145/73007.73038), Repository derivation using Section 1.2 and the certificate-query method of Lemma 4.1.
- Proof: Let T be worst-case expected cost. On any 1-input, accepting transcripts are certificates, so C1<=2T. Query a consistent 1-certificate each round. For any surviving 0-input, coupling it with an input satisfying each queried certificate forces probability at least 1/2 of probing a new disagreement block. Blocks from different rounds are disjoint, so at most floor(2T) rounds are possible. Thus D<=2T*C1<=4T^2. One-bit identity has T=1/2 (acceptance implies a query), attaining equality.

Not attributed as an original Nisan constant or a published correction. The default capped R_1 is a distinct measure.

## perm-chain-permBS-permFBS

bs<=fbs.

- Kind: upper_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Theorem 3.1; Section 4.2 parameters; Lemma 3.5 for C.
- Proof: The unit-weight integral packing is feasible for the fractional LP.

## perm-chain-permFBS-permC

fbs<=C.

- Kind: upper_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Theorem 3.1; Section 4.2 parameters; Lemma 3.5 for C.
- Proof: A certificate must intersect every opposite-output disagreement block; use the certificate as a feasible dual cover.

## perm-chain-permC-permUC

C<=U.

- Kind: upper_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Theorem 3.1; Section 4.2 parameters; Lemma 3.5 for C.
- Proof: Every unambiguous partition certificate is an ordinary certificate.

## perm-chain-permUC-permD

U<=D.

- Kind: upper_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Theorem 3.1; Section 4.2 parameters; Lemma 3.5 for C.
- Proof: Each decision-tree leaf supplies a compatible permutation-entry certificate. The leaf sets partition S_n.

## perm-chain-permBS-permR

bs<=3R.

- Kind: upper_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Theorem 3.1; Section 4.2 parameters; Lemma 3.5 for C.
- Proof: Choose disjoint sensitive neighbors and apply the classical distinguishing/coupling lower bound at error 1/3.

## perm-chain-permR-permRfail23

R<=R_0.

- Kind: upper_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Theorem 3.1; Section 4.2 parameters; Lemma 3.5 for C.
- Proof: On detectable failure, output a uniformly random bit. Success is at least 1/3+(2/3)/2=2/3 with the same depth cap; this uses Boolean output.

## perm-chain-permRfail23-permD

R_0<=D.

- Kind: upper_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Theorem 3.1; Section 4.2 parameters; Lemma 3.5 for C.
- Proof: The deterministic tree never fails.

## perm-chain-permAdeg-permQ

approx_degree<=2Q.

- Kind: upper_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Theorem 3.1; Section 4.2 parameters; Lemma 3.5 for C.
- Proof: Quantum acceptance probabilities are polynomials of degree at most twice the symbol-query count in the domain indicators.

## perm-chain-permQ-permQE

Q<=Q_E.

- Kind: upper_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Theorem 3.1; Section 4.2 parameters; Lemma 3.5 for C.
- Proof: An exact solver is bounded-error.

## perm-chain-permQE-permD

Q_E<=D.

- Kind: upper_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Theorem 3.1; Section 4.2 parameters; Lemma 3.5 for C.
- Proof: Execute each deterministic symbol query coherently.

## perm-chain-permD-permBS

D<=18*bs^4.

- Kind: upper_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Theorem 3.1; Section 4.2 parameters; Lemma 3.5 for C.
- Proof: Specialize the general certificate-query simulation with Delta=2, conflict bound M=n and beta>=1/3 for perfect matchings representing permutations.

## perm-chain-permC-permBS

C<=3*bs^2.

- Kind: upper_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Theorem 3.1; Section 4.2 parameters; Lemma 3.5 for C.
- Proof: Apply Lemma 3.5 with beta>=1/3: maximal disjoint minimal disagreement sets form a certificate.

## perm-chain-permS-permBS

s<=bs.

- Kind: upper_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Theorem 3.1; Section 4.2 parameters; Lemma 3.5 for C.
- Proof: Disjoint sensitive transpositions are a special case of disjoint sensitive moved-point supports.

## perm-chain-permAdeg-permDegree

approx_degree<=degree.

- Kind: upper_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Section 2.2 and Theorem 3.1.
- Proof: An exact polynomial approximates with zero error.

## perm-chain-permDegree-permD

degree<=D.

- Kind: upper_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Section 2.2 and Theorem 3.1.
- Proof: Sum the products of entry indicators along accepting leaves of an optimal tree; each product has degree at most the depth.

## perm-chain-permQ-permR

Q<=R.

- Kind: upper_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Section 2.2 and Theorem 3.1.
- Proof: Simulate a capped classical randomized symbol-query algorithm with a quantum query algorithm, including its random choices.

## critical-bs-completion-bs

criticalBScompletion<=completion_bs.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Definitions 18–19 and 45.
- Proof: For every completion, its maximum block sensitivity over promised points is at most its maximum over the whole cube. Minimize the former and evaluate it at a completion minimizing the latter.

## weak-C-critical-certificate

C<=criticalCertificate.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Definitions 18–19 and 45.
- Proof: Any full-cube certificate in a block-optimal total completion is a valid weak promise certificate. Maximize over promised inputs and then minimize over block-optimal completions.

## perm-edge-no-power-permD

No finite power bounds permEdgeS by permD: the single-entry indicator has edge sensitivity n-1 and permD=O(1).

- Kind: no_polynomial_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository example using DFLLV21 Section 2.2 definitions.
- Proof: For f(pi)=[pi(1)=1], one symbol query solves the function and degree is one. Its n-1 sensitive transpositions at a positive input all share position 1, so the disjoint packing is one. A one-entry certificate and its n disjoint output cases give certificate, fractional and unambiguous complexities at most one. Quantum and randomized costs are also at most one.

## perm-edge-no-power-permRfail23

No finite power bounds permEdgeS by permRfail23: the single-entry indicator has edge sensitivity n-1 and permRfail23=O(1).

- Kind: no_polynomial_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository example using DFLLV21 Section 2.2 definitions.
- Proof: For f(pi)=[pi(1)=1], one symbol query solves the function and degree is one. Its n-1 sensitive transpositions at a positive input all share position 1, so the disjoint packing is one. A one-entry certificate and its n disjoint output cases give certificate, fractional and unambiguous complexities at most one. Quantum and randomized costs are also at most one.

## perm-edge-no-power-permR

No finite power bounds permEdgeS by permR: the single-entry indicator has edge sensitivity n-1 and permR=O(1).

- Kind: no_polynomial_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository example using DFLLV21 Section 2.2 definitions.
- Proof: For f(pi)=[pi(1)=1], one symbol query solves the function and degree is one. Its n-1 sensitive transpositions at a positive input all share position 1, so the disjoint packing is one. A one-entry certificate and its n disjoint output cases give certificate, fractional and unambiguous complexities at most one. Quantum and randomized costs are also at most one.

## perm-edge-no-power-permC

No finite power bounds permEdgeS by permC: the single-entry indicator has edge sensitivity n-1 and permC=O(1).

- Kind: no_polynomial_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository example using DFLLV21 Section 2.2 definitions.
- Proof: For f(pi)=[pi(1)=1], one symbol query solves the function and degree is one. Its n-1 sensitive transpositions at a positive input all share position 1, so the disjoint packing is one. A one-entry certificate and its n disjoint output cases give certificate, fractional and unambiguous complexities at most one. Quantum and randomized costs are also at most one.

## perm-edge-no-power-permUC

No finite power bounds permEdgeS by permUC: the single-entry indicator has edge sensitivity n-1 and permUC=O(1).

- Kind: no_polynomial_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository example using DFLLV21 Section 2.2 definitions.
- Proof: For f(pi)=[pi(1)=1], one symbol query solves the function and degree is one. Its n-1 sensitive transpositions at a positive input all share position 1, so the disjoint packing is one. A one-entry certificate and its n disjoint output cases give certificate, fractional and unambiguous complexities at most one. Quantum and randomized costs are also at most one.

## perm-edge-no-power-permFBS

No finite power bounds permEdgeS by permFBS: the single-entry indicator has edge sensitivity n-1 and permFBS=O(1).

- Kind: no_polynomial_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository example using DFLLV21 Section 2.2 definitions.
- Proof: For f(pi)=[pi(1)=1], one symbol query solves the function and degree is one. Its n-1 sensitive transpositions at a positive input all share position 1, so the disjoint packing is one. A one-entry certificate and its n disjoint output cases give certificate, fractional and unambiguous complexities at most one. Quantum and randomized costs are also at most one.

## perm-edge-no-power-permBS

No finite power bounds permEdgeS by permBS: the single-entry indicator has edge sensitivity n-1 and permBS=O(1).

- Kind: no_polynomial_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository example using DFLLV21 Section 2.2 definitions.
- Proof: For f(pi)=[pi(1)=1], one symbol query solves the function and degree is one. Its n-1 sensitive transpositions at a positive input all share position 1, so the disjoint packing is one. A one-entry certificate and its n disjoint output cases give certificate, fractional and unambiguous complexities at most one. Quantum and randomized costs are also at most one.

## perm-edge-no-power-permS

No finite power bounds permEdgeS by permS: the single-entry indicator has edge sensitivity n-1 and permS=O(1).

- Kind: no_polynomial_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository example using DFLLV21 Section 2.2 definitions.
- Proof: For f(pi)=[pi(1)=1], one symbol query solves the function and degree is one. Its n-1 sensitive transpositions at a positive input all share position 1, so the disjoint packing is one. A one-entry certificate and its n disjoint output cases give certificate, fractional and unambiguous complexities at most one. Quantum and randomized costs are also at most one.

## perm-edge-no-power-permDegree

No finite power bounds permEdgeS by permDegree: the single-entry indicator has edge sensitivity n-1 and permDegree=O(1).

- Kind: no_polynomial_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository example using DFLLV21 Section 2.2 definitions.
- Proof: For f(pi)=[pi(1)=1], one symbol query solves the function and degree is one. Its n-1 sensitive transpositions at a positive input all share position 1, so the disjoint packing is one. A one-entry certificate and its n disjoint output cases give certificate, fractional and unambiguous complexities at most one. Quantum and randomized costs are also at most one.

## perm-edge-no-power-permAdeg

No finite power bounds permEdgeS by permAdeg: the single-entry indicator has edge sensitivity n-1 and permAdeg=O(1).

- Kind: no_polynomial_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository example using DFLLV21 Section 2.2 definitions.
- Proof: For f(pi)=[pi(1)=1], one symbol query solves the function and degree is one. Its n-1 sensitive transpositions at a positive input all share position 1, so the disjoint packing is one. A one-entry certificate and its n disjoint output cases give certificate, fractional and unambiguous complexities at most one. Quantum and randomized costs are also at most one.

## perm-edge-no-power-permQE

No finite power bounds permEdgeS by permQE: the single-entry indicator has edge sensitivity n-1 and permQE=O(1).

- Kind: no_polynomial_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository example using DFLLV21 Section 2.2 definitions.
- Proof: For f(pi)=[pi(1)=1], one symbol query solves the function and degree is one. Its n-1 sensitive transpositions at a positive input all share position 1, so the disjoint packing is one. A one-entry certificate and its n disjoint output cases give certificate, fractional and unambiguous complexities at most one. Quantum and randomized costs are also at most one.

## perm-edge-no-power-permQ

No finite power bounds permEdgeS by permQ: the single-entry indicator has edge sensitivity n-1 and permQ=O(1).

- Kind: no_polynomial_bound; domain: total decision_function; classes: symmetric_group.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository example using DFLLV21 Section 2.2 definitions.
- Proof: For f(pi)=[pi(1)=1], one symbol query solves the function and degree is one. Its n-1 sensitive transpositions at a positive input all share position 1, so the disjoint packing is one. A one-entry certificate and its n disjoint output cases give certificate, fractional and unambiguous complexities at most one. Quantum and randomized costs are also at most one.

## relevant-depth-exact-upper

nRelevant(f)<=2^D(f)-1, attained by a complete decision tree with a distinct variable at every internal node.

- Kind: nonpolynomial_upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: A depth-d binary tree has at most 2^d-1 internal nodes, and every relevant variable must label some internal node. The recursively addressed tree on fresh variables attains the bound.

## core-at-most-relevant-D

D(f)<=O(nRelevant(f)) for total Boolean functions.

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: Query all relevant variables. This gives D<=nRelevant; the indexed total-core comparison bounds the indicated measure by O(D).

## relevant-no-power-D

No finite c bounds nRelevant(f) by O(D(f)^c) over all total Boolean functions.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: On the complete fresh-variable depth-d decision tree, nRelevant=2^d-1 while every core measure is O(d). Exponential growth exceeds every fixed power.

## core-at-most-relevant-R0

R0(f)<=O(nRelevant(f)) for total Boolean functions.

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: Query all relevant variables. This gives D<=nRelevant; the indexed total-core comparison bounds the indicated measure by O(D).

## relevant-no-power-R0

No finite c bounds nRelevant(f) by O(R0(f)^c) over all total Boolean functions.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: On the complete fresh-variable depth-d decision tree, nRelevant=2^d-1 while every core measure is O(d). Exponential growth exceeds every fixed power.

## core-at-most-relevant-R

R(f)<=O(nRelevant(f)) for total Boolean functions.

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: Query all relevant variables. This gives D<=nRelevant; the indexed total-core comparison bounds the indicated measure by O(D).

## relevant-no-power-R

No finite c bounds nRelevant(f) by O(R(f)^c) over all total Boolean functions.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: On the complete fresh-variable depth-d decision tree, nRelevant=2^d-1 while every core measure is O(d). Exponential growth exceeds every fixed power.

## core-at-most-relevant-C

C(f)<=O(nRelevant(f)) for total Boolean functions.

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: Query all relevant variables. This gives D<=nRelevant; the indexed total-core comparison bounds the indicated measure by O(D).

## relevant-no-power-C

No finite c bounds nRelevant(f) by O(C(f)^c) over all total Boolean functions.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: On the complete fresh-variable depth-d decision tree, nRelevant=2^d-1 while every core measure is O(d). Exponential growth exceeds every fixed power.

## core-at-most-relevant-RC

RC(f)<=O(nRelevant(f)) for total Boolean functions.

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: Query all relevant variables. This gives D<=nRelevant; the indexed total-core comparison bounds the indicated measure by O(D).

## relevant-no-power-RC

No finite c bounds nRelevant(f) by O(RC(f)^c) over all total Boolean functions.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: On the complete fresh-variable depth-d decision tree, nRelevant=2^d-1 while every core measure is O(d). Exponential growth exceeds every fixed power.

## core-at-most-relevant-bs

bs(f)<=O(nRelevant(f)) for total Boolean functions.

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: Query all relevant variables. This gives D<=nRelevant; the indexed total-core comparison bounds the indicated measure by O(D).

## relevant-no-power-bs

No finite c bounds nRelevant(f) by O(bs(f)^c) over all total Boolean functions.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: On the complete fresh-variable depth-d decision tree, nRelevant=2^d-1 while every core measure is O(d). Exponential growth exceeds every fixed power.

## core-at-most-relevant-s

s(f)<=O(nRelevant(f)) for total Boolean functions.

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: Query all relevant variables. This gives D<=nRelevant; the indexed total-core comparison bounds the indicated measure by O(D).

## relevant-no-power-s

No finite c bounds nRelevant(f) by O(s(f)^c) over all total Boolean functions.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: On the complete fresh-variable depth-d decision tree, nRelevant=2^d-1 while every core measure is O(d). Exponential growth exceeds every fixed power.

## core-at-most-relevant-lambda

lambda(f)<=O(nRelevant(f)) for total Boolean functions.

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: Query all relevant variables. This gives D<=nRelevant; the indexed total-core comparison bounds the indicated measure by O(D).

## relevant-no-power-lambda

No finite c bounds nRelevant(f) by O(lambda(f)^c) over all total Boolean functions.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: On the complete fresh-variable depth-d decision tree, nRelevant=2^d-1 while every core measure is O(d). Exponential growth exceeds every fixed power.

## core-at-most-relevant-QE

QE(f)<=O(nRelevant(f)) for total Boolean functions.

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: Query all relevant variables. This gives D<=nRelevant; the indexed total-core comparison bounds the indicated measure by O(D).

## relevant-no-power-QE

No finite c bounds nRelevant(f) by O(QE(f)^c) over all total Boolean functions.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: On the complete fresh-variable depth-d decision tree, nRelevant=2^d-1 while every core measure is O(d). Exponential growth exceeds every fixed power.

## core-at-most-relevant-deg

deg(f)<=O(nRelevant(f)) for total Boolean functions.

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: Query all relevant variables. This gives D<=nRelevant; the indexed total-core comparison bounds the indicated measure by O(D).

## core-at-most-relevant-Q

Q(f)<=O(nRelevant(f)) for total Boolean functions.

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: Query all relevant variables. This gives D<=nRelevant; the indexed total-core comparison bounds the indicated measure by O(D).

## relevant-no-power-Q

No finite c bounds nRelevant(f) by O(Q(f)^c) over all total Boolean functions.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: On the complete fresh-variable depth-d decision tree, nRelevant=2^d-1 while every core measure is O(d). Exponential growth exceeds every fixed power.

## core-at-most-relevant-adeg

adeg(f)<=O(nRelevant(f)) for total Boolean functions.

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: Query all relevant variables. This gives D<=nRelevant; the indexed total-core comparison bounds the indicated measure by O(D).

## relevant-no-power-adeg

No finite c bounds nRelevant(f) by O(adeg(f)^c) over all total Boolean functions.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 3.6; total-core comparison chains.
- Proof: On the complete fresh-variable depth-d decision tree, nRelevant=2^d-1 while every core measure is O(d). Exponential growth exceeds every fixed power.

## relevant-hybrid-degree-sensitivity

nRelevant=O(sqrt(2^degree*4^sensitivity)).

- Kind: nonpolynomial_upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: statement_checked_proof_pending; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Theorem 3.18, equations (3.25)–(3.26).
- Proof: The author outlines applying the restriction method to convex combinations of the coordinate-degree, coordinate-sensitivity and coordinate-certificate measures. The paper explicitly omits the technical proof for brevity.

Mixed-measure bound; not a scalar exponent in the B measure. Second inequality retains the source tildeO notation; hidden factors not independently extracted.

## relevant-hybrid-certificate-sensitivity

nRelevant=tildeO(sqrt(4^certificate*4^sensitivity)).

- Kind: nonpolynomial_upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: statement_checked_proof_pending; loss: none.
- Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Theorem 3.18, equations (3.25)–(3.26).
- Proof: The author outlines applying the restriction method to convex combinations of the coordinate-degree, coordinate-sensitivity and coordinate-certificate measures. The paper explicitly omits the technical proof for brevity.

Mixed-measure bound; not a scalar exponent in the B measure. Second inequality retains the source tildeO notation; hidden factors not independently extracted.

## completion-relevance-Dna

completion_nRelevant(f)=Dna(f) for partial Boolean decision functions.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Repository derivation from Definition 45 and fixed-set nonadaptive queries.
- Proof: A nonadaptive algorithm queries a fixed set S that separates every promised opposite-output pair. Define a completion depending only on S, assigning arbitrary values to unseen S-patterns. Conversely, querying the relevant coordinates of any completion solves f nonadaptively.

## Dna-completion-relevance

Dna(f)=completion_nRelevant(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Repository derivation from Definition 45 and fixed-set nonadaptive queries.
- Proof: The same projection-separation argument gives the reverse inequality.

## completion-relevance-depth-upper

completion_nRelevant(f)<=2^D(f)-1.

- Kind: nonpolynomial_upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Repository derivation from Definition 45 and fixed-set nonadaptive queries.
- Proof: An optimal partial decision tree induces a total completion of the same depth. Its number of relevant variables is at most its 2^D-1 internal nodes.

## completion-relevance-depth-lower

D(f)<=completion_nRelevant(f).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Repository derivation from Definition 45 and fixed-set nonadaptive queries.
- Proof: Query the relevant coordinates of an optimal completion, or use the equality with nonadaptive complexity.

## completion-fbs-FC

completion_fbs=completion_FC.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45; LP duality in the total-function definitions.
- Proof: The total-function LP-dual identity fbs=FC holds for every completion. Taking minima over the identical completion set preserves equality.

## completion-FC-fbs

completion_FC=completion_fbs.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45; LP duality.
- Proof: The same pointwise identity holds before taking minima.

## domain-chain-domainAdeg-domainDegree

approx_degree<=degree.

- Kind: upper_bound; domain: total decision_function; classes: composable_query_domain.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Theorem 3.1.
- Proof: An exact representation is a zero-error approximant.

## domain-chain-domainDegree-domainD

degree<=D.

- Kind: upper_bound; domain: total decision_function; classes: composable_query_domain.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Theorem 3.1.
- Proof: Sum the products of membership indicators on accepting decision-tree paths.

## domain-chain-domainBS-domainFBS

bs<=fbs.

- Kind: upper_bound; domain: total decision_function; classes: composable_query_domain.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Theorem 3.1.
- Proof: Integral disjoint blocks give a feasible fractional packing.

## domain-chain-domainFBS-domainC

fbs<=C.

- Kind: upper_bound; domain: total decision_function; classes: composable_query_domain.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Theorem 3.1.
- Proof: A certificate supplies a feasible dual cover for every opposite-output disagreement set.

## domain-chain-domainC-domainUC

C<=U.

- Kind: upper_bound; domain: total decision_function; classes: composable_query_domain.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Theorem 3.1.
- Proof: Every partition certificate is a certificate.

## domain-chain-domainUC-domainD

U<=D.

- Kind: upper_bound; domain: total decision_function; classes: composable_query_domain.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Theorem 3.1.
- Proof: Tree leaves give unambiguous certificates.

## domain-chain-domainBS-domainR

bs<=3R.

- Kind: upper_bound; domain: total decision_function; classes: composable_query_domain.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Theorem 3.1.
- Proof: Disjoint sensitive alternatives must be distinguished with constant success.

## domain-chain-domainR-domainRfail23

R<=R_0.

- Kind: upper_bound; domain: total decision_function; classes: composable_query_domain.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Theorem 3.1.
- Proof: Guess a fresh fair bit on failure; success at least 1/3+(2/3)/2=2/3, with no extra queries.

## domain-chain-domainRfail23-domainD

R_0<=D.

- Kind: upper_bound; domain: total decision_function; classes: composable_query_domain.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Theorem 3.1.
- Proof: A deterministic tree never fails.

## domain-chain-domainAdeg-domainQ

approx_degree<=2Q.

- Kind: upper_bound; domain: total decision_function; classes: composable_query_domain.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Theorem 3.1.
- Proof: Acceptance probabilities are domain-indicator polynomials of degree at most twice the query count.

## domain-chain-domainQ-domainQE

Q<=Q_E.

- Kind: upper_bound; domain: total decision_function; classes: composable_query_domain.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Theorem 3.1.
- Proof: Exact algorithms are bounded-error algorithms.

## domain-chain-domainQE-domainD

Q_E<=D.

- Kind: upper_bound; domain: total decision_function; classes: composable_query_domain.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Theorem 3.1.
- Proof: Coherently simulate the deterministic symbol-query tree.

## domain-chain-domainS-domainBS

s<=bs.

- Kind: upper_bound; domain: total decision_function; classes: composable_query_domain.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Theorem 3.1.
- Proof: Chunk-size disjoint changes are a subclass of disjoint changes.

## domain-chain-domainBS-domainAdeg

bs<=6*approx_degree^2.

- Kind: upper_bound; domain: total decision_function; classes: composable_query_domain.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Theorem 3.1.
- Proof: Composability embeds the disjoint-block alternatives in a Boolean cube; apply the symmetrized polynomial degree lower bound.

## domain-parameterized-domainD-domainBS

D<=beta^(-2)*max(Delta,n/M)*bs^4.

- Kind: upper_bound; domain: total decision_function; classes: composable_query_domain.
- Evidence: primary_statement_and_proof_route_checked; loss: domain_parameters.
- Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Theorem 3.1.
- Proof: Apply the parameterized certificate-query and block-shortening arguments of Theorem 3.1 and Lemma 3.5. Domain parameters remain explicit.

M>0 required for n/M; no pure-power bound is asserted uniformly over domains.

## domain-parameterized-domainC-domainBS

C<=beta^(-1)*bs^2.

- Kind: upper_bound; domain: total decision_function; classes: composable_query_domain.
- Evidence: primary_statement_and_proof_route_checked; loss: domain_parameters.
- Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Theorem 3.1.
- Proof: Apply the parameterized certificate-query and block-shortening arguments of Theorem 3.1 and Lemma 3.5. Domain parameters remain explicit.

M>0 required for n/M; no pure-power bound is asserted uniformly over domains.

## forward-permutation-no-power-domainDegree

Forward-only deterministic complexity is n/2 while domainDegree=1 for f(pi)=[pi^(-1)(1)<=n/2].

- Kind: no_polynomial_bound; domain: total decision_function; classes: forward_only_permutation_queries.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository example using Sections 2.1,2.2 and 4.3.
- Proof: One inverse query finds the position of 1, and sum_{i<=n/2} [pi(i)=1] has degree one. Query an entire half for the forward upper bound. For fewer than n/2 queries an adversary answers with distinct values other than 1, leaving possible positions in both halves.

## forward-permutation-no-power-permD

Forward-only deterministic complexity is n/2 while permD=1 for f(pi)=[pi^(-1)(1)<=n/2].

- Kind: no_polynomial_bound; domain: total decision_function; classes: forward_only_permutation_queries.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository example using Sections 2.1,2.2 and 4.3.
- Proof: One inverse query finds the position of 1, and sum_{i<=n/2} [pi(i)=1] has degree one. Query an entire half for the forward upper bound. For fewer than n/2 queries an adversary answers with distinct values other than 1, leaving possible positions in both halves.

## completion-containment-completion_C0-completion_C

completion_C0<= completion_C.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45; LP duality in the total-function definitions.
- Proof: Evaluate the componentwise total-function inequality at a completion optimal for the right-hand measure, then minimize the left.

Do not interchange min_F and max_b: minimizing completions can differ.

## completion-containment-completion_C1-completion_C

completion_C1<= completion_C.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45; LP duality in the total-function definitions.
- Proof: Evaluate the componentwise total-function inequality at a completion optimal for the right-hand measure, then minimize the left.

Do not interchange min_F and max_b: minimizing completions can differ.

## completion-containment-completion_UC0-completion_UC

completion_UC0<= completion_UC.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45; LP duality in the total-function definitions.
- Proof: Evaluate the componentwise total-function inequality at a completion optimal for the right-hand measure, then minimize the left.

Do not interchange min_F and max_b: minimizing completions can differ.

## completion-containment-completion_UC1-completion_UC

completion_UC1<= completion_UC.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45; LP duality in the total-function definitions.
- Proof: Evaluate the componentwise total-function inequality at a completion optimal for the right-hand measure, then minimize the left.

Do not interchange min_F and max_b: minimizing completions can differ.

## completion-containment-completion_C-completion_UC

completion_C<= completion_UC.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45; LP duality in the total-function definitions.
- Proof: Evaluate the componentwise total-function inequality at a completion optimal for the right-hand measure, then minimize the left.

Do not interchange min_F and max_b: minimizing completions can differ.

## BD16-domainD-domainQ

D(f)=O(Q(f)^18) on a single multislice, uniformly over multiplicities and alphabet size.

- Kind: upper_bound; domain: total decision_function; classes: single_multislice_forward_queries.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BD16](https://doi.org/10.4230/LIPIcs.TQC.2016.7), Theorems 5 and 12.
- Proof: Either certificates are large and Corollary 9 supplies the lower bound, or Lemma 10 restricts to small certificates using a bounded set of alphabet symbols. Hard disjoint certificate arrangements reduce to permutation inversion, and the adversary method gives the remaining quantum lower bound.

An indexed original-source bound, not a globally certified best exponent. For binary full slices compare the later HKMP26 improvements.

## BD16-domainD-domainR

D(f)=O(R(f)^9) on a single multislice, uniformly over multiplicities and alphabet size.

- Kind: upper_bound; domain: total decision_function; classes: single_multislice_forward_queries.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BD16](https://doi.org/10.4230/LIPIcs.TQC.2016.7), Theorem 12.
- Proof: Use the same large-certificate versus restricted-symbol hard-instance dichotomy; the classical distinguishing lower bound yields the ninth-power relationship.

An indexed original-source bound, not a globally certified best exponent. For binary full slices compare the later HKMP26 improvements.

## BD16-domainC-domainBS

C(f)<=3*bs(f)^2 on a single multislice.

- Kind: upper_bound; domain: total decision_function; classes: single_multislice_forward_queries.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [BD16](https://doi.org/10.4230/LIPIcs.TQC.2016.7), Theorem 8 and Definition 7.
- Proof: Theorem 8 gives C<=3*bs*s_2. A maximal disjoint collection of minimal sensitive blocks forms a certificate, and cycle decomposition bounds block size by 3*s_2. Since s_2<=bs, the square follows.

An indexed original-source bound, not a globally certified best exponent. For binary full slices compare the later HKMP26 improvements.

## side-C0-C

C0(f)<=O(C(f)).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, AIK26 preliminary definitions, article p.3; repository elementary derivation.
- Proof: The maximum over inputs of one output is at most the maximum over both outputs.

## side-C0-UC0

C0(f)<=O(UC0(f)).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, AIK26 preliminary definitions, article p.3; repository elementary derivation.
- Proof: Each term of an unambiguous representation is a certificate; drop the uniqueness requirement.

## side-UC0-UC

UC0(f)<=O(UC(f)).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, AIK26 preliminary definitions, article p.3; repository elementary derivation.
- Proof: UC is the maximum of the separately optimized two output unambiguous certificate costs.

## side-UC0-D

UC0(f)<=O(D(f)).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, AIK26 preliminary definitions, article p.3; repository elementary derivation.
- Proof: The leaves of a deterministic tree labeled by the chosen output partition that output class into disjoint subcubes of codimension at most the tree depth.

## side-C1-C

C1(f)<=O(C(f)).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, AIK26 preliminary definitions, article p.3; repository elementary derivation.
- Proof: The maximum over inputs of one output is at most the maximum over both outputs.

## side-C1-UC1

C1(f)<=O(UC1(f)).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, AIK26 preliminary definitions, article p.3; repository elementary derivation.
- Proof: Each term of an unambiguous representation is a certificate; drop the uniqueness requirement.

## side-UC1-UC

UC1(f)<=O(UC(f)).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, AIK26 preliminary definitions, article p.3; repository elementary derivation.
- Proof: UC is the maximum of the separately optimized two output unambiguous certificate costs.

## side-UC1-D

UC1(f)<=O(D(f)).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, AIK26 preliminary definitions, article p.3; repository elementary derivation.
- Proof: The leaves of a deterministic tree labeled by the chosen output partition that output class into disjoint subcubes of codimension at most the tree depth.

## side-UC-D

UC(f)<=O(D(f)).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, AIK26 preliminary definitions, article p.3; repository elementary derivation.
- Proof: Apply the leaf partition argument to each output; take their maximum.

## side-R-R1

R(f)<=O(R1(f)).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, AIK26 preliminary definitions, article p.3; repository elementary derivation.
- Proof: A no-false-positive, positive-success-at-least-2/3 algorithm has two-sided error at most 1/3.

## side-R1-D

R1(f)<=O(D(f)).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, AIK26 preliminary definitions, article p.3; repository elementary derivation.
- Proof: A deterministic tree has no false positives and succeeds with probability one.

## side-R1-R0

R1(f)<=O(R0(f)).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, AIK26 preliminary definitions, article p.3; repository elementary derivation.
- Proof: Run an expected zero-error algorithm to three times its worst-input expectation. If it has not halted, output zero. Markov bounds failure on positive inputs by 1/3; negative inputs never produce one. Integer ceilings and the zero-cost constant case do not change the big-O bound.

## side-C1-R1

C1(f)<=O(R1(f)).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, AIK26 preliminary definitions, article p.3; repository elementary derivation.
- Proof: For a positive input, some accepting query transcript has positive probability. Its queried literals exclude every negative input: otherwise the same positive-probability event of random choices would produce the same accepting transcript there, contradicting no false positives. The transcript is a positive certificate of width at most the query cap.

## side-deg-UC0

deg(f)<=O(UC0(f)).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, AIK26 preliminary definitions, article p.3; repository elementary derivation.
- Proof: Sum the disjoint zero-certificate indicator monomials; this is exactly 1-f on every Boolean input. Each indicator has degree at most UC0; complementing does not raise degree.

## total-unbounded-D-C1-OR

On OR_n, C1=1 and D tends to infinity; no finite power of max(1,C1) bounds D.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while D diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-R0-C1-OR

On OR_n, C1=1 and R0 tends to infinity; no finite power of max(1,C1) bounds R0.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while R0 diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-R-C1-OR

On OR_n, C1=1 and R tends to infinity; no finite power of max(1,C1) bounds R.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while R diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-C-C1-OR

On OR_n, C1=1 and C tends to infinity; no finite power of max(1,C1) bounds C.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while C diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-RC-C1-OR

On OR_n, C1=1 and RC tends to infinity; no finite power of max(1,C1) bounds RC.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while RC diverges. At the unique extreme input, the n singleton sensitive blocks give fractional block sensitivity n. LP duality and the indexed RC equivalence give RC=Theta(n); QC=Theta(sqrt(RC)) gives QC=Theta(sqrt(n)).

## total-unbounded-bs-C1-OR

On OR_n, C1=1 and bs tends to infinity; no finite power of max(1,C1) bounds bs.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while bs diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-s-C1-OR

On OR_n, C1=1 and s tends to infinity; no finite power of max(1,C1) bounds s.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while s diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-lambda-C1-OR

On OR_n, C1=1 and lambda tends to infinity; no finite power of max(1,C1) bounds lambda.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while lambda diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-QE-C1-OR

On OR_n, C1=1 and QE tends to infinity; no finite power of max(1,C1) bounds QE.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while QE diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-deg-C1-OR

On OR_n, C1=1 and deg tends to infinity; no finite power of max(1,C1) bounds deg.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while deg diverges. Exact degree is n, by the nonzero full multilinear coefficient. Either output unambiguous representation gives an exact polynomial of degree at most its width.

## total-unbounded-Q-C1-OR

On OR_n, C1=1 and Q tends to infinity; no finite power of max(1,C1) bounds Q.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while Q diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-adeg-C1-OR

On OR_n, C1=1 and adeg tends to infinity; no finite power of max(1,C1) bounds adeg.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while adeg diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-nRelevant-C1-OR

On OR_n, C1=1 and nRelevant tends to infinity; no finite power of max(1,C1) bounds nRelevant.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while nRelevant diverges. All n variables are relevant.

## total-unbounded-C0-C1-OR

On OR_n, C1=1 and C0 tends to infinity; no finite power of max(1,C1) bounds C0.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while C0 diverges. The opposite-output input requires fixing all n bits.

## total-unbounded-UC-C1-OR

On OR_n, C1=1 and UC tends to infinity; no finite power of max(1,C1) bounds UC.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while UC diverges. Exact degree is n, by the nonzero full multilinear coefficient. Either output unambiguous representation gives an exact polynomial of degree at most its width.

## total-unbounded-UC0-C1-OR

On OR_n, C1=1 and UC0 tends to infinity; no finite power of max(1,C1) bounds UC0.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while UC0 diverges. Exact degree is n, by the nonzero full multilinear coefficient. Either output unambiguous representation gives an exact polynomial of degree at most its width.

## total-unbounded-UC1-C1-OR

On OR_n, C1=1 and UC1 tends to infinity; no finite power of max(1,C1) bounds UC1.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while UC1 diverges. Exact degree is n, by the nonzero full multilinear coefficient. Either output unambiguous representation gives an exact polynomial of degree at most its width.

## total-unbounded-fbs-C1-OR

On OR_n, C1=1 and fbs tends to infinity; no finite power of max(1,C1) bounds fbs.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while fbs diverges. At the unique extreme input, the n singleton sensitive blocks give fractional block sensitivity n. LP duality and the indexed RC equivalence give RC=Theta(n); QC=Theta(sqrt(RC)) gives QC=Theta(sqrt(n)).

## total-unbounded-FC-C1-OR

On OR_n, C1=1 and FC tends to infinity; no finite power of max(1,C1) bounds FC.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while FC diverges. At the unique extreme input, the n singleton sensitive blocks give fractional block sensitivity n. LP duality and the indexed RC equivalence give RC=Theta(n); QC=Theta(sqrt(RC)) gives QC=Theta(sqrt(n)).

## total-unbounded-QC-C1-OR

On OR_n, C1=1 and QC tends to infinity; no finite power of max(1,C1) bounds QC.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while QC diverges. At the unique extreme input, the n singleton sensitive blocks give fractional block sensitivity n. LP duality and the indexed RC equivalence give RC=Theta(n); QC=Theta(sqrt(RC)) gives QC=Theta(sqrt(n)).

## total-unbounded-Q0-C1-OR

On OR_n, C1=1 and Q0 tends to infinity; no finite power of max(1,C1) bounds Q0.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while Q0 diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-R1-C1-OR

On OR_n, C1=1 and R1 tends to infinity; no finite power of max(1,C1) bounds R1.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On OR_n, C1=1, while R1 diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-D-C0-AND

On AND_n, C0=1 and D tends to infinity; no finite power of max(1,C0) bounds D.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while D diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-R0-C0-AND

On AND_n, C0=1 and R0 tends to infinity; no finite power of max(1,C0) bounds R0.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while R0 diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-R-C0-AND

On AND_n, C0=1 and R tends to infinity; no finite power of max(1,C0) bounds R.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while R diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-C-C0-AND

On AND_n, C0=1 and C tends to infinity; no finite power of max(1,C0) bounds C.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while C diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-RC-C0-AND

On AND_n, C0=1 and RC tends to infinity; no finite power of max(1,C0) bounds RC.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while RC diverges. At the unique extreme input, the n singleton sensitive blocks give fractional block sensitivity n. LP duality and the indexed RC equivalence give RC=Theta(n); QC=Theta(sqrt(RC)) gives QC=Theta(sqrt(n)).

## total-unbounded-bs-C0-AND

On AND_n, C0=1 and bs tends to infinity; no finite power of max(1,C0) bounds bs.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while bs diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-s-C0-AND

On AND_n, C0=1 and s tends to infinity; no finite power of max(1,C0) bounds s.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while s diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-lambda-C0-AND

On AND_n, C0=1 and lambda tends to infinity; no finite power of max(1,C0) bounds lambda.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while lambda diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-QE-C0-AND

On AND_n, C0=1 and QE tends to infinity; no finite power of max(1,C0) bounds QE.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while QE diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-deg-C0-AND

On AND_n, C0=1 and deg tends to infinity; no finite power of max(1,C0) bounds deg.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while deg diverges. Exact degree is n, by the nonzero full multilinear coefficient. Either output unambiguous representation gives an exact polynomial of degree at most its width.

## total-unbounded-Q-C0-AND

On AND_n, C0=1 and Q tends to infinity; no finite power of max(1,C0) bounds Q.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while Q diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-adeg-C0-AND

On AND_n, C0=1 and adeg tends to infinity; no finite power of max(1,C0) bounds adeg.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while adeg diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-nRelevant-C0-AND

On AND_n, C0=1 and nRelevant tends to infinity; no finite power of max(1,C0) bounds nRelevant.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while nRelevant diverges. All n variables are relevant.

## total-unbounded-C1-C0-AND

On AND_n, C0=1 and C1 tends to infinity; no finite power of max(1,C0) bounds C1.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while C1 diverges. The opposite-output input requires fixing all n bits.

## total-unbounded-UC-C0-AND

On AND_n, C0=1 and UC tends to infinity; no finite power of max(1,C0) bounds UC.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while UC diverges. Exact degree is n, by the nonzero full multilinear coefficient. Either output unambiguous representation gives an exact polynomial of degree at most its width.

## total-unbounded-UC0-C0-AND

On AND_n, C0=1 and UC0 tends to infinity; no finite power of max(1,C0) bounds UC0.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while UC0 diverges. Exact degree is n, by the nonzero full multilinear coefficient. Either output unambiguous representation gives an exact polynomial of degree at most its width.

## total-unbounded-UC1-C0-AND

On AND_n, C0=1 and UC1 tends to infinity; no finite power of max(1,C0) bounds UC1.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while UC1 diverges. Exact degree is n, by the nonzero full multilinear coefficient. Either output unambiguous representation gives an exact polynomial of degree at most its width.

## total-unbounded-fbs-C0-AND

On AND_n, C0=1 and fbs tends to infinity; no finite power of max(1,C0) bounds fbs.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while fbs diverges. At the unique extreme input, the n singleton sensitive blocks give fractional block sensitivity n. LP duality and the indexed RC equivalence give RC=Theta(n); QC=Theta(sqrt(RC)) gives QC=Theta(sqrt(n)).

## total-unbounded-FC-C0-AND

On AND_n, C0=1 and FC tends to infinity; no finite power of max(1,C0) bounds FC.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while FC diverges. At the unique extreme input, the n singleton sensitive blocks give fractional block sensitivity n. LP duality and the indexed RC equivalence give RC=Theta(n); QC=Theta(sqrt(RC)) gives QC=Theta(sqrt(n)).

## total-unbounded-QC-C0-AND

On AND_n, C0=1 and QC tends to infinity; no finite power of max(1,C0) bounds QC.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while QC diverges. At the unique extreme input, the n singleton sensitive blocks give fractional block sensitivity n. LP duality and the indexed RC equivalence give RC=Theta(n); QC=Theta(sqrt(RC)) gives QC=Theta(sqrt(n)).

## total-unbounded-Q0-C0-AND

On AND_n, C0=1 and Q0 tends to infinity; no finite power of max(1,C0) bounds Q0.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while Q0 diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## total-unbounded-R1-C0-AND

On AND_n, C0=1 and R1 tends to infinity; no finite power of max(1,C0) bounds R1.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On AND_n, C0=1, while R1 diverges. Approximate degree is Omega(sqrt(n)) by the indexed block-sensitivity lower bound, since bs=n. Polynomial and query simulations, and s=bs=n with lambda>=sqrt(s), give divergence of all the remaining listed core/query measures; R1 dominates R and Q0 dominates Q up to constant amplification.

## forward-multislice-D-unbounded-domainDegree

Forward-only all-distinct multislices have domainD=n/2 and domainDegree=1; no uniform finite polynomial comparison.

- Kind: no_polynomial_bound; domain: total decision_function; classes: single_multislice_forward_queries.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On permutations of [n], n even, use f(pi)=[the position of 1 is in the first half], with forward coordinate queries. A certificate is the single observed coordinate containing 1. These certificates partition both output classes, so C=UC=1. The sum of entry indicators for positions in the first half is an exact degree-one polynomial. Every sensitive change must include the original position of 1, so bs=fbs=s=1. An adversary avoids returning 1 for fewer than n/2 queries, leaving positions in both halves; querying a half suffices, hence D=n/2.

## forward-multislice-D-unbounded-domainAdeg

Forward-only all-distinct multislices have domainD=n/2 and domainAdeg=1; no uniform finite polynomial comparison.

- Kind: no_polynomial_bound; domain: total decision_function; classes: single_multislice_forward_queries.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On permutations of [n], n even, use f(pi)=[the position of 1 is in the first half], with forward coordinate queries. A certificate is the single observed coordinate containing 1. These certificates partition both output classes, so C=UC=1. The sum of entry indicators for positions in the first half is an exact degree-one polynomial. Every sensitive change must include the original position of 1, so bs=fbs=s=1. An adversary avoids returning 1 for fewer than n/2 queries, leaving positions in both halves; querying a half suffices, hence D=n/2.

## forward-multislice-D-unbounded-domainC

Forward-only all-distinct multislices have domainD=n/2 and domainC=1; no uniform finite polynomial comparison.

- Kind: no_polynomial_bound; domain: total decision_function; classes: single_multislice_forward_queries.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On permutations of [n], n even, use f(pi)=[the position of 1 is in the first half], with forward coordinate queries. A certificate is the single observed coordinate containing 1. These certificates partition both output classes, so C=UC=1. The sum of entry indicators for positions in the first half is an exact degree-one polynomial. Every sensitive change must include the original position of 1, so bs=fbs=s=1. An adversary avoids returning 1 for fewer than n/2 queries, leaving positions in both halves; querying a half suffices, hence D=n/2.

## forward-multislice-D-unbounded-domainUC

Forward-only all-distinct multislices have domainD=n/2 and domainUC=1; no uniform finite polynomial comparison.

- Kind: no_polynomial_bound; domain: total decision_function; classes: single_multislice_forward_queries.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On permutations of [n], n even, use f(pi)=[the position of 1 is in the first half], with forward coordinate queries. A certificate is the single observed coordinate containing 1. These certificates partition both output classes, so C=UC=1. The sum of entry indicators for positions in the first half is an exact degree-one polynomial. Every sensitive change must include the original position of 1, so bs=fbs=s=1. An adversary avoids returning 1 for fewer than n/2 queries, leaving positions in both halves; querying a half suffices, hence D=n/2.

## forward-multislice-D-unbounded-domainBS

Forward-only all-distinct multislices have domainD=n/2 and domainBS=1; no uniform finite polynomial comparison.

- Kind: no_polynomial_bound; domain: total decision_function; classes: single_multislice_forward_queries.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On permutations of [n], n even, use f(pi)=[the position of 1 is in the first half], with forward coordinate queries. A certificate is the single observed coordinate containing 1. These certificates partition both output classes, so C=UC=1. The sum of entry indicators for positions in the first half is an exact degree-one polynomial. Every sensitive change must include the original position of 1, so bs=fbs=s=1. An adversary avoids returning 1 for fewer than n/2 queries, leaving positions in both halves; querying a half suffices, hence D=n/2.

## forward-multislice-D-unbounded-domainFBS

Forward-only all-distinct multislices have domainD=n/2 and domainFBS=1; no uniform finite polynomial comparison.

- Kind: no_polynomial_bound; domain: total decision_function; classes: single_multislice_forward_queries.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On permutations of [n], n even, use f(pi)=[the position of 1 is in the first half], with forward coordinate queries. A certificate is the single observed coordinate containing 1. These certificates partition both output classes, so C=UC=1. The sum of entry indicators for positions in the first half is an exact degree-one polynomial. Every sensitive change must include the original position of 1, so bs=fbs=s=1. An adversary avoids returning 1 for fewer than n/2 queries, leaving positions in both halves; querying a half suffices, hence D=n/2.

## forward-multislice-D-unbounded-domainS

Forward-only all-distinct multislices have domainD=n/2 and domainS=1; no uniform finite polynomial comparison.

- Kind: no_polynomial_bound; domain: total decision_function; classes: single_multislice_forward_queries.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: On permutations of [n], n even, use f(pi)=[the position of 1 is in the first half], with forward coordinate queries. A certificate is the single observed coordinate containing 1. These certificates partition both output classes, so C=UC=1. The sum of entry indicators for positions in the first half is an exact degree-one polynomial. Every sensitive change must include the original position of 1, so bs=fbs=s=1. An adversary avoids returning 1 for fewer than n/2 queries, leaving positions in both halves; querying a half suffices, hence D=n/2.

## completion-support-FC-fbs

FC(f)=O(fbs(f)^1).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: At each input the certificate covering LP and sensitive-block packing LP are dual: constraints are that each opposite-output disagreement block has covering weight at least one. Finite LP strong duality gives equality; maximize over inputs.

## completion-support-fbs-FC

fbs(f)=O(FC(f)^1).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: The same primal/dual LP identity gives the reverse direction.

## completion-support-QC-FC

QC(f)=O(FC(f)^0.5).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Aar02 Theorem 7 and Lemma 5; repository LP identification.
- Proof: Use FC=Theta(RC) and Aaronson’s QC=Theta(sqrt(RC)) certificate characterization. Both are maximum-over-input verification costs with fixed constant rejection probability.

## completion-support-FC-QC

FC(f)=O(QC(f)^2).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Aar02 Theorem 7 and Lemma 5; repository LP identification.
- Proof: Square Aaronson’s RC=O(QC^2), then use FC=Theta(RC). No promise-completion minima are interchanged.

## completion-support-RC-FC

RC(f)<=(ln 2)*FC(f) for expected classical verification accepting the claimed input with certainty and rejecting opposite outputs with probability at least 1/2.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: For a fixed claimed input x, choose a fractional certificate w. Query coordinate i independently with probability 1-2^(-w_i), rejecting on disagreement. For any opposite-output y, the probability of missing every disagreement is 2^(-sum_{i:x_i!=y_i} w_i)<=1/2. The expected query count is sum_i(1-2^(-w_i))<=(ln 2)*sum_i w_i. The verifier accepts x certainly; maximize over x.

Repository constant refinement of fractional sampling, not a constant quoted from Aaronson. The ln 2 coefficient is asymptotically optimal for native measures over partial functions, as separately proved; sharpness for total functions or minimum-completion measures is not asserted.

## completion-support-Q-Q0

Q(f)=O(Q0(f)^1).

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: Repeat the fixed-cap never-wrong algorithm a constant number of times to reduce inconclusive probability from at most 1/2 to at most 1/3; output an arbitrary bit if still inconclusive.

## address-unbounded-nRelevant-UC

Total address functions have nRelevant=2^k+k and UC=O(k+1), excluding every finite power.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: Use k address bits to select one of 2^k data bits. Every input bit is relevant, and reading the address followed by its selected data bit costs k+1. A deterministic tree supplies unambiguous certificate families from its leaves and simulates all the query measures here; fractional certificates and quantum verifiers cost at most the corresponding ordinary certificates/tree depth. Thus the right measure is at most O(k+1), while relevance is exponential in k. Total functions have a unique completion, so these witnesses lift unchanged.

## address-unbounded-nRelevant-UC0

Total address functions have nRelevant=2^k+k and UC0=O(k+1), excluding every finite power.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: Use k address bits to select one of 2^k data bits. Every input bit is relevant, and reading the address followed by its selected data bit costs k+1. A deterministic tree supplies unambiguous certificate families from its leaves and simulates all the query measures here; fractional certificates and quantum verifiers cost at most the corresponding ordinary certificates/tree depth. Thus the right measure is at most O(k+1), while relevance is exponential in k. Total functions have a unique completion, so these witnesses lift unchanged.

## address-unbounded-nRelevant-UC1

Total address functions have nRelevant=2^k+k and UC1=O(k+1), excluding every finite power.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: Use k address bits to select one of 2^k data bits. Every input bit is relevant, and reading the address followed by its selected data bit costs k+1. A deterministic tree supplies unambiguous certificate families from its leaves and simulates all the query measures here; fractional certificates and quantum verifiers cost at most the corresponding ordinary certificates/tree depth. Thus the right measure is at most O(k+1), while relevance is exponential in k. Total functions have a unique completion, so these witnesses lift unchanged.

## address-unbounded-nRelevant-fbs

Total address functions have nRelevant=2^k+k and fbs=O(k+1), excluding every finite power.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: Use k address bits to select one of 2^k data bits. Every input bit is relevant, and reading the address followed by its selected data bit costs k+1. A deterministic tree supplies unambiguous certificate families from its leaves and simulates all the query measures here; fractional certificates and quantum verifiers cost at most the corresponding ordinary certificates/tree depth. Thus the right measure is at most O(k+1), while relevance is exponential in k. Total functions have a unique completion, so these witnesses lift unchanged.

## address-unbounded-nRelevant-FC

Total address functions have nRelevant=2^k+k and FC=O(k+1), excluding every finite power.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: Use k address bits to select one of 2^k data bits. Every input bit is relevant, and reading the address followed by its selected data bit costs k+1. A deterministic tree supplies unambiguous certificate families from its leaves and simulates all the query measures here; fractional certificates and quantum verifiers cost at most the corresponding ordinary certificates/tree depth. Thus the right measure is at most O(k+1), while relevance is exponential in k. Total functions have a unique completion, so these witnesses lift unchanged.

## address-unbounded-nRelevant-QC

Total address functions have nRelevant=2^k+k and QC=O(k+1), excluding every finite power.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: Use k address bits to select one of 2^k data bits. Every input bit is relevant, and reading the address followed by its selected data bit costs k+1. A deterministic tree supplies unambiguous certificate families from its leaves and simulates all the query measures here; fractional certificates and quantum verifiers cost at most the corresponding ordinary certificates/tree depth. Thus the right measure is at most O(k+1), while relevance is exponential in k. Total functions have a unique completion, so these witnesses lift unchanged.

## address-unbounded-nRelevant-Q0

Total address functions have nRelevant=2^k+k and Q0=O(k+1), excluding every finite power.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: Use k address bits to select one of 2^k data bits. Every input bit is relevant, and reading the address followed by its selected data bit costs k+1. A deterministic tree supplies unambiguous certificate families from its leaves and simulates all the query measures here; fractional certificates and quantum verifiers cost at most the corresponding ordinary certificates/tree depth. Thus the right measure is at most O(k+1), while relevance is exponential in k. Total functions have a unique completion, so these witnesses lift unchanged.

## address-unbounded-nRelevant-R1

Total address functions have nRelevant=2^k+k and R1=O(k+1), excluding every finite power.

- Kind: no_polynomial_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository elementary proof; source measure conventions.
- Proof: Use k address bits to select one of 2^k data bits. Every input bit is relevant, and reading the address followed by its selected data bit costs k+1. A deterministic tree supplies unambiguous certificate families from its leaves and simulates all the query measures here; fractional certificates and quantum verifiers cost at most the corresponding ordinary certificates/tree depth. Thus the right measure is at most O(k+1), while relevance is exponential in k. Total functions have a unique completion, so these witnesses lift unchanged.

## domain-added-domainDegree-domainQE

domainDegree(f)<=2 domainQE(f).

- Kind: upper_bound; domain: total decision_function; classes: composable_query_domain.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [DFLLV26](https://doi.org/10.5070/C6.68665), Lemma 2.2(l), article p.13.
- Proof: Each query changes an amplitude polynomial by at most one degree in the input-entry indicators. A T-query algorithm has acceptance probability of degree at most 2T; exact acceptance equals f on the domain.

## domain-added-domainQ-domainR

domainQ(f)<=O(domainR(f)).

- Kind: upper_bound; domain: total decision_function; classes: composable_query_domain.
- Evidence: repository_derivation_checked; loss: none.
- Source: [DFLLV26](https://doi.org/10.5070/C6.68665), Section 2.2 query model; repository simulation.
- Proof: Simulate each classical query with the quantum oracle, maintain the classical transcript and random seed, and use the same output distribution.

## Goos15-D-UC0-square

D(f)<=UC0(f)*(UC0(f)+1)/2 for total Boolean functions; in particular D=O(UC0^2).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Goos15](https://eccc.weizmann.ac.il/report/2015/012/), Proposition 5, p.4; complement symmetry; repository triangular-count refinement.
- Proof: Distinct unambiguous b-certificates conflict. Query all literals of one surviving certificate. If it matches, return b; otherwise each surviving certificate loses at least one queried variable. The maximum residual width decreases each round, so widths k,k-1,...,1 sum to k(k+1)/2. A zero-width surviving certificate fixes the output. Apply to the cheaper output side for UCmin.

The original proposition states D<=UP^dt(f)^2, with UP^dt=UC1. The triangular bound is an explicit repository refinement of its proof, not quoted as a printed source constant. No sharp leading-constant optimality claimed.

## Goos15-D-UC1-square

D(f)<=UC1(f)*(UC1(f)+1)/2 for total Boolean functions; in particular D=O(UC1^2).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Goos15](https://eccc.weizmann.ac.il/report/2015/012/), Proposition 5, p.4; complement symmetry; repository triangular-count refinement.
- Proof: Distinct unambiguous b-certificates conflict. Query all literals of one surviving certificate. If it matches, return b; otherwise each surviving certificate loses at least one queried variable. The maximum residual width decreases each round, so widths k,k-1,...,1 sum to k(k+1)/2. A zero-width surviving certificate fixes the output. Apply to the cheaper output side for UCmin.

The original proposition states D<=UP^dt(f)^2, with UP^dt=UC1. The triangular bound is an explicit repository refinement of its proof, not quoted as a printed source constant. No sharp leading-constant optimality claimed.

## Goos15-D-UCmin-square

D(f)<=UCmin(f)*(UCmin(f)+1)/2 for total Boolean functions; in particular D=O(UCmin^2).

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Goos15](https://eccc.weizmann.ac.il/report/2015/012/), Proposition 5, p.4; complement symmetry; repository triangular-count refinement.
- Proof: Distinct unambiguous b-certificates conflict. Query all literals of one surviving certificate. If it matches, return b; otherwise each surviving certificate loses at least one queried variable. The maximum residual width decreases each round, so widths k,k-1,...,1 sum to k(k+1)/2. A zero-width surviving certificate fixes the output. Apply to the cheaper output side for UCmin.

The original proposition states D<=UP^dt(f)^2, with UP^dt=UC1. The triangular bound is an explicit repository refinement of its proof, not quoted as a printed source constant. No sharp leading-constant optimality claimed.

## product-domainD-domainUC-square

On full Cartesian products with coordinate symbol queries, domainD<=O(domainUC^2).

- Kind: upper_bound; domain: total decision_function; classes: full_product_coordinate_queries.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository extension of certificate querying to full products.
- Proof: An unambiguous certificate family on a full Cartesian product has pairwise conflicting partial assignments: compatible assignments would have a common valid extension. Querying one surviving certificate reduces all others by at least one coordinate after failure, yielding k(k+1)/2 queries.

This is a profile-specific theorem. It is not inserted as a uniform bound over all composable query domains. Compatible partial assignments need not extend to a permutation or multislice input.

## product-domainD-domainC-square

On full Cartesian products with coordinate symbol queries, domainD<=O(domainC^2).

- Kind: upper_bound; domain: total decision_function; classes: full_product_coordinate_queries.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository extension of certificate querying to full products.
- Proof: Use D<=C0*C1: query a consistent positive certificate. At a fixed surviving negative input each failed round reveals a new coordinate of any fixed negative certificate, because opposite-output certificates conflict on a full product. At most C0 rounds of at most C1 queries suffice. Thus D<=C^2. Alphabets need not be binary; compatibility still implies a valid extension.

This is a profile-specific theorem. It is not inserted as a uniform bound over all composable query domains. Compatible partial assignments need not extend to a permutation or multislice input.

## domain-parameterized-domainD-domainC

D(f)<=max(Delta,n/M)*C(f)^2 for M>0. If C(f)<=M, D(f)<=Delta*C0(f)*C1(f)<=Delta*C(f)^2.

- Kind: upper_bound; domain: total decision_function; classes: composable_query_domain.
- Evidence: repository_derivation_checked; loss: domain_parameters.
- Source: [DFLLV26](https://doi.org/10.5070/C6.68665), Lemma 3.3, article pp.19–20.
- Proof: Query a consistent positive certificate and all allowed queries mentioning its elements. Under the conflict threshold, each round reveals a new element of any surviving negative certificate. At most C0 rounds cost Delta*C1 each. If C>M, use D<=n and C0*C1>M; the global n/M prefactor covers this case.

M>0 required for n/M; no pure-power bound is asserted uniformly over domains.

## profile-witnessing-degree-sensitivity

degree(f)<=alpha^(-1)*s(f)^2 on alpha-witnessing domains, alpha>0.

- Kind: upper_bound; domain: total decision_function; classes: alpha_witnessing_composable_query_domain.
- Evidence: repository_derivation_checked; loss: domain_parameters.
- Source: [DFLLV26](https://doi.org/10.5070/C6.68665), Theorem 5.3, article p.31.
- Proof: Choose a degree-witnessing pseudo-character correlated with f, restrict to its induced Boolean cube of dimension at least alpha*degree, and apply Huang’s sensitivity theorem.

M>0 required for n/M; no pure-power bound is asserted uniformly over domains.

## profile-certificate-sensitivity-five

C(f)<=6*beta_c^(-1)*alpha^(-2)*s(f)^5 when beta_c>0 and the domain is alpha-witnessing.

- Kind: upper_bound; domain: total decision_function; classes: alpha_witnessing_composable_query_domain.
- Evidence: repository_derivation_checked; loss: domain_parameters.
- Source: [DFLLV26](https://doi.org/10.5070/C6.68665), Lemmas 3.5–3.6 and Theorem 5.3; repository composition.
- Proof: Lemma 3.5 gives C<=beta_c^(-1)*s*bs. Lemma 3.6 gives bs<=6*adeg^2<=6*degree^2. Substitute Theorem 5.3, degree<=alpha^(-1)*s^2, retaining all constants.

M>0 required for n/M; no pure-power bound is asserted uniformly over domains.

## capped-D-R1-square

For capped one-sided R1 with positive success at least p, D<=floor(R1/p)*C1<=R1^2/p. At p=2/3, D<=3 R1^2/2.

- Kind: upper_bound; domain: total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Repository certificate-query coupling proof; compare Nis89 one-sided argument and AIK26 capped convention.
- Proof: Query a consistent positive certificate each round. At any surviving zero input x, replace only its disagreeing literals in each queried certificate to obtain positive inputs y_j; their disagreement blocks are nonempty and disjoint. Couple an R1 computation on x and each y_j with the same randomness. Acceptance probability at least p on y_j and no false positives on x force querying block j with probability at least p on x. Hence kp<=T. After floor(T/p) rounds a nonconstant restriction would allow one more disjoint block, impossible. Each round costs at most C1. A positive accepting transcript is a certificate of width at most T, so C1<=T.

R1 here is a worst-execution query cap, with no false positives. This constant is not transferred to the expected-cost Nisan convention. Constant functions use zero queries. No optimality claim for the quadratic leading constant.

## uniform-hypermatching-D-sensitivity-lift

On uniform k-hypermatchings with vertex-to-hyperedge queries, D(f)<=10368*(2k-1)^10*s(f)^10, k>=2.

- Kind: upper_bound; domain: total decision_function; classes: uniform_hypermatching_vertex_queries.
- Evidence: repository_derivation_checked; loss: domain_parameters.
- Source: Repository proof, Repository permutation-lift derivation from final-journal Lemmas 3.3,3.5,3.6 and Theorem 5.3.
- Proof: Lift f to permutations of kn vertices by grouping consecutive positions into k-sets. A permutation query or inverse query can be simulated with at most one hyperedge query by lazily assigning each newly discovered hyperedge to an unused position block. For t disjoint sensitive permutation transpositions, form a multigraph on original hyperedges. Sensitive swaps join distinct hyperedges, and each hyperedge has degree at most k because the transpositions use disjoint positions. Greedy matching gives at least t/(2k-1) swaps on disjoint hyperedge pairs, so s_perm<=(2k-1)*s_hyper. The permutation inequalities degree<=2s^2, bs<=6degree^2, C<=3s*bs and D<=2C^2 give D_perm<=10368*s_perm^10. Combine the query simulation and sensitivity comparison. The fresh source audit repairs the imported cube orientation to output/B-column transpositions; the constant survives.

A proved repository reduction with original-source inputs, not a priority or best-known claim. This does not establish an alpha-witnessing theorem or cover all lambda-partite hypermatching profiles. Empty/trivial domains are handled separately.

## completion-support-FC-RC

FC(f)<=2*RC(f) under the accepting-x-certainly, rejecting-opposites-with-probability-at-least-1/2, expected-query convention.

- Kind: upper_bound; domain: partial_or_total decision_function; classes: unrestricted.
- Evidence: repository_derivation_checked; loss: none.
- Source: [Aar02](https://arxiv.org/abs/quant-ph/0210020), Lemma 5 and the fractional certificate LP; repository directed extraction.
- Proof: Fix x and a verifier. Let q_i be its probability of querying i on x. Coupling to any opposite-output y forces a query to their disagreement set with probability at least 1/2. Union bound gives sum_{i:x_i!=y_i} 2q_i>=1, so 2q_i form a fractional certificate, of cost at most twice the expected number of queries. Clipping weights to one preserves feasibility. Maximize over x.

## C0-R1-2-sep-AIK

The AIK26 underlying DNF has C0=Theta(n^2) and capped R1=O(n).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [AIK26](https://arxiv.org/abs/2609.11664), Theorem 2.2; Lemma 3.4; Section 3.1.
- Proof: Lemma 3.4 ensures that any assignment of fewer than tau_n=n*(ceil(n/2)+1) variables consistent with all zeros still has a completion in the domain of H, hence a satisfying input of the underlying DNF. Therefore C0 at zero is Omega(n^2); input length gives the upper bound. The capped one-sided algorithm is Theorem 2.2.

## lambda-partite-D-sensitivity-product-lift

For lambda-partite perfect hypermatchings with k=sum_i lambda_i>=2, D<=10368*(2k-1)^10*s^10 under vertex-to-entire-hyperedge queries.

- Kind: upper_bound; domain: total decision_function; classes: lambda_partite_hypermatching_vertex_queries.
- Evidence: repository_derivation_checked; loss: domain_parameters.
- Source: Repository proof, Repository product-permutation lift using final-journal Theorems 5.3/5.5 and Lemmas 3.3,3.5,3.6.
- Proof: Represent a hypermatching by independent permutations of the lambda_i*n vertices in each color class, grouping lambda_i consecutive positions per common block label. Lazy simultaneous assignment of a discovered hyperedge to a free common block label simulates each forward/inverse permutation query using at most one hyperedge query. Products of the source permutation pseudo-characters span the product degree filtration and induce product cubes of at least half their degree, giving degree<=2s^2 on the permutation product. There Delta<=2, beta_c>=1/3, M=sum_i(lambda_i*n), and total set-input size is k*n. Thus C<=72s^5 and D<=2*C^2. Disjoint sensitive component transpositions form a multigraph on original hyperedges of maximum degree at most k; matching extraction gives s_product<=(2k-1)*s_hyper. Combine these inequalities. The simulation invariant is existential: every transcript admits a representative of the fixed input, not that all arbitrary completions project to it. Independent audit checked the tensor grading, full conflict threshold, simulation and matching argument. The fresh source audit repairs the imported cube orientation to output/B-column transpositions; the constant survives.

Repository derivation; separately audited by another assistant agent against original journal inputs. Not formal verification, human peer review, a printed source theorem, or a priority/best-known claim. The alpha=1/2 witnessing argument applies to the permutation product only, not directly to hypermatchings. Full-domain and oracle hypotheses remain essential.

## AIK26-Q0-Q-quadratic

The AIK26 total family gives Q0>=Omega_tilde(Q^2).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylog.
- Source: [AIK26](https://arxiv.org/abs/2609.11664), Theorems 2.1 and 2.3; Lemmas 7.3–7.4, article pp.4,19.
- Proof: Theorems 2.1 and 2.3 give Q<=O(sqrt(n)*log^3 n) and Q0=Theta(n*log^2 n). The zero-error lower bound restricts the count fields to AND on Theta(n*log^2 n) bits; a nonzero accepting amplitude for AND needs full degree. Exact term evaluation gives the matching Q0 upper bound. Together with C=Omega(n^2) and C=O(Q^4), logarithms of n and Q are comparable, yielding the quadratic lower exponent with polylog loss.

New catalogue consequence of the original paper’s jointly specified family, not a new independent construction. Query caps, exactness and detectable-failure conventions match the source preliminary definitions.

## AIK26-C-Q0-quadratic

The same AIK26 total family gives C>=Omega_tilde(Q0^2).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylog.
- Source: [AIK26](https://arxiv.org/abs/2609.11664), Theorems 2.1 and 2.3; Lemmas 7.3–7.4, article pp.4,19.
- Proof: Theorem 2.1 gives C>=Omega(n^2); Theorem 2.3 and Lemmas 7.3–7.4 give Q0=Theta(n*log^2 n). Thus C>=Omega(Q0^2/log^4 Q0). The count-field AND restriction forces the zero-error cost, and exact evaluation supplies its upper bound.

New catalogue consequence of the original paper’s jointly specified family, not a new independent construction. Query caps, exactness and detectable-failure conventions match the source preliminary definitions.

## AIK26-C-QE-quadratic

The same AIK26 total family gives C>=Omega_tilde(QE^2).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: polylog.
- Source: [AIK26](https://arxiv.org/abs/2609.11664), Theorems 2.1 and 2.3; Lemmas 7.3–7.4, article pp.4,19.
- Proof: Theorem 2.1 gives C>=Omega(n^2), while Theorem 2.3 gives QE=Theta(n*log^2 n). Hence C>=Omega(QE^2/log^4 QE). The exact algorithm finds the unambiguous terms, reads the selected bits and checks the addressed cheat-sheet cell; the AND restriction gives its lower bound.

New catalogue consequence of the original paper’s jointly specified family, not a new independent construction. Query caps, exactness and detectable-failure conventions match the source preliminary definitions.

## bs-s-superquadratic-baseline

There are total Boolean functions with unbounded sensitivity and bs(f)>=s(f)^(2.000252407).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_statement_and_proof_route_checked; loss: none.
- Source: [OAIsens26](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/paper.pdf), Original paper Theorem 1.1, Section 4 and Corollary 4.3; campaign OpenAI Baseline decimal certificate.
- Proof: Random edge labels exclude excessive simultaneous near-satisfied clauses. Four coupled profiles control ordinary sensitivity and simultaneous flips of distinct nested predicates. Block witnesses at zero multiply through recursion; OR balancing gives s<=2(d+2)M^(d+1) and bs at zero >=M^2(2M^2+1)^d for M>=9^(d+1). Composition multiplies the zero-input block lower bound and at most multiplies sensitivity.

Publication status: repository_preprint.

The decimal is the exact recorded target, not a rounded claim of a stronger power. Platform-attested does not mean independently kernel-checked by this catalogue. For campaign records the loss is conservatively retained at exponent level.

## bs-s-superquadratic-depth20

There are total Boolean functions with unbounded sensitivity and bs(f)>=s(f)^(2.006470828 - o(1)).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_platform_theorem_and_attestation_checked; loss: subpolynomial.
- Source: [P2Mdepth2026](https://prove2.me/missions/Block_Sensitivity_vs._Sensitivity%3A_Depth-20_Improvement), Mission description and completed goal; original general seed bounds in OAIsens26 Section 4.
- Proof: Specialize the same general seed bounds to depth twenty, certify the stated decimal below log(B)/log(A), and invoke finite-seed amplification. This is a stronger specialization, not a different base architecture.

The decimal is the exact recorded target, not a rounded claim of a stronger power. Platform-attested does not mean independently kernel-checked by this catalogue. For campaign records the loss is conservatively retained at exponent level.

## bs-s-superquadratic-2007

There are total Boolean functions with unbounded sensitivity and bs(f)>=s(f)^(2.007 - o(1)).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_platform_theorem_and_attestation_checked; loss: subpolynomial.
- Source: [P2M200726](https://prove2.me/missions/Block_Sensitivity_vs._Sensitivity%3A_Reach_2.007), Campaign completed entry; mission goal and certificate framework.
- Proof: The campaign records the asymptotic goal as proved. Its stated route is to certify a finite seed with s<=A, bs at a chosen input >=B, and A^2.007<=B, then use the shared normalization/composition theorem. The accepted proof body was not recovered here; this is a summary of the published certificate framework, not an assertion of its exact implementation.

The decimal is the exact recorded target, not a rounded claim of a stronger power. Platform-attested does not mean independently kernel-checked by this catalogue. For campaign records the loss is conservatively retained at exponent level.

## bs-s-superquadratic-20205

There are total Boolean functions with unbounded sensitivity and bs(f)>=s(f)^(2.0205 - o(1)).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_platform_theorem_and_attestation_checked; loss: subpolynomial.
- Source: [P2M2020526](https://prove2.me/missions/Block_Sensitivity_vs._Sensitivity%3A_Reach_2.0205), Mission construction description, specified parameters, exact certificate and PROVED goal.
- Proof: Retain four profiles, reduce the target-row count to fifteen, and split the gate estimate by whether the candidate tournament has a sink. The resulting finite certificate satisfies A^4041<B^2000, so A^2.0205<B. Apply the shared finite-certificate amplification theorem.

The decimal is the exact recorded target, not a rounded claim of a stronger power. Platform-attested does not mean independently kernel-checked by this catalogue. For campaign records the loss is conservatively retained at exponent level.

## bs-s-superquadratic-20391

There are total Boolean functions with unbounded sensitivity and bs(f)>=s(f)^(2.0391 - o(1)).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_platform_theorem_and_attestation_checked; loss: subpolynomial.
- Source: [P2M2039126](https://prove2.me/missions/Block_Sensitivity_vs._Sensitivity%3A_%CE%B1_%E2%89%A5_2.0391), Mission goal, explicit PROVED badge, campaign completed entry.
- Proof: The source marks the goal proved and records accepted activity. It formulates the finite-certificate route s<=A, bs at a chosen input >=B, A^2.0391<=B. The accepted proof body and actual seed parameters were not inspected; no more specific construction mechanism is asserted.

The decimal is the exact recorded target, not a rounded claim of a stronger power. Platform-attested does not mean independently kernel-checked by this catalogue. For campaign records the loss is conservatively retained at exponent level.

## bs-s-superquadratic-205

There are total Boolean functions with unbounded sensitivity and bs(f)>=s(f)^(2.05 - o(1)).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_platform_theorem_and_attestation_checked; loss: subpolynomial.
- Source: [P2M20526](https://prove2.me/missions/Block_Sensitivity_vs._Sensitivity%3A_Reach_2.05), Mission SensitivityCampaign.reach_205; explicit PROVED goal and accepted activity; campaign completed entry.
- Proof: The inspected mission marks reach_205 proved and displays accepted activity attributed to Robin Kothari. The stated certificate criterion is s<=A, bs at a chosen input >=B, and A^(41/20)<=B, followed by the shared amplification theorem. The accepted proof body was not retrieved, so its exact seed and proof route remain source-extraction gaps.

The decimal is the exact recorded target, not a rounded claim of a stronger power. Platform-attested does not mean independently kernel-checked by this catalogue. For campaign records the loss is conservatively retained at exponent level.

## bs-s-superquadratic-20635

For every epsilon>0 and every integer S>=2 there is a total Boolean function f with s(f)>=S and bs(f)>=s(f)^(alpha-epsilon), where alpha=2.0635.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_platform_theorem_and_attestation_checked; loss: subpolynomial.
- Source: [P2M2063526](https://prove2.me/theorems/f4a6abf1-69b0-4785-a7d9-cd45649231b2), Public quantified theorem, construction/provenance notes and dated campaign completed entry; theorem f4a6abf1-69b0-4785-a7d9-cd45649231b2.
- Proof: The tracker now records the exact target 4127/2000 proved. Later Kothari/Codex sources identify accepted submission f80a3f37-72fa-4d56-a094-3e4d351764f3 as their foundation. The theorem provenance still contains stale prose saying full verification is outstanding; the dated proved badge and tracker supersede that status wording. Actual seed and proof details remain unextracted. Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

## bs-s-superquadratic-2075

For every epsilon>0 and every integer S>=2 there is a total Boolean function f with s(f)>=S and bs(f)>=s(f)^(alpha-epsilon), where alpha=2.075.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_platform_theorem_and_attestation_checked; loss: subpolynomial.
- Source: [P2M207526](https://prove2.me/theorems/49fdd176-c319-4f1e-b15f-b1fd5130f0bc), Public quantified theorem, construction/provenance notes and dated campaign completed entry; theorem 49fdd176-c319-4f1e-b15f-b1fd5130f0bc.
- Proof: Joint-change bounds and finite labeling existence control the nine sensitivity profiles; construct disjoint block witnesses and certify the finite exponent 83/40 by exact integer arithmetic. The public record identifies Full2075.lean, SHA-256 b8b3d440c3c148ee8401967fc8f2270df9c8c142dfb63f8fde28dfb88bf8c152, and accepted submission 819ad4c6-aa25-48ca-82e9-c8df39c182c0. Apply the campaign finite-certificate theorem. The actual seed integers are not exposed in the public summary. Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

## bs-s-superquadratic-2085

For every epsilon>0 and every integer S>=2 there is a total Boolean function f with s(f)>=S and bs(f)>=s(f)^(alpha-epsilon), where alpha=2.085.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_platform_theorem_and_attestation_checked; loss: subpolynomial.
- Source: [P2M208526](https://prove2.me/theorems/7e54a28e-196b-40a3-a2c0-957e75db9e4f), Public quantified theorem, construction/provenance notes and dated campaign completed entry; theorem 7e54a28e-196b-40a3-a2c0-957e75db9e4f.
- Proof: Refine the finite sensitivity-profile certificate and assemble actual Boolean functions, then invoke finite-seed amplification. The source names Sensitivity20855.finite_seed and achieves_20855 and accepted submission c6096517-61e7-4f51-bc68-c1521d61eb65. The public target is exactly 2.085; the internal declaration name alone is not evidence for a 2.0855 bound. Seed integers remain unavailable. Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

## bs-s-superquadratic-2119

For every epsilon>0 and every integer S>=2 there is a total Boolean function f with s(f)>=S and bs(f)>=s(f)^(alpha-epsilon), where alpha=2.119.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_platform_theorem_and_attestation_checked; loss: subpolynomial.
- Source: [P2M211926](https://prove2.me/theorems/cf005af0-93b2-44c1-991f-ddab41d85874), Public quantified theorem, construction/provenance notes and dated campaign completed entry; theorem cf005af0-93b2-44c1-991f-ddab41d85874.
- Proof: An exact two-stage invariant improves the profile recurrence in the inherited nine-predicate framework. The source reports standalone verification and accepted submission bb3251a4-f00f-4b06-962a-97be2de5db1b. The public summary does not specify each parameter’s recurrence role, so no unprinted formula is inferred from their names. Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

## bs-s-superquadratic-21

For every epsilon>0 and every integer S>=2 there is a total Boolean function f with s(f)>=S and bs(f)>=s(f)^(alpha-epsilon), where alpha=2.1.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_platform_theorem_and_attestation_checked; loss: subpolynomial.
- Source: [P2M2126](https://prove2.me/theorems/34794a98-e5bd-4623-ae65-526fc87e9ad1), Public quantified theorem, construction/provenance notes and dated campaign completed entry; theorem 34794a98-e5bd-4623-ae65-526fc87e9ad1.
- Proof: Use the current campaign completed status for the exact formal 21/10 goal. The stronger informal 2.105 label is not imported as a verified exponent: the public formal target at this theorem remains 2.10. Accepted proof details are not public without authentication. Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

## bs-s-superquadratic-2127294

For every epsilon>0 and every integer S>=2 there is a total Boolean function f with s(f)>=S and bs(f)>=s(f)^(alpha-epsilon), where alpha=2.127294.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_platform_theorem_and_attestation_checked; loss: subpolynomial.
- Source: [P2M212729426](https://prove2.me/missions/Block_Sensitivity_vs._Sensitivity%3A_Reach_2.127294), Public quantified theorem, construction/provenance notes and dated campaign completed entry.
- Proof: Sharpen joint boundary estimates in the twelve-predicate recursion, then prove the campaign asymptotic goal. The tracker records completion on 20 October 2026; exact seed parameters and the accepted proof body remain unavailable in the inspected public record. Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

## bs-s-superquadratic-21301

For every epsilon>0 and every integer S>=2 there is a total Boolean function f with s(f)>=S and bs(f)>=s(f)^(alpha-epsilon), where alpha=2.1301.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_platform_theorem_and_attestation_checked; loss: subpolynomial.
- Source: [P2M2130126](https://prove2.me/theorems/ff7ef69d-ca91-413b-872c-cf760dc244dc), Public quantified theorem, construction/provenance notes and dated campaign completed entry; theorem ff7ef69d-ca91-413b-872c-cf760dc244dc.
- Proof: Multiple defect tolerances and coupled target/guard profiles improve a periodic recursion. Verify the shared labeling conditions and actual disjoint block assembly, then obtain the finite-family bounds and the logarithmic exponent log(G)/log(R)>2.1301. The construction must bound sensitivity at every input and exhibit nonempty pairwise disjoint sensitive blocks at zero. Fixed prefactors are absorbed into an arbitrary positive exponent loss; the known polynomial relation between block sensitivity and sensitivity ensures unbounded sensitivity. Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

## bs-s-superquadratic-21303

For every epsilon>0 and every integer S>=2 there is a total Boolean function f with s(f)>=S and bs(f)>=s(f)^(alpha-epsilon), where alpha=2.1303.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_platform_theorem_and_attestation_checked; loss: subpolynomial.
- Source: [P2M2130326](https://prove2.me/theorems/637bbe88-761a-4bb9-bad9-78a8c1bb90c7), Public quantified theorem, construction/provenance notes and dated campaign completed entry; theorem 637bbe88-761a-4bb9-bad9-78a8c1bb90c7.
- Proof: Apply the finite asymmetric Lovasz local lemma to simultaneous bad-label events, proving joint independence, dependency counts and an exact integer activity certificate. A coupled four-stage profile recurrence and actual Boolean/block assembly give the finite family. Its exponent log(G)/log(R)>2.1303. The construction must bound sensitivity at every input and exhibit nonempty pairwise disjoint sensitive blocks at zero. Fixed prefactors are absorbed into an arbitrary positive exponent loss; the known polynomial relation between block sensitivity and sensitivity ensures unbounded sensitivity. The mission description preserves a historical server-timeout note; the supporting finite-family theorem is now publicly marked Proved. Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

## bs-s-superquadratic-213

For every epsilon>0 and every integer S>=2 there is a total Boolean function f with s(f)>=S and bs(f)>=s(f)^(alpha-epsilon), where alpha=2.13.

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_platform_theorem_and_attestation_checked; loss: subpolynomial.
- Source: [P2M21326](https://prove2.me/missions/Block_Sensitivity_vs._Sensitivity%3A_Reach_2.13), Public quantified theorem, construction/provenance notes and dated campaign completed entry.
- Proof: The tracker records the 2.13 goal completed. Independently, AchievesExponent(2.1301) implies AchievesExponent(2.13) by replacing epsilon with epsilon+0.0001. This is a valid implication from the public stronger theorem, not a claim about the unretrieved accepted 2.13 proof implementation. Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

## bs-s-superquadratic-21308255793978239

For every epsilon>0 and every integer S>=2 there is a total Boolean function f with s(f)>=S and bs(f)>=s(f)^(alpha-epsilon), where alpha=log(14055^8)/log(3738277295413674).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_platform_theorem_and_attestation_checked; loss: subpolynomial.
- Source: [P2M2130825579397823926](https://prove2.me/theorems/01bb63ef-ced2-4ae9-8b81-b5ed295526c6), Public quantified theorem, construction/provenance notes and dated campaign completed entry; theorem 01bb63ef-ced2-4ae9-8b81-b5ed295526c6.
- Proof: Share one labeling across six ordinary defect tolerances and a source tolerance; feed the simultaneous bounds into a recursive Boolean sensitivity profile and block amplification. The public primitive theorem explicitly expands sensitivity and block sensitivity as finite maxima, proves the full asymptotic quantifiers, and strictly improves log(14055^8)/log(3738289747988852). The campaign wrapper transfers the primitive definitions to the shared ones. Accepted construction submission: a9d25c46-43bd-4fb1-826b-0ed075b8cf0a. The exact exponent is logarithmic, not the truncated tracker decimal. Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

## bs-s-superquadratic-coupled-exact

The campaign quantified separation holds at exact exponent alpha=log(201838849)/log(7922).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_platform_theorem_and_attestation_checked; loss: subpolynomial.
- Source: [P2Mcoupledexact26](https://prove2.me/theorems/ddfe4bf3-88be-4876-a196-33c20c0319ff), Public exact endpoint/finite-family theorem ddfe4bf3-88be-4876-a196-33c20c0319ff.
- Proof: Multiple defect tolerances and coupled target/guard profiles improve a periodic recursion. Verify the shared labeling conditions and actual disjoint block assembly, then obtain the finite-family bounds and the logarithmic exponent log(G)/log(R)>2.1301. The construction must bound sensitivity at every input and exhibit nonempty pairwise disjoint sensitive blocks at zero. Fixed prefactors are absorbed into an arbitrary positive exponent loss; the known polynomial relation between block sensitivity and sensitivity ensures unbounded sensitivity. Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

## bs-s-superquadratic-shared-exact

The campaign quantified separation holds at exact exponent alpha=log(25260794820729601)/log(50063687).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_platform_theorem_and_attestation_checked; loss: subpolynomial.
- Source: [P2Msharedexact26](https://prove2.me/theorems/2bc2b8ee-797d-4500-9dc8-9b23c457e131), Public exact endpoint/finite-family theorem 2bc2b8ee-797d-4500-9dc8-9b23c457e131.
- Proof: Apply the finite asymmetric Lovasz local lemma to simultaneous bad-label events, proving joint independence, dependency counts and an exact integer activity certificate. A coupled four-stage profile recurrence and actual Boolean/block assembly give the finite family. Its exponent log(G)/log(R)>2.1303. The construction must bound sensitivity at every input and exhibit nonempty pairwise disjoint sensitive blocks at zero. Fixed prefactors are absorbed into an arbitrary positive exponent loss; the known polynomial relation between block sensitivity and sensitivity ensures unbounded sensitivity. The mission description preserves a historical server-timeout note; the supporting finite-family theorem is now publicly marked Proved. Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

## bs-s-superquadratic-refined-exact

The campaign quantified separation holds at exact exponent alpha=log(25260794820729601)/log(50063523).

- Kind: separation; domain: total decision_function; classes: unrestricted.
- Evidence: primary_platform_theorem_and_attestation_checked; loss: subpolynomial.
- Source: [P2Mrefinedexact26](https://prove2.me/theorems/62961329-4b50-48c7-a1fd-11159da9de26), Public exact endpoint/finite-family theorem 62961329-4b50-48c7-a1fd-11159da9de26.
- Proof: Keep the shared labeling and block amplification of the four-stage construction, refine the finite sensitivity recipe from growth factor 50063687 to 50063523, and retain block growth 12607^4. Absorb the fixed prefactor into positive exponent loss. Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

Public construction summary and quantified theorem checked; accepted Lean proof body is behind authentication and has not been downloaded or replayed by this atlas.

## hypermatching-degree-sensitivity-descent

For full lambda-partite perfect hypermatchings with k=sum_i lambda_i>=2 and n>=2, degree_H(f)<=(2k-1)*s_H(f)^2.

- Kind: upper_bound; domain: total decision_function; classes: lambda_partite_hypermatching_vertex_queries, uniform_hypermatching_vertex_queries.
- Evidence: repository_derivation_checked; loss: domain_parameters.
- Source: Repository proof, Derived research proof, docs/hypermatching-proof.md; full source audit 23 October 2026.
- Proof: Average entry polynomials over uniform representation fibers; partition-lattice inversion gives 2degree_H<=degree_Z. Corrected output/B-column pseudo-characters give a correlated D-dimensional cube with D>=degree_Z/2. Nonzero top correlation excludes loop axes. A matching of at least D/(2k-1) axes yields an injectively projected native face after some fixing preserving its top coefficient. Huang gives s_H^2>=D/(2k-1).

The printed DFLLV26 input/A-column cube orientation fails in S_3. The separate proof uses output/B-column transpositions, directly checks homogeneous filtration, and preserves native disjointness. No intrinsic hypermatching witnessing family is asserted.

## exact-search-two-query-rigidity

For full-cube total certificate-output search, QE(S)<=2 implies D(S)<=2, and D(S)=QE(S) whenever QE(S)<=2.

- Kind: parameterized_upper_bound; domain: total search_relation; classes: certificate_output_search, exact_quantum_at_most_two_queries.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Derived research note, docs/exact-search-proof.md; fresh independent source audit 23 October 2026.
- Proof: A T-query amplitude supported on an output certificate factors as its subcube indicator times a polynomial on the unassigned coordinates, with degrees adding. At T=2 every width-two output probability is a constant nonnegative multiple of its indicator. Exclude all allowed singleton outputs on a residual subcube. A nonnegative 2x2 additive-table decomposition supplies a two-query tree there; provenance of residual singleton terms supplies one-coordinate singleton fallbacks making the tree correct on the whole cube. The T=0,1 cases are proved separately.

Small-query rigidity only; this is not an asymptotic exponent-one inequality. The asymptotic BK24 Open Problem 1 remains separately recorded. Publication priority is not certified.

## four-query-4maj-certificate-obstruction

For the fixed full-cube eight-output 4-MAJ certificate partition S, D(S)=QE(S)=4.

- Kind: identity; domain: total search_relation; classes: certificate_output_search, fixed_four_bit_4maj_certificate_partition.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Derived proof, docs/width-three-proof.md, exact 10-orbit affine certificate and PSD star trace contradiction.
- Proof: At three queries, width-three output amplitudes force identical endpoint states and a fixed final Gram. Last-query support constraints and the 48 partition symmetries reduce all possible quadratic prefix Grams to a scalar multiple of one six-by-six matrix; exact orbit equations independently reconstruct this identity. Its forced star signs require twice the available trace for any two-query prefix. The old partition and classical lower bound are credited to KRS15.

Known 4-MAJ partition and known classical D=4; exact quantum eight-output lower-bound priority not certified. No asymptotic exponent or separation is inferred.

## rooted-path-native-influence

For ancestor-descendant tree-path Fourier support of length at most d, max_e I_e(p)>=Var(p)^2/(8d osc(p)^2); a self-contained moment proof gives denominator 12d instead.

- Kind: multivariate_lower_bound; domain: total real_valued_function; classes: ancestor_descendant_tree_path_fourier_support.
- Evidence: repository_derivation_checked; loss: none.
- Source: Repository proof, Derived classical-method consequence, docs/rooted-paths-proof.md; Szarek76 Theorem 1 for the sharper constant.
- Proof: Prefix characters turn path monomials into endpoint pairs. Orient endpoints from descendants to ancestors to get outdegree at most d. Symmetric polarization, convex sign rounding and the Rademacher L1 inequality control the sum of incident coefficient l2 norms by oscillation. Charging coefficients to tails controls Fourier l1 mass; a largest original coefficient supplies a native influence without identifying transformed influences. Root-anchor homogenization preserves range. The fourth-moment version is self-contained; sharp Khintchine improves 12d to 8d.

Explicit consequence of classical quadratic-chaos methods; no analytic novelty, general AA resolution, or optimality certification. Degree is the original path-length bound. Broader known coefficient estimates give other tree-path influence consequences.
