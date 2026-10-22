# Witness gallery and the 2026 sensitivity-separation updates

## Update checked 22 October 2026

The tracker now records **16 completed superquadratic checkpoints**, plus the separately indexed classical quadratic benchmark. Ten completed entries have been added since the 17 October snapshot: 2.0635, 2.075, 2.085, 2.10, 2.119, 2.127294, 2.13, 2.1301, 2.1303, and the exact logarithmic endpoint below. **2.15 remains open** and is excluded from every bound calculation. Completion timestamps and ingestion timestamps are stored separately; neither is treated as certified discovery priority.

The strongest completed exponent is

$$\alpha=\frac{\log(14055^8)}{\log(3738277295413674)}=2.130825579397823947629976285043\ldots.$$

For every positive exponent loss and every sensitivity threshold at least two, the recorded theorem supplies a total Boolean function above that threshold with block sensitivity at least sensitivity to the power alpha minus the loss. This is an exponent-level lower bound with arbitrary positive loss. The universal upper exponent remains four. The exact logarithmic expression is authoritative; the tracker decimal is a display approximation. The [public primitive theorem](https://prove2.me/theorems/01bb63ef-ced2-4ae9-8b81-b5ed295526c6) expands both complexity measures as finite maxima and includes the asymptotic quantifiers and a strict comparison to the preceding five-tolerance endpoint.

The gallery now has **136 construction records**, indexing all **83 separation claims** and **299 no-finite-power claims**. The complete catalogue has 782 claims and 127 references.

### Construction and proof details recovered from public primary records

| Checkpoint or exact endpoint | Public construction information | Proof route and limits |
|---|---|---|
| 2.0635 | Attributed to `abhishekdpseok`; accepted submission identified by the later Kothari source. | Original analytic/seed details remain unavailable in the current public description. Tracker and proved badge supersede stale outstanding-verification prose. |
| 2.075 | Robin Kothari and Codex: seven levels, nine nested predicates. Full2075.lean has a published SHA-256 identifier. | Joint-boundary estimates, finite labeling, disjoint blocks and exact integer certificate, followed by amplification. Seed integers remain unextracted. |
| 2.085 | `yousofy` with Codex: eight-layer refinement in the inherited nine-predicate framework. | Exact profile certificate and Boolean-family assembly. The internal name Sensitivity20855 does not by itself establish 2.0855. |
| 2.119 | Periodic two-stage invariant, published parameters K=44759, R=24501, C=83673433898775. | Strengthen the profile recurrence and assemble the Boolean construction. No undocumented recurrence role is inferred from these parameter names. |
| 2.10 | Completed formal goal 21/10. | A later proposal calls the linked proof “2.105”; that stronger informal value is not imported as a verified exponent. |
| 2.127294 | Twelve nested predicates and sharper joint boundary estimates. | Public proposal and completed goal checked; exact certificate remains unavailable. |
| 2.1301 | Fifteen predicates, coupled target/guard profiles, K=14207, R=7922, G=K², C=32057676379612508934192581. | One family per m with s≤C R^m and bs at zero ≥G^m. Multiple defect controls and periodic profiles yield the exact endpoint log(G)/log(R), also indexed. |
| 2.13 | Completed checkpoint, also implied by 2.1301. | Exponent weakening is a checked logical implication; it is not asserted to be the accepted checkpoint proof implementation. |
| 2.1303 | Fifteen predicates, four-stage cycle, K=12607, defect cutoffs (23,33,45,57,71), gamma=254/253. | Finite asymmetric Lovász local lemma supplies one shared labeling. The public source describes joint independence, dependency counts and an integer activity certificate. R=50063687, G=12607^4, C=3418946681687790375032 give s≤C R^m, bs at zero ≥G^m. |
| Refined four-stage endpoint | Keep G=12607^4 and reduce R from 50063687 to 50063523. | Public exact theorem yields log(G)/log(50063523)≈2.130320333220366; both exact endpoints are indexed separately from 2.1303. |
| Latest endpoint | One binary tournament labeling, ordinary defect cutoffs (24,31,38,44,50,55), source cutoff 22, recursive Boolean profile. | Six shared tolerances improve the sensitivity profile. The accepted primitive theorem and campaign wrapper preserve actual total functions, global sensitivity and disjoint blocks. Full recurrence and labeling proof bodies require authenticated access. |

For the finite-family route, a fixed prefactor C disappears into any positive exponent loss as m grows. The increasing zero-input block lower bounds, together with the known polynomial relation between block sensitivity and sensitivity, force sensitivity to become unbounded. For losses so large that the target power is nonpositive, witnesses for a smaller positive loss suffice. No inference uses extra coordinates alone to argue that sensitivity grows.

The five-tolerance comparison log(14055^8)/log(3738289747988852) is approximately 2.130825381447605; it is distinct from the earlier four-stage endpoint approximately 2.130320333220366. The latest theorem improves the former by about 1.98×10^−7 and the latter by about 0.000505246. The campaign mission text mentions both comparisons, and they must not be conflated.

### Verification and access

Fetched the live tracker, all current campaign goal pages, and the linked public theorem/finite-family statements. Per-page SHA-256 identifiers are recorded in the campaign manifest or bibliographic read-version fields. The sources credit usernames where verified full names are absent. Moser–Tardos is indexed as the classical local-lemma input, with journal metadata checked against its publisher-deposited Crossref record; this is not a new local lemma attributed to the 2026 constructions.

Public accepted-solution downloads return **HTTP 401**, requiring a Prove2Me login. This atlas therefore distinguishes **public primary statement/construction checks**, **platform-reported acceptance**, **source-reported local kernel verification**, and **independent proof replay**. It performs the first two checks; it has not replayed the later Lean proofs. Some exact seeds, recurrence coefficients and old 2.007/2.0391/2.05 proof bodies remain extraction gaps. The cards retain those limitations. No by-sorry statement skeleton is treated as an accepted proof. The older 2.1303 mission timeout note is historical; its linked finite-family theorem is now publicly marked Proved.

85-digit Decimal checks independently reproduce the public logarithmic scores and comparisons; they are consistency checks, not rigorous interval certificates. Exact formulas remain in the claims and propagated exponent chains. The new before/after report, data/sensitivity-campaign-oct22-matrix-improvements.json, records **four core entries and ten completion entries** improved from the 17 October publication. This includes consequences for spectral sensitivity through lambda≤s; the new ordinary-sensitivity result now slightly exceeds the older 2.127 spectral lower bound. All source-attestation and positive-exponent-loss qualifications propagate. The 176 unmatched completion intervals remain unmatched.

The campaign panel and footer now show the campaign check date independently of the broader catalogue audit date. The site labels exact logarithmic values as exact formulas and keeps open targets separate.

## Historical snapshot: 17 October 2026


Inspected on 17 October 2026. This edition adds a searchable witness gallery, mathematical rendering of inequalities and a dated record of the sensitivity/block-sensitivity campaign. No result is certified globally current best.

## The gallery

`data/witness-constructions.json` contains editorial construction overviews tied to exact existing claim IDs. `tools/witness_gallery.py` combines those with the witness registry, explicit dependency links and remaining source proof overviews to generate `data/separation-gallery.json`. The current gallery contains 126 construction records and indexes all 70 separation claims and all 299 no-finite-power claims. Some cards group source-specific variants; some retain an explicitly marked definition-extraction gap. A source/proof overview is not represented as a fully transcribed formal construction.

Every card includes a construction description or a clearly labelled source overview, separated measure pairs, proof summary, references and raw provenance. Table cells have a witness-gallery arrow when a relevant witness is indexed. Dossiers link to the constructions supporting their lower bounds and to the historical direct witnesses. Gallery measure pairs link back to the relevant scoped comparison. Promise witnesses are not silently used for total-function entries; completion links inherit the actual total witness through their recorded claim paths.

The renderer uses exact TeX where supplied and a conservative mathematical-expression parser elsewhere. Unknown prose remains escaped text. Presentation-only transcriptions for nonstandard statement strings live in `data/statement-latex.json`. Original statements, costs, scopes, qualifiers and losses remain available in the complete records. KaTeX runs with trust disabled, and tests check every displayed inequality statement's mathematical component.

## The original OpenAI construction

OpenAI, *A superquadratic separation between sensitivity and block sensitivity*, 25 September 2026, 11 pages, repository preprint. This is separately keyed **OAIsens26**, distinct from the already indexed OpenAI randomized/quantum query separation **OAI26**. The source is pinned to Git commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`; the PDF has its own SHA-256 snapshot. [Paper](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/paper.pdf).

Theorem 1.1 gives, for each depth d, a total function whose block-sensitivity/squared-sensitivity ratio is at least `2^d/(4(d+2)^2)`. The construction uses nested predicates, regular tournament rows and labelled outgoing blocking coordinates. A probabilistic label exclusion controls near-satisfied clauses. Four coupled profiles bound ordinary sensitivity and simultaneous flips of two predicates. OR balancing and the source estimates give, for M>=9^(d+1),

`A=2(d+2)M^(d+1), B=M^2(2M^2+1)^d, s(f)<=A, bs(f,0)>=B`.

Lemma 4.2 proves the composition inequalities; Corollary 4.3 chooses d=9, M=9^10 and self-composes the seed. The resulting exponent log(B)/log(A) is strictly above the campaign's recorded exact decimal `2.000252407`. The theorem rules out every universal quadratic bound. This ordinary-sensitivity argument is stronger than the earlier spectral-sensitivity counterexample, which by itself did not settle the ordinary question.

The depth-20 specialization uses d=20 and M=9^21, with A=44M^21 and B=M^2(2M^2+1)^20. The campaign records the stronger decimal target `2.006470828`. This changes parameters in the same general construction rather than establishing a new architecture. The selected original proof route and parameters were inspected; the Lean development was not rebuilt. High-precision numerical consistency checks are saved separately and explicitly are not formal certificates.

## What the campaign records

The [Prove2Me campaign](https://prove2.me/campaigns/block-sensitivity-vs-sensitivity) was inspected directly, including its public HTML data and individual goal pages. SHA-256 identifiers, mission URLs, status, recorded timestamps and platform solve timestamps are in `data/sensitivity-campaign.json`. This is a static dated snapshot, not an automatic monitor.

Completed milestones on inspection:

| Exact recorded target | Platform solve date (UTC) | Construction/proof access |
|---|---|---|
| 2.000252407 | 15 October 2026 | Original OpenAI fixed seed; selected paper proof checked. |
| 2.006470828 | 15 October 2026 | Depth-20 specialization of the same bounds. |
| 2.007 | 15 October 2026 | Goal and certificate framework inspected; accepted seed/proof body not recovered. |
| 2.0205 | 16 October 2026 | Mission specifies sharper four-profile estimates, target-row count fifteen, and a sink/no-sink gate split. |
| 2.0391 | 16 October 2026 | Explicit PROVED status and accepted activity; actual accepted seed/proof body not recovered. |
| 2.05 = 41/20 | 16 October 2026 | Explicit PROVED status; accepted activity attributed to Robin Kothari. Actual accepted seed/proof body not recovered. |

The 2.0205 mission specifies d=17, M=1475863, r=88 and K=1439236 OR copies, and states the exact certificate `A^4041 < B^2000`. These are estimates for its refined construction/proof, not an application of the original paper's much stronger M>=9^(d+1) requirement at those parameters.

For the campaign theorem, the quantifiers are essential: for every epsilon>0 and threshold S>=2, there exists a total Boolean function with s(f)>=S and bs(f)>=s(f)^(alpha-epsilon). The catalogue conservatively stores campaign lower bounds with subpolynomial loss; it does not turn this into a loss-free fixed endpoint inequality. The public proposal text explains a sufficient finite-certificate route, not necessarily the accepted proof's actual implementation. No exact seed is invented for a missing proof body.

Some mission pages retain the heading “Open Problem”, old challenge prose and a `by sorry` statement skeleton despite an explicit **PROVED** goal status and accepted activity. Neither the stale prose nor the placeholder is treated as the proof. Status comes from the campaign's completed entries and the explicit goal state. This is platform attestation, not an independent kernel check or a journal publication.

**2.0635 and 2.10 were open targets**, not completed lower bounds. They are displayed separately and excluded from the exponent matrix. The goal/attestation-access limitations are prominent on the later witness cards and the bound dossier.

## Consequences and preserved qualifications

The recorded bs/s interval is now 2.05 to 4. The existing rules also improve RC/s to lower exponent 2.05 and five completion lower entries; their full before/after provenance is saved in `data/sensitivity-campaign-matrix-improvements.json`. The 176 unmatched completion intervals remain unmatched. These mechanical consequences inherit the source attestation and subpolynomial qualifications.

The qualitative sensitivity conjecture remains resolved positively. Its quadratic strengthening is now separately recorded as refuted, with the original preprint and campaign improvements linked. The spectral conjecture's status record has been clarified to distinguish these two refutations.
