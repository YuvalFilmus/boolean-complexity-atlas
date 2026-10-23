# Quadratic sensitivity bounds for hypermatchings

Derived research note, 23 October 2026. A fresh source-level audit checked the imported permutation argument and repaired an orientation error in its cube construction. The complete corrected argument is given below. This is assistant mathematical review, not formal verification or human peer review. Prior publication of the general result was not located in the sources searched; novelty is not certified.

Averaging a polynomial over all permutation representations of a hypermatching reduces its degree by at least a factor of two. This supplies a quadratic intrinsic-degree bound, strengthening the coarse deterministic-query comparison previously recorded in the atlas.

## The domain and the result

Fix positive integers $\lambda_1,\ldots,\lambda_r$ with $k=\sum_i\lambda_i\geq2$, and an integer $n\geq2$. Let $P_i$ be disjoint vertex classes of size $\lambda_i n$. Write $\mathcal H$ for **all** partitions of their union into $n$ edges, each containing $\lambda_i$ vertices of color $i$. The uncolored $k$-uniform perfect-hypermatching domain is the case $r=1$, $\lambda_1=k$.

For each potential edge $e$, let $X_e(H)=1[e\in H]$. Define $\deg_{\mathcal H}(f)$ to be the minimum degree of a real polynomial in the coordinates $X_e$ representing $f$ on $\mathcal H$.

For Boolean $f$, define $s_{\mathcal H}(f,H)$ as the maximum number of inputs $H_j$ with $f(H_j)\neq f(H)$ such that each set $H\setminus H_j$ has size two and these sets are pairwise disjoint. Let $s_{\mathcal H}(f)$ be the maximum over $H$. This is the packing sensitivity of the source domain framework; it does not count all sensitive neighboring inputs.

**Proposition.** For every Boolean function on this full domain,

$$\deg_{\mathcal H}(f)\leq(2k-1)^2s_{\mathcal H}(f)^2.$$

The coefficient is uniform in $n$ and in the individual color multiplicities for fixed $k$. Its optimality is not asserted. The result does not apply automatically to restricted promises or a different sensitivity convention.

The main algebraic input is stronger. Let $Z=\prod_i S_{\lambda_i n}$, with spatial degree in tagged permutation-entry coordinates. Divide the positions in component $i$ into $n$ groups of size $\lambda_i$, with common group labels across components. Let $\pi:Z\to\mathcal H$ forget the group labels and within-group orders. For every real function $f$,

$$2\deg_{\mathcal H}(f)\leq\deg_Z(f\circ\pi)\leq k\deg_{\mathcal H}(f).$$

The same comparison holds for $\varepsilon$-approximate degree, with the same error on both native domains. There is no claim of boundedness on an ambient Boolean cube outside those domains.

## Averaging over representations

Every $H$ has exactly $n!\prod_i(\lambda_i!)^n$ representations in $Z$. A uniform representation is obtained by assigning its edges bijectively to the $n$ group labels, then independently ordering the vertices of each color inside each group. Write $\mathcal A P(H)$ for the average of $P$ over this fiber.

**Lemma.** If $P$ has permutation-entry degree at most $d$, then $\mathcal A P$ has a hyperedge-coordinate representation of degree at most $\lfloor d/2\rfloor$.

**Proof.** By linearity, consider an entry monomial $M$. Delete repeated entries by idempotence. If its remaining entries prescribe two images at one position, or prescribe one color's vertex at two different positions, then $M$ vanishes identically. Its average is zero. The empty monomial averages to one.

Suppose $M$ is nonempty and compatible, with $t$ distinct entries. Let $B$ be its touched group labels and $h=|B|$. Let $V_{b,i}$ be the prescribed color-$i$ vertices in group $b$, and put $V_b=\bigcup_iV_{b,i}$. Compatibility implies that the sets $V_b$ are nonempty and pairwise disjoint, and their total cardinality is $t$. In particular $h\leq n$ and $|V_{b,i}|\leq\lambda_i$.

Use the falling-factorial notation $(a)_u=a(a-1)\cdots(a-u+1)$, with $(a)_0=1$. Counting label assignments and internal orders gives

$$\mathcal A M(H)=\frac{N_M(H)}{(n)_h\prod_{b\in B,i}(\lambda_i)_{|V_{b,i}|}},$$

where $N_M(H)$ counts injective assignments $b\mapsto e_b\in H$ with $V_b\subseteq e_b$. The denominator is positive and independent of $H$. For any fixed admissible assignment, its label probability is $1/(n)_h$; each prescribed within-group injection has probability $1/(\lambda_i)_{|V_{b,i}|}$. The assignments are disjoint events, proving the formula.

For a nonempty vertex set $U$, define

$$J_U(H)=\sum_{e\supseteq U}X_e(H).$$

This is the indicator that all vertices of $U$ lie in one edge. If $|U|=1$, it equals one on every input. If no potential edge contains $U$, it equals zero.

Let $\Pi(B)$ be the set of partitions of $B$. Inclusion–exclusion for injective assignments gives

$$N_M(H)=\sum_{\rho\in\Pi(B)}\mu(\rho)\prod_{C\in\rho}J_{\bigcup_{b\in C}V_b}(H),\qquad
\mu(\rho)=\prod_{C\in\rho}(-1)^{|C|-1}(|C|-1)!.$$

To verify the identity, expand each product as assignments constant on the blocks of $\rho$. An admissible assignment with equality partition $\eta$ receives coefficient $\sum_{\rho\leq\eta}\mu(\rho)$, which is one for the discrete partition and zero otherwise. Thus precisely the injective assignments remain.

In each partition term, replace every singleton-vertex factor $J_U$ by one. Each remaining factor is linear in $X_e$ and involves at least two prescribed vertices. The block unions are pairwise disjoint and contain $t$ vertices altogether, so there are at most $\lfloor t/2\rfloor$ remaining factors. Their product has degree at most $\lfloor t/2\rfloor$. Repeated edge coordinates after expansion can be removed by idempotence; incompatible edge products vanish on the domain. Consequently $\mathcal A M$ has the asserted degree. Applying this argument to every monomial proves the lemma. ∎

Apply the lemma to a minimum-degree polynomial for $F=f\circ\pi$. Since $F$ is constant on each fiber, its average equals $f$, proving $2\deg_{\mathcal H}f\leq\deg_ZF$. Conversely, the pullback of $X_e$ is a sum over group labels and internal bijections of degree-$k$ entry monomials. On each representation exactly one term is one if $e$ is present, and all terms vanish otherwise. Substitution proves $\deg_ZF\leq k\deg_{\mathcal H}f$.

The approximate-degree assertion follows by averaging a pointwise approximant and by the same substitution. Averaging preserves its error by convexity.

## Sensitivity transfer

We first prove the imported product-permutation estimate in the precise filtration and sensitivity conventions needed here. The published permutation argument contains an orientation error, so reproducing its conclusion without checking the construction would be insufficient.

### Permutation characters and degree

For a partition $\mu\vdash N$, let $M^\mu$ be the real tabloid permutation module, with its tabloids as an orthonormal basis. A tabloid records an unordered set in each row. Let $A,B$ range over all tableaux of shape $\mu$, and write $\{A\},\{B\}$ for their row tabloids. Write $C_B$ for the column stabilizer of the tableau $B$, and define

$$e_B=\sum_{\sigma\in C_B}\operatorname{sgn}(\sigma)\{\sigma B\},\qquad
\chi_{A,B}(z)=\langle e_B,z\{A\}\rangle.$$

The irreducibility and completeness of real Specht modules are the representation-theoretic inputs: the polytabloids $e_B$ span an irreducible module of shape $\mu$, and all shapes give the irreducible modules of $S_N$. These inputs were checked in Sagan, second edition, Sections 2.3–2.4. Consequently the functions $\chi_{A,B}$ span the matrix-coefficient space of that irreducible: the orthogonal projections of the tabloid basis vectors onto the Specht module span it, as do the polytabloids. Matrix-coefficient spaces of distinct irreducibles are orthogonal and together span all functions on $S_N$.

Put $d_\mu=N-\mu_1$. Each row-map indicator in $\chi_{A,B}$ has degree at most $d_\mu$: specify the images of all entries outside the first row and sum over their within-row bijections. The first row is then forced by bijectivity. Thus $\deg\chi_{A,B}\leq d_\mu$.

We also need orthogonality to every lower-degree entry polynomial. Consider an entry monomial of degree $e<d_\mu$. It names at most $e$ output values, leaving more than $\mu_1$ unused values. Since $B$ has $\mu_1$ columns, two unused values lie in one column. Their **output-value** transposition $\tau$ fixes the monomial and satisfies $\chi_{A,B}(\tau z)=-\chi_{A,B}(z)$. Averaging over the bijection $z\mapsto\tau z$ proves that the monomial is orthogonal to $\chi_{A,B}$.

It follows that the spatial degree filtration is the orthogonal sum of these coefficient spaces with $d_\mu$ at most the filtration degree. This proves the instance of DFLLV26 Theorem 5.5 used here, rather than assuming it from a generic spanning claim. In particular the top degree can be detected by correlation with a character of exactly that depth.

### Corrected cube construction

The values of $\chi_{A,B}$ are in $\{-1,0,1\}$. Indeed, distinct column permutations of $B$ give distinct tabloids: a permutation preserving both each row and each column must fix every entry. At a given $z$, at most one tabloid in this alternating sum equals $z\{A\}$.

Pair entries inside the columns of $B$, leaving one unpaired entry in each odd column. The resulting $D$ disjoint output-value transpositions satisfy

$$D=\sum_{\text{columns }c}\left\lfloor\frac{|c|}{2}\right\rfloor
\geq\frac{N-\mu_1}{2}.$$

They commute and generate a group of size $2^D$, acting freely by left multiplication on permutations. Each generator reverses $\chi_{A,B}$, because it acts by minus one on $e_B$. Therefore every orbit is either entirely outside its support or is a parity cube in its support. At a permutation $z$, one such transposition changes exactly the two entries whose images are its paired output values. Disjoint output pairs have disjoint preimage positions, so the removed permutation entries are pairwise disjoint at that vertex.

**Source correction.** DFLLV26 Section 5.3, article pp.33–34, instead chooses input-position transpositions from columns of $A$. With the printed definition of $\chi_{A,B}$, that sign claim can fail. For shape $(2,1)$ and both tabloids having rows $\{1,2\}/\{3\}$,

$$\chi(z)=1[z(3)=3]-1[z(3)=1].$$

At $z=(2,1,3)$ this equals one. Swapping input positions 1 and 3 gives $(3,1,2)$ and value zero. Swapping output values 1 and 3 gives $(2,3,1)$ and value minus one. The latter is the corrected construction used throughout this proof. It preserves the constants and the disjoint local changes; the invalid printed orientation is not used as an imported lemma.

### Products and the cube theorem

For $Z=\prod_i S_{\lambda_i n}$, an entry monomial factors by component. Hence its degree-at-most-$d$ space is the sum of tensor products of component filtrations with total degree at most $d$. The orthogonal component decomposition just proved refines this into exact grades. If a Boolean function $F$ has degree $d>0$, its top-grade projection is nonzero. It therefore correlates with a product of component characters whose depths sum to $d$.

The component support cubes multiply. Their dimensions add, their signs multiply to parity, and their removed entries are disjoint within each factor and across tagged factors. Thus a support cube of dimension $D\geq d/2$ has nonzero correlation with the restriction of $F$ and its full parity character.

For completeness, the required cube implication follows directly from Huang's signed-matrix argument. For a Boolean function $g$ on a $D$-cube with nonzero full-parity coefficient, $g$ XOR parity has a level set of size more than $2^{D-1}$. An edge inside that level set is sensitive for $g$. Huang's signed adjacency matrices are defined recursively by

$$A_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
A_D=\begin{pmatrix}A_{D-1}&I\\I&-A_{D-1}\end{pmatrix}.$$

Induction gives $A_D^2=DI$ and trace zero, so its eigenvalues are $\pm\sqrt D$, each with multiplicity $2^{D-1}$. Its support is exactly the cube edges. A principal submatrix on more than half the vertices has largest eigenvalue at least $\sqrt D$ by interlacing. The largest absolute eigenvector entry bounds that eigenvalue by the maximum degree of the induced graph. Thus that graph, and hence the sensitivity of $g$, has maximum degree at least $\sqrt D$. All these steps are Huang's Lemmas 2.1–2.3 and Theorem 1.1; no additional degree–sensitivity conjecture is imported.

At the selected support cube, its sensitive neighbors map to disjoint component transpositions. Consequently

$$s_Z(F)\geq\sqrt D\geq\sqrt{d/2},\qquad\deg_Z(F)\leq2s_Z(F)^2.$$

The degree-zero case is immediate. This also proves the precise cube-witness implication needed from DFLLV26 Lemma 5.2. It does not rely on inferring top-degree correlation from an arbitrary nonorthogonal spanning family.

### Passing sensitivity to hypermatchings

Fix $z\in Z$ and a packing of $a$ sensitive component transpositions. A transposition within one common group fixes $\pi(z)$, so every sensitive one joins two different original hyperedges. Make a multigraph whose vertices are the original hyperedges and whose edges are these transpositions. Disjoint permutation changes use each position at most once, so its maximum degree is at most $k$.

Greedy matching selects at least $a/(2k-1)$ multigraph edges: selecting one removes at most $2k-1$ edges meeting its endpoints. Each selected transposition projects to a sensitive change removing exactly two original hyperedges, and the selected removal pairs are disjoint. Therefore

$$s_Z(F)\leq(2k-1)s_{\mathcal H}(f).$$

Combining the degree-descent lemma and these two sensitivity comparisons proves

$$\deg_{\mathcal H}(f)\leq\tfrac12\deg_Z(F)\leq s_Z(F)^2\leq(2k-1)^2s_{\mathcal H}(f)^2.$$ ∎

## Sources and status

Neta Dafni, Yuval Filmus, Noam Lifshitz, Nathan Lindzey and Marc Vinyals, *Complexity measures on the symmetric group and beyond*, Combinatorial Theory **6**(2), article 6 (2026), 60 pp., DOI [10.5070/C6.68665](https://doi.org/10.5070/C6.68665). Spatial degree: Section 2.2, article p.7. Permutation degree decomposition and pseudo-characters: Theorem 5.5 and Section 5.3. Cube-witness implication: Lemma 5.2. The opening of Section 5 states the limitation of the direct representation-theoretic method on hypergraphical perfect matchings.

Hao Huang, *Induced subgraphs of hypercubes and a proof of the Sensitivity Conjecture*, Annals of Mathematics **190**(3), 949–955 (2019), DOI [10.4007/annals.2019.190.3.6](https://doi.org/10.4007/annals.2019.190.3.6).

Bruce E. Sagan, *The Symmetric Group: Representations, Combinatorial Algorithms, and Symmetric Functions*, second edition, Graduate Texts in Mathematics **203**, Springer-Verlag, New York (2001), DOI [10.1007/978-1-4757-6804-6](https://doi.org/10.1007/978-1-4757-6804-6). Sections 2.3–2.4 provide the tabloid, polytabloid and Specht-module input.

The [full source audit](hypermatching-full-source-audit.md) checks the imported arguments, the orientation repair, degree descent and sensitivity transfer. The [literature check](hypermatching-priority-audit.md) records the original sources, searches and priority limits. Older atlas reviews of the product construction are superseded on the transposition orientation; their constants survive the explicit repair above.

The proof establishes a precise fixed-$k$ quadratic interpretation of the historical hypergraphical question. For $k=2$, stronger published bounds already exist; the displayed coefficient is not promoted as best known in those special cases. It does not determine the original authors' intended quantifiers, produce an intrinsic witnessing family, or establish a constant independent of $k$. Targeted literature searches have not certified novelty. The argument is supplied for the user's mathematical review; no general AA, D-versus-bs, or exact-search conjecture is claimed resolved.
