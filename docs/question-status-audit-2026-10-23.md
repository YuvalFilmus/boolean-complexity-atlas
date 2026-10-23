# Literature-status audit of the Open Questions tab

Checked 23 October 2026. All 15 active published-question candidates were examined. No complete resolution of any of those 15 was established by this audit. This is distinct from certifying that all 15 are open: six are explicitly still posed in checked recent primary sources, seven have only a bounded search finding no resolution, and two retain formulation issues. The eight previously resolved/refuted formulations remain archived. Inferred exponent-table gaps were not subjected to individual literature-openness certification.

## Findings and source limits

| Question | Audit outcome | Checked evidence |
|---|---|---|
| D-bs-quadratic | no resolution found | [ABKBRT21](https://arxiv.org/abs/2010.12629) Conjecture 1; [CPS23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2023.27) Question 1 and Theorems 4–5 |
| extremal-forrelation-sqrt | primary reaffirmed open | [GS26](https://doi.org/10.4230/LIPIcs.ITCS.2026.72) Conjecture 6, Section 1.3; [CCM26](https://arxiv.org/abs/2602.07503v2) v2 Theorems 1/3, Appendix B.4, Appendix D |
| extremal-k-forrelation | no resolution found | [GS26](https://doi.org/10.4230/LIPIcs.ITCS.2026.72) Conjecture 7, Section 1.3; [CCM26](https://arxiv.org/abs/2602.07503v2) v2 Introduction and Theorem 3 |
| BK24-search-QE-R | no resolution found | [BK24](https://arxiv.org/abs/2410.16245) Section 1.3, Open Problem 1, PDF pp.8–9 |
| BK24-search-poly-conical | no resolution found | [BK24](https://arxiv.org/abs/2410.16245) Section 1.3, Open Problem 2, PDF pp.8–9 |
| BK24-search-Adv-degree | no resolution found | [BK24](https://arxiv.org/abs/2410.16245) Section 1.3, Open Problem 3, PDF pp.8–9 |
| KLMY-pure-monomial-AND | no resolution found | [KLMY21](https://doi.org/10.1145/3406325.3450999) Conjecture 6.1; [KLMY21survey](https://cseweb.ucsd.edu/~shmcguir/papers/KLMYsigact.pdf) Conjecture 3.13 and Theorem 3.11; [BBCLD26](https://arxiv.org/abs/2606.03249v1) Section 1.1, PDF pp.3–5; [NPS26](https://arxiv.org/abs/2602.01042v2) Sections 3–4 |
| Wellens-relevant-sensitivity | no resolution found | [Wel22](https://arxiv.org/abs/2005.00566v2) Conjecture 3.17; discussion near end of paper |
| HKMP-natural-perturbation | formulation unresolved | [HKMP26](https://arxiv.org/abs/2603.29256) v3 Conjecture 72 and Lemma 71 |
| HKMP-dense-almost-completion | primary reaffirmed open | [HKMP26](https://arxiv.org/abs/2603.29256) v3 Conjectures 77–78, manuscript p.36 |
| domain-robust-low-degree | primary reaffirmed open | [DFLLV26](https://doi.org/10.5070/C6.68665) Section 8, article pp.48–49; [FLM26](https://arxiv.org/abs/2608.11320v1) Theorems 1.2–1.3 |
| domain-q-analog-framework | primary reaffirmed open | [DFLLV26](https://doi.org/10.5070/C6.68665) Section 8, q-analogs, article p.49; [FLM26](https://arxiv.org/abs/2608.11320v1) Introduction and Theorem 1.3 |
| AA-folklore-average-simulation | primary reaffirmed open | [LMparallel26](https://arxiv.org/abs/2608.20297v2) Conjecture 1.1, Theorems 1.6–1.8, PDF pp.3,7–8; [GMNR26](https://arxiv.org/abs/2609.35327) Introduction and Theorem 1.1; [BSW22](https://arxiv.org/abs/2203.00212v1) Conjecture 1.1 and Section 4; [HKMP26](https://arxiv.org/abs/2603.29256) Conjecture 77 |
| AA-bounded-polynomial-influence | primary reaffirmed open | [LMparallel26](https://arxiv.org/abs/2608.20297v2) Introduction, PDF p.4; [GMNR26](https://arxiv.org/abs/2609.35327) Conjecture 4.2 and Theorem 4.3; [BSW22](https://arxiv.org/abs/2203.00212v1) Conjecture 1.2 and Theorem 1.3; [Bha26](https://eccc.weizmann.ac.il/report/2024/035/revision/2/) Conjecture 1.3 and main result |
| FLLV20-hypergraphical-sensitivity-question | formulation unresolved | [FLLV20notes](https://yuvalfilmus.cs.technion.ac.il/Talks/ComplexityMeasures-HUJI.pdf) Section 7, p.7; [DFLLV26](https://doi.org/10.5070/C6.68665) Section 8 and query-domain framework |

## Recurring questions

The following distinct-work counts are passage-level lower counts in the indexed literature. A later paper must discuss the same question, or an explicitly justified equivalent formulation; a related theorem or a citation alone does not qualify. Preprint and journal/proceedings versions count once.

- **Folklore average-case simulation: five works** — AA14, BSW22 Conjecture 1.1, HKMP26 Conjecture 77, GMNR26 and LMparallel26 Conjecture 1.1. The dense-promise version is an equivalent formulation, not the polynomial influence conjecture.
- **Bounded-polynomial influence: five works** — AA14 Conjecture 1.7, BSW22 Conjecture 1.2, Bha26 Conjecture 1.3, GMNR26 Conjecture 4.2 and LMparallel26 Introduction p.4. The random-restriction paper’s mean-square simulation discussion is not separately counted as a literal deterministic simulation formulation.
- **Quadratic D versus block sensitivity: two works** — ABKBRT21 Conjecture 1 and CPS23 Question 1/discussion. CPS22 and CPS23 are versions of one work, not two occurrences.
- **Adaptive Extremal Forrelation: two works** — GS26 Conjecture 6 and CCM26 v2 Introduction/Appendix B.4. The stronger old v1 claim is not used.
- **Dimension-free AND-query depth versus log sparsity: two works** — KLMY21 Conjecture 6.1 and KLMY21survey Conjecture 3.13. The latter uses rank of the AND-composed communication matrix, equal to the ordinary 0/1 monomial sparsity. The related lifting Conjecture 3.14 is not counted as a second occurrence.

The final DFLLV26 open questions were added as explicit additional passages, but they are versions of DFLLV22author and do not increase the distinct-paper recurrence count. FLM26 is adjacent progress rather than a recurrence of a full complexity-equivalence conjecture.

## Important distinctions

Liu–Mutreja v2 (20 October 2026) states deterministic simulation for parallel queries (Theorem 1.6), limited preprocessing before a parallel stage (Theorem 1.7), and fixed adaptive layer count (Theorem 1.8). The latter has an exponent growing exponentially with the layer count and does not settle unrestricted adaptivity. The proof route uses dense-to-uniform coupling and hybrid arguments, followed by distinct preprocessing and layer-induction extensions. Selected theorem statements, scope and the stated proof route were checked; this audit does not independently verify all 58 pages.

BSW22 proves the influence conjecture for completely bounded block-multilinear forms, using a noncommutative root-influence inequality. Bha26 (original ECCC report 2024; revision 2 in March 2026) proves a random-restriction result under variance hypotheses. Neither removes the restrictions in the general real-polynomial conjecture. Both the polynomial conjecture and the algorithmic simulation question remain explicitly open in the checked recent sources.

CCM26 v2 is nonadaptive. Appendix D describes the gap in v1, while Appendix B.4 distinguishes an adaptive algorithm for its particular hard distribution from the general adaptive Extremal Forrelation conjecture. No claim that the latter has been resolved is made here. The k>2 extremal conjecture remains a separate question with no new resolution found.

BBCLD26 establishes a quantum/deterministic **communication** relation for AND-functions with polylogarithmic input-length factors. Its Section 1.1 retains log n in the underlying sparsity comparison. It does not prove the dimension-free **query** conjecture. NPS26 addresses hardness condensation, another distinct question. These related results are recorded as related evidence, not counted as repeated formulations of the exact dimension-free conjecture.

The 2026 Grassmann FKN theorem gives degree-one robust structure. It is not an arbitrary-degree symmetric-group robustness theorem and does not supply a general query-model equivalence on Grassmann, bilinear and general linear group domains. The final DFLLV26 Section 8 explicitly preserves those open directions.

The HKMP v3 Conjecture 78 concerns completion of a subfunction after discarding a delta fraction of the promise. Conjecture 72 retains a different issue: an intended nontrivial perturbation characterization needs exact support, norm, fixed-target and margin quantifiers. Unrestricted coefficient subtraction alone is a representation equivalence. The prior dependent-support normalization gap is not repaired by this audit.

## Reproducibility

data/question-status-audit.json stores all 15 verdicts, source locators, search queries, limitations and current-version metadata hashes. New PDF snapshots have SHA-256 records in data/source-snapshots.json; source PDFs are not redistributed. Original catalogue statuses are retained in each updated question’s status_history. A checked date is not an exhaustive absence-of-resolution proof. Recent papers were examined as primary sources; search snippets and aggregator status labels were not used as mathematical authority.

The site exposes the verdict and its scope on every published-question card. Centrality also counts explicitly annotated measure mentions in checked question passages, with the source and locator exposed in the evidence list. No combined importance score is introduced.

The published random-restriction paper is also indexed as Bha25, *Random Restrictions of Bounded Low Degree Polynomials Are Juntas*, ITCS 2025, DOI 10.4230/LIPIcs.ITCS.2025.17. Its Conjecture 4 and Theorems 5/30 correspond to the revised report. The changed title and newer report revision do not create a sixth distinct-paper occurrence.

## Follow-up: seven negative searches and two formulation issues

A second pass on 23 October checked the seven negative-search entries again. None has a verified new resolution. These remain bounded negative findings, not certifications of current openness. Every affected website card now exposes its precise model/direction and the nearby result most likely to be confused with a resolution.

Two primary references were added, with source hashes and full bibliography entries:

- Ryan Anselm, Michelle Ding, Dar Gilboa and Sabee Grewal, *Optimal and Verifiable Quantum Advantages in Communication Complexity*, arXiv:2610.05585v1, 4 October 2026, 65 pp., [original manuscript](https://arxiv.org/abs/2610.05585v1). Theorem 1.1 and Section 1.1.1 imply one-query bounded-error versus linear randomized complexity for Pelagic Fourier Fishing. Fourier sampling hits the middle of squared Fourier mass with probability at least 3/4. A classical query to h=fg can be simulated by exchanging at most two bits, transferring the two-way communication lower bound. The lower-bound route uses entropy/coupling and a two-sided Gaussian window robust to independent shifts; a complete independent proof audit is not claimed. The exact quantum protocol in Theorem 1.3 is for a different communication relation, with fixed-degree polynomial classical cost. It does not answer BK24's exponential exact-query question.
- Parikshit Gopalan, Noam Nisan, Rocco A. Servedio, Kunal Talwar and Avi Wigderson, *Smooth Boolean Functions are Easy: Efficient Algorithms for Low-Sensitivity Functions*, ITCS 2016, pp.59–70, DOI [10.1145/2840728.2840738](https://doi.org/10.1145/2840728.2840738); [author proceedings PDF](https://www.cs.columbia.edu/~rocco/Public/GNSTW.pdf). Theorem 8 attributes n(f)<=s(f)4^{s(f)} to Simon. This is a historical reference for the starting bound, not another occurrence of Wellens' sharper later conjecture. The majority-neighborhood reconstruction results do not remove that prefactor.

Additional checked contextual references are attached to the question cards: BS21 for ordinary k-Forrelation, AGL26 for pseudo-deterministic search, Sparse25 for De Morgan sparsity, and BK24 Definitions 10–13 for bounded relation polynomial systems and positive adversary. They do not increase same-question recurrence counts: none was verified to restate these exact open targets. Preprint/proceedings versions continue to count once.

The seven outstanding targets are now displayed with their directions: unrestricted quadratic D versus bs; extremal k>2 Forrelation; exact quantum versus randomized total search in either direction; conical versus approximate relation degree and exact versus approximate relation degree; positive adversary above approximate relation degree; dimension-free AND-query depth versus ordinary monomial sparsity; and sensitivity-only relevant-variable bounds. They retain their existing verdicts.

### Perturbation: fixed completion, two degree scales, and a precise sufficient statement

[HKMP26 v3](https://arxiv.org/abs/2603.29256v3), Definition 59 (p.27), fixes F_p(x)=+1 if p(x)>=0 and -1 otherwise. “Without a degree blow-up” there uses native approximate degree a=adeg(f). Conjecture 72 (p.34) instead writes d=deg(p). To identify polynomial-in-d overhead with polynomial-in-a overhead, require d=poly(a), uniformly for the family.

A diagnostic family shows the distinction is substantive. Let the promise be product_{i=2}^n x_i=1, let f_n=x_1 on that promise, and choose p_n=product_{i=1}^n x_i. Then a_n=1, d_n=n, and the fixed natural completion is n-bit parity, of approximate degree n. Delta=0 is already a degree-d_n approximant to that completion. Both promised labels occur, so native degree cannot be zero. Parity's approximate-degree lower bound follows directly from orthogonality: every polynomial r of degree less than n has E[r chi_[n]]=0, whereas uniform error below one would force the expectation positive. Thus the arbitrary-p/native-degree reading fails; this does not refute an intended version requiring an optimal-degree p.

After fixing the same target F_p and tying d to native degree, the unrestricted enlarged-basis statement is a coordinate identity: if q approximates F_p, choose Delta=qhat-phat; conversely, p_Delta already is the approximant. An exact promise-kernel requirement is stronger and is not automatic. A kernel perturbation or promise-sign preservation establishes a completion of f, but does not identify its off-promise signs with F_p.

An explicit **editorial sufficient statement**, not an author conjecture, is: if q has degree t, full-cube norm at most K, full-cube margin at least gamma>0, and sign(q)=F_p everywhere, then adeg(F_p)=O(tK/gamma) at fixed error. Normalize by K and compose with a sign approximant. Uniform polynomial bounds on t and K/gamma in a give polynomial native-degree overhead. Bounding only coefficient infinity norm does not supply K. The unrestricted dependent-original-support normalization problem remains unverified. No source correction or general repair of Lemma 71 is claimed.

### Hypergraphical sensitivity: three distinct targets

The original [2020 notes](https://yuvalfilmus.cs.technion.ac.il/Talks/ComplexityMeasures-HUJI.pdf), Sections 1/3/7, motivate Huang-type bounds but leave the closing hypergraphical question unquantified. The site now labels the following as **editorial readings**, rather than retroactively attributing exact conjectures:

1. On all lambda-partite perfect hypermatchings, with fixed positive lambda_i and k=sum_i lambda_i, a vertex query reveals its entire hyperedge. The audited atlas product-permutation lift proves D<=10368(2k-1)^10 s^10. This settles that particular coarse, fixed-k polynomial comparison in the stated oracle model; its published priority remains unverified.
2. A direct intrinsic-degree inequality deg_H(f)<=C_lambda s(f)^2 is stronger. Neither that coarse lift nor the checked journal method proves this for the hypermatching domains.
3. Constants independent of lambda, or a direct witnessing framework, are additional requirements. The final DFLLV26 Section 5 opening states that its representation-theoretic technique does not capture hypergraphical perfect matching domains. This is a method limitation, not a counterexample to polynomial equivalence.

Changing the oracle, restricting the allowed hypermatchings, or allowing k to grow changes what is being asked. The historical entry keeps its formulation-review badge because the authors' exact intended quantitative target has not been established. The site does not silently replace it by either the coarse statement or the quadratic variant.

Source PDFs remain outside the repository. Only bibliography, source hashes, checked locators, summaries and the diagnostic argument are published. No exponent table was changed by this status follow-up.
