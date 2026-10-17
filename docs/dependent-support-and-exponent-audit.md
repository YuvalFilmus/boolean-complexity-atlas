# Dependent-support normalization, completion intervals and hypermatching lift

Later status: see [unmatched intervals and kernel-line audit](unmatched-and-kernel-line-audit.md), including the general lambda-partite product lift.

The 23-measure completion inventory now has 442 finite exponent intervals and 64 no-finite-power directions. Of the finite intervals, 254 have matching upper and lower exponents in the recorded evidence. This is an exponent comparison, not a certification of all endpoint losses, best-known constants or literature completeness. The new interval records retain the witness, transformations, exact exponent expressions and source-claim paths.

## Capped one-sided randomization

The catalogue's R1 has a worst-execution query cap T, no false positives and positive-input success probability p=2/3. Under that convention,

`D <= floor(T/p)*C1 <= T^2/p`.

Here is a direct proof. Query a consistent positive certificate in each round, recording every revealed literal. At any surviving zero input x, change only the conflicting literals of each chosen certificate to produce a positive input y_j. The disagreement sets are nonempty and disjoint, because a later chosen certificate must agree with all earlier revealed literals. Coupling the one-sided randomized algorithm on x and y_j forces it to query disagreement set j with probability at least p: otherwise an accepting computation on y_j would also accept x. Summing these hit probabilities gives kp<=T for k such disjoint sets.

After floor(T/p) certificate rounds, a nonconstant remaining restriction would supply another consistent positive certificate and hence one more disjoint set, contradicting that inequality. Each round costs at most C1. Finally, a positive-probability accepting transcript is a certificate of length at most T, so C1<=T. Constant functions need no queries.

For p=2/3 the resulting coefficient is 3/2. No optimal leading constant for the quadratic bound is claimed. OR on three bits, querying a uniformly chosen pair, attains equality in the intermediate product bound D<=T*C1/p. This capped proof is distinct from the previously audited expected-cost Nisan factor-four repair.

This tightens seven completion upper exponents from 3 to 2, including D, R0, QE, Q0 and unambiguous certificate measures versus completion_R1. AIK26's original Theorem 2.2 was revisited: its quadratic C-versus-R1 witness and C<=D give the matching D-versus-R1 lower exponent. The proof route is randomized elimination in its underlying unambiguous DNF; the original preliminary definitions explicitly use the capped, no-false-positive orientation.

## Transferred lower bounds

The new lower-bound generator transfers original total witnesses through the same audited upper graph. If a witness gives X>=Y^ell, while X<=O(A^u) and B<=O(Y^v), then every target exponent below ell/(u*v) is excluded. It preserves exact logarithmic exponent expressions where stored and retains source endpoint losses.

Complementing a witness swaps C0/C1 and UC0/UC1; it preserves the other relevant measures except oriented R1, which is not treated as complement invariant. If a witness is stated for C=max(C0,C1) and its denominator is complement invariant, choose an infinite fixed-side subsequence and complement if necessary to obtain either prescribed side. Parity supplies a baseline: all 23 listed measures are Theta(n), except QC=Theta(sqrt(n)) by the quantum-certificate characterization. Total witnesses have unique completions.

GSS13 Theorem 32 and its construction were revisited. Random sparse codewords are far apart but hit large subcubes; an OR composition then gives C=Omega(n^2), fbs=O(n). This witnesses the quadratic certificate/fractional-certificate gap, and via QC=Theta(sqrt(FC)) supports further transferred bounds. These are consequences of existing witnesses, not new independent separations.

## The exact missing normalization control

Fix the original supported uniform Walsh characters S. Let A be their promise evaluation matrix and v_x their vector of values at a cube input x. Define the diagnostic

`kappa = max_x max { |v_x^T Delta| : A Delta=0, ||Delta||_infinity<=1 }`.

Finite LP duality gives exactly

`kappa = max_x min_y ||v_x-A^T y||_1`.

The feasible kernel-box set is symmetric, so the absolute-value maximum equals the positive linear-functional maximum. Dualizing the box constraints produces the l1 distance to the row space. The primal is feasible and bounded, so strong duality applies. In particular, 0<=kappa<=|S|, and kappa=0 exactly when the domain kernel is trivial, since distinct full-cube Fourier characters are linearly independent.

For any actual domain-preserving perturbation of coefficient infinity norm at most M, global boundedness of p gives

`||p_Delta||_infinity <= 1+kappa*M`.

With full-cube margin gamma, the sign-approximation construction therefore gives degree `O(d*(1+kappa*M)/gamma)`. This works for dependent supports as well as independent ones. Polynomial kappa, M and inverse margin suffice for polynomial overhead. Kappa is a repository diagnostic, not a measure named in the source, and no polynomial bound on it follows here from support minimality alone. It is a worst-case amplification over all kernel vectors, so a large kappa does not itself refute existence of a useful perturbation or the final decision-complexity conclusion.

Support minimality also gives a necessary geometric obstruction. Along a kernel direction h, compare the first coefficient-zero time with the end of the feasible interval |p+t h|<=1 over all cube points. If the zero occurs while that whole segment remains feasible, the resulting polynomial preserves the promise and degree but has smaller support, a contradiction. In dependent-support cases, range constraints can stop the movement first, even immediately at an already saturated cube point. This explains why the coefficient-l1 elimination proof cannot simply be extended to every bounded polynomial. The previously proved l1<=1 and independent-character sufficient cases remain valid; the unrestricted higher-degree case remains proof-pending.

## Uniform hypermatchings: a separate query lift

A new seventh profile treats partitions of kn vertices into n unordered k-sets, with an oracle revealing the block containing a vertex. For k>=2, a repository reduction gives

`D_hyper(f) <= 10368*(2k-1)^10 * s_hyper(f)^10`.

Lift f to permutations of kn vertices by grouping consecutive positions into k-sets. Simulate a forward permutation query lazily: if its position block is unassigned, query an unused vertex's hyperedge and assign that edge to the block. For an inverse query to an undiscovered vertex, query its edge and assign it to an unused position block. Assign all vertices of a discovered block consistently. Each permutation query costs at most one hyperedge query, and at every transcript there exists a complete representation of the fixed original partition following that transcript. Hence D_hyper<=D_perm of the lift.

To compare sensitivities, take t disjoint sensitive transpositions at a lifted permutation. Each joins two distinct original hyperedges. Form a multigraph whose vertices are those hyperedges and whose edges are the swaps. Its maximum degree is at most k, because the transpositions use disjoint positions. Greedily selecting edges gives a matching of size at least t/(2k-1). The selected swaps change disjoint pairs of hyperedges and are sensitive minimal changes of the hypermatching. Thus s_perm<=(2k-1)*s_hyper.

The final DFLLV26 journal supplies the permutation inputs: degree<=2s^2, bs<=6degree^2, C<=3s*bs and D<=2C^2. These give D_perm<=10368*s_perm^10, proving the displayed lift bound. The numerical coefficient is conservative and depends on k. No priority or best-known claim is made; this is a repository derivation, not a quoted hypermatching theorem or a claim of independent review.

This fills all eleven reverse-sensitivity directions for the uniform subprofile through A<=O(D). It does not establish an alpha-witnessing theorem, and does not cover every lambda-partite profile. The seven profile grids now have 913 parameterized upper chains across 924 cells; the eleven unindexed cells remain in the general lambda-partite hypermatching profile. Existing M>0 and parameter-growth guards remain unchanged. For k=2 the source's direct perfect-matching bounds can be stronger than this lift.

## Conjectures and source status

The official arXiv version history was rechecked and still lists HKMP26 v3, revised 30 September 2026, as the current version. This does not constitute a correction of its normalization argument. Conjecture 72 still needs the fixed-target, fixed-support versus enlarged-basis, exact-promise versus label-approximation, and uniform polynomial quantifiers distinguished. The LP diagnostic supplies a sufficient norm-control condition; it is not claimed to resolve the intended characterization.

Nis91 and AB25 journal proof comparisons remain uninspected. Extended exponent optimality, the general dependent-support lemma and general lambda-partite sensitivity comparisons remain unfinished. No HTML generated.
