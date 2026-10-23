# Priority review: native influence for quadratic character changes

23October2026. Review target: `work/other-open-problems-round4.md`§§2–3. No public edits. This is a bounded original/primary-source priority review, not a global novelty certification.

## Conclusion

The stronger estimate

    max_native I_i ≥ Var(p)²/(12 osc(p)²)

for Fourier supports made singleton/pair characters by an invertible F₂ character change is mathematically independently audited. It applies to **all simple tree-path supports**, without an ancestor restriction or a path-length parameter in the influence bound. I did not locate an original publication explicitly stating this exact native-coordinate consequence. That failure is not evidence of novelty.

The quadratic norm ingredient, the endpoint capacity assignment, and the sharper Khintchine constant are established classical tools. The proper description is **a checked derived consequence of classical quadratic-chaos and fractional-orientation methods; exact prior publication not located**. It should not be presented as a resolution of general AA, as a newly discovered quadratic-chaos theorem, or as the first AA-positive support class.

The earlier Boolean Bohnenblust–Hille/large-coefficient route gives a variance-**cubic** guarantee after arbitrary invertible character transforms making the support quadratic. The new cut argument improves this to variance-**quadratic** by retaining the full native-cut energies. The weaker consequence alone does not establish that the stronger exponent was previously published.

## Sharp Khintchine substitution

The stronger proof has R≤2√3 W and V≤√I_max R. Substituting the published sharp L1 Rademacher bound gives R≤2√2 W and therefore

    I_max ≥ V²/(8 W²).

For range[0,1], this is V²/8; for range[−1,1], it is V²/32. Influences here are Fourier/half-bitflip influences; the full squared-flip convention multiplies all influence values by4. **The8 is not certified optimal for this problem.** Only the imported1/√2 Khintchine constant is sharp.

Direct original verification: S. J. Szarek, *On the best constants in the Khinchin inequality*, Studia Mathematica58(2),197–208(1976), DOI [Original source](https://doi.org/10.4064/sm-58-2-197-208) , Theorem1 printedp198. Original scan [Original source](https://matwbn.icm.edu.pl/ksiazki/sm/sm58/sm58113.pdf) , privately captured as `work/round4-sources/Sz76.pdf`, SHA25631bf836a493917760154c0886181feb023bbc2d193edc8c70211eac0b767a070. I visually checked the real square-summable hypothesis and1/√2 constant on spread2left. This is statement verification, not a fresh proof audit of Szarek's entire paper.

## Established analytic predecessor

Sergey V. Astashkin and Konstantin V. Lykov, *Random unconditional convergence of Rademacher chaos in L∞ and sharp estimates for discrepancy of weighted graphs and hypergraphs*, Mathematische Annalen393(1),407–438(2025), DOI [Original source](https://doi.org/10.1007/s00208-025-03257-9) ; original preprint arXiv:2412.20107v1,28December2024, [Original source](https://arxiv.org/html/2412.20107v1) . Directly checked §2.1 Eq(6), §2.4 Lemma1, and Theorem3/Eq(27). These treat signed real coefficients, allow zero coefficients, and establish quadratic-chaos norm control by coefficient row/column ℓ2 sums. They overlap the graph analytic mechanism directly. They do **not**, in the inspected passages, identify original-coordinate influences after arbitrary binary character changes or state the weighted separating-cut consequence. Their supremum/decoupling constants should not be silently identified with the elementary oscillation proof's constants. Their introduction attributes the unimodular precedent to Bennett1977 and mentions later rediscovery; I did not re-audit Bennett's original proof.

Earlier direct source: S. V. Astashkin, *Rademacher chaos in symmetric spaces*, East Journal on Approximations4(3),311–336(1998), author manuscript [Original source](https://astashkin.ssau.ru/papers/21.pdf) . Freshly inspected manuscript§4, Theorem5,p13, and the Walsh-matrix proposition,pp14–15. These supply explicit Khintchine/bilinear and Hadamard predecessors. Local source hash5e7312cefdc2aac8d5a890654712713ab38834a20a4f5b01c97809994c2f2272. Thus the variance-exponent boundary construction is classical; its use to delimit the present consequence is derived.

## Established fractional endpoint assignment

A direct modern primary statement covers exactly the weighted fractional-orientation ingredient:

Aleksander Bjørn Christiansen, Ivor van der Hoog, and Eva Rotenberg, *Local Density and Its Distributed Approximation*,42nd International Symposium on Theoretical Aspects of Computer Science(STACS2025), LIPIcs327,25:1–25:20(2025), DOI [Original source](https://doi.org/10.4230/LIPIcs.STACS.2025.25) . Original published full text:
[Original source](https://drops.dagstuhl.de/storage/00lipics/lipics-vol327-stacs2025/html/LIPIcs.STACS.2025.25/LIPIcs.STACS.2025.25.html) . Directly inspected §2 “Preliminaries and related work”: positive weighted edges and fractional orientation definitions, DS/FO dual linear programs, and the equality between maximum weighted subgraph density and minimum maximum fractional outdegree. Corollary10 reiterates the equality. Zero-energy edges may simply be deleted. Consequently, induced density≤t supplies a fractional endpoint assignment with every load≤t. This verifies that this ingredient is established, without attributing real-weighted indivisible orientations to an inappropriate source. The research note's explicit max-flow proof is a self-contained derivation of this standard feasibility fact.

Historical precursor: S. Louis Hakimi, *On the degrees of the vertices of a directed graph*, Journal of the Franklin Institute279(4),290–308(1965), DOI [Original source](https://doi.org/10.1016/0016-0032(65))90340-6 . Bibliography and its degree-constrained orientation role are cross-checked in primary later papers, including ICALP2025 *On Deleting Vertices to Reduce Density in Graphs*. The original full text was not accessible in this review. **Do not label its exact weighted fractional statement directly read.** Integral orientation, fractional endpoint assignment and unsplit real edge weights must remain distinct.

The only graph-specific step beyond standard feasibility is the separating-label recursion: if every label-coordinate cut has energy≤t, splitting any induced vertex subset along a nonconstant coordinate gives internal energy≤t(|A|−1). This recursion plus the standard fractional-orientation theorem yields V≤√t Σ_v√D_v. No exact original source for that package under the label/cut wording was found. It is elementary enough that absence from these searches does not warrant a priority claim.

## Comparison with published coefficient bounds

Andreas Defant, Mieczysław Mastyło and Antonio Pérez, *On the Fourier spectrum of functions on Boolean cubes*, Mathematische Annalen374(1–2),653–680(2019), DOI [Original source](https://doi.org/10.1007/s00208-018-1756-y) ; original arXiv:1706.03670v1,12June2017, [Original source](https://arxiv.org/pdf/1706.03670) . Direct locator: §1.1 Eq(2),manuscriptp2, and Theorem1.1. For degree2 it gives a dimension-free coefficientℓ_(4/3) bound. Because invertible character changes preserve coefficients, its largest-coefficient consequence supplies native influence≥c V³/W⁴ for the present broader class. It does not automatically give the exponent2. The cut proof uses more structure than this generic coefficient argument. The paper credits Blei for the existence of general Boolean coefficient bounds; that earlier original was not independently located here.

Historical references, metadata checked but full original proofs not read in this task: J. E. Littlewood, *On bounded bilinear forms in an infinite number of variables*, Quarterly Journal of Mathematics os-1(1),164–174(1930), DOI10.1093/qmath/os-1.1.164; H. F. Bohnenblust and Einar Hille, *On the Absolute Convergence of Dirichlet Series*, Annals of Mathematics(2)32(3),600–622(1931), DOI10.2307/1968255. These support historical context, not a direct claim that they state native tree-edge influences.

## Linear-transform influence literature is adjacent, not interchangeable

Nathan Keller and Haran Pilpel, *Linear transformations of monotone functions on the discrete cube*, Discrete Mathematics309(12),4210–4214(2009), DOI [Original source](https://doi.org/10.1016/j.disc.2008.12.018) . Author original dated17July2008: [Original source](https://u.math.biu.ac.il/~nkeller/keller-pilpel.pdf) . Directly checked abstract and Definitions1–2/introduction: invertible F₂ input changes and **total influence of monotone Boolean** functions.

Demetres Christofides, *Influences of monotone Boolean functions*, Discrete Mathematics310(8),1401–1402(2010), DOI [Original source](https://doi.org/10.1016/j.disc.2009.12.017) ; original arXiv:0909.5652v1,30September2009, [Original source](https://arxiv.org/pdf/0909.5652) . Its introduction defines directional influences and proves the Keller–Pilpel conjecture that total influence of a monotone Boolean function does not decrease under invertible linear changes. This is a genuine nearby published result but involves Boolean output, monotonicity and **total**, not maximum, influence. Neither source verifies the present bounded-real quadratic-support statement.

## Scope and claim status

For the native polynomial conclusion, the endpoint characters must be independent coordinates of a bijective character transformation, with the optional zero anchor. Distinct dependent labels suffice for the combinatorial cut lemma but fail the full-graph-range argument. Under arbitrary dependent labels one could represent a general polynomial by a star, and mistakenly derive dimension-free general AA. The checked theorem excludes this.

No general AA result or conjecture-status update follows. For the class at hand, the Hadamard family has V=1/m and I_max=V² under bounded range, so no uniform exponent<2 is possible. This proves the variance exponent is sharp **within the class**, not that constants12 or8 are sharp or that the exact consequence is a published new theorem.

Priority status suitable for a website: “Verified derived consequence; classical norm and fractional-assignment ingredients; exact earlier publication of the native influence formulation not located.” Keep an explicit checked date and the difference between source-stated, derived and not-yet-located claims.

## Search scope and limits

Queries covered “Aaronson Ambainis linear transformation”, “influence quadratic characters”, “Fourier influence graphic matroid”, “quadratic Fourier support influence”, “influences linear changes Boolean”, “influence tree paths Fourier”, “fractional orientation weighted Hakimi”, and density/endpoint assignment variants. Several broad queries returned irrelevant uses of arithmetic quadratic characters and were discarded. Checked primary targets were the works above, rather than counting those irrelevant retrievals as evidence. This is a finite literature pass, not an exhaustive search of all books, theses, preprints or equivalent Banach-space/matroid formulations. No author contact or private correspondence was undertaken.

## Additional original flow source checked for this publication

L. R. Ford, Jr. and D. R. Fulkerson, *Maximal Flow Through a Network*, Canadian Journal of Mathematics **8**, 399–404 (1956), DOI [10.4153/CJM-1956-045-5](https://doi.org/10.4153/CJM-1956-045-5). Theorem 1, printed p.400, was visually checked in the original six-page scan. Its historical formulation uses chain flows in a network. The atlas gives its own directed real-capacity argument using compactness and residual paths, so it does not silently substitute an algorithmic termination claim for the flow theorem. The weighted fractional-orientation LP in CHR25 Section 2, printed p.25:4, explicitly allows nonnegative allocations; Lemma 2 and Corollary 10 state the weighted density equivalence. These are checked established ingredients, not a priority claim for the native influence consequence.
