# Witness gallery and the 2026 sensitivity-separation updates

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
