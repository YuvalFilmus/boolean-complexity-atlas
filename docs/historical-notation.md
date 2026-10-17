# Historical notation register

TeX strings transcribe printed notation; they are not quotations of the authors’ TeX source. Source-dependent cost conventions and parameter conversions are part of the alias. Candidate names and repaired seed attributions remain visible in the JSON and are not silently treated as established occurrences.

| Measure | Name or notation | Source and locator | Normalization / status |
|---|---|---|---|
| D | `deterministic decision-tree complexity` | [BdW02](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf), Section 3.1 | Same measure; source-specific cost/encoding caveats remain in the definition.; source_checked |
| D | `DT` | [LM26](https://dmtcs.episciences.org/en/articles/18512), Section 2; DM23 Section 2 | same definition; source_checked |
| D | `Depth` | [LM26](https://dmtcs.episciences.org/en/articles/18512), Section 2; DM23 Section 2 | same definition; source_checked |
| D | `Depth` | [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 2 | same deterministic query depth; source_checked |
| D | `P^dt` | [GPW18](https://eccc.weizmann.ac.il/report/2015/050/revision/1/), Section 1, query notation | same definition; source_checked |
| D | `D` | [ABK16](https://arxiv.org/abs/1511.01937), Section 2.2 | same definition; source_checked |
| D | `D` | [SW86](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/SW86/SW86.pdf), Section I, p.29 | deterministic query complexity; source_checked |
| D | `D^dt` | [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2: decision-tree and pseudo-deterministic definitions | Depth is worst case; psD^dt is randomized pseudo-deterministic depth despite the letter D. The notation also applies to search relations.; source_checked |
| D | `P^dt(f)` | [Goos15](https://eccc.weizmann.ac.il/report/2015/012/), Sections 1.1–2, pp.2–4 | Total Boolean functions; superscript dt denotes query model.; source_checked |
| R | `R` | [ABK16](https://arxiv.org/abs/1511.01937), Section 2.2 | same definition; source_checked |
| R | `BPP^dt` | [GJPW18](https://eccc.weizmann.ac.il/report/2015/169/), Section 2 | same definition; source_checked |
| R | `R_2` | [Aar02](https://arxiv.org/abs/quant-ph/0210020), Section 1 | Equivalent up to constants; inspect the source’s expected-cost and one-sided conventions.; source_checked |
| R | `Monte Carlo` | [ABBLS17](https://arxiv.org/abs/1506.04719), Section 2, Randomized decision tree algorithms | Expected query cost in this source; source error constants differ from fixed-cap R.; source_checked |
| R | `R^dt` | [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2: decision-tree and pseudo-deterministic definitions | Depth is worst case; psD^dt is randomized pseudo-deterministic depth despite the letter D. The notation also applies to search relations.; source_checked |
| R | `BPP^dt` | [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36), Theorem 4 and Section 2 | Search relations; classical/quantum bounded-error depth and pseudo-deterministic depth, as specified by the stable ID.; source_checked |
| R0 | `R_0` | [ABK16](https://arxiv.org/abs/1511.01937), Section 2.2 | same definition; source_checked |
| R0 | `Las Vegas` | [BdW02](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf), Section 3.3, footnote | Zero-error randomized model; numerical cost convention must be specified.; source_checked |
| R0 | `R` | [SW86](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/SW86/SW86.pdf), Section I, p.29 | Source requires always-correct output and uses worst-case expected queries. R here means modern R0, not bounded-error R.; source_checked |
| R0 | `Las Vegas` | [ABBLS17](https://arxiv.org/abs/1506.04719), Section 2, Randomized decision tree algorithms | Expected query cost in this source; source error constants differ from fixed-cap R.; source_checked |
| R1 | `R_1` | [AIK26](https://arxiv.org/abs/2609.11664), Section 2 | same definition; source_checked |
| Q | `Q` | [ABK16](https://arxiv.org/abs/1511.01937), Section 2.2 | same definition; source_checked |
| Q | `Q_2` | [Aar02](https://arxiv.org/abs/quant-ph/0210020), Section 1 | Equivalent up to constants; inspect the source’s expected-cost and one-sided conventions.; source_checked |
| Q | `Q_{1/3}` | [HS05survey](https://arxiv.org/abs/quant-ph/0509153), Section 2 | Fixed two-sided error 1/3; Q_epsilon is parameterized.; source_checked |
| Q | `Q^dt` | [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36), Theorem 4 and Section 2 | Search relations; classical/quantum bounded-error depth and pseudo-deterministic depth, as specified by the stable ID.; source_checked |
| QE | `Q_E` | [ABK16](https://arxiv.org/abs/1511.01937), Section 2.2 | same definition; source_checked |
| Q0 | `Q_0` | [Aar02](https://arxiv.org/abs/quant-ph/0210020), Section 1 | Equivalent up to constants; inspect the source’s expected-cost and one-sided conventions.; source_checked |
| s | `s` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 31 | same definition; source_checked |
| s | `critical sensitivity` | [Nis89](https://doi.org/10.1145/73007.73038), Publisher abstract | Historical name identified in the original introduction/abstract; later sensitivity definitions fix the normalization.; source_checked |
| s | `s_w(f)` | [Nis89](https://doi.org/10.1145/73007.73038), Section 2, p.330 | Input-local notation, not the global maximum.; source_checked |
| s0 | `s_0` | [ABKBRT21](https://arxiv.org/abs/2010.12629), Appendix A, Lemma 31 | same definition; source_checked |
| s1 | `s_1` | [ABKBRT21](https://arxiv.org/abs/2010.12629), Appendix A, Lemma 31 | same definition; source_checked |
| bs | `bs` | [NS94](https://web.vu.lt/mif/s.jukna/boolean/Nisan-Szegedy.pdf), Definition 3.6 | same definition; source_checked |
| bs | `bs_w(f)` | [Nis89](https://doi.org/10.1145/73007.73038), Section 2, p.330 | Input-local notation, not the global maximum.; source_checked |
| bs0 | `bs_0` | [GSS13](https://arxiv.org/abs/1306.0630), Section 2 | same definition; source_checked |
| bs1 | `bs_1` | [GSS13](https://arxiv.org/abs/1306.0630), Section 2 | same definition; source_checked |
| bs_l | `bs_ell` | [HKP11](https://tocmirror.cs.uchicago.edu/articles/gs004/), Section 3.1 | Same measure; source-specific cost/encoding caveats remain in the definition.; source_checked |
| bs_l | `ell-block sensitivity` | [HKP11](https://tocmirror.cs.uchicago.edu/articles/gs004/), Section 3.1 | Same measure; source-specific cost/encoding caveats remain in the definition.; source_checked |
| C | `certificate size` | [BdW02](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf), Section 2.2 | Same measure; source-specific cost/encoding caveats remain in the definition.; source_checked |
| C | `C` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 22 | same definition; source_checked |
| C | `N` | [SW86](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/SW86/SW86.pdf), Section I, p.31 | Nondeterministic complexity means maximum over both output orientations, modern C.; source_checked |
| C | `HSC` | [CDMRS23](https://doi.org/10.1145/3564246.3585199), Definition 2.4 | A set hits every minimal sensitive block iff fixing it certifies the target value.; source_checked |
| C | `C_w(f)` | [Nis89](https://doi.org/10.1145/73007.73038), Section 2, p.330 | Input-local notation, not the global maximum.; source_checked |
| C0 | `C^0` | [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 1 notation paragraph | same definition; source_checked |
| C0 | `C_0` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 22 | same definition; source_checked |
| C0 | `CNF width` | [GPW18](https://eccc.weizmann.ac.il/report/2015/050/revision/1/), Section 1, complement of nondeterministic model | Minimum width over CNFs; follows by complementing the DNF characterization.; source_checked |
| C0 | `coNP^dt(f)` | [Goos15](https://eccc.weizmann.ac.il/report/2015/012/), Sections 1.1–2, pp.2–4 | Total Boolean functions; superscript dt denotes query model.; source_checked |
| C1 | `C^1` | [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 1 notation paragraph | same definition; source_checked |
| C1 | `NP^dt` | [GPW18](https://eccc.weizmann.ac.il/report/2015/050/revision/1/), Section 1, query notation | same definition; source_checked |
| C1 | `C_1` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 22 | same definition; source_checked |
| C1 | `DNF width` | [GPW18](https://eccc.weizmann.ac.il/report/2015/050/revision/1/), Section 1 | Minimum width over DNFs for a total function.; source_checked |
| C1 | `C^(1)(f)` | [Nis89](https://doi.org/10.1145/73007.73038), Section 4, p.333 | As defined in the original.; source_checked |
| C1 | `NP^dt(f)` | [Goos15](https://eccc.weizmann.ac.il/report/2015/012/), Sections 1.1–2, pp.2–4 | Total Boolean functions; superscript dt denotes query model.; source_checked |
| fbs | `fbs` | [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 2 | same definition; source_checked |
| fbs | `bs^*` | [GSS13](https://arxiv.org/abs/1306.0630), Section 2 | Fractional block packing LP.; source_checked |
| FC | `FC` | [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 2 | same definition; source_checked |
| FC | `C^*` | [GSS13](https://arxiv.org/abs/1306.0630), Section 2 and Appendix A | Fractional certificate LP; within constants of RC and exactly dual to fbs.; source_checked |
| FC | `randomized certificate complexity` | [FLLV20notes](https://yuvalfilmus.cs.technion.ac.il/Talks/ComplexityMeasures-HUJI.pdf), Section 2, p.3, immediately after the certificate LP relaxation | Here the literal name labels the fractional covering LP, numerically FC. This must not identify its exact value with Aar02 operational expected-query RC; the measures are only constant-factor equivalent under the stored verifier convention.; source_checked |
| RC | `RC` | [Aar02](https://arxiv.org/abs/quant-ph/0210020), Definition 3 | same definition; source_checked |
| QC | `QC` | [Aar02](https://arxiv.org/abs/quant-ph/0210020), Definition 3 | same definition; source_checked |
| UC | `UC` | [AIK26](https://arxiv.org/abs/2609.11664), Section 2 | same definition; source_checked |
| UC | `2UP^dt` | [GPW18](https://eccc.weizmann.ac.il/report/2015/050/revision/1/), Section 1, query notation | same definition; source_checked |
| UC | `subcube partition complexity` | [AKK16](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2016.4), Introduction, query complexity | Minimum maximum codimension, not logarithm of the number of partition parts.; source_checked |
| UC0 | `UC_0` | [AIK26](https://arxiv.org/abs/2609.11664), Section 2 | same definition; source_checked |
| UC0 | `coUP^dt` | [GPW18](https://eccc.weizmann.ac.il/report/2015/050/revision/1/), Section 1, query notation | same definition; source_checked |
| UC1 | `UC_1` | [AIK26](https://arxiv.org/abs/2609.11664), Section 2 | same definition; source_checked |
| UC1 | `UP^dt` | [GPW18](https://eccc.weizmann.ac.il/report/2015/050/revision/1/), Section 1, query notation | same definition; source_checked |
| UC1 | `one-sided subcube partition complexity` | [AKK16](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2016.4), Introduction, quantum query complexity | Positive side; complement gives the other orientation.; source_checked |
| UC1 | `UP^dt(f)` | [Goos15](https://eccc.weizmann.ac.il/report/2015/012/), Sections 1.1–2, pp.2–4 | Total Boolean functions; superscript dt denotes query model.; source_checked |
| UCmin | `UC_min` | [AIK26](https://arxiv.org/abs/2609.11664), Section 2 | same definition; source_checked |
| deg | `deg` | [NS94](https://web.vu.lt/mif/s.jukna/boolean/Nisan-Szegedy.pdf), Definition 1.1 | same definition; source_checked |
| deg | `Fourier degree` | [NS94](https://web.vu.lt/mif/s.jukna/boolean/Nisan-Szegedy.pdf), Definition 1.1; representation by real polynomials | Same measure; source-specific cost/encoding caveats remain in the definition.; source_checked |
| deg | `real degree` | [NS94](https://web.vu.lt/mif/s.jukna/boolean/Nisan-Szegedy.pdf), Definition 1.1; representation by real polynomials | Same measure; source-specific cost/encoding caveats remain in the definition.; definition_equivalence_checked_literal_name_pending |
| deg | `Fourier-degree` | [ABKBRT21](https://arxiv.org/abs/2010.12629), Section 2.3 | Equal degree under the source’s Fourier encoding.; source_checked |
| deg | `gdeg` | [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Definition 2.11 and Remark 2.12 | Generalized subcube-indicator degree equals ordinary degree by replacing every complement variable with 1-x_i. Approximate version has pointwise error 1/3.; source_checked |
| adeg | `\widetilde{deg}` | [ABK16](https://arxiv.org/abs/1511.01937), Section 2.2 | same definition; source_checked |
| adeg | `approximate polynomial degree` | [ABK16](https://arxiv.org/abs/1511.01937), Section 2.2 | Same measure; source-specific cost/encoding caveats remain in the definition.; source_checked |
| adeg | `tilde gdeg` | [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Definition 2.11 and Remark 2.12 | Generalized subcube-indicator degree equals ordinary degree by replacing every complement variable with 1-x_i. Approximate version has pointwise error 1/3.; source_checked |
| adeg_eps | `\widetilde{deg}_epsilon` | [BT17](https://arxiv.org/abs/1703.05784), Section 2.1 | Signed target in this source: epsilon signed error corresponds to epsilon/2 for a 0/1 target.; source_checked |
| adeg_bounded | `\widetilde{deg}_epsilon` | [ABKBRT21](https://arxiv.org/abs/2010.12629), Section 2.3 | Bounded range on Boolean inputs; source epsilon convention. This occurrence belongs to adeg_bounded, not unrestricted adeg_eps.; source_checked |
| lambda | `lambda` | [ABKBRT21](https://arxiv.org/abs/2010.12629), Section 3 | same definition; source_checked |
| lambda | `K` | [ABKBRT21](https://arxiv.org/abs/2010.12629), Appendix A.1, Theorem 28 | Koutsoupias complexity, with norm unsquared; square gives formula-size lower bound.; source_checked |
| lambda | `Adv_1` | [ABKBRT21](https://arxiv.org/abs/2010.12629), Appendix A.1, Theorem 28 | Single-bit positive adversary, equal to lambda.; source_checked |
| lambda | `Adv_1^{pm}` | [ABKBRT21](https://arxiv.org/abs/2010.12629), Appendix A.1, Theorem 28 | Single-bit negative adversary, equal to lambda.; source_checked |
| lambda | `SA_1` | [ABKBRT21](https://arxiv.org/abs/2010.12629), Appendix A.1, Theorem 28 | Single-bit restrictions of the respective adversary formulations; equal to lambda, not to the unrestricted adversary.; source_checked |
| lambda | `SWA_1` | [ABKBRT21](https://arxiv.org/abs/2010.12629), Appendix A.1, Theorem 28 | Single-bit restrictions of the respective adversary formulations; equal to lambda, not to the unrestricted adversary.; source_checked |
| lambda | `MM_1` | [ABKBRT21](https://arxiv.org/abs/2010.12629), Appendix A.1, Theorem 28 | Single-bit restrictions of the respective adversary formulations; equal to lambda, not to the unrestricted adversary.; source_checked |
| lambda | `GSA_1` | [ABKBRT21](https://arxiv.org/abs/2010.12629), Appendix A.1, Theorem 28 | Single-bit restrictions of the respective adversary formulations; equal to lambda, not to the unrestricted adversary.; source_checked |
| rdeg | `rational degree` | [IJKKSWW23](https://arxiv.org/abs/2310.08004), Introduction and definitions | Same measure; source-specific cost/encoding caveats remain in the definition.; source_checked |
| rdeg | `rdeg` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 37 | same definition; source_checked |
| ndeg | `ndeg` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 36 | same definition; source_checked |
| AdvPlus | `Adv` | [BK19](https://arxiv.org/abs/1902.03660), Section 1.1 | Same measure; source-specific cost/encoding caveats remain in the definition.; source_checked |
| AdvPlus | `positive adversary` | [BK19](https://arxiv.org/abs/1902.03660), Section 1.1 | Same measure; source-specific cost/encoding caveats remain in the definition.; definition_equivalence_checked_literal_name_pending |
| AdvPlus | `MM` | [BK19](https://arxiv.org/abs/1902.03660), Section 1.1 and references to equivalent formulations | same definition; source_checked |
| AdvPlus | `SA` | [ABKBRT21](https://arxiv.org/abs/2010.12629), Definition 8 | positive spectral adversary; source_checked |
| AdvGeneral | `Adv^{\pm}` | [ABK16](https://arxiv.org/abs/1511.01937), Section 2; general-adversary characterization cited in Section 5 | The spectral norm is used; the general adversary differs from the positive-weight bound. Original HLS/LMRSS source reconciliation is in the bibliography queue.; source_checked |
| AdvGeneral | `negative-weight adversary bound` | [ABK16](https://arxiv.org/abs/1511.01937), Section 2; general-adversary characterization cited in Section 5 | The spectral norm is used; the general adversary differs from the positive-weight bound. Original HLS/LMRSS source reconciliation is in the bibliography queue.; source_checked |
| AdvGeneral | `ADV^{pm}` | [HLS07](https://arxiv.org/abs/quant-ph/0611054), Definition 2 | TeX transcription of the printed plus/minus superscript; signed spectral adversary.; source_checked |
| QD | `QD` | [BK19](https://arxiv.org/abs/1902.03660), Definition 5, PDF p.7 | Trace distance is half the Schatten 1-norm. DQA is attributed to Barnum–Saks–Szegedy 2001 Remark 1 in Section 1.1; retain that historical attribution separately.; source_checked |
| QD | `DQA` | [BK19](https://arxiv.org/abs/1902.03660), Definition 5, PDF p.7 | Trace distance is half the Schatten 1-norm. DQA is attributed to Barnum–Saks–Szegedy 2001 Remark 1 in Section 1.1; retain that historical attribution separately.; source_checked |
| QSZK | `QSZK` | [BK19](https://arxiv.org/abs/1902.03660), Definition 14, PDF p.12 | This is the complete-problem-based state-distance definition, not an automatically identical interactive-protocol cost.; source_checked |
| RS | `RS` | [CG22](https://arxiv.org/abs/2211.03396), Definition 5.6 | Zero-error expected queries. Oracle alphabet {0,1,*,dagger}; underlying f may be partial. Original definition: Ben-David–Kothari randomized query composition and sabotage complexity.; source_checked |
| QS | `QS_{weak}` | [CMP24](https://arxiv.org/abs/2408.12595), Section 2 and Definition 1 | Do not identify with QD. BK19 suggests the name quantum sabotage for QD, whereas CMP24 studies four distinct sabotage oracle/output variants.; source_checked |
| QS | `QS` | [CMP24](https://arxiv.org/abs/2408.12595), Section 1.1, before the four-model split | Initially Q(f_sab), the weak-input distinguishing model. Later unqualified QS may refer schematically to a selected variant; retain the model subscript when making comparisons.; source_checked |
| CGpub | `CG^{pub}` | [CG22](https://arxiv.org/abs/2211.03396), Definition 2.4 | Possibly partial f. This is inverse probability, not its logarithm.; source_checked |
| CGpriv | `CG^{priv}` | [CG22](https://arxiv.org/abs/2211.03396), Definition 2.3 | Possibly partial f. This is inverse probability, not its logarithm.; source_checked |
| CGent | `CG^*` | [CG22](https://arxiv.org/abs/2211.03396), Definition 2.5 | Possibly partial f. This is inverse probability, not its logarithm.; source_checked |
| CGns | `CG^{ns}` | [CG22](https://arxiv.org/abs/2211.03396), Definitions 2.1 and 2.6 | Possibly partial f. This is inverse probability, not its logarithm.; source_checked |
| conical | `\widetilde{deg}^{+2}` | [BK24](https://arxiv.org/abs/2410.16245), Definition 12, decision-function specialization | As in the cited definition.; source_checked |
| conical | `conical junta degree` | [BK24](https://arxiv.org/abs/2410.16245), Definition 12, decision-function specialization | As in the cited definition.; source_checked |
| rel_adeg | `\widetilde{deg}` | [BK24](https://arxiv.org/abs/2410.16245), Definition 10, PDF pp.11–12 | Default epsilon=1/3. Positivity and normalization also hold off-promise. Single-output-function degree is a separate specialization.; source_checked |
| Rexp | `RE` | [KLW14](https://arxiv.org/abs/1411.7280), Section 2.3 and Theorem 9 | f maps the full cube to nonnegative reals. This is not expected running time.; source_checked |
| Qexp | `QE` | [KLW14](https://arxiv.org/abs/1411.7280), Section 2.3 and Theorem 12 | Source QE collides with exact quantum query complexity Q_E. Preserve the distinction by stable IDs.; source_checked |
| literaldeg | `ldeg_+` | [KLW14](https://arxiv.org/abs/1411.7280), Section 2.3 and Theorem 9 | As in the cited definition.; source_checked |
| sosdeg | `deg_sos` | [KLW14](https://arxiv.org/abs/1411.7280), Section 2.3 and Theorem 12 | The roots have degree d; the sum of squares has formal degree at most 2d. Other SOS conventions count 2d.; source_checked |
| psR | `psR` | [AGL26](https://doi.org/10.4230/LIPIcs.ICALP.2026.3), Definitions 2.1–2.2 | The canonical selector may depend on the algorithm, but cannot depend on its random coins or measurement outcomes.; source_checked |
| psR | `psD^dt` | [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2: decision-tree and pseudo-deterministic definitions | Depth is worst case; psD^dt is randomized pseudo-deterministic depth despite the letter D. The notation also applies to search relations.; source_checked |
| psR | `psP^dt` | [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36), Theorem 4 and Section 2 | Search relations; classical/quantum bounded-error depth and pseudo-deterministic depth, as specified by the stable ID.; source_checked |
| psQ | `psQ` | [AGL26](https://doi.org/10.4230/LIPIcs.ICALP.2026.3), Definitions 2.1–2.2 | The canonical selector may depend on the algorithm, but cannot depend on its random coins or measurement outcomes.; source_checked |
| psQ | `psQ^dt` | [GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36), Theorem 4 and Section 2 | Search relations; classical/quantum bounded-error depth and pseudo-deterministic depth, as specified by the stable ID.; source_checked |
| blocknumber | `N_b` | [CG26](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.61), Definitions 3–4 | KT13 Section 5 uses nbs. The size-ell version counts blocks of size at most ell in CG26, unlike exact-size nbs_k in KT13.; source_checked |
| blocknumber | `nbs` | [CG26](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.61), Definitions 3–4 | KT13 Section 5 uses nbs. The size-ell version counts blocks of size at most ell in CG26, unlike exact-size nbs_k in KT13.; source_checked |
| blocknumber | `#bs` | [CDMRS23](https://doi.org/10.1145/3564246.3585199), Definition 2.4 | Number of minimal sensitive blocks, not a maximum disjoint packing.; source_checked |
| bricknumber | `N_{br}` | [CG26](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.61), Definitions 7–8 | A brick need not itself be a sensitive block when |B|>1. Do not replace the defining condition by minimal sensitivity.; source_checked |
| rel_conical | `\widetilde{deg}^{+2}` | [BK24](https://arxiv.org/abs/2410.16245), Definition 12 | As in the cited definition.; source_checked |
| rel_conical | `conical junta degree` | [BK24](https://arxiv.org/abs/2410.16245), Definition 12 | As in the cited definition.; source_checked |
| rel_conical | `two-sided conical junta degree` | [BK24](https://arxiv.org/abs/2410.16245), Definition 12 | As in the cited definition.; source_checked |
| mbs | `mbs` | [BJKM24](https://arxiv.org/abs/2406.07859), Definitions 5–8 | Defined for arbitrary total f. This is not merely ordinary complexity restricted to monotone f.; source_checked |
| mbs | `bs_0` | [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2, lines 235–245 | Flip only input-zero coordinates; NOT the maximum over zero-output inputs. The source expressly identifies these with monotone sensitivity / monotone block sensitivity on total Boolean functions.; source_checked |
| mbs | `bs_0` | [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), Section 2: directed sensitivity definitions | Subscript is the value of the input bits being flipped, not an output restriction. Final Theorem 5.2 uses this convention.; source_checked |
| mbs | `MBS` | [KLMY21](https://doi.org/10.1145/3406325.3450999), Section 2.1 | Monotone block sensitivity on the upward restriction at each input.; source_checked |
| mbs | `bs^{0→1}` | [CDM25](https://doi.org/10.1007/s00037-025-00266-7), Section 2 and Theorem 6.1 | Direction of input-coordinate flips, not output value.; source_checked |
| fmbs | `fmbs` | [BJKM24](https://arxiv.org/abs/2406.07859), Definitions 5–8 | Defined for arbitrary total f. This is not merely ordinary complexity restricted to monotone f.; source_checked |
| fmbs | `FHSC_0` | [CDMRS23](https://doi.org/10.1145/3564246.3585199), Definition 2.6 | Fractional hitting-set LP dual to the fractional packing of sensitive input-zero blocks. Not output-zero fractional block sensitivity.; source_checked |
| fmbs | `FHSC` | [KLMY21](https://doi.org/10.1145/3406325.3450999), Definition 2.13 | Fractional input-directed hitting-set LP, equal to FMBS. Interpret the printed smallest-p wording using the explicitly stated LP and largest feasible p.; source_checked |
| fmbs | `FMBS` | [KLMY21](https://doi.org/10.1145/3406325.3450999), Section 2.1 | Fractional monotone block sensitivity, equal by LP duality to FHSC.; source_checked |
| MCC | `MCC` | [BJKM24](https://arxiv.org/abs/2406.07859), Definitions 5–8 | Defined for arbitrary total f. This is not merely ordinary complexity restricted to monotone f.; source_checked |
| MCC | `hitting set complexity` | [BJKM24](https://arxiv.org/abs/2406.07859), Definitions 5–8 | Defined for arbitrary total f. This is not merely ordinary complexity restricted to monotone f.; source_checked |
| MCC | `HSC_0` | [CDMRS23](https://doi.org/10.1145/3564246.3585199), Definition 2.5 | Hit every sensitive block consisting of input-zero positions, at every input. This matches monotone certificate complexity, not output-zero C0.; source_checked |
| MCC | `HSC` | [KLMY21](https://doi.org/10.1145/3406325.3450999), Definition 2.10 | Input-zero/upward sensitive blocks. CDMRS23 uses bare HSC for ordinary C and HSC_0 for this quantity.; source_checked |
| ms | `ms` | [BJKM24](https://arxiv.org/abs/2406.07859), Definitions 5–8 | Defined for arbitrary total f. This is not merely ordinary complexity restricted to monotone f.; source_checked |
| ms | `s_0` | [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2, lines 235–245 | Flip only input-zero coordinates; NOT the maximum over zero-output inputs. The source expressly identifies these with monotone sensitivity / monotone block sensitivity on total Boolean functions.; source_checked |
| ms | `s_0` | [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), Section 2: directed sensitivity definitions | Subscript is the value of the input bits being flipped, not an output restriction. Final Theorem 5.2 uses this convention.; source_checked |
| DTSize | `DTSize` | [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 2 | same definition; source_checked |
| DTSize | `DSize^dt` | [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2: decision-tree and pseudo-deterministic definitions | Depth is worst case; psD^dt is randomized pseudo-deterministic depth despite the letter D. The notation also applies to search relations.; source_checked |
| DTRank | `Rank` | [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 2 | same definition; source_checked |
| DTRank | `Strahler number` | [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 1 | First a rooted-tree statistic; function measure minimizes over computing trees.; source_checked |
| DTRank | `Horton-Strahler number` | [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 1 | First a rooted-tree statistic; function measure minimizes over computing trees.; source_checked |
| DTRank | `tree rank` | [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 1 | First a rooted-tree statistic; function measure minimizes over computing trees.; source_checked |
| DTRank | `rank` | [CDMRS23](https://doi.org/10.1145/3564246.3585199), Definition 2.10 | Minimum Strahler rank of a correct deterministic tree.; source_checked |
| DTRank | `rank` | [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Definition 3 | Strahler rank; randomized rank takes the maximum rank in the support.; source_checked |
| DTRank | `r(f)` | [EH89](https://doi.org/10.1016/0890-5401(89)90001-1), Definition p.241 | As defined in the original.; source_checked |
| sparsity | `spar` | [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 2, Fourier representation, PDF p.6 | As in the cited definition.; source_checked |
| ANDD | `D_wedge` | [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 7, AND-decision tree model | This source model uses monotone conjunctions; do not silently allow arbitrary negated literals.; source_checked |
| IC | `InstC` | [LM26](https://dmtcs.episciences.org/en/articles/18512), Definition 2.3 | Competitive ratio. Constant functions require a separate zero-denominator convention; source results involving them are stated separately.; source_checked |
| hazardD | `D_u` | [BKMNSS25](https://arxiv.org/abs/2507.00148), Definition 2.1 | Input and output alphabets are ternary. The symbol u is a queried value, distinct from an unrevealed coordinate.; source_checked |
| hazardR | `R_u` | [BKMNSS25](https://arxiv.org/abs/2507.00148), Definition 2.5 | Input and output alphabets are ternary. The symbol u is a queried value, distinct from an unrevealed coordinate.; source_checked |
| hazardQ | `Q_u` | [BKMNSS25](https://arxiv.org/abs/2507.00148), Definition 2.6 | Input and output alphabets are ternary. The symbol u is a queried value, distinct from an unrevealed coordinate.; source_checked |
| rdeg_eps | `rdeg_epsilon` | [IJKKSWW23](https://arxiv.org/abs/2310.08004), Introduction and Section 2 | Explicit error and denominator nonvanishing condition; no off-promise bound is imposed here.; source_checked |
| PostQ | `PostQ_epsilon` | [IJKKSWW23](https://arxiv.org/abs/2310.08004), Section 2, postselection definitions | The postselection success probability need not be inverse polynomial.; source_checked |
| PostQE | `PostQ_E` | [IJKKSWW23](https://arxiv.org/abs/2310.08004), Section 2 and Appendix A | Exact conditioned output; not zero-error quantum query complexity Q_0.; source_checked |
| PostQE | `PostEQP query complexity` | [IJKKSWW23](https://arxiv.org/abs/2310.08004), Section 2 and Appendix A | Exact conditioned output; not zero-error quantum query complexity Q_0.; source_checked |
| QSweakIndex | `QS^{ind}_{weak}` | [CMP24](https://arxiv.org/abs/2408.12595), Section 2; four-variant definitions | All component input queries count; source access conventions retained.; source_checked |
| QSstrong | `QS_{str}` | [CMP24](https://arxiv.org/abs/2408.12595), Section 2; four-variant definitions | All component input queries count; source access conventions retained.; source_checked |
| QSstrongIndex | `QS^{ind}_{str}` | [CMP24](https://arxiv.org/abs/2408.12595), Section 2; four-variant definitions | All component input queries count; source access conventions retained.; source_checked |
| CGpubSingle | `CG^{pub}_{[1]}` | [CG22](https://arxiv.org/abs/2211.03396), Section 8, Theorems 8.4 and 8.8 | As in the cited definition.; source_checked |
| CGprivSingle | `CG^{priv}_{[1]}` | [CG22](https://arxiv.org/abs/2211.03396), Section 8, Theorems 8.4 and 8.8 | As in the cited definition.; source_checked |
| CAdv | `CAdv` | [BK24](https://arxiv.org/abs/2410.16245), Definition 14 | CG22 Definition 4.2 uses probability-normalized CMM; its equivalent normalization is recorded. Total-function CAdv=FC does not extend to all partial functions.; source_checked |
| CAdv | `CMM` | [BK24](https://arxiv.org/abs/2410.16245), Definition 14 | CG22 Definition 4.2 uses probability-normalized CMM; its equivalent normalization is recorded. Total-function CAdv=FC does not extend to all partial functions.; source_checked |
| EC | `EC` | [CG22](https://arxiv.org/abs/2211.03396), Definition 4.5 | The source extends this definition to partial functions. Distinct from randomized query complexity in expectation.; source_checked |
| rel_udeg | `\widetilde{udeg}` | [BK24](https://arxiv.org/abs/2410.16245), Definition 11 | No off-promise boundedness. Do not conflate with bounded relation degree.; source_checked |
| rel_deg | `deg` | [BK24](https://arxiv.org/abs/2410.16245), Definition 10, epsilon=0 | As in the cited definition.; source_checked |
| rel_Adv | `Adv` | [BK24](https://arxiv.org/abs/2410.16245), Definition 13 | As in the cited definition.; source_checked |
| rel_CAdv | `CAdv` | [BK24](https://arxiv.org/abs/2410.16245), Definition 14 | As in the cited definition.; source_checked |
| rel_bs | `bs` | [BK24](https://arxiv.org/abs/2410.16245), Definition 15 | As in the cited definition.; source_checked |
| rel_cbs | `cbs` | [BK24](https://arxiv.org/abs/2410.16245), Definition 16 | As in the cited definition.; source_checked |
| rel_fbs | `fbs` | [BK24](https://arxiv.org/abs/2410.16245), Definition 17 | As in the cited definition.; source_checked |
| rel_fcbs | `fcbs` | [BK24](https://arxiv.org/abs/2410.16245), Definition 17 | As in the cited definition.; source_checked |
| blocknumber_l | `N_b^{ell}` | [CG26](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.61), Definition 4 | As in the cited definition.; source_checked |
| bricknumber_l | `N_{br}^{ell}` | [CG26](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.61), Definition 8 | As in the cited definition.; source_checked |
| sparsityNonempty | `\widetilde{spar}` | [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 2, Fourier representation, PDF p.6 | As in the cited definition.; source_checked |
| Cmin | `C_min` | [LM26](https://dmtcs.episciences.org/en/articles/18512), Definition 2.2 | K in DM23 is unrelated to the Koutsoupias spectral-sensitivity alias K.; source_checked |
| Cmin | `subcube kill number` | [LM26](https://dmtcs.episciences.org/en/articles/18512), Definition 2.2 | K in DM23 is unrelated to the Koutsoupias spectral-sensitivity alias K.; source_checked |
| Cmin | `K` | [LM26](https://dmtcs.episciences.org/en/articles/18512), Definition 2.2 | K in DM23 is unrelated to the Koutsoupias spectral-sensitivity alias K.; source_checked |
| hazardS | `s_u` | [BKMNSS25](https://arxiv.org/abs/2507.00148), Definition 2.2 | Input and output alphabets are ternary. The symbol u is a queried value, distinct from an unrevealed coordinate.; source_checked |
| hazardBS | `bs_u` | [BKMNSS25](https://arxiv.org/abs/2507.00148), Definition 2.3 | Input and output alphabets are ternary. The symbol u is a queried value, distinct from an unrevealed coordinate.; source_checked |
| hazardC | `cc_u` | [BKMNSS25](https://arxiv.org/abs/2507.00148), Definition 2.4 | Input and output alphabets are ternary. The symbol u is a queried value, distinct from an unrevealed coordinate.; source_checked |
| Qnegligent | `Q^{neg}_{p,epsilon}` | [ARS26](https://arxiv.org/abs/2610.00506), Section 1, equations (1.4) and (1.6) | Fix p and epsilon explicitly; query-index dephasing differs from oracle negligence.; source_checked |
| Qdephasing | `Q^{deph}_{p,epsilon}` | [ARS26](https://arxiv.org/abs/2610.00506), Section 1, equations (1.4) and (1.6) | Fix p and epsilon explicitly; query-index dephasing differs from oracle negligence.; source_checked |
| cubeBoundedDeg | `deg` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 7 | For partial f this differs from unrestricted exact degree. The source uses the same symbol deg; the stable ID distinguishes them.; source_checked |
| cubeBoundedDeg | `deg` | [AB23](https://doi.org/10.4230/LIPIcs.CCC.2023.24), Section 2.1 | Exact representing polynomial is in [0,1] on the entire cube, including off-promise inputs; this is not unrestricted promise interpolation degree.; source_checked |
| cubeBoundedAdeg | `\widetilde{deg}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 7 | same definition; source_checked |
| cubeBoundedAdeg | `tilde deg` | [AB23](https://doi.org/10.4230/LIPIcs.CCC.2023.24), Section 2.1 | AB23 explicitly says approximate degree can be defined analogously but does not require it. Its detailed representing-polynomial definition is for exact degree; do not count this as a verified literal approximate-degree alias.; definition_convention_checked_not_literal_alias |
| boundedPolyDelta | `Delta_{epsilon0,epsilon1,beta}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 7 | All three parameters are explicit.; source_checked |
| osdeg0 | `\widehat{osdeg}^0` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 7 | same definition; source_checked |
| osdeg1 | `\widehat{osdeg}^1` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 7 | same definition; source_checked |
| osdeg | `\widehat{osdeg}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 7 | Distinct from one-sided approximation notions allowing unbounded values on the other side.; source_checked |
| bmAdeg | `\widehat{bm-deg}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 38 | Source error/encoding follows Definition 38. Each monomial uses exactly one variable from each block.; source_checked |
| D_cert | `D^{cert}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12 | The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.; source_checked |
| R_cert | `R^{cert}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12 | The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.; source_checked |
| R0_cert | `R_0^{cert}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12 | The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.; source_checked |
| QE_cert | `Q_E^{cert}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12 | The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.; source_checked |
| Q0_cert | `Q_0^{cert}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12 | The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.; source_checked |
| Q_cert | `Q^{cert}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12 | The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.; source_checked |
| QD_cert | `QD^{cert}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12 | The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.; source_checked |
| AdvPlus_cert | `Adv^{cert}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12 | The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.; source_checked |
| RS_cert | `RS^{cert}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12 | The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.; source_checked |
| QS_cert | `QS_{weak}^{cert}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12 | The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.; source_checked |
| EC_cert | `EC^{cert}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12 | The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.; source_checked |
| UC_cert | `UC^{cert}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12 | The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.; source_checked |
| CAdv_cert | `CAdv^{cert}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12 | The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.; source_checked |
| cubeBoundedDeg_cert | `deg^{cert}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12 | The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.; source_checked |
| cubeBoundedAdeg_cert | `\widetilde{deg}^{cert}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12 | The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.; source_checked |
| osdeg_cert | `\widehat{osdeg}^{cert}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12 | The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.; source_checked |
| lambda_cert | `lambda^{cert}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12 | The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.; source_checked |
| rdeg_cert | `rdeg^{cert}` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definitions 1–2 and corresponding Theorems 3–12 | The certification problem always has a promise, even when the parent f is total. Preserve the base degree’s off-promise boundedness convention.; source_checked |
| signDeg | `deg_{\pm}` | [KKWY26](https://arxiv.org/abs/2601.08727v3), Definition 3 | Source conventions use sign (-1)^f. Nonconstant Boolean inputs are the intended setting.; source_checked |
| nRelevant | `n(f)` | [Wel22](https://arxiv.org/abs/2005.00566v2), Section 2 | Does not count dummy input variables; distinguish from ambient input length n.; source_checked |
| nRelevant | `R(f)` | [CHS20](https://doi.org/10.1007/s00493-019-4136-7), Introduction, p.1 | Number of relevant variables, not randomized query complexity.; source_checked |
| Dweighted | `Depth_w` | [DM23](https://www.imsc.res.in/~meena/papers/rank-tcs.pdf), Section 2, weighted decision trees | Coordinate weights are part of the measure’s parameters.; source_checked |
| RCmin | `RC_min` | [KKWY26](https://arxiv.org/abs/2601.08727v3), Definition 10 | same definition; source_checked |
| fbsmin | `fbs_min` | [KKWY26](https://arxiv.org/abs/2601.08727v3), Definition 10 | same definition; source_checked |
| RCminDown | `RC_min^downarrow` | [KKWY26](https://arxiv.org/abs/2601.08727v3), Definition 11 | same definition; source_checked |
| fbsminDown | `fbs_min^downarrow` | [KKWY26](https://arxiv.org/abs/2601.08727v3), Definition 11 | same definition; source_checked |
| fbs_at0 | `fbs(f,0^n)` | [ARS26](https://arxiv.org/abs/2610.00506), Theorem 1.1 and Section 2 | same definition; source_checked |
| fbs0 | `fbs^0` | [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 1 notation and Section 2 definitions | same definition; source_checked |
| fbs1 | `fbs^1` | [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 1 notation and Section 2 definitions | same definition; source_checked |
| FC0 | `FC^0` | [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 1 notation and Section 2 definitions | same definition; source_checked |
| FC1 | `FC^1` | [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 1 notation and Section 2 definitions | same definition; source_checked |
| RC0 | `RC^0` | [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 1 notation and Section 2 definitions | same definition; source_checked |
| RC1 | `RC^1` | [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 1 notation and Section 2 definitions | same definition; source_checked |
| QC0 | `QC^0` | [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 1 notation and Section 2 definitions | same definition; source_checked |
| QC1 | `QC^1` | [KT13](https://eccc.weizmann.ac.il/report/2013/168/), Section 1 notation and Section 2 definitions | same definition; source_checked |
| cfbs_boolean | `cfbs` | [KLLPV26](https://arxiv.org/abs/2609.26757), Definition 35 | ; source_checked |
| Cset | `C_Sigma` | [Bal21](https://arxiv.org/abs/2103.05593v1), Section 1 | Output sets 0,1,bar0={1,*},bar1={0,*}.; source_checked |
| Cbar0 | `C_{\bar{0}}` | [Bal21](https://arxiv.org/abs/2103.05593v1), Section 1 | Repository-qualified names; the source uses the displayed notation for ternary output functions. Not weak promise certificates.; source_checked |
| Cbar1 | `C_{\bar{1}}` | [Bal21](https://arxiv.org/abs/2103.05593v1), Section 1 | Repository-qualified names; the source uses the displayed notation for ternary output functions. Not weak promise certificates.; source_checked |
| Cstrong | `C` | [Bal21](https://arxiv.org/abs/2103.05593v1), Section 1 | Repository-qualified names; the source uses the displayed notation for ternary output functions. Not weak promise certificates.; source_checked |
| Q_eps | `Q_epsilon` | [HLS07](https://arxiv.org/abs/quant-ph/0611054), Section 2 | Q is the specialization epsilon=1/3, up to the source oracle convention.; source_checked |
| V | `V` | [AGL26](https://doi.org/10.4230/LIPIcs.ICALP.2026.3), ICALP introduction before Theorem 5 | This need not be small for an arbitrary total relation. TFNP in the query model additionally requires short, locally checkable solution certificates.; source_checked |
| input1s | `s_1` | [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2, lines 235–245 | Input direction, not an output-conditioned maximum. Applies also to multi-output functions.; source_checked |
| input1s | `s_1` | [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), Section 2: directed sensitivity definitions | Subscript is the value of the input bits being flipped, not an output restriction. Final Theorem 5.2 uses this convention.; source_checked |
| input1bs | `bs_1` | [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2, lines 235–245 | Input direction, not an output-conditioned maximum.; source_checked |
| input1bs | `bs_1` | [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), Section 2: directed sensitivity definitions | Subscript is the value of the input bits being flipped, not an output restriction. Final Theorem 5.2 uses this convention.; source_checked |
| RSize | `RSize^dt` | [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2, lines 275–277 | Worst support size, not expected size and not random seed length.; source_checked |
| Ddist | `D^dt_{mu,epsilon}` | [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2, lines 278–282 | The parameters mu and epsilon are part of the measure.; source_checked |
| DSizeDist | `DSize^dt_{mu,epsilon}` | [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2, lines 278–283 | Different from averaging query cost over mu.; source_checked |
| psDTSize | `psDSize^dt` | [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 2, lines 296–305 | Worst support size, not expected size. The algorithm must output one fixed valid selector value with high probability.; source_checked |
| DandPos | `D^wedge-dt` | [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 6, lines 660–664 | An entire positive and query costs one. These are different measures from bit-query complexity.; source_checked |
| DandPos | `P^{wedge-dt}` | [KLMY21](https://doi.org/10.1145/3406325.3450999), Introduction and Claim 4.4 | P denotes deterministic positive-conjunction query depth, not a polynomial-time class parameter.; source_checked |
| DandPos | `D^{dt}_{AND}` | [LM19](https://doi.org/10.4230/LIPIcs.STACS.2019.50), Definition 10 | Zero-answer depth and positive-conjunction depth for search relations. The subscript 0 is a cost convention, not an error probability.; source_checked |
| RandPos | `R^wedge-dt` | [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 6, lines 660–664 | An entire positive and query costs one. These are different measures from bit-query complexity.; source_checked |
| psRandPos | `psD^wedge-dt` | [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 6, lines 660–664 | An entire positive and query costs one. These are different measures from bit-query complexity.; source_checked |
| Dpar | `D^oplus-dt` | [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 6, lines 660–664 | An entire parity query costs one. These are different measures from bit-query complexity.; source_checked |
| Rpar | `R^oplus-dt` | [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 6, lines 660–664 | An entire parity query costs one. These are different measures from bit-query complexity.; source_checked |
| psRpar | `psD^oplus-dt` | [CDM23full](https://eccc.weizmann.ac.il/report/2023/039/), Section 6, lines 660–664 | An entire parity query costs one. These are different measures from bit-query complexity.; source_checked |
| DandOr | `D^{(wedge,vee)-dt}` | [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), Section 5, before Proposition 5.1 | Both subset queries cost one; do not identify with bit queries or conjunctions of arbitrary signed literals.; source_checked |
| RandOr | `R^{(wedge,vee)-dt}` | [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), Section 5, before Proposition 5.1 | Both subset queries cost one; do not identify with bit queries or conjunctions of arbitrary signed literals.; source_checked |
| psRandOr | `psD^{(wedge,vee)-dt}` | [CDM23](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34), Section 5, before Proposition 5.1 | Both subset queries cost one; do not identify with bit queries or conjunctions of arbitrary signed literals.; source_checked |
| DzeroDepth | `D^{0-dt}` | [CDMRS23](https://doi.org/10.1145/3564246.3585199), Section 2.2 | Zero-answer cost, not zero-error randomized complexity.; source_checked |
| DzeroDepth | `P^{0-dt}` | [KLMY21](https://doi.org/10.1145/3406325.3450999), Section 4.2, Claim 4.4 | Deterministic count of zero answers; not a zero-error randomized measure.; source_checked |
| DzeroDepth | `D^{dt}_0` | [LM19](https://doi.org/10.4230/LIPIcs.STACS.2019.50), Definition 9 | Zero-answer depth and positive-conjunction depth for search relations. The subscript 0 is a cost convention, not an error probability.; source_checked |
| RzeroDepth | `R^{0-dt}_{epsilon}` | [CDMRS23](https://doi.org/10.1145/3564246.3585199), Section 2.2 | Counts zero answers along paths; NOT R0, the expected cost of a zero-error algorithm.; source_checked |
| rrank | `rrank` | [CDMRS23](https://doi.org/10.1145/3564246.3585199), Definitions 2.9–2.10 | Support maximum, not expected rank; deterministic rank is DTRank.; source_checked |
| rrank | `rrank` | [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Definition 3 | Strahler rank; randomized rank takes the maximum rank in the support.; source_checked |
| coverN0 | `N_0` | [CDMRS23](https://doi.org/10.1145/3564246.3585199), Definition 2.2 | Counts subcubes, not certificate width; zero for an empty output fibre.; source_checked |
| coverN1 | `N_1` | [CDMRS23](https://doi.org/10.1145/3564246.3585199), Definition 2.2 | Counts subcubes, not certificate width; zero for an empty output fibre.; source_checked |
| coverN | `N` | [CDMRS23](https://doi.org/10.1145/3564246.3585199), Definition 2.2 | Unbounded counts are distinct from certificate widths and logarithms of cover counts.; source_checked |
| DTNodes | `DTSize` | [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Introduction, Corollary 9 and Appendix A.1 | CMP22 counts nodes; CDM23/CDMRS23 count leaves. For full binary trees DTNodes=2 DTSize(repository leaf count)-1. Do not use the same source typography to assert identical normalizations.; source_checked |
| RNodes | `RDTSize` | [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Corollary 27; Appendix A.1 | Whole-node count, not leaf count or expected size. RNodes=2 RSize-1 under full binary tree conventions.; source_checked |
| rel_Qeps | `Q_epsilon` | [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Theorem 5 and Corollary 27 | CMP22 uses epsilon=2/5 for randomized-tree simulations. Arbitrary relations do not automatically admit majority error reduction; this is separate from decision Q_eps and default search Q at error 1/3.; source_checked |
| DTGuess | `G` | [CMP22](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.15), Definitions 10–11 and Claim 12 | The source defines G(T) for a tree; this catalogue additionally minimizes it over valid trees. Claim 12 identifies tree guessing complexity with tree Strahler rank. No new source notation G(f) is asserted. Printed G(T), not the repository function-level minimum.; source_checked |
| Bbomb | `B` | [LL16](https://theoryofcomputing.org/articles/v012a018/), Section 3 and Theorem 4.1 | Fixed error constants; the source shorthand B is used only up to its constant-error equivalence.; source_checked |
| BbombParams | `B_{epsilon,delta}` | [LL16](https://theoryofcomputing.org/articles/v012a018/), Section 3 and Theorem 4.1 | Both error budgets are explicit; 0<epsilon<=delta in the usual regime. The source total-error requirement is not error conditioned on survival.; source_checked |
| monomialSparsity | `spar` | [KLMY21](https://doi.org/10.1145/3406325.3450999), Introduction before Theorem 1.1 | The 0/1 monomial basis, not the Walsh Fourier basis. KLMY21 separately uses Fourier sparsity when discussing XOR-functions.; source_checked |
| approxMonomialSparsity | `tilde spar` | [KLMY21survey](https://cseweb.ucsd.edu/~shmcguir/papers/KLMYsigact.pdf), Definition 3.18 | Approximation on the full cube and sparsity in the 0/1 monomial basis, not Walsh approximate Fourier sparsity.; source_checked |
| monomialWeight | `wt` | [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Definitions 2.2–2.3 | ; source_checked |
| approxMonomialWeight | `tilde wt` | [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Definition 2.5 | ; source_checked |
| generalizedSparsity | `gspar` | [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Definitions 2.9–2.11 | ; source_checked |
| approxGeneralizedSparsity | `tilde gspar` | [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Definitions 2.9–2.11 | ; source_checked |
| generalizedWeight | `gwt` | [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Definitions 2.9–2.11 | ; source_checked |
| approxGeneralizedWeight | `tilde gwt` | [Sparse25](https://eccc.weizmann.ac.il/report/2025/172/), Definitions 2.9–2.11 | ; source_checked |
| NisR2expect | `R_2` | [Nis89](https://doi.org/10.1145/73007.73038), Section 1.2, p.329 | ; source_checked |
| NisR1expect | `R_1` | [Nis89](https://doi.org/10.1145/73007.73038), Section 1.2, p.329 | ; source_checked |
| permD | `D` | [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Introduction and Section 2.2 | ; source_checked |
| permDegree | `deg` | [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Introduction and Section 2.2 | ; source_checked |
| permAdeg | `tilde deg` | [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Introduction and Section 2.2 | ; source_checked |
| permS | `s` | [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Introduction and Section 2.2 | ; source_checked |
| permEdgeS | `t` | [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Introduction and Section 2.2 | ; source_checked |
| permBS | `bs` | [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Introduction and Section 2.2 | ; source_checked |
| completion_D | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic source template, explicitly instantiated here with M=D. The instantiated display symbol is repository notation, not a separate literal occurrence.; source_checked |
| completion_R0 | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic source template, explicitly instantiated here with M=R0. The instantiated display symbol is repository notation, not a separate literal occurrence.; source_checked |
| completion_R | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic source template, explicitly instantiated here with M=R. The instantiated display symbol is repository notation, not a separate literal occurrence.; source_checked |
| completion_C | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic source template, explicitly instantiated here with M=C. The instantiated display symbol is repository notation, not a separate literal occurrence.; source_checked |
| completion_RC | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic source template, explicitly instantiated here with M=RC. The instantiated display symbol is repository notation, not a separate literal occurrence.; source_checked |
| completion_bs | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic source template, explicitly instantiated here with M=bs. The instantiated display symbol is repository notation, not a separate literal occurrence.; source_checked |
| completion_s | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic source template, explicitly instantiated here with M=s. The instantiated display symbol is repository notation, not a separate literal occurrence.; source_checked |
| completion_lambda | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic source template, explicitly instantiated here with M=lambda. The instantiated display symbol is repository notation, not a separate literal occurrence.; source_checked |
| completion_QE | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic source template, explicitly instantiated here with M=QE. The instantiated display symbol is repository notation, not a separate literal occurrence.; source_checked |
| completion_deg | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic source template, explicitly instantiated here with M=deg. The instantiated display symbol is repository notation, not a separate literal occurrence.; source_checked |
| completion_Q | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic source template, explicitly instantiated here with M=Q. The instantiated display symbol is repository notation, not a separate literal occurrence.; source_checked |
| completion_adeg | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic source template, explicitly instantiated here with M=adeg. The instantiated display symbol is repository notation, not a separate literal occurrence.; source_checked |
| promiseS | `s prime` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 15 | ; source_checked |
| promiseBS | `bs prime` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 15 | ; source_checked |
| criticalBScompletion | `cbs` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 18 | ; source_checked |
| criticalCertificate | `C_cri` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 19 | ; source_checked |
| permC | `C` | [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Section 2.2 | ; source_checked |
| permUC | `U` | [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Section 2.2 | ; source_checked |
| permFBS | `fbs` | [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Section 2.2 | ; source_checked |
| permR | `R` | [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Section 2.2 | ; source_checked |
| permRfail23 | `R_0` | [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Section 2.2 | ; source_checked |
| permQ | `Q` | [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Section 2.2 | ; source_checked |
| permQE | `Q_E` | [DFLLV21](https://doi.org/10.4230/LIPIcs.ITCS.2021.87), Section 2.2 | ; source_checked |
| completion_nRelevant | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic overline-M template instantiated at relevant-variable count.; source_checked |
| completion_C0 | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic overline-M template instantiated at M=C0.; source_checked |
| completion_C1 | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic overline-M template instantiated at M=C1.; source_checked |
| completion_UC | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic overline-M template instantiated at M=UC.; source_checked |
| completion_UC0 | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic overline-M template instantiated at M=UC0.; source_checked |
| completion_UC1 | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic overline-M template instantiated at M=UC1.; source_checked |
| completion_fbs | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic overline-M template instantiated at M=fbs.; source_checked |
| completion_FC | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic overline-M template instantiated at M=FC.; source_checked |
| completion_QC | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic overline-M template instantiated at M=QC.; source_checked |
| completion_Q0 | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic overline-M template instantiated at M=Q0.; source_checked |
| completion_R1 | `overline M` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 45, p.22 | Generic overline-M template instantiated at M=R1.; source_checked |
| domainD | `D` | [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2 | ; source_checked |
| domainR | `R` | [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2 | ; source_checked |
| domainRfail23 | `R_0` | [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2 | ; source_checked |
| domainQ | `Q` | [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2 | ; source_checked |
| domainQE | `Q_E` | [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2 | ; source_checked |
| domainDegree | `deg` | [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2 | ; source_checked |
| domainAdeg | `tilde deg` | [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2 | ; source_checked |
| domainC | `C` | [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2 | ; source_checked |
| domainUC | `U` | [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2 | ; source_checked |
| domainBS | `bs` | [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2 | ; source_checked |
| domainFBS | `fbs` | [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2 | ; source_checked |
| domainS | `s` | [DFLLV22author](https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf), Sections 2.1–2.2 | ; source_checked |
| domainS | `s_2(f)` | [BD16](https://doi.org/10.4230/LIPIcs.TQC.2016.7), Definition 7 | Packing sensitivity for disjoint sensitive two-coordinate blocks on a single multislice; equals domain chunk sensitivity there.; source_checked |
| domainCoverRadius | `r_C` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 61 | ; source_checked |
| polyCoordSparsity | `spar_i` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 28 | ; source_checked |
| polyCoordInfluence | `Inf_i` | [HKMP26](https://arxiv.org/abs/2603.29256), Definitions 21–22 | ; source_checked |
| polyMaxDerivative | `max_i ||D_i p||_infinity` | [HKMP26](https://arxiv.org/abs/2603.29256), Corollary 62 | ; definition_equivalence_checked_literal_name_pending |
| distFlipInfluence | `Inf_i^(lambda)` | [GMNR26](https://arxiv.org/abs/2609.35327), Definition 2.5 | ; source_checked |
| distFlipInfluence | `Inf_i[p]` | [AA14](https://theoryofcomputing.org/articles/v010a006/), Before Conjecture 1.7, p.139 | Uniform cube; unnormalized squared flip difference. Equals four times the HKMP26 derivative-normalized influence for the same full-cube function.; source_checked |
| distTotalInfluence | `Inf^(lambda)` | [GMNR26](https://arxiv.org/abs/2609.35327), Definition 2.5 | ; source_checked |
| distVariance | `Var^(lambda)` | [GMNR26](https://arxiv.org/abs/2609.35327), Definition 2.5 | ; source_checked |
| sliceSwapInfluence | `swInf_(i,j)` | [GMNR26](https://arxiv.org/abs/2609.35327), Lemma 2.6 | ; source_checked |
| degreeOptimalFourierSparsity | `spar` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 29 | ; source_checked |
| adegOptimalFourierSparsity | `tilde spar` | [HKMP26](https://arxiv.org/abs/2603.29256), Definition 29 | ; source_checked |
| biasedCoordInfluence | `Inf_i` | [HKMP26](https://arxiv.org/abs/2603.29256), Definitions 22–25 and Lemma 66 | ; source_checked |
