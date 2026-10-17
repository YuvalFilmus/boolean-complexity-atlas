# Independent checks, source corrections and remaining gaps

Audit date: 17 October 2026. No HTML has been started. The 23-measure completion grid still has 506 directions: 442 finite recorded intervals, 266 matching exponents, 176 unmatched intervals and 64 no-finite-power directions. This round does not claim a further exponent improvement.

## Independent mathematical review

A separate assistant agent independently reconstructed four arguments from their stored statements and conventions: the sharp verification/fractional-certificate constants, the capped one-sided deterministic simulation, quantitative kernel-line avoidance and the bounded-interpolation vertex lemma. All four passed. The [complete review](new-derivations-independent-audit.md) is preserved, with exact reviewed records and their hashes in `data/new-derivations-independent-audit.json`. This is a separate-agent mathematical audit, not formal verification, human peer review, priority certification or a complete audit of the supporting literature.

In particular, the review confirms that the conditional normalization arguments retain parameters that may grow badly. Neither implies a polynomial bound for unrestricted dependent support. The source-minimality requirement has not been removed, nor has a counterexample satisfying all of its hypotheses been constructed. The remaining task is a uniform bound on the full-cube norm relative to the resulting margin, with degree controlled by native approximate degree. Augmented vertex rank alone does not supply that bound.

## Aaronson source correction

The author-hosted [Quantum Certificate Complexity manuscript](https://www.scottaaronson.com/papers/qcc.pdf) has 12 pages; the stored original preprint has nine. Both are now separately identified by cryptographic hashes. The author manuscript's footnote 3 on page 6 acknowledges that the earlier Theorem 10 proof contains a false, superfluous claim, credited to Gatis Midrijanis. Comparing the proofs isolates the old reset-to-a-zero-input assertion as a passage to avoid. The footnote itself does not name the assertion. A separately checked two-bit example refutes that intermediate assertion directly: for OR on two bits, the zero-input verifier independently samples each coordinate with probability one half. It is a valid optimal independent verifier, but resetting the input 11 toward 00 makes its output zero only when both bits are sampled, with probability one quarter. This does not refute Theorem 10.

The corrected proof directly uses coupling: querying a randomized certificate for a consistent zero input hits every maximal monomial of a nondeterministic representative with probability at least one half. The monomial-shrinking potential bounds the number of rounds, yielding `R0=O(RC*ndeg*log(2+n))` for total functions, with expected classical query costs. The mixed bound and its corrected proof summary are now indexed in `algorithmic_bounds`. They retain the input-length factor and do not multiply separately minimized completion measures.

The independently checked verification-constant proof uses Definition 3 and direct coupling, not the faulty earlier Theorem 10 passage. The author manuscript is undated and is not identified here with the publisher's ten-page journal article. Journal metadata remains: Scott Aaronson, *Quantum Certificate Complexity*, Journal of Computer and System Sciences **74**(3), 313–322 (2008), DOI [10.1016/j.jcss.2007.06.020](https://doi.org/10.1016/j.jcss.2007.06.020).

## A recovered constant-factor comparison and its priority chain

Tal's original ECCC TR12-163, Section 5.1.2, pages 13–14, prints

`fbs(f) <= bs(f)*(s(f)-1+1/s(f))`

for nonconstant total Boolean functions. Constants are treated separately. This supplements the coarser product inequality without changing an exponent. In particular, put g(0)=0 and g(b)=b^2-b+1 for integer b>=1. Since t-1+1/t increases on [1,infinity) and s<=bs, it gives `fbs=FC<=g(bs)`. Choosing a single extension minimizing bs gives `completion_fbs=completion_FC<=g(completion_bs)`. A separate agent checked the original Tal statement, the algebra and the completion lift; its follow-up checks, including the OR_2 reset example, are preserved in `data/supplemental-independent-checks.json`. No separate completion minima are multiplied.

Proof summary: minimal sensitive blocks at an input form a hypergraph whose integral and fractional matching numbers are block sensitivity and fractional block sensitivity at that input. Each block has size at most global sensitivity: at the input obtained by flipping a minimal block, every bit of that block is sensitive. Padding smaller edges with private vertices makes the hypergraph uniform without changing either matching number. Apply the fractional matching integrality-gap bound and maximize over inputs. Single-input projective-plane sharpness does not certify sharpness after maximizing over all Boolean inputs.

The bibliography now includes Yuk Hei Chan and Lap Chi Lau, *On linear and semidefinite programming relaxations for hypergraph matching*, Mathematical Programming **135**(1–2), 123–148 (2012), DOI [10.1007/s10107-011-0451-5](https://doi.org/10.1007/s10107-011-0451-5), with its SODA 2010 predecessor distinguished. The 26-page author-hosted journal-layout manuscript has been hashed and selected passages checked. It attributes the earlier unweighted result to Zoltán Füredi, *Maximum degree and fractional matchings in uniform hypergraphs*, Combinatorica **1**(2), 155–162 (1981), and the weighted extension to Zoltán Füredi, Jeff Kahn and Paul Seymour, *On the fractional matching polytope of a hypergraph*, Combinatorica **13**(2), 167–180 (1993). Those earlier texts remain uninspected; their bibliographic details are recorded as cited by the checked source, not as independently verified original-source entries. Tal and Chan–Lau are not assigned priority for the packing theorem.

Tal's Section 5.1.1 also supplies an original printed proof of the constant-factor equivalence of FC and operational RC. It does not print the sharp ln(2) coefficient or the partial-promise sharpness family in the repository. Exact-phrase searches did not locate such a printed theorem; that limited search does not establish novelty.

## Journal and completion status

AB25's [Crossmark record](https://crossmark.crossref.org/dialog/?doi=10.1007/s00037-025-00277-4) reports the document current, with online publication on 3 October 2025 and print publication in December 2025. This closes a metadata check, not the outstanding journal-proof comparison. The Nis91 journal text likewise remains uninspected; the supplied Nis89 conference text remains the basis for the expected-cost constant discrepancy. No journal correction is asserted.

The unmatched interval queue remains an evidence queue, not a list of 176 certified open problems. The newly recovered mixed inequalities have no justified route that improves its parameter-free exponents: both the surviving logarithmic input-length factor and the noncommutation of separate completion minima must be respected. Source, priority and normalization gaps remain explicitly marked rather than counted as closed.
