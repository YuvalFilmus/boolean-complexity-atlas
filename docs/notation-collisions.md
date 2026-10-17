# Notation collisions

Exact display-string collisions only; visually equivalent TeX is not normalized. A collision does not assert equivalence.

- `Adv`: AdvPlus, rel_Adv.
- `C`: C, Cstrong, domainC, permC.
- `CAdv`: CAdv, rel_CAdv.
- `D`: D, domainD, permD.
- `DTSize`: DTNodes, DTSize.
- `HSC`: C, MCC.
- `Inf_i`: biasedCoordInfluence, polyCoordInfluence.
- `K`: Cmin, lambda.
- `N`: C, coverN.
- `Q`: Q, domainQ, permQ.
- `Q_E`: QE, domainQE, permQE.
- `Q_epsilon`: Q_eps, rel_Qeps.
- `R`: R, R0, domainR, permR.
- `R_0`: R0, domainRfail23, permRfail23.
- `R_1`: NisR1expect, R1.
- `R_2`: NisR2expect, R.
- `U`: domainUC, permUC.
- `\widetilde{deg}`: adeg, cubeBoundedAdeg, rel_adeg.
- `\widetilde{deg}^{+2}`: conical, rel_conical.
- `\widetilde{deg}_epsilon`: adeg_bounded, adeg_eps.
- `bs`: bs, domainBS, permBS, rel_bs.
- `bs_0`: bs0, mbs.
- `bs_1`: bs1, input1bs.
- `cbs`: criticalBScompletion, rel_cbs.
- `conical junta degree`: conical, rel_conical.
- `deg`: cubeBoundedDeg, deg, domainDegree, permDegree, rel_deg.
- `fbs`: domainFBS, fbs, permFBS, rel_fbs.
- `overline M`: completion_C, completion_C0, completion_C1, completion_D, completion_FC, completion_Q, completion_Q0, completion_QC, completion_QE, completion_R, completion_R0, completion_R1, completion_RC, completion_UC, completion_UC0, completion_UC1, completion_adeg, completion_bs, completion_deg, completion_fbs, completion_lambda, completion_nRelevant, completion_s.
- `s`: domainS, permS, s.
- `s_0`: ms, s0.
- `s_1`: input1s, s1.
- `spar`: degreeOptimalFourierSparsity, monomialSparsity, sparsity.
- `tilde deg`: cubeBoundedAdeg, domainAdeg, permAdeg.
- `tilde spar`: adegOptimalFourierSparsity, approxMonomialSparsity.

# Measure families

These are parameterized constructions or discovery groupings, rather than single scalar measures.

[
  {
    "id": "certification",
    "name": "certification transform",
    "definition": "For a measure M defined on partial Boolean functions, M^cert(f)=max_z M(f_z^cert), where f_z^cert accepts z and rejects all inputs with opposite f-value.",
    "source": "KLLPV26",
    "locator": "Definitions 1–2"
  },
  {
    "id": "CGsingle",
    "name": "single-bit certificate game variants",
    "definition": "Restrict the input pairs of a certificate game to Hamming distance one; retain the randomness/resource model.",
    "source": "CG22",
    "locator": "Section 8"
  },
  {
    "id": "noisyQ",
    "name": "noisy-oracle quantum query models",
    "definition": "Separate measures for negligent, dephasing, and hybrid oracle access; these models are not interchangeable.",
    "source": "ARS26",
    "locator": "Section 1"
  }
]
