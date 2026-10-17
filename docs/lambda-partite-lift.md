# A product-permutation lift for lambda-partite hypermatchings

This is a repository derivation using the inspected final DFLLV26 journal as input. It is not attributed as a printed theorem or claimed novel. A separate-agent source-level mathematical audit passed after a simulation-invariant correction; this is not formal verification or human peer review. See [the audit](lambda-lift-independent-audit.md). It gives coarse polynomial sensitivity comparisons without constructing hypermatching pseudo-characters.

Let lambda=(lambda_1,...,lambda_r), with every lambda_i positive, k=sum_i lambda_i>=2. There are n>=2 hyperedges, each containing lambda_i vertices from the color class P_i of size lambda_i*n. The input is any perfect lambda-partite hypermatching. One query reveals the hyperedge containing a specified vertex. Sensitivity packs disjoint sensitive changes of minimum chunk size two.

For every Boolean function on this domain,

`D(f) <= 10368*(2k-1)^10*s(f)^10`.

The coefficient depends only on k, not on the color-multiplicity ratio. For fixed k this is a uniform polynomial bound. It does not imply the stronger direct estimate degree<=O(s^2) on the hypermatching domain.

## Product of permutation domains

Put N_i=lambda_i*n and consider Z=product_i S_(N_i), with forward and inverse permutation queries in each component. Spatial degree on this product is the minimum degree in the usual permutation-entry indicators.

First, this product is 1/2-witnessing. Here are the linear-algebra details needed for the tensor argument. Let V_d^i be the degree-at-most-d function space on component i. Since each indicator monomial factors across components,

`V_d(Z) = sum_{sum_i d_i<=d} tensor_i V_(d_i)^i`.

DFLLV26 Theorem 5.5 and Section 5.3 decompose the permutation function space orthogonally into isotypic components indexed by partitions of depth d_i=N_i-lambda_first_row. Each component has pure filtration degree d_i and is spanned by the source's pseudo-characters. A degree-d function on Z therefore has a nonzero component in a tensor of such spaces whose depths sum to d, and correlates with a product of their spanning pseudo-characters.

Each factor pseudo-character takes values in {-1,0,1} and partitions its support into induced cubes of dimension at least d_i/2. Taking Cartesian products of those partitions gives cubes of dimension the sum of the factor dimensions, at least d/2. Neighbor changes within distinct components are disjoint, while disjointness within a component is the source's construction. Products of the signs alternate across each cube edge. Lemma 5.2, or equivalently its proof applied to this product pseudo-character, yields

`degree_Z <= 2*s_Z^2`.

The product has chunk size two, query overlap at most two, conflict threshold M=sum_i N_i, and beta_c>=1/3. For the conflict assertion, any two partial inputs not separated by a forward or inverse query have a union which is a partial bijection in every factor. Each partial bijection extends componentwise to a full permutation. Hence every incompatible pair is query-separated regardless of size, and the source-capped threshold is M=sum_i N_i. Composability also holds componentwise. For the shortening ratio, use each factor's shortening witnesses while leaving the other components equal to the second input. Their disagreement sets lie in different components and are disjoint; the counts sum to at least one third of the total difference size. Each shortening still changes only a minimum chunk.

Apply the original journal's Lemmas 3.3, 3.5 and 3.6:

`C_Z <= 3*s_Z*bs_Z <= 18*s_Z*degree_Z^2 <= 72*s_Z^5`,

and

`D_Z <= 2*C_Z^2`.

Thus `D_Z<=10368*s_Z^10`. The witnessing result is for Z, not an assertion of a hypermatching witnessing parameter.

## Lifting the input and simulating queries

Represent a hypermatching by a tuple of permutations of its color classes. In component i, divide positions into n consecutive groups of lambda_i positions. Positions with the same group label across all colors form one hyperedge. Any tuple of permutations gives a valid hypermatching, and every hypermatching has such representations. Lift f to the function F on Z defined by this projection.

A deterministic tree for F can be simulated with at most one hypermatching query per permutation query. Maintain a common assignment of discovered hyperedges to group labels and fill every position of such a group in every color simultaneously, using any fixed order within the color.

For a forward query to an unassigned group label, choose an undiscovered vertex of that color and query its hyperedge, assigning the result to that label. Such a vertex exists whenever an unassigned label remains, since every remaining hyperedge has positive multiplicity in every color. For an inverse query to an undiscovered vertex, query its hyperedge and assign it to any free common label. Queries concerning discovered hyperedges are answered from the stored bijections. At each transcript there exists a complete tuple of permutations extending the stored answers and representing the fixed input: assign the remaining actual hyperedges to the free common labels. That representative reaches the same leaf of the decision tree, so the leaf output is f. Arbitrary completions may regroup undiscovered vertices and need not represent the fixed input; their existence is irrelevant. Thus `D(f)<=D(F)`.

## Sensitivity comparison

At any representation, take t disjoint sensitive minimum changes of Z. They are transpositions within individual permutation components. A transposition within a position group changes no hyperedge and cannot be sensitive. Each sensitive transposition therefore joins two different hyperedges.

Make a multigraph on the original hyperedges, with one edge per sensitive transposition. Disjointness of the permutation changes means that no position is used twice. An original hyperedge has k positions across all components, so its multigraph degree is at most k. Greedily choosing an edge removes at most 2k-1 edges, giving a matching of size at least t/(2k-1).

The selected transpositions change disjoint pairs of hyperedges. Each is sensitive for f and changes a minimum chunk of two hyperedges. Therefore

`s_Z(F) <= (2k-1)*s(f)`.

Combining this with the product decision bound proves the stated inequality. All other measures in the twelve-measure profile are bounded by a domain-independent constant times D, so this supplies their reverse-sensitivity chains as well.

## Limits and provenance

The product filtration, cube witnesses, oracle simulation and sensitivity packing are separate proof steps. Their source inputs are DFLLV26's permutation degree decomposition, pseudo-character construction and parameterized certificate/degree inequalities. The lifting and tensor assembly are repository arguments. No plethysm decomposition for hypermatchings is used, and the source's stated limitation of its direct representation-theoretic technique is not contradicted.

This fills the eleven previously unindexed parameterized sensitivity directions in the general lambda-partite profile. The seven profile matrices now have 924 upper chains across 924 ordered cells. They are conservative upper chains, not optimal exponent tables; their lambda-dependent coefficients cannot be dropped. Stronger sensitivity estimates, priority and optimality remain separate audit tasks. The independent audit and incorporated repairs are recorded in data/lambda-lift-independent-audit.json.
