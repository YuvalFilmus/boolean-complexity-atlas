# Data model and mathematical conventions

## Ordered exponent questions

For an admissible class F, define

    alpha_F(A,B) = inf {p >= 0 : exists C, all f in F, A(f) <= C max(1,B(f))^p}.

C must be independent of input length and f. Additional fixed parameters and permitted dependencies must be stated. Using max(1,B) handles constant functions; a source's exact formula is preserved separately. p=0 and lack of any finite exponent are legitimate possibilities even though this initial catalogue contains no p=0 record.

Store the set of known admissible upper bounds and known exclusions separately. An inequality A <= O(B^u) gives alpha <= u. A family with B tending to infinity and A >= B^(l-o(1)) gives alpha >= l. The same lower endpoint may follow from A >= B^l/polylog(B). Neither establishes the endpoint inequality A <= O(B^l). An upper bound with a logarithmic loss gives bounds for every exponent larger than u, and hence alpha <= u, but does not certify endpoint attainment.

If B stays bounded while A grows unbounded, there is no finite exponent. An exponential separation as a function of an external parameter must be translated carefully: record the explicit pair of parameterized complexities before labelling it “no polynomial bound.”

Exact identities, Theta relations, multivariate bounds, and constant-factor improvements are separate claim types. A comparison with epsilon-dependent constants cannot be reduced to a fixed constant without an epsilon convention. Keep raw statements authoritative when a simplified machine-readable exponent loses detail.

## Source objects

`sources` contains stable citation keys, complete author lists for the cited version, title, year, persistent identifiers, accessed date, inspected version when pinned, publication fields when reconciled, and annotations for surveys. A preprint citation is a legitimate complete citation of that version; it does not substitute for eventual journal/conference reconciliation. Title and author lists can change across versions.

## Measures and aliases

Each measure has a stable ID, canonical display name, symbol, mathematical definition, definition status, and provenance. `working_definition` means a working definition has been entered, not that all source normalizations have been audited. `source_checked` means the definition and its normalization were inspected in the indicated source. A discovery lead means a measure was found in the literature but still requires definition extraction; do not infer through it.

Each alias keeps its source, evidence status, and normalization caveat. Existing seed aliases need exact page-level occurrence audits. Do not collapse equivalent-up-to-constants measures into identities: e.g. fbs and RC remain distinct; fractional certificate complexity equals fbs only with matching LP definitions. Do not conflate a named source measure K with lambda until the original normalization is reconciled. Keep display strings non-unique.

Future alias fields should include source locator, exact TeX, introduction date, alternative English names, collision IDs, and whether the relationship is identity, rescaling, Theta equivalence, or a genuinely different variant. Definitions for one-sided, local, distributional, promise-restricted, and relation versions must be explicit. Source-defined names override repository shorthand in quotations.

## Scope

Every claim has a scope:

- `object_kind`: decision_function, multi_output_function, search_relation, real_valued_function, or hazard_free_extension.
- `totality`: total, partial, or partial_or_total.
- `classes`: conjunction of restrictions, such as symmetric, monotone, unate, transitive, or read_once. An empty list is unrestricted.
- `input_alphabet`, `output_alphabet`: currently bits or arbitrary finite. Hazard-free models require a ternary alphabet rather than silently joining Boolean rows.
- `cost`, `error`: references to the measure definitions, with source-specific overrides where needed.
- `assumptions`: explicit extra hypotheses (for example nonconstant).

For a bit-input search relation S subset X times Y, the catalogue tag total requires X to be the full Boolean cube and every input to have a valid output. A relation whose input set is a proper promise receives the tag partial even when every promised input has a solution. Source terminology such as total on a domain is retained in notes, rather than silently changing this convention. Total search need not be an efficiently verifiable TFNP problem in the uniform computational sense; query complexity and uniform verification are different attributes. Treat “TFNP query analogue” as a source/model statement.

A symmetric search relation requires specifying the group action on inputs and outputs, not just reusing the definition of a symmetric Boolean function. A single-valued multi-output map is also distinct from a relation permitting multiple valid outputs. Canonical-output and pseudo-deterministic requirements must be explicit.

Universal inequalities restrict to subclasses; separating families do not. For example, a total-function upper bound applies to symmetric total functions, while a general total separating family gives no lower bound for the symmetric subclass without a symmetric witness. Likewise, an upper bound on all partial functions covers total functions, while a separation using a genuine promise need not.

The claim CLI performs direct scope filtering. It restricts universal statements to subclasses and includes a witness in any superclass explicitly supported by its recorded properties. It does not infer class implications (such as symmetric implying transitive) or compose bounds.

## Claim provenance

`kind` separates upper_bound, separation, identity, theta_bound, multivariate_upper_bound, no_polynomial_bound, and superpolynomial_separation. `A` is always the left-hand measure in the ordered question. `exponent` stores an exact integer or rational string where meaningful; `null` indicates that the raw statement or multiple factors is needed.

`source_checked` means the statement and the cited proof route were located. It is not an independent proof certification. `secondary_checked` indicates a cited attribution in a later paper. `statement_checked_proof_pending` is weaker still. `definition_proof` and `derived` record repository reasoning, with dependency IDs when available. Every entry also has a proof-audit status. This first version has no independently audited results.

For future completeness, separating families need their own shared objects, with definitions, input-length parameterization, verified growth of B, and independently sourced upper/lower bounds on all their measures. A common witness can establish many pair separations; it should not be copied with incompatible parameters.

## Conjectures and implications

Record who stated a conjecture, in which version and location, its hypotheses, and dated status evidence. A conjecture can be resolved, refuted, open-as-of-a-source, or current-status-unverified. Implications should become typed dependency records rather than prose-only edges before automated inference is enabled.

## Generation and audit workflow

1. Finish versioned source and measure definitions.
2. Extract a theorem or witness with exact hypotheses and proof route.
3. Reconcile bibliographic publication versions and priorities.
4. Review mathematical translation, constants, and scope.
5. Search later citing papers and recent preprints for improvements or corrections.
6. Mark the pair's coverage and date; only then certify best-known endpoints.
7. Generate tables and pair pages, displaying both endpoint evidence and completeness status.

Automated transitive closure will require typed hypotheses and cost/error conversions. Multiplying exponents along a path alone is insufficient: logarithms, constants, fixed parameters, multi-measure bounds, and witness directions all need handling. The repository now includes a restricted total-function exponent closure in tools/matrix.py. It composes only eligible scalar power bounds, explicit multivariate products and witness transfers, preserves logarithmic endpoint flags and provenance, and excludes unknown parameter losses. This is not a general inference engine.

The promise matrix in tools/partial_matrix.py uses only promise-valid scalar bounds. It keeps bounded and unrestricted degrees distinct, and uses shared witness growth records to justify each non-polynomial entry. Its finite lower endpoints are parity or the exact-search star promise. Search comparison matrices are direct evidence inventories, not transitive numerical closures.
