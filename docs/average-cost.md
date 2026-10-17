# Average cost, distributional error and zero-error conventions

The input distribution mu is fixed. In the strong average-cost model of GIPS21 Definition 24, the algorithm must meet its correctness requirement on **every promised input**; only its query count is averaged over mu and its coins. This differs from `Ddist`, where a deterministic tree may err on an epsilon fraction of mu and its cost is worst-case depth.

The catalogue now defines `Davg`, `Ravg`, `R0avg`, `psRavg` and `psR0avg` separately. Their display labels are repository notation, not claimed historical symbols. Canonical bounded-error average cost requires one fixed valid output on every input with probability at least 2/3. The strict zero-error canonical variant requires that selector value with probability one.

## Published results

[GIPS21](https://doi.org/10.4230/LIPIcs.CCC.2021.36) establishes:

- Proposition 25: for every distribution on dense Find1 inputs, a correct deterministic algorithm has average cost at most log n+1. Fix a small set hitting almost all inputs, and scan the remaining coordinates on the exceptional inputs.
- Theorem 26: zero-error randomized, zero-error canonical and deterministic average solvability coincide up to polylogarithmic factors. Its proof obtains O(r log² n+1) by selecting and interleaving a logarithmic family of algorithms and summing tail bounds.
- Theorem 27: for every input distribution, normalized Hamming-weight estimation to fixed additive epsilon has canonical average cost O(log n/epsilon²). Fix a sample that works for most mu-inputs, cross-check with fresh randomness, and read all bits on disagreement. Canonical correctness holds pointwise; expensive computation is rare only under mu.
- Theorem 28: a q-query randomized epsilon/4-approximator of a metric-valued target gives a canonical epsilon-approximator of average cost O(q log n). The two algorithms have different approximation radii; this is not a scalar comparison for an unchanged relation.
- Proposition 29: under full support, strict zero-error additive-epsilon Hamming-weight estimation requires at least (1-2epsilon)n queries on a terminating path. An earlier leaf would contain completions whose weights differ by more than the allowable approximation diameter.

## Two explicit finite-domain observations

The following are repository derivations, with no first-discovery claim. They sharpen the recorded average-cost statements under the precise nonuniform, finite-domain, strict Las Vegas conventions above.

**Fixing coins gives exact equality.** For an almost-surely correct and terminating algorithm, the event that fixed coins yield correctness and termination on all promised inputs has probability one: there are only finitely many inputs. Average its mu-cost over the coins and fix a seed of cost at most that average. Prune repeated queries. This is a deterministic solver correct on the entire promise. Conversely, any deterministic solver is strict Las Vegas and canonically zero-error. Hence

    Davg_mu = R0avg_mu = psR0avg_mu.

The published weaker simulation is retained with its own proof route. Theorem 26's proof also discusses algorithms succeeding with probability 2/3; that proof language must not erase the distinction between strict Las Vegas and a fixed-cap solver allowed to return a failure flag. This observation is not an assertion that every interpretation of “zero-error” in that paper has identical optima.

**Dense Find1 admits average cost below two.** On a fixed weight-k input, scanning a uniformly random coordinate permutation stops at expected position (n+1)/(k+1). For k>=ceil(n/2), this is at most (n+1)/(ceil(n/2)+1)<2. Average over mu and fix one permutation no worse than the average. Every fixed permutation is correct on every dense input. Thus the same nonuniform model admits a constant bound, stronger than the logarithmic statement of Proposition 25. Small-instance permutation calculations are checked independently in the regression suite.

These arguments are about averaged cost of a distribution-dependent deterministic tree, not worst-case derandomization or uniform efficient construction of the tree.

## Detectable failure is a separate resource

[ZPP26](https://doi.org/10.4230/LIPIcs.ITCS.2026.60), Definition 14, uses a randomized query cap that permits the symbol bottom but never an invalid answer. The scalar specialization is recorded as `Rfail`, with failure at most 1/3. Repetition until success gives R0<=1.5 Rfail in expectation; truncation gives Rfail=O(R0). Candidate verification gives Rfail=O(R+V). Input-query verification cost V cannot be suppressed.

Query-TFZPP additionally requires efficient verification, so an arbitrary relation with small expected R0 need not belong to query-TFNP. The 2026 paper's reduction-class separations from PLS and PPP are recorded as class facts, not converted into unsupported scalar exponent claims.
