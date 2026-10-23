# Influence bounds for all tree-path supports

The path-length factor in the earlier rooted-path influence bound can be removed. The result applies to every tree-path Fourier support, including paths between incomparable vertices. More generally, it applies whenever an invertible binary change of character basis makes the polynomial quadratic.

The proof uses each original coordinate influence as a cut energy in a graph of transformed characters. Those cuts permit a fractional allocation of edge energies to endpoints. Combining this allocation with a classical quadratic-chaos estimate gives a variance-quadratic influence bound. The [priority review](graphic-influence-priority-audit.md) records the established ingredients and the limits of the search for this precise consequence.

## Statement and conventions

Let $p$ be a nonconstant real function on $N$ independent uniform signs, with Fourier expansion

$$p(x)=a_0+\sum_{S\ne\varnothing}a_S\chi_S(x),\qquad\chi_S(x)=\prod_{i\in S}x_i.$$

Assume there is a basis $\lambda_1,\ldots,\lambda_N$ of $\mathbb F_2^N$ such that every nonzero nonconstant Fourier coefficient is indexed by either $\lambda_u$ or $\lambda_u+\lambda_v$ with $u\ne v$. Equivalently, setting $z_v=\chi_{\lambda_v}(x)$ expresses $p$ as a polynomial of degree at most two in independent signs $z$.

Write

$$V=\operatorname{Var}(p)=\sum_{S\ne\varnothing}a_S^2,\qquad W=\max_xp(x)-\min_xp(x)>0,$$

and use the influence of an **original** coordinate,

$$I_i(p)=\mathbb E\!\left[\left(\frac{p(x)-p(x^{\oplus i})}{2}\right)^2\right]=\sum_{S\ni i}a_S^2.$$

**Proposition.** Under these assumptions,

$$\max_i I_i(p)\geq\frac{V^2}{12W^2}.$$

A self-contained moment proof gives this constant. Importing Szarek's sharp real lower Khintchine inequality improves it to

$$\max_i I_i(p)\geq\frac{V^2}{8W^2}.$$

For $0\leq p\leq1$, this gives $V^2/8$; for $-1\leq p\leq1$, it gives $V^2/32$. Full squared-flip influences are four times the displayed half-flip/Fourier convention. No constant is asserted optimal.

## A weighted cut lemma

Let $G=(U,E)$ be a finite simple graph with energies $b_e\geq0$ and injective labels $\lambda:U\to\mathbb F_2^N$. Define

$$t_i=\sum_{uv:\,\lambda(u)_i\ne\lambda(v)_i}b_{uv},\qquad t=\max_i t_i,\qquad B=\sum_e b_e,\qquad R=\sum_{v\in U}\sqrt{\sum_{e\ni v}b_e}.$$

**Lemma.** $B\leq\sqrt t\,R$. If $N=0$, injectivity allows at most one vertex, so the conclusion is immediate with $B=0$.

**Proof.** If $t=0$, any positive-energy edge would have a coordinate separating its distinct endpoint labels and would make that cut positive. Hence $B=0$. Assume $t>0$.

Every nonempty vertex set $A$ satisfies

$$b(E(A))\leq t(|A|-1).$$

Induct on its size. A singleton has no internal edges. For larger $A$, some label coordinate splits it into two nonempty sets $A_0,A_1$. Their crossing energy is at most $t$. Adding the two induction bounds and this crossing bound proves the claim. The graph may be disconnected and may contain isolated vertices.

Allocate each edge energy fractionally to its endpoints using the following finite network. The source has an arc of capacity $b_e$ to each edge node. Each edge node has arcs of capacity $C>B$ to its two endpoints. Each vertex has an arc of capacity $t$ to the sink. Any source–sink cut of capacity below $B$ would avoid all edge-to-endpoint arcs. If $A$ is its source-side vertex set, all its source-side edge nodes then lie in $E(A)$, and its capacity is at least

$$B-b(E(A))+t|A|\geq B.$$

For $A=\varnothing$ the lower bound is $B$ directly. Thus every cut has capacity at least $B$.

For completeness, the needed real-capacity flow assertion follows from a short maximality argument. The feasible flows form a nonempty compact set, so a flow of maximum value exists. If its residual network has a source–sink path, augment by the minimum positive residual capacity on a simple such path, contradicting maximality. Otherwise the vertices reachable from the source form a cut. Every forward arc of that cut is saturated and every backward arc carries zero flow. Conservation then makes the flow value equal its cut capacity. Hence the maximum equals the minimum cut, and in this network it is $B$, since the source arcs have total capacity $B$. This proof does not assume termination of an augmenting-path algorithm with irrational capacities.

The resulting endpoint loads $w_v$ satisfy

$$\sum_vw_v=B,\qquad 0\leq w_v\leq t,\qquad w_v\leq\sum_{e\ni v}b_e.$$

Therefore

$$B=\sum_vw_v\leq\sqrt t\sum_v\sqrt{w_v}\leq\sqrt t\sum_v\sqrt{\sum_{e\ni v}b_e}=\sqrt t\,R.$$

Only a fractional allocation is claimed; an unsplit orientation of real edge weights is unnecessary. ∎

This allocation is a classical weighted-density/fractional-orientation mechanism. The proof above includes its full feasibility argument. Historical flow and modern weighted-orientation sources are detailed in the [priority review](graphic-influence-priority-audit.md).

## The quadratic norm estimate

For a weighted graph quadratic $Q(z)=\sum_{uv}a_{uv}z_uz_v$, set $W_Q=\max Q-\min Q$ and $R=\sum_v\sqrt{\sum_u a_{uv}^2}$. We need

$$R\leq2\sqrt3\,W_Q.$$

For sign vectors $s,t$, symmetric polarization gives

$$\frac12\sum_{uv}a_{uv}(s_ut_v+s_vt_u)=Q((s+t)/2)-Q((s-t)/2).$$

Both arguments are in $[-1,1]^U$. A multilinear polynomial there is an average of sign-cube values by independent rounding with the prescribed means. Thus the absolute difference is at most $W_Q$. For fixed $t$, choose each $s_v$ to agree with its incident linear sum. The left side becomes $\tfrac12\sum_v|\sum_u a_{uv}t_u|$.

For $L=\sum_j c_j\epsilon_j$ in independent signs, with $\sigma^2=\sum_jc_j^2$, direct expansion and Hölder give

$$\mathbb EL^4=3\sigma^4-2\sum_jc_j^4\leq3\sigma^4,\qquad\sigma^2\leq(\mathbb E|L|)^{2/3}(\mathbb EL^4)^{1/3}.$$

Hence $\mathbb E|L|\geq\sigma/\sqrt3$. Average the chosen bilinear form over $t$ to obtain $W_Q\geq R/(2\sqrt3)$. This proves the displayed estimate. Szarek's published inequality $\mathbb E|L|\geq\sigma/\sqrt2$ gives the source-dependent improvement $R\leq2\sqrt2\,W_Q$ by the identical argument.

## Apply the graph lemma in the original coordinates

Represent a singleton term $a_u z_u$ as an edge from vertex $u$ to an anchor $o$ labeled $\lambda_o=0$. Represent a pair term by its endpoint edge. The other vertex labels are the independent basis vectors $\lambda_v$. All labels are distinct, and distinct edges have distinct nonzero native character labels $\lambda_u+\lambda_v$. Put $b_{uv}=a_{uv}^2$.

Flipping original coordinate $i$ changes precisely the edge characters whose endpoint labels differ at that coordinate. Fourier orthogonality therefore gives the exact identity

$$I_i(p)=\sum_{uv:\,\lambda(u)_i\ne\lambda(v)_i}b_{uv}=t_i,\qquad B=V.$$

The cut lemma yields $V\leq\sqrt{\max_iI_i}\,R$. To apply the quadratic estimate with the original oscillation, note that the nonroot characters form an invertible basis change and so range over the full independent sign cube. The anchor is initially fixed at one. If $q(z)=p(x(z))-a_0=L(z)+Q_2(z)$, freeing its sign gives

$$Q(1,z)=q(z),\qquad Q(-1,z)=-L(z)+Q_2(z)=q(-z).$$

Both slices have the same range. Thus $W_Q=W$, and

$$V\leq2\sqrt{3\max_iI_i}\,W.$$

Rearranging proves the denominator-12 bound. The imported sharp Khintchine inequality replaces 3 by 2 and gives the denominator-8 bound. ∎

The graph lemma only requires distinct labels. Its polynomial application additionally requires the independent-basis/range condition. Dependent character labels may restrict the free graph variables to a small subset and increase the free graph oscillation. They cannot be substituted here to infer a general AA theorem. Nor are transformed-coordinate influences identified with original-coordinate influences.

## Every tree path is covered

Put independent original input signs on the edges of any finite rooted tree. For each nonroot vertex $v$, let $z_v$ be the product of edge signs on the root-to-$v$ path. The inverse $x_{\operatorname{parent}(v),v}=z_{\operatorname{parent}(v)}z_v$ proves that these prefix characters form an invertible basis. For **any** simple path between distinct vertices $u,v$, including incomparable endpoints,

$$\prod_{e\in[u,v]}x_e=z_uz_v,\qquad z_o=1.$$

Consequently a polynomial whose nonconstant Fourier supports are arbitrary tree paths satisfies the proposition. No path-length, branching, height or occurrence-count factor appears in this influence bound. Short original paths are needed only when translating term approximations into native query cost.

The earlier [rooted-path page](rooted-paths-proof.md) retains its stronger Fourier-mass estimate on ancestor–descendant supports and its different approximation bound. The present result strengthens its influence conclusion and broadens the support class; it does not assert a dimension-free Fourier $\ell_1$ bound.

## Variance exponent and approximation

The variance exponent two cannot be uniformly reduced on this class of bounded polynomials. On a star, split $2m$ leaf-edge variables as $x,y$, choose a real Hadamard matrix $H$ of order $m$, and put

$$p_m(x,y)=x^{\mathsf T}Hy/m^{3/2}.$$

Then $|p_m|\leq1$, $V=1/m$, and every native influence is $1/m^2=V^2$. All supports are length-two paths. Mapping to $[0,1]$ gives native influence $4V_{\rm new}^2$ and arbitrarily small positive variance. Thus no fixed positive multiple of $V^\alpha$ with $\alpha<2$ works uniformly. This does not establish an optimal numerical constant or oscillation dependence.

A separate classical coefficient argument also gives a representation-available nonadaptive approximation when every original support has size at most $d$. Let $L=\sum_{uv}|a_{uv}|^{4/3}$. Writing $R_v=(\sum_u a_{uv}^2)^{1/2}$ and applying Hölder with exponents $3,3,3$ to the symmetric matrix gives

$$2L\leq R^{4/3}.$$

Indeed factor each ordered term as $(a_{uv}^2/R_u)^{1/3}(a_{uv}^2/R_v)^{1/3}(R_uR_v)^{1/3}$, omitting zero rows. The first two sums equal $R$ and the third is at most $R^2$. Keep the $m$ largest coefficients. If $t$ is the largest omitted magnitude, squared tail energy is at most

$$t^{2/3}(L-mt^{4/3})\leq\frac{2L^{3/2}}{3\sqrt{3m}}\leq\sqrt{\frac83}\frac{W^2}{\sqrt m}.$$

For $0\leq p\leq1$, choosing $m=\lceil8/(3\delta^2\varepsilon^4)\rceil$, querying the union of those supports, and clipping the estimate gives uniform-input additive error at most $\varepsilon$ with failure probability at most $\delta$. This uses at most $dm$ original queries. This approximation is a classical mixed-norm consequence, separate from the stronger weighted-cut influence argument; it is not an efficient coefficient-recovery algorithm.

## Sources, reproducibility and status

The [fresh independent audit](graphic-influence-full-source-audit.md) checks the graph, flow, character-basis, normalization and boundary arguments. An [independent exact verifier](checks/graphic_influence_independent_check.py) uses exhaustive endpoint-allocation search rather than the author's flow implementation. A [second verifier](checks/graphic_influence_check.py) checks exact rational flows and native-cut identities. Finite checks supplement the universal proof.

S. J. Szarek, *On the best constants in the Khinchin inequality*, Studia Mathematica **58**(2), 197–208 (1976), DOI [10.4064/sm-58-2-197-208](https://doi.org/10.4064/sm-58-2-197-208), Theorem 1, printed p.198, supplies only the source-dependent sharp constant. Its original statement was visually checked; its full original proof is not reconstructed here.

The analytic estimate and fractional-allocation method are established ingredients. The [original-source and priority review](graphic-influence-priority-audit.md) gives bibliographic details and distinguishes this variance-quadratic native consequence from earlier coefficient-based variance-cubic bounds. No prior publication of this precise consequence was located in the bounded search. Novelty, global optimality, formal verification and human peer review are not certified. The general Aaronson–Ambainis conjecture remains unresolved.
