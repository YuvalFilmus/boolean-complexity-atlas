# Fresh source-level audit of the full hypermatching argument

Audit date: 23 October 2026. This audit starts from the proof and the original imported arguments, rather than accepting the previous assistants' verdicts. It covers the exact and approximate degree comparison, product-permutation degree/sensitivity theorem, Huang's theorem and its reduction, and sensitivity transfer. Published novelty is a separate literature question and is not certified here.

The final independently audited bound is $\deg_{\mathcal H}(f)\leq(2k-1)s_{\mathcal H}(f)^2$. The initial audit below established the squared coefficient; the final section checks the stronger cube-first argument.

## Initial source-audit verdict

**PASS AFTER AN EXPLICIT REPAIR TO THE IMPORTED PERMUTATION CUBE CONSTRUCTION.**

For the stated full lambda-partite domain, Boolean f, k=sum lambda_i>=2, n>=2, the conclusion

$$
\deg_{\mathcal H}(f)\le (2k-1)^2s_{\mathcal H}(f)^2
$$

is mathematically supported. The proof should not be published with its present opaque statement that the imported cube construction was simply checked: DFLLV26 Section 5.3 has an orientation error under its displayed definition of the pseudo-character. Transpositions of **output values in columns of B** repair the construction. Transpositions of **input positions in columns of A**, as printed, need not preserve its support or flip its sign. The repaired argument is given below and suffices for every later use.

This is an independent assistant audit, not formal verification or human peer review. The arbitrary restricted-promise version, a constant independent of k, and published priority are not established.

## Inspected primary sources and exact locators

* Dafni, Filmus, Lifshitz, Lindzey and Vinyals, *Complexity measures on the symmetric group and beyond*, Combinatorial Theory 6(2), article 6 (2026), DOI 10.5070/C6.68665. Local PDF `work/sources/DFLLV26journal.pdf`, extracted text of the same version. Spatial degree: Section 2.2, article p.7/PDF p.8. Sensitivity convention: Section 2.2. Cube-inducing definition and Lemma 5.2: article p.30/PDF p.31. Witnessing statement and Theorem 5.3: article p.31/PDF p.32. Theorem 5.5 and pseudo-characters: Section 5.3, article pp.32–34/PDF pp.33–35. Source orientation error: article pp.33–34. Spatial degree decomposition proof: Appendix A.1, article p.54/PDF p.55. The opening of Section 5, article p.29/PDF p.30, states its direct technique's hypermatching limitation.
* Hao Huang, *Induced subgraphs of hypercubes and a proof of the Sensitivity Conjecture*, Annals of Mathematics 190(3), 949–955 (2019), DOI 10.4007/annals.2019.190.3.6. Inspected author manuscript arXiv:1907.00847v2, 29 August 2019, local `work/sources/Hua19.pdf` and `.txt`. Theorems 1.1 and 1.4: manuscript pp.1 and 3. Signed adjacency proof: Lemmas 2.1–2.3 and proof of Theorem 1.1, manuscript pp.3–5. Below the needed Boolean-function reduction is proved directly, avoiding any unchecked dependence on Gotsman–Linial Theorem 1.3.
* Bruce E. Sagan, *The Symmetric Group: Representations, Combinatorial Algorithms, and Symmetric Functions*, second edition, Graduate Texts in Mathematics 203, Springer, 2001, DOI 10.1007/978-1-4757-6804-6. Inspected complete book PDF from https://fardila.com/Clase/RepTh/sagan.pdf, saved as `work/sources/Sagan01-audit.pdf`; text is `Sagan01-audit.txt`. Definition 2.3.2 and Lemma 2.3.3: printed pp.61–62/PDF pp.75–76. Specht-module Definition 2.3.4 and cyclicity Proposition 2.3.5: p.62/PDF p.76. Sign Lemma 2.4.1: p.64/PDF p.78. Corollaries 2.4.2–2.4.3 and Submodule Theorem 2.4.4 with proof: pp.64–65/PDF pp.78–79. Classification Theorem 2.4.6: p.66/PDF p.80. These checks address the actual polytabloid import, not an arbitrary column-alternating function.
* Ellis, Friedgut and Pilpel, *Intersecting families of permutations*, Journal of the American Mathematical Society 24(3), 649–682 (2011), DOI 10.1090/S0894-0347-2011-00690-5. Inspected original paper's Theorem 7 and proof via https://arxiv.org/pdf/1011.3342, current author manuscript v2 (7 July 2017), manuscript pp.25–26/PDF pp.25–26 in zero-based web display. It identifies the span of k-coset indicators with first-row-at-least-n−k Fourier support. No use is made of that paper's distinct Boolean nonnegative/decomposition claims such as Theorem 8.

## Dependency 1: the correct pseudo-characters and their homogeneous filtration

Let M^lambda have orthonormal basis the row tabloids of shape lambda. For a tableau B, let C_B be its column stabilizer and let

$$
e_B=\sum_{\sigma\in C_B}\operatorname{sgn}(\sigma)\{\sigma B\}.
$$

Use the source's exact function

$$
\chi_{A,B}(z)=\sum_{\sigma\in C_B}\operatorname{sgn}(\sigma)
  1[z\{A\}=\{\sigma B\}]
=\langle e_B,z\{A\}\rangle.
$$

The distinct column permutations of B produce distinct row tabloids: two that give identical row sets have quotient in both the row and column stabilizers, whose intersection is trivial. Hence chi takes values in {-1,0,1}. It is nonzero, since a permutation mapping A to B contributes the unique identity summand.

### Why the span really is the pure lambda isotypic component

The polytabloids e_B span the Specht submodule S^lambda of M^lambda. The inspected Sagan submodule theorem proves irreducibility in characteristic zero: column antisymmetrization of any vector is a scalar multiple of e_B, and any invariant subspace either contains the polytabloid span or is perpendicular to it. Applying this to a nonzero subspace of S^lambda, positive definiteness excludes the perpendicular alternative. Conjugacy of tableaux gives cyclic generation. Sagan's classification theorem gives pairwise inequivalent Specht modules exhausting the irreducibles.

Let P_lambda be the orthogonal projection of M^lambda onto this particular Specht submodule. Since e_B belongs to S^lambda and the action is orthogonal,

$$
\chi_{A,B}(z)=\langle e_B,zP_\lambda\{A\}\rangle.
$$

As A varies, the projected row-tabloid basis vectors span S^lambda; as B varies, the polytabloids span it. Thus these functions span every matrix coefficient of S^lambda. Orthogonality of matrix coefficients of inequivalent irreducible real orthogonal representations puts their span exactly in the lambda isotypic coefficient space in R[S_N]. There are no lower-shape components hidden in this construction. The argument would fail for a general column-alternating function; the actual polytabloid realization matters.

### Independent direct check of purity in the spatial degree filtration

Put d=N−lambda_1. Every row-map indicator e_{A,B} has spatial degree at most d: sum over bijections mapping the d entries outside the first row to their prescribed target rows. Each summand is an entry monomial of degree d; the remaining row follows automatically because z is a bijection. Thus deg chi<=d.

Conversely, let m be a compatible entry monomial of degree e<d. Its prescribed output set J has size e. Since N−e>lambda_1 and there are lambda_1 columns in B, some column contains two output values outside J. Let tau swap these two values. The monomial obeys m(tau z)=m(z), while the correct covariance below gives chi(tau z)=−chi(z). Uniform averaging therefore gives <m,chi>=0. Incompatible monomials vanish, so chi is perpendicular to the entire degree-at-most-(d−1) space.

This proves that every nonzero chi of shape lambda is homogeneous of filtration degree d without assuming the isotypic assertion. Together with the Specht completeness above it also proves the spatial degree decomposition needed in Theorem 5.5. It independently checks the central part of the original Appendix A.1, whose own sign cancellation has a typographical missing minus sign in its final displayed comparison.

## Dependency 2: the printed orientation error and its repair

Take N=3 and A=B with first row (1,2), second row (3). Then

$$
\chi(z)=1[z(3)=3]-1[z(3)=1].
$$

For z=(2,1,3), chi(z)=1. Swapping input positions 1 and 3 gives z'=(3,1,2), for which chi(z')=0. This contradicts the sign-flip assertion made for the source's stated A-column/input-position transposition. In contrast, swapping output values 1 and 3 gives z''=(2,3,1), for which chi(z'')=−1.

The repaired construction pairs entries within each column of **B**, using each output value at most once. A column of height h contributes floor(h/2)>= (h−1)/2 pairs. Since sum_columns(h−1)=N−lambda_1=d, the number D of pairs satisfies D>=d/2.

For tau in C_B, the sign lemma gives tau^{-1}e_B=sgn(tau)e_B; hence

$$
\chi(\tau z)=\langle \tau^{-1}e_B,z\{A\}\rangle
=\operatorname{sgn}(\tau)\chi(z).
$$

The selected transpositions commute. Their group has size 2^D, acts freely by left multiplication on S_N, preserves the support of chi, and flips its sign on every generator. Consequently its orbits partition the support into cubes with parity signs, up to an overall constant ±1 on each cube. The source Lemma 5.2's parity argument is unchanged by this constant sign.

At a fixed z, an output swap (u,v) changes precisely input positions z^{-1}(u),z^{-1}(v). The removed entry set is {(z^{-1}u,u),(z^{-1}v,v)} and has size two. Selected output pairs are disjoint, so their removed entry sets are disjoint. This holds at every vertex of every orbit, although the positions corresponding to a particular output value change from vertex to vertex. The cube definition requires disjointness at each vertex, not one globally fixed set of input positions. Thus the repaired cubes meet the exact native sensitivity convention.

## Dependency 3: products and the correlation step

For Z=product_i S_{N_i}, represent entries with their component tags. Degree-at-most-d functions form the sum of tensor products of component degree spaces with total degree at most d. This follows by factoring each entry monomial by component, and conversely multiplying component polynomial representations.

Take a nonzero degree-d homogeneous component of F. By the component decomposition just verified, it has a nonzero projection into some tensor of pure shape spaces with depths d_i summing to d. The products of chi_{A_i,B_i} span that tensor space, so at least one product Psi correlates nontrivially with F. Orthogonality to all other tensor shape spaces rules out cancellation from lower-degree or unrelated components. This explicitly supplies the often implicit correlation step in Theorem 5.3; nonzero F squared alone is not a sufficient justification absent the homogeneous decomposition.

Each factor's repaired support is partitioned into cubes of dimension D_i>=d_i/2. Their Cartesian products partition the support of Psi into cubes of dimension D=sum D_i>=d/2. Changes within a component are disjoint by the repaired construction; changes in distinct components are disjoint because entries are tagged. Psi takes values ±1 on its support and is parity up to a cube-dependent overall sign. Nonzero global correlation implies nonzero correlation on at least one cube.

Thus the needed product theorem is truly

$$
\deg_Z(F)\le 2s_Z(F)^2,
$$

rather than an unsupported tensorization of a numerical single-factor inequality.

## Dependency 4: Huang's theorem, with its needed reduction checked directly

On a D-cube where Boolean g has nonzero correlation with full parity, set b=1−2g and epsilon(x)=(-1)^{|x|}. For D>0, the nonzero full-parity coefficient says sum b epsilon!=0. Hence the agreement set {b=epsilon} has size different from half the cube; either it or its complement has more than half the vertices. Within either set, adjacent vertices have opposite b values because epsilon flips. Thus every induced edge in that set is a sensitive edge for g.

Huang constructs a symmetric signed adjacency matrix A_D with entries ±1 on cube edges, zero elsewhere, and A_D^2=D I. Its trace is zero, so its +sqrt(D) eigenspace has dimension 2^{D−1}. Every coordinate subspace supported on more than half the vertices intersects that positive eigenspace nontrivially, by the dimension formula. A vector in this intersection has Rayleigh quotient sqrt(D) for the corresponding principal submatrix. Therefore that principal submatrix has largest eigenvalue at least sqrt(D). Its spectral radius is at most its maximum absolute row sum, which equals the induced graph's maximum degree. Hence g has sensitivity at least sqrt(D).

This checks the exact signed-matrix proof in Huang's Lemma 2.2 and Theorem 1.1, including its eigenvalue multiplicities, and proves the full-parity Boolean case required here without leaving the Gotsman–Linial equivalence as an unchecked import. D=0 is vacuous. The native cubes above transfer these sensitive neighbors to disjoint size-two entry changes, giving s_Z>=sqrt(D)>=sqrt(d/2).

## Dependency 5: averaging over hypermatching representations

Every full hypermatching has n! product_i(lambda_i!)^n representations. A fiber-uniform representation assigns hyperedges uniformly to common group labels, then orders same-color vertices independently within each group.

For an entry monomial, erase duplicates; incompatible prescriptions give zero. For a nonempty compatible degree-t monomial, group its prescribed vertices by the h touched common group labels, giving nonempty disjoint sets V_b with total size t. Its fiber expectation equals

$$
\frac{N(H)}{(n)_h\prod_{b,i}(\lambda_i)_{|V_{b,i}|}},
$$

where N counts distinct hyperedges assigned to these labels subject to V_b being contained in its assigned edge. Every denominator is positive, since h<=n and |V_{b,i}|<=lambda_i. There is no hidden dependence on the hypermatching.

For any nonempty U, J_U=sum_{e superset U}X_e is precisely the indicator that U is in one edge. This uses the full partition domain; for |U|=1 it is identically one. A union too large or with forbidden color multiplicities has J_U=0.

The partition-lattice formula

$$
N(H)=\sum_{\rho}\prod_{C\in\rho}(-1)^{|C|-1}(|C|-1)!\,J_{\cup_{b\in C}V_b}(H)
$$

is correct: after expanding, an assignment with equality partition eta has coefficient sum_{rho<=eta}mu(discrete,rho), which is one exactly when eta is discrete and zero otherwise. This is inclusion–exclusion for injective assignments, not an assumption that the noninjective assignments are impossible.

In each term every singleton-vertex J factor is one. Remaining block unions are disjoint and each consumes at least two of the t prescribed vertices, so at most floor(t/2) nonconstant factors remain. Each is degree one in hyperedge coordinates. Therefore the averaged monomial has degree at most floor(t/2), and linearity proves the general averaging lemma. The empty monomial is constant and meets the same bound. Repeated edge coordinates can be made multilinear by idempotence; incompatible products vanish, and neither operation increases degree.

For a fiber-constant F=f composed with pi, averaging a minimum-degree representative of F gives f exactly. Thus deg_H f<=floor(deg_Z F/2). The pullback of a native edge indicator is the sum over its common group labels and compatible color bijections of degree-k entry monomials, with exactly one active term when that edge is present. Substitution gives the reverse comparison deg_Z F<=k deg_H f. The same operations preserve uniform approximation error on the stated domains by convexity, proving the approximate-degree counterpart, including the floor refinement. No ambient-cube boundedness follows or is needed.

## Dependency 6: local sensitivity transfer and the final constant

Fix a representation z and a packing of a sensitive size-two permutation-entry changes. A minimum nontrivial change of a permutation is a transposition within one component. Distinct packed changes use disjoint input positions in that component: if a position occurred twice, its original tagged entry would occur in both removed-entry sets. This remains true for the output-transposition cubes above.

A transposition within one common position group fixes the projected hypermatching and cannot be sensitive. Every sensitive transposition therefore swaps two distinct same-color vertices in two distinct original hyperedges. It changes exactly those two hyperedges: each of the new edges contains at least one vertex of the other original edge, so neither new edge equals an original one. Because k>=2 there is a vertex left from each original edge; the two new edges are distinct and cannot equal any other edge of the original perfect partition. Color multiplicities are preserved.

Make the multigraph on original hyperedges with one edge for each packed transposition. A hyperedge has k occupied positions in all components together, and disjointness uses each at most once, so maximum multigraph degree is at most k. There are no loops. Greedily selecting an edge deletes at most deg(u)+deg(v)−1<=2k−1 edges including itself; parallel edges only reduce this count. Thus there is a matching of size at least a/(2k−1). Each selected change projects to a sensitive removal pair of size two, and matching edges give disjoint removal pairs. Hence s_Z(F)<= (2k−1)s_H(f).

Combining the audited steps gives

$$
\deg_H f\le\tfrac12\deg_ZF\le s_Z(F)^2\le(2k-1)^2s_H(f)^2.
$$

The constant depends only on k and is uniform in n and the individual positive color multiplicities. Constant functions and trivial degree-zero tensor factors cause no exception.

## Exact finite checks performed for this audit

`python3 work/check_hypermatching_imports.py` passed. It independently enumerates the source functions for every partition shape of N=2,3,4,5 (canonical tableaux), checks 3,434 output-transposition covariance instances, and checks exact integer orthogonality against 1,467 compatible lower-degree monomials. It also reproduces the orientation counterexample, with function values (1,0,−1) at original/input-swapped/output-swapped permutations. These checks support the audit and expose the source orientation issue; they do not replace the proofs above or certify all n.

## Required publication changes

1. Replace the opaque imported cube step with the explicit output/B-column construction.
2. State the printed A/input orientation issue and give the three-point counterexample, without claiming the published corollary itself is false.
3. Include the direct homogeneous-filtration argument or the full matrix-coefficient explanation; avoid the bare assertion that degree-d spanning vectors necessarily correlate with a degree-d function.
4. Retain exact domain, degree and packing-sensitivity definitions, fixed-k quantifiers and novelty limitations.
5. Mark earlier assistant audit verdicts as superseded by this source-level repair wherever the earlier reports simply accepted the printed cube step.


## Independent refinement audit: choosing a native face before applying Huang

23 October 2026. This is a new sharpening beyond the already audited square coefficient. It does not certify published novelty.

### Refinement verdict

**PASS.** The repaired output-transposition pseudo-character construction supports

$$
\boxed{\deg_{\mathcal H}(f)\le (2k-1)s_{\mathcal H}(f)^2.}
$$

The domain, degree and sensitivity conventions and fixed-k quantifiers are exactly those of the complete proof: all lambda-partite perfect hypermatchings, n>=2, positive multiplicities summing to k>=2, hyperedge-coordinate degree, packing of size-two sensitive edge removals. The factor of two from representation averaging is retained and used. No assumption is made that all cube axes are sensitive at their base point.

The improvement comes from choosing a large matching of **cube axes** first and then applying Huang to a face whose projection is a native hypermatching cube. The previous square-coefficient argument instead applied Huang before extracting a matching of sensitive axes.

### Audited refinement construction

Write h=deg_H f, F=f composed with pi, and d=deg_Z F. The audited averaging lemma gives d>=2h. For d>0, the repaired homogeneous tensor pseudo-character argument gives a cube of dimension D>=d/2, parameterized by disjoint output-value transpositions, on which g=F restricted to that cube has nonzero full-parity coefficient. Thus D>=h. Constant functions are immediate.

At a fixed initial permutation representation z, draw each of its D output transpositions as an edge between the common position-group labels containing the two swapped output values. Different axes use disjoint output values in their respective tagged components. At z these correspond to disjoint tagged positions, so each common group has at most k incident stubs.

### Required extra observation: there are no loops

A cube axis need not be sensitive at z, so absence of loops must not be justified by base-point sensitivity. Instead, suppose its two output values occupy positions in the same common group. Every other cube generator swaps different output values and hence leaves both these values at their existing positions. Flipping the selected axis consequently only changes the within-group ordering, at every point of the whole cube. It fixes pi and therefore F on the whole cube. This makes g independent of that axis, contradicting the nonzero full-parity coefficient. Thus the multigraph is loopless and has maximum degree at most k.

Greedy matching supplies a set I of m axes with

$$
m\ge \frac{D}{2k-1}.
$$

Parallel edges are harmless: selecting an edge deletes no more than deg(u)+deg(v)−1<=2k−1 edges. The chosen group pairs are disjoint.

### Fixing the other axes preserves a top coefficient somewhere

Let J be the remaining axes. For each y in {0,1}^J, write g_y for the restricted function on I and let

$$
a(y)=2^{-m}\sum_{x\in\{0,1\}^{I}}g(x,y)(-1)^{\sum_{i\in I}x_i}.
$$

Then

$$
\widehat g([D])=\mathbb E_y\left[a(y)(-1)^{\sum_{j\in J}y_j}\right]\ne0.
$$

Therefore some fixing y has a(y)!=0. The selected-axis face at this fixing retains a nonzero full-parity coefficient; it is not necessary to retain its numerical magnitude.

### The selected face remains a native cube after fixing

Each unselected generator swaps output values disjoint from the selected ones. Hence fixing the J axes does not move any selected output value from its original tagged position. The group pair associated with each selected axis remains the same after every such fixing. As the selected axes themselves vary, their values only alternate between their own two positions; no other selected axis touches either group in that pair.

Fix the J-axis state y. On the projected face, each selected axis consequently acts on its own disjoint pair of groups, swapping one same-color vertex between their two edges. Because k>=2, each edge retains at least one other vertex. The new pair of edges is different from the old pair, even after edge labels are forgotten: a retained vertex from either group prevents its new edge from equaling the other group's old edge, while the incoming distinct vertex prevents equality with its own old edge. No other hyperedge can equal either new edge because all these vertices belong to this pair's disjoint vertex union.

The 2k-vertex unions for different selected group pairs are disjoint at this fixed face. Each coordinate therefore has two different local partitions on its own union, independently of the other coordinates. This proves that the projected face has exactly 2^m distinct hypermatchings. Thus projection of this face is injective, including the uncolored case where the common group labels are not part of an input.

At every face vertex each axis changes exactly two hyperedges, and the removal pairs of different axes are disjoint. The projected face is consequently a cube embedding of precisely the type required by the native packing-sensitivity convention. This argument concerns disjointness locally at every vertex; it does not assume that the two edge sets themselves remain unchanged as the associated coordinate flips.

### Apply Huang on this face

The selected fixing has nonzero full-parity coefficient, so Huang gives s(g_y)>=sqrt(m). At a point attaining this sensitivity, each of those sensitive face neighbors projects to a different native hypermatching neighbor. Their two-edge removal sets are disjoint. Hence

$$
s_H(f)^2\ge m\ge\frac{D}{2k-1}\ge\frac{h}{2k-1}.
$$

Rearranging proves the displayed refinement. No unrestricted full-cube boundedness, promise extension, non-disjoint block sensitivity, or variable group labels are introduced.

### Refinement traps checked

* **Axes insensitive at the base point:** allowed. Only a globally dummy axis is excluded, via the full-parity coefficient.
* **Loops:** excluded by the separate argument above, not by assuming sensitivity.
* **Fixing changes the selected graph:** it does not, because unselected output supports are disjoint from selected supports. This is precisely where the repaired output-transposition construction matters.
* **Loss of top Fourier coefficient:** some fixing preserves nonzeroness by the explicit identity above, although most fixings may not.
* **Forgotten group labels collapse two states:** disjoint local vertex unions and the retained k−1 vertices exclude this for k>=2.
* **Sensitivity uses disjoint removed edges, not sensitive degree:** the selected matching supplies disjoint group pairs at every face vertex.
* **Dimension comparison:** D>=d/2>=h uses the audited degree-halving lemma. Using only d>=h would lose another factor two.
* **Maximum degree:** at most k, even with multiple colors, because a group contains exactly k tagged positions in all components together.

### Refinement structural checks

`python3 tests/hypermatching_cube_faces_check.py` passed. It enumerates all partial disjoint-output-swap families in eleven small lambda/n cases, including uncolored 2-uniform n=4 and colored (1,1), n=4, so multidimensional native faces are checked. Across 2,071 loopless axis families it checked 28,836 faces, including all fixings of their unselected axes, 66,096 native-neighbor instances, and 34,544 dummy-loop instances. Every selected matching face projected injectively, and every vertex had disjoint size-two removed-edge sets. The base representative is the identity, without loss for this structural check by relabeling the output vertices within each color.

These enumerations check the structural invariants; the general proof above, not finite enumeration, establishes the result.
