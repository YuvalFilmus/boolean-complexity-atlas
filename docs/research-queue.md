# Conjectures and research queue

Historical conjectures are preserved. “Current status unverified” means precisely that; it does not mean open.

## sensitivity-polynomial

bs(f) <= poly(s(f)) for all total Boolean functions

Status: resolved.

Source: [HKP11](https://tocmirror.cs.uchicago.edu/articles/gs004/), Central sensitivity conjecture.

- The recorded Huang and Nisan–Szegedy bounds give bs(f) <= 2 s(f)^4.
- Later constant improvements are recorded separately (bs-deg2-Tal, bs-deg2-Pro, and the Wellens bound); the displayed historical consequence is not the sharpest coefficient.

Resolution records: bs-s4.

## D-bs-quadratic

D(f) = O(bs(f)^2)

Status: historical_conjecture_current_status_unverified.

Source: [ABKBRT21](https://arxiv.org/abs/2010.12629), Conjecture 1.

- Would imply D=O(R^2) using bs=O(R).
- Would imply D=O(adeg^4) using bs=O(adeg^2).

## R-Q-cubic

R(f) = O(Q(f)^3)

Status: reported_refuted_in_primary_preprint.

Source: [ABKBRT21](https://arxiv.org/abs/2010.12629), Conjecture 2.

- A near-quartic separation would refute this.

Resolution records: R-Q4-sep-2026.

## rational-polynomial

deg(f) <= poly(rdeg(f)) for total Boolean functions

Status: resolved_in_primary_paper.

Source: [IJKKSWW23](https://arxiv.org/abs/2310.08004), Introduction / abstract.

- Would relate exact rational representations to the usual total-function polynomial cluster.

Resolution records: deg-rdeg3.

## bs-lambda-quadratic

bs(f)=O(lambda(f)^2) for all total Boolean f

Status: reported_refuted_in_primary_preprint.

Source: [ABKBRT21](https://arxiv.org/abs/2010.12629), Open problems / spectral sensitivity questions.

- The spectral variant is distinct from the still stronger sensitivity question bs=O(s^2); refuting it does not refute that sensitivity conjecture.

Resolution records: bs-lambda-sep-2026.

## Saks-Wigderson-maximal-speedup

In the source’s zero-error convention, R(f)>=Omega(D(f)^log_2((1+sqrt(33))/4)) for all total Boolean f.

Status: refuted.

Source: [SW86](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/SW86/SW86.pdf), Conjecture 1.6, p.31.

- Would make balanced NAND trees extremal for randomized speedup. Pointer functions in ABBLS17 refute this historical conjecture.

Resolution records: D-R0-sep-ABB.

## extremal-forrelation-sqrt

The randomized complexity of Extremal Forrelation is tildeOmega(2^(n/2)).

Status: conjectured_in_inspected_2026_source_current_status_unverified.

Source: [GS26](https://doi.org/10.4230/LIPIcs.ITCS.2026.72), Conjecture 6.

- Would improve the proven tildeOmega(2^(n/4)) lower bound. The paper reports a 2^(n/4+o(n)) distinguisher for its own two hard distributions, so new distributions are needed.
- CCM26 v2 proves a near-half-exponent NONADAPTIVE lower bound. It does not resolve this adaptive conjecture. Appendix D explains a gap in the stronger v1 claim.

## extremal-k-forrelation

For k>2, the randomized complexity of extremal k-Forrelation is tildeOmega(2^(n*(1-1/k))).

Status: conjectured_in_inspected_2026_source_current_status_unverified.

Source: [GS26](https://doi.org/10.4230/LIPIcs.ITCS.2026.72), Conjecture 7.

- Would approach the best bounded-error quantum/classical separations using exact quantum algorithms.

## BK24-search-QE-R

Can a total search problem have an exponential QE/R separation in either direction?

Status: open_question_as_of_inspected_2024_source_current_status_unverified.

Source: [BK24](https://arxiv.org/abs/2410.16245), Section 1.3, Open Problem 1.

- The 2024 paper does not establish exact-query separations; its Q and bounded-polynomial constructions alone do not answer this.

## BK24-search-poly-conical

Can total search exponentially separate bounded approximate polynomial degree from bounded approximate nonnegative degree? What about exact degree versus approximate degree?

Status: open_question_as_of_inspected_2024_source_current_status_unverified.

Source: [BK24](https://arxiv.org/abs/2410.16245), Section 1.3, Open Problem 2.

- Uses relation polynomial systems, not the ordinary unrestricted polynomial of a Boolean function.

## BK24-search-Adv-degree

Does Adv(S)=O(rel_adeg(S)^2) hold for total search? Can Adv be exponentially larger than rel_adeg?

Status: open_question_as_of_inspected_2024_source_current_status_unverified.

Source: [BK24](https://arxiv.org/abs/2410.16245), Section 1.3, Open Problem 3.

- Do not extend the partial decision-function theorem ABK21 to relations automatically. BK24 supplies an exponential separation in the opposite direction.

## KLMY-randomized-AND-derandomization

DandPos(f)<=poly(RandPos(f),log n) for total Boolean functions.

Status: resolved_as_stated_by_2023.

Source: [KLMY21survey](https://cseweb.ucsd.edu/~shmcguir/papers/KLMYsigact.pdf), Conjecture 3.16.

- CDMRS23 Theorem 4.5 gives DandPos=O(RandPos^3 log^4 n). Input-length logarithms remain essential: and-threshold-no-pure-power shows that a pure RandPos power cannot hold.

Resolution records: and-D-R3.

## KLMY-monomial-approximation

Exact 0/1 monomial sparsity is polynomially bounded by approximate 0/1 monomial sparsity for total Boolean functions.

Status: refuted_as_literally_stated.

Source: [KLMY21survey](https://cseweb.ucsd.edu/~shmcguir/papers/KLMYsigact.pdf), Conjecture 3.19 and Claim 3.20.

- The literal absolute-sparsity statement in Conjecture 3.19 is false. Sparse25 Remark 1.2 gives OR and near-top threshold counterexamples. The later positive result concerns logarithms and includes log n; it must not be recorded as a proof of the literal conjecture.

Resolution records: monomial-sparsity-no-pure-approx-power.

## KLMY-pure-monomial-AND

DandPos(f)<=poly(log(2+monomialSparsity(f))) for total Boolean functions, eliminating input-length dependence.

Status: conjectured_in_inspected_2020_preprint_current_status_unverified.

Source: [KLMY21](https://doi.org/10.1145/3406325.3450999), Conjecture 6.1.

- Theorem 1.2 establishes O(log^5(2+spar)*log(2n)); the conjecture would eliminate its input-length logarithm. Do not confuse this with polynomial derandomization allowing log n factors.

## Wellens-relevant-sensitivity

For every total Boolean function, nRelevant(f)=O(4^s(f)). The source also conjectures a stronger bounded coordinate-sensitivity potential.

Status: conjectured_in_2022_source_current_status_unverified.

Source: [Wel22](https://arxiv.org/abs/2005.00566v2), Conjecture 3.17.

- Would remove the factor s from Simon’s bound. Monotone address functions show the exponential base 4 cannot be improved uniformly. The stronger potential requires its own definition; it is not entered as an additional scalar theorem.

## HKMP-natural-perturbation

Characterize polynomial approximate-degree natural completions by perturbing Fourier coefficients, allowing basis terms up to polynomial degree.

Status: formulation_or_current_resolution_unverified.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Conjecture 72.

- The exact support, coefficient norm and sign-preservation constraints need clarification. Without constraints, every target polynomial in the enlarged basis is a coefficient perturbation, so that literal formulation is a representation identity. Lemma 71 does not currently provide a verified normalization route.

## HKMP-dense-almost-completion

If Dom(f) has density at least epsilon and bounded approximate degree d, can one discard a delta fraction of the promise and extend the remainder to a total function with approximate degree poly(d,1/epsilon,1/delta)?

Status: formulation_or_current_resolution_unverified.

Source: [HKMP26](https://arxiv.org/abs/2603.29256), Conjecture 78.

- The extension is of a subfunction, not necessarily of f on its whole domain. It is a polynomial-degree analogue of the average-case simulation question recalled as Conjecture 77.

## domain-robust-low-degree

A Boolean function on S_n close in uniform squared L2 to degree d should be close to a Boolean function computable by a decision tree of polynomial depth in d; perhaps to a Boolean degree-d function. A corresponding question is proposed for perfect matchings.

Status: still_proposed_in_2026_journal_current_resolution_unverified.

Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Section 9, Robust versions.

- A robustness conjecture, not a consequence of exact low-degree polynomial equivalence. The source gives no explicit uniform error modulus for the full conjecture.

## domain-q-analog-framework

Can the polynomial-equivalence framework be extended to Grassmann, bilinear and general linear group domains, or can nontrivial counterexamples be found?

Status: still_proposed_in_2026_journal_current_resolution_unverified.

Source: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Section 9, q-analogs.

- A research direction rather than a proved scalar exponent comparison; query models and domain constants must be specified.

## AA-folklore-average-simulation

A T-query quantum acceptance probability can be approximated within epsilon on at least 1-delta of uniform inputs by a deterministic classical tree of depth poly(T,1/epsilon,1/delta).

Status: conjectured_in_original_and_recalled_in_2026_primary_source_no_resolution_verified.

Source: [AA14](https://theoryofcomputing.org/articles/v010a006/), Conjecture 1.5 and Appendix Conjecture 7.1.

- The paper explicitly calls this folklore. Appendix 7 gives the equivalent dense-promise formulation. HKMP26 Conjecture 77 recalls that formulation; do not label the influence conjecture equivalent to it without a converse proof.

## AA-bounded-polynomial-influence

Every full-cube [0,1]-bounded degree-d polynomial with uniform variance at least v has a coordinate influence at least (v/d)^O(1).

Status: conjectured_in_original_and_recalled_in_2026_primary_source_no_resolution_verified.

Source: [AA14](https://theoryofcomputing.org/articles/v010a006/), Conjecture 1.7; Theorem 1.8.

- This implies the folklore simulation conjecture. GMNR26 restates it as Conjecture 4.2 and proves equivalence of its uniform, fixed-bias product and fixed-density slice analogues, not its truth.

## FLLV20-hypergraphical-sensitivity-question

Historical question: extend sensitivity theorems to hypergraphical analogues of the symmetric group and perfect matching scheme.

Status: historical_question_precise_exponent_and_current_literature_status_unverified.

Source: [FLLV20notes](https://yuvalfilmus.cs.technion.ac.il/Talks/ComplexityMeasures-HUJI.pdf), Section 7, p.7.

- Separate coarse polynomial equivalence for fixed hyperedge size from a direct quadratic intrinsic degree/sensitivity theorem or a witnessing framework.
- The separately audited repository query lift gives coarse parameterized polynomial bounds on full lambda-partite hypermatching domains; no published priority or resolution of every intended formulation is claimed.

## Queue: quartic-RQ-2026

Primary PDF, pinned commit, theorem and proof route inspected and recorded. Remaining: independent full-proof audit, subsequent corrections and publication tracking.

Status: source_extracted_followup_audit_needed.

[Primary source](https://github.com/openai/math/blob/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf)

## Queue: search-definitions

Extract every relation polynomial definition, all theorem parameters, and exact proof summaries. Relation degree cannot inherit the decision-function definition.

Status: source_extracted_followup_audit_needed.

## Queue: certification-2026

Certification transform, eighteen instantiated measures and main comparisons extracted. Remaining: every parameterized variant, complete proof audit and original attribution chain.

Status: source_extracted_followup_audit_needed.

## Queue: games

Private/public/entangled/nonsignaling and single-bit variants extracted. Remaining: source-wide alias audit, partial-certificate conventions and every separating example.

Status: source_extracted_followup_audit_needed.

## Queue: new-block-measures

Block/brick definitions and sensitivity counting bounds extracted. Remaining: all DNF/tree-size applications and cross-version notation.

Status: source_extracted_followup_audit_needed.

## Queue: expectation

Expectation-model definitions and literal-degree/SOS exact characterizations extracted. Remaining: Boolean-output sharper comparisons and all auxiliary polynomial variants.

Status: source_extracted_followup_audit_needed.

## Queue: noisy

Separate negligent, dephasing, hybrid, and time-dependent models and extract multivariate tradeoffs.

Status: source_extracted_followup_audit_needed.

## Queue: core-table-completion

Total core has 132 evidence chains. Promise core has all 132 cells classified: 49 matched finite power exponents and 83 non-polynomial pairs, using weak certificates and unrestricted promise degrees. Complete search, globally bounded polynomial, other-measure and priority coverage remains pending.

Status: total_and_promise_core_grids_filled_other_models_incomplete.

## Queue: notation-completion

Historical core aliases and source clashes extracted; unsupported seed attributions repaired. Finish candidate occurrences and expand beyond the checked-source inventory. CDM23 input-directed s_b/bs_b, GIPS search notation, and nonadaptive/restricted-query conventions are now extracted; output-conditioned s_b/bs_b remain separate.

Status: core_historical_occurrences_extracted_inventory_incomplete.

## Queue: search-model-survey

Read Query Complexity of Search Problems; reconcile cubic/quartic pseudo-deterministic statements with later formulations and their output conventions.

Status: source_extracted_followup_audit_needed.

[Primary source](https://drops.dagstuhl.de/storage/00lipics/lipics-vol272-mfcs2023/LIPIcs.MFCS.2023.34/LIPIcs.MFCS.2023.34.pdf)

## Queue: additional-polynomial-measures

Add finite-field/modular degree, threshold/sign degree, approximate rational degree, postselection complexity, one-sided/nonnegative/SOS/block-multilinear/completely-bounded degrees, query lower-bound LPs and partition measures, with explicit definitions before relations.

Status: pending.

## Queue: restricted-classes

Add monotone, transitive, symmetric, graph properties, read-once formulas, composition families, and distributional/average-case restrictions; restrictions are intersected, not unioned.

Status: pending.

## Queue: bibliography-completion

Publication metadata and original sources added for size/AND queries and quantum tree simulation (CDMRS23, KLMY21, LM19, LL16, BT20, CMP22), plus KLMY21survey and ZPP26. EH89 bibliography and attribution are complete but its original full proof is uninspected; Nis91 original-source access gap also remains.

Status: 87_versioned_references_original_text_gaps_remain.

## Queue: rational-degree-version-discrepancy

Version-specific authors and bounds recorded under KKWY26. v1 quartic, v2/v3 cubic with logarithmic loss; retain both historical conjecture and resolution provenance.

Status: reconciled.

## Queue: monotone-variants

Extract mbs, fmbs, MCC, monotone sensitivity, and their names/notations. These variants are not the ordinary measures restricted to monotone functions.

Status: source_extracted_followup_audit_needed.

## Queue: rank-size-and-instance

Extract decision-tree rank, size, conjunctive depth, and sparsity bounds; then process LM26 for instance complexity.

Status: source_extracted_followup_audit_needed.

## Queue: hazard-free

Extend scope schema to ternary inputs/outputs and add hazard-free measures. Do not put hazard-free upper bounds in Boolean-function rows.

Status: source_extracted_followup_audit_needed.

## Queue: search-frontier-completion

Six scope-separated search evidence matrices generated; finish unindexed comparisons, exact/zero-error search, full relation degree/conical gaps and forward-citation checks on BK24 questions. Do not declare its 2024 questions open today.

Status: partially_extracted_not_exhaustive.

## Queue: search-size-and-distribution-completion

Closed the final-version ApproxMaj/canonical-size, unlifted CNF, AND/OR, strong average-cost and quantum-size error-convention gaps. Remaining: complete exact/zero-error search frontiers, optimal size endpoints and error-dependent comparisons; original EH89 proof and complete attribution chains still pending.

Status: final_MFCS_size_ANDOR_and_GIPS_average_results_extracted.

## Queue: partial-noncore-completion

Extend the complete core promise grid to globally bounded polynomial degrees, strong certificates, adversary and error/local variants; complete original-priority and historical-name inventories.

Status: core_finished_extended_inventory_incomplete.

## Queue: general-search-error-reduction

Q_{2/5} relation simulation kept separate from default Q_{1/3}. Inventory error-dependent search measures and reductions with verification or canonical output; do not assume Boolean majority amplification for relations.

Status: identified_and_guarded_further_audit_pending.

## Queue: strong-average-cost-observations

GIPS21 Theorems 26–29 and Proposition 25 extracted. Strict finite nonuniform Las Vegas averages admit fixed-coins equality, and dense Find1 admits a distribution-dependent deterministic scan of mean cost below two. These are explicitly repository derivations, not first-priority claims; retain distinctions from failure-flagged caps and uniform algorithms.

Status: source_extracted_repository_sharpenings_explicit.

## Queue: new-domain-and-completion-extraction

Extract promised sensitivity/bs, critical certificates and minimum-over-completions measures with all bounds; audit HKMP26 Conjectures 72,77,78. Complete DFLLV21 general-domain parameter matrix, perfect matching/multislice definitions and journal-version check; follow 2025/2026 Hamming-graph relevant-variable papers.

Status: source_extracted_followup_audit_needed.
