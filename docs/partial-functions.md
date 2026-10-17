# Partial Boolean functions: conventions, comparisons and proofs

The [promise matrix](partial-matrix.md) has an evidence record for each of the 132 ordered off-diagonal pairs in its twelve-measure vocabulary. There are 49 finite entries, with matching power exponents, and 83 pairs for which no finite exponent exists. This completes that specified matrix, not the inventory of all promise measures, aliases or results. In particular, bounded polynomials, strong certificates, distributional costs and adversary variants need additional comparisons outside this grid.

The matrix concerns arbitrary promise domains in the Boolean cube, including total domains. All growth comparisons use A=O(max(1,B)^p); this prevents zero graph sensitivity from creating an undefined exponent comparison. Its lower witnesses have a numerator tending to infinity while the denominator stays bounded. This is stronger than merely exhibiting an exponential gap at one input length.

## Definitions that change a comparison

A weak certificate for x only excludes opposite-output inputs **inside the promise**. A strong certificate refers to an extension or full-cube subcube condition; see the separate certificate IDs. Promise block sensitivity packs disjoint changes x→x^B whose endpoints are both promised and have different outputs. The sensitivity graph uses only promised adjacent opposite-output pairs. Its norm can therefore be zero for a nonconstant function.

`deg` and `adeg` in the matrix impose their value/approximation requirements only on the promise. They impose no bounds elsewhere. `cubeBoundedDeg` and `cubeBoundedAdeg` require the polynomial to lie in [0,1] everywhere on the Boolean cube. AB23 Section 2.1 calls the former simply “degree”; this source occurrence is registered under the globally bounded ID. ABK21 uses globally bounded approximate degree, as its definition explicitly specifies.

`R0` is maximum-over-input expected query cost of an always-correct classical algorithm. `R`, `Q` and `QE` use a worst-case query cap. Truncating a Las Vegas algorithm gives R=O(R0), including on promises; an exact quantum cap cannot be obtained by that truncation.

## Explicit counterexample families

All families are defined in `data/catalog.json`, with growth bounds, proof summaries and stable witness IDs. Consequences repeated for different pairs are separate claim records, not separate discoveries or independent literature results.

### Zero or a unit vector (`promise-unit-OR`)

Promise weight zero or one and compute OR. The unrestricted polynomial sum x_i has degree one. At zero, all m singleton changes are sensitive, so s=bs=C=Theta(m). Fractional certificates and fixed-target verification give RC=Theta(m). Classical randomized search takes Theta(m) queries. The promised sensitivity graph is a star, with norm sqrt(m).

Quantum search takes Theta(sqrt(m)) queries. For the exact upper bound, run amplitude amplification tuned to marked fraction 1/m and verify its returned index. If one mark exists it is found with certainty; if no mark exists verification rejects. [BHMT02](https://arxiv.org/abs/quant-ph/0005055), Theorem 4, supplies the exact amplification. The star adversary gives the matching lower bound. Thus s, bs and RC can all be quadratic in Q and QE; s can be quadratic in lambda. It also disproves control of sensitivity, block sensitivity and verification by unrestricted promise degree.

### Doubled parity (`promise-doubled-parity`)

Promise that consecutive pairs agree and compute parity of the m decoded bits. There are no promised pairs at distance one, so s=lambda=0. Flipping whole pairs gives bs=m. Substituting one decoded variable for both members of each pair turns any promise approximant into an approximant for total parity, forcing degree m. All query costs, certificate costs and verification costs in the core are linear. This disproves every nontrivial core measure's polynomial control by the promised adjacency measures. The remaining s/lambda comparisons themselves follow from maximum degree and the star subgraph bound.

### Dense disjoint halves (`promise-dense-two-axes`)

On 2m bits, promise either (a,0) with |a|>=ceil(m/2), or (0,b) with |b|>=ceil(m/2); output the nonzero half. Any 1 position is a one-bit weak certificate. Sampling until a 1 is seen is always correct and takes at most four queries in expectation. Hence R0, R, Q, C, RC and bs are bounded, whereas D, QE and exact unrestricted degree grow linearly.

For the exact-degree lower bound, symmetrize a representing polynomial on each coordinate half separately, obtaining univariate polynomials u(t) and v(t) with u(0)=v(0). Each equals its required constant at all weights ceil(m/2),...,m, and the constants differ. If both degrees were below floor(m/2)+1, root counting would force both to be constant, contradicting their agreement at zero. Thus degree is Omega(m), as are QE and D by the polynomial method. Reading all bits proves the upper bounds. This is an explicit repository derivation; no first-discovery attribution is claimed.

### Nonempty disjoint halves (`promise-nonempty-two-axes`)

Allow every nonempty string in the nonzero half. Again C=RC=fbs=bs=1 and s=lambda=0, but even unrestricted approximate degree is Omega(sqrt(m)). To see this, amplify a proposed promise approximant to error 1/12 by a constant-degree polynomial on the two fixed separated approximation intervals. Subtract its restrictions p(0,z)-p(z,0), choosing the sign according to the side label. This difference is zero at z=0 and within 1/6 of one at every nonzero z. It therefore approximates total OR, requiring degree Omega(sqrt(m)). The same argument with exact representations forces degree m by root counting. In particular, small weak certificates do not bound promise approximate degree. This is also a repository derivation, not an original-source priority claim.

### Projective-plane lines (`promise-projective-plane`)

Promise the zero vector or a line-incidence vector in a finite projective plane of order t. Any two lines intersect, so bs=1. Assign each line fractional weight 1/(t+1): each point lies on t+1 lines, giving fbs=Theta(t). Consequently RC is unbounded despite bs=1. A fixed line meets every other line, so querying its t+1 points decides the function. This also gives linear-in-t C and classical query costs; unrestricted degree is one. The construction and its sharp input-length tradeoff are [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 17. Theorem 15 proves fbs<=sqrt(n bs). The factor sqrt(n) must not be erased.

### Restricted Deutsch–Jozsa (`promise-restricted-DJ`)

Promise zero or a balanced string of even length m. Preparing the uniform state, applying input phases and measuring its overlap with the uniform state distinguishes the cases exactly with one phase query. At zero, a weak certificate needs m/2+1 zero positions, giving linear C, D and R0. Random sampling gives bounded R and RC. The unrestricted polynomial 2|x|/m is exact of degree one. The phase-query proof here is explicit; [DJ92](https://doi.org/10.1098/rspa.1992.0167) is the historical problem citation, not a claim to have audited the modern one-query circuit in the original article.

### Unique mark color (`promise-unique-mark-color`)

Promise one marked bit and ask which half contains it. The marked position gives C=RC=fbs=bs=1, while the complete bipartite classical adversary proves R=Omega(m). This is [AKPVZ18](https://arxiv.org/abs/1709.08985v3), Theorem 9. It is precisely why the total-function identity CAdv=FC cannot be applied to partial functions.

### Extremal Forrelation (`promise-extremal-forrelation`)

[GS26](https://doi.org/10.4230/LIPIcs.ITCS.2026.72), Theorem 4, gives exact quantum cost one in its joint phase-oracle convention versus randomized cost tildeOmega(2^(n/4)); the truth tables contain 2^(n+1) bits. Converting to a standard bit oracle changes the quantum query count by at most a constant. The lower bound uses bent functions and linear algebra. Its earlier Simon/Hadamard-encoding antecedents and the paper's stronger conjectures are retained as priority information; this catalogue does not assign first priority to all constant-query exact separations to GS26.

## Beyond the matrix

[AB23](https://doi.org/10.4230/LIPIcs.CCC.2023.24) proves Q can exceed even globally bounded exact degree by more than every fixed power: bounded degree O(log N), Q=tildeOmega(N^(1/3)). It uses threshold satisfiability and a negative-weight adversary for tripartite shift. [BK24](https://arxiv.org/abs/2410.16245) strengthens the polynomial/conical side using bounded approximate polynomial systems and a search-to-decision conversion.

[ABK21](https://doi.org/10.4230/LIPIcs.CCC.2021.30) proves Adv<=CAdv<=2 Adv² and Adv=O(bounded approximate degree²) for partial functions. Its final Lemmas 26–27 give cfbs/2<=CAdv<=cfbs. The final proof corrects a spurious factor two in the preprint weight construction, so the published constants can be recorded without the earlier discrepancy. Keep `cfbs_boolean` separate from relation critical fractional sensitivity.

The remaining work is not hidden by the complete core promise grid: globally bounded polynomial/strong-certificate comparisons, all historical names, noisy and distributional variants, restricted promise classes, and complete original-priority chains still require further extraction and review.
