# Hypermatching degree/sensitivity: independent priority audit

Checked 23 October 2026. This is a targeted literature check, **not a novelty certification**. No public catalogue edits were made by this reviewer.

## Finding

I did not locate an earlier statement of either the full fixed-edge-size hypermatching inequality

$$
\deg_{\mathcal H}(f)\le(2k-1)s_{\mathcal H}(f)^2
$$

or the general colored-domain comparison

$$
2\deg_{\mathcal H}(f)\le\deg_{\prod_i S_{\lambda_i n}}(f\circ\pi)\le k\deg_{\mathcal H}(f).
$$

This permits the carefully qualified label **derived research note; prior publication not located in the sources searched**. It does not justify “first proof”, “new theorem”, or “resolved the authors' conjecture” without author confirmation and wider citation searching. The special case k=2 is already covered, with better sensitivity constants, by existing permutation/perfect-matching results.

## Closest original sources checked

1. Neta Dafni, Yuval Filmus, Noam Lifshitz, Nathan Lindzey, Marc Vinyals, *Complexity measures on the symmetric group and beyond*, Combinatorial Theory 6(2), #6 (2026), 60 pp., DOI https://doi.org/10.5070/C6.68665 . Checked the full locally captured journal text `work/sources/DFLLV26journal.txt`, rather than abstract-only inference. Section 4.2 (article pp.24–26) defines exactly the full lambda-partite perfect-hypermatching domains under discussion. Section 5 opening (article p.29, PDF p.30) expressly excludes hypergraphical perfect-matching domains from its sensitivity method because their representation decomposition is not sufficiently understood. Its direct sensitivity results concern products, permutations, ordinary perfect matchings and multislices. Section 8 (article pp.48–49) does not supply a later hypermatching sensitivity theorem. The degree averaging/quotient argument is not stated there. Its known k=2 theorems remain the relevant special-case priority.

2. Same authors, author manuscript dated 13 May 2022, https://yuvalfilmus.cs.technion.ac.il/Papers/measures.pdf , locally `work/sources/DFLLV22author.txt`. Sections 4.2 and 5 contain the same domain and exclusion. This is an earlier version of the same work, not an independent recurrence or new priority candidate.

3. Yuval Filmus, Noam Lifshitz, Nathan Lindzey, Marc Vinyals, 24 June 2020 notes/talk, https://yuvalfilmus.cs.technion.ac.il/Talks/ComplexityMeasures-HUJI.pdf . Locally captured notes `work/question-status-oct23/FLLV20notes.txt`, closing section 7. These explicitly leave the hypergraphical sensitivity extension open. The wording does not quantify whether the intended coefficient must be uniform in k, or demand an intrinsic pseudo-character family. Therefore the research note should say it proves a precise fixed-k quadratic version, not claim to settle every interpretation of that closing question.

4. Original ITCS extended abstract, *Complexity Measures on the Symmetric Group and Beyond*, ITCS 2021, LIPIcs 185, 87:1–87:5, DOI https://doi.org/10.4230/LIPIcs.ITCS.2021.87 , https://drops.dagstuhl.de/storage/00lipics/lipics-vol185-itcs2021/LIPIcs.ITCS.2021.87/LIPIcs.ITCS.2021.87.pdf . Metadata and abstract checked. It directs to arXiv:2010.07405; it is not evidence for an additional general hypermatching theorem.

5. Sara Asensio, Yuval Filmus, Ignacio García-Marco, Kolja Knauer, *Sensitivity and Hamming Graphs*, Journal of Graph Theory 112(3), 296–305 (2026), DOI https://doi.org/10.1002/jgt.70034 . Primary publisher full-text sections 4–5 checked. Its degree/sensitivity theorem concerns finite-alphabet product domains and a different polynomial degree/sensitivity convention. It does not state the lambda-partite hypermatching quotient theorem. Its references give a route to graph-based generalized-sensitivity literature, but graph maximum-degree sensitivity cannot be identified with disjoint native-change packing sensitivity without proof.

## Why classical ingredients do not themselves settle priority

The uniform-fiber average is a finite-group Reynolds operator. Injective-assignment inclusion–exclusion is the classical Möbius formula on the partition lattice. These are established techniques and should not be advertised as invented here. The specific use of singleton-vertex relations J_{\{v\}}=1 gives the half-degree descent in this coordinate filtration; I did not retrieve an earlier statement of that consequence for all lambda-partite domains. Standard quotient and Foulkes-module descriptions alone do not prove the exact filtration comparison, and multiplicity decompositions or plethysm results concern another question.

The product-permutation sensitivity step is a derived tensor-product application of the published permutation pseudo-character method, not a verbatim theorem for products in the cited paper. The final proof must present that extension explicitly; the independent mathematical audit is responsible for verifying it.

## Search record and limitations

Primary search queries included:

- `"hypergraphical" "sensitivity" matchings degree`
- `"hypermatchings" "sensitivity" degree`
- `"hypermatching" "degree" "sensitivity"`
- `"hypergraphical" "Huang"`
- `"perfect matchings" "quotient" "degree" polynomials sensitivity`
- `"hypermatchings" "Boolean functions"`
- `"sensitivity" "uniform partitions" Boolean degree`
- `"hypermatching" "polynomial" Boolean functions degree`
- `"perfect matching domains" "sensitivity"` excluding the two known author hosts
- `"Foulkes" "degree" "Boolean functions"`
- `"Boolean" "set partitions" "sensitivity"`
- `"hypermatchings" "invariant" polynomials`
- `"perfect hypermatchings" "degree" sensitivity`

The directly relevant retrieved original work was DFLLV and its versions. Hidden (hyper)matching communication-complexity papers, ordinary graph matching polynomials and hypergraph degree-sequence problems are different models. Generalized Foulkes-module papers concern characters, not the target comparison. I did not exhaust theses, informal correspondence, all papers citing DFLLV, or non-indexed manuscripts. No theorem should be called novel on the strength of negative searches.
