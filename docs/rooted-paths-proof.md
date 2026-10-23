# Influence bounds for rooted-path Fourier supports

A polynomial whose Fourier supports are short ancestor–descendant paths can have unbounded variable occurrence. Nevertheless, its Fourier mass and a native coordinate influence admit bounds independent of the size of the tree. A change to prefix characters makes the polynomial quadratic; an orientation of its endpoint graph controls its coefficients.

This is a support-restricted application of classical Rademacher-chaos methods. The analytic mechanism is already known. The [priority review](rooted-paths-priority-audit.md) separates the classical ingredients, the explicit rooted-path application, and stronger related statements. No novelty or general Aaronson–Ambainis resolution is asserted.

## Definitions and statement

Let $T$ be a finite tree rooted at $o$, with one independent uniform input sign $x_e\in\{-1,1\}$ per edge. Let

$$p(x)=a_0+\sum_{P\in\mathcal F}a_P\prod_{e\in P}x_e,$$

where the distinct nonempty supports $P$ are paths from an ancestor to a descendant, each of length at most the integer $d\geq1$. Assume $p$ is real and nonconstant. Write

$$A=\sum_P|a_P|,\quad V=\operatorname{Var}(p)=\sum_P a_P^2,\quad W=\max_xp(x)-\min_xp(x)>0,\quad I_e=\sum_{P\ni e}a_P^2.$$

Here $I_e=\mathbb E[((p(x)-p(x^{\oplus e}))/2)^2]$ is the derivative-normalized influence of an original edge variable. A convention using the full squared flip difference gives $4I_e$.

**Proposition.**

$$A\leq2\sqrt{3d}\,W,\qquad\max_e I_e\geq\frac{V^2}{12dW^2}.$$

If $p$ takes values in $[0,1]$, then for every $\varepsilon>0$ and $0<\delta<1$ there is a deterministic nonadaptive approximation using at most

$$d\left\lceil\frac{3d}{\delta\varepsilon^2}\right\rceil$$

original edge queries and having additive error at most $\varepsilon$ except on a uniform-input set of probability at most $\delta$. The procedure assumes the Fourier representation is available; it does not recover coefficients efficiently from query access.

These estimates allow arbitrary height, branching and occurrence count. For example, a root edge $a$ followed by child edges $b_1,\ldots,b_m$ gives paths $\{a,b_j\}$ of length two, although $a$ occurs in arbitrarily many supports.

## A quadratic graph estimate

Let $G$ be a finite simple graph with real weights $a_{uv}$ and an orientation of maximum outdegree at most $r\geq1$. Define

$$Q(z)=\sum_{uv\in E(G)}a_{uv}z_uz_v,\quad W_G=\max_zQ(z)-\min_zQ(z),\quad R=\sum_v\sqrt{\sum_{u:\,uv\in E(G)}a_{uv}^2}.$$

We first prove $R\leq2\sqrt3\,W_G$. For sign vectors $s,t$, put

$$B(s,t)=\frac12\sum_{uv}a_{uv}(s_ut_v+s_vt_u)=Q((s+t)/2)-Q((s-t)/2).$$

A multilinear polynomial at any point of $[-1,1]^{V(G)}$ is an average of its sign-cube values, obtained by independently rounding each coordinate with the prescribed mean. Hence $|B(s,t)|\leq W_G$. For fixed $t$, choose each $s_v$ to agree with the sign of its incident linear sum. This gives

$$B(s,t)=\frac12\sum_v\left|\sum_{u:\,uv\in E(G)}a_{uv}t_u\right|.$$

For independent uniform signs $\epsilon_j$ and $L=\sum_j b_j\epsilon_j$, write $\sigma^2=\sum_jb_j^2$. Direct expansion and Hölder give

$$\mathbb E L^4=3\sigma^4-2\sum_jb_j^4\leq3\sigma^4,\qquad\sigma^2\leq(\mathbb E|L|)^{2/3}(\mathbb E L^4)^{1/3}.$$

Thus $\mathbb E|L|\geq\sigma/\sqrt3$, including the zero case. Averaging the chosen bilinear form over uniform $t$ yields $W_G\geq R/(2\sqrt3)$.

Charge each edge coefficient to its tail. Cauchy–Schwarz on at most $r$ outgoing edges at each vertex gives

$$\sum_{uv}|a_{uv}|\leq\sqrt r\sum_v\sqrt{\sum_{v\to u}a_{uv}^2}\leq\sqrt r\,R\leq2\sqrt{3r}\,W_G.$$

This establishes the graph estimate using only explicit moment calculations and elementary inequalities.

## Prefix characters and original influences

For each nonroot vertex $v$, set $z_v=\prod_{e\in[o,v]}x_e$ and set $z_o=1$. The inverse relation $x_{\operatorname{parent}(v),v}=z_{\operatorname{parent}(v)}z_v$ proves that this is a bijection between original edge signs and nonroot vertex signs, preserving uniform measure and range. For an ancestor–descendant path $[u,v]$, cancellation gives

$$\prod_{e\in[u,v]}x_e=z_uz_v.$$

Make a graph whose edges are these endpoint pairs and orient each from descendant to ancestor. For any descendant and any length $1\leq\ell\leq d$, at most one ancestor lies at that distance. Thus its outdegree is at most $d$.

The root character is initially constant, whereas the quadratic graph estimate allows an independent sign at every vertex. This changes no range. Write the transformed polynomial minus $a_0$ as $q(z)=L(z)+R_2(z)$, with root-incident linear terms $L$ and the other quadratic terms $R_2$. Freeing the root gives

$$Q(1,z)=q(z),\qquad Q(-1,z)=-L(z)+R_2(z)=q(-z).$$

The two root slices have the same range, so $W_G=W$. The graph estimate with $r=d$ proves the stated bound on $A$.

Let $M=\max_P|a_P|$. Parseval gives $V\leq AM$, and a nonempty maximizing path contains an original edge whose influence is at least $M^2$. Therefore

$$\max_eI_e\geq(V/A)^2\geq V^2/(12dW^2).$$

This uses original Fourier coefficients, not an identification of transformed and original influences. Those influences can differ: $x_a(x_b+x_c)$ becomes $z_b+z_c$ when $a$ is a root edge and $b,c$ its children. The native influence of $a$ is two, while the transformed influence of $z_a$ is zero.

## Nonadaptive approximation

Assume $0\leq p\leq1$. Retain the $m$ largest nonconstant Fourier coefficients, query the union of their original path supports, and evaluate their sum plus $a_0$. Clip the estimate to $[0,1]$. This uses at most $dm$ queries. If there are at most $m$ terms it is exact; otherwise let $t$ be the largest omitted magnitude. Parseval gives squared mean error at most

$$\sum_{P\text{ omitted}}a_P^2\leq t(A-mt)\leq\frac{A^2}{4m}\leq\frac{3d}{m}.$$

The middle inequality maximizes a quadratic in $t$ and handles coefficient ties. Taking $m=\lceil3d/(\delta\varepsilon^2)\rceil$ and applying Markov to squared error gives the claimed failure bound. Clipping cannot increase the pointwise error. ∎

## A source-dependent constant improvement

Szarek's classical sharp lower Khintchine inequality replaces the moment estimate by

$$\mathbb E\left|\sum_jb_j\epsilon_j\right|\geq\frac1{\sqrt2}\left(\sum_jb_j^2\right)^{1/2}.$$

Its original Theorem 1 is printed on p.198 of *On the best constants in the Khinchin inequality*, Studia Mathematica **58**(2), 197–208 (1976), DOI [10.4064/sm-58-2-197-208](https://doi.org/10.4064/sm-58-2-197-208). The scanned original statement, real-coefficient hypothesis and constant were inspected. Applying that published theorem at exactly the averaging step above yields the following coefficient and influence bounds; the query bound additionally assumes $0\leq p\leq1$:

$$A\leq2\sqrt{2d}\,W,\qquad\max_eI_e\geq\frac{V^2}{8dW^2},\qquad\text{queries}\leq d\left\lceil\frac{2d}{\delta\varepsilon^2}\right\rceil.$$

The first proof is self-contained with constant 12; this strengthening imports the stated classical theorem. These constants are not asserted optimal for the rooted-path problem.

## Scope and boundary

For each fixed path length, the endpoint graph is a forest. On a cycle a deepest vertex would have two ancestors at that same distance, which is impossible. Its edge characters are independent over $\mathbb F_2$, even with the root fixed: a nonempty forest has a leaf, and a graph cannot have only the root of odd degree. Thus one length class captures at least $A/d$ Fourier mass in an independent family. The quadratic argument above gives a stronger estimate than the earlier independent-mass route within this class.

The spectral-mass estimate does not extend to arbitrary paths of bounded length. On a star with $2m$ leaf-edge inputs split as $x,y$, let $H$ be a real Hadamard matrix of order $m$ and put

$$p_m(x,y)=\frac{x^{\mathsf T}Hy}{m^{3/2}}.$$

Every support is a length-two path between incomparable leaves. Yet $|p_m|\leq1$, $A=\sqrt m$, $V=1/m$ and each native influence is $1/m^2$. Therefore $A/W\geq\sqrt m/2$ diverges. Equal-magnitude coefficients also give independent-mass ratio $(2m-1)/m^2$, by the binary rank of the connected graph $K_{m,m}$.

This classical example obstructs the spectral-mass extension, not the AA influence conjecture. Its variance decreases, and its influences equal $V^2$. More general influence results may use a different argument; no impossibility for those is claimed.

## Sources, checks and status

Scott Aaronson and Andris Ambainis, *The Need for Structure in Quantum Speedups*, Theory of Computing **10**(6), 133–166 (2014), DOI [10.4086/toc.2014.v010a006](https://doi.org/10.4086/toc.2014.v010a006), for the general influence and simulation questions. This page states the derivative normalization explicitly.

S. V. Astashkin, *Rademacher chaos in symmetric spaces*, East Journal on Approximations **4**(3), 311–336 (1998), [author manuscript](https://astashkin.ssau.ru/papers/21.pdf), Section 4, Theorem 5 and the following Walsh-matrix example, for classical related methods. Astashkin–Lykov's later weighted-chaos estimates and their historical context are detailed in the [priority review](rooted-paths-priority-audit.md).

The [fresh independent audit](rooted-paths-full-source-audit.md) checks the proof, native coordinates, range identity, constant improvement and query normalization. The [exact arithmetic verifier](checks/rooted_paths_independent_check.py) supplements the universal proof with 3,905 Rademacher moment cases and 30,948 truncation inequalities. Neither finite checks nor assistant review are formal verification or human peer review. The full AA conjecture remains unresolved; the exact priority of this rooted-path formulation is not certified.
