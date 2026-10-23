# Exact two-query certificate search: publication-priority and source audit

Checked 23 October 2026. This report audits prior sources and their models; it does **not** count the earlier mathematical proof review as a fresh proof audit. The [complete proof](exact-search-proof.md) and [fresh mathematical audit](exact-search-full-source-audit.md) are separate pages.

## Finding and recommended wording

I did not locate an original paper stating the precise implication

$$
Q_E(S)\le2\quad\Longrightarrow\quad D(S)\le2
$$

for **full-cube total certificate-output search** in the standard worst-case bit-query model. There is substantial earlier work on every ingredient and on the unweighted width-two partition special case. The appropriate label remains **derived research note; prior publication of this precise implication not located**. Neither “new” nor “first” is justified by these searches. Direct inquiry to authors familiar with fractional subcube partitions would still be useful before asserting novelty.

The important predecessor is not merely general quantum polynomial degree: the amplitude-factorization step, the passage to constant nonnegative weights for maximum-width outputs, and the singleton restriction/recovery must all be present to imply this exact statement. No original source located in this audit supplies that full chain.

## 1. The search model and current open problem

**Shalev Ben-David and Srijita Kundu.** *Separations in Query Complexity for Total Search Problems.* arXiv:2410.16245v1, submitted 21 October 2024, 47 pp. [Original source](https://arxiv.org/abs/2410.16245) ; full HTML [Original source](https://arxiv.org/html/2410.16245v1) . Checked the original full text, especially §2.1 and §1.3 Open Problem 1. The official arXiv entry currently lists v1 and no journal reference.

Their search outputs are partial assignments contained in the input. Their explicit distinction between certificate-output search and a general relation possessing short certificates matches the restriction in the research note. Open Problem 1 asks for an **asymptotic exponential** separation of exact quantum and randomized complexity, in either direction. The small-query rigidity theorem does not settle that problem. Nothing in these checked sections states the two-query classification.

This is already source BK24 in the catalogue; no duplicate bibliographic work should be created.

## 2. The original amplitude method

**Robert Beals, Harry Buhrman, Richard Cleve, Michele Mosca and Ronald de Wolf.** *Quantum lower bounds by polynomials.* Journal of the ACM **48**(4), 778–797 (July 2001), DOI [DOI](https://doi.org/10.1145/502090.502097) ; original preprint quant-ph/9802049, [Original source](https://arxiv.org/abs/quant-ph/9802049) . The amplitude-polynomial induction is the classical input to the derived note. Its usual scalar acceptance-probability consequence has degree at most twice the number of queries; that consequence alone does not imply D≤2 here. Vanishing on every point outside a certificate and the full-cube multilinear factorization supply the stronger necessary condition used in the note.

This audit relies on the source already captured in the atlas and the explicit reproof in the research note, rather than presenting the amplitude lemma as a new result. This is already the catalogue's original polynomial-method work; retain its existing source identity.

## 3. The closest subcube-partition predecessor, with version correction

**Yuval Filmus, Edward A. Hirsch, Sascha Kurz, Ferdinand Ihringer, Artur Riazanov, Alexander V. Smal and Marc Vinyals.** *Irreducible Subcube Partitions.* The Electronic Journal of Combinatorics **30**(3), #P3.29 (2023), 51 pp. Published 8 September 2023. DOI [DOI](https://doi.org/10.37236/11862) . Original final journal PDF: [Original source](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v30i3p29/pdf/) .

The final journal's **Lemma 53, p.28, §2.8.1**, rules out irreducible homogeneous codimension-two subcube partitions. Corollary 51 supplies its parity proof. These are **unweighted disjoint partitions**. They establish a genuinely relevant predecessor but do not, as written, treat overlapping nonnegative weighted covers or quantum certificate-output algorithms. Applying this lemma to arbitrary positive weights requires an additional argument; clearing denominators does not turn overlaps into disjoint pieces while retaining the same width.

Version map, verified from the original PDFs:

| Version | Date / pagination | Width-two locator |
|---|---|---|
| Final EJC journal | 2023; 51 pp. | Lemma 53, p.28 |
| arXiv:2212.14685v3 | 18 August 2023; 39 pp. | Lemma 2.48, p.22 |
| arXiv:2212.14685v4 | 8 September 2026; 37 pp. | Lemma 2.47, p.23 |

The current arXiv version is v4: [Original source](https://arxiv.org/abs/2212.14685) . Its latest changes address counterexamples to two maximal-size/point-count conjectures. The width-two result is unchanged. Neither `fractional` nor `quantum` occurs in its full HTML. Those keyword checks supplement inspection of the relevant section; they are not an exhaustive semantic proof of absence. Older mirrors have different lemma numbering and should not be cited interchangeably with the final journal or current v4.

## 4. Earlier hitting-clause-set route

**Oliver Kullmann and Xishun Zhao.** *Unsatisfiable hitting clause-sets with three more clauses than variables.* arXiv:1604.01288v1 [cs.DM], 5 April 2016, 17 pp. [Original source](https://arxiv.org/abs/1604.01288) ; original PDF [Original source](https://arxiv.org/pdf/1604.01288v1) . No journal reference or subsequent arXiv version was found in the official record.

Checked §3 and §5.2 in the original PDF. **Corollary 17, p.7**, classifies the failure of full-subsumption resolution for unsatisfiable hitting clause-sets with at most five clauses. **Lemma 41, p.12**, identifies the sole irreducible deficiency-two example up to isomorphism. The final EJC proof explicitly cites Lemma 41 as an alternative route for its three-variable residual case. These are disjoint unweighted tautology/partition structures. They are historical predecessors of the width-two partition observation, not an identified publication of its overlapping weighted extension or the quantum statement.

## 5. Weighted/normalized partition literature

**Rahul Jain and Hartmut Klauck.** *The Partition Bound for Classical Communication Complexity and Query Complexity.* In *25th Annual IEEE Conference on Computational Complexity (CCC 2010)*, pp.247–258. IEEE, 2010. DOI [DOI](https://doi.org/10.1109/CCC.2010.31) . Full version arXiv:0910.4266v2 [cs.CC], 19 November 2009, 28 pp., [Original source](https://arxiv.org/pdf/0910.4266v2) .

Checked the full version's **Definition 15, p.18, §3.1.1**, and, more directly, **Definition 22, p.25, §3.4**, for relations. Its primal LP includes nonnegative weighted subcubes and pointwise normalization. This is a direct original source for the surrounding fractional-partition formalism. Its objective sums weights times 2^{width}; it is **not** a hard maximum-width cutoff. The checked statements do not classify the width-at-most-two feasible cone or imply Q_E≤2⇒D≤2. The relation formulation is more appropriate background here than citing only the scalar-function LP.

**Robin Kothari, David Racicot-Desloges and Miklos Santha.** *Separating Decision Tree Complexity from Subcube Partition Complexity.* In *APPROX/RANDOM 2015*, LIPIcs **40**, pp.915–930, Schloss Dagstuhl, 2015. DOI [DOI](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2015.915) . Full published conference PDF [Original source](https://drops.dagstuhl.de/storage/00lipics/lipics-vol040-approx-random2015/LIPIcs.APPROX-RANDOM.2015.915/LIPIcs.APPROX-RANDOM.2015.915.pdf) ; preprint arXiv:1504.01339. No separate journal version was located.

Checked §§2.2–2.3, pp.920–922, and Proposition 13, p.923. Randomized subcube partitions there are distributions over **disjoint** deterministic partitions; the ordinary partition LP is a relaxation. The width-three partition of 4-MAJ already differs from a decision tree. None of these checked statements identifies arbitrary weighted width-two covers with depth-two trees or studies exact quantum certificate outputs. The width-three example is relevant motivation for why a width-two proof does not extend automatically.

**Mika Göös and T. S. Jayram.** *A Composition Theorem for Conical Juntas.* In *31st Conference on Computational Complexity (CCC 2016)*, LIPIcs **50**, pp.5:1–5:16, Schloss Dagstuhl, 2016. DOI [DOI](https://doi.org/10.4230/LIPIcs.CCC.2016.5) . Earlier original full report ECCC TR15-167, 15 October 2015, [Original source](https://eccc.weizmann.ac.il/report/2015/167/download/) .

Checked the original report, particularly its opening “Related models” paragraph (article p.1; PDF p.2), definitions and theorem list. It explicitly links conical juntas to partition bounds, query complexity in expectation, randomized subcube partitions and unambiguous DNFs. It is valuable terminology/priority context for the classical nonnegative-combination mechanism. I did not find the precise width-two support-extraction lemma or the certificate-output quantum theorem there. Its main result is a composition lower-bound method, not a small-width classification.

## 6. Exact two-query Boolean-function classification is a different target

**Shaoliang Ye, Wei Yang and Liusheng Huang.** *Characterization of exact two-query quantum algorithms.* Information and Computation **298** (June 2024), article 105166. DOI [DOI](https://doi.org/10.1016/j.ic.2024.105166) . Original publisher preview: [Original source](https://www.sciencedirect.com/science/article/pii/S0890540124000312) .

The publisher's abstract and introduction were accessible and checked; I did **not** obtain or audit the paywalled full text. They study scalar-output total Boolean functions. Their announced classification is conditional on numerical four-bit classification results and includes many functions with Q_E=2 and D>2. This does not contradict the note: outputting f(x) differs from returning an input partial assignment certifying an output. Conversely this Boolean-function classification does not establish the certificate-output theorem. No full-text or unconditional-classification claim should be made on this audit's evidence.

## 7. A useful precise relationship to the earlier formalism

The classical lemma proved in the note concerns a nonnegative identity

$$
\sum_{|c|\le2}w_c\mathbf1_c=1.
$$

It extracts a depth-two tree using allowed positive-support certificates. This can be understood as a hard-width-two special case of normalized fractional-subcube formalisms, with additional provenance requirements for output labels. The note then adds the quantum amplitude restriction and the singleton fallback to reach its theorem. A citation to the partition LP should explain this relationship rather than suggest that the existing LP theorem already supplies the needed exact extraction.

A stronger convex-decomposition statement for arbitrary width-two normalized covers might follow by tracking every row/column contribution, but it is not required for the theorem. Neither its novelty nor its prior publication was established here; do not introduce it into the website as a historical fact.

## 8. Search record, limits and source hashes

Queries included exact/two-query/certificate-output search, fractional or weighted subcube partitions, width/codimension two partitions, conical-junta degree two, and the cited original titles. The search traversed the EJC bibliography to the Kullmann–Zhao original source and the conical-junta bibliography to Jain–Klauck and Kothari–Racicot-Desloges–Santha. No exact predecessor of the complete quantum implication was retrieved. Non-indexed discussions, theses and all citation descendants were not exhaustively examined. General exact Grover search with a unique marked item is promised-input oracle identification and cannot serve as a full-cube counterexample.

PDFs and page-separated extracted texts are private working captures in `work/exact-search-priority-sources/`; the accompanying `metadata.json` contains SHA-256 hashes and page counts for seven captures. Do not redistribute the complete sources in the public atlas. Full hashes:

| Capture | SHA-256 |
|---|---|
| FHKIRSV23 final | `53575b90c5c258a7f5e7bb467c32c5fb52ce3ad8e393774921a0fad6a127a5b3` |
| FHKIRSV23 v3 | `8fc45ebdf1748a8d4f8fc5e02c54d3bae16342ce4b303c6709bee7ac2c15687b` |
| FHKIRSV23 v4 | `351acde7c7f6fb3859dc9d86c04866fb3a27ece03730e6b3db35a46b33da7083` |
| KZ16 v1 | `f73bead90b9236326da51001159efb7e03adda96ca91a83428f5cb5090859b2f` |
| KRS15 published conference | `7e9e15bbb6231fa5c8a596939f642fcb1f51ae94e63ee5a697f86167d9197bf6` |
| JK10 full v2 | `af7e9e8994d2bc06f07f096489e3677cf7d7f74d3b36935ce2a9fad85c97fc79` |
| GJ16 earlier ECCC report | `47cef694b0e4efaee4c243564f21203f9489f284bda17831424ae6dada607d74` |

For a minimal public bibliography update, the closest new entries are FHKIRSV23, KZ16 and the normalized weighted-partition source JK10. KRS15/GJ16 provide additional historical context; reuse existing source identities if already indexed. The Ye–Yang–Huang entry is useful chiefly to explain the model distinction and should carry the preview-only and conditional-result qualifications.
