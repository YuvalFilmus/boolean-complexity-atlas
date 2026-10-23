# Fresh independent audit of the rooted-path AA consequence

23 October2026 audit; literature checked in this task. Audited target: `outputs/open-problem-progress-round3-2026-10-23/aa-rooted-paths.md`. This reviewer authored the separate exact-search work, not this AA argument. I read the prior audit only after locating the target and independently checked every universal step below. No public edits.

**Verdict: PASS for the stated12d influence constant, spectral-mass estimate, and nonadaptive query bound.** A classical source-dependent strengthening replaces12d by8d. The target is a support-restricted analytic consequence, not a general AA resolution; novelty is not certified. A materially broader classical comparison is recorded separately below.

## Independent derivation

Let p=a_0+Σ_P a_P χ_P in independent uniform signs on original tree edges, where P ranges over distinct nonempty ancestor–descendant paths of length≤d. Let A=Σ|a_P|, V=Σa_P², W=maxp−minp, and I_e=Σ_(P∋e)a_P². The last expression is the half-bitflip/Fourier influence. Nonconstant p gives d≥1 and W>0.

For a simple endpoint graph, Q(z)=Σ_uv a_uv z_u z_v. Its symmetric bilinear form has matrix entries b_uv=a_uv/2 off the diagonal, and B(s,t)=Σ_uv b_uv s_u t_v. Expansion gives

    B(s,t)=Q((s+t)/2)−Q((s−t)/2).

Both arguments are in the sign cube's convex hull. Independently rounding each coordinate with its prescribed mean represents each multilinear Q value as an average of Boolean values, so |B(s,t)|≤W_Q. For fixed t, maximizing over s gives exactly(1/2)Σ_v|Σ_u a_uv t_u|, with no missing factor2. Distinct neighbors correspond to distinct independent signs; loops or duplicate coefficients would invalidate this immediate use of Rademacher sums, but the path graph has neither.

For L=Σb_jε_j, direct expansion gives E L²=Σb_j²=σ² and E L⁴=3σ⁴−2Σb_j⁴≤3σ⁴. Hölder yields σ²≤(E|L|)^(2/3)(E L⁴)^(1/3), hence E|L|≥σ/√3, including σ=0 by continuity/direct evaluation. Therefore

    W_Q≥(1/(2√3))Σ_v sqrt(Σ_u a_uv²).

Orient the endpoint edge of each path from descendant to ancestor. At a fixed tail there is at most one ancestor at each distance1,…,d; outdegree≤d regardless of branching or height. Charge each edge coefficient once to its tail. Cauchy–Schwarz gives A≤√d Σ_v sqrt(Σ_u a_uv²), and hence A≤2√(3d)W_Q.

For nonroot v put z_v=∏_(e on[o,v])x_e and z_o=1. The inverse x_(parent(v),v)=z_parent(v)z_v establishes bijectivity, uniformity and exact range preservation. Every path monomial becomes z_u z_v. The root-incident monomials are linear; writing the transformed polynomial without its constant as q=L+R, freeing the root sign creates Q(1,z)=q(z) and Q(−1,z)=q(−z). Both root slices have identical ranges, so W_Q=W, exactly. No extra factor2 is introduced.

Now V≤A max_P|a_P|. A maximizing nonempty path contains at least one original edge e, whose native influence contains the squared coefficient. Thus max_e I_e≥(V/A)²≥V²/(12dW²). This avoids transferring influences through a nonlocal character transformation: such a transfer would be false. For example x_a(x_b+x_c) becomes z_b+z_c, so the original a-influence is2 while prefix z_a-influence is0.

For[0,1]-valued p, W≤1, giving V²/(12d). For[−1,1], W≤2, giving V²/(48d). Mapping the input bits between{0,1} and{±1} does not alter the bitflip difference, but using the full difference rather than half-difference multiplies influence by4. In particular the original AA2014 Conjecture1.7 uses the full-bitflip convention; the target's Fourier convention is correctly explicit.

## Nonadaptive approximation, in native query cost

Select the m largest nonconstant coefficient magnitudes. Let t be the largest omitted magnitude; when any are omitted, the retained mass is≥mt and omitted mass is≤A−mt. Therefore the omitted squared mass is≤t(A−mt)≤A²/(4m). Ties and zero omitted mass cause no exceptions. Original-character orthogonality gives the exact uniform squared approximation error. For[0,1]-valued p, A²≤12d, so squared error≤3d/m. Markov on squared error gives failure probability≤δ with m=ceil(3d/(δε²)). Each retained original path costs≤d edge queries, so the deterministic nonadaptive total is≤d ceil(3d/(δε²)). Root-prefix variables are not treated as unit-cost queries. Clipping to[0,1] cannot increase error. This is representation-available existence, not efficient Fourier-coefficient discovery and not arbitrary quantum simulation.

## Other assertions

At fixed path lengthℓ the endpoint graph is a forest: a maximum-depth vertex in any cycle would need two different ancestors at the same distance. Its edge incidence vectors over F₂ are independent; setting z_o=1 cannot create a relation supported only at the root, because a graph cannot have exactly one odd-degree vertex. Length partitioning therefore gives independent coefficient mass≥A/d.

For the arbitrary-path boundary example with Hadamard H, HHᵀ=mI gives ||H||_(2→2)=√m. Thus |xᵀHy|≤m^(3/2), A=√m, V=1/m, and each native influence=1/m²=V². The connected K_(m,m) incidence rank is2m−1, giving the stated independent-mass ratio. It defeats the proposed ℓ1/independence-mass extension, and does not refute AA.

## Separately source-dependent8d improvement

Szarek's sharp real Rademacher L1 lower bound E|Σb_jε_j|≥||b||₂/√2 replaces the weaker fourth-moment1/√3 step. All remaining steps above are unchanged. It gives

    A≤2√(2d)W,
    max_e I_e≥V²/(8dW²),
    native queries≤d ceil(2d/(δε²))  for range[0,1].

For range[−1,1], the corresponding influence guarantee is V²/(32d). This is a classical constant substitution, not a new sharp Khintchine theorem. The target12d version remains self-contained. Original Szarek1976 Theorem1, printedp198 (left half ofPDFspread2), has now been visually checked in the original scan obtained by root: `work/round4-sources/Sz76.pdf`, SHA25631bf836a493917760154c0886181feb023bbc2d193edc8c70211eac0b767a070. It states precisely the1/√2 lower bound for every real square-summable coefficient sequence; finite independent signs are the finite Rademacher special case. Originalabstract printedp197 also states the sharpconstant. This verifies the imported statement, not a fresh reconstruction of Szarek's proof. Explicit primary restatements are Astashkin–Lykov arXiv2412.20107v1 §2.1 Eq(6), and Eskenazis–Nayar–Tkocz introduction Eq(1).

## Broader classical comparison, not a novelty claim

The prefix transform sends **every** simple path in a tree to an endpoint quadratic monomial, even when its endpoints are incomparable. A dimension-free Boolean degree-two Bohnenblust–Hille bound therefore applies to all tree-path Fourier support. In the notation C₂ for a valid degree-two coefficient constant,

    (Σ_P|a_P|^(4/3))^(3/4)≤C₂ W.

Let M=max|a_P|. Then V≤M^(2/3)Σ|a_P|^(4/3)≤M^(2/3)(C₂W)^(4/3), so max_native I_e≥M²≥V³/(C₂⁴W⁴), independently of d. This is a verified derived consequence of the published coefficient theorem, not a claim that the original BH papers state native tree-edge influences.

For comparison, the rooted-path bound V²/(12dW²) has a better variance exponent but introduces d; neither estimate uniformly dominates for all V,d. Likewise BH coefficient truncation supplies dimension-free term approximations that can be evaluated in native path cost, with a different δ,ε dependence. The target should not imply that AA's qualitative polynomial-in-variance validity on tree-path supports was previously unattainable; its useful feature is the explicit stronger spectral/variance estimate on the ancestor–descendant subclass.

The source/priority report records exact original locators and limitations. No global openness status, native-vs-transformed influence identification, or general quantum simulation is justified by this audit.

## Final publication rewrite

The fresh reviewer also read [the exact publication rewrite](rooted-paths-proof.md). Verdict: **PASS** after explicitly attaching the range $0\leq p\leq1$ to the source-dependent improved query bound. The theorem and constants retain their stated native-coordinate conventions. The imported Szarek statement was visually checked in the original scan; its full original proof was not reconstructed.
