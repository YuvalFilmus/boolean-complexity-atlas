# Total-function core matrix

Each entry is **recorded lower exponent / recorded upper exponent**. Rows are A, columns B for A=O(B^p). These are infimum-exponent bounds; matching endpoints do not assert constant-factor tightness. A † marks an upper bound whose endpoint still has a logarithmic loss.

All 132 off-diagonal cells have source-linked support or an explicit derivation. This is complete grid coverage for these twelve measures, not exhaustive literature verification or coverage of all 134+ measures. The JSON stores claim IDs, exact lower-exponent expressions, publication caveats and historical entries. Repository-preprint evidence is included and remains labelled.

| A \ B | D | R0 | R | C | RC | bs | s | lambda | QE | deg | Q | adeg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D | 1/1 | 2/2 | 2/3 | 2/2 | 2/3 | 2/3 | 3/6 | 4/6 | 2/3 | 2/3 | 4/4 | 4/4 |
| R0 | 1/1 | 1/1 | 2/2† | 2/2 | 2/3 | 2/3 | 3/6 | 4/6 | 2/3 | 2/3 | 4/4 | 4/4 |
| R | 1/1 | 1/1 | 1/1 | 2/2 | 2/3 | 2/3 | 3/6 | 4/6 | 1.50000…/3 | 2/3 | 4/4 | 4/4 |
| C | 1/1 | 1/1 | 2/2 | 1/1 | 2/2 | 2/2 | 3/5 | 4/6 | 2/3 | 2/3 | 4/4 | 4/4 |
| RC | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 | 1.50000…/2 | 2/4 | 2.12700…/4 | 1.15270…/2 | 1.63093…/2 | 2/2 | 2/2 |
| bs | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 | 2/4 | 2.12700…/4 | 1.15270…/2 | 1.63093…/2 | 2/2 | 2/2 |
| s | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 | 2/2 | 1.15270…/2 | 1.63093…/2 | 2/2 | 2/2 |
| lambda | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 |
| QE | 1/1 | 1.32674…/2 | 1.32674…/3 | 2/2 | 2/3 | 2/3 | 3/6 | 4/6 | 1/1 | 2/3 | 2/4 | 4/4 |
| deg | 1/1 | 1.32674…/2 | 1.32674…/2 | 2/2 | 2/2 | 2/2 | 2/2 | 2/2 | 1/1 | 1/1 | 2/2 | 2/2 |
| Q | 1/1 | 1/1 | 1/1 | 2/2 | 2/3 | 2/3 | 3/6 | 4/6 | 1/1 | 2/3 | 1/1 | 4/4 |
| adeg | 1/1 | 1/1 | 1/1 | 2/2 | 2/2 | 2/2 | 2/2 | 2/2 | 1/1 | 1/1 | 1/1 | 1/1 |

## Evidence for each ordered pair

### D / R0

Lower: 2; witness `D-R0-sep-ABB`; claims `D-R0-sep-ABB`.

Upper: 2 (endpoint without logarithmic loss). Claims: `D-C2`, `C-R0`.

2021 table: 2/2; attributed there to ABBLS17. Historical rounded labels are not exact exponents.

### D / R

Lower: 2; witness `C-R2-sep-BK`; claims `C-R2-sep-BK`, `C-D`.

Upper: 3 (endpoint without logarithmic loss). Claims: `D-R3`.

2021 table: 2/3; attributed there to ABBLS17. Historical rounded labels are not exact exponents.

### D / C

Lower: 2; witness `D-UC-sep-AKK`; claims `D-UC-sep-AKK`, `C-UC`.

Upper: 2 (endpoint without logarithmic loss). Claims: `D-C2`.

2021 table: 2/2; attributed there to ANDOR. Historical rounded labels are not exact exponents.

### D / RC

Lower: (4/2); witness `D-Q4-sep`; claims `D-Q4-sep`, `partial-RC-Q2`.

Upper: 3 (endpoint without logarithmic loss). Claims: `D-bs3`, `partial-bs-RC`.

2021 table: 2/3; attributed there to ANDOR. Historical rounded labels are not exact exponents.

### D / bs

Lower: (4/2); witness `D-Q4-sep`; claims `D-Q4-sep`, `partial-bs-RC`, `partial-RC-Q2`.

Upper: 3 (endpoint without logarithmic loss). Claims: `D-bs3`.

2021 table: 2/3; attributed there to ANDOR. Historical rounded labels are not exact exponents.

### D / s

Lower: 3; witness `C-s3-Pab`; claims `C-s3-Pab`, `C-D`.

Upper: 6 (endpoint without logarithmic loss). Claims: `D-deg3`, `deg-s2`.

2021 table: 3/6; attributed there to BHT17. Historical rounded labels are not exact exponents.

### D / lambda

Lower: 4; witness `D-Q4-sep`; claims `D-Q4-sep`, `partial-lambda-Q`.

Upper: 6 (endpoint without logarithmic loss). Claims: `D-deg3`, `deg-lambda2`.

2021 table: 4/6; attributed there to ABBLS17. Historical rounded labels are not exact exponents.

### D / QE

Lower: 2; witness `R0-QE-sep-ABB`; claims `R0-QE-sep-ABB`, `R0-D`.

Upper: 3 (endpoint without logarithmic loss). Claims: `D-deg3`, `deg-QE`.

2021 table: 2/3; attributed there to ABBLS17. Historical rounded labels are not exact exponents.

### D / deg

Lower: (4/2); witness `D-Q4-sep`; claims `D-Q4-sep`, `deg-Q2`.

Upper: 3 (endpoint without logarithmic loss). Claims: `D-deg3`.

2021 table: 2/3; attributed there to GPW18. Historical rounded labels are not exact exponents.

### D / Q

Lower: 4; witness `D-Q4-sep`; claims `D-Q4-sep`.

Upper: 4 (endpoint without logarithmic loss). Claims: `D-Q4`.

2021 table: 4/4; attributed there to ABBLS17. Historical rounded labels are not exact exponents.

### D / adeg

Lower: 4; witness `D-Q4-sep`; claims `D-Q4-sep`, `adeg-Q`.

Upper: 4 (endpoint without logarithmic loss). Claims: `D-adeg4`.

2021 table: 4/4; attributed there to ABBLS17. Historical rounded labels are not exact exponents.

### R0 / D

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `R0-D`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### R0 / R

Lower: 2; witness `R0-R-sep-ABB`; claims `R0-R-sep-ABB`.

Upper: 2 (infimum bound; logarithmic endpoint loss retained). Claims: `R0-R2`.

2021 table: 2/2; attributed there to ABBLS17. Historical rounded labels are not exact exponents.

### R0 / C

Lower: 2; witness `Q-C2-sep`; claims `Q-C2-sep`, `Q-R`, `R-R0`.

Upper: 2 (endpoint without logarithmic loss). Claims: `R0-D`, `D-C2`.

2021 table: 2/2; attributed there to ANDOR. Historical rounded labels are not exact exponents.

### R0 / RC

Lower: (4/2); witness `R0-Q4-sep`; claims `R0-Q4-sep`, `partial-RC-Q2`.

Upper: 3 (endpoint without logarithmic loss). Claims: `R0-D`, `D-bs3`, `partial-bs-RC`.

2021 table: 2/3; attributed there to ANDOR. Historical rounded labels are not exact exponents.

### R0 / bs

Lower: 2; witness `R0-R-sep-ABB`; claims `R0-R-sep-ABB`, `bs-R`.

Upper: 3 (endpoint without logarithmic loss). Claims: `R0-D`, `D-bs3`.

2021 table: 2/3; attributed there to ANDOR. Historical rounded labels are not exact exponents.

### R0 / s

Lower: 3; witness `C-s3-Pab`; claims `C-s3-Pab`, `C-R0`.

Upper: 6 (endpoint without logarithmic loss). Claims: `R0-D`, `D-deg3`, `deg-s2`.

2021 table: 3/6; attributed there to BHT17. Historical rounded labels are not exact exponents.

### R0 / lambda

Lower: 4; witness `R0-Q4-sep`; claims `R0-Q4-sep`, `partial-lambda-Q`.

Upper: 6 (endpoint without logarithmic loss). Claims: `R0-D`, `D-deg3`, `deg-lambda2`.

2021 table: 4/6; attributed there to ABBLS17. Historical rounded labels are not exact exponents.

### R0 / QE

Lower: 2; witness `R0-QE-sep-ABB`; claims `R0-QE-sep-ABB`.

Upper: 3 (endpoint without logarithmic loss). Claims: `R0-D`, `D-deg3`, `deg-QE`.

2021 table: 2/3; attributed there to ABBLS17. Historical rounded labels are not exact exponents.

### R0 / deg

Lower: (4/2); witness `R0-Q4-sep`; claims `R0-Q4-sep`, `deg-Q2`.

Upper: 3 (endpoint without logarithmic loss). Claims: `R0-D`, `D-deg3`.

2021 table: 2/3; attributed there to GJPW18. Historical rounded labels are not exact exponents.

### R0 / Q

Lower: 4; witness `R0-Q4-sep`; claims `R0-Q4-sep`.

Upper: 4 (endpoint without logarithmic loss). Claims: `R0-Q4-upper`.

2021 table: 3/4; attributed there to ABBLS17. Historical rounded labels are not exact exponents.

### R0 / adeg

Lower: 4; witness `C-adeg4-sep`; claims `C-adeg4-sep`, `C-R0`.

Upper: 4 (endpoint without logarithmic loss). Claims: `R0-D`, `D-adeg4`.

2021 table: 4/4; attributed there to ABBLS17. Historical rounded labels are not exact exponents.

### R / D

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `R-D`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### R / R0

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `R-R0`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### R / C

Lower: 2; witness `Q-C2-sep`; claims `Q-C2-sep`, `Q-R`.

Upper: 2 (endpoint without logarithmic loss). Claims: `R-D`, `D-C2`.

2021 table: 2/2; attributed there to ANDOR. Historical rounded labels are not exact exponents.

### R / RC

Lower: (4/2); witness `R-Q4-sep-2026`; claims `R-Q4-sep-2026`, `partial-RC-Q2`.

Upper: 3 (endpoint without logarithmic loss). Claims: `R-D`, `D-bs3`, `partial-bs-RC`.

2021 table: 2/3; attributed there to ANDOR. Historical rounded labels are not exact exponents.

### R / bs

Lower: (4/2); witness `R-adeg-sep-ABB`; claims `R-adeg-sep-ABB`, `bs-adeg2`.

Upper: 3 (endpoint without logarithmic loss). Claims: `R-D`, `D-bs3`.

2021 table: 2/3; attributed there to ANDOR. Historical rounded labels are not exact exponents.

### R / s

Lower: 3; witness `Q-s3-sep-BHT`; claims `Q-s3-sep-BHT`, `Q-R`.

Upper: 6 (endpoint without logarithmic loss). Claims: `R-D`, `D-deg3`, `deg-s2`.

2021 table: 3/6; attributed there to BHT17. Historical rounded labels are not exact exponents.

### R / lambda

Lower: 4; witness `R-Q4-sep-2026`; claims `R-Q4-sep-2026`, `partial-lambda-Q`.

Upper: 6 (endpoint without logarithmic loss). Claims: `R-D`, `D-deg3`, `deg-lambda2`.

2021 table: 4/6; attributed there to ABBLS17. Historical rounded labels are not exact exponents.

### R / QE

Lower: 3/2; witness `R-QE-sep-ABB`; claims `R-QE-sep-ABB`.

Upper: 3 (endpoint without logarithmic loss). Claims: `R-D`, `D-deg3`, `deg-QE`.

2021 table: 1.5/3; attributed there to ABBLS17. Historical rounded labels are not exact exponents.

### R / deg

Lower: 2; witness `R-deg2-GJPW`; claims `R-deg2-GJPW`.

Upper: 3 (endpoint without logarithmic loss). Claims: `R-D`, `D-deg3`.

2021 table: 2/3; attributed there to GJPW18. Historical rounded labels are not exact exponents.

### R / Q

Lower: 4; witness `R-Q4-sep-2026`; claims `R-Q4-sep-2026`.

Upper: 4 (endpoint without logarithmic loss). Claims: `R-Q4`.

2021 table: 3/4; attributed there to BS21+SSW20. Historical rounded labels are not exact exponents.

### R / adeg

Lower: 4; witness `R-adeg-sep-ABB`; claims `R-adeg-sep-ABB`.

Upper: 4 (endpoint without logarithmic loss). Claims: `R-D`, `D-adeg4`.

2021 table: 4/4; attributed there to ABBLS17. Historical rounded labels are not exact exponents.

### C / D

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `C-D`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### C / R0

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `C-R0`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### C / R

Lower: 2; witness `C-R2-sep-BK`; claims `C-R2-sep-BK`.

Upper: 2 (endpoint without logarithmic loss). Claims: `C-R2`.

2021 table: 1/2; attributed there to parity. Historical rounded labels are not exact exponents.

### C / RC

Lower: 2; witness `C-R2-sep-BK`; claims `C-R2-sep-BK`, `RC-R`.

Upper: 2 (endpoint without logarithmic loss). Claims: `C-bs2`, `partial-bs-RC`.

2021 table: 2/2; attributed there to GSS13. Historical rounded labels are not exact exponents.

### C / bs

Lower: 2; witness `C-R2-sep-BK`; claims `C-R2-sep-BK`, `bs-R`.

Upper: 2 (endpoint without logarithmic loss). Claims: `C-bs2`.

2021 table: 2/2; attributed there to GSS13. Historical rounded labels are not exact exponents.

### C / s

Lower: 3; witness `C-s3-Pab`; claims `C-s3-Pab`.

Upper: 5 (endpoint without logarithmic loss). Claims: `C-bs-s`, `bs-s4`.

2021 table: 2.22/5; attributed there to BHT17. Historical rounded labels are not exact exponents.

### C / lambda

Lower: 4; witness `C-lambda4-BBGJK`; claims `C-lambda4-BBGJK`.

Upper: 6 (endpoint without logarithmic loss). Claims: `C-D`, `D-deg3`, `deg-lambda2`.

2021 table: 2.44/6; attributed there to BHT17footnote. Historical rounded labels are not exact exponents.

### C / QE

Lower: 2; witness `AIK26-C-QE-quadratic`; claims `AIK26-C-QE-quadratic`.

Upper: 3 (endpoint without logarithmic loss). Claims: `C-D`, `D-deg3`, `deg-QE`.

2021 table: 1.15/3; attributed there to Amb13. Historical rounded labels are not exact exponents.

### C / deg

Lower: 2; witness `C-deg2-Pab`; claims `C-deg2-Pab`.

Upper: 3 (endpoint without logarithmic loss). Claims: `C-D`, `D-deg3`.

2021 table: 1.63/3; attributed there to NW95. Historical rounded labels are not exact exponents.

### C / Q

Lower: 4; witness `C-Q4-sep-BK`; claims `C-Q4-sep-BK`.

Upper: 4 (endpoint without logarithmic loss). Claims: `C-Q4`.

2021 table: 2/4; attributed there to AND. Historical rounded labels are not exact exponents.

### C / adeg

Lower: 4; witness `C-adeg4-sep`; claims `C-adeg4-sep`.

Upper: 4 (endpoint without logarithmic loss). Claims: `C-adeg4-upper`.

2021 table: 2/4; attributed there to AND. Historical rounded labels are not exact exponents.

### RC / D

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `RC-R`, `R-D`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### RC / R0

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `RC-R`, `R-R0`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### RC / R

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `RC-R`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### RC / C

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `RC-C`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### RC / bs

Lower: 3/2; witness `fbs-bs-sep-constant`; claims `fbs-bs-sep-constant`, `fbs-RC`.

Upper: 2 (endpoint without logarithmic loss). Claims: `RC-C`, `C-bs2`.

2021 table: 1.5/2; attributed there to GSS13. Historical rounded labels are not exact exponents.

### RC / s

Lower: 2; witness `bs-s2-sep-AS`; claims `bs-s2-sep-AS`, `partial-bs-RC`.

Upper: 4 (endpoint without logarithmic loss). Claims: `RC-adeg2`, `adeg-deg`, `deg-s2`.

2021 table: 2/4; attributed there to Rub95. Historical rounded labels are not exact exponents.

### RC / lambda

Lower: 2.127; witness `bs-lambda-sep-2026`; claims `bs-lambda-sep-2026`, `partial-bs-RC`.

Upper: 4 (endpoint without logarithmic loss). Claims: `RC-adeg2`, `adeg-deg`, `deg-lambda2`.

2021 table: 2/4; attributed there to AND. Historical rounded labels are not exact exponents.

### RC / QE

Lower: (8*log(3)/log(2048)); witness `s-QE-Amb13`; claims `s-QE-Amb13`, `s-bs`, `partial-bs-RC`.

Upper: 2 (endpoint without logarithmic loss). Claims: `partial-RC-Q2`, `Q-QE`.

2021 table: 1.15/2; attributed there to Amb13. Historical rounded labels are not exact exponents.

### RC / deg

Lower: log(6)/log(3); witness `s-deg-Kushilevitz`; claims `s-deg-Kushilevitz`, `s-bs`, `partial-bs-RC`.

Upper: 2 (endpoint without logarithmic loss). Claims: `RC-adeg2`, `adeg-deg`.

2021 table: 1.63/2; attributed there to NW95. Historical rounded labels are not exact exponents.

### RC / Q

Lower: (4/2); witness `C-Q4-sep-BK`; claims `C-Q4-sep-BK`, `C-bs2`, `partial-bs-RC`.

Upper: 2 (endpoint without logarithmic loss). Claims: `partial-RC-Q2`.

2021 table: 2/2; attributed there to AND. Historical rounded labels are not exact exponents.

### RC / adeg

Lower: (4/2); witness `C-adeg4-sep`; claims `C-adeg4-sep`, `C-bs2`, `partial-bs-RC`.

Upper: 2 (endpoint without logarithmic loss). Claims: `RC-adeg2`.

2021 table: 2/2; attributed there to AND. Historical rounded labels are not exact exponents.

### bs / D

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `bs-R`, `R-D`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### bs / R0

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `bs-R`, `R-R0`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### bs / R

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `bs-R`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### bs / C

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `bs-C`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### bs / RC

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `partial-bs-RC`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### bs / s

Lower: 2; witness `bs-s2-sep-AS`; claims `bs-s2-sep-AS`.

Upper: 4 (endpoint without logarithmic loss). Claims: `bs-s4`.

2021 table: 2/4; attributed there to Rub95. Historical rounded labels are not exact exponents.

### bs / lambda

Lower: 2.127; witness `bs-lambda-sep-2026`; claims `bs-lambda-sep-2026`.

Upper: 4 (endpoint without logarithmic loss). Claims: `bs-deg2-Pro`, `deg-lambda2`.

2021 table: 2/4; attributed there to AND. Historical rounded labels are not exact exponents.

### bs / QE

Lower: (8*log(3)/log(2048)); witness `s-QE-Amb13`; claims `s-QE-Amb13`, `s-bs`.

Upper: 2 (endpoint without logarithmic loss). Claims: `bs-deg2-Pro`, `deg-QE`.

2021 table: 1.15/2; attributed there to Amb13. Historical rounded labels are not exact exponents.

### bs / deg

Lower: log(6)/log(3); witness `s-deg-Kushilevitz`; claims `s-deg-Kushilevitz`, `s-bs`.

Upper: 2 (endpoint without logarithmic loss). Claims: `bs-deg2-Pro`.

2021 table: 1.63/2; attributed there to NW95. Historical rounded labels are not exact exponents.

### bs / Q

Lower: (4/2); witness `C-Q4-sep-BK`; claims `C-Q4-sep-BK`, `C-bs2`.

Upper: 2 (endpoint without logarithmic loss). Claims: `partial-bs-RC`, `partial-RC-Q2`.

2021 table: 2/2; attributed there to AND. Historical rounded labels are not exact exponents.

### bs / adeg

Lower: (4/2); witness `C-adeg4-sep`; claims `C-adeg4-sep`, `C-bs2`.

Upper: 2 (endpoint without logarithmic loss). Claims: `bs-adeg2`.

2021 table: 2/2; attributed there to AND. Historical rounded labels are not exact exponents.

### s / D

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `s-bs`, `bs-R`, `R-D`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### s / R0

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `s-bs`, `bs-R`, `R-R0`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### s / R

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `s-bs`, `bs-R`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### s / C

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `s-bs`, `bs-C`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### s / RC

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `s-bs`, `partial-bs-RC`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### s / bs

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `s-bs`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### s / lambda

Lower: 2; witness `OR-s-lambda`; claims `OR-s-lambda`.

Upper: 2 (endpoint without logarithmic loss). Claims: `s-lambda2`.

2021 table: 2/2; attributed there to AND. Historical rounded labels are not exact exponents.

### s / QE

Lower: (8*log(3)/log(2048)); witness `s-QE-Amb13`; claims `s-QE-Amb13`.

Upper: 2 (endpoint without logarithmic loss). Claims: `s-bs`, `bs-deg2-Pro`, `deg-QE`.

2021 table: 1.15/2; attributed there to Amb13. Historical rounded labels are not exact exponents.

### s / deg

Lower: log(6)/log(3); witness `s-deg-Kushilevitz`; claims `s-deg-Kushilevitz`.

Upper: 2 (endpoint without logarithmic loss). Claims: `s-bs`, `bs-deg2-Pro`.

2021 table: 1.63/2; attributed there to NW95. Historical rounded labels are not exact exponents.

### s / Q

Lower: 2; witness `OR-s-Q`; claims `OR-s-Q`.

Upper: 2 (endpoint without logarithmic loss). Claims: `s-lambda2`, `partial-lambda-Q`.

2021 table: 2/2; attributed there to AND. Historical rounded labels are not exact exponents.

### s / adeg

Lower: 2; witness `OR-s-adeg`; claims `OR-s-adeg`.

Upper: 2 (endpoint without logarithmic loss). Claims: `s-bs`, `bs-adeg2`.

2021 table: 2/2; attributed there to AND. Historical rounded labels are not exact exponents.

### lambda / D

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `lambda-deg`, `deg-QE`, `QE-D`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### lambda / R0

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `partial-lambda-Q`, `Q-R`, `R-R0`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### lambda / R

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `partial-lambda-Q`, `Q-R`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### lambda / C

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `lambda-s`, `s-bs`, `bs-C`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### lambda / RC

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `lambda-s`, `s-bs`, `partial-bs-RC`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### lambda / bs

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `lambda-s`, `s-bs`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### lambda / s

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `lambda-s`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### lambda / QE

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `lambda-deg`, `deg-QE`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### lambda / deg

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `lambda-deg`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### lambda / Q

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `partial-lambda-Q`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### lambda / adeg

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `lambda-adeg`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### QE / D

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `QE-D`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### QE / R0

Lower: log(2)/log(((1+sqrt(33))/4)); witness `QE-R0-NAND-SW`; claims `QE-R0-NAND-SW`.

Upper: 2 (endpoint without logarithmic loss). Claims: `QE-D`, `D-C2`, `C-R0`.

2021 table: 1.33/2; attributed there to NANDtree. Historical rounded labels are not exact exponents.

### QE / R

Lower: log(2)/log(((1+sqrt(33))/4)); witness `QE-R0-NAND-SW`; claims `QE-R0-NAND-SW`, `R-R0`.

Upper: 3 (endpoint without logarithmic loss). Claims: `QE-D`, `D-R3`.

2021 table: 1.33/3; attributed there to NANDtree. Historical rounded labels are not exact exponents.

### QE / C

Lower: 2; witness `Q-C2-sep`; claims `Q-C2-sep`, `Q-QE`.

Upper: 2 (endpoint without logarithmic loss). Claims: `QE-D`, `D-C2`.

2021 table: 2/2; attributed there to ANDOR. Historical rounded labels are not exact exponents.

### QE / RC

Lower: 2; witness `Q-C2-sep`; claims `Q-C2-sep`, `Q-QE`, `RC-C`.

Upper: 3 (endpoint without logarithmic loss). Claims: `QE-D`, `D-bs3`, `partial-bs-RC`.

2021 table: 2/3; attributed there to ANDOR. Historical rounded labels are not exact exponents.

### QE / bs

Lower: 2; witness `Q-C2-sep`; claims `Q-C2-sep`, `Q-QE`, `bs-C`.

Upper: 3 (endpoint without logarithmic loss). Claims: `QE-D`, `D-bs3`.

2021 table: 2/3; attributed there to ANDOR. Historical rounded labels are not exact exponents.

### QE / s

Lower: 3; witness `Q-s3-sep-BHT`; claims `Q-s3-sep-BHT`, `Q-QE`.

Upper: 6 (endpoint without logarithmic loss). Claims: `QE-D`, `D-deg3`, `deg-s2`.

2021 table: 3/6; attributed there to BHT17. Historical rounded labels are not exact exponents.

### QE / lambda

Lower: 4; witness `Q-adeg4-sep`; claims `Q-adeg4-sep`, `Q-QE`, `lambda-adeg`.

Upper: 6 (endpoint without logarithmic loss). Claims: `QE-D`, `D-deg3`, `deg-lambda2`.

2021 table: 4/6; attributed there to ABK16. Historical rounded labels are not exact exponents.

### QE / deg

Lower: 2; witness `Q-deg2-ABK`; claims `Q-deg2-ABK`, `Q-QE`.

Upper: 3 (endpoint without logarithmic loss). Claims: `QE-D`, `D-deg3`.

2021 table: 2/3; attributed there to ABK16. Historical rounded labels are not exact exponents.

### QE / Q

Lower: 2; witness `OR-deg-Q`; claims `OR-deg-Q`, `deg-QE`.

Upper: 4 (endpoint without logarithmic loss). Claims: `QE-D`, `D-Q4`.

2021 table: 2/4; attributed there to AND. Historical rounded labels are not exact exponents.

### QE / adeg

Lower: 4; witness `Q-adeg4-sep`; claims `Q-adeg4-sep`, `Q-QE`.

Upper: 4 (endpoint without logarithmic loss). Claims: `QE-D`, `D-adeg4`.

2021 table: 4/4; attributed there to ABK16. Historical rounded labels are not exact exponents.

### deg / D

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `deg-QE`, `QE-D`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### deg / R0

Lower: log(2)/log(((1+sqrt(33))/4)); witness `deg-R0-NAND-SW`; claims `deg-R0-NAND-SW`.

Upper: 2 (endpoint without logarithmic loss). Claims: `deg-Q2`, `Q-R`, `R-R0`.

2021 table: 1.33/2; attributed there to NANDtree. Historical rounded labels are not exact exponents.

### deg / R

Lower: log(2)/log(((1+sqrt(33))/4)); witness `deg-R0-NAND-SW`; claims `deg-R0-NAND-SW`, `R-R0`.

Upper: 2 (endpoint without logarithmic loss). Claims: `deg-Q2`, `Q-R`.

2021 table: 1.33/2; attributed there to NANDtree. Historical rounded labels are not exact exponents.

### deg / C

Lower: 2; witness `deg-C2-ANDOR`; claims `deg-C2-ANDOR`.

Upper: 2 (endpoint without logarithmic loss). Claims: `deg-s2`, `s-bs`, `bs-C`.

2021 table: 2/2; attributed there to ANDOR. Historical rounded labels are not exact exponents.

### deg / RC

Lower: 2; witness `deg-C2-ANDOR`; claims `deg-C2-ANDOR`, `RC-C`.

Upper: 2 (endpoint without logarithmic loss). Claims: `deg-s2`, `s-bs`, `partial-bs-RC`.

2021 table: 2/2; attributed there to ANDOR. Historical rounded labels are not exact exponents.

### deg / bs

Lower: 2; witness `deg-C2-ANDOR`; claims `deg-C2-ANDOR`, `bs-C`.

Upper: 2 (endpoint without logarithmic loss). Claims: `deg-s2`, `s-bs`.

2021 table: 2/2; attributed there to ANDOR. Historical rounded labels are not exact exponents.

### deg / s

Lower: 2; witness `deg-C2-ANDOR`; claims `deg-C2-ANDOR`, `s-bs`, `bs-C`.

Upper: 2 (endpoint without logarithmic loss). Claims: `deg-s2`.

2021 table: 2/2; attributed there to ANDOR. Historical rounded labels are not exact exponents.

### deg / lambda

Lower: 2; witness `OR-deg-Q`; claims `OR-deg-Q`, `partial-lambda-Q`.

Upper: 2 (endpoint without logarithmic loss). Claims: `deg-lambda2`.

2021 table: 2/2; attributed there to AND. Historical rounded labels are not exact exponents.

### deg / QE

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `deg-QE`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### deg / Q

Lower: 2; witness `OR-deg-Q`; claims `OR-deg-Q`.

Upper: 2 (endpoint without logarithmic loss). Claims: `deg-Q2`.

2021 table: 2/2; attributed there to AND. Historical rounded labels are not exact exponents.

### deg / adeg

Lower: 2; witness `OR-deg-adeg`; claims `OR-deg-adeg`.

Upper: 2 (endpoint without logarithmic loss). Claims: `deg-adeg2`.

2021 table: 2/2; attributed there to AND. Historical rounded labels are not exact exponents.

### Q / D

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `Q-R`, `R-D`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### Q / R0

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `Q-R`, `R-R0`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### Q / R

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `Q-R`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### Q / C

Lower: 2; witness `Q-C2-sep`; claims `Q-C2-sep`.

Upper: 2 (endpoint without logarithmic loss). Claims: `Q-C2-upper`.

2021 table: 2/2; attributed there to ABK16. Historical rounded labels are not exact exponents.

### Q / RC

Lower: 2; witness `Q-C2-sep`; claims `Q-C2-sep`, `RC-C`.

Upper: 3 (endpoint without logarithmic loss). Claims: `Q-R`, `R-D`, `D-bs3`, `partial-bs-RC`.

2021 table: 2/3; attributed there to ABK16. Historical rounded labels are not exact exponents.

### Q / bs

Lower: 2; witness `Q-C2-sep`; claims `Q-C2-sep`, `bs-C`.

Upper: 3 (endpoint without logarithmic loss). Claims: `Q-R`, `R-D`, `D-bs3`.

2021 table: 2/3; attributed there to ABK16. Historical rounded labels are not exact exponents.

### Q / s

Lower: 3; witness `Q-s3-sep-BHT`; claims `Q-s3-sep-BHT`.

Upper: 6 (endpoint without logarithmic loss). Claims: `Q-R`, `R-D`, `D-deg3`, `deg-s2`.

2021 table: 3/6; attributed there to BHT17. Historical rounded labels are not exact exponents.

### Q / lambda

Lower: 4; witness `Q-adeg4-sep`; claims `Q-adeg4-sep`, `lambda-adeg`.

Upper: 6 (endpoint without logarithmic loss). Claims: `Q-R`, `R-D`, `D-deg3`, `deg-lambda2`.

2021 table: 4/6; attributed there to ABK16. Historical rounded labels are not exact exponents.

### Q / QE

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `Q-QE`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### Q / deg

Lower: 2; witness `Q-deg2-ABK`; claims `Q-deg2-ABK`.

Upper: 3 (endpoint without logarithmic loss). Claims: `Q-R`, `R-D`, `D-deg3`.

2021 table: 2/3; attributed there to ABK16. Historical rounded labels are not exact exponents.

### Q / adeg

Lower: 4; witness `Q-adeg4-sep`; claims `Q-adeg4-sep`.

Upper: 4 (endpoint without logarithmic loss). Claims: `Q-adeg4-upper`.

2021 table: 4/4; attributed there to ABK16. Historical rounded labels are not exact exponents.

### adeg / D

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `partial-adeg-R`, `R-D`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### adeg / R0

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `partial-adeg-R`, `R-R0`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### adeg / R

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `partial-adeg-R`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### adeg / C

Lower: 2; witness `adeg-C2-BT17`; claims `adeg-C2-BT17`.

Upper: 2 (endpoint without logarithmic loss). Claims: `adeg-Q`, `Q-C2-upper`.

2021 table: 2/2; attributed there to BT17. Historical rounded labels are not exact exponents.

### adeg / RC

Lower: 2; witness `adeg-C2-BT17`; claims `adeg-C2-BT17`, `RC-C`.

Upper: 2 (endpoint without logarithmic loss). Claims: `adeg-deg`, `deg-s2`, `s-bs`, `partial-bs-RC`.

2021 table: 2/2; attributed there to BT17. Historical rounded labels are not exact exponents.

### adeg / bs

Lower: 2; witness `adeg-C2-BT17`; claims `adeg-C2-BT17`, `bs-C`.

Upper: 2 (endpoint without logarithmic loss). Claims: `adeg-deg`, `deg-s2`, `s-bs`.

2021 table: 2/2; attributed there to BT17. Historical rounded labels are not exact exponents.

### adeg / s

Lower: 2; witness `adeg-C2-BT17`; claims `adeg-C2-BT17`, `s-bs`, `bs-C`.

Upper: 2 (endpoint without logarithmic loss). Claims: `adeg-deg`, `deg-s2`.

2021 table: 2/2; attributed there to BT17. Historical rounded labels are not exact exponents.

### adeg / lambda

Lower: 2; witness `adeg-C2-BT17`; claims `adeg-C2-BT17`, `lambda-s`, `s-bs`, `bs-C`.

Upper: 2 (endpoint without logarithmic loss). Claims: `adeg-deg`, `deg-lambda2`.

2021 table: 2/2; attributed there to AND. Historical rounded labels are not exact exponents.

### adeg / QE

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `adeg-deg`, `deg-QE`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### adeg / deg

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `adeg-deg`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

### adeg / Q

Lower: 1; witness `parity-core`; claims .

Upper: 1 (endpoint without logarithmic loss). Claims: `adeg-Q`.

2021 table: 1/1; attributed there to parity. Historical rounded labels are not exact exponents.

