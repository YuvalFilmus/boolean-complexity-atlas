# Fresh independent audit of the four-query matching obstruction

23 October 2026. Audited exact target: `outputs/open-problem-progress-round3-2026-10-23/exact-width-three-proof.md`. I read the accompanying prior audit, but did not treat its PASS as evidence of correctness. I reconstructed the necessary model reductions and wrote a fresh exact certificate checker, `work/check_width_three_fresh_round4.py`, without importing either earlier checker.

**Verdict: PASS for the stated computationally assisted finite theorem.** For this precise full-cube eight-output certificate partition, in the standard fixed worst-case bit-query model, Q_E=D=4. No proof gap was found. This is an assistant audit, not formal verification or human peer review; priority is reported separately.

## Model and amplitude argument

Diagonalizing the standard XOR answer register produces four nontrivial query sectors z_i and an identity sector. The identity sector can include all plus-answer components, arbitrary index and workspace registers, inactive queries and padded early-stopping branches. The queried index and answer eigenspace are orthogonal sectors, so their projected Grams add. Coherently storing measurement records and dilating finite measurements preserves the exact query budget and the necessary polynomial-amplitude bound. This is an ordinary definite-order query model; postselection and unbounded expected-query branches are excluded.

A final computational-basis amplitude assigned to certificate c vanishes at every input outside c because invalid-output probability is a sum of nonnegative squared moduli. On the entire Boolean cube, uniqueness of multilinear representation yields a=1_c b in the disjoint free variables. When a is nonzero, the top monomial of 1_c times a top monomial of b cannot cancel; hence deg(a)=|c|+deg(b). At three queries and certificate width three, b is constant. This is a stronger conclusion than merely having the same output label. Every final state is identical at an edge's two endpoints, including its global phase, workspace and deferred records. Distinct edges have orthogonal output labels and each edge vector is normalized. Thus K=CCᵀ exactly. No errorless/SOS converse is assumed.

The final input-independent unitary can be undone without changing any inner products, so the state immediately after the last oracle has the same edge-constant form. Each query-sector projection gives a PSD Hermitian eight-edge Gram M_q, and their sum is I. Reversing that sector's last phase multiplication yields z_q C a, which has degree at most two. Its degree-three/four Fourier coefficients vanish, giving L_q M_q=0. Depending on the convention for coefficient column vectors, Gram ranges involve conjugate coefficient vectors; the kernel is defined over the reals and is conjugation invariant, so the displayed range condition remains valid. The missing factor 1/16 in L_q is irrelevant.

## Symmetry and real reduction

I reconstructed all signed coordinate permutations preserving the partition and obtained 48. They can be simulated with no extra input queries: relabel the query index, apply known answer flips for fixed input bit flips, and relabel the output certificates. In sector Grams the fixed phase signs cancel. Therefore the action on M_q is precisely edge permutation together with coordinate-query permutation, fixing q=0.

Averaging feasible hypothetical algorithms over this group is physical: use an input-independent orthogonal control register and a direct sum of the transformed circuits. The final edge vectors remain orthonormal. This preserves the two-query-prefix constraints as well as the final-query constraints. Complex-conjugating the complete circuit is also legitimate because the XOR oracle is real; a direct-sum average with the conjugate circuit realizes real Gram data. Equivalently, the real parts preserve all real necessary PSD constraints. Thus it suffices to contradict invariant real symmetric tuples without silently excluding complex or adaptive solvers.

## Fresh finite certificate reconstruction

The fresh checker generates the group directly from the 384 possible signed coordinate maps. It independently builds the orbits of the 180 symmetric entries (q,a,b), obtains ten orbits, writes **all** support and normalization equations on their ten values, and performs exact rational elimination. The constraint rank is eight and the affine dimension is two.

It then verifies the explicit particular vector and two directions in the prior audit's ten-orbit table against every equation. The directions are independent, so together with the computed rank this table describes the entire invariant affine solution space. Finally, instead of accepting the earlier Fourier-block computation, the checker constructs the 16-by-16 input Gram G and evaluates each quadratic Fourier entry by a direct sum over all 256 input pairs. It obtains scales 1,−2,+2 on the particular vector and the two directions. Thus H=(1−2t+2u)B is verified exactly for the entire affine space. This computation does not import prior checker functions or assume their dimensions.

The table's use of orbit representatives does not rely on guessed symmetry: the fresh checker verifies that their generated orbits are disjoint and cover every symmetric matrix coordinate. All arithmetic uses fractions.Fraction. No PSD optimizer or numerical tolerance occurs.

## Positivity, zero scale and the prefix obstruction

H is a Fourier coefficient Gram, so its diagonal makes sigma nonnegative. If sigma=0, every quadratic coefficient vector of the actual averaged pre-last-query state has norm zero. The support conditions already ensure degree at most two, so that state has degree at most one. One more query plus a fixed unitary could then give degree at most two, contradicting any nonzero width-three final amplitude. Hence sigma>0. It is important that this argument concerns the averaged hypothetical algorithm, not arbitrary feasible last-query relaxation data; the physical averaging construction supplies that distinction.

For a two-query state, the second oracle multiplies a degree-at-most-one sector amplitude by z_i. Its quadratic terms can only use pairs containing i. The identity sector supplies none. Orthogonality of the query sectors therefore decomposes the quadratic Gram into four PSD star-supported matrices. Any final fixed unitary preserves the Fourier Gram. This necessity holds for coherently adaptive algorithms too.

Two distinct intersecting pair masks have exactly one common coordinate, so their off-diagonal H entry comes from one unique star block. The fresh checker verifies all four triples of forced signs in B: each off-diagonal magnitude is 1/16, and the sign product is negative. Three sign changes can consequently make all three off-diagonal entries negative. Evaluating the PSD star form on the all-ones vector gives trace(H_i)≥6sigma/16. Summing gives trace(H)≥3sigma/2, whereas the six diagonal entries of sigma B sum to 3sigma/4. Since sigma>0 this is impossible.

Thus Q_E≥4; four classical queries give Q_E≤D≤4. A separate classical enumeration is unnecessary for the equality, although both original scripts' classical checks passed.

## Reproduction and qualifications

I reran both shipped checkers; they reported the claimed 272 matchings, eight irreducible matchings, 48 automorphisms, five four-dimensional support spaces, five-dimensional invariant supported space, two-dimensional normalized affine space and trace contradiction. My fresh checker independently verified the decisive affine identity and all sign/trace constants; output is `work/width-three-fresh-check-round4.json`.

I additionally verified directly that labels 0–3 of the candidate are the zero-output subcubes of the published 4-MAJ partition and labels 4–7 are its one-output subcubes. This gives more direct known construction provenance than merely an isomorphic later irreducibility catalogue. The separate priority report distinguishes the old construction and classical lower bound from the exact quantum obstruction.

Publication should retain: full-cube standard-bit-query model; output is the unique containing certificate; computationally assisted rational affine identity; last-query feasibility is only a relaxation; no certified novelty; BK24 asymptotic question remains unresolved. The optional stronger parameterization printed by a later author script is not needed and was not used to approve this proof.
