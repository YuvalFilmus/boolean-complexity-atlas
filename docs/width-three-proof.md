# Four queries for the 4-MAJ certificate partition

The eight subcubes below have codimension three and partition the four-dimensional Boolean cube. Finding the unique subcube containing an input requires four exact quantum queries. A three-query algorithm would force a particular quadratic Fourier Gram matrix, but that matrix cannot arise after two queries.

## The search problem

The input is $x\in\{0,1\}^4$. A valid output is the unique compatible partial assignment in the following table. Integer endpoints use the usual binary order; query mask $1$ denotes the rightmost input bit.

| Label | Integer endpoints | Certificate |
|---|---|---|
| 0 | 0, 8 | `*000` |
| 1 | 1, 5 | `0*01` |
| 2 | 2, 3 | `001*` |
| 3 | 4, 6 | `01*0` |
| 4 | 7, 15 | `*111` |
| 5 | 9, 11 | `10*1` |
| 6 | 10, 14 | `1*10` |
| 7 | 12, 13 | `110*` |

This is the published 4-MAJ monochromatic partition of Kothari–Racicot-Desloges–Santha, Proposition 13, pp.923–924. Labels 0–3 have 4-MAJ value zero, and labels 4–7 have value one. The same partition, after flipping the rightmost two input bits, occurs in Filmus–Hirsch–Kurz–Ihringer–Riazanov–Smal–Vinyals, current author manuscript Theorem 2.49. The construction and its classical four-query lower bound are already known. The [priority review](width-three-priority-audit.md) distinguishes those facts from the quantum lower bound proved here.

Let $D(S)$ denote deterministic complexity and $Q_E(S)$ exact quantum complexity with the standard bit oracle, a fixed worst-case query budget, and probability-one correctness on every full-cube input. Finite-dimensional workspaces, intermediate measurements and final finite POVMs are allowed. Inactive queries are allowed, equivalently through a known-zero index or a dummy answer register in state $|+\rangle$.

**Proposition.** For this certificate-output search problem,

$$D(S)=Q_E(S)=4.$$

Reading all four bits proves the upper bound. We rule out three queries. This is a fixed finite instance, not an asymptotic query separation or an answer to the general exact-search question.

## Final-state rigidity

Every amplitude after $T$ queries is a complex multilinear polynomial of degree at most $T$, by the oracle-update induction of Beals–Buhrman–Cleve–Mosca–de Wolf, Lemma 4.1. For completeness, one oracle call replaces amplitudes $a,b$ by $(1-x_i)a+x_i b$ and $x_i a+(1-x_i)b$. Input-independent linear maps preserve degree, and multilinear reduction cannot increase it. Purification, coherent measurement histories, inactive-query padding and final POVM dilation preserve this statement; their details are also given in the [two-query proof](exact-search-proof.md).

An amplitude $a$ labeled by certificate $c$ vanishes at every input outside that certificate, since invalid-output probability is a sum of nonnegative squared magnitudes. Thus on the full cube,

$$a(x)=\mathbf1_c(x)b(x_{[4]\setminus\operatorname{dom}(c)}).$$

Uniqueness of multilinear representation makes this a polynomial identity. If it is nonzero, its degree is $|c|+\deg b$, because the factors use disjoint variables. Since every output here has width three, a three-query algorithm has constant $b$ for every final amplitude. Fewer than three queries are already impossible.

Consequently the entire purified final state is identical at the two endpoints of each edge, including its global phase. States for different edges are orthogonal, since their output labels differ. Let $C_{x,e}=\mathbf1[x\in e]$ be the $16$-by-$8$ incidence matrix. The final state Gram matrix, and the Gram matrix after undoing the last input-independent unitary, is exactly $CC^{\mathsf T}$.

## What the last query requires

Diagonalize the answer qubit of the XOR oracle. Its identity sector has label $q=0$; the other sectors have masks $q\in\{1,2,4,8\}$ and phases $z_q(x)=(-1)^{\operatorname{popcount}(q\mathbin\&x)}$. Put $z_0=1$.

Project the state just after the last oracle into these orthogonal sectors. Its edge-constant vectors give Hermitian positive semidefinite matrices $M_q$ satisfying

$$\sum_q M_q=I_8.$$

Before that query the amplitudes in sector $q$ are multiplied by $z_q$ and must have Fourier degree at most two. For a Fourier mask $A$, write $\chi_A(x)=(-1)^{\operatorname{popcount}(A\mathbin\&x)}$ and define

$$(L_q)_{A,e}=\sum_{x\in e}\chi_{A\triangle q}(x),\qquad |A|>2.$$

There are five rows: the four triple masks and the full mask. Necessarily $L_qM_q=0$. The omitted Fourier normalization does not affect this kernel condition. The pre-last-query Gram is

$$G(x,y)=\sum_q z_q(x)z_q(y)(CM_qC^{\mathsf T})_{x,y}.$$

These are necessary last-query conditions. They alone do not guarantee that a two-query algorithm can prepare this Gram.

## Symmetry and an exact rational certificate

The signed coordinate permutations preserving the eight edges form a group of order 48. They act on edge labels and permute the four nonzero query masks. A fixed input flip contributes an input-independent sign in a query sector; that sign cancels in its Gram. Averaging a hypothetical algorithm over these symmetries preserves query count, exactness, positivity, normalization and all prefix-state requirements. The average can be implemented as a coherent direct sum with an input-independent group register. Averaging also with the conjugate algorithm makes all Gram data real. Thus it suffices to consider invariant real symmetric $M_q$.

Here is a complete finite certificate for their affine-linear constraints. A triple $(q,a,b)$ indexes a symmetric matrix entry; all entries in its symmetry orbit agree. There are 10 orbits among the $5\cdot36=180$ entries. For each representative below the entry equals $b_0+t v+u w$.

| Orbit representative | $b_0$ | $v$ | $w$ |
|---|---|---|---|
| (0,0,1) | 0 | 0 | -4 |
| (0,0,0) | 1/2 | 0 | -4 |
| (0,0,4) | 1/2 | 0 | -4 |
| (1,0,0) | 1/6 | 0 | 1 |
| (1,0,1) | 0 | -1 | 2 |
| (1,0,2) | 0 | 0 | 1 |
| (1,0,3) | 0 | 1 | 0 |
| (1,0,4) | -1/6 | 0 | 1 |
| (1,2,2) | 0 | 0 | 1 |
| (1,2,7) | 0 | 0 | 1 |

The constraints $L_qM_q=0$ and $\sum_qM_q=I$ have rank eight on these ten variables. The displayed particular solution and two homogeneous directions therefore give every invariant supported normalized tuple, before any positivity restriction. The [independent rational verifier](checks/width_three_independent_check.py) constructs the group and orbits, generates these equations directly, and proves the rank and table by exact elimination. A [second verifier](checks/width_three_check.py) instead averages bases of the five support spaces and reconstructs the same two-dimensional affine family. No floating-point feasibility decision is used.

Define the quadratic Fourier block of $G$ by

$$H_{A,B}=\mathbb E_{x,y}[\chi_A(x)G(x,y)\chi_B(y)],\qquad |A|=|B|=2,$$

where $x,y$ are independent uniform inputs. In mask order $(3,5,6,9,10,12)$ the table gives

$$H=\sigma B_0,\qquad\sigma=1-2t+2u,\qquad B_0=\frac1{16}\begin{pmatrix}2&1&1&1&-1&0\\1&2&1&-1&0&1\\1&1&2&0&1&-1\\1&-1&0&2&-1&-1\\-1&0&1&-1&2&-1\\0&1&-1&-1&-1&2\end{pmatrix}.$$

The orbit verifier evaluates the Fourier transform exactly on the displayed particular solution and two directions, obtaining scale factors $1,-2,2$. The basis-averaging verifier independently obtains the same scalar-multiple image in its own affine coordinates. Linearity proves the identity for the whole affine space. This is the computationally assisted step of the proof, with the explicit certificate and two independently implemented checks supplied for reproduction.

For an actual prefix state, $H$ is the Gram of its quadratic coefficient vectors and is positive semidefinite, so $\sigma\geq0$. If $\sigma=0$, all those coefficient vectors vanish. The pre-last-query amplitudes then have degree at most one; one further query can only raise degree to two, contradicting the nonzero degree-three amplitudes required at an output. Therefore $\sigma>0$ for a hypothetical solver. This argument applies to the physically averaged algorithm, not to arbitrary feasible matrices in the relaxation.

## The two-query prefix is impossible

Immediately before a second query, amplitudes have degree at most one. In nontrivial query sector $i$, multiplying by $z_i$ can create a quadratic monomial only on a pair containing $i$; the identity sector creates none. The subsequent input-independent unitary preserves the coefficient Gram. Every two-query state therefore has

$$H=\sum_{i=1}^4 H_i,$$

where $H_i$ is positive semidefinite and supported on the three pairs containing coordinate $i$. These supports are the four stars of $K_4$. Two distinct intersecting pairs have a unique common coordinate, so their off-diagonal entry is forced into that one star.

In $B_0$, each star has three off-diagonal magnitudes $1/16$ with negative sign product. Conjugating that star by diagonal signs makes all three entries $-\sigma/16$. Positivity on the all-ones vector gives

$$\operatorname{tr}H_i\geq\frac{6\sigma}{16}.$$

Summing the four stars yields $\operatorname{tr}H\geq3\sigma/2$, while the six diagonal entries of $\sigma B_0$ sum to $3\sigma/4$. This is impossible for $\sigma>0$. No three-query exact solver exists, and hence $4\leq Q_E(S)\leq D(S)\leq4$. ∎

## A feasible weaker relaxation

The last-query degree conditions really are weaker. Pair antipodal edge labels as $(0,4),(3,5),(1,6),(2,7)$. Let $P_+$ project onto their symmetric subspace, and let $P_-^{e}$ be the antisymmetric rank-one projector for pair $e$. The four pairs have distinct coordinate orientations $i(e)$. Then

$$M_0=P_+,\qquad M_i=\frac13\sum_{e:\,i(e)\ne i}P_-^{e}$$

are positive semidefinite, sum to $I$, satisfy the support equations, and give quadratic block $B_0$. The second verifier checks these identities as well. The preceding trace argument prevents a two-query prefix for these matrices and, by symmetry, for every alternative hypothetical solver. A degree or sum-of-squares relaxation must not be mistaken for quantum realizability.

## Sources and status

Robin Kothari, David Racicot-Desloges and Miklos Santha, *Separating Decision Tree Complexity from Subcube Partition Complexity*, APPROX/RANDOM 2015, LIPIcs **40**, 915–930, DOI [10.4230/LIPIcs.APPROX-RANDOM.2015.915](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2015.915), Proposition 13, pp.923–924, for this exact partition and classical complexity.

Robert Beals, Harry Buhrman, Richard Cleve, Michele Mosca and Ronald de Wolf, *Quantum lower bounds by polynomials*, Journal of the ACM **48**(4), 778–797 (2001), DOI [10.1145/502090.502097](https://doi.org/10.1145/502090.502097), inspected manuscript Lemma 4.1, for amplitude degree. The support factorization is proved above.

The [fresh independent audit](width-three-full-source-audit.md) checks the quantum model and exact certificate. The [literature review](width-three-priority-audit.md) records known predecessors and search limits. This is an assistant-reviewed computational proof, not formal verification or human peer review. Prior publication of this precise quantum lower bound has not been certified absent; no novelty or asymptotic separation is asserted.
