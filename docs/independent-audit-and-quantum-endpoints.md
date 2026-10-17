# Independent lift audit, quantum endpoints and normalization status

This round independently checks the lambda-partite lift, tightens fifteen completion lower bounds, records an original historical question and refines what the dependent-support geometry does and does not prove. The 176 unmatched intervals remain unmatched, but several are narrower; their count is not evidence that no progress occurred or that all are open problems.

## Independent audit and incorporated repair

A separate assistant agent audited the complete lift against the final DFLLV26 journal, including the actual parameter proofs, exact-degree isotypic decomposition, pseudo-character spanning and cube construction. Its [full report](lambda-lift-independent-audit.md) is preserved. The manifest `data/lambda-lift-independent-audit.json` stores the original claim, original proof hash, findings and corrected proof hash. This is a separate-agent source-level mathematical check, not formal verification or human peer review.

The audit found a false sentence in the simulation proof: arbitrary completions of the stored partial representation need not all project to the fixed hypermatching. Two undiscovered edges can be regrouped. The needed invariant is existential: at every transcript there exists a complete representative of the fixed input extending all answers. Assign the remaining actual hyperedges to free common labels to obtain such a representative. At a leaf it follows the transcript and certifies the leaf's correct value. The main bound survives this correction. The earlier uniform-lift explanation has been corrected as well.

The independent audit also strengthens the product conflict bound. If two partial product-permutation inputs are not separated by a forward or inverse query, their union is a partial bijection in every component. Each extends independently to a full permutation. Thus every incompatible pair is separated regardless of size, and the source-capped threshold is M=N_total, not merely the previously used lower bound min_i N_i.

Consequently D_Z<=2C_Z^2. Together with the checked product sensitivity/certificate chain and the hyperedge matching argument, the corrected stronger bound is

`D_hyper(f) <= 10368*(2k-1)^10*s_hyper(f)^10`,

where k is the total hyperedge size. The color-multiplicity ratio has disappeared. The coefficient still depends on k. Full-domain availability and the vertex-to-entire-hyperedge oracle remain essential. The audit verifies the product witnessing theorem, not a direct hypermatching alpha-witnessing system or a quadratic intrinsic degree/sensitivity theorem. All seven profile grids retain their 924 parameterized upper chains; optimality is not certified.

## Tightened unmatched quantum intervals

The original AIK26 v3 Theorems 2.1 and 2.3 concern the same total family F_n:

- C(F_n)>=Omega(n^2);
- Q(F_n)<=O(sqrt(n)*log^3 n);
- QE(F_n)=Theta(n*log^2 n) and Q0(F_n)=Theta(n*log^2 n).

The joint consequences were not previously extracted into the extended interval table. They give Q0>=Omega_tilde(Q^2), C>=Omega_tilde(Q0^2), and C>=Omega_tilde(QE^2). Fifteen lower records improve through the existing checked transfers, including side-specific and unambiguous-certificate versions. The machine-readable before/after list is `data/quantum-endpoint-lower-improvements.json`.

For example, completion_C versus either completion_QE or completion_Q0 now has lower exponent two rather than the earlier exact exponent 8 log(3)/log(2048). Completion_Q0 versus completion_Q now has lower exponent two rather than the parity baseline one. Their upper exponents remain three, four and four respectively, so these are narrower gaps, not newly matched intervals.

The proof routes were checked in the original: Lemma 7.3 exactly evaluates the function by finding terms, reading selected bits and checking the addressed cheat-sheet cell. Lemma 7.4 fixes all fields except count fields, leaving an AND on Theta(n log^2 n) bits. Any zero-error algorithm with positive acceptance on the unique positive AND input has a nonzero accepting amplitude which vanishes on every other input; its multilinear degree is the full number of bits. The amplitude polynomial method therefore supplies the required query lower bound. This checks the capped, detectable-failure convention rather than borrowing an expected quantum cost convention.

Polylogarithmic losses are retained. For the Q0-versus-Q consequence, C=O(Q^4) and C>=Omega(n^2) also give Q>=Omega(sqrt(n)), so log Q and log n are comparable; the parameter logarithms are not silently exchanged. Official arXiv version histories still identify AIK26 v3 (5 October 2026) and HKMP26 v3 (30 September 2026) as their current listed versions.

## Dependent support: what minimality really supplies

The unrestricted normalization step remains unverified. A further polyhedral lemma now isolates the correct rank statement available from support minimality.

Fix the support S of a bounded support-minimal approximant p, let A be its promise evaluation matrix, and H the full-cube evaluation matrix on S. Consider

`P={a: A a=A a_p, -1<=H a<=1}`.

This polytope is nonempty and compact: full-cube boundedness bounds every Fourier coefficient by one. Every feasible point has all its S coefficients nonzero; otherwise it would supply a bounded approximant with identical promised values and smaller support. In particular, choose a vertex a*. At that vertex the stacked matrix consisting of A and saturated cube-evaluation rows has full column rank. Otherwise a nonzero common null direction permits sufficiently small positive and negative movements while maintaining all inactive inequalities, contradicting extremality.

This is an augmented rank statement. It does not prove full rank of A alone, nor polynomial control of the kernel amplification, slab-escape radius or full-cube margin. Saturated off-promise constraints are precisely what can stop coefficient elimination. The lemma does not construct a support-minimal counterexample to the source conclusion; it identifies what an argument based on bounded-polytope vertices actually establishes.

Together with the earlier results, the current verified sufficient cases are: coefficient l1 norm at most one for a support-minimal approximant; independent supported characters; polynomially bounded support or logarithmic character rank; polynomially bounded kernel amplification; or a quantitatively well-conditioned kernel direction satisfying the explicit slab-length bounds. None is shown here to follow from unrestricted support minimality. The enlarged-basis majority obstruction remains separate from the original-support case and the final D-versus-Q conclusion.

## Original sources, historical notation and priority

The dated original notes *Complexity measures on the symmetric group* (24 June 2020), by Yuval Filmus, Noam Lifshitz, Nathan Lindzey and Marc Vinyals, are now a separate bibliography record FLLV20notes. Their four-author cover is not merged with the later five-author journal paper. Section 7 explicitly raises hypergraphical sensitivity as a historical question. The nearby context concerns Huang-type sensitivity bounds; its closing sentence does not fix an exponent or parameter uniformity. The coarse fixed-k query-lift result must therefore not be announced as resolving every intended version of that question.

The final DFLLV26 journal records limitations of its direct representation-theoretic technique. The audited product lift uses permutation representations instead and does not establish the missing direct hypermatching witnesses. Limited targeted primary-source searches found no printed version of the exact lift theorem, but this does not certify novelty or current literature priority. The catalogue keeps priority unverified.

The notes also call the fractional certificate LP “randomized certificate complexity.” That literal historical name is now indexed under FC with a normalization warning: it is not numerically identical to the operational expected-query RC used elsewhere. This matters especially now that the constant factors are explicit.

## Remaining status

There are 442 finite completion intervals: 266 with matching recorded exponents and 176 unmatched; 64 directions exclude every finite power. Current-best certification, priority, the unrestricted dependent-support lemma and pending Nis91/AB25 journal proofs remain unfinished. Conjecture records distinguish fixed targets, original versus enlarged support, exact promise interpolation versus label approximation, direct quadratic sensitivity versus coarse polynomial equivalence, and uniform family-polynomial quantifiers. No HTML generated.
