# Source priority and version audit

Specific reconciliations, not a complete first-attribution inventory. Source checks are statement/normalization/proof-route checks, not independent certification.

## classical-pseudodeterminism-cubic

Use CDM23 Theorem 3.2: D=O(psR^3) for total relations. AGL26 compares its quantum result to an older quartic classical theorem; that does not supersede the cubic bound. Original GGR13 Theorem 4.1(3) was now read directly; its quartic bound has no input-length logarithm. Treat the extra logarithm in AGL26’s discussion as a weaker summary, not part of the original theorem.

Sources: [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), [AGL26](https://doi.org/10.4230/LIPIcs.ICALP.2026.3), [GGR13](https://www.wisdom.weizmann.ac.il/~oded/p_balg.html). Status: original_statements_and_full_proof_route_checked.

## partial-bounded-degree-quantum

AB23 separates Q from exact degree bounded on the entire cube (Boolean degree O(log N)); BK24 separates Q even from bounded approximate degree and conical degree. Neither statement is an unrestricted promise-degree result in disguise.

Sources: [AB23](https://doi.org/10.4230/LIPIcs.CCC.2023.24), [BK24](https://arxiv.org/abs/2410.16245). Status: original_definitions_and_theorems_checked.

## classical-adversary-authors

Four-author STACS publication and five-author arXiv v3 are separate records. Theorems 9, 15 and 17 inspected here are the v3 locators.

Sources: [AKPV18](https://doi.org/10.4230/LIPIcs.STACS.2018.8), [AKPVZ18](https://arxiv.org/abs/1709.08985v3). Status: versions_separated.

## ABK21-published-constant-repair

Final CCC Lemma 27 repairs arXiv v1: q(x,i)=q_x(i). This closes the statement/proof factor discrepancy and supports CAdv<=cfbs with constant one. Lemma 26 supplies cfbs<=2 CAdv.

Sources: [ABK21](https://doi.org/10.4230/LIPIcs.CCC.2021.30). Status: preprint_and_final_proof_constructions_compared.

## CDM23-final-report-new-results

The final MFCS Theorems 4.5–4.6 and 5.5–5.7 contain the ApproxMaj completion lower bound, exponential canonical-size gap and AND/OR extensions absent from the inspected earlier ECCC report. Its Theorem 4.5 expressly credits the corruption argument to Swagato Sanyal.

Sources: [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/). Status: versions_compared_and_final_proof_read.

## CDMRS23-original-size-derandomization

Replaced secondary-only use of logarithmic size derandomization by the original STOC Theorem 3.1, and original AND/OR and AND-query bounds (Theorems 4.1 and 4.5). Proposition 2.11 attributes deterministic rank-size to Ehrenfeucht–Haussler; randomized extension is syntactic.

Sources: [CDMRS23](https://doi.org/10.1145/3564246.3585199), [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34). Status: original_theorems_and_proof_routes_checked.

## zero-answer-versus-zero-error

R^{0-dt} counts zero answers, while R0 is expected zero-error cost. HSC_0/FHSC_0 refer to input-zero sensitive blocks, not output-zero certificates. Registered as separate measures / qualified aliases.

Sources: [CDMRS23](https://doi.org/10.1145/3564246.3585199). Status: original_definitions_checked.

## CMP22-node-size-and-error

CMP22 DTSize/RDTSize count total nodes, unlike CDM23/CDMRS23 leaf size. Its randomized-relation simulation is Q_{2/5}, not default Q_{1/3}; Boolean majority reduction is only used in a decision-function record. Coupled rank/depth tree bounds are stored without multiplying separately minimized measures.

Sources: [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), [CDMRS23](https://doi.org/10.1145/3564246.3585199). Status: original_definitions_and_error_composition_checked.

## guessing-simulation-priority

LL16 supplies the original guessing-algorithm O(sqrt(TG)) simulation and bomb-query characterization. BT20 generalizes input/output alphabets and expected random-algorithm parameters using span programs and adversary SDPs. CMP22 identifies guessing complexity with Strahler rank and optimizes edge weights to obtain the sqrt(node-size) bound.

Sources: [LL16](https://theoryofcomputing.org/articles/v012a018/), [BT20](https://doi.org/10.22331/q-2020-03-02-241), [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15). Status: original_results_and_proof_routes_read.

## input-hitting-set-historical-clash

KLMY21 bare HSC/FHSC are input-directed and match MCC/fmbs. CDMRS23 bare HSC is ordinary certificate complexity and HSC_0/FHSC_0 are the directed variants. KLMY21 also uses P^{wedge-dt}/P^{0-dt}, where later papers use D. Its Claim 4.4 reproduces the zero-depth/conjunction proof and attributes it to Loff–Mukhopadhyay 2019; the original STACS Definitions 9–10 and Lemma 11 are now inspected. Its omitted proof is supplied by KLMY21.

Sources: [KLMY21](https://doi.org/10.1145/3406325.3450999), [CDMRS23](https://doi.org/10.1145/3564246.3585199), [LM19](https://doi.org/10.4230/LIPIcs.STACS.2019.50). Status: original_definitions_and_reproduced_proof_checked.

## monomial-versus-Fourier-sparsity

KLMY21 spar counts nonzero 0/1 monomials, whereas the parity-query survey uses Walsh Fourier sparsity. AND_n has monomial sparsity 1 and Fourier sparsity 2^n. A separate measure prevents transferring its hitting-set and AND-query bounds to the wrong basis.

Sources: [KLMY21](https://doi.org/10.1145/3406325.3450999), [KLMY21survey](https://cseweb.ucsd.edu/~shmcguir/papers/KLMYsigact.pdf). Status: original_basis_definitions_checked.

## literal-sparsity-conjecture-correction

Conjecture 3.19 says spar<=poly(approx_spar) literally. Sparse25 Remark 1.2 disproves that scale while proving a log-scale relationship with input length. Keep the negative and positive results separate.

Sources: [KLMY21survey](https://cseweb.ucsd.edu/~shmcguir/papers/KLMYsigact.pdf), [DMbasis25](https://eccc.weizmann.ac.il/report/2025/101/), [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/). Status: literal_statement_and_counterexample_checked.

## Forrelation-v1-v2-correction

The October 2026 revision restricts its near-half-exponent lower bound to nonadaptive algorithms and explicitly identifies the v1 gap in Appendix D. GS26 adaptive Conjecture 6 remains unresolved by this source.

Sources: [GS26](https://doi.org/10.4230/LIPIcs.ITCS.2026.72), [CCM26](https://arxiv.org/abs/2602.07503v2). Status: revision_and_model_checked.

## CDM25-HTML-PDF-disagreement

Publisher HTML abstract names CONJ and ApproxHW, whereas the pinned 57-page journal PDF defines positive AND/OR queries and uses ApproxHamWt. Do not silently identify signed conjunction queries with positive AND/OR queries. Journal theorem numbers are separately recorded.

Sources: [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), [CDM25](https://doi.org/10.1007/s00037-025-00266-7). Status: publisher_pdf_checked.

## EH89-Nis91-original-access

Earlier publisher full-text requests failed. User subsequently supplied original EH89 journal and Nis89 conference PDFs; statements and proof routes now inspected. Nis91 journal full text remains uninspected. See user-originals-EH89-Nis89 for conventions and the one-sided constant discrepancy.

Sources: [EH89](https://doi.org/10.1016/0890-5401(89)90001-1), [Nis89](https://doi.org/10.1145/73007.73038), [Nis91](https://epubs.siam.org/doi/10.1137/0220062). Status: EH89_and_Nis89_access_resolved_Nis91_journal_pending.

## user-originals-EH89-Nis89

User supplied original EH89 journal and Nis89 conference PDFs. Rank counts total nodes in EH89; Nis89 uses expected R_1/R_2 with success 1/2 and 3/4. Lemma 2.5 credits earlier work, perhaps Blum, via Blum–Impagliazzo. Journal Nis91 proof text remains uninspected; conference source closes the original cubic-proof access gap.

Sources: [EH89](https://doi.org/10.1016/0890-5401(89)90001-1), [Nis89](https://doi.org/10.1145/73007.73038), [Nis91](https://epubs.siam.org/doi/10.1137/0220062). Status: original_statements_and_proof_routes_checked.

## Nisan-expectation-constant-repair

Literal factor 2 disproved by one-bit expected-cost solver. The certificate-query proof gives sharp factor 4 at success 1/2; repository derivation, not a claimed published erratum. Nis91 journal text still uninspected.

Sources: [Nis89](https://doi.org/10.1145/73007.73038), [Nis91](https://epubs.siam.org/doi/10.1137/0220062). Status: literal_counterexample_and_repair_checked.

## Wellens-inner-theorem-constant

Theorem 3.13 gives 4.3935, sharper than 4.394 in introductory Theorem 1.1. Formula visually checked; source Maple LP computation not independently repeated.

Sources: [Wel22](https://arxiv.org/abs/2005.00566v2). Status: source_constant_and_proof_route_checked.

## DFLLV-2022-author-version

The 62-page May 2022 author manuscript confirms the main indexed general-domain/sensitivity statements and adds a Circuits section. Open questions move to Section 9. It is not identified as the 2026 journal proof; direct journal PDF attempts returned non-PDF responses.

Sources: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), [DFLLV26](https://doi.org/10.5070/C6.68665). Status: later_full_manuscript_checked_journal_pending.

## HKMP71-coefficient-versus-function-norm

The Lemma 71 proof normalizes by coefficient infinity norm but uses it as a function sup-norm bound. These differ by potentially the Fourier support size. The specific proof step is blocked; the final lemma is not claimed refuted.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256). Status: normalization_step_unverified.

## DFLLV26-journal-obtained

Normal browser access and download obtained the final 2026 journal PDF after shell/web downloads failed. It has 60 article pages plus repository cover. Main bound constants, R0 failure probability 2/3 and the oracle conventions are preserved. The journal omits the author manuscript Circuits section; open questions are in Section 8, not Section 9. Robust/q-analog questions are still proposed there.

Sources: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), [DFLLV26](https://doi.org/10.5070/C6.68665). Status: selected_final_journal_statements_and_proof_routes_checked.

## single-orbit-priority-BD16

The final domain journal paper credits BD16 for uniform D/Q polynomial equivalence on single multislices with coordinate queries. The original TQC paper proves D=O(Q^18), D=O(R^9) and C<=3bs*s_2. These do not imply uniform D/degree equivalence on unbalanced domains; later full-slice refinements are separate.

Sources: [BD16](https://doi.org/10.4230/LIPIcs.TQC.2016.7), [DFLLV26](https://doi.org/10.5070/C6.68665), [HKMP26](https://arxiv.org/abs/2603.29256). Status: original_source_and_model_checked.

## lambda-lift-independent-and-priority-audit

Separate-agent source-level audit validates the product lift after correcting an overstrong simulation sentence. It strengthens the product conflict bound to M=N_total and improves the coefficient to 10368*(2k-1)^10. Original 24 June 2020 author notes Section 7 say hypergraphical sensitivity remains open, but do not specify the precise exponent/uniformity in that closing sentence. The final journal records limitations of its direct representation-theoretic method. These do not certify current openness or novelty of this coarse fixed-k query-lift bound. Limited targeted primary searches found no printed exact lift theorem; priority remains unverified.

Sources: [FLLV20notes](https://yuvalfilmus.cs.technion.ac.il/Talks/ComplexityMeasures-HUJI.pdf), [DFLLV26](https://doi.org/10.5070/C6.68665). Status: independent_agent_mathematical_audit_passed_priority_unverified.

## verification-constants-and-corrected-Aaronson-route

Tal original Section 5.1.1 Claim 5.5 proves the constant-factor equivalence using independent coordinate sampling; it does not state the sharp ln(2) coefficient or the partial-promise sharpness example. Limited exact-phrase searches located no printed sharp-constant theorem. No novelty claim. Later Aaronson author manuscript explicitly repairs its old Theorem 10 proof; the four independently audited derivations do not use that proof.

Sources: [Aar02](https://arxiv.org/abs/quant-ph/0210020), [Tal13](https://eccc.weizmann.ac.il/report/2012/163/). Status: mathematical_audit_passed_exact_constant_priority_unverified.

## Tal-fractional-packing-constant-priority

Original Tal Section 5.1.2 prints fbs<=bs*(s-1+1/s). Chan–Lau later author-hosted journal-layout text credits the unweighted hypergraph theorem to Füredi (1981), and the weighted extension to Füredi–Kahn–Seymour (1993). Do not assign the packing theorem priority to Tal or Chan–Lau. Older texts remain to inspect.

Sources: [Tal13](https://eccc.weizmann.ac.il/report/2012/163/), [CL12](https://cs.uwaterloo.ca/~lapchi/papers/hypergraph.pdf). Status: Boolean_statement_original_checked_earlier_combinatorial_originals_pending.

## Targeted search: BK24-forward-targeted-2026-10-17

No resolving original source for BK24 Open Problems 1–3 was identified in these targeted searches. Their present status remains unverified; this is not evidence of openness or an exhaustive citation search.

Queries: total search exact quantum 2026; search problems approximate degree adversary 2025 2026; Separations in query complexity for total search problems 2025 2026 exact degree.

## Targeted search: conjecture-status-revisions-2026-10-17

Literal sparsity conjecture refuted; log-scale progress entered. Forrelation v2 is nonadaptive only. No resolving primary source for remaining BK24 questions, D versus bs quadratic conjecture or pure input-independent monomial AND conjecture was identified; this is not certification of current openness.

Queries: exact approximate monomial sparsity conjecture restriction trees 2025 2026; extremal Forrelation conjecture lower bound 2026 revision; total search exact quantum adversary degree open problems 2025 2026.

## Targeted search: search-status-2026-10-17-followup

BK24 arXiv page lists only v1. MFCS 2026 cites that preprint but does not resolve its three search questions. A search hit at ECCC TR24-172 is a different paper, Quantum Communication Advantage in TFNP; it is not a BK24 revision. No resolving primary source identified; present openness remains unverified.

Queries: total search exact quantum randomized separation 2025 2026; total search adversary approximate degree conical 2026; Separations in query complexity for total search problems publication.

## Targeted search: relevant-variable-status-2026-10-17

The original paper itself improves its introductory constant to 4.3935 in Theorem 3.13. No resolving primary source for Conjecture 3.17 identified; current status remains unverified.

Queries: Wellens 4.3935 relevant variables; Conjecture 3.17 Wellens; relevant variables sensitivity 4^s constant bound.

## Targeted search: broader-domain-conjectures-2026-10-17

The 2026 distributional paper proves equivalences and still states the influence conjecture, not a resolution. No primary resolution identified for HKMP26 Conjectures 72/78, robust low degree on S_n or perfect matchings, or the general q-analog framework; the records retain formulation/current-status caveats.

Queries: symmetric group robust low degree 2025 Boolean; perfect matching low degree robust Boolean 2026; 2603.29256 correction; Distributional Variants Aaronson Ambainis conjecture 2026.

## Targeted search: perturbation-correction-followup-2026-10-17

No primary-source correction of HKMP26 Lemma 71 identified. This limited search does not establish absence of a correction or present openness. Restricted perturbation formulation remains unverified.

Queries: "2603.29256" "perturbation"; "Complexity measures on the symmetric group" "robust" conjecture.

## Targeted search: higher-support-normalization-followup

No primary correction located in these narrow searches. No conclusion about absence of a correction or current openness is drawn. Source-level proof-pending status remains.

Queries: "2603.29256" "Lemma 71"; "From Promises to Totality" "Conjecture 72".

## Targeted search: lambda-partite-lift-priority-search

No primary publication of this exact product-lift bound located in this limited search. It is recorded as a repository derivation without a novelty/priority claim. Source representation-theoretic limitations for direct hypermatching witnesses are not claimed resolved.

Queries: hypermatchings sensitivity decision tree complexity permutation lift; "partite" "sensitivity" "complexity measures".

## Targeted search: verification-sharp-constants-priority-check

Original Tal Claim 5.5 checked: printed constant-factor equivalence, not the claimed optimal upper coefficient. Limited search does not establish priority.

Queries: "randomized certificate" "ln 2"; "fractional certificate" "ln 2"; "randomized certificate" "fractional" Aaronson constants.

