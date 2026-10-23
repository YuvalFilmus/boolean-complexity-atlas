# Fresh independent audit: exact two-query certificate search

23 October 2026. Audited manuscript: `outputs/open-problem-progress-round2-2026-10-23/exact-search-two-query.md`. This reviewer did not author or review the second-round argument previously. The proof was checked from the quantum query model and elementary multilinear algebra, including its imported amplitude lemma. The publication version is [the complete proof](exact-search-proof.md).

## Verdict and exact scope

**PASS.** For a finite collection S of partial assignments on N Boolean bits, with the input domain the full Boolean cube, if an exact standard bit-oracle algorithm always outputs a member of S extended by its input and makes at most two queries in the worst case, then D(S)<=2. Consequently D(S)=Q_E(S) whenever Q_E(S)<=2.

The proof remains valid with complex amplitudes, input-independent mixed initial states, finite intermediate measurements and adaptive control, and a general finite final POVM. These model extensions must be explained if they are intended; the manuscript's short deferred-measurement sentence is correct but compressed. The proof does not cover a promise subset, postselection, expected-time zero-error complexity, arbitrary output relations whose labels are not specified partial assignments, or a model granting a stronger oracle at unit cost.

There is no asymptotic resolution of BK24 Open Problem 1. Published novelty and overlap with fractional partition results are separate questions; this audit does not certify novelty.

## Actual primary sources inspected

1. Robert Beals, Harry Buhrman, Richard Cleve, Michele Mosca and Ronald de Wolf, *Quantum lower bounds by polynomials*, Journal of the ACM 48(4), 778–797 (2001), DOI 10.1145/502090.502097. Inspected author preprint arXiv:quant-ph/9802049v3, 30 September 1998, local `work/sources/BBCMW01.pdf` and its extracted `.txt`. Section 3.2, PDF p.4, defines the standard XOR bit oracle on |i,b,z>, complex amplitudes, and probability-one exactness. Lemma 4.1 and its proof, PDF pp.4–5, prove degree-at-most-T complex multilinear final amplitudes. The proof explicitly uses input-independent linearity between queries, not a special real-amplitude assumption. Lemma 4.2, PDF p.5, sums squared amplitudes to obtain output probabilities, but the new argument requires the stronger amplitude statement of Lemma 4.1 rather than merely degree-at-most-2T probabilities. Source PDF: 10 pages, SHA256 `afec116657493976b70df7dcb8b174c8c0be55a9337d9e035afd5f1fc4d9cd4c`.
2. Shalev Ben-David and Srijita Kundu, *Separations in query complexity for total search problems*, arXiv:2410.16245v1 (2024). Inspected local `work/sources/BK24.pdf` and `.txt`. Section 2.1, manuscript pp.9–10/PDF pp.9–10, defines S as a set of partial assignments and the search relation by c subset x, distinguishing certificate-output search from a general relation merely having short certificates. Section 2.2, manuscript p.11/PDF p.11, defines Q_E by probability-one correctness and fixed query count, separately from expected Las Vegas Q_0. Section 1.3, Open Problem 1, is the broad exact-quantum/randomized separation question. Source PDF: 47 pages, SHA256 `3812ede6832eeadf0665f8ac895bb3e923a6f14a119383d91365e8e387373dd3`.

The row-plus-column decomposition and singleton fallback were reproved below rather than accepted as external results. No purported sufficiency of polynomial/SOS constraints for quantum algorithms is used.

## 1. Quantum amplitudes, measurement and adaptivity

Under the standard oracle O_x|i,b,z>=|i,b XOR x_i,z>, an amplitude after a query is (1−x_i)alpha+x_i beta, or x_i alpha+(1−x_i)beta, for the two possible answer-bit values. It increases polynomial degree by at most one. Input-independent linear maps combine amplitudes with constant complex coefficients. Induction, followed by x_i^m=x_i on Boolean inputs, therefore gives multilinear amplitudes of degree at most T. This is exactly the inspected original Lemma 4.1 proof.

A mixed initial state can be purified with an input-independent environment. Intermediate measurement outcomes can be kept coherently in an orthogonal history register and subsequent operations controlled on that register; no postselection or normalization by outcome-dependent probabilities is performed. A history branch that terminates early can be padded without extra effective information by querying a dummy target |+>, which the XOR oracle fixes. Controlled swapping of the active answer register with this dummy implements a branchwise skipped query with one ordinary bit-oracle call, so padding a worst-case-T adaptive solver preserves T. N=0 is trivial and needs no oracle.

For an arbitrary final finite POVM {E_c}, append the input-independent isometry

V|psi>=sum_c |c> sqrt(E_c)|psi>.

Its norm preservation follows from sum_c E_c=I. This converts the POVM into a basis measurement of a labeled output register and a work register without changing query count or amplitude degrees. Equivalently every resulting amplitude is an input-independent linear combination of the previous ones. Thus output c has probability sum_r |a_{c,r}(x)|^2, where each a_{c,r} is a degree-at-most-T complex multilinear polynomial. Auxiliary failure/other outcomes, if included, have zero probability on every input of an exact solver. Classical randomness can be included in an orthogonal environment as well.

The standard finite-dimensional fixed-query model is sufficient. No infinite runtime, unbounded query branches, or postselected amplitudes are admitted.

## 2. Full-cube support factorization

Fix a certificate c with coordinate set K. Exactness on every Boolean input implies p_c(x)=0 whenever x fails to extend c. Since p_c is a sum of nonnegative squared magnitudes, each amplitude a_{c,r}(x) separately vanishes at every such x.

Let b(y)=a_{c,r}(c,y), a function of the remaining coordinates. Let its unique complex multilinear polynomial represent it. Pointwise on the full cube,

$$
a_{c,r}(x)=1_c(x)b(x_{[N]\setminus K}).
$$

If x extends c, this is the definition of b; otherwise both sides vanish. Uniqueness of multilinear representation therefore makes this an identity of multilinear polynomials, not merely a divisibility assertion modulo an unspecified promise ideal.

If b is nonzero, the variables of b are disjoint from K, and the leading monomial in the product of all certificate-literal factors has nonzero coefficient ±1. Multiplying it by a nonzero highest-degree monomial of b produces a nonzero monomial of total degree |K|+deg b. No other terms cancel it. Thus

$$
\deg a_{c,r}=|K|+\deg b\ge |K|.
$$

For T=2, certificates wider than two have every amplitude identically zero. For width exactly two every surviving b is constant, so

$$
p_c(x)=w_c1_c(x),\qquad w_c=\sum_r|b_r|^2\ge0.
$$

These statements do not assume all allowed certificates are used. An unused certificate simply has w_c=0. Complex phases or destructive interference within an amplitude do not evade the argument; factorization is applied after forming that amplitude, while distinct outcome probabilities cannot cancel.

## 3. Nonnegative width-two partition lemma

Consider an identity sum_c w_c1_c=1 on an unrestricted cube, with constant weights w_c>=0 and certificate widths at most two. A positive empty certificate immediately gives a valid zero-query output, regardless of its weight. Ignore zero-weight certificates.

For a fixed coordinate pair {i,j}, write its four weights w_00,w_01,w_10,w_11. The coefficient of x_i x_j in the normalization identity is exactly

$$
w_{00}-w_{01}-w_{10}+w_{11}=0.
$$

No singleton or different coordinate pair contributes to that monomial. Hence the difference w_0b−w_1b is independent of b. Set u_a=min_b w_ab and v_b=w_ab−u_a. Translating a row by a constant translates its minimum by the same constant, so v_b does not depend on a and is nonnegative. All u_a are nonnegative as well. Thus w_ab=u_a+v_b.

Summing the corresponding pair indicators gives u_0(1−x_i)+u_1 x_i+v_0(1−x_j)+v_1 x_j. Positive u_a requires both original weights w_a0,w_a1 to be positive; positive v_b similarly requires both w_0b,w_1b positive. Coalescing identical certificates changes no support or permissible output.

After decomposing every pair and retaining the original singleton contributions, normalization becomes

$$
\sum_i[\alpha_{i0}(1-x_i)+\alpha_{i1}x_i]=1,
\quad \alpha_{ib}\ge0.
$$

Linear coefficient comparison gives alpha_i0=alpha_i1, and the constant coefficient gives sum_i alpha_i0=1. Some coordinate therefore has positive contributions on both branches. Query it. For each branch select one positive original singleton contribution, or one positive complete-row/complete-column contribution. The former already gives a valid output; in the latter querying its partner selects a valid original pair certificate. The choices can differ by root outcome. This is a deterministic tree of depth at most two.

This is a support conclusion derived from weights. It does not require constructing a quantum algorithm from the resulting weighted partition.

## 4. Singleton fallback and the full-cube tree

If S contains an empty certificate, output it. If it contains both singleton literals of some coordinate, query that coordinate and output the corresponding singleton. Otherwise every coordinate has at most one allowed singleton literal. Fix each such coordinate to its opposite value, obtaining a nonempty residual cube H. The simultaneous fixing is consistent because each coordinate has only one such constraint; the residual cube can be a point.

On H every allowed singleton is invalid, and therefore has output probability zero. No certificate of width greater than two can be output anywhere. Normalization of the exact solver therefore gives a constant nonnegative partition of H by its width-two certificates. Terms incompatible with H vanish; each compatible term restricts to width zero, one or two on the free coordinates.

If a positive term restricts to width zero, its original pair consists of two fixed coordinates. Query them sequentially. Any mismatch with H satisfies the corresponding allowed singleton, which can be output immediately. If both match, output the original pair. This uses at most two queries on every full-cube input, including inputs not in H.

Otherwise apply the width-two lemma on the free coordinates. It chooses a free root coordinate i and, for each outcome, a positive source contribution. A residual singleton comes from an original pair containing i and exactly one fixed coordinate j. Query j next: agreement with H makes that original pair valid, and disagreement makes the allowed singleton on j valid. A complete row or column of a residual pair involves two free coordinates, so its original pair has no additional fixed-coordinate condition; query its free partner and output the indicated original certificate.

There is no requirement to check every coordinate fixed in defining H. Only the one fixed coordinate in the selected original pair matters. An input outside H may disagree at unrelated fixed coordinates, but that cannot invalidate the selected output. If there are no free coordinates, the normalized partition necessarily has a positive width-zero residual term, already handled.

Thus every branch has at most two queries and returns an actual member of S extended by the actual input. Certificate labels are not replaced by arbitrary scalar function values.

## 5. Equality and boundary cases

The theorem proves D<=2 if Q_E<=2. Deterministic simulation always gives Q_E<=D. To infer equality also when Q_E is zero or one, the same amplitude argument supplies the needed smaller thresholds directly: at T=0 a nonzero output amplitude can only label an empty certificate; at T=1 every used nonempty certificate has width one with constant probability weight. Its normalized singleton identity either contains an empty certificate or gives opposite singleton outputs at some coordinate by linear coefficient comparison. Hence D<=T for T=0,1 too. The equality claim therefore does not rely on an uninspected earlier research note.

N=0 or N=1 causes no exception. Wide unused labels, duplicate labels for the same partial assignment, ancillas, complex amplitudes, and different second queries in the two classical branches cause no exception.

## 6. Explicit obstruction checked

The displayed three-bit cover consists of pair assignments 12=00,01,10; 13=10; 23=11. It is total. At inputs 010 and 011, a constant-weight partition would force respectively w_(12,01)=1 and w_(12,01)+w_(23,11)=1, whereas input 111 forces w_(23,11)=1. This is contradictory, so no exact two-query solver exists. A three-query solver reads all bits, so Q_E=3. An independent decision-tree recurrence also gives D=3; see the finite check below.

This example does not contradict the main theorem. It shows why certificate width alone is insufficient; a normalized nonnegative partition is an additional necessary condition of the actual exact quantum solver.

## 7. Independent exact finite check

New script: `tests/exact_search_independent_check.py`. It does not reuse the author's row/column support test. For three-bit width-two certificates, each certificate is an edge of the ordinary three-cube. A normalized nonnegative constant-weight partition is a fractional perfect matching in the supported cube subgraph. Because the graph is bipartite, this exists exactly when Hall's subset inequalities hold, equivalently when a perfect matching exists. Necessity follows by summing fractional degrees over any side subset; sufficiency is the ordinary finite bipartite matching theorem, or direct enumeration here.

The script checks Hall's condition on all subsets of the four even vertices and compares it with a separate recursive minimax decision-tree computation on all 4,096 supports. Result: 1,699 total covers, comprising 1,431 with D=2 and 268 with D=3. Exactly the 1,431 depth-two covers satisfy the fractional normalized-partition feasibility test. The explicit displayed cover has D=3 and fails Hall's condition. All checks use integers and finite sets, not a floating-point SDP or the quantum-realizability converse.

The author's much larger mixed singleton/pair enumeration was read but is not itself the independent test reported here. Its crucial singleton handling is proved directly in Section 4. Finite tests supplement the proof and do not establish the arbitrary-N theorem.

## Publication recommendation

The mathematical statement is supported with its exact certificate-output/full-cube/fixed-query qualifiers. If published on the atlas, label it a derived research result, retain the necessary-condition-versus-realizability distinction and the unresolved novelty status, link a separate complete proof, and explain finite POVM/adaptive padding and the T=0,1 equality cases so the displayed equality is self-contained. Do not change the general BK24 exact-search question to solved.

## Review of the exact publication rewrite

The same fresh reviewer subsequently read the complete publication source [exact-search-proof.md](exact-search-proof.md). Verdict: **PASS, no mathematical drift.** The rewrite explicitly states inactive-query conventions, proves the zero- and one-query equality cases, and checks each root obstruction for the three-query example. The publication audit manifest binds the reviewed proof and these audit pages by SHA-256.
