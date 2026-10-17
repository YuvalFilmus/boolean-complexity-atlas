# Query domains and their parameters

Sources: DFLLV22author, Sections 2.1,2.3.2 and 5.1; corresponding definitions and selected bounds checked in final journal DFLLV26 (60 article pages).

- Composability and alpha-witnessing are separate assumptions.
- All parameter values are source bounds unless explicitly exact.
- No uniform scalar upper bound is inferred by dropping n/M, Delta, beta or alpha.

## Definitions

- **n**: Common cardinality of each set input x in X, not the size of the ambient indicator cube.
- **c**: Minimum positive |x minus y| over distinct x,y in X.
- **Delta**: Maximum number of allowed queries mentioning a universe element.
- **M**: Largest threshold <=n such that every pair of conflicting partial inputs, each of size <=M, is separated by a query.
- **beta**: Largest factor guaranteeing at least beta*|x minus y| distinct z_j with x minus z_j strictly contained in x minus y and pairwise disjoint y minus z_j.
- **beta_c**: Same shortening condition as beta, requiring |y minus z_j|=c.
- **alpha**: A witnessing parameter: degree-d pseudo-characters induce Boolean cubes of dimension at least alpha*d.

## Domain profiles

| Domain | Query | c | Delta | M | beta | beta_c | alpha |
|---|---|---:|---|---|---|---|---|
| Product H(m_1,...,m_n) | Reveal coordinate i. | 1 | 1 | n | 1 | 1 | 1 |
| Symmetric group S_n | Reveal pi(i) or inverse pi(j). | 2 | 2 | n | 1/3 | 1/3 | 1/2 |
| Perfect matchings of K_(2n) | Reveal the partner of a vertex. | 2 | 2 | n | >=1/3 | >=1/3 | 1 |
| P(n;lambda) | Reveal the hyperedge containing a vertex. | 2 | \|lambda\| | n | >=1/(\|lambda\|*(\|lambda\|-1)+1) | not bounded here for \|lambda\|>2 | not established by this source |
| M(lambda): words with fixed color multiplicities | Reveal coordinate color. | 2 | 1 | floor(min(lambda)/2) | >=1/3 | >=1/3 | 1/2 |
| k-slice of {0,1}^n | Reveal a coordinate bit. | 2 | 1 | floor(min(k,n-k)/2) | >=1/2 | 1/2 | 1/2 |
| Partitions of kn vertices into n unordered k-sets (lambda=(k)) | Reveal the block containing a vertex. | 2 | k | n | >=1/(k*(k-1)+1) | not needed for the lift | not asserted; use permutation sensitivity lift |

The same underlying set can have different query families. S_n with both forward and inverse queries is different from the all-distinct multislice with forward-only coordinate queries. The latter can have linear deterministic complexity at degree one.

- P(n;lambda): The source does not establish beta_c or alpha for this whole family. A separately audited repository product-permutation query lift gives D<=10368*(2k-1)^10*s^10, k=|lambda|. This is not a direct hypermatching alpha-witnessing theorem; retain the k-dependent factor.
- M(lambda): words with fixed color multiplicities: Do not divide by M when min(lambda)=1. Uniform polynomial equivalence is asserted for balanced multislices, or the source low-complexity conditions.
- k-slice of {0,1}^n: The balanced-slice theorem is not an unrestricted promise theorem. Full-slice improvements also appear in HKMP26.
- Partitions of kn vertices into n unordered k-sets (lambda=(k)): Reverse sensitivity uses a separate query lift with coefficient 10368*(2k-1)^10, not the unproved hypermatching witnessing parameter. Fixed k gives a uniform coefficient; growing k must be retained.
