# Exact two-query certificate search

An exact quantum algorithm that returns a compatible partial input assignment gains no queries over a deterministic algorithm when it uses at most two queries. The mechanism is a rigidity statement for nonnegative weighted covers by subcubes of codimension at most two.

## Model and statement

Let $N\geq0$ and let $S\subseteq\{0,1,*\}^N$ be a finite family of partial assignments. An input $x\in\{0,1\}^N$ accepts an output $c\in S$ precisely when $c\subseteq x$, meaning that $x$ agrees with every specified coordinate of $c$. Assume every input accepts at least one output. Write $|c|$ for the number of specified coordinates and $\mathbf1_c$ for the indicator of its subcube.

Let $D(S)$ be deterministic worst-case bit-query complexity. Let $Q_E(S)$ be exact quantum complexity with a fixed worst-case query budget and the standard oracle $|i,b,z\rangle\mapsto|i,b\mathbin\oplus x_i,z\rangle$. Input-independent computation is free; a query may be inactive, equivalently using an additional index with known bit zero. Correctness has probability one on every input of the full cube. Finite-dimensional algorithms, intermediate measurements and final finite POVMs are allowed.

**Proposition.** In this model,

$$Q_E(S)\leq2\quad\Longrightarrow\quad D(S)\leq2.$$

Moreover, $D(S)=Q_E(S)$ whenever $Q_E(S)\leq2$.

The statement concerns certificate-output search. It gives no such conclusion for arbitrary output relations, promise inputs, or expected-time zero-error algorithms. It does not resolve the asymptotic exact-quantum-versus-randomized question of Ben-David and Kundu.

## Amplitudes supported on a certificate

After $T$ bit queries, every final basis amplitude is a complex multilinear polynomial of degree at most $T$. Initially the amplitudes are constant. An input-independent linear operation takes linear combinations. A query replaces two amplitudes $a,b$ by $(1-x_i)a+x_ib$ and $x_ia+(1-x_i)b$, increasing degree by at most one. Reduction by $x_i^2=x_i$ does not increase degree. This is the induction in Beals–Buhrman–Cleve–Mosca–de Wolf, Lemma 4.1.

A mixed initial state can be purified. Intermediate measurements can be recorded coherently, with later operations controlled by their history; terminated branches use inactive queries to reach the fixed budget. A final POVM can be dilated by an input-independent isometry. These operations preserve the amplitude degree bound. Thus we may use a final orthonormal basis whose outcomes have fixed output labels in $S$.

Take an amplitude $a$ labeled by $c$, and put $K=\operatorname{dom}(c)$. Exactness implies $a(x)=0$ whenever $x$ does not extend $c$: invalid-output probability is a sum of nonnegative squared absolute amplitudes. Define $b(y)=a(c,y)$ on the coordinates outside $K$. On the full cube, uniqueness of multilinear representation gives

$$a(x)=\mathbf1_c(x)b(x_{[N]\setminus K}).$$

If $a\ne0$, then $\deg a=|K|+\deg b$. Indeed, multiplying a highest-degree monomial of $b$ by the top monomial of $\mathbf1_c$ produces a nonzero coefficient, and no lower-degree term can cancel it. Consequently every output used with positive probability has width at most $T$. If $|c|=T$, every amplitude labeled by $c$ is a constant multiple of $\mathbf1_c$, so

$$p_c(x)=w_c\mathbf1_c(x),\qquad w_c\geq0,$$

where $w_c$ is constant. In particular, this holds for width-two outputs of an exact two-query algorithm. It need not hold for its singleton outputs. We use this only as a necessary property of an actual quantum algorithm; a polynomial or sum-of-squares identity alone does not construct one.

## A weighted width-two cover

**Lemma.** Suppose nonnegative constants satisfy

$$\sum_{|c|\leq2}w_c\mathbf1_c(y)=1$$

on a full Boolean cube. If a positive-weight empty assignment occurs, the positive support has a zero-query solver. Otherwise that support has a deterministic solver of depth at most two.

**Proof.** Coalesce repeated assignments by adding their weights. For each unordered pair $\{i,j\}$, put its four weights in a nonnegative table $W=(w_{ab})_{a,b\in\{0,1\}}$, with absent entries zero. The coefficient of $y_iy_j$ in the normalization identity is

$$w_{00}-w_{01}-w_{10}+w_{11}=0.$$

No singleton or different pair contributes to this coefficient. The two rows therefore differ by a constant. Set $u_a=\min_b w_{ab}$ and $v_b=w_{ab}-u_a$; the latter is independent of $a$. Then $u_a,v_b\geq0$ and $w_{ab}=u_a+v_b$. A positive $u_a$ guarantees both original certificates $(i=a,j=0)$ and $(i=a,j=1)$ have positive weight. A positive $v_b$ guarantees the analogous complete column.

Replace each pair table by its row and column contributions, retaining their provenance. Together with the original singleton weights this gives

$$\sum_i\bigl[\alpha_{i0}(1-y_i)+\alpha_{i1}y_i\bigr]=1,\qquad \alpha_{ib}\geq0.$$

Comparing linear and constant coefficients gives $\alpha_{i0}=\alpha_{i1}$ and $\sum_i\alpha_{i0}=1$. Choose $i$ with both coefficients positive and query $y_i$. For each answer choose one positive contribution. An original singleton supplies a valid output immediately. A row or column contribution supplies a partner coordinate; query it and output the corresponding positive-weight original pair. Each branch uses at most two queries. ∎

The lemma allows overlaps and arbitrary nonnegative real weights. Earlier irreducible-subcube-partition results concern disjoint unweighted partitions; the [priority check](exact-search-priority-audit.md) separates those predecessors from the present application.

## Handling singleton outputs

**Proof of the proposition.** If $S$ contains the empty assignment, $D(S)=0$. If it contains both singleton assignments on some coordinate, querying that coordinate gives $D(S)\leq1$. Otherwise each coordinate has at most one allowed singleton. Fix every such coordinate opposite its allowed singleton, obtaining a nonempty subcube $H$. Call these coordinates fixed and the other coordinates free.

Every singleton output is invalid throughout $H$, so its probability there is zero. Outputs wider than two are unused everywhere. The width-two constants therefore satisfy

$$\sum_{|c|=2}w_c\mathbf1_c(x)=1\qquad(x\in H).$$

Discard terms incompatible with $H$. Viewed on its free coordinates, the remaining terms have residual widths zero, one or two, with the same nonnegative constant weights and their original output labels retained.

If a positive term has residual width zero, its original certificate fixes two distinct fixed coordinates. Query those coordinates. A mismatch with $H$ verifies the allowed singleton on that coordinate. If both agree with $H$, the original pair is valid. This solves the problem on the full cube in at most two queries.

Otherwise use the lemma's decomposition on the free cube and choose a free root coordinate $i$ with positive contributions for both answers. Query $i$. For each answer $b$, choose a positive contribution and proceed as follows.

- A residual singleton comes from an original pair fixing $i=b$ and one fixed coordinate $j$. Query $j$. Agreement with $H$ verifies that original pair; disagreement verifies the allowed singleton at $j$.
- A row or column of a residual pair uses two free coordinates. Query its partner $j$ and output the positive-weight original pair matching the observed answer. Both possible partner answers have such a certificate.

These outputs are valid even outside $H$; the restriction only selected the tree. If there are no free coordinates, normalization forces the residual-width-zero case. If there is one free coordinate, the same argument uses residual singletons. Thus $D(S)\leq2$.

For completeness, if $Q_E(S)=0$, a nonzero constant amplitude must have an empty output label, so $D(S)=0$. If $Q_E(S)\leq1$, all used outputs have width at most one. In the absence of an empty output, a collection of singleton assignments covers the cube only if both assignments of some coordinate occur: otherwise choosing the opposite value at every mentioned coordinate avoids all of them. Hence $D(S)\leq1$. Together with the classical simulation $Q_E(S)\leq D(S)$, this proves equality throughout the stated range. ∎

## An obstruction with three queries

On three input bits, allow the five certificates

$$S=\{00*,\ 01*,\ 10*,\ 1*0,\ *11\}.$$

They cover the cube. No two-query tree solves this search problem. There are no singleton outputs, so after querying a root coordinate, each branch must contain a complete row of pair certificates sharing that root literal. Root 1 fails at answer 1, root 2 fails at answer 1, and root 3 fails at answer 0. Querying all three bits works, so $D(S)=3$.

There is also a direct quantum obstruction. At input $010$, normalization of a hypothetical two-query solver forces $w_{01*}=1$. At $011$ it then forces $w_{*11}=0$, whereas $111$ forces $w_{*11}=1$. Thus $Q_E(S)\geq3$, and classical simulation gives equality. Width-two certificates alone do not imply a two-query algorithm.

## Sources and verification

Robert Beals, Harry Buhrman, Richard Cleve, Michele Mosca and Ronald de Wolf, *Quantum lower bounds by polynomials*, Journal of the ACM **48**(4), 778–797 (2001), DOI [10.1145/502090.502097](https://doi.org/10.1145/502090.502097). Inspected manuscript [quant-ph/9802049v3](https://arxiv.org/abs/quant-ph/9802049v3), Section 3.2 and Lemmas 4.1–4.2, PDF pp.4–5. The amplitude argument above extends the outcome labeling and supplies the support factorization explicitly.

Shalev Ben-David and Srijita Kundu, *Separations in query complexity for total search problems*, [arXiv:2410.16245v1](https://arxiv.org/abs/2410.16245v1) (2024), Section 2.1, PDF pp.9–10, for certificate-output search; Section 1.3, Open Problem 1, PDF p.8, for the broader exact-quantum/randomized question.

The [independent source audit](exact-search-full-source-audit.md) checks the amplitude import, weighted-cover argument, singleton recovery and boundary cases. The [literature check](exact-search-priority-audit.md) records related partition and quantum results with their precise scope. This is an independently assistant-reviewed research note, not formal verification, human peer review or a certified novelty claim.
