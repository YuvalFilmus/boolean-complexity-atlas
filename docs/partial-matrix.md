# Promise-function comparison matrix

Boolean decision functions on arbitrary promises; weak certificates; unrestricted promise polynomial degrees; R0 worst-case expected Las Vegas cost.

A=O(max(1,B)^p). A no_finite_power entry uses a growing numerator and bounded denominator, or an original-source superpolynomial separation.

Evidence inventory, not a globally certified best-known table. Finite entries have matching lower exponents from parity or the zero-or-unit-vector promise. These are statements about power exponents, not optimal constants.

A row A and column B describe A versus B. `p` is a matched finite power exponent; `∞` disproves every finite exponent; `?` is an unresolved audit cell, not a claim that the literature has no answer. Finite cells have matching witness exponents; consult the per-cell JSON lower record.

| A / B | D | R0 | R | C | RC | bs | s | lambda | QE | deg | Q | adeg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D | 1 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| R0 | 1 | 1 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| R | 1 | 1 | 1 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| C | 1 | 1 | ∞ | 1 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| RC | 1 | 1 | 1 | 1 | 1 | ∞ | ∞ | ∞ | 2 | ∞ | 2 | ∞ |
| bs | 1 | 1 | 1 | 1 | 1 | 1 | ∞ | ∞ | 2 | ∞ | 2 | ∞ |
| s | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | ∞ | 2 | ∞ |
| lambda | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | ∞ | 1 | ∞ |
| QE | 1 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | 1 | ∞ | ∞ | ∞ |
| deg | 1 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | 1 | 1 | ∞ | ∞ |
| Q | 1 | 1 | 1 | ∞ | ∞ | ∞ | ∞ | ∞ | 1 | ∞ | 1 | ∞ |
| adeg | 1 | 1 | 1 | ∞ | ∞ | ∞ | ∞ | ∞ | 1 | 1 | 1 | 1 |

## Cell provenance

- D / R0: no_finite_power; [promise-unbounded-D-R0-promise-dense-two-axes](claims.md#promise-unbounded-D-R0-promise-dense-two-axes).
- D / R: no_finite_power; [promise-unbounded-D-R-promise-dense-two-axes](claims.md#promise-unbounded-D-R-promise-dense-two-axes), [promise-unbounded-D-R-promise-restricted-DJ](claims.md#promise-unbounded-D-R-promise-restricted-DJ).
- D / C: no_finite_power; [promise-unbounded-D-C-promise-dense-two-axes](claims.md#promise-unbounded-D-C-promise-dense-two-axes), [promise-unbounded-D-C-promise-nonempty-two-axes](claims.md#promise-unbounded-D-C-promise-nonempty-two-axes), [promise-unbounded-D-C-promise-unique-mark-color](claims.md#promise-unbounded-D-C-promise-unique-mark-color).
- D / RC: no_finite_power; [promise-unbounded-D-RC-promise-dense-two-axes](claims.md#promise-unbounded-D-RC-promise-dense-two-axes), [promise-unbounded-D-RC-promise-nonempty-two-axes](claims.md#promise-unbounded-D-RC-promise-nonempty-two-axes), [promise-unbounded-D-RC-promise-restricted-DJ](claims.md#promise-unbounded-D-RC-promise-restricted-DJ), [promise-unbounded-D-RC-promise-unique-mark-color](claims.md#promise-unbounded-D-RC-promise-unique-mark-color).
- D / bs: no_finite_power; [promise-unbounded-D-bs-promise-dense-two-axes](claims.md#promise-unbounded-D-bs-promise-dense-two-axes), [promise-unbounded-D-bs-promise-nonempty-two-axes](claims.md#promise-unbounded-D-bs-promise-nonempty-two-axes), [promise-unbounded-D-bs-promise-projective-plane](claims.md#promise-unbounded-D-bs-promise-projective-plane), [promise-unbounded-D-bs-promise-restricted-DJ](claims.md#promise-unbounded-D-bs-promise-restricted-DJ), [promise-unbounded-D-bs-promise-unique-mark-color](claims.md#promise-unbounded-D-bs-promise-unique-mark-color).
- D / s: no_finite_power; [promise-unbounded-D-s-promise-doubled-parity](claims.md#promise-unbounded-D-s-promise-doubled-parity), [promise-unbounded-D-s-promise-dense-two-axes](claims.md#promise-unbounded-D-s-promise-dense-two-axes), [promise-unbounded-D-s-promise-nonempty-two-axes](claims.md#promise-unbounded-D-s-promise-nonempty-two-axes), [promise-unbounded-D-s-promise-projective-plane](claims.md#promise-unbounded-D-s-promise-projective-plane), [promise-unbounded-D-s-promise-restricted-DJ](claims.md#promise-unbounded-D-s-promise-restricted-DJ), [promise-unbounded-D-s-promise-unique-mark-color](claims.md#promise-unbounded-D-s-promise-unique-mark-color).
- D / lambda: no_finite_power; [promise-unbounded-D-lambda-promise-doubled-parity](claims.md#promise-unbounded-D-lambda-promise-doubled-parity), [promise-unbounded-D-lambda-promise-dense-two-axes](claims.md#promise-unbounded-D-lambda-promise-dense-two-axes), [promise-unbounded-D-lambda-promise-nonempty-two-axes](claims.md#promise-unbounded-D-lambda-promise-nonempty-two-axes), [promise-unbounded-D-lambda-promise-projective-plane](claims.md#promise-unbounded-D-lambda-promise-projective-plane), [promise-unbounded-D-lambda-promise-restricted-DJ](claims.md#promise-unbounded-D-lambda-promise-restricted-DJ), [promise-unbounded-D-lambda-promise-unique-mark-color](claims.md#promise-unbounded-D-lambda-promise-unique-mark-color).
- D / QE: no_finite_power; [promise-unbounded-D-QE-promise-extremal-forrelation](claims.md#promise-unbounded-D-QE-promise-extremal-forrelation), [promise-unbounded-D-QE-promise-restricted-DJ](claims.md#promise-unbounded-D-QE-promise-restricted-DJ).
- D / deg: no_finite_power; [promise-unbounded-D-deg-promise-unit-OR](claims.md#promise-unbounded-D-deg-promise-unit-OR), [promise-unbounded-D-deg-promise-projective-plane](claims.md#promise-unbounded-D-deg-promise-projective-plane), [promise-unbounded-D-deg-promise-extremal-forrelation](claims.md#promise-unbounded-D-deg-promise-extremal-forrelation), [promise-unbounded-D-deg-promise-restricted-DJ](claims.md#promise-unbounded-D-deg-promise-restricted-DJ), [promise-unbounded-D-deg-promise-unique-mark-color](claims.md#promise-unbounded-D-deg-promise-unique-mark-color).
- D / Q: no_finite_power; [promise-unbounded-D-Q-promise-dense-two-axes](claims.md#promise-unbounded-D-Q-promise-dense-two-axes), [promise-unbounded-D-Q-promise-extremal-forrelation](claims.md#promise-unbounded-D-Q-promise-extremal-forrelation), [promise-unbounded-D-Q-promise-restricted-DJ](claims.md#promise-unbounded-D-Q-promise-restricted-DJ).
- D / adeg: no_finite_power; [promise-unbounded-D-adeg-promise-unit-OR](claims.md#promise-unbounded-D-adeg-promise-unit-OR), [promise-unbounded-D-adeg-promise-dense-two-axes](claims.md#promise-unbounded-D-adeg-promise-dense-two-axes), [promise-unbounded-D-adeg-promise-projective-plane](claims.md#promise-unbounded-D-adeg-promise-projective-plane), [promise-unbounded-D-adeg-promise-extremal-forrelation](claims.md#promise-unbounded-D-adeg-promise-extremal-forrelation), [promise-unbounded-D-adeg-promise-restricted-DJ](claims.md#promise-unbounded-D-adeg-promise-restricted-DJ), [promise-unbounded-D-adeg-promise-unique-mark-color](claims.md#promise-unbounded-D-adeg-promise-unique-mark-color).
- R0 / D: finite_upper_bound; [R0-D](claims.md#R0-D).
- R0 / R: no_finite_power; [promise-unbounded-R0-R-promise-restricted-DJ](claims.md#promise-unbounded-R0-R-promise-restricted-DJ).
- R0 / C: no_finite_power; [promise-unbounded-R0-C-promise-unique-mark-color](claims.md#promise-unbounded-R0-C-promise-unique-mark-color).
- R0 / RC: no_finite_power; [promise-unbounded-R0-RC-promise-restricted-DJ](claims.md#promise-unbounded-R0-RC-promise-restricted-DJ), [promise-unbounded-R0-RC-promise-unique-mark-color](claims.md#promise-unbounded-R0-RC-promise-unique-mark-color).
- R0 / bs: no_finite_power; [promise-unbounded-R0-bs-promise-projective-plane](claims.md#promise-unbounded-R0-bs-promise-projective-plane), [promise-unbounded-R0-bs-promise-restricted-DJ](claims.md#promise-unbounded-R0-bs-promise-restricted-DJ), [promise-unbounded-R0-bs-promise-unique-mark-color](claims.md#promise-unbounded-R0-bs-promise-unique-mark-color).
- R0 / s: no_finite_power; [promise-unbounded-R0-s-promise-doubled-parity](claims.md#promise-unbounded-R0-s-promise-doubled-parity), [promise-unbounded-R0-s-promise-projective-plane](claims.md#promise-unbounded-R0-s-promise-projective-plane), [promise-unbounded-R0-s-promise-restricted-DJ](claims.md#promise-unbounded-R0-s-promise-restricted-DJ), [promise-unbounded-R0-s-promise-unique-mark-color](claims.md#promise-unbounded-R0-s-promise-unique-mark-color).
- R0 / lambda: no_finite_power; [promise-unbounded-R0-lambda-promise-doubled-parity](claims.md#promise-unbounded-R0-lambda-promise-doubled-parity), [promise-unbounded-R0-lambda-promise-projective-plane](claims.md#promise-unbounded-R0-lambda-promise-projective-plane), [promise-unbounded-R0-lambda-promise-restricted-DJ](claims.md#promise-unbounded-R0-lambda-promise-restricted-DJ), [promise-unbounded-R0-lambda-promise-unique-mark-color](claims.md#promise-unbounded-R0-lambda-promise-unique-mark-color).
- R0 / QE: no_finite_power; [promise-unbounded-R0-QE-promise-extremal-forrelation](claims.md#promise-unbounded-R0-QE-promise-extremal-forrelation), [promise-unbounded-R0-QE-promise-restricted-DJ](claims.md#promise-unbounded-R0-QE-promise-restricted-DJ).
- R0 / deg: no_finite_power; [promise-unbounded-R0-deg-promise-unit-OR](claims.md#promise-unbounded-R0-deg-promise-unit-OR), [promise-unbounded-R0-deg-promise-projective-plane](claims.md#promise-unbounded-R0-deg-promise-projective-plane), [promise-unbounded-R0-deg-promise-extremal-forrelation](claims.md#promise-unbounded-R0-deg-promise-extremal-forrelation), [promise-unbounded-R0-deg-promise-restricted-DJ](claims.md#promise-unbounded-R0-deg-promise-restricted-DJ), [promise-unbounded-R0-deg-promise-unique-mark-color](claims.md#promise-unbounded-R0-deg-promise-unique-mark-color).
- R0 / Q: no_finite_power; [promise-unbounded-R0-Q-promise-extremal-forrelation](claims.md#promise-unbounded-R0-Q-promise-extremal-forrelation), [promise-unbounded-R0-Q-promise-restricted-DJ](claims.md#promise-unbounded-R0-Q-promise-restricted-DJ).
- R0 / adeg: no_finite_power; [promise-unbounded-R0-adeg-promise-unit-OR](claims.md#promise-unbounded-R0-adeg-promise-unit-OR), [promise-unbounded-R0-adeg-promise-projective-plane](claims.md#promise-unbounded-R0-adeg-promise-projective-plane), [promise-unbounded-R0-adeg-promise-extremal-forrelation](claims.md#promise-unbounded-R0-adeg-promise-extremal-forrelation), [promise-unbounded-R0-adeg-promise-restricted-DJ](claims.md#promise-unbounded-R0-adeg-promise-restricted-DJ), [promise-unbounded-R0-adeg-promise-unique-mark-color](claims.md#promise-unbounded-R0-adeg-promise-unique-mark-color).
- R / D: finite_upper_bound; [R-D](claims.md#R-D).
- R / R0: finite_upper_bound; [R-R0](claims.md#R-R0).
- R / C: no_finite_power; [promise-unbounded-R-C-promise-unique-mark-color](claims.md#promise-unbounded-R-C-promise-unique-mark-color).
- R / RC: no_finite_power; [promise-unbounded-R-RC-promise-unique-mark-color](claims.md#promise-unbounded-R-RC-promise-unique-mark-color).
- R / bs: no_finite_power; [promise-unbounded-R-bs-promise-projective-plane](claims.md#promise-unbounded-R-bs-promise-projective-plane), [promise-unbounded-R-bs-promise-unique-mark-color](claims.md#promise-unbounded-R-bs-promise-unique-mark-color).
- R / s: no_finite_power; [promise-unbounded-R-s-promise-doubled-parity](claims.md#promise-unbounded-R-s-promise-doubled-parity), [promise-unbounded-R-s-promise-projective-plane](claims.md#promise-unbounded-R-s-promise-projective-plane), [promise-unbounded-R-s-promise-unique-mark-color](claims.md#promise-unbounded-R-s-promise-unique-mark-color).
- R / lambda: no_finite_power; [promise-unbounded-R-lambda-promise-doubled-parity](claims.md#promise-unbounded-R-lambda-promise-doubled-parity), [promise-unbounded-R-lambda-promise-projective-plane](claims.md#promise-unbounded-R-lambda-promise-projective-plane), [promise-unbounded-R-lambda-promise-unique-mark-color](claims.md#promise-unbounded-R-lambda-promise-unique-mark-color).
- R / QE: no_finite_power; [partial-R-QE-GS26](claims.md#partial-R-QE-GS26), [promise-unbounded-R-QE-promise-extremal-forrelation](claims.md#promise-unbounded-R-QE-promise-extremal-forrelation).
- R / deg: no_finite_power; [promise-unbounded-R-deg-promise-unit-OR](claims.md#promise-unbounded-R-deg-promise-unit-OR), [promise-unbounded-R-deg-promise-projective-plane](claims.md#promise-unbounded-R-deg-promise-projective-plane), [promise-unbounded-R-deg-promise-extremal-forrelation](claims.md#promise-unbounded-R-deg-promise-extremal-forrelation), [promise-unbounded-R-deg-promise-unique-mark-color](claims.md#promise-unbounded-R-deg-promise-unique-mark-color).
- R / Q: no_finite_power; [partial-R-Q](claims.md#partial-R-Q), [promise-unbounded-R-Q-promise-extremal-forrelation](claims.md#promise-unbounded-R-Q-promise-extremal-forrelation).
- R / adeg: no_finite_power; [promise-unbounded-R-adeg-promise-unit-OR](claims.md#promise-unbounded-R-adeg-promise-unit-OR), [promise-unbounded-R-adeg-promise-projective-plane](claims.md#promise-unbounded-R-adeg-promise-projective-plane), [promise-unbounded-R-adeg-promise-extremal-forrelation](claims.md#promise-unbounded-R-adeg-promise-extremal-forrelation), [promise-unbounded-R-adeg-promise-unique-mark-color](claims.md#promise-unbounded-R-adeg-promise-unique-mark-color).
- C / D: finite_upper_bound; [C-D](claims.md#C-D).
- C / R0: finite_upper_bound; [C-R0](claims.md#C-R0).
- C / R: no_finite_power; [promise-unbounded-C-R-promise-restricted-DJ](claims.md#promise-unbounded-C-R-promise-restricted-DJ).
- C / RC: no_finite_power; [promise-unbounded-C-RC-promise-restricted-DJ](claims.md#promise-unbounded-C-RC-promise-restricted-DJ).
- C / bs: no_finite_power; [promise-unbounded-C-bs-promise-projective-plane](claims.md#promise-unbounded-C-bs-promise-projective-plane), [promise-unbounded-C-bs-promise-restricted-DJ](claims.md#promise-unbounded-C-bs-promise-restricted-DJ).
- C / s: no_finite_power; [promise-unbounded-C-s-promise-doubled-parity](claims.md#promise-unbounded-C-s-promise-doubled-parity), [promise-unbounded-C-s-promise-projective-plane](claims.md#promise-unbounded-C-s-promise-projective-plane), [promise-unbounded-C-s-promise-restricted-DJ](claims.md#promise-unbounded-C-s-promise-restricted-DJ).
- C / lambda: no_finite_power; [promise-unbounded-C-lambda-promise-doubled-parity](claims.md#promise-unbounded-C-lambda-promise-doubled-parity), [promise-unbounded-C-lambda-promise-projective-plane](claims.md#promise-unbounded-C-lambda-promise-projective-plane), [promise-unbounded-C-lambda-promise-restricted-DJ](claims.md#promise-unbounded-C-lambda-promise-restricted-DJ).
- C / QE: no_finite_power; [promise-unbounded-C-QE-promise-restricted-DJ](claims.md#promise-unbounded-C-QE-promise-restricted-DJ).
- C / deg: no_finite_power; [promise-unbounded-C-deg-promise-unit-OR](claims.md#promise-unbounded-C-deg-promise-unit-OR), [promise-unbounded-C-deg-promise-projective-plane](claims.md#promise-unbounded-C-deg-promise-projective-plane), [promise-unbounded-C-deg-promise-restricted-DJ](claims.md#promise-unbounded-C-deg-promise-restricted-DJ).
- C / Q: no_finite_power; [promise-unbounded-C-Q-promise-restricted-DJ](claims.md#promise-unbounded-C-Q-promise-restricted-DJ).
- C / adeg: no_finite_power; [promise-unbounded-C-adeg-promise-unit-OR](claims.md#promise-unbounded-C-adeg-promise-unit-OR), [promise-unbounded-C-adeg-promise-projective-plane](claims.md#promise-unbounded-C-adeg-promise-projective-plane), [promise-unbounded-C-adeg-promise-restricted-DJ](claims.md#promise-unbounded-C-adeg-promise-restricted-DJ).
- RC / D: finite_upper_bound; [RC-R](claims.md#RC-R), [R-D](claims.md#R-D).
- RC / R0: finite_upper_bound; [RC-R](claims.md#RC-R), [R-R0](claims.md#R-R0).
- RC / R: finite_upper_bound; [RC-R](claims.md#RC-R).
- RC / C: finite_upper_bound; [RC-C](claims.md#RC-C).
- RC / bs: no_finite_power; [promise-unbounded-RC-bs-promise-projective-plane](claims.md#promise-unbounded-RC-bs-promise-projective-plane).
- RC / s: no_finite_power; [promise-unbounded-RC-s-promise-doubled-parity](claims.md#promise-unbounded-RC-s-promise-doubled-parity), [promise-unbounded-RC-s-promise-projective-plane](claims.md#promise-unbounded-RC-s-promise-projective-plane).
- RC / lambda: no_finite_power; [promise-unbounded-RC-lambda-promise-doubled-parity](claims.md#promise-unbounded-RC-lambda-promise-doubled-parity), [promise-unbounded-RC-lambda-promise-projective-plane](claims.md#promise-unbounded-RC-lambda-promise-projective-plane).
- RC / QE: finite_upper_bound; [partial-RC-Q2](claims.md#partial-RC-Q2), [Q-QE](claims.md#Q-QE).
- RC / deg: no_finite_power; [promise-unbounded-RC-deg-promise-unit-OR](claims.md#promise-unbounded-RC-deg-promise-unit-OR), [promise-unbounded-RC-deg-promise-projective-plane](claims.md#promise-unbounded-RC-deg-promise-projective-plane).
- RC / Q: finite_upper_bound; [partial-RC-Q2](claims.md#partial-RC-Q2).
- RC / adeg: no_finite_power; [promise-unbounded-RC-adeg-promise-unit-OR](claims.md#promise-unbounded-RC-adeg-promise-unit-OR), [promise-unbounded-RC-adeg-promise-projective-plane](claims.md#promise-unbounded-RC-adeg-promise-projective-plane).
- bs / D: finite_upper_bound; [bs-R](claims.md#bs-R), [R-D](claims.md#R-D).
- bs / R0: finite_upper_bound; [bs-R](claims.md#bs-R), [R-R0](claims.md#R-R0).
- bs / R: finite_upper_bound; [bs-R](claims.md#bs-R).
- bs / C: finite_upper_bound; [bs-C](claims.md#bs-C).
- bs / RC: finite_upper_bound; [partial-bs-RC](claims.md#partial-bs-RC).
- bs / s: no_finite_power; [promise-unbounded-bs-s-promise-doubled-parity](claims.md#promise-unbounded-bs-s-promise-doubled-parity).
- bs / lambda: no_finite_power; [promise-unbounded-bs-lambda-promise-doubled-parity](claims.md#promise-unbounded-bs-lambda-promise-doubled-parity).
- bs / QE: finite_upper_bound; [partial-bs-RC](claims.md#partial-bs-RC), [partial-RC-Q2](claims.md#partial-RC-Q2), [Q-QE](claims.md#Q-QE).
- bs / deg: no_finite_power; [promise-unbounded-bs-deg-promise-unit-OR](claims.md#promise-unbounded-bs-deg-promise-unit-OR).
- bs / Q: finite_upper_bound; [partial-bs-RC](claims.md#partial-bs-RC), [partial-RC-Q2](claims.md#partial-RC-Q2).
- bs / adeg: no_finite_power; [promise-unbounded-bs-adeg-promise-unit-OR](claims.md#promise-unbounded-bs-adeg-promise-unit-OR).
- s / D: finite_upper_bound; [s-bs](claims.md#s-bs), [bs-R](claims.md#bs-R), [R-D](claims.md#R-D).
- s / R0: finite_upper_bound; [s-bs](claims.md#s-bs), [bs-R](claims.md#bs-R), [R-R0](claims.md#R-R0).
- s / R: finite_upper_bound; [s-bs](claims.md#s-bs), [bs-R](claims.md#bs-R).
- s / C: finite_upper_bound; [s-bs](claims.md#s-bs), [bs-C](claims.md#bs-C).
- s / RC: finite_upper_bound; [s-bs](claims.md#s-bs), [partial-bs-RC](claims.md#partial-bs-RC).
- s / bs: finite_upper_bound; [s-bs](claims.md#s-bs).
- s / lambda: finite_upper_bound; [s-lambda2](claims.md#s-lambda2).
- s / QE: finite_upper_bound; [s-lambda2](claims.md#s-lambda2), [partial-lambda-Q](claims.md#partial-lambda-Q), [Q-QE](claims.md#Q-QE).
- s / deg: no_finite_power; [promise-unbounded-s-deg-promise-unit-OR](claims.md#promise-unbounded-s-deg-promise-unit-OR).
- s / Q: finite_upper_bound; [s-lambda2](claims.md#s-lambda2), [partial-lambda-Q](claims.md#partial-lambda-Q).
- s / adeg: no_finite_power; [promise-unbounded-s-adeg-promise-unit-OR](claims.md#promise-unbounded-s-adeg-promise-unit-OR).
- lambda / D: finite_upper_bound; [partial-lambda-Q](claims.md#partial-lambda-Q), [Q-R](claims.md#Q-R), [R-D](claims.md#R-D).
- lambda / R0: finite_upper_bound; [partial-lambda-Q](claims.md#partial-lambda-Q), [Q-R](claims.md#Q-R), [R-R0](claims.md#R-R0).
- lambda / R: finite_upper_bound; [partial-lambda-Q](claims.md#partial-lambda-Q), [Q-R](claims.md#Q-R).
- lambda / C: finite_upper_bound; [lambda-s](claims.md#lambda-s), [s-bs](claims.md#s-bs), [bs-C](claims.md#bs-C).
- lambda / RC: finite_upper_bound; [lambda-s](claims.md#lambda-s), [s-bs](claims.md#s-bs), [partial-bs-RC](claims.md#partial-bs-RC).
- lambda / bs: finite_upper_bound; [lambda-s](claims.md#lambda-s), [s-bs](claims.md#s-bs).
- lambda / s: finite_upper_bound; [lambda-s](claims.md#lambda-s).
- lambda / QE: finite_upper_bound; [partial-lambda-Q](claims.md#partial-lambda-Q), [Q-QE](claims.md#Q-QE).
- lambda / deg: no_finite_power; [promise-unbounded-lambda-deg-promise-unit-OR](claims.md#promise-unbounded-lambda-deg-promise-unit-OR).
- lambda / Q: finite_upper_bound; [partial-lambda-Q](claims.md#partial-lambda-Q).
- lambda / adeg: no_finite_power; [promise-unbounded-lambda-adeg-promise-unit-OR](claims.md#promise-unbounded-lambda-adeg-promise-unit-OR).
- QE / D: finite_upper_bound; [QE-D](claims.md#QE-D).
- QE / R0: no_finite_power; [promise-unbounded-QE-R0-promise-dense-two-axes](claims.md#promise-unbounded-QE-R0-promise-dense-two-axes).
- QE / R: no_finite_power; [promise-unbounded-QE-R-promise-dense-two-axes](claims.md#promise-unbounded-QE-R-promise-dense-two-axes).
- QE / C: no_finite_power; [promise-unbounded-QE-C-promise-dense-two-axes](claims.md#promise-unbounded-QE-C-promise-dense-two-axes), [promise-unbounded-QE-C-promise-nonempty-two-axes](claims.md#promise-unbounded-QE-C-promise-nonempty-two-axes).
- QE / RC: no_finite_power; [promise-unbounded-QE-RC-promise-dense-two-axes](claims.md#promise-unbounded-QE-RC-promise-dense-two-axes), [promise-unbounded-QE-RC-promise-nonempty-two-axes](claims.md#promise-unbounded-QE-RC-promise-nonempty-two-axes).
- QE / bs: no_finite_power; [promise-unbounded-QE-bs-promise-dense-two-axes](claims.md#promise-unbounded-QE-bs-promise-dense-two-axes), [promise-unbounded-QE-bs-promise-nonempty-two-axes](claims.md#promise-unbounded-QE-bs-promise-nonempty-two-axes).
- QE / s: no_finite_power; [promise-unbounded-QE-s-promise-doubled-parity](claims.md#promise-unbounded-QE-s-promise-doubled-parity), [promise-unbounded-QE-s-promise-dense-two-axes](claims.md#promise-unbounded-QE-s-promise-dense-two-axes), [promise-unbounded-QE-s-promise-nonempty-two-axes](claims.md#promise-unbounded-QE-s-promise-nonempty-two-axes).
- QE / lambda: no_finite_power; [promise-unbounded-QE-lambda-promise-doubled-parity](claims.md#promise-unbounded-QE-lambda-promise-doubled-parity), [promise-unbounded-QE-lambda-promise-dense-two-axes](claims.md#promise-unbounded-QE-lambda-promise-dense-two-axes), [promise-unbounded-QE-lambda-promise-nonempty-two-axes](claims.md#promise-unbounded-QE-lambda-promise-nonempty-two-axes).
- QE / deg: no_finite_power; [promise-unbounded-QE-deg-promise-unit-OR](claims.md#promise-unbounded-QE-deg-promise-unit-OR).
- QE / Q: no_finite_power; [promise-unbounded-QE-Q-promise-dense-two-axes](claims.md#promise-unbounded-QE-Q-promise-dense-two-axes).
- QE / adeg: no_finite_power; [promise-unbounded-QE-adeg-promise-unit-OR](claims.md#promise-unbounded-QE-adeg-promise-unit-OR), [promise-unbounded-QE-adeg-promise-dense-two-axes](claims.md#promise-unbounded-QE-adeg-promise-dense-two-axes).
- deg / D: finite_upper_bound; [deg-QE](claims.md#deg-QE), [QE-D](claims.md#QE-D).
- deg / R0: no_finite_power; [promise-unbounded-deg-R0-promise-dense-two-axes](claims.md#promise-unbounded-deg-R0-promise-dense-two-axes).
- deg / R: no_finite_power; [promise-unbounded-deg-R-promise-dense-two-axes](claims.md#promise-unbounded-deg-R-promise-dense-two-axes).
- deg / C: no_finite_power; [promise-unbounded-deg-C-promise-dense-two-axes](claims.md#promise-unbounded-deg-C-promise-dense-two-axes), [promise-unbounded-deg-C-promise-nonempty-two-axes](claims.md#promise-unbounded-deg-C-promise-nonempty-two-axes).
- deg / RC: no_finite_power; [promise-unbounded-deg-RC-promise-dense-two-axes](claims.md#promise-unbounded-deg-RC-promise-dense-two-axes), [promise-unbounded-deg-RC-promise-nonempty-two-axes](claims.md#promise-unbounded-deg-RC-promise-nonempty-two-axes).
- deg / bs: no_finite_power; [promise-unbounded-deg-bs-promise-dense-two-axes](claims.md#promise-unbounded-deg-bs-promise-dense-two-axes), [promise-unbounded-deg-bs-promise-nonempty-two-axes](claims.md#promise-unbounded-deg-bs-promise-nonempty-two-axes).
- deg / s: no_finite_power; [promise-unbounded-deg-s-promise-doubled-parity](claims.md#promise-unbounded-deg-s-promise-doubled-parity), [promise-unbounded-deg-s-promise-dense-two-axes](claims.md#promise-unbounded-deg-s-promise-dense-two-axes), [promise-unbounded-deg-s-promise-nonempty-two-axes](claims.md#promise-unbounded-deg-s-promise-nonempty-two-axes).
- deg / lambda: no_finite_power; [promise-unbounded-deg-lambda-promise-doubled-parity](claims.md#promise-unbounded-deg-lambda-promise-doubled-parity), [promise-unbounded-deg-lambda-promise-dense-two-axes](claims.md#promise-unbounded-deg-lambda-promise-dense-two-axes), [promise-unbounded-deg-lambda-promise-nonempty-two-axes](claims.md#promise-unbounded-deg-lambda-promise-nonempty-two-axes).
- deg / QE: finite_upper_bound; [deg-QE](claims.md#deg-QE).
- deg / Q: no_finite_power; [promise-unbounded-deg-Q-promise-dense-two-axes](claims.md#promise-unbounded-deg-Q-promise-dense-two-axes).
- deg / adeg: no_finite_power; [promise-unbounded-deg-adeg-promise-dense-two-axes](claims.md#promise-unbounded-deg-adeg-promise-dense-two-axes).
- Q / D: finite_upper_bound; [Q-R](claims.md#Q-R), [R-D](claims.md#R-D).
- Q / R0: finite_upper_bound; [Q-R](claims.md#Q-R), [R-R0](claims.md#R-R0).
- Q / R: finite_upper_bound; [Q-R](claims.md#Q-R).
- Q / C: no_finite_power; [promise-unbounded-Q-C-promise-nonempty-two-axes](claims.md#promise-unbounded-Q-C-promise-nonempty-two-axes).
- Q / RC: no_finite_power; [promise-unbounded-Q-RC-promise-nonempty-two-axes](claims.md#promise-unbounded-Q-RC-promise-nonempty-two-axes).
- Q / bs: no_finite_power; [promise-unbounded-Q-bs-promise-nonempty-two-axes](claims.md#promise-unbounded-Q-bs-promise-nonempty-two-axes).
- Q / s: no_finite_power; [promise-unbounded-Q-s-promise-doubled-parity](claims.md#promise-unbounded-Q-s-promise-doubled-parity), [promise-unbounded-Q-s-promise-nonempty-two-axes](claims.md#promise-unbounded-Q-s-promise-nonempty-two-axes).
- Q / lambda: no_finite_power; [promise-unbounded-Q-lambda-promise-doubled-parity](claims.md#promise-unbounded-Q-lambda-promise-doubled-parity), [promise-unbounded-Q-lambda-promise-nonempty-two-axes](claims.md#promise-unbounded-Q-lambda-promise-nonempty-two-axes).
- Q / QE: finite_upper_bound; [Q-QE](claims.md#Q-QE).
- Q / deg: no_finite_power; [promise-unbounded-Q-deg-promise-unit-OR](claims.md#promise-unbounded-Q-deg-promise-unit-OR).
- Q / adeg: no_finite_power; [promise-unbounded-Q-adeg-promise-unit-OR](claims.md#promise-unbounded-Q-adeg-promise-unit-OR).
- adeg / D: finite_upper_bound; [partial-adeg-R](claims.md#partial-adeg-R), [R-D](claims.md#R-D).
- adeg / R0: finite_upper_bound; [partial-adeg-R](claims.md#partial-adeg-R), [R-R0](claims.md#R-R0).
- adeg / R: finite_upper_bound; [partial-adeg-R](claims.md#partial-adeg-R).
- adeg / C: no_finite_power; [promise-unbounded-adeg-C-promise-nonempty-two-axes](claims.md#promise-unbounded-adeg-C-promise-nonempty-two-axes).
- adeg / RC: no_finite_power; [promise-unbounded-adeg-RC-promise-nonempty-two-axes](claims.md#promise-unbounded-adeg-RC-promise-nonempty-two-axes).
- adeg / bs: no_finite_power; [promise-unbounded-adeg-bs-promise-nonempty-two-axes](claims.md#promise-unbounded-adeg-bs-promise-nonempty-two-axes).
- adeg / s: no_finite_power; [promise-unbounded-adeg-s-promise-doubled-parity](claims.md#promise-unbounded-adeg-s-promise-doubled-parity), [promise-unbounded-adeg-s-promise-nonempty-two-axes](claims.md#promise-unbounded-adeg-s-promise-nonempty-two-axes).
- adeg / lambda: no_finite_power; [promise-unbounded-adeg-lambda-promise-doubled-parity](claims.md#promise-unbounded-adeg-lambda-promise-doubled-parity), [promise-unbounded-adeg-lambda-promise-nonempty-two-axes](claims.md#promise-unbounded-adeg-lambda-promise-nonempty-two-axes).
- adeg / QE: finite_upper_bound; [adeg-deg](claims.md#adeg-deg), [deg-QE](claims.md#deg-QE).
- adeg / deg: finite_upper_bound; [adeg-deg](claims.md#adeg-deg).
- adeg / Q: finite_upper_bound; [adeg-Q](claims.md#adeg-Q).
