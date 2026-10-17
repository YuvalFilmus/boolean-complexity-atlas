# Measures and notation

Generated from data/catalog.json. Alias lists are seeds; exact occurrences and full historical coverage remain to be audited. Stable IDs, not symbols, identify measures.

## D: deterministic query complexity

Symbol: `D`. Definition status: source_checked.

Minimum worst-case depth of a deterministic bit-query tree computing the required value (or a valid output for a relation).



Definition locator: KLLPV26 Definition 14.

- Alias `deterministic decision-tree complexity`: [BdW02](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf), Section 3.1; source_checked.
- Alias `DT`: [LM26](https://dmtcs.episciences.org/en/articles/18512), Section 2; DM23 Section 2; source_checked.
- Alias `Depth`: [LM26](https://dmtcs.episciences.org/en/articles/18512), Section 2; DM23 Section 2; source_checked.
- Alias `Depth`: [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 2; source_checked.
- Alias `P^dt`: [GPW18](https://eccc.weizmann.ac.il/report/2015/050/revision/1/), Section 1, query notation; source_checked.
- Alias `D`: [ABK16](https://arxiv.org/abs/1511.01937), Section 2.2; source_checked.
- Alias `D`: [SW86](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/SW86/SW86.pdf), Section I, p.29; source_checked.
- Alias `D^dt`: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2: decision-tree and pseudo-deterministic definitions; source_checked.
- Alias `P^dt(f)`: [Goos15](https://eccc.weizmann.ac.il/report/2015/012/), Sections 1.1–2, pp.2–4; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [BdW02](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf), [KLLPV26](https://arxiv.org/abs/2609.26757), [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/).

## R: bounded-error randomized query complexity

Symbol: `R`. Definition status: source_checked.

Minimum worst-case query cap with success at least 2/3 on every input in the domain.



Definition locator: KLLPV26 Definition 15.

- Alias `R`: [ABK16](https://arxiv.org/abs/1511.01937), Section 2.2; source_checked.
- Alias `BPP^dt`: [GJPW18](https://eccc.weizmann.ac.il/report/2015/169/), Section 2; source_checked.
- Alias `R_2`: [Aar02](https://arxiv.org/abs/quant-ph/0210020), Section 1; source_checked.
- Alias `Monte Carlo`: [ABBLS17](https://arxiv.org/abs/1506.04719), Section 2, Randomized decision tree algorithms; source_checked.
- Alias `R^dt`: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2: decision-tree and pseudo-deterministic definitions; source_checked.
- Alias `BPP^dt`: [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36), Theorem 4 and Section 2; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `R_{1/3}`: ABK16; repository_display_not_a_historical_occurrence.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [ABK16](https://arxiv.org/abs/1511.01937), [KLLPV26](https://arxiv.org/abs/2609.26757), [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36).

## R0: zero-error randomized query complexity

Symbol: `R_0`. Definition status: source_checked.

Minimum worst-input expected number of queries of an always-correct randomized algorithm. Fixed-cap algorithms with constant inconclusive probability are equivalent only up to constants.

 ABK16 Section 2.2 uses fixed worst-case cost with failure symbol probability <=1/2; KLLPV26 Definition 16 uses worst-case expected cost and always-correct output. These are equivalent up to universal factors by truncation/restart, not numerically identical. Exact constants require selecting a convention.

Definition locator: KLLPV26 Definition 16.

- Alias `R_0`: [ABK16](https://arxiv.org/abs/1511.01937), Section 2.2; source_checked.
- Alias `Las Vegas`: [BdW02](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf), Section 3.3, footnote; source_checked.
- Alias `R`: [SW86](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/SW86/SW86.pdf), Section I, p.29; source_checked.
- Alias `Las Vegas`: [ABBLS17](https://arxiv.org/abs/1506.04719), Section 2, Randomized decision tree algorithms; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [ABK16](https://arxiv.org/abs/1511.01937), [KLLPV26](https://arxiv.org/abs/2609.26757).

## R1: one-sided-error randomized query complexity

Symbol: `R_1`. Definition status: source_checked.

Query cap with no false positives and acceptance probability at least 2/3 on positive inputs. Complement orientation must be separate.

Other sources reverse the one-sided orientation; do not merge without complementing f.

Definition locator: AIK26 Section 2, preliminaries.

- Alias `R_1`: [AIK26](https://arxiv.org/abs/2609.11664), Section 2; source_checked.

Sources: [AIK26](https://arxiv.org/abs/2609.11664).

## Q: bounded-error quantum query complexity

Symbol: `Q`. Definition status: source_checked.

Minimum quantum bit-oracle query cap with success at least 2/3 on every promised input.



Definition locator: KLLPV26 Definition 17.

- Alias `Q`: [ABK16](https://arxiv.org/abs/1511.01937), Section 2.2; source_checked.
- Alias `Q_2`: [Aar02](https://arxiv.org/abs/quant-ph/0210020), Section 1; source_checked.
- Alias `Q_{1/3}`: [HS05survey](https://arxiv.org/abs/quant-ph/0509153), Section 2; source_checked.
- Alias `Q^dt`: [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36), Theorem 4 and Section 2; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [ABK16](https://arxiv.org/abs/1511.01937), [KLLPV26](https://arxiv.org/abs/2609.26757), [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36).

## QE: exact quantum query complexity

Symbol: `Q_E`. Definition status: source_checked.

Minimum fixed query cap of a quantum algorithm computing f with certainty.



Definition locator: KLLPV26 Definition 19.

- Alias `Q_E`: [ABK16](https://arxiv.org/abs/1511.01937), Section 2.2; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `Q_{\mathrm E}`: Mid04; repository_display_not_a_historical_occurrence.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [Mid04](https://arxiv.org/abs/quant-ph/0403168), [KLLPV26](https://arxiv.org/abs/2609.26757).

## Q0: zero-error quantum query complexity

Symbol: `Q_0`. Definition status: source_checked.

Minimum fixed query cap returning a correct answer with probability at least 1/2 and otherwise inconclusive; never wrong.

Do not silently identify fixed-cap, expected-time, and exact models when tracking constants.

Definition locator: KLLPV26 Definition 18.

- Alias `Q_0`: [Aar02](https://arxiv.org/abs/quant-ph/0210020), Section 1; source_checked.

Sources: [Aar02](https://arxiv.org/abs/quant-ph/0210020), [KLLPV26](https://arxiv.org/abs/2609.26757).

## s: sensitivity

Symbol: `s`. Definition status: source_checked.

max_x |{i : f(x) != f(x xor e_i)}|, with both inputs in the domain when used on a promise.



Definition locator: KLLPV26 Definition 31 (output-restricted maxima for s_b).

- Alias `s`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 31; source_checked.
- Alias `critical sensitivity`: [Nis89](https://doi.org/10.1145/73007.73038), Publisher abstract; source_checked.
- Alias `s_w(f)`: [Nis89](https://doi.org/10.1145/73007.73038), Section 2, p.330; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [BdW02](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf), [KLLPV26](https://arxiv.org/abs/2609.26757).

## s0: 0-sensitivity

Symbol: `s_0`. Definition status: source_checked.

Maximum local sensitivity over promised inputs x with output f(x)=0. This is output-conditioned, not a restriction on the values of the flipped input coordinates.

 Notation clash: CDM23 Section 2 also uses this typography for input-directed flips. Its output-conditioned version is described separately immediately afterwards; do not identify the two definitions.

Definition locator: KLLPV26 Definition 31 (output-restricted maxima for s_b).

- Alias `s_0`: [ABKBRT21](https://arxiv.org/abs/2010.12629), Appendix A, Lemma 31; source_checked.

Sources: [ABKBRT21](https://arxiv.org/abs/2010.12629), [KLLPV26](https://arxiv.org/abs/2609.26757).

## s1: 1-sensitivity

Symbol: `s_1`. Definition status: source_checked.

Maximum local sensitivity over promised inputs x with output f(x)=1. This is output-conditioned, not a restriction on the values of the flipped input coordinates.

 Notation clash: CDM23 Section 2 also uses this typography for input-directed flips. Its output-conditioned version is described separately immediately afterwards; do not identify the two definitions.

Definition locator: KLLPV26 Definition 31 (output-restricted maxima for s_b).

- Alias `s_1`: [ABKBRT21](https://arxiv.org/abs/2010.12629), Appendix A, Lemma 31; source_checked.

Sources: [ABKBRT21](https://arxiv.org/abs/2010.12629), [KLLPV26](https://arxiv.org/abs/2609.26757).

## bs: block sensitivity

Symbol: `bs`. Definition status: source_checked.

Maximum over inputs of the largest family of pairwise disjoint sensitive coordinate blocks.



Definition locator: KLLPV26 Definition 33 (output-restricted maxima for bs_b).

- Alias `bs`: [NS94](https://web.vu.lt/mif/s.jukna/boolean/Nisan-Szegedy.pdf), Definition 3.6; source_checked.
- Alias `bs_w(f)`: [Nis89](https://doi.org/10.1145/73007.73038), Section 2, p.330; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [Nis91](https://epubs.siam.org/doi/10.1137/0220062), [KLLPV26](https://arxiv.org/abs/2609.26757).

## bs0: 0-block sensitivity

Symbol: `bs_0`. Definition status: source_checked.

Maximum local block sensitivity over promised inputs x with output f(x)=0. This is output-conditioned, not input-directed.

 Notation clash: CDM23 Section 2 also uses this typography for input-directed flips. Its output-conditioned version is described separately immediately afterwards; do not identify the two definitions.

Definition locator: KLLPV26 Definition 33 (output-restricted maxima for bs_b).

- Alias `bs_0`: [GSS13](https://arxiv.org/abs/1306.0630), Section 2; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [ABK16](https://arxiv.org/abs/1511.01937), [KLLPV26](https://arxiv.org/abs/2609.26757).

## bs1: 1-block sensitivity

Symbol: `bs_1`. Definition status: source_checked.

Maximum local block sensitivity over promised inputs x with output f(x)=1. This is output-conditioned, not input-directed.

 Notation clash: CDM23 Section 2 also uses this typography for input-directed flips. Its output-conditioned version is described separately immediately afterwards; do not identify the two definitions.

Definition locator: KLLPV26 Definition 33 (output-restricted maxima for bs_b).

- Alias `bs_1`: [GSS13](https://arxiv.org/abs/1306.0630), Section 2; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [ABK16](https://arxiv.org/abs/1511.01937), [KLLPV26](https://arxiv.org/abs/2609.26757).

## bs_l: bounded-block-size sensitivity

Symbol: `bs_ell`. Definition status: source_checked.

Block sensitivity with each sensitive block of size at most ell; ell is an explicit parameter.



Definition locator: HKP11 Section 3.1 discussion of ell-block sensitivity.

- Alias `bs_ell`: [HKP11](https://tocmirror.cs.uchicago.edu/articles/gs004/), Section 3.1; source_checked.
- Alias `ell-block sensitivity`: [HKP11](https://tocmirror.cs.uchicago.edu/articles/gs004/), Section 3.1; source_checked.

Sources: [HKP11](https://tocmirror.cs.uchicago.edu/articles/gs004/).

## C: certificate complexity

Symbol: `C`. Definition status: source_checked.

Maximum over x of the minimum number of coordinates fixing f(x) among inputs in the domain.

 Partial-function certificates here are weak: only promised opposite-output inputs must be excluded. Strong certificates that exclude off-promise inputs are a different measure.

Definition locator: KLLPV26 Definition 22.

- Alias `certificate size`: [BdW02](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf), Section 2.2; source_checked.
- Alias `C`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 22; source_checked.
- Alias `N`: [SW86](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/SW86/SW86.pdf), Section I, p.31; source_checked.
- Alias `HSC`: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Definition 2.4; source_checked.
- Alias `C_w(f)`: [Nis89](https://doi.org/10.1145/73007.73038), Section 2, p.330; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [BdW02](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf), [KLLPV26](https://arxiv.org/abs/2609.26757), [CDMRS23](https://doi.org/10.1145/3564246.3585199).

## C0: 0-certificate complexity

Symbol: `C_0`. Definition status: source_checked.

Maximum minimum certificate size over 0-inputs.

 Partial-function certificates here are weak: only promised opposite-output inputs must be excluded. Strong certificates that exclude off-promise inputs are a different measure.

Definition locator: KLLPV26 Definition 22.

- Alias `C^0`: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 1 notation paragraph; source_checked.
- Alias `C_0`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 22; source_checked.
- Alias `CNF width`: [GPW18](https://eccc.weizmann.ac.il/report/2015/050/revision/1/), Section 1, complement of nondeterministic model; source_checked.
- Alias `coNP^dt(f)`: [Goos15](https://eccc.weizmann.ac.il/report/2015/012/), Sections 1.1–2, pp.2–4; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [BdW02](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf), [KLLPV26](https://arxiv.org/abs/2609.26757).

## C1: 1-certificate complexity

Symbol: `C_1`. Definition status: source_checked.

Maximum minimum certificate size over 1-inputs.

 Partial-function certificates here are weak: only promised opposite-output inputs must be excluded. Strong certificates that exclude off-promise inputs are a different measure.

Definition locator: KLLPV26 Definition 22.

- Alias `C^1`: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 1 notation paragraph; source_checked.
- Alias `NP^dt`: [GPW18](https://eccc.weizmann.ac.il/report/2015/050/revision/1/), Section 1, query notation; source_checked.
- Alias `C_1`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 22; source_checked.
- Alias `DNF width`: [GPW18](https://eccc.weizmann.ac.il/report/2015/050/revision/1/), Section 1; source_checked.
- Alias `C^(1)(f)`: [Nis89](https://doi.org/10.1145/73007.73038), Section 4, p.333; source_checked.
- Alias `NP^dt(f)`: [Goos15](https://eccc.weizmann.ac.il/report/2015/012/), Sections 1.1–2, pp.2–4; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [BdW02](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf), [KLLPV26](https://arxiv.org/abs/2609.26757).

## fbs: fractional block sensitivity

Symbol: `fbs`. Definition status: source_checked.

Maximum over x of the LP packing of sensitive blocks: nonnegative weights with total weight through any coordinate at most 1.



Definition locator: KLLPV26 Definition 34.

- Alias `fbs`: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 2; source_checked.
- Alias `bs^*`: [GSS13](https://arxiv.org/abs/1306.0630), Section 2; source_checked.

Sources: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), [KLLPV26](https://arxiv.org/abs/2609.26757).

## FC: fractional certificate complexity

Symbol: `FC`. Definition status: source_checked.

Maximum over x of the LP covering of sensitive blocks by nonnegative coordinate weights, each sensitive block receiving weight at least 1.

LP duality gives FC=fbs under this definition. Keep RC as a distinct, only constant-factor equivalent measure.

Definition locator: KLLPV26 Definition 24.

- Alias `FC`: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 2; source_checked.
- Alias `C^*`: [GSS13](https://arxiv.org/abs/1306.0630), Section 2 and Appendix A; source_checked.
- Alias `randomized certificate complexity`: [FLLV20notes](https://yuvalfilmus.cs.technion.ac.il/Talks/ComplexityMeasures-HUJI.pdf), Section 2, p.3, immediately after the certificate LP relaxation; source_checked.

Sources: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), [KLLPV26](https://arxiv.org/abs/2609.26757).

## RC: randomized certificate complexity

Symbol: `RC`. Definition status: source_checked.

For each fixed x, minimum worst-case expected number of classical queries of a verifier accepting x with probability 1 and rejecting every promised y with f(y)!=f(x) with probability at least 1/2; maximize over x. Its behavior on other same-output inputs is unrestricted.



Definition locator: Aar02 Definition 3 and Proposition 4.

- Alias `RC`: [Aar02](https://arxiv.org/abs/quant-ph/0210020), Definition 3; source_checked.

Sources: [Aar02](https://arxiv.org/abs/quant-ph/0210020).

## QC: quantum certificate complexity

Symbol: `QC`. Definition status: source_checked.

For each fixed x, minimum quantum query cost of a verifier accepting x with certainty and rejecting every promised y with f(y)!=f(x) with probability at least 1/2; maximize over x. Allowing two-sided constant error changes the measure by at most a constant factor.

 Quantum query cost uses a fixed query cap; the original text defines the quantum analogue of its verifier. Do not identify numerical constants across expected-classical and fixed-quantum cost conventions.

Definition locator: Aar02 Definition 3 and Proposition 4.

- Alias `QC`: [Aar02](https://arxiv.org/abs/quant-ph/0210020), Definition 3; source_checked.

Sources: [Aar02](https://arxiv.org/abs/quant-ph/0210020).

## UC: unambiguous certificate complexity

Symbol: `UC`. Definition status: source_checked.

Maximum of UC_0 and UC_1; UC_b is minimum maximum width of a disjoint monochromatic b-subcube cover.

Do not equate with subcube partition complexity without checking the exact partition objective. Keep as a candidate alias in the notation-completion backlog.

Definition locator: KLLPV26 Definition 23.

- Alias `UC`: [AIK26](https://arxiv.org/abs/2609.11664), Section 2; source_checked.
- Alias `2UP^dt`: [GPW18](https://eccc.weizmann.ac.il/report/2015/050/revision/1/), Section 1, query notation; source_checked.
- Alias `subcube partition complexity`: [AKK16](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2016.4), Introduction, query complexity; source_checked.

Sources: [AIK26](https://arxiv.org/abs/2609.11664), [KLLPV26](https://arxiv.org/abs/2609.26757).

## UC0: 0-unambiguous certificate complexity

Symbol: `UC_0`. Definition status: source_checked.

Minimum maximum width of an unambiguous DNF for the complement of f.



Definition locator: KLLPV26 Definition 23.

- Alias `UC_0`: [AIK26](https://arxiv.org/abs/2609.11664), Section 2; source_checked.
- Alias `coUP^dt`: [GPW18](https://eccc.weizmann.ac.il/report/2015/050/revision/1/), Section 1, query notation; source_checked.

Sources: [AIK26](https://arxiv.org/abs/2609.11664), [KLLPV26](https://arxiv.org/abs/2609.26757).

## UC1: 1-unambiguous certificate complexity

Symbol: `UC_1`. Definition status: source_checked.

Minimum maximum width of an unambiguous DNF for f.



Definition locator: KLLPV26 Definition 23.

- Alias `UC_1`: [AIK26](https://arxiv.org/abs/2609.11664), Section 2; source_checked.
- Alias `UP^dt`: [GPW18](https://eccc.weizmann.ac.il/report/2015/050/revision/1/), Section 1, query notation; source_checked.
- Alias `one-sided subcube partition complexity`: [AKK16](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2016.4), Introduction, quantum query complexity; source_checked.
- Alias `UP^dt(f)`: [Goos15](https://eccc.weizmann.ac.il/report/2015/012/), Sections 1.1–2, pp.2–4; source_checked.

Sources: [AIK26](https://arxiv.org/abs/2609.11664), [KLLPV26](https://arxiv.org/abs/2609.26757).

## UCmin: minimum one-sided unambiguous certificate complexity

Symbol: `UC_min`. Definition status: source_checked.

min(UC_0,UC_1).



Definition locator: AIK26 Section 2, preliminary definitions.

- Alias `UC_min`: [AIK26](https://arxiv.org/abs/2609.11664), Section 2; source_checked.

Sources: [AIK26](https://arxiv.org/abs/2609.11664).

## deg: real exact polynomial degree

Symbol: `deg`. Definition status: source_checked.

Minimum degree of a real multilinear polynomial equal to f on its domain; for total functions the representing polynomial is unique.

 No condition off the promised domain; keep distinct from cubeBoundedDeg/cubeBoundedAdeg.

Definition locator: ABK16 Section 2.2, pp.7–8 (arXiv v2).

- Alias `deg`: [NS94](https://web.vu.lt/mif/s.jukna/boolean/Nisan-Szegedy.pdf), Definition 1.1; source_checked.
- Alias `Fourier degree`: [NS94](https://web.vu.lt/mif/s.jukna/boolean/Nisan-Szegedy.pdf), Definition 1.1; representation by real polynomials; source_checked.
- Alias `real degree`: [NS94](https://web.vu.lt/mif/s.jukna/boolean/Nisan-Szegedy.pdf), Definition 1.1; representation by real polynomials; definition_equivalence_checked_literal_name_pending.
- Alias `Fourier-degree`: [ABKBRT21](https://arxiv.org/abs/2010.12629), Section 2.3; source_checked.
- Alias `gdeg`: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Definition 2.11 and Remark 2.12; source_checked.

Sources: [NS94](https://web.vu.lt/mif/s.jukna/boolean/Nisan-Szegedy.pdf), [ABK16](https://arxiv.org/abs/1511.01937).

## adeg: approximate degree

Symbol: `\widetilde{deg}`. Definition status: source_checked.

Minimum real polynomial degree approximating the 0/1 output within 1/3 in absolute value on the domain.

 No condition off the promised domain; keep distinct from cubeBoundedDeg/cubeBoundedAdeg.

Definition locator: ABK16 Section 2.2, pp.7–8 (arXiv v2).

- Alias `\widetilde{deg}`: [ABK16](https://arxiv.org/abs/1511.01937), Section 2.2; source_checked.
- Alias `approximate polynomial degree`: [ABK16](https://arxiv.org/abs/1511.01937), Section 2.2; source_checked.
- Alias `tilde gdeg`: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Definition 2.11 and Remark 2.12; source_checked.

Sources: [ABK16](https://arxiv.org/abs/1511.01937).

## adeg_eps: error-parameterized approximate degree

Symbol: `\widetilde{deg}_epsilon`. Definition status: source_checked.

As adeg, with explicit error epsilon in [0,1/2); bounded versus unrestricted polynomial ranges must be recorded.

Theorem 18 uses bounded signed-range approximation; constants cannot be copied to another normalization. No condition off the promised domain; keep distinct from cubeBoundedDeg/cubeBoundedAdeg.

Definition locator: ABK16 Section 2.2, pp.7–8 (arXiv v2).

- Alias `\widetilde{deg}_epsilon`: [BT17](https://arxiv.org/abs/1703.05784), Section 2.1; source_checked.

Sources: [ABKBRT21](https://arxiv.org/abs/2010.12629), [ABK16](https://arxiv.org/abs/1511.01937).

## adeg_bounded: bounded-range approximate degree

Symbol: `\widetilde{deg}^{bounded}_epsilon`. Definition status: source_checked.

Minimum degree of q with 0<=q(x)<=epsilon on 0-inputs and 1-epsilon<=q(x)<=1 on 1-inputs. Equivalently, for signed target 2f-1 use 2q-1 in [-1,-1+2epsilon] and [1-2epsilon,1].

Repository-qualified symbol; source writes a tilde-degree symbol. Keep separate from unrestricted absolute-error degree.

Definition locator: ABKBRT21 Section 2.3.

- Alias `\widetilde{deg}_epsilon`: [ABKBRT21](https://arxiv.org/abs/2010.12629), Section 2.3; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `\widetilde{deg}^{bounded}_epsilon`: ABKBRT21; repository_display_not_a_historical_occurrence.

Sources: [ABKBRT21](https://arxiv.org/abs/2010.12629).

## lambda: spectral sensitivity

Symbol: `lambda`. Definition status: source_checked.

Spectral norm of the adjacency matrix of the sensitivity graph.

Koutsoupias K and the single-bit positive/negative adversary formulations equal lambda in ABKBRT21 Theorem 28. The square of K is the formula-size lower bound; do not confuse the squared normalization with K itself. On a promise domain, take only edges whose endpoints are both promised and have different outputs; a nonconstant promised function can have an empty sensitivity graph.

Definition locator: KLLPV26 Definition 32.

- Alias `lambda`: [ABKBRT21](https://arxiv.org/abs/2010.12629), Section 3; source_checked.
- Alias `K`: [ABKBRT21](https://arxiv.org/abs/2010.12629), Appendix A.1, Theorem 28; source_checked.
- Alias `Adv_1`: [ABKBRT21](https://arxiv.org/abs/2010.12629), Appendix A.1, Theorem 28; source_checked.
- Alias `Adv_1^{pm}`: [ABKBRT21](https://arxiv.org/abs/2010.12629), Appendix A.1, Theorem 28; source_checked.
- Alias `SA_1`: [ABKBRT21](https://arxiv.org/abs/2010.12629), Appendix A.1, Theorem 28; source_checked.
- Alias `SWA_1`: [ABKBRT21](https://arxiv.org/abs/2010.12629), Appendix A.1, Theorem 28; source_checked.
- Alias `MM_1`: [ABKBRT21](https://arxiv.org/abs/2010.12629), Appendix A.1, Theorem 28; source_checked.
- Alias `GSA_1`: [ABKBRT21](https://arxiv.org/abs/2010.12629), Appendix A.1, Theorem 28; source_checked.

Sources: [ABKBRT21](https://arxiv.org/abs/2010.12629), [KLLPV26](https://arxiv.org/abs/2609.26757).

## rdeg: exact rational degree

Symbol: `rdeg`. Definition status: source_checked.

Minimum max(deg p,deg q) such that p/q equals f on its domain and q is nonzero there.



Definition locator: KLLPV26 Definition 37.

- Alias `rational degree`: [IJKKSWW23](https://arxiv.org/abs/2310.08004), Introduction and definitions; source_checked.
- Alias `rdeg`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 37; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [IJKKSWW23](https://arxiv.org/abs/2310.08004), [KLLPV26](https://arxiv.org/abs/2609.26757).

## ndeg: nondeterministic polynomial degree

Symbol: `ndeg`. Definition status: source_checked.

Minimum degree of a real polynomial nonzero exactly on the 1-inputs.

Orientation matters. Extract precise original source and quantum nondeterminism characterization.

Definition locator: KLLPV26 Definition 36.

- Alias `ndeg`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 36; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [IJKKSWW23](https://arxiv.org/abs/2310.08004), [KLLPV26](https://arxiv.org/abs/2609.26757).

## AdvPlus: positive-weight adversary bound

Symbol: `Adv`. Definition status: source_checked.

Maximum ||Gamma||/max_i ||Gamma Hadamard D_i|| over nonzero symmetric entrywise nonnegative adversary matrices Gamma supported on pairs with different outputs; D_i[x,y]=1 iff x_i!=y_i. Norm is spectral norm. For a partial f matrices are indexed by its promised domain.

Adv without a superscript can mean the general adversary elsewhere; source-specific identification is mandatory.

Definition locator: ABKBRT21 Definition 8.

- Alias `Adv`: [BK19](https://arxiv.org/abs/1902.03660), Section 1.1; source_checked.
- Alias `positive adversary`: [BK19](https://arxiv.org/abs/1902.03660), Section 1.1; definition_equivalence_checked_literal_name_pending.
- Alias `MM`: [BK19](https://arxiv.org/abs/1902.03660), Section 1.1 and references to equivalent formulations; source_checked.
- Alias `SA`: [ABKBRT21](https://arxiv.org/abs/2010.12629), Definition 8; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [BK19](https://arxiv.org/abs/1902.03660), [ABKBRT21](https://arxiv.org/abs/2010.12629).

## AdvGeneral: general adversary bound

Symbol: `Adv^{\pm}`. Definition status: source_checked.

Maximum ||Gamma||/max_i ||Gamma o D_i|| over real symmetric matrices Gamma indexed by promised inputs, with Gamma_xy=0 whenever f(x)=f(y); D_i(x,y)=1 iff x_i!=y_i. Entries may be negative.

Negative entries are allowed. HLS07 supplies the original generalization and explicit error-dependent lower bound; LMRSS11 gives a tight characterization for finite input/output alphabets.

Definition locator: HLS07 Definition 2; LMRSS11 Definition 3.3.

- Alias `Adv^{\pm}`: [ABK16](https://arxiv.org/abs/1511.01937), Section 2; general-adversary characterization cited in Section 5; source_checked.
- Alias `negative-weight adversary bound`: [ABK16](https://arxiv.org/abs/1511.01937), Section 2; general-adversary characterization cited in Section 5; source_checked.
- Alias `ADV^{pm}`: [HLS07](https://arxiv.org/abs/quant-ph/0611054), Definition 2; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [ABK16](https://arxiv.org/abs/1511.01937), [HLS07](https://arxiv.org/abs/quant-ph/0611054), [LMRSS11](https://arxiv.org/abs/1011.3020v2).

## QD: quantum distinguishing complexity

Symbol: `QD`. Definition status: source_checked.

Minimum k for a k-query quantum algorithm producing states rho_x with trace distance at least 1/6 for every promised opposite-output pair x,y.

Trace distance is half the Schatten 1-norm. DQA is attributed to Barnum–Saks–Szegedy 2001 Remark 1 in Section 1.1; retain that historical attribution separately.

Definition locator: Definition 5, PDF p.7.

- Alias `QD`: [BK19](https://arxiv.org/abs/1902.03660), Definition 5, PDF p.7; source_checked.
- Alias `DQA`: [BK19](https://arxiv.org/abs/1902.03660), Definition 5, PDF p.7; source_checked.

Sources: [BK19](https://arxiv.org/abs/1902.03660).

## QSZK: quantum statistical-zero-knowledge query complexity

Symbol: `QSZK`. Definition status: source_checked.

Minimum total queries of two state-preparation algorithms producing rho_x,sigma_x with trace distance >=2/3 on 1-inputs and <=1/3 on 0-inputs.

This is the complete-problem-based state-distance definition, not an automatically identical interactive-protocol cost.

Definition locator: Definition 14, PDF p.12.

- Alias `QSZK`: [BK19](https://arxiv.org/abs/1902.03660), Definition 14, PDF p.12; source_checked.

Sources: [BK19](https://arxiv.org/abs/1902.03660).

## RS: randomized sabotage complexity

Symbol: `RS`. Definition status: source_checked.

R_0(f_sab): a sabotaged input is a partial assignment with blanks all marked * or all marked dagger, consistent with both a 0-input and a 1-input of f; output which marker occurs.

Zero-error expected queries. Oracle alphabet {0,1,*,dagger}; underlying f may be partial. Original definition: Ben-David–Kothari randomized query composition and sabotage complexity.

Definition locator: Definition 5.6.

- Alias `RS`: [CG22](https://arxiv.org/abs/2211.03396), Definition 5.6; source_checked.

Sources: [CG22](https://arxiv.org/abs/2211.03396).

## QS: weak-input quantum sabotage complexity

Symbol: `QS_{weak}`. Definition status: source_checked.

Bounded-error quantum queries to the sabotaged string alone, distinguishing * from dagger in the sabotage promise.

Do not identify with QD. BK19 suggests the name quantum sabotage for QD, whereas CMP24 studies four distinct sabotage oracle/output variants.

Definition locator: Section 2 and Definition 1.

- Alias `QS_{weak}`: [CMP24](https://arxiv.org/abs/2408.12595), Section 2 and Definition 1; source_checked.
- Alias `QS`: [CMP24](https://arxiv.org/abs/2408.12595), Section 1.1, before the four-model split; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [CMP24](https://arxiv.org/abs/2408.12595).

## CGpub: public-coin certificate game complexity

Symbol: `CG^{pub}`. Definition status: source_checked.

Inverse of the best worst-pair winning probability in the zero-communication game: x is a 0-input, y a 1-input, and players must output the same index i with x_i!=y_i. Strategies use a shared random distribution over deterministic output maps.

Possibly partial f. This is inverse probability, not its logarithm.

Definition locator: Definition 2.4.

- Alias `CG^{pub}`: [CG22](https://arxiv.org/abs/2211.03396), Definition 2.4; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [CG22](https://arxiv.org/abs/2211.03396).

## CGpriv: private-coin certificate game complexity

Symbol: `CG^{priv}`. Definition status: source_checked.

Inverse of the best worst-pair winning probability in the zero-communication game: x is a 0-input, y a 1-input, and players must output the same index i with x_i!=y_i. Strategies use independent randomized output maps.

Possibly partial f. This is inverse probability, not its logarithm.

Definition locator: Definition 2.3.

- Alias `CG^{priv}`: [CG22](https://arxiv.org/abs/2211.03396), Definition 2.3; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [CG22](https://arxiv.org/abs/2211.03396).

## CGent: entangled certificate game complexity

Symbol: `CG^*`. Definition status: source_checked.

Inverse of the best worst-pair winning probability in the zero-communication game: x is a 0-input, y a 1-input, and players must output the same index i with x_i!=y_i. Strategies use a fixed input-independent bipartite state and local measurements.

Possibly partial f. This is inverse probability, not its logarithm.

Definition locator: Definition 2.5.

- Alias `CG^*`: [CG22](https://arxiv.org/abs/2211.03396), Definition 2.5; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [CG22](https://arxiv.org/abs/2211.03396).

## CGns: nonsignaling certificate game complexity

Symbol: `CG^{ns}`. Definition status: source_checked.

Inverse of the best worst-pair winning probability in the zero-communication game: x is a 0-input, y a 1-input, and players must output the same index i with x_i!=y_i. Strategies use conditional output distributions whose marginals do not depend on the other input.

Possibly partial f. This is inverse probability, not its logarithm.

Definition locator: Definitions 2.1 and 2.6.

- Alias `CG^{ns}`: [CG22](https://arxiv.org/abs/2211.03396), Definitions 2.1 and 2.6; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [CG22](https://arxiv.org/abs/2211.03396).

## conical: two-sided approximate nonnegative degree for decision functions

Symbol: `\widetilde{deg}^{+2}`. Definition status: source_checked.

Minimum maximum conjunction width in nonnegative linear combinations {h_s} of conjunctions of literals, with sum_s h_s<=1 everywhere and sum_{s valid for x} h_s(x)>=2/3 on the promise. Here the valid output set is the singleton {f(x)}.



Definition locator: Definition 12, decision-function specialization.

- Alias `\widetilde{deg}^{+2}`: [BK24](https://arxiv.org/abs/2410.16245), Definition 12, decision-function specialization; source_checked.
- Alias `conical junta degree`: [BK24](https://arxiv.org/abs/2410.16245), Definition 12, decision-function specialization; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [BK24](https://arxiv.org/abs/2410.16245).

## rel_adeg: bounded approximate degree for relations

Symbol: `\widetilde{deg}`. Definition status: source_checked.

Minimum maximum degree of real polynomials {p_s}, one per output, with p_s(x)>=0 and sum_s p_s(x)<=1 on the entire cube, and sum_{s valid for x} p_s(x)>=1-epsilon on promised inputs.

Default epsilon=1/3. Positivity and normalization also hold off-promise. Single-output-function degree is a separate specialization.

Definition locator: Definition 10, PDF pp.11–12.

- Alias `\widetilde{deg}`: [BK24](https://arxiv.org/abs/2410.16245), Definition 10, PDF pp.11–12; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [BK24](https://arxiv.org/abs/2410.16245).

## Rexp: randomized query complexity in expectation

Symbol: `RE`. Definition status: source_checked.

Minimum worst-case query cap of a randomized algorithm outputting a nonnegative real variable whose expectation is f(x) on every input.

f maps the full cube to nonnegative reals. This is not expected running time.

Definition locator: Section 2.3 and Theorem 9.

- Alias `RE`: [KLW14](https://arxiv.org/abs/1411.7280), Section 2.3 and Theorem 9; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [KLW14](https://arxiv.org/abs/1411.7280).

## Qexp: quantum query complexity in expectation

Symbol: `QE`. Definition status: source_checked.

Quantum analogue of RE: output a nonnegative real variable with expectation f(x), minimizing worst-case oracle calls.

Source QE collides with exact quantum query complexity Q_E. Preserve the distinction by stable IDs.

Definition locator: Section 2.3 and Theorem 12.

- Alias `QE`: [KLW14](https://arxiv.org/abs/1411.7280), Section 2.3 and Theorem 12; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [KLW14](https://arxiv.org/abs/1411.7280).

## literaldeg: nonnegative literal degree

Symbol: `ldeg_+`. Definition status: source_checked.

Minimum d such that f is a nonnegative linear combination of conjunctions of at most d literals.



Definition locator: Section 2.3 and Theorem 9.

- Alias `ldeg_+`: [KLW14](https://arxiv.org/abs/1411.7280), Section 2.3 and Theorem 9; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [KLW14](https://arxiv.org/abs/1411.7280).

## sosdeg: sum-of-squares degree

Symbol: `deg_sos`. Definition status: source_checked.

Minimum d such that f(x)=sum_j p_j(x)^2 on the cube with every real p_j of degree <=d.

The roots have degree d; the sum of squares has formal degree at most 2d. Other SOS conventions count 2d.

Definition locator: Section 2.3 and Theorem 12.

- Alias `deg_sos`: [KLW14](https://arxiv.org/abs/1411.7280), Section 2.3 and Theorem 12; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [KLW14](https://arxiv.org/abs/1411.7280).

## psR: pseudo-deterministic randomized classical query complexity

Symbol: `psR`. Definition status: source_checked.

Minimum worst-case query cap of a randomized classical algorithm for a relation S, for which there exists a fixed valid selector g with Pr[A(x)=g(x)]>=2/3 for every promised input.

The canonical selector may depend on the algorithm, but cannot depend on its random coins or measurement outcomes.

Definition locator: Definitions 2.1–2.2.

- Alias `psR`: [AGL26](https://doi.org/10.4230/LIPIcs.ICALP.2026.3), Definitions 2.1–2.2; source_checked.
- Alias `psD^dt`: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2: decision-tree and pseudo-deterministic definitions; source_checked.
- Alias `psP^dt`: [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36), Theorem 4 and Section 2; source_checked.

Sources: [AGL26](https://doi.org/10.4230/LIPIcs.ICALP.2026.3), [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36).

## psQ: pseudo-deterministic quantum query complexity

Symbol: `psQ`. Definition status: source_checked.

Minimum worst-case query cap of a quantum algorithm for a relation S, for which there exists a fixed valid selector g with Pr[A(x)=g(x)]>=2/3 for every promised input.

The canonical selector may depend on the algorithm, but cannot depend on its random coins or measurement outcomes.

Definition locator: Definitions 2.1–2.2.

- Alias `psQ`: [AGL26](https://doi.org/10.4230/LIPIcs.ICALP.2026.3), Definitions 2.1–2.2; source_checked.
- Alias `psQ^dt`: [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36), Theorem 4 and Section 2; source_checked.

Sources: [AGL26](https://doi.org/10.4230/LIPIcs.ICALP.2026.3), [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36).

## blocknumber: block number

Symbol: `N_bs`. Definition status: source_checked.

Maximum over x of the number of inclusion-minimal sensitive blocks of f at x.

KT13 Section 5 uses nbs. The size-ell version counts blocks of size at most ell in CG26, unlike exact-size nbs_k in KT13.

Definition locator: Definitions 3–4.

- Alias `N_b`: [CG26](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.61), Definitions 3–4; source_checked.
- Alias `nbs`: [CG26](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.61), Definitions 3–4; source_checked.
- Alias `#bs`: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Definition 2.4; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [CG26](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.61), [CDMRS23](https://doi.org/10.1145/3564246.3585199).

## bricknumber: brick number

Symbol: `N_{br}`. Definition status: source_checked.

Maximum over x of the number of nonempty blocks B such that f(x^B)!=f(x^(B minus {i})) for every i in B.

A brick need not itself be a sensitive block when |B|>1. Do not replace the defining condition by minimal sensitivity.

Definition locator: Definitions 7–8.

- Alias `N_{br}`: [CG26](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.61), Definitions 7–8; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [CG26](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.61).

## rel_conical: two-sided approximate nonnegative degree for relations

Symbol: `\widetilde{deg}^{+2}`. Definition status: source_checked.

Minimum maximum conjunction width in nonnegative linear combinations {h_s} of conjunctions of literals, with sum_s h_s<=1 everywhere and sum_{s valid for x} h_s(x)>=2/3 on the promise.



Definition locator: Definition 12.

- Alias `\widetilde{deg}^{+2}`: [BK24](https://arxiv.org/abs/2410.16245), Definition 12; source_checked.
- Alias `conical junta degree`: [BK24](https://arxiv.org/abs/2410.16245), Definition 12; source_checked.
- Alias `two-sided conical junta degree`: [BK24](https://arxiv.org/abs/2410.16245), Definition 12; source_checked.

Sources: [BK24](https://arxiv.org/abs/2410.16245).

## mbs: monotone block sensitivity

Symbol: `mbs`. Definition status: source_checked.

For each x, fix every coordinate in supp(x) to 1 and let f_x be the function of the remaining coordinates. Take the block sensitivity of f_x at its all-zero input, then maximize over x.

Defined for arbitrary total f. This is not merely ordinary complexity restricted to monotone f. CDM23 also defines this input-directed quantity for promised and multi-output functions, requiring the flipped input to remain promised.

Definition locator: Definitions 5–8.

- Alias `mbs`: [BJKM24](https://arxiv.org/abs/2406.07859), Definitions 5–8; source_checked.
- Alias `bs_0`: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2, lines 235–245; source_checked.
- Alias `bs_0`: [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), Section 2: directed sensitivity definitions; source_checked.
- Alias `MBS`: [KLMY21](https://doi.org/10.1145/3406325.3450999), Section 2.1; source_checked.
- Alias `bs^{0→1}`: [CDM25](https://doi.org/10.1007/s00037-025-00266-7), Section 2 and Theorem 6.1; source_checked.

Sources: [BJKM24](https://arxiv.org/abs/2406.07859), [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), [KLMY21](https://doi.org/10.1145/3406325.3450999).

## fmbs: fractional monotone block sensitivity

Symbol: `fmbs`. Definition status: source_checked.

For each x, fix every coordinate in supp(x) to 1 and let f_x be the function of the remaining coordinates. Take the fractional block sensitivity of f_x at its all-zero input, then maximize over x.

Defined for arbitrary total f. This is not merely ordinary complexity restricted to monotone f.

Definition locator: Definitions 5–8.

- Alias `fmbs`: [BJKM24](https://arxiv.org/abs/2406.07859), Definitions 5–8; source_checked.
- Alias `FHSC_0`: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Definition 2.6; source_checked.
- Alias `FHSC`: [KLMY21](https://doi.org/10.1145/3406325.3450999), Definition 2.13; source_checked.
- Alias `FMBS`: [KLMY21](https://doi.org/10.1145/3406325.3450999), Section 2.1; source_checked.

Sources: [BJKM24](https://arxiv.org/abs/2406.07859), [CDMRS23](https://doi.org/10.1145/3564246.3585199), [KLMY21](https://doi.org/10.1145/3406325.3450999).

## MCC: monotone certificate complexity

Symbol: `MCC`. Definition status: source_checked.

For each x, fix every coordinate in supp(x) to 1 and let f_x be the function of the remaining coordinates. Take the certificate complexity of f_x at its all-zero input, then maximize over x.

Defined for arbitrary total f. This is not merely ordinary complexity restricted to monotone f.

Definition locator: Definitions 5–8.

- Alias `MCC`: [BJKM24](https://arxiv.org/abs/2406.07859), Definitions 5–8; source_checked.
- Alias `hitting set complexity`: [BJKM24](https://arxiv.org/abs/2406.07859), Definitions 5–8; source_checked.
- Alias `HSC_0`: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Definition 2.5; source_checked.
- Alias `HSC`: [KLMY21](https://doi.org/10.1145/3406325.3450999), Definition 2.10; source_checked.

Sources: [BJKM24](https://arxiv.org/abs/2406.07859), [CDMRS23](https://doi.org/10.1145/3564246.3585199), [KLMY21](https://doi.org/10.1145/3406325.3450999).

## ms: monotone sensitivity

Symbol: `ms`. Definition status: source_checked.

For each x, fix every coordinate in supp(x) to 1 and let f_x be the function of the remaining coordinates. Take the sensitivity of f_x at its all-zero input, then maximize over x.

Defined for arbitrary total f. This is not merely ordinary complexity restricted to monotone f. CDM23 also defines this input-directed quantity for promised and multi-output functions, requiring the flipped input to remain promised.

Definition locator: Definitions 5–8.

- Alias `ms`: [BJKM24](https://arxiv.org/abs/2406.07859), Definitions 5–8; source_checked.
- Alias `s_0`: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2, lines 235–245; source_checked.
- Alias `s_0`: [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), Section 2: directed sensitivity definitions; source_checked.

Sources: [BJKM24](https://arxiv.org/abs/2406.07859), [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34).

## DTSize: decision tree leaf size

Symbol: `DTSize`. Definition status: source_checked.

Minimum number of leaves of a deterministic bit-query tree computing f.



Definition locator: DM23 Section 2, Decision trees.

- Alias `DTSize`: [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 2; source_checked.
- Alias `DSize^dt`: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2: decision-tree and pseudo-deterministic definitions; source_checked.

Sources: [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/).

## DTRank: decision tree rank

Symbol: `Rank`. Definition status: source_checked.

Minimum Strahler rank: leaves have rank 0; unequal child ranks give their maximum, equal child ranks give that rank plus 1.



Definition locator: DM23 Section 2, Decision Tree Rank, PDF p.7.

- Alias `Rank`: [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 2; source_checked.
- Alias `Strahler number`: [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 1; source_checked.
- Alias `Horton-Strahler number`: [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 1; source_checked.
- Alias `tree rank`: [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 1; source_checked.
- Alias `rank`: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Definition 2.10; source_checked.
- Alias `rank`: [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Definition 3; source_checked.
- Alias `r(f)`: [EH89](https://doi.org/10.1016/0890-5401(89)90001-1), Definition p.241; source_checked.

Sources: [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), [CDMRS23](https://doi.org/10.1145/3564246.3585199), [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15).

## sparsity: Fourier sparsity

Symbol: `spar`. Definition status: source_checked.

Number of nonzero coefficients in f=sum_S fhat(S) (-1)^(sum_{i in S} x_i), including the empty-set coefficient.



Definition locator: Section 2, Fourier representation, PDF p.6.

- Alias `spar`: [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 2, Fourier representation, PDF p.6; source_checked.

Sources: [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf).

## ANDD: conjunctive decision tree depth

Symbol: `Conj`. Definition status: source_checked.

Minimum worst-case number of queries in a decision tree whose internal nodes query conjunctions of literals, allowing both positive and negated variables.

The original seed incorrectly restricted queries to monotone conjunctions. Corrected from the full paper.

Definition locator: DM23 Section 7.2.

- Alias `D_wedge`: [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 7, AND-decision tree model; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf).

## IC: query instance complexity

Symbol: `InstC`. Definition status: source_checked.

Minimum over deterministic decision trees T computing nonconstant f of max_x T(x)/C(f,x).

Competitive ratio. Constant functions require a separate zero-denominator convention; source results involving them are stated separately.

Definition locator: Definition 2.3.

- Alias `InstC`: [LM26](https://dmtcs.episciences.org/en/articles/18512), Definition 2.3; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [LM26](https://dmtcs.episciences.org/en/articles/18512).

## hazardD: deterministic u-query complexity

Symbol: `D_u`. Definition status: source_checked.

Minimum depth of a ternary decision tree computing the hazard-free extension. For a Boolean f, its extension maps z in {0,u,1}^n to b if every Boolean resolution of z has value b, and to u otherwise.

Input and output alphabets are ternary. The symbol u is a queried value, distinct from an unrevealed coordinate.

Definition locator: Definition 2.1.

- Alias `D_u`: [BKMNSS25](https://arxiv.org/abs/2507.00148), Definition 2.1; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [BKMNSS25](https://arxiv.org/abs/2507.00148).

## hazardR: randomized u-query complexity

Symbol: `R_u`. Definition status: source_checked.

Minimum worst-case query cap with error <=1/3 for the hazard-free extension. For a Boolean f, its extension maps z in {0,u,1}^n to b if every Boolean resolution of z has value b, and to u otherwise.

Input and output alphabets are ternary. The symbol u is a queried value, distinct from an unrevealed coordinate.

Definition locator: Definition 2.5.

- Alias `R_u`: [BKMNSS25](https://arxiv.org/abs/2507.00148), Definition 2.5; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [BKMNSS25](https://arxiv.org/abs/2507.00148).

## hazardQ: quantum u-query complexity

Symbol: `Q_u`. Definition status: source_checked.

Minimum bounded-error queries to |i,b,w> -> |i,b+x_i mod 3,w>, encoding u as 2, for the hazard-free extension. For a Boolean f, its extension maps z in {0,u,1}^n to b if every Boolean resolution of z has value b, and to u otherwise.

Input and output alphabets are ternary. The symbol u is a queried value, distinct from an unrevealed coordinate.

Definition locator: Definition 2.6.

- Alias `Q_u`: [BKMNSS25](https://arxiv.org/abs/2507.00148), Definition 2.6; source_checked.

Earlier seed attributions corrected; see `alias_attribution_history` in the source JSON.

Sources: [BKMNSS25](https://arxiv.org/abs/2507.00148).

## rdeg_eps: approximate rational degree

Symbol: `rdeg_epsilon`. Definition status: source_checked.

Minimum max(deg p,deg q) with q nonzero on the domain and |p(x)/q(x)-f(x)|<=epsilon throughout the domain.

Explicit error and denominator nonvanishing condition; no off-promise bound is imposed here.

Definition locator: Introduction and Section 2.

- Alias `rdeg_epsilon`: [IJKKSWW23](https://arxiv.org/abs/2310.08004), Introduction and Section 2; source_checked.

Sources: [IJKKSWW23](https://arxiv.org/abs/2310.08004).

## PostQ: postselected bounded-error quantum query complexity

Symbol: `PostQ_epsilon`. Definition status: source_checked.

Minimum quantum queries allowing a postselection event of nonzero probability on every promised input, with conditional output error at most epsilon.

The postselection success probability need not be inverse polynomial.

Definition locator: Section 2, postselection definitions.

- Alias `PostQ_epsilon`: [IJKKSWW23](https://arxiv.org/abs/2310.08004), Section 2, postselection definitions; source_checked.

Sources: [IJKKSWW23](https://arxiv.org/abs/2310.08004).

## PostQE: exact postselected quantum query complexity

Symbol: `PostQ_E`. Definition status: source_checked.

Postselected quantum query complexity with zero conditional error and positive postselection probability on every promised input.

Exact conditioned output; not zero-error quantum query complexity Q_0.

Definition locator: Section 2 and Appendix A.

- Alias `PostQ_E`: [IJKKSWW23](https://arxiv.org/abs/2310.08004), Section 2 and Appendix A; source_checked.
- Alias `PostEQP query complexity`: [IJKKSWW23](https://arxiv.org/abs/2310.08004), Section 2 and Appendix A; source_checked.

Sources: [IJKKSWW23](https://arxiv.org/abs/2310.08004).

## QSweakIndex: quantum sabotage complexity (QSweakIndex)

Symbol: `QS^{ind}_{weak}`. Definition status: source_checked.

Weak input, but output both the marker type and an index containing it.

All component input queries count; source access conventions retained.

Definition locator: Section 2; four-variant definitions.

- Alias `QS^{ind}_{weak}`: [CMP24](https://arxiv.org/abs/2408.12595), Section 2; four-variant definitions; source_checked.

Sources: [CMP24](https://arxiv.org/abs/2408.12595).

## QSstrong: quantum sabotage complexity (QSstrong)

Symbol: `QS_{str}`. Definition status: source_checked.

Strong input: also query the underlying opposite-output pair x,y; only determine the marker type.

All component input queries count; source access conventions retained.

Definition locator: Section 2; four-variant definitions.

- Alias `QS_{str}`: [CMP24](https://arxiv.org/abs/2408.12595), Section 2; four-variant definitions; source_checked.

Sources: [CMP24](https://arxiv.org/abs/2408.12595).

## QSstrongIndex: quantum sabotage complexity (QSstrongIndex)

Symbol: `QS^{ind}_{str}`. Definition status: source_checked.

Strong input: also query x,y and output the marker type and a differing index.

All component input queries count; source access conventions retained.

Definition locator: Section 2; four-variant definitions.

- Alias `QS^{ind}_{str}`: [CMP24](https://arxiv.org/abs/2408.12595), Section 2; four-variant definitions; source_checked.

Sources: [CMP24](https://arxiv.org/abs/2408.12595).

## CGpubSingle: single-bit public-coin certificate game complexity

Symbol: `CG^{pub}_{[1]}`. Definition status: source_checked.

Inverse of the best worst-pair winning probability in the zero-communication game: x is a 0-input, y a 1-input, and players must output the same index i with x_i!=y_i. Strategies use a shared random distribution over deterministic output maps. Only pairs with Hamming distance one are allowed.



Definition locator: Section 8, Theorems 8.4 and 8.8.

- Alias `CG^{pub}_{[1]}`: [CG22](https://arxiv.org/abs/2211.03396), Section 8, Theorems 8.4 and 8.8; source_checked.

Sources: [CG22](https://arxiv.org/abs/2211.03396).

## CGprivSingle: single-bit private-coin certificate game complexity

Symbol: `CG^{priv}_{[1]}`. Definition status: source_checked.

Inverse of the best worst-pair winning probability in the zero-communication game: x is a 0-input, y a 1-input, and players must output the same index i with x_i!=y_i. Strategies use independent randomized output maps. Only pairs with Hamming distance one are allowed.



Definition locator: Section 8, Theorems 8.4 and 8.8.

- Alias `CG^{priv}_{[1]}`: [CG22](https://arxiv.org/abs/2211.03396), Section 8, Theorems 8.4 and 8.8; source_checked.

Sources: [CG22](https://arxiv.org/abs/2211.03396).

## CAdv: classical adversary bound

Symbol: `CAdv`. Definition status: source_checked.

Minimum max_x sum_i m_x(i) over nonnegative weights with sum_{i:x_i!=y_i} min(m_x(i),m_y(i))>=1 for every opposite-output promised pair.

CG22 Definition 4.2 uses probability-normalized CMM; its equivalent normalization is recorded. Total-function CAdv=FC does not extend to all partial functions.

Definition locator: Definition 14.

- Alias `CAdv`: [BK24](https://arxiv.org/abs/2410.16245), Definition 14; source_checked.
- Alias `CMM`: [BK24](https://arxiv.org/abs/2410.16245), Definition 14; source_checked.

Sources: [BK24](https://arxiv.org/abs/2410.16245).

## EC: expectational certificate complexity

Symbol: `EC`. Definition status: source_checked.

Minimum max_x sum_i w_xi, with 0<=w_xi<=1 and sum_{i:x_i!=y_i} w_xi w_yi>=1 for every opposite-output pair.

The source extends this definition to partial functions. Distinct from randomized query complexity in expectation.

Definition locator: Definition 4.5.

- Alias `EC`: [CG22](https://arxiv.org/abs/2211.03396), Definition 4.5; source_checked.

Sources: [CG22](https://arxiv.org/abs/2211.03396).

## rel_udeg: promise-only approximate degree for relations

Symbol: `\widetilde{udeg}`. Definition status: source_checked.

Minimum maximum degree of real polynomials {p_s}, one per output, with p_s(x)>=0 and sum_s p_s(x)<=1 on the promised domain, and sum_{s valid for x} p_s(x)>=1-epsilon on promised inputs.

No off-promise boundedness. Do not conflate with bounded relation degree.

Definition locator: Definition 11.

- Alias `\widetilde{udeg}`: [BK24](https://arxiv.org/abs/2410.16245), Definition 11; source_checked.

Sources: [BK24](https://arxiv.org/abs/2410.16245).

## rel_deg: exact bounded polynomial degree for relations

Symbol: `deg`. Definition status: source_checked.

Minimum maximum degree of real polynomials {p_s}, one per output, with p_s(x)>=0 and sum_s p_s(x)<=1 on the entire cube, and sum_{s valid for x} p_s(x)>=1 on promised inputs.



Definition locator: Definition 10, epsilon=0.

- Alias `deg`: [BK24](https://arxiv.org/abs/2410.16245), Definition 10, epsilon=0; source_checked.

Sources: [BK24](https://arxiv.org/abs/2410.16245).

## rel_Adv: relation positive adversary bound

Symbol: `Adv`. Definition status: source_checked.

Minimum max_x sum_i m_x(i), with nonnegative m and sum_{i:x_i!=y_i} sqrt(m_x(i)m_y(i))>=1 whenever the valid-output sets for x,y are disjoint.



Definition locator: Definition 13.

- Alias `Adv`: [BK24](https://arxiv.org/abs/2410.16245), Definition 13; source_checked.

Sources: [BK24](https://arxiv.org/abs/2410.16245).

## rel_CAdv: relation classical adversary bound

Symbol: `CAdv`. Definition status: source_checked.

Minimum max_x sum_i m_x(i), with nonnegative m and sum_{i:x_i!=y_i} min(m_x(i),m_y(i))>=1 whenever the valid-output sets for x,y are disjoint.



Definition locator: Definition 14.

- Alias `CAdv`: [BK24](https://arxiv.org/abs/2410.16245), Definition 14; source_checked.

Sources: [BK24](https://arxiv.org/abs/2410.16245).

## rel_bs: relation block sensitivity

Symbol: `bs`. Definition status: source_checked.

Maximum number of pairwise disjoint blocks B at an input x such that f(x) and f(x^B) have disjoint valid-output sets. Maximize over promised x.



Definition locator: Definition 15.

- Alias `bs`: [BK24](https://arxiv.org/abs/2410.16245), Definition 15; source_checked.

Sources: [BK24](https://arxiv.org/abs/2410.16245).

## rel_cbs: critical block sensitivity

Symbol: `cbs`. Definition status: source_checked.

Minimum over single-valued completions g(x) in f(x) of max bs_x(g) over critical inputs x with exactly one valid output.

 The maximum over an empty critical-input set is taken to be zero; a relation with no singleton valid-output set can therefore have critical measure zero.

Definition locator: Definition 16.

- Alias `cbs`: [BK24](https://arxiv.org/abs/2410.16245), Definition 16; source_checked.

Sources: [BK24](https://arxiv.org/abs/2410.16245).

## rel_fbs: relation fractional block sensitivity

Symbol: `fbs`. Definition status: source_checked.

Fractional packing of the sensitive blocks from relation block sensitivity, with total weight through each coordinate at most one; maximize over x.



Definition locator: Definition 17.

- Alias `fbs`: [BK24](https://arxiv.org/abs/2410.16245), Definition 17; source_checked.

Sources: [BK24](https://arxiv.org/abs/2410.16245).

## rel_fcbs: fractional critical block sensitivity

Symbol: `fcbs`. Definition status: source_checked.

Minimum over single-valued completions g(x) in f(x) of max fbs_x(g) over critical inputs x with exactly one valid output.

 The maximum over an empty critical-input set is taken to be zero; a relation with no singleton valid-output set can therefore have critical measure zero.

Definition locator: Definition 17.

- Alias `fcbs`: [BK24](https://arxiv.org/abs/2410.16245), Definition 17; source_checked.

Sources: [BK24](https://arxiv.org/abs/2410.16245).

## blocknumber_l: bounded-size block number

Symbol: `N_bs^ell`. Definition status: source_checked.

Maximum over x of the number of inclusion-minimal sensitive blocks of cardinality at most ell.



Definition locator: Definition 4.

- Alias `N_b^{ell}`: [CG26](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.61), Definition 4; source_checked.

Sources: [CG26](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.61).

## bricknumber_l: bounded-size brick number

Symbol: `N_{br}^{ell}`. Definition status: source_checked.

Brick number restricted to blocks of size at most ell.



Definition locator: Definition 8.

- Alias `N_{br}^{ell}`: [CG26](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.61), Definition 8; source_checked.

Sources: [CG26](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.61).

## sparsityNonempty: nonconstant Fourier sparsity

Symbol: `\widetilde{spar}`. Definition status: source_checked.

Number of nonzero Fourier coefficients indexed by nonempty S.



Definition locator: Section 2, Fourier representation, PDF p.6.

- Alias `\widetilde{spar}`: [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 2, Fourier representation, PDF p.6; source_checked.

Sources: [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf).

## Cmin: minimum certificate complexity

Symbol: `C_min`. Definition status: source_checked.

min_x C(f,x), equivalently minimum codimension of a monochromatic subcube.

K in DM23 is unrelated to the Koutsoupias spectral-sensitivity alias K.

Definition locator: Definition 2.2.

- Alias `C_min`: [LM26](https://dmtcs.episciences.org/en/articles/18512), Definition 2.2; source_checked.
- Alias `subcube kill number`: [LM26](https://dmtcs.episciences.org/en/articles/18512), Definition 2.2; source_checked.
- Alias `K`: [LM26](https://dmtcs.episciences.org/en/articles/18512), Definition 2.2; source_checked.

Sources: [LM26](https://dmtcs.episciences.org/en/articles/18512).

## hazardS: u-sensitivity

Symbol: `s_u`. Definition status: source_checked.

Maximum over ternary inputs of the number of coordinates admitting a replacement that changes the hazard-free output. For a Boolean f, its extension maps z in {0,u,1}^n to b if every Boolean resolution of z has value b, and to u otherwise.

Input and output alphabets are ternary. The symbol u is a queried value, distinct from an unrevealed coordinate.

Definition locator: Definition 2.2.

- Alias `s_u`: [BKMNSS25](https://arxiv.org/abs/2507.00148), Definition 2.2; source_checked.

Sources: [BKMNSS25](https://arxiv.org/abs/2507.00148).

## hazardBS: u-block sensitivity

Symbol: `bs_u`. Definition status: source_checked.

Maximum number of disjoint coordinate sets, each admitting a replacement that changes the hazard-free output. For a Boolean f, its extension maps z in {0,u,1}^n to b if every Boolean resolution of z has value b, and to u otherwise.

Input and output alphabets are ternary. The symbol u is a queried value, distinct from an unrevealed coordinate.

Definition locator: Definition 2.3.

- Alias `bs_u`: [BKMNSS25](https://arxiv.org/abs/2507.00148), Definition 2.3; source_checked.

Sources: [BKMNSS25](https://arxiv.org/abs/2507.00148).

## hazardC: u-certificate complexity

Symbol: `cc_u`. Definition status: source_checked.

Maximum minimum number of revealed ternary coordinates fixing the hazard-free output among all consistent ternary completions. For a Boolean f, its extension maps z in {0,u,1}^n to b if every Boolean resolution of z has value b, and to u otherwise.

Input and output alphabets are ternary. The symbol u is a queried value, distinct from an unrevealed coordinate.

Definition locator: Definition 2.4.

- Alias `cc_u`: [BKMNSS25](https://arxiv.org/abs/2507.00148), Definition 2.4; source_checked.

Sources: [BKMNSS25](https://arxiv.org/abs/2507.00148).

## Qnegligent: noisy quantum query complexity (Qnegligent)

Symbol: `Q^{neg}_{p,epsilon}`. Definition status: source_checked.

Minimum queries to the channel (1-p) O_x rho O_x^dagger + p rho, succeeding with probability >=1-epsilon.

Fix p and epsilon explicitly; query-index dephasing differs from oracle negligence.

Definition locator: Section 1, equations (1.4) and (1.6).

- Alias `Q^{neg}_{p,epsilon}`: [ARS26](https://arxiv.org/abs/2610.00506), Section 1, equations (1.4) and (1.6); source_checked.

Sources: [ARS26](https://arxiv.org/abs/2610.00506).

## Qdephasing: noisy quantum query complexity (Qdephasing)

Symbol: `Q^{deph}_{p,epsilon}`. Definition status: source_checked.

Minimum queries to the bit oracle followed by complete dephasing of its index register independently with probability p, succeeding with probability >=1-epsilon.

Fix p and epsilon explicitly; query-index dephasing differs from oracle negligence.

Definition locator: Section 1, equations (1.4) and (1.6).

- Alias `Q^{deph}_{p,epsilon}`: [ARS26](https://arxiv.org/abs/2610.00506), Section 1, equations (1.4) and (1.6); source_checked.

Sources: [ARS26](https://arxiv.org/abs/2610.00506).

## cubeBoundedDeg: globally bounded exact polynomial degree

Symbol: `deg`. Definition status: source_checked.

Minimum real multilinear degree of p agreeing with f on its domain and satisfying 0<=p<=1 on the entire Boolean cube.

For partial f this differs from unrestricted exact degree. The source uses the same symbol deg; the stable ID distinguishes them.

Definition locator: Definition 7.

- Alias `deg`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 7; source_checked.
- Alias `deg`: [AB23](https://doi.org/10.4230/LIPIcs.CCC.2023.24), Section 2.1; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757), [AB23](https://doi.org/10.4230/LIPIcs.CCC.2023.24).

## cubeBoundedAdeg: globally bounded approximate polynomial degree

Symbol: `\widetilde{deg}`. Definition status: source_checked.

Minimum degree of p in [0,1] on the whole cube with |p-f|<=1/3 on the promised domain.



Definition locator: Definition 7.

- Alias `\widetilde{deg}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 7; source_checked.
- Alias `tilde deg`: [AB23](https://doi.org/10.4230/LIPIcs.CCC.2023.24), Section 2.1; definition_convention_checked_not_literal_alias.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757), [AB23](https://doi.org/10.4230/LIPIcs.CCC.2023.24).

## boundedPolyDelta: asymmetric bounded polynomial degree

Symbol: `Delta_{epsilon0,epsilon1,beta}`. Definition status: source_checked.

Minimum multilinear degree of p in [0,beta] on the entire cube, approximating 0-inputs within epsilon0 and 1-inputs within epsilon1.

All three parameters are explicit.

Definition locator: Definition 7.

- Alias `Delta_{epsilon0,epsilon1,beta}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 7; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## osdeg0: one-sided bounded polynomial degree (osdeg0)

Symbol: `\widehat{osdeg}^0`. Definition status: source_checked.

Delta_{1/3,0,1}(f): globally [0,1]-bounded polynomial with error only on the indicated output side.



Definition locator: Definition 7.

- Alias `\widehat{osdeg}^0`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 7; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## osdeg1: one-sided bounded polynomial degree (osdeg1)

Symbol: `\widehat{osdeg}^1`. Definition status: source_checked.

Delta_{0,1/3,1}(f): globally [0,1]-bounded polynomial with error only on the indicated output side.



Definition locator: Definition 7.

- Alias `\widehat{osdeg}^1`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 7; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## osdeg: two-orientation one-sided bounded polynomial degree

Symbol: `\widehat{osdeg}`. Definition status: source_checked.

max(osdeg0,osdeg1).

Distinct from one-sided approximation notions allowing unbounded values on the other side.

Definition locator: Definition 7.

- Alias `\widehat{osdeg}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 7; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## bmAdeg: block-multilinear bounded approximate degree

Symbol: `\widehat{bm-deg}`. Definition status: source_checked.

Minimum d for a degree-d block-multilinear real polynomial P on d independent blocks of n+1 signed variables, each monomial containing exactly one variable from each block, such that |P(z)|<=1 on all independent signed block inputs; on promised diagonal inputs x, 0<=P((1,x),...,(1,x))<=1 and |P((1,x),...,(1,x))-f(x)|<=1/3. The target f is 0/1-valued.

Source error/encoding follows Definition 38. Each monomial uses exactly one variable from each block.

Definition locator: Definition 38.

- Alias `\widehat{bm-deg}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 38; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## D_cert: certification of deterministic query complexity

Symbol: `D^{cert}`. Definition status: source_checked.

max_z deterministic query complexity of the partial decision problem accepting z and rejecting all x with f(x)!=f(z).

The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.

Definition locator: Definitions 1–2 and corresponding Theorems 3–12.

- Alias `D^{cert}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## R_cert: certification of bounded-error randomized query complexity

Symbol: `R^{cert}`. Definition status: source_checked.

max_z bounded-error randomized query complexity of the partial decision problem accepting z and rejecting all x with f(x)!=f(z).

The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.

Definition locator: Definitions 1–2 and corresponding Theorems 3–12.

- Alias `R^{cert}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## R0_cert: certification of zero-error randomized query complexity

Symbol: `R_0^{cert}`. Definition status: source_checked.

max_z zero-error randomized query complexity of the partial decision problem accepting z and rejecting all x with f(x)!=f(z).

The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.

Definition locator: Definitions 1–2 and corresponding Theorems 3–12.

- Alias `R_0^{cert}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## QE_cert: certification of exact quantum query complexity

Symbol: `Q_E^{cert}`. Definition status: source_checked.

max_z exact quantum query complexity of the partial decision problem accepting z and rejecting all x with f(x)!=f(z).

The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.

Definition locator: Definitions 1–2 and corresponding Theorems 3–12.

- Alias `Q_E^{cert}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## Q0_cert: certification of zero-error quantum query complexity

Symbol: `Q_0^{cert}`. Definition status: source_checked.

max_z zero-error quantum query complexity of the partial decision problem accepting z and rejecting all x with f(x)!=f(z).

The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.

Definition locator: Definitions 1–2 and corresponding Theorems 3–12.

- Alias `Q_0^{cert}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## Q_cert: certification of bounded-error quantum query complexity

Symbol: `Q^{cert}`. Definition status: source_checked.

max_z bounded-error quantum query complexity of the partial decision problem accepting z and rejecting all x with f(x)!=f(z).

The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.

Definition locator: Definitions 1–2 and corresponding Theorems 3–12.

- Alias `Q^{cert}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## QD_cert: certification of quantum distinguishing complexity

Symbol: `QD^{cert}`. Definition status: source_checked.

max_z quantum distinguishing complexity of the partial decision problem accepting z and rejecting all x with f(x)!=f(z).

The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.

Definition locator: Definitions 1–2 and corresponding Theorems 3–12.

- Alias `QD^{cert}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## AdvPlus_cert: certification of positive-weight adversary bound

Symbol: `Adv^{cert}`. Definition status: source_checked.

max_z positive-weight adversary bound of the partial decision problem accepting z and rejecting all x with f(x)!=f(z).

The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.

Definition locator: Definitions 1–2 and corresponding Theorems 3–12.

- Alias `Adv^{cert}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## RS_cert: certification of randomized sabotage complexity

Symbol: `RS^{cert}`. Definition status: source_checked.

max_z randomized sabotage complexity of the partial decision problem accepting z and rejecting all x with f(x)!=f(z).

The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.

Definition locator: Definitions 1–2 and corresponding Theorems 3–12.

- Alias `RS^{cert}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## QS_cert: certification of weak-input quantum sabotage complexity

Symbol: `QS_{weak}^{cert}`. Definition status: source_checked.

max_z weak-input quantum sabotage complexity of the partial decision problem accepting z and rejecting all x with f(x)!=f(z).

The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.

Definition locator: Definitions 1–2 and corresponding Theorems 3–12.

- Alias `QS_{weak}^{cert}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## EC_cert: certification of expectational certificate complexity

Symbol: `EC^{cert}`. Definition status: source_checked.

max_z expectational certificate complexity of the partial decision problem accepting z and rejecting all x with f(x)!=f(z).

The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.

Definition locator: Definitions 1–2 and corresponding Theorems 3–12.

- Alias `EC^{cert}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## UC_cert: certification of unambiguous certificate complexity

Symbol: `UC^{cert}`. Definition status: source_checked.

max_z unambiguous certificate complexity of the partial decision problem accepting z and rejecting all x with f(x)!=f(z).

The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.

Definition locator: Definitions 1–2 and corresponding Theorems 3–12.

- Alias `UC^{cert}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## CAdv_cert: certification of classical adversary bound

Symbol: `CAdv^{cert}`. Definition status: source_checked.

max_z classical adversary bound of the partial decision problem accepting z and rejecting all x with f(x)!=f(z).

The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.

Definition locator: Definitions 1–2 and corresponding Theorems 3–12.

- Alias `CAdv^{cert}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## cubeBoundedDeg_cert: certification of globally bounded exact polynomial degree

Symbol: `deg^{cert}`. Definition status: source_checked.

max_z globally bounded exact polynomial degree of the partial decision problem accepting z and rejecting all x with f(x)!=f(z).

The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.

Definition locator: Definitions 1–2 and corresponding Theorems 3–12.

- Alias `deg^{cert}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## cubeBoundedAdeg_cert: certification of globally bounded approximate polynomial degree

Symbol: `\widetilde{deg}^{cert}`. Definition status: source_checked.

max_z globally bounded approximate polynomial degree of the partial decision problem accepting z and rejecting all x with f(x)!=f(z).

The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.

Definition locator: Definitions 1–2 and corresponding Theorems 3–12.

- Alias `\widetilde{deg}^{cert}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## osdeg_cert: certification of two-orientation one-sided bounded polynomial degree

Symbol: `\widehat{osdeg}^{cert}`. Definition status: source_checked.

max_z two-orientation one-sided bounded polynomial degree of the partial decision problem accepting z and rejecting all x with f(x)!=f(z).

The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.

Definition locator: Definitions 1–2 and corresponding Theorems 3–12.

- Alias `\widehat{osdeg}^{cert}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## lambda_cert: certification of spectral sensitivity

Symbol: `lambda^{cert}`. Definition status: source_checked.

max_z spectral sensitivity of the partial decision problem accepting z and rejecting all x with f(x)!=f(z).

The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.

Definition locator: Definitions 1–2 and corresponding Theorems 3–12.

- Alias `lambda^{cert}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## rdeg_cert: certification of exact rational degree

Symbol: `rdeg^{cert}`. Definition status: source_checked.

max_z exact rational degree of the partial decision problem accepting z and rejecting all x with f(x)!=f(z).

The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.

Definition locator: Definitions 1–2 and corresponding Theorems 3–12.

- Alias `rdeg^{cert}`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## signDeg: sign / threshold degree

Symbol: `deg_{\pm}`. Definition status: source_checked.

Minimum real multilinear degree of p with p(x)<0 exactly on 1-inputs and p(x)>=0 on 0-inputs; equivalent to strict sign representation after an arbitrarily small shift on a finite cube.

Source conventions use sign (-1)^f. Nonconstant Boolean inputs are the intended setting.

Definition locator: Definition 3.

- Alias `deg_{\pm}`: [KKWY26](https://arxiv.org/abs/2601.08727v3), Definition 3; source_checked.

Sources: [KKWY26](https://arxiv.org/abs/2601.08727v3).

## nRelevant: number of relevant variables

Symbol: `n(f)`. Definition status: source_checked.

Number of coordinates i for which flipping i changes f somewhere.

Does not count dummy input variables; distinguish from ambient input length n.

Definition locator: Section 2.

- Alias `n(f)`: [Wel22](https://arxiv.org/abs/2005.00566v2), Section 2; source_checked.
- Alias `R(f)`: [CHS20](https://doi.org/10.1007/s00493-019-4136-7), Introduction, p.1; source_checked.

Sources: [Wel22](https://arxiv.org/abs/2005.00566v2), [CHS20](https://doi.org/10.1007/s00493-019-4136-7).

## Dweighted: weighted deterministic query complexity

Symbol: `Depth_w`. Definition status: source_checked.

Minimum over decision trees of the maximum sum of prescribed nonnegative coordinate-query weights along an input path.

Coordinate weights are part of the measure’s parameters.

Definition locator: Section 2, weighted decision trees.

- Alias `Depth_w`: [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 2, weighted decision trees; source_checked.

Sources: [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf).

## RCmin: minimum randomized certificate complexity

Symbol: `RC_min`. Definition status: source_checked.

min_x RC_x(f).



Definition locator: Definition 10.

- Alias `RC_min`: [KKWY26](https://arxiv.org/abs/2601.08727v3), Definition 10; source_checked.

Sources: [KKWY26](https://arxiv.org/abs/2601.08727v3).

## fbsmin: minimum fractional block sensitivity

Symbol: `fbs_min`. Definition status: source_checked.

min_x fbs_x(f).



Definition locator: Definition 10.

- Alias `fbs_min`: [KKWY26](https://arxiv.org/abs/2601.08727v3), Definition 10; source_checked.

Sources: [KKWY26](https://arxiv.org/abs/2601.08727v3).

## RCminDown: downward-closed minimum randomized certificate complexity

Symbol: `RC_min^downarrow`. Definition status: source_checked.

Maximum of RC_min(f restricted by rho) over coordinate restrictions rho.



Definition locator: Definition 11.

- Alias `RC_min^downarrow`: [KKWY26](https://arxiv.org/abs/2601.08727v3), Definition 11; source_checked.

Sources: [KKWY26](https://arxiv.org/abs/2601.08727v3).

## fbsminDown: downward-closed minimum fractional block sensitivity

Symbol: `fbs_min^downarrow`. Definition status: source_checked.

Maximum of fbs_min(f restricted by rho) over coordinate restrictions rho.



Definition locator: Definition 11.

- Alias `fbs_min^downarrow`: [KKWY26](https://arxiv.org/abs/2601.08727v3), Definition 11; source_checked.

Sources: [KKWY26](https://arxiv.org/abs/2601.08727v3).

## fbs_at0: fractional block sensitivity at the all-zero input

Symbol: `fbs(f,0^n)`. Definition status: source_checked.

The fractional packing of sensitive blocks at 0^n, provided that 0^n lies in the domain.



Definition locator: Theorem 1.1 and Section 2.

- Alias `fbs(f,0^n)`: [ARS26](https://arxiv.org/abs/2610.00506), Theorem 1.1 and Section 2; source_checked.

Sources: [ARS26](https://arxiv.org/abs/2610.00506).

## fbs0: 0-input fractional block sensitivity

Symbol: `fbs^0`. Definition status: source_checked.

Maximum local fbs value over inputs with f(x)=0.



Definition locator: Section 1 notation and Section 2 definitions.

- Alias `fbs^0`: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 1 notation and Section 2 definitions; source_checked.

Sources: [KT13](https://eccc.weizmann.ac.il/report/2013/168/).

## fbs1: 1-input fractional block sensitivity

Symbol: `fbs^1`. Definition status: source_checked.

Maximum local fbs value over inputs with f(x)=1.



Definition locator: Section 1 notation and Section 2 definitions.

- Alias `fbs^1`: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 1 notation and Section 2 definitions; source_checked.

Sources: [KT13](https://eccc.weizmann.ac.il/report/2013/168/).

## FC0: 0-input fractional certificate complexity

Symbol: `FC^0`. Definition status: source_checked.

Maximum local FC value over inputs with f(x)=0.



Definition locator: Section 1 notation and Section 2 definitions.

- Alias `FC^0`: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 1 notation and Section 2 definitions; source_checked.

Sources: [KT13](https://eccc.weizmann.ac.il/report/2013/168/).

## FC1: 1-input fractional certificate complexity

Symbol: `FC^1`. Definition status: source_checked.

Maximum local FC value over inputs with f(x)=1.



Definition locator: Section 1 notation and Section 2 definitions.

- Alias `FC^1`: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 1 notation and Section 2 definitions; source_checked.

Sources: [KT13](https://eccc.weizmann.ac.il/report/2013/168/).

## RC0: 0-input randomized certificate complexity

Symbol: `RC^0`. Definition status: source_checked.

Maximum local RC value over inputs with f(x)=0.



Definition locator: Section 1 notation and Section 2 definitions.

- Alias `RC^0`: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 1 notation and Section 2 definitions; source_checked.

Sources: [KT13](https://eccc.weizmann.ac.il/report/2013/168/).

## RC1: 1-input randomized certificate complexity

Symbol: `RC^1`. Definition status: source_checked.

Maximum local RC value over inputs with f(x)=1.



Definition locator: Section 1 notation and Section 2 definitions.

- Alias `RC^1`: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 1 notation and Section 2 definitions; source_checked.

Sources: [KT13](https://eccc.weizmann.ac.il/report/2013/168/).

## QC0: 0-input quantum certificate complexity

Symbol: `QC^0`. Definition status: source_checked.

Maximum local QC value over inputs with f(x)=0.



Definition locator: Section 1 notation and Section 2 definitions.

- Alias `QC^0`: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 1 notation and Section 2 definitions; source_checked.

Sources: [KT13](https://eccc.weizmann.ac.il/report/2013/168/).

## QC1: 1-input quantum certificate complexity

Symbol: `QC^1`. Definition status: source_checked.

Maximum local QC value over inputs with f(x)=1.



Definition locator: Section 1 notation and Section 2 definitions.

- Alias `QC^1`: [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 1 notation and Section 2 definitions; source_checked.

Sources: [KT13](https://eccc.weizmann.ac.il/report/2013/168/).

## cfbs_boolean: critical fractional block sensitivity of a partial Boolean function

Symbol: `cfbs`. Definition status: source_checked.

Minimum over total Boolean completions g of f of max over x in Dom(f) of fbs(g,x). The maximum ranges over the original promise, rather than all inputs of g.

Keep separate from critical fractional block sensitivity of general search relations; the two definitions require a model translation.

Definition locator: KLLPV26 Definition 35.

- Alias `cfbs`: [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 35; source_checked.

Sources: [KLLPV26](https://arxiv.org/abs/2609.26757).

## Cset: output-set certificate complexity

Symbol: `C_Sigma`. Definition status: source_checked.

For f:{0,1}^n->{0,1,*} and Sigma a subset of {0,1,*}, C_Sigma(f,x) is the fewest fixed coordinates of a subcube containing x on which every output belongs to Sigma. Maximize over x with f(x) in Sigma for C_Sigma(f).

Here * is an output denoting undefined, not an unqueried input coordinate. C_0/C_1 in this strong convention exclude undefined completions; do not combine with weak partial certificates.

Definition locator: Bal21 Section 1; BBGJK21 Puzzle II.

- Alias `C_Sigma`: [Bal21](https://arxiv.org/abs/2103.05593v1), Section 1; source_checked.

Sources: [Bal21](https://arxiv.org/abs/2103.05593v1), [BBGJK21](https://arxiv.org/abs/2102.08348v2).

## Cbar0: certificate complexity for excluding output zero

Symbol: `C_bar0`. Definition status: source_checked.

C_Sigma(f) with Sigma={1,*}, maximizing the output-set certificate complexity over all x with f(x) in Sigma.

Undefined output * is included explicitly. Local quantities C_Sigma(f,x) remain parameterized; this ID denotes their indicated maximum.

Definition locator: Bal21 Section 1; BBGJK21 Puzzle II.

- Alias `C_{\bar{0}}`: [Bal21](https://arxiv.org/abs/2103.05593v1), Section 1; source_checked.

Sources: [Bal21](https://arxiv.org/abs/2103.05593v1), [BBGJK21](https://arxiv.org/abs/2102.08348v2).

## Cbar1: certificate complexity for excluding output one

Symbol: `C_bar1`. Definition status: source_checked.

C_Sigma(f) with Sigma={0,*}, maximizing the output-set certificate complexity over all x with f(x) in Sigma.

Undefined output * is included explicitly. Local quantities C_Sigma(f,x) remain parameterized; this ID denotes their indicated maximum.

Definition locator: Bal21 Section 1; BBGJK21 Puzzle II.

- Alias `C_{\bar{1}}`: [Bal21](https://arxiv.org/abs/2103.05593v1), Section 1; source_checked.

Sources: [Bal21](https://arxiv.org/abs/2103.05593v1), [BBGJK21](https://arxiv.org/abs/2102.08348v2).

## Cstrong: strong certificate complexity of a partial function

Symbol: `C`. Definition status: source_checked.

max(C_{Sigma={0}}(f),C_{Sigma={1}}(f)). Certificates must force the declared output on all cube completions, excluding undefined outputs as well as the opposite Boolean output.

Undefined output * is included explicitly. Local quantities C_Sigma(f,x) remain parameterized; this ID denotes their indicated maximum.

Definition locator: Bal21 Section 1; BBGJK21 Puzzle II.

- Alias `C`: [Bal21](https://arxiv.org/abs/2103.05593v1), Section 1; source_checked.

Sources: [Bal21](https://arxiv.org/abs/2103.05593v1), [BBGJK21](https://arxiv.org/abs/2102.08348v2).

## Q_eps: error-parameter quantum query complexity

Symbol: `Q_epsilon`. Definition status: source_checked.

Minimum worst-case quantum oracle queries giving the correct Boolean output with probability at least 1-epsilon on every promised input. Epsilon is explicit; fixed 0<epsilon<1/2 is the usual bounded-error regime.

Epsilon-dependent constants cannot be suppressed if epsilon varies with input length.

Definition locator: HLS07 Section 2, before Theorem 1.

- Alias `Q_epsilon`: [HLS07](https://arxiv.org/abs/quant-ph/0611054), Section 2; source_checked.

Sources: [HLS07](https://arxiv.org/abs/quant-ph/0611054).

## V: deterministic verification query complexity

Symbol: `V`. Definition status: source_checked.

Maximum over candidate outputs y of the deterministic input-query complexity of deciding (x,y) in S. The candidate y is supplied without query charge; the algorithm must accept valid pairs and reject invalid pairs on every promised x.

This need not be small for an arbitrary total relation. TFNP in the query model additionally requires short, locally checkable solution certificates.

Definition locator: ICALP introduction before Theorem 5.

- Alias `V`: [AGL26](https://doi.org/10.4230/LIPIcs.ICALP.2026.3), ICALP introduction before Theorem 5; source_checked.

Sources: [AGL26](https://doi.org/10.4230/LIPIcs.ICALP.2026.3).

## input1s: input-one sensitivity

Symbol: `s_1`. Definition status: source_checked.

Maximum over promised x of the number of coordinates i with x_i=1, x^i promised, and f(x^i)!=f(x).

Input direction, not an output-conditioned maximum. Applies also to multi-output functions.

Definition locator: Section 2, lines 235–245.

- Alias `s_1`: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2, lines 235–245; source_checked.
- Alias `s_1`: [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), Section 2: directed sensitivity definitions; source_checked.

Sources: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34).

## input1bs: input-one block sensitivity

Symbol: `bs_1`. Definition status: source_checked.

Maximum over promised x of the number of pairwise disjoint sensitive blocks B contained in {i:x_i=1}, requiring x^B in the promise.

Input direction, not an output-conditioned maximum.

Definition locator: Section 2, lines 235–245.

- Alias `bs_1`: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2, lines 235–245; source_checked.
- Alias `bs_1`: [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), Section 2: directed sensitivity definitions; source_checked.

Sources: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34).

## RSize: randomized decision tree leaf size

Symbol: `RSize^dt`. Definition status: source_checked.

Minimum, over randomized decision trees solving a relation with error at most epsilon on every promised input, of the maximum number of leaves of any deterministic tree in the support. Epsilon is 1/3 unless specified.

Worst support size, not expected size and not random seed length.

Definition locator: Section 2, lines 275–277.

- Alias `RSize^dt`: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2, lines 275–277; source_checked.

Sources: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/).

## Ddist: distributional deterministic query depth

Symbol: `D^dt_{mu,epsilon}`. Definition status: source_checked.

Minimum depth of a deterministic tree whose output is valid with probability at least 1-epsilon when x is drawn from the specified input distribution mu.

The parameters mu and epsilon are part of the measure.

Definition locator: Section 2, lines 278–282.

- Alias `D^dt_{mu,epsilon}`: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2, lines 278–282; source_checked.

Sources: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/).

## DSizeDist: distributional deterministic leaf size

Symbol: `DSize^dt_{mu,epsilon}`. Definition status: source_checked.

Minimum number of leaves of a deterministic tree whose output is valid with probability at least 1-epsilon under input distribution mu.

Different from averaging query cost over mu.

Definition locator: Section 2, lines 278–283.

- Alias `DSize^dt_{mu,epsilon}`: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2, lines 278–283; source_checked.

Sources: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/).

## psDTSize: pseudo-deterministic randomized decision tree leaf size

Symbol: `psDSize^dt`. Definition status: source_checked.

Minimum, over valid selectors g of S, of the randomized worst-support leaf-size complexity of g, with error at most 1/3 on each promised input.

Different from ordinary randomized leaf size, which permits varying valid answers.

Definition locator: Section 2, lines 296–305.

- Alias `psDSize^dt`: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2, lines 296–305; source_checked.

Sources: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/).

## Dna: nonadaptive deterministic query complexity

Symbol: `D_nonadaptive`. Definition status: source_checked.

Minimum number of input bits read by a deterministic algorithm that fixes all queried coordinates before seeing any values, then computes a valid output.

The displayed symbol is a repository label; no claim that this typography appears in GGR13.

Definition locator: Theorem 4.1(2) and its nonadaptive algorithm convention.


Sources: [GGR13](https://www.wisdom.weizmann.ac.il/~oded/p_balg.html).

## Rna: nonadaptive randomized query complexity

Symbol: `R_nonadaptive`. Definition status: source_checked.

Minimum worst-case number of bits read by a randomized algorithm that chooses its queried coordinates using its coins but independently of input answers, and outputs a valid answer with probability at least 2/3 on every promised input.

The displayed symbol is a repository label; no claim that this typography appears in GGR13.

Definition locator: Theorem 4.1(2) and its nonadaptive algorithm convention.


Sources: [GGR13](https://www.wisdom.weizmann.ac.il/~oded/p_balg.html).

## psRna: nonadaptive pseudo-deterministic randomized query complexity

Symbol: `psR_nonadaptive`. Definition status: source_checked.

Minimum worst-case number of bits read by a nonadaptive randomized algorithm with one fixed valid selector value produced with probability at least 2/3 on each promised input.

The displayed symbol is a repository label; no claim that this typography appears in GGR13.

Definition locator: Theorem 4.1(2) and its nonadaptive algorithm convention.


Sources: [GGR13](https://www.wisdom.weizmann.ac.il/~oded/p_balg.html).

## DandPos: deterministic positive and query complexity

Symbol: `D^wedge-dt`. Definition status: source_checked.

Minimum worst-case number of queries, each returning the conjunction of a chosen subset of input variables (no negated literals), sufficient to output a valid answer deterministically on every promised input.

For positive conjunctions, do not identify with ANDD/Conj, whose allowed literals may include negations.

Definition locator: Section 6, lines 660–664.

- Alias `D^wedge-dt`: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 6, lines 660–664; source_checked.
- Alias `P^{wedge-dt}`: [KLMY21](https://doi.org/10.1145/3406325.3450999), Introduction and Claim 4.4; source_checked.
- Alias `D^{dt}_{AND}`: [LM19](https://doi.org/10.4230/LIPIcs.STACS.2019.50), Definition 10; source_checked.

Sources: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), [KLMY21](https://doi.org/10.1145/3406325.3450999), [LM19](https://doi.org/10.4230/LIPIcs.STACS.2019.50).

## RandPos: bounded-error randomized positive and query complexity

Symbol: `R^wedge-dt`. Definition status: source_checked.

Minimum worst-case number of queries, each returning the conjunction of a chosen subset of input variables (no negated literals), sufficient to output a valid answer with probability at least 2/3 on every promised input.

For positive conjunctions, do not identify with ANDD/Conj, whose allowed literals may include negations.

Definition locator: Section 6, lines 660–664.

- Alias `R^wedge-dt`: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 6, lines 660–664; source_checked.

Sources: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/).

## psRandPos: pseudo-deterministic randomized positive and query complexity

Symbol: `psD^wedge-dt`. Definition status: source_checked.

Minimum worst-case number of queries, each returning the conjunction of a chosen subset of input variables (no negated literals), sufficient to output one fixed valid selector with probability at least 2/3 on every promised input.

For positive conjunctions, do not identify with ANDD/Conj, whose allowed literals may include negations.

Definition locator: Section 6, lines 660–664.

- Alias `psD^wedge-dt`: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 6, lines 660–664; source_checked.

Sources: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/).

## Dpar: deterministic parity query complexity

Symbol: `D^oplus-dt`. Definition status: source_checked.

Minimum worst-case number of queries, each returning the parity over F_2 of a chosen subset of input bits, sufficient to output a valid answer deterministically on every promised input.

The queried subset can depend on previous parity answers unless nonadaptivity is explicitly imposed.

Definition locator: Section 6, lines 660–664.

- Alias `D^oplus-dt`: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 6, lines 660–664; source_checked.

Sources: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/).

## Rpar: bounded-error randomized parity query complexity

Symbol: `R^oplus-dt`. Definition status: source_checked.

Minimum worst-case number of queries, each returning the parity over F_2 of a chosen subset of input bits, sufficient to output a valid answer with probability at least 2/3 on every promised input.

The queried subset can depend on previous parity answers unless nonadaptivity is explicitly imposed.

Definition locator: Section 6, lines 660–664.

- Alias `R^oplus-dt`: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 6, lines 660–664; source_checked.

Sources: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/).

## psRpar: pseudo-deterministic randomized parity query complexity

Symbol: `psD^oplus-dt`. Definition status: source_checked.

Minimum worst-case number of queries, each returning the parity over F_2 of a chosen subset of input bits, sufficient to output one fixed valid selector with probability at least 2/3 on every promised input.

The queried subset can depend on previous parity answers unless nonadaptivity is explicitly imposed.

Definition locator: Section 6, lines 660–664.

- Alias `psD^oplus-dt`: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 6, lines 660–664; source_checked.

Sources: [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/).

## DandOr: deterministic positive AND/OR query complexity

Symbol: `D^{(wedge,vee)-dt}`. Definition status: source_checked.

Minimum worst-case query cap when each query is either a conjunction or a disjunction of a chosen subset of non-negated input variables. The algorithm is deterministic and returns a valid output.

Both subset queries cost one; do not identify with bit queries or conjunctions of arbitrary signed literals.

Definition locator: Section 5, before Proposition 5.1.

- Alias `D^{(wedge,vee)-dt}`: [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), Section 5, before Proposition 5.1; source_checked.

Sources: [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34).

## RandOr: bounded-error randomized positive AND/OR query complexity

Symbol: `R^{(wedge,vee)-dt}`. Definition status: source_checked.

Minimum worst-case query cap when each query is either a conjunction or a disjunction of a chosen subset of non-negated input variables. On every promised input it returns a valid answer with probability at least 2/3.

Both subset queries cost one; do not identify with bit queries or conjunctions of arbitrary signed literals.

Definition locator: Section 5, before Proposition 5.1.

- Alias `R^{(wedge,vee)-dt}`: [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), Section 5, before Proposition 5.1; source_checked.

Sources: [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34).

## psRandOr: pseudo-deterministic randomized positive AND/OR query complexity

Symbol: `psD^{(wedge,vee)-dt}`. Definition status: source_checked.

Minimum worst-case query cap when each query is either a conjunction or a disjunction of a chosen subset of non-negated input variables. On every promised input it returns one fixed valid selector value with probability at least 2/3.

Both subset queries cost one; do not identify with bit queries or conjunctions of arbitrary signed literals.

Definition locator: Section 5, before Proposition 5.1.

- Alias `psD^{(wedge,vee)-dt}`: [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), Section 5, before Proposition 5.1; source_checked.

Sources: [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34).

## DzeroDepth: deterministic zero-answer depth

Symbol: `D^{0-dt}`. Definition status: source_checked.

Minimum over correct deterministic bit-query trees of the maximum number of edges labelled zero on a root-to-leaf path. Edges labelled one cost zero.

Zero-answer cost, not zero-error randomized complexity.

Definition locator: Section 2.2.

- Alias `D^{0-dt}`: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Section 2.2; source_checked.
- Alias `P^{0-dt}`: [KLMY21](https://doi.org/10.1145/3406325.3450999), Section 4.2, Claim 4.4; source_checked.
- Alias `D^{dt}_0`: [LM19](https://doi.org/10.4230/LIPIcs.STACS.2019.50), Definition 9; source_checked.

Sources: [CDMRS23](https://doi.org/10.1145/3564246.3585199), [KLMY21](https://doi.org/10.1145/3406325.3450999), [LM19](https://doi.org/10.4230/LIPIcs.STACS.2019.50).

## RzeroDepth: randomized zero-answer depth

Symbol: `R^{0-dt}_{epsilon}`. Definition status: source_checked.

Minimum worst-support zero-answer depth of a randomized bit-query tree correct with probability at least 1-epsilon on every input. Epsilon=1/3 unless specified.

Counts zero answers along paths; NOT R0, the expected cost of a zero-error algorithm.

Definition locator: Section 2.2.

- Alias `R^{0-dt}_{epsilon}`: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Section 2.2; source_checked.

Sources: [CDMRS23](https://doi.org/10.1145/3564246.3585199).

## rrank: randomized decision tree rank

Symbol: `rrank`. Definition status: source_checked.

Minimum over bounded-error randomized trees of the maximum Strahler rank of any deterministic tree in the support. Error is 1/3 on each input.

Support maximum, not expected rank; deterministic rank is DTRank.

Definition locator: Definitions 2.9–2.10.

- Alias `rrank`: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Definitions 2.9–2.10; source_checked.
- Alias `rrank`: [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Definition 3; source_checked.

Sources: [CDMRS23](https://doi.org/10.1145/3564246.3585199), [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15).

## coverN0: 0-monochromatic subcube cover number

Symbol: `N_0`. Definition status: source_checked.

Minimum number of 0-monochromatic subcubes whose union is f^{-1}(0).

Counts subcubes, not certificate width; zero for an empty output fibre.

Definition locator: Definition 2.2.

- Alias `N_0`: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Definition 2.2; source_checked.

Sources: [CDMRS23](https://doi.org/10.1145/3564246.3585199).

## coverN1: 1-monochromatic subcube cover number

Symbol: `N_1`. Definition status: source_checked.

Minimum number of 1-monochromatic subcubes whose union is f^{-1}(1).

Counts subcubes, not certificate width; zero for an empty output fibre.

Definition locator: Definition 2.2.

- Alias `N_1`: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Definition 2.2; source_checked.

Sources: [CDMRS23](https://doi.org/10.1145/3564246.3585199).

## coverN: monochromatic subcube cover number

Symbol: `N`. Definition status: source_checked.

The sum N_0(f)+N_1(f) of the two monochromatic subcube cover numbers.

Unbounded counts are distinct from certificate widths and logarithms of cover counts.

Definition locator: Definition 2.2.

- Alias `N`: [CDMRS23](https://doi.org/10.1145/3564246.3585199), Definition 2.2; source_checked.

Sources: [CDMRS23](https://doi.org/10.1145/3564246.3585199).

## Davg: average-cost deterministic query complexity

Symbol: `Davg_mu`. Definition status: source_checked.

Minimum expected query count E_{x~mu} cost(T,x) over deterministic trees correct on every promised input.

The distribution mu is fixed and known in this nonuniform query model. This is not Ddist, which budgets average error instead of averaging cost. Display symbol is repository notation, not a verified literal source occurrence.

Definition locator: Definition 24.


Sources: [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36).

## Ravg: average-cost bounded-error randomized query complexity

Symbol: `Ravg_mu`. Definition status: source_checked.

Minimum E_{x~mu,coins} cost(A,x) over randomized solvers with probability at least 2/3 of a valid answer on every promised input.

The distribution mu is fixed and known in this nonuniform query model. This is not Ddist, which budgets average error instead of averaging cost. Display symbol is repository notation, not a verified literal source occurrence.

Definition locator: Definition 24.


Sources: [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36).

## R0avg: average-cost strict Las Vegas query complexity

Symbol: `R0avg_mu`. Definition status: source_checked.

Minimum E_{x~mu,coins} cost(A,x) over randomized algorithms that terminate and return a valid answer with probability one on every promised input.

The distribution mu is fixed and known in this nonuniform query model. This is not Ddist, which budgets average error instead of averaging cost. Display symbol is repository notation, not a verified literal source occurrence.

Definition locator: Definition 24.


Sources: [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36).

## psRavg: average-cost pseudo-deterministic query complexity

Symbol: `psRavg_mu`. Definition status: source_checked.

Minimum E_{x~mu,coins} cost(A,x) over algorithms with one fixed valid selector value returned with probability at least 2/3 on every promised input.

The distribution mu is fixed and known in this nonuniform query model. This is not Ddist, which budgets average error instead of averaging cost. Display symbol is repository notation, not a verified literal source occurrence.

Definition locator: Definition 24.


Sources: [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36).

## psR0avg: average-cost strict canonical zero-error query complexity

Symbol: `psR0avg_mu`. Definition status: source_checked.

Minimum over valid selectors g of R0avg_mu(g); equivalently, an almost-surely terminating randomized algorithm must output the same g(x) with probability one on every input.

The distribution mu is fixed and known in this nonuniform query model. This is not Ddist, which budgets average error instead of averaging cost. Display symbol is repository notation, not a verified literal source occurrence.

Definition locator: Definition 24.


Sources: [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36).

## Rfail: zero-error randomized query cap with detectable failure

Symbol: `Rfail`. Definition status: source_checked.

Minimum worst-case query cap of a randomized search algorithm that never outputs an invalid answer, but may output the failure symbol bottom with probability at most 1/3 on each input.

A failure flag is permitted. R0 instead requires eventual valid output and uses expected cost. The displayed symbol is a repository scalar label. Display symbol is repository notation, not a verified literal source occurrence.

Definition locator: Definition 14 (scalar cap specialization).


Sources: [ZPP26](https://doi.org/10.4230/LIPIcs.ITCS.2026.60).

## DTNodes: deterministic decision tree total-node size

Symbol: `DTSize`. Definition status: source_checked.

Minimum total number of nodes, including leaves and internal nodes, of a correct full binary bit-query tree.

CMP22 counts nodes; CDM23/CDMRS23 count leaves. For full binary trees DTNodes=2 DTSize(repository leaf count)-1. Do not use the same source typography to assert identical normalizations.

Definition locator: Introduction, Corollary 9 and Appendix A.1.

- Alias `DTSize`: [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Introduction, Corollary 9 and Appendix A.1; source_checked.

Sources: [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15).

## RNodes: randomized decision tree total-node size

Symbol: `RDTSize`. Definition status: source_checked.

Minimum worst-support total-node count of a randomized bit-query tree correct with probability at least 2/3 on each input.

Whole-node count, not leaf count or expected size. RNodes=2 RSize-1 under full binary tree conventions.

Definition locator: Corollary 27; Appendix A.1.

- Alias `RDTSize`: [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Corollary 27; Appendix A.1; source_checked.

Sources: [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15).

## rel_Qeps: error-parameter quantum search query complexity

Symbol: `Q_epsilon`. Definition status: source_checked.

Minimum quantum bit-query cap with probability at least 1-epsilon of outputting some valid answer on every promised input.

CMP22 uses epsilon=2/5 for randomized-tree simulations. Arbitrary relations do not automatically admit majority error reduction; this is separate from decision Q_eps and default search Q at error 1/3.

Definition locator: Theorem 5 and Corollary 27.

- Alias `Q_epsilon`: [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Theorem 5 and Corollary 27; source_checked.

Sources: [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15).

## DTGuess: minimum deterministic tree guessing complexity

Symbol: `G`. Definition status: source_checked.

Minimum over correct deterministic trees T of G(T), where G(T) minimizes the largest number of red edges on a path over edge colorings having at most one black child edge at each node.

The source defines G(T) for a tree; this catalogue additionally minimizes it over valid trees. Claim 12 identifies tree guessing complexity with tree Strahler rank. No new source notation G(f) is asserted.

Definition locator: Definitions 10–11 and Claim 12.

- Alias `G`: [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Definitions 10–11 and Claim 12; source_checked.

Sources: [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15).

## Bbomb: bomb query complexity

Symbol: `B`. Definition status: source_checked.

Minimum bomb-query cap with explosion probability at most 0.01 and total error (including explosion) at most 0.01 on every promised input. A bomb query uses a controlled input query with a clean zero record bit, measures it immediately, and terminates on outcome one.

Fixed error constants; the source shorthand B is used only up to its constant-error equivalence.

Definition locator: Section 3; Theorem 4.1.

- Alias `B`: [LL16](https://theoryofcomputing.org/articles/v012a018/), Section 3 and Theorem 4.1; source_checked.

Sources: [LL16](https://theoryofcomputing.org/articles/v012a018/).

## BbombParams: error-parameter bomb query complexity

Symbol: `B_{epsilon,delta}`. Definition status: source_checked.

Minimum number of controlled queries in the bomb model with explosion probability at most epsilon and total error, including explosion, at most delta on every promised input. The record starts at zero and is measured immediately after each query; outcome one terminates the algorithm.

Both error budgets are explicit; 0<epsilon<=delta in the usual regime. The source total-error requirement is not error conditioned on survival.

Definition locator: Section 3; Theorem 4.1.

- Alias `B_{epsilon,delta}`: [LL16](https://theoryofcomputing.org/articles/v012a018/), Section 3 and Theorem 4.1; source_checked.

Sources: [LL16](https://theoryofcomputing.org/articles/v012a018/).

## monomialSparsity: real multilinear monomial sparsity on the 0/1 cube

Symbol: `spar`. Definition status: source_checked.

Number of nonzero coefficients in the unique representation f(x)=sum_{S subset [n]} a_S product_{i in S} x_i on {0,1}^n, including the empty monomial.

For AND_n this sparsity is 1, while every Walsh Fourier coefficient is nonzero. Logarithmic bounds are interpreted with log(2+spar) at the constant-size boundary.

Definition locator: Introduction before Theorem 1.1, and Section 2.

- Alias `spar`: [KLMY21](https://doi.org/10.1145/3406325.3450999), Introduction before Theorem 1.1; source_checked.

Sources: [KLMY21](https://doi.org/10.1145/3406325.3450999).

## approxMonomialSparsity: approximate real monomial sparsity

Symbol: `tilde spar`. Definition status: source_checked.

Minimum number of nonzero coefficients in the 0/1 multilinear monomial representation of a real polynomial p with |p(x)-f(x)|<=1/3 on every Boolean input.

Kept separate from exact monomial sparsity and Fourier sparsity.

Definition locator: Definition 3.18.

- Alias `tilde spar`: [KLMY21survey](https://cseweb.ucsd.edu/~shmcguir/papers/KLMYsigact.pdf), Definition 3.18; source_checked.

Sources: [KLMY21survey](https://cseweb.ucsd.edu/~shmcguir/papers/KLMYsigact.pdf).

## monomialWeight: real monomial coefficient weight

Symbol: `wt`. Definition status: source_checked.

Sum of absolute coefficients of the unique multilinear real polynomial equal to f on the full Boolean cube, in the 0/1 monomial basis.

Total Boolean functions; signed coefficients. Generalized representations are not conical nonnegative representations.

Definition locator: Definitions 2.2–2.3.

- Alias `wt`: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Definitions 2.2–2.3; source_checked.

Sources: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/).

## approxMonomialWeight: approximate real monomial coefficient weight

Symbol: `tilde wt`. Definition status: source_checked.

Minimum sum of absolute coefficients of a real multilinear 0/1 monomial polynomial that pointwise approximates f within 1/3 on the full cube.

Total Boolean functions; signed coefficients. Generalized representations are not conical nonnegative representations.

Definition locator: Definition 2.5.

- Alias `tilde wt`: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Definition 2.5; source_checked.

Sources: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/).

## generalizedSparsity: generalized real monomial sparsity

Symbol: `gspar`. Definition status: source_checked.

Minimum number of nonzero signed real coefficients representing f exactly as a linear combination of subcube indicators product_{i in S} x_i product_{j in T}(1-x_j), with S and T disjoint.

Total Boolean functions; signed coefficients. Generalized representations are not conical nonnegative representations.

Definition locator: Definitions 2.9–2.11.

- Alias `gspar`: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Definitions 2.9–2.11; source_checked.

Sources: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/).

## approxGeneralizedSparsity: approximate generalized real monomial sparsity

Symbol: `tilde gspar`. Definition status: source_checked.

Minimum number of nonzero signed real coefficients in a linear combination of subcube indicators approximating f pointwise within 1/3 on the full cube.

Total Boolean functions; signed coefficients. Generalized representations are not conical nonnegative representations.

Definition locator: Definitions 2.9–2.11.

- Alias `tilde gspar`: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Definitions 2.9–2.11; source_checked.

Sources: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/).

## generalizedWeight: generalized real monomial coefficient weight

Symbol: `gwt`. Definition status: source_checked.

Minimum sum of absolute signed real coefficients among exact representations of f by subcube indicators. The dictionary is redundant; minimize over representations.

Total Boolean functions; signed coefficients. Generalized representations are not conical nonnegative representations.

Definition locator: Definitions 2.9–2.11.

- Alias `gwt`: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Definitions 2.9–2.11; source_checked.

Sources: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/).

## approxGeneralizedWeight: approximate generalized real monomial coefficient weight

Symbol: `tilde gwt`. Definition status: source_checked.

Minimum sum of absolute signed real coefficients among subcube-indicator representations approximating f pointwise within 1/3 on the full cube.

Total Boolean functions; signed coefficients. Generalized representations are not conical nonnegative representations.

Definition locator: Definitions 2.9–2.11.

- Alias `tilde gwt`: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Definitions 2.9–2.11; source_checked.

Sources: [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/).

## NisR2expect: Nisan expected two-sided-error randomized query complexity

Symbol: `R_2`. Definition status: source_checked.

Minimum worst-case expected number of queries of an always-terminating randomized decision tree with error at most 1/4 on every input.



Definition locator: Section 1.2, p.329.

- Alias `R_2`: [Nis89](https://doi.org/10.1145/73007.73038), Section 1.2, p.329; source_checked.

Sources: [Nis89](https://doi.org/10.1145/73007.73038).

## NisR1expect: Nisan expected one-sided-error randomized query complexity

Symbol: `R_1`. Definition status: source_checked.

Minimum worst-case expected queries; always reject 0-inputs and accept 1-inputs with probability at least 1/2.



Definition locator: Section 1.2, p.329.

- Alias `R_1`: [Nis89](https://doi.org/10.1145/73007.73038), Section 1.2, p.329; source_checked.

Sources: [Nis89](https://doi.org/10.1145/73007.73038).

## permD: permutation decision-tree depth

Symbol: `D`. Definition status: source_checked.

Minimum worst-case number of queries pi(i)=? or pi^{-1}(j)=? computing f:S_n->{0,1}; each query returns a symbol in [n].



Definition locator: Introduction and Section 2.2.

- Alias `D`: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Introduction and Section 2.2; source_checked.

Sources: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), [DFLLV26](https://doi.org/10.5070/C6.68665).

## permDegree: permutation polynomial degree

Symbol: `deg`. Definition status: source_checked.

Minimum degree of a real polynomial in permutation-matrix entries agreeing with f on S_n. Equivalently, span of functions depending on at most d values pi(i).



Definition locator: Introduction and Section 2.2.

- Alias `deg`: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Introduction and Section 2.2; source_checked.

Sources: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), [DFLLV26](https://doi.org/10.5070/C6.68665).

## permAdeg: permutation approximate degree

Symbol: `tilde deg`. Definition status: source_checked.

Minimum degree of a real polynomial in permutation-matrix entries approximating f within 1/3 on S_n.



Definition locator: Introduction and Section 2.2.

- Alias `tilde deg`: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Introduction and Section 2.2; source_checked.

Sources: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), [DFLLV26](https://doi.org/10.5070/C6.68665).

## permS: disjoint-transposition sensitivity

Symbol: `s`. Definition status: source_checked.

Maximum over pi of the largest family of pairwise disjoint transpositions tau with f(tau*pi)!=f(pi).



Definition locator: Introduction and Section 2.2.

- Alias `s`: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Introduction and Section 2.2; source_checked.

Sources: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), [DFLLV26](https://doi.org/10.5070/C6.68665).

## permEdgeS: transposition edge sensitivity

Symbol: `t`. Definition status: source_checked.

Maximum over pi of the total number of transpositions tau with f(pi*tau)!=f(pi); disjointness is not required.



Definition locator: Introduction and Section 2.2.

- Alias `t`: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Introduction and Section 2.2; source_checked.

Sources: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), [DFLLV26](https://doi.org/10.5070/C6.68665).

## permBS: permutation block sensitivity

Symbol: `bs`. Definition status: source_checked.

Maximum over pi of the largest family of permutations tau_j with pairwise disjoint moved-point supports and f(tau_j*pi)!=f(pi).



Definition locator: Introduction and Section 2.2.

- Alias `bs`: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Introduction and Section 2.2; source_checked.

Sources: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), [DFLLV26](https://doi.org/10.5070/C6.68665).

## completion_D: minimum-completion deterministic query complexity

Symbol: `overline D`. Definition status: source_checked.

Minimum of D(F) over all total Boolean completions F on the same cube with F(x)=f(x) for every promised x. On a total domain this equals D(f).

The source defines an arbitrary-measure template; this record is an explicit instantiation. Each minimum may use a different completion. Overline notation visually checked in the original PDF.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline D`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_R0: minimum-completion zero-error randomized query complexity

Symbol: `overline R_0`. Definition status: source_checked.

Minimum of R0(F) over all total Boolean completions F on the same cube with F(x)=f(x) for every promised x. On a total domain this equals R0(f).

The source defines an arbitrary-measure template; this record is an explicit instantiation. Each minimum may use a different completion. Overline notation visually checked in the original PDF.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline R_0`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_R: minimum-completion bounded-error randomized query complexity

Symbol: `overline R`. Definition status: source_checked.

Minimum of R(F) over all total Boolean completions F on the same cube with F(x)=f(x) for every promised x. On a total domain this equals R(f).

The source defines an arbitrary-measure template; this record is an explicit instantiation. Each minimum may use a different completion. Overline notation visually checked in the original PDF.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline R`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_C: minimum-completion certificate complexity

Symbol: `overline C`. Definition status: source_checked.

Minimum of C(F) over all total Boolean completions F on the same cube with F(x)=f(x) for every promised x. On a total domain this equals C(f).

The source defines an arbitrary-measure template; this record is an explicit instantiation. Each minimum may use a different completion. Overline notation visually checked in the original PDF.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline C`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_RC: minimum-completion randomized certificate complexity

Symbol: `overline RC`. Definition status: source_checked.

Minimum of RC(F) over all total Boolean completions F on the same cube with F(x)=f(x) for every promised x. On a total domain this equals RC(f).

The source defines an arbitrary-measure template; this record is an explicit instantiation. Each minimum may use a different completion. Overline notation visually checked in the original PDF.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline RC`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_bs: minimum-completion block sensitivity

Symbol: `overline bs`. Definition status: source_checked.

Minimum of bs(F) over all total Boolean completions F on the same cube with F(x)=f(x) for every promised x. On a total domain this equals bs(f).

The source defines an arbitrary-measure template; this record is an explicit instantiation. Each minimum may use a different completion. Overline notation visually checked in the original PDF.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline bs`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_s: minimum-completion sensitivity

Symbol: `overline s`. Definition status: source_checked.

Minimum of s(F) over all total Boolean completions F on the same cube with F(x)=f(x) for every promised x. On a total domain this equals s(f).

The source defines an arbitrary-measure template; this record is an explicit instantiation. Each minimum may use a different completion. Overline notation visually checked in the original PDF.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline s`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_lambda: minimum-completion spectral sensitivity

Symbol: `overline lambda`. Definition status: source_checked.

Minimum of lambda(F) over all total Boolean completions F on the same cube with F(x)=f(x) for every promised x. On a total domain this equals lambda(f).

The source defines an arbitrary-measure template; this record is an explicit instantiation. Each minimum may use a different completion. Overline notation visually checked in the original PDF.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline lambda`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_QE: minimum-completion exact quantum query complexity

Symbol: `overline Q_E`. Definition status: source_checked.

Minimum of QE(F) over all total Boolean completions F on the same cube with F(x)=f(x) for every promised x. On a total domain this equals QE(f).

The source defines an arbitrary-measure template; this record is an explicit instantiation. Each minimum may use a different completion. Overline notation visually checked in the original PDF.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline Q_E`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_deg: minimum-completion real exact polynomial degree

Symbol: `overline deg`. Definition status: source_checked.

Minimum of deg(F) over all total Boolean completions F on the same cube with F(x)=f(x) for every promised x. On a total domain this equals deg(f).

The source defines an arbitrary-measure template; this record is an explicit instantiation. Each minimum may use a different completion. Overline notation visually checked in the original PDF.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline deg`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_Q: minimum-completion bounded-error quantum query complexity

Symbol: `overline Q`. Definition status: source_checked.

Minimum of Q(F) over all total Boolean completions F on the same cube with F(x)=f(x) for every promised x. On a total domain this equals Q(f).

The source defines an arbitrary-measure template; this record is an explicit instantiation. Each minimum may use a different completion. Overline notation visually checked in the original PDF.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline Q`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_adeg: minimum-completion approximate degree

Symbol: `overline \widetilde{deg}`. Definition status: source_checked.

Minimum of adeg(F) over all total Boolean completions F on the same cube with F(x)=f(x) for every promised x. On a total domain this equals adeg(f).

The source defines an arbitrary-measure template; this record is an explicit instantiation. Each minimum may use a different completion. Overline notation visually checked in the original PDF.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline \widetilde{deg}`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## promiseS: exit-sensitive sensitivity

Symbol: `s prime`. Definition status: source_checked.

Maximum over promised x of the number of single-bit flips yielding the opposite output OR leaving the promise.



Definition locator: Definition 15.

- Alias `s prime`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 15; source_checked.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## promiseBS: exit-sensitive block sensitivity

Symbol: `bs prime`. Definition status: source_checked.

Maximum over promised x of the number of pairwise disjoint blocks whose flip yields the opposite output OR leaves the promise.



Definition locator: Definition 15.

- Alias `bs prime`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 15; source_checked.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## criticalBScompletion: completion-critical block sensitivity

Symbol: `cbs`. Definition status: source_checked.

Minimum over total Boolean completions F of max_{x in Dom(f)} bs(F,x). Off-promise inputs are excluded from the outer maximum, but blocks may lead to them.



Definition locator: Definition 18.

- Alias `cbs`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 18; source_checked.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## criticalCertificate: block-optimal-completion critical certificate complexity

Symbol: `C_cri`. Definition status: source_checked.

Among total completions F attaining completion-critical block sensitivity, minimize max_{x in Dom(f)} C(F,x). The minimization is constrained to block-optimal completions.



Definition locator: Definition 19.

- Alias `C_cri`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 19; source_checked.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## permC: permutation certificate complexity

Symbol: `C`. Definition status: source_checked.

Maximum over pi of the minimum number of specified permutation entries whose presence forces f(pi) on S_n.

Not the Boolean-cube measure. In particular R_0 here is a capped detectable-failure model with failure 2/3, not expected Las Vegas cost.

Definition locator: Section 2.2.

- Alias `C`: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Section 2.2; source_checked.

Sources: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), [DFLLV26](https://doi.org/10.5070/C6.68665).

## permUC: permutation unambiguous certificate complexity

Symbol: `U`. Definition status: source_checked.

Minimum maximum size of permutation-entry certificates forming a partition: each permutation extends exactly one certificate.

Not the Boolean-cube measure. In particular R_0 here is a capped detectable-failure model with failure 2/3, not expected Las Vegas cost.

Definition locator: Section 2.2.

- Alias `U`: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Section 2.2; source_checked.

Sources: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), [DFLLV26](https://doi.org/10.5070/C6.68665).

## permFBS: permutation fractional block sensitivity

Symbol: `fbs`. Definition status: source_checked.

At pi, maximize the total nonnegative weight on opposite-output permutations, with total weight at most one for each removed entry of pi. Maximize over pi.

Not the Boolean-cube measure. In particular R_0 here is a capped detectable-failure model with failure 2/3, not expected Las Vegas cost.

Definition locator: Section 2.2.

- Alias `fbs`: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Section 2.2; source_checked.

Sources: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), [DFLLV26](https://doi.org/10.5070/C6.68665).

## permR: permutation randomized query depth

Symbol: `R`. Definition status: source_checked.

Minimum worst-case depth cap for forward/inverse symbol queries, with error at most 1/3 on every permutation.

Not the Boolean-cube measure. In particular R_0 here is a capped detectable-failure model with failure 2/3, not expected Las Vegas cost.

Definition locator: Section 2.2.

- Alias `R`: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Section 2.2; source_checked.

Sources: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), [DFLLV26](https://doi.org/10.5070/C6.68665).

## permRfail23: permutation detectable-failure query depth

Symbol: `R_0`. Definition status: source_checked.

Minimum depth cap returning f(pi) or a detectable star, never wrong, and star probability at most 2/3 on each permutation.

Not the Boolean-cube measure. In particular R_0 here is a capped detectable-failure model with failure 2/3, not expected Las Vegas cost.

Definition locator: Section 2.2.

- Alias `R_0`: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Section 2.2; source_checked.

Sources: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), [DFLLV26](https://doi.org/10.5070/C6.68665).

## permQ: permutation bounded-error quantum query complexity

Symbol: `Q`. Definition status: source_checked.

Minimum number of coherent forward/inverse symbol-oracle queries computing f on S_n with error at most 1/3.

Not the Boolean-cube measure. In particular R_0 here is a capped detectable-failure model with failure 2/3, not expected Las Vegas cost.

Definition locator: Section 2.2.

- Alias `Q`: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Section 2.2; source_checked.

Sources: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), [DFLLV26](https://doi.org/10.5070/C6.68665).

## permQE: permutation exact quantum query complexity

Symbol: `Q_E`. Definition status: source_checked.

Minimum fixed number of coherent forward/inverse symbol-oracle queries computing f on S_n with certainty.

Not the Boolean-cube measure. In particular R_0 here is a capped detectable-failure model with failure 2/3, not expected Las Vegas cost.

Definition locator: Section 2.2.

- Alias `Q_E`: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Section 2.2; source_checked.

Sources: [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), [DFLLV26](https://doi.org/10.5070/C6.68665).

## completion_nRelevant: minimum relevant-variable count of a total completion

Symbol: `overline nRelevant`. Definition status: source_checked.

Minimum nRelevant(F) over total Boolean functions F agreeing with f on its promised domain.

Generic completion-template instantiation. Equals deterministic nonadaptive bit-query complexity of a partial decision function; not polynomially equivalent to D even on total functions.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline nRelevant`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_C0: minimum-completion 0-certificate complexity

Symbol: `overline C_0`. Definition status: source_checked.

Minimum C0(F) over total Boolean functions F agreeing with f on every promised input.

Explicit instance of the generic source template, not a separately named source measure. One-sided measures need not be polynomially equivalent to D on total functions; no automatic equivalence is asserted.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline C_0`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_C1: minimum-completion 1-certificate complexity

Symbol: `overline C_1`. Definition status: source_checked.

Minimum C1(F) over total Boolean functions F agreeing with f on every promised input.

Explicit instance of the generic source template, not a separately named source measure. One-sided measures need not be polynomially equivalent to D on total functions; no automatic equivalence is asserted.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline C_1`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_UC: minimum-completion unambiguous certificate complexity

Symbol: `overline UC`. Definition status: source_checked.

Minimum UC(F) over total Boolean functions F agreeing with f on every promised input.

Explicit instance of the generic source template, not a separately named source measure. One-sided measures need not be polynomially equivalent to D on total functions; no automatic equivalence is asserted.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline UC`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_UC0: minimum-completion 0-unambiguous certificate complexity

Symbol: `overline UC_0`. Definition status: source_checked.

Minimum UC0(F) over total Boolean functions F agreeing with f on every promised input.

Explicit instance of the generic source template, not a separately named source measure. One-sided measures need not be polynomially equivalent to D on total functions; no automatic equivalence is asserted.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline UC_0`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_UC1: minimum-completion 1-unambiguous certificate complexity

Symbol: `overline UC_1`. Definition status: source_checked.

Minimum UC1(F) over total Boolean functions F agreeing with f on every promised input.

Explicit instance of the generic source template, not a separately named source measure. One-sided measures need not be polynomially equivalent to D on total functions; no automatic equivalence is asserted.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline UC_1`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_fbs: minimum-completion fractional block sensitivity

Symbol: `overline fbs`. Definition status: source_checked.

Minimum fbs(F) over total Boolean functions F agreeing with f on every promised input.

Explicit instance of the generic source template, not a separately named source measure. One-sided measures need not be polynomially equivalent to D on total functions; no automatic equivalence is asserted.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline fbs`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_FC: minimum-completion fractional certificate complexity

Symbol: `overline FC`. Definition status: source_checked.

Minimum FC(F) over total Boolean functions F agreeing with f on every promised input.

Explicit instance of the generic source template, not a separately named source measure. One-sided measures need not be polynomially equivalent to D on total functions; no automatic equivalence is asserted.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline FC`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_QC: minimum-completion quantum certificate complexity

Symbol: `overline QC`. Definition status: source_checked.

Minimum QC(F) over total Boolean functions F agreeing with f on every promised input.

Explicit instance of the generic source template, not a separately named source measure. One-sided measures need not be polynomially equivalent to D on total functions; no automatic equivalence is asserted.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline QC`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_Q0: minimum-completion zero-error quantum query complexity

Symbol: `overline Q_0`. Definition status: source_checked.

Minimum Q0(F) over total Boolean functions F agreeing with f on every promised input.

Explicit instance of the generic source template, not a separately named source measure. One-sided measures need not be polynomially equivalent to D on total functions; no automatic equivalence is asserted.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline Q_0`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## completion_R1: minimum-completion one-sided-error randomized query complexity

Symbol: `overline R_1`. Definition status: source_checked.

Minimum R1(F) over total Boolean functions F agreeing with f on every promised input.

Explicit instance of the generic source template, not a separately named source measure. One-sided measures need not be polynomially equivalent to D on total functions; no automatic equivalence is asserted.

Definition locator: Definition 45, p.22.

- Alias `overline M`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22; source_checked.

Unverified occurrences / repository variants (not established historical notation):
- `overline R_1`: HKMP26; repository_display_not_a_historical_occurrence.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## domainD: query-domain deterministic depth

Symbol: `D`. Definition status: source_checked.

Minimum depth of a decision tree whose query Q returns the unique element of x intersect Q, for x in X.

Domain X consists of n-element subsets of U. Each allowed query intersects every input in exactly one element, and queries cover U. Use domain-qualified scopes; this is not an additional Boolean-cube definition.

Definition locator: Sections 2.1–2.2.

- Alias `D`: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2; source_checked.

Sources: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), [DFLLV26](https://doi.org/10.5070/C6.68665).

## domainR: query-domain bounded-error randomized depth

Symbol: `R`. Definition status: source_checked.

Minimum common depth cap of a distribution over domain decision trees, with success at least 2/3 on each x in X.

Domain X consists of n-element subsets of U. Each allowed query intersects every input in exactly one element, and queries cover U. Use domain-qualified scopes; this is not an additional Boolean-cube definition.

Definition locator: Sections 2.1–2.2.

- Alias `R`: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2; source_checked.

Sources: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), [DFLLV26](https://doi.org/10.5070/C6.68665).

## domainRfail23: query-domain detectable-failure depth

Symbol: `R_0`. Definition status: source_checked.

Minimum common depth cap of zero-error trees with outputs 0,1,star and failure probability at most 2/3 on every x.

Domain X consists of n-element subsets of U. Each allowed query intersects every input in exactly one element, and queries cover U. Use domain-qualified scopes; this is not an additional Boolean-cube definition.

Definition locator: Sections 2.1–2.2.

- Alias `R_0`: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2; source_checked.

Sources: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), [DFLLV26](https://doi.org/10.5070/C6.68665).

## domainQ: query-domain bounded-error quantum queries

Symbol: `Q`. Definition status: source_checked.

Minimum coherent domain-symbol oracle queries computing the Boolean output with error at most 1/3.

Domain X consists of n-element subsets of U. Each allowed query intersects every input in exactly one element, and queries cover U. Use domain-qualified scopes; this is not an additional Boolean-cube definition.

Definition locator: Sections 2.1–2.2.

- Alias `Q`: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2; source_checked.

Sources: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), [DFLLV26](https://doi.org/10.5070/C6.68665).

## domainQE: query-domain exact quantum queries

Symbol: `Q_E`. Definition status: source_checked.

Minimum fixed coherent domain-symbol oracle query count computing the output with certainty.

Domain X consists of n-element subsets of U. Each allowed query intersects every input in exactly one element, and queries cover U. Use domain-qualified scopes; this is not an additional Boolean-cube definition.

Definition locator: Sections 2.1–2.2.

- Alias `Q_E`: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2; source_checked.

Sources: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), [DFLLV26](https://doi.org/10.5070/C6.68665).

## domainDegree: query-domain spatial degree

Symbol: `deg`. Definition status: source_checked.

Minimum maximum |A| in a linear combination of indicators [A subseteq x] representing f on X; equivalently degree in membership indicators.

Domain X consists of n-element subsets of U. Each allowed query intersects every input in exactly one element, and queries cover U. Use domain-qualified scopes; this is not an additional Boolean-cube definition.

Definition locator: Sections 2.1–2.2.

- Alias `deg`: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2; source_checked.

Sources: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), [DFLLV26](https://doi.org/10.5070/C6.68665).

## domainAdeg: query-domain spatial approximate degree

Symbol: `tilde deg`. Definition status: source_checked.

Minimum maximum |A| in a real linear combination of indicators [A subseteq x] approximating f within 1/3 on X. No bound outside X is imposed.

Domain X consists of n-element subsets of U. Each allowed query intersects every input in exactly one element, and queries cover U. Use domain-qualified scopes; this is not an additional Boolean-cube definition.

Definition locator: Sections 2.1–2.2.

- Alias `tilde deg`: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2; source_checked.

Sources: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), [DFLLV26](https://doi.org/10.5070/C6.68665).

## domainC: query-domain certificate complexity

Symbol: `C`. Definition status: source_checked.

Maximum over x in X of the minimum |a| for a subset a of x such that every y in X extending a has f(y)=f(x).

Domain X consists of n-element subsets of U. Each allowed query intersects every input in exactly one element, and queries cover U. Use domain-qualified scopes; this is not an additional Boolean-cube definition.

Definition locator: Sections 2.1–2.2.

- Alias `C`: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2; source_checked.

Sources: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), [DFLLV26](https://doi.org/10.5070/C6.68665).

## domainUC: query-domain unambiguous certificate complexity

Symbol: `U`. Definition status: source_checked.

Minimum largest certificate size in a collection of subsets of the universe such that every x in X extends exactly one certificate.

Domain X consists of n-element subsets of U. Each allowed query intersects every input in exactly one element, and queries cover U. Use domain-qualified scopes; this is not an additional Boolean-cube definition.

Definition locator: Sections 2.1–2.2.

- Alias `U`: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2; source_checked.

Sources: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), [DFLLV26](https://doi.org/10.5070/C6.68665).

## domainBS: query-domain block sensitivity

Symbol: `bs`. Definition status: source_checked.

Maximum over x of the largest family of opposite-output y_j in X for which the removed-entry sets x minus y_j are pairwise disjoint.

Domain X consists of n-element subsets of U. Each allowed query intersects every input in exactly one element, and queries cover U. Use domain-qualified scopes; this is not an additional Boolean-cube definition.

Definition locator: Sections 2.1–2.2.

- Alias `bs`: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2; source_checked.

Sources: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), [DFLLV26](https://doi.org/10.5070/C6.68665).

## domainFBS: query-domain fractional block sensitivity

Symbol: `fbs`. Definition status: source_checked.

Maximum over x of the nonnegative weighted packing of opposite-output y, subject to total weight at most one through each removed element of x.

Domain X consists of n-element subsets of U. Each allowed query intersects every input in exactly one element, and queries cover U. Use domain-qualified scopes; this is not an additional Boolean-cube definition.

Definition locator: Sections 2.1–2.2.

- Alias `fbs`: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2; source_checked.

Sources: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), [DFLLV26](https://doi.org/10.5070/C6.68665).

## domainS: query-domain chunk sensitivity

Symbol: `s`. Definition status: source_checked.

Maximum over x of the largest family of opposite-output y_j with pairwise disjoint x minus y_j and each |x minus y_j| equal to the domain chunk size c.

Domain X consists of n-element subsets of U. Each allowed query intersects every input in exactly one element, and queries cover U. Use domain-qualified scopes; this is not an additional Boolean-cube definition.

Definition locator: Sections 2.1–2.2.

- Alias `s`: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2; source_checked.
- Alias `s_2(f)`: [BD16](https://doi.org/10.4230/LIPIcs.TQC.2016.7), Definition 7; source_checked.

Sources: [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), [DFLLV26](https://doi.org/10.5070/C6.68665), [BD16](https://doi.org/10.4230/LIPIcs.TQC.2016.7).

## domainCoverRadius: covering radius of a promise domain

Symbol: `r_C`. Definition status: source_checked.

For nonempty X=Dom(f) subseteq {+1,-1}^n, max over cube points y of min_{x in X} HammingDistance(x,y).

These are domain/polynomial parameters, not canonical Fourier statistics of an incompletely defined Boolean function.

Definition locator: Definition 61.

- Alias `r_C`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 61; source_checked.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## polyCoordSparsity: coordinate Fourier sparsity of a fixed polynomial

Symbol: `spar_i`. Definition status: source_checked.

Number of nonzero Walsh Fourier coefficients of p whose index sets contain the specified coordinate i.

These are domain/polynomial parameters, not canonical Fourier statistics of an incompletely defined Boolean function.

Definition locator: Definition 28 and Lemma 63.

- Alias `spar_i`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 28; source_checked.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## polyCoordInfluence: coordinate Fourier influence of a fixed polynomial

Symbol: `Inf_i`. Definition status: source_checked.

E[(D_i p)^2] under the uniform full cube, where D_i p(x)=(p(x)-p(x^i))/2; equals sum_{S containing i} p_hat(S)^2.

These are domain/polynomial parameters, not canonical Fourier statistics of an incompletely defined Boolean function.

Definition locator: Definitions 21–22.

- Alias `Inf_i`: [HKMP26](https://arxiv.org/abs/2603.29256), Definitions 21–22; source_checked.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## polyMaxDerivative: maximum coordinate derivative sup norm

Symbol: `max_i ||D_i p||_infinity`. Definition status: source_checked.

Maximum over i and full-cube x of |p(x)-p(x^i)|/2 for a fixed polynomial p.

These are domain/polynomial parameters, not canonical Fourier statistics of an incompletely defined Boolean function. The maximum is an equivalent repository aggregation of the source’s bounds for every coordinate; its literal displayed name is not verified.

Definition locator: Corollary 62.

- Alias `max_i ||D_i p||_infinity`: [HKMP26](https://arxiv.org/abs/2603.29256), Corollary 62; definition_equivalence_checked_literal_name_pending.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## distFlipInfluence: distributional bit-flip squared influence

Symbol: `Inf_i^(lambda)`. Definition status: source_checked.

E_{X drawn from lambda}[(p(X)-p(X flipped at i))^2] for a function p on the entire Boolean cube. The off-support value is used even if lambda is a slice distribution.

Distribution/coordinate parameters stay explicit. This is an averaged squared difference, not maximum disjoint-transposition sensitivity.

Definition locator: Definition 2.5.

- Alias `Inf_i^(lambda)`: [GMNR26](https://arxiv.org/abs/2609.35327), Definition 2.5; source_checked.
- Alias `Inf_i[p]`: [AA14](https://theoryofcomputing.org/articles/v010a006/), Before Conjecture 1.7, p.139; source_checked.

Sources: [GMNR26](https://arxiv.org/abs/2609.35327), [AA14](https://theoryofcomputing.org/articles/v010a006/).

## distTotalInfluence: distributional total bit-flip squared influence

Symbol: `Inf^(lambda)`. Definition status: source_checked.

Sum over coordinates i of E_lambda[(p(X)-p(X flipped at i))^2] for a full-cube function p.

Distribution/coordinate parameters stay explicit. This is an averaged squared difference, not maximum disjoint-transposition sensitivity.

Definition locator: Definition 2.5.

- Alias `Inf^(lambda)`: [GMNR26](https://arxiv.org/abs/2609.35327), Definition 2.5; source_checked.

Sources: [GMNR26](https://arxiv.org/abs/2609.35327).

## distVariance: distributional variance

Symbol: `Var^(lambda)`. Definition status: source_checked.

E_lambda[(p(X)-E_lambda p)^2] for a full-cube function p; only its restriction to the support is needed for variance.

Distribution/coordinate parameters stay explicit. This is an averaged squared difference, not maximum disjoint-transposition sensitivity.

Definition locator: Definition 2.5.

- Alias `Var^(lambda)`: [GMNR26](https://arxiv.org/abs/2609.35327), Definition 2.5; source_checked.

Sources: [GMNR26](https://arxiv.org/abs/2609.35327).

## sliceSwapInfluence: slice transposition squared influence

Symbol: `swInf_(i,j)`. Definition status: source_checked.

E over the uniform k-slice of (p(X)-p(X with coordinates i,j swapped))^2. This depends only on values on the slice.

Distribution/coordinate parameters stay explicit. This is an averaged squared difference, not maximum disjoint-transposition sensitivity.

Definition locator: Lemma 2.6.

- Alias `swInf_(i,j)`: [GMNR26](https://arxiv.org/abs/2609.35327), Lemma 2.6; source_checked.

Sources: [GMNR26](https://arxiv.org/abs/2609.35327).

## degreeOptimalFourierSparsity: degree-optimal bounded exact Fourier sparsity of a partial function

Symbol: `spar`. Definition status: source_checked.

Minimum number of nonzero Walsh coefficients among full-cube [-1,1]-bounded polynomials representing the ±1-valued partial function exactly on its promise, constrained to have minimum possible globally bounded exact degree.

Keep degree optimality, the basis, output encoding and bias convention explicit. These are not ordinary unconstrained approximate monomial sparsity.

Definition locator: Definition 29.

- Alias `spar`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 29; source_checked.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## adegOptimalFourierSparsity: degree-optimal bounded approximate Fourier sparsity of a partial function

Symbol: `tilde spar`. Definition status: source_checked.

Minimum number of nonzero Walsh coefficients among full-cube [-1,1]-bounded polynomials approximating the ±1-valued partial function within 1/3 on its promise, constrained to have minimum possible bounded approximate degree at that error.

Keep degree optimality, the basis, output encoding and bias convention explicit. These are not ordinary unconstrained approximate monomial sparsity.

Definition locator: Definition 29.

- Alias `tilde spar`: [HKMP26](https://arxiv.org/abs/2603.29256), Definition 29; source_checked.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).

## biasedCoordInfluence: biased Fourier coefficient influence

Symbol: `Inf_i`. Definition status: source_checked.

Sum of squared p-biased orthonormal Fourier coefficients indexed by sets containing i. HKMP26 uses p=Pr[x_i=-1], mean mu=1-2p and sigma=2*sqrt(p*(1-p)). This equals sigma^2*E_p[(D_i f)^2].

Keep degree optimality, the basis, output encoding and bias convention explicit. These are not ordinary unconstrained approximate monomial sparsity.

Definition locator: Definitions 22–25 and Lemma 66.

- Alias `Inf_i`: [HKMP26](https://arxiv.org/abs/2603.29256), Definitions 22–25 and Lemma 66; source_checked.

Sources: [HKMP26](https://arxiv.org/abs/2603.29256).
