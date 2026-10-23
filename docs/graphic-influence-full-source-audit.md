# Fresh independent audit: graphic-character native influence

23 October 2026. **PASS** for the main weighted-cut lemma, its native-influence consequence, the all-tree-path specialization, and the stated auxiliary coefficient/truncation bounds. I did not author or review the stronger weighted-cut argument in round four. I read the exact target afresh and reconstructed its universal proof; this verdict does not rely on its prior independent-review label. No public files were edited.

Target: `outputs/open-problem-progress-round4-2026-10-23/graphic-character-influence.md`, SHA-256 `af8d415dec6c7cdab014f7f8c1d4e1ef9a395e04af6eddf798a903d3e826dbad`. Imported elementary analytic proof independently reconstructed from `work/aa-round3.md`, SHA-256 `a55a5e77ac3c3da4849a5a2916082a20fe9338f06a0750d85e95d0445606f24f`. This is assistant mathematical review plus independent finite checks, not formal verification, human peer review, or novelty certification.

## 1. Weighted-cut lemma, including real capacities

Let b_e be nonnegative real edge energies, and let vertex labels in F_2^N be injective. The subset-energy induction is correct for every nonempty A, even if disconnected or containing isolated vertices. At least one coordinate separates two labels whenever |A|≥2, so A splits into two nonempty parts; the crossing energy is at most the global t for that coordinate. Adding both induction hypotheses yields b(E(A))≤t(|A|−1). The choice of splitting coordinate may change between induction nodes. No binary independence or connectivity is required here.

If t=0, a positive-energy edge would be separated by a label coordinate, a contradiction; thus V=0. If N=0, injectivity permits at most one vertex and a simple graph has no edge. Empty graphs and zero-energy edges cause no problem. Treat these cases before dividing or taking maxima over empty coordinate sets.

For t>0, choose any real C>V in the edge-to-endpoint arcs. In a source–sink cut of capacity less than V, no such arc can cross. For its source-side vertex set A, every source-side edge node consequently represents an internal edge of A. The source-to-edge contribution is therefore at least V−b(E(A)); the vertex-to-sink contribution is t|A|. Their sum is ≥V for nonempty A, and ≥V directly when A is empty. Thus no cut has capacity below V. The cut consisting only of the source has capacity V, so the minimum cut equals V.

The finite max-flow/min-cut theorem is valid for **real**, not just rational or integral, capacities. One can use the standard finite-dimensional linear-programming theorem (or a compactness/minimum-cut proof); termination of an arbitrary augmenting-path algorithm is not needed. Feasible flows are bounded by finite capacities, a maximum exists, and equality with the minimum cut supplies a value-V flow. This saturates all source-edge supplies, producing endpoint loads w_v with sum V, w_v≤t, and w_v≤incident energy at v. No indivisible orientation is claimed.

The scalar inequality w≤sqrt(t)sqrt(w) follows from 0≤w≤t, including w=0. Summing and then replacing each w_v by its incident energy proves V≤sqrt(t)R. Every imported graph feasibility condition is explicit. I found no missing cut condition or integrality assumption.

## 2. Quadratic moment and polarization ingredient reconstructed

For the homogeneous simple-graph quadratic Q, define B(s,t)=1/2 sum a_uv(s_u t_v+s_v t_u). Direct expansion gives B(s,t)=Q((s+t)/2)−Q((s−t)/2). Both arguments lie in the continuous box. A multilinear polynomial's value there is a convex combination of sign-cube values (independent sign rounding with specified means); hence |B|≤osc(Q), rather than an unspecified supremum norm.

Choose each s_v as the sign of its row linear form. This gives B=1/2 sum_v |sum_u a_uv t_u|. Under independent uniform t, for L=sum b_j t_j, E L²=σ² and E L⁴=3σ⁴−2sum b_j⁴≤3σ⁴. Hölder with exponents 3/2 and 3 applied to |L|^(2/3)|L|^(4/3) yields E|L|≥σ/sqrt(3), including σ=0 separately. Therefore R≤2sqrt(3)osc(Q). This step requires **no orientation or outdegree bound**; those occurred only in the older spectral-mass application. Arbitrary real signs and zero rows are allowed.

These normalizations yield exactly V≤sqrt(t)R≤2sqrt(3t)W, so t≥V²/(12W²). There is no missing factor of two in either the symmetric bilinear form or the incidence energies.

## 3. Character change, anchor and original influences

An invertible binary character change is a bijection of the sign cube, preserving its uniform distribution and its entire range. Its N nonzero basis labels are independent, distinct, and distinct from the anchor label zero. Singleton and unordered pair supports are distinct nonempty sums of these labels. Thus graph edges correspond one-to-one with the original nonconstant Fourier supports; energies are a_e² and Parseval gives V=sum_e a_e². No collisions or coefficient cancellations are silently discarded.

The anchor is initially the **constant** sign. After subtracting the constant Fourier coefficient, write the anchored polynomial q(z)=L(z)+R(z), with L linear and R homogeneous quadratic. Freeing the anchor yields Q(1,z)=q(z), Q(−1,z)=q(−z). Because all nonanchor z signs are independently free, the latter has exactly the same set of values. Therefore the full graph cube has exactly the original oscillation W. A constant term only translates the range.

For native coordinate i, the native support associated with uv contains i exactly when the endpoint labels differ at i. Consequently its native Fourier influence is exactly the coordinate-cut energy t_i. It is **not** identified with the influence of a transformed basis variable. Combining this precise identity with the weighted-cut lemma proves the proposition. For nonconstant p, V>0 and W>0, so division is legitimate. For constant p the undivided inequality is trivial, while the displayed quotient should remain excluded. The range[0,1] and range[−1,1] constants 1/12 and 1/48 follow from W≤1 and W≤2.

The dependent-label warning is essential and correct: the graph lemma permits dependent labels, but its polynomial consequence needs a free independent character cube. For an explicit test, take all seven nonzero characters on three bits as leaves of a star with unit coefficients and anchor zero. Their sum is 7 at the all-plus native point and −1 at the other seven points, with oscillation 8. The corresponding independent seven-leaf star has oscillation 14. Thus replacing native range by free graph range under arbitrary dependent labels is false. The proof does not do so.

## 4. Tree paths, auxiliary bounds and boundary example

For a finite tree with one native variable per edge, root-prefix characters of the nonroot vertices form a binary basis: the inverse is x_parent(v),v=z_parent(v)z_v. Every nonempty simple path, including between incomparable vertices, becomes the pair of endpoint characters, with root endpoints interpreted as singleton terms. Different endpoint pairs give different path supports. Hence the proposition applies to **all** tree paths with no length, height, branching or occurrence restriction in the influence bound.

The Littlewood-type auxiliary calculation also checks. Three-factor Hölder on ordered edges gives 2L≤R^(4/3); the first two factor sums equal R and the third is bounded by R². V≤M^(2/3)L gives M²≥8V³/R⁴≥V³/(18W⁴). This is a weaker alternative to the weighted-cut consequence, with correctly stated constants.

For m retained coefficients and largest omitted magnitude t, the tail energy is ≤t^(2/3)(L−m t^(4/3)). Optimizing gives 2L^(3/2)/(3sqrt(3m))≤sqrt(8/3)W²/sqrt(m). For range[0,1], m=ceil(8/(3δ²ε⁴)) makes this ≤δε². Markov on squared error and optional clipping give the stated average-input ε approximation with failure probability ≤δ; at most dm **native** variables are queried only if each original support has size≤d. These are existence statements given the representation. Querying transformed characters for unit cost is not assumed.

For the Hadamard boundary, HHᵀ=mI gives |xᵀHy|≤m^(3/2); scaling gives V=1/m and each native I=1/m². These are tree paths on a star with 2m leaves. Therefore no fixed positive bound cV^α with α<2 holds uniformly on this bounded class. After mapping to [0,1], V_new=1/(4m), I_new=1/(4m²)=4V_new². No best constant claim follows.

## 5. Source-dependent denominator 8

I visually re-read the original Szarek scan, Theorem 1, printed p.198 (`work/round4-sources/Sz76-page2.png`). It states the real-coefficient Rademacher L1 lower bound with constant 1/sqrt(2). Finite independent uniform signs have precisely that distribution, so replacing only the moment estimate by this theorem gives R≤2sqrt(2)W and **max native I≥V²/(8W²)**. This constant depends on importing Szarek's theorem, whose full proof was not freshly audited here. The denominator12 proof remains elementary and self-contained apart from finite max-flow/min-cut. Both versions have the same independence/range/native-coordinate requirements.

Reference: S. J. Szarek, “On the best constants in the Khinchin inequality,” *Studia Mathematica* 58(2), 197–208 (1976), DOI [Original source](https://doi.org/10.4064/sm-58-2-197-208). Original scan [Original source](https://matwbn.icm.edu.pl/ksiazki/sm/sm58/sm58113.pdf) ; private snapshot SHA-256 `31bf836a493917760154c0886181feb023bbc2d193edc8c70211eac0b767a070`. The imported statement and its application are verified; no novelty follows from using it.

## 6. Fresh independent structural verifier

I wrote `work/check_graphic_influence_fresh_round5.py` without reading or importing the author's flow checker. Instead of max flow it uses exhaustive endpoint-load dynamic programming for finite integer edge energies. This is a genuinely different implementation of the finite allocation feasibility check. Integer energies also represent rational energies after common scaling; the universal proof handles all real energies.

The checker exhausts all 168 ordered invertible bases on three bits and all 728 nonzero coefficient vectors in {−1,0,1}^6 for the four-vertex anchor graph: **122,304 signed polynomial cases**. It computes native character values, anchored and free quadratic ranges independently, checks unique supports and the exact native-cut identity, every induced subset inequality, and the integer form of both denominator12 and denominator8 influence bounds. It separately checks **4,980 injectively labeled graph energy instances**, allowing dependent labels, with exhaustive endpoint allocation rather than a flow implementation. Empty N=0 cases and the explicit dependent-label range counterexample also pass.

Reproduce with `python3 work/check_graphic_influence_fresh_round5.py`. Output: `work/graphic-influence-fresh-checks-round5.json`, status PASS. The finite tests do not replace the universal proof or establish optimal constants.

## Conclusion

No flaw or publication-blocking issue found in the audited target. Preserve the invertible character-change hypothesis, full independent range, native influence convention, nonconstant W>0 condition, and degree bound only for native query cost. The general AA conjecture remains unresolved and no priority certification is supplied by this audit. Final public rewrite remains to be checked separately when provided.

## Final public rewrite review

I separately read the exact completed public rewrite `outputs/boolean-measures/docs/graphic-influence-proof.md` in full. **PASS; no correction required.** It preserves the assumptions, native half-flip normalization, denominator12 elementary proof, source-dependent denominator8 improvement, anchor range identity, independent-label warning, all-tree-path specialization, Hadamard boundary and original-coordinate approximation interpretation.

The newly expanded real-capacity max-flow proof is correct: its finite feasible-flow polytope is nonempty and compact; an actual maximum therefore exists. A residual source–sink path would admit positive augmentation by its smallest residual capacity and contradict maximality. Otherwise reachability defines a cut whose forward arcs are saturated and backward arcs have zero flow, proving equality by conservation. It does not assume that an iterative algorithm terminates for irrational capacities. Every arc capacity in the present finite network is finite, so the compactness argument applies.

The mixed-norm paragraph retains 2L≤R^(4/3), the tail bound sqrt(8/3)W²/sqrt(m), and, explicitly for range[0,1], m=ceil(8/(3δ²ε⁴)), at most dm native queries and failure probability≤δ. The page correctly gives range[0,1] and range[−1,1] influence corollaries V²/8 and V²/32 only for the imported denominator8 estimate, and notes that full squared-flip influences are four times these conventions. No mathematical drift from the freshly audited packet was found.

Reviewed final-page SHA-256: `9e26b9edde1c8a7b7825acf5758eb2b09cc4e5dbe4a154b12df77ba67dee8210`.
