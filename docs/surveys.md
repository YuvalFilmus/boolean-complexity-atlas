# Annotated surveys

Generated from the source catalogue. These are entry points, not certifications of current best bounds.

## BdW02

Harry Buhrman, Ronald de Wolf. [Complexity measures and decision tree complexity: a survey](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf) (2002).

Start here for classical definitions, elementary inequalities, and historical attribution. Predates cheat sheets and Huang; historical best bounds require updates.

## HKP11

Pooya Hatami, Raghav Kulkarni, Denis Pankratov. [Variations on the Sensitivity Conjecture](https://tocmirror.cs.uchicago.edu/articles/gs004/) (2011).

Variants, equivalent formulations, constructions, and links to Fourier and communication complexity. Read its open questions as historical statements from before 2019.

## Amb18

Andris Ambainis. [Understanding Quantum Algorithms via Query Complexity](https://arxiv.org/abs/1712.06349) (2017).

Invited survey of quantum algorithms, classical/quantum gaps, promises, and symmetric functions. This record cites the 2017 preprint; proceedings metadata remains to be reconciled.

## BT22

Mark Bun, Justin Thaler. [Approximate Degree in Classical and Quantum Computing](https://open.bu.edu/items/88330d18-3f1f-4fc4-8552-17e432f8475f) (2022).

Main polynomial-method reference: approximation, dual witnesses, composition, and applications. Use the publication year 2022; the repository deposit is dated 2023.

## KSP20

Rohan Karthikeyan, Siddharth Sinha, Vallabh Patil. [On the resolution of the sensitivity conjecture](https://arxiv.org/abs/1912.05406) (2020).

Exposition of the ideas leading to Huang’s proof; complements the pre-resolution survey HKP11. Bulletin of the American Mathematical Society, DOI 10.1090/bull/1697.

## Aar21survey

Scott Aaronson. [Open Problems Related to Quantum Query Complexity](https://www.scottaaronson.com/papers/open.pdf) (2021).

Problem-oriented companion survey. Sections 4–5 discuss maximal gaps and globally bounded polynomial degree for partial functions. Its open-problem status is historical as of 2021; later resolutions must be linked separately.

## HS05survey

Peter Høyer, Robert Špalek. [Lower Bounds on Quantum Query Complexity](https://arxiv.org/abs/quant-ph/0509153) (2005).

Survey of polynomial and adversary lower-bound methods, their proof mechanisms and limitations. Predates negative-weight adversaries, general-adversary tightness, and cheat sheets; use as a historical techniques reference.

## LS21survey

Lily Li, Morgan Shirley. [The General Adversary Bound: A Survey](https://arxiv.org/abs/2104.06380) (2021).

Focused exposition of the general adversary characterization: lower-bound progress arguments, semidefinite duality, span-program witness size and the upper-bound algorithm. Useful proof-level companion to HLS07 and LMRSS11; cite original results for priority.

## KLMY21survey

Alexander Knop, Shachar Lovett, Sam McGuire, Weiqiang Yuan. [Guest Column: Models of Computation between Decision Trees and Communication](https://cseweb.ucsd.edu/~shmcguir/papers/KLMYsigact.pdf) (2021).

Survey of parity and positive-conjunction query models and their connections to communication. Source for model distinctions and dated questions; later size derandomization results are in CDMRS23. Communication claims remain outside the initial scalar bit-query core.

## Results papers with useful overview tables

[ABK16](https://arxiv.org/abs/1511.01937), Section 2.3, and [ABKBRT21](https://arxiv.org/abs/2010.12629), Table 1. Both require forward-citation updates before their tables are treated as current.


## Promise and search reading routes

For promises, combine Amb18 and Aar21survey with the polynomial conventions in AB23 and ABK21. For search, BK24, GIPS21, CDM23 and AGL26 provide useful introductory comparisons and precise definitions; they remain research papers rather than survey entries. See [the search audit](search-problems.md) and [the promise audit](partial-functions.md).
