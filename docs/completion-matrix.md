# Minimum-completion exponent bounds

Lift recorded total-core upper chains; no new priority or best-known certification.

For every pair choose the completion optimal for the right-hand measure. The minima may use different completions. Native promise measures are not substituted for minimum-completion measures.

| A | B | Lower exponent | Upper exponent | Pure endpoint? | Base claim chain |
|---|---|---:|---:|---|---|
| completion_D | completion_R0 | 2 | 2 | yes | D-C2, C-R0 |
| completion_D | completion_R | 2 | 3 | yes | D-R3 |
| completion_D | completion_C | 2 | 2 | yes | D-C2 |
| completion_D | completion_RC | {'op': 'div', 'left': 4, 'right': '2'} | 3 | yes | D-bs3, partial-bs-RC |
| completion_D | completion_bs | {'op': 'div', 'left': 4, 'right': '2'} | 3 | yes | D-bs3 |
| completion_D | completion_s | 3 | 6 | yes | D-deg3, deg-s2 |
| completion_D | completion_lambda | 4 | 6 | yes | D-deg3, deg-lambda2 |
| completion_D | completion_QE | 2 | 3 | yes | D-deg3, deg-QE |
| completion_D | completion_deg | {'op': 'div', 'left': 4, 'right': '2'} | 3 | yes | D-deg3 |
| completion_D | completion_Q | 4 | 4 | yes | D-Q4 |
| completion_D | completion_adeg | 4 | 4 | yes | D-adeg4 |
| completion_R0 | completion_D | 1 | 1 | yes | R0-D |
| completion_R0 | completion_R | 2 | 2 | no: retain logarithmic loss | R0-R2 |
| completion_R0 | completion_C | 2 | 2 | yes | R0-D, D-C2 |
| completion_R0 | completion_RC | {'op': 'div', 'left': 4, 'right': '2'} | 3 | yes | R0-D, D-bs3, partial-bs-RC |
| completion_R0 | completion_bs | 2 | 3 | yes | R0-D, D-bs3 |
| completion_R0 | completion_s | 3 | 6 | yes | R0-D, D-deg3, deg-s2 |
| completion_R0 | completion_lambda | 4 | 6 | yes | R0-D, D-deg3, deg-lambda2 |
| completion_R0 | completion_QE | 2 | 3 | yes | R0-D, D-deg3, deg-QE |
| completion_R0 | completion_deg | {'op': 'div', 'left': 4, 'right': '2'} | 3 | yes | R0-D, D-deg3 |
| completion_R0 | completion_Q | 4 | 4 | yes | R0-Q4-upper |
| completion_R0 | completion_adeg | 4 | 4 | yes | R0-D, D-adeg4 |
| completion_R | completion_D | 1 | 1 | yes | R-D |
| completion_R | completion_R0 | 1 | 1 | yes | R-R0 |
| completion_R | completion_C | 2 | 2 | yes | R-D, D-C2 |
| completion_R | completion_RC | {'op': 'div', 'left': 4, 'right': '2'} | 3 | yes | R-D, D-bs3, partial-bs-RC |
| completion_R | completion_bs | {'op': 'div', 'left': 4, 'right': '2'} | 3 | yes | R-D, D-bs3 |
| completion_R | completion_s | 3 | 6 | yes | R-D, D-deg3, deg-s2 |
| completion_R | completion_lambda | 4 | 6 | yes | R-D, D-deg3, deg-lambda2 |
| completion_R | completion_QE | 3/2 | 3 | yes | R-D, D-deg3, deg-QE |
| completion_R | completion_deg | 2 | 3 | yes | R-D, D-deg3 |
| completion_R | completion_Q | 4 | 4 | yes | R-Q4 |
| completion_R | completion_adeg | 4 | 4 | yes | R-D, D-adeg4 |
| completion_C | completion_D | 1 | 1 | yes | C-D |
| completion_C | completion_R0 | 1 | 1 | yes | C-R0 |
| completion_C | completion_R | 2 | 2 | yes | C-R2 |
| completion_C | completion_RC | 2 | 2 | yes | C-bs2, partial-bs-RC |
| completion_C | completion_bs | 2 | 2 | yes | C-bs2 |
| completion_C | completion_s | 3 | 5 | yes | C-bs-s, bs-s4 |
| completion_C | completion_lambda | 4 | 6 | yes | C-D, D-deg3, deg-lambda2 |
| completion_C | completion_QE | 2 | 3 | yes | C-D, D-deg3, deg-QE |
| completion_C | completion_deg | 2 | 3 | yes | C-D, D-deg3 |
| completion_C | completion_Q | 4 | 4 | yes | C-Q4 |
| completion_C | completion_adeg | 4 | 4 | yes | C-adeg4-upper |
| completion_RC | completion_D | 1 | 1 | yes | RC-R, R-D |
| completion_RC | completion_R0 | 1 | 1 | yes | RC-R, R-R0 |
| completion_RC | completion_R | 1 | 1 | yes | RC-R |
| completion_RC | completion_C | 1 | 1 | yes | RC-C |
| completion_RC | completion_bs | 3/2 | 2 | yes | RC-C, C-bs2 |
| completion_RC | completion_s | {'op': 'log_ratio', 'numerator': '1522813785050025472152230187890625', 'denominator': '3738277295413674'} | 4 | yes | RC-adeg2, adeg-deg, deg-s2 |
| completion_RC | completion_lambda | {'op': 'log_ratio', 'numerator': '1522813785050025472152230187890625', 'denominator': '3738277295413674'} | 4 | yes | RC-adeg2, adeg-deg, deg-lambda2 |
| completion_RC | completion_QE | {'op': 'mul', 'left': 8, 'right': {'op': 'log_ratio', 'numerator': 3, 'denominator': 2048}} | 2 | yes | partial-RC-Q2, Q-QE |
| completion_RC | completion_deg | {'op': 'log_ratio', 'numerator': 6, 'denominator': 3} | 2 | yes | RC-adeg2, adeg-deg |
| completion_RC | completion_Q | {'op': 'div', 'left': 4, 'right': '2'} | 2 | yes | partial-RC-Q2 |
| completion_RC | completion_adeg | {'op': 'div', 'left': 4, 'right': '2'} | 2 | yes | RC-adeg2 |
| completion_bs | completion_D | 1 | 1 | yes | bs-R, R-D |
| completion_bs | completion_R0 | 1 | 1 | yes | bs-R, R-R0 |
| completion_bs | completion_R | 1 | 1 | yes | bs-R |
| completion_bs | completion_C | 1 | 1 | yes | bs-C |
| completion_bs | completion_RC | 1 | 1 | yes | partial-bs-RC |
| completion_bs | completion_s | {'op': 'log_ratio', 'numerator': '1522813785050025472152230187890625', 'denominator': '3738277295413674'} | 4 | yes | bs-s4 |
| completion_bs | completion_lambda | {'op': 'log_ratio', 'numerator': '1522813785050025472152230187890625', 'denominator': '3738277295413674'} | 4 | yes | bs-deg2-Pro, deg-lambda2 |
| completion_bs | completion_QE | {'op': 'mul', 'left': 8, 'right': {'op': 'log_ratio', 'numerator': 3, 'denominator': 2048}} | 2 | yes | bs-deg2-Pro, deg-QE |
| completion_bs | completion_deg | {'op': 'log_ratio', 'numerator': 6, 'denominator': 3} | 2 | yes | bs-deg2-Pro |
| completion_bs | completion_Q | {'op': 'div', 'left': 4, 'right': '2'} | 2 | yes | partial-bs-RC, partial-RC-Q2 |
| completion_bs | completion_adeg | {'op': 'div', 'left': 4, 'right': '2'} | 2 | yes | bs-adeg2 |
| completion_s | completion_D | 1 | 1 | yes | s-bs, bs-R, R-D |
| completion_s | completion_R0 | 1 | 1 | yes | s-bs, bs-R, R-R0 |
| completion_s | completion_R | 1 | 1 | yes | s-bs, bs-R |
| completion_s | completion_C | 1 | 1 | yes | s-bs, bs-C |
| completion_s | completion_RC | 1 | 1 | yes | s-bs, partial-bs-RC |
| completion_s | completion_bs | 1 | 1 | yes | s-bs |
| completion_s | completion_lambda | 2 | 2 | yes | s-lambda2 |
| completion_s | completion_QE | {'op': 'mul', 'left': 8, 'right': {'op': 'log_ratio', 'numerator': 3, 'denominator': 2048}} | 2 | yes | s-bs, bs-deg2-Pro, deg-QE |
| completion_s | completion_deg | {'op': 'log_ratio', 'numerator': 6, 'denominator': 3} | 2 | yes | s-bs, bs-deg2-Pro |
| completion_s | completion_Q | 2 | 2 | yes | s-lambda2, partial-lambda-Q |
| completion_s | completion_adeg | 2 | 2 | yes | s-bs, bs-adeg2 |
| completion_lambda | completion_D | 1 | 1 | yes | lambda-deg, deg-QE, QE-D |
| completion_lambda | completion_R0 | 1 | 1 | yes | partial-lambda-Q, Q-R, R-R0 |
| completion_lambda | completion_R | 1 | 1 | yes | partial-lambda-Q, Q-R |
| completion_lambda | completion_C | 1 | 1 | yes | lambda-s, s-bs, bs-C |
| completion_lambda | completion_RC | 1 | 1 | yes | lambda-s, s-bs, partial-bs-RC |
| completion_lambda | completion_bs | 1 | 1 | yes | lambda-s, s-bs |
| completion_lambda | completion_s | 1 | 1 | yes | lambda-s |
| completion_lambda | completion_QE | 1 | 1 | yes | lambda-deg, deg-QE |
| completion_lambda | completion_deg | 1 | 1 | yes | lambda-deg |
| completion_lambda | completion_Q | 1 | 1 | yes | partial-lambda-Q |
| completion_lambda | completion_adeg | 1 | 1 | yes | lambda-adeg |
| completion_QE | completion_D | 1 | 1 | yes | QE-D |
| completion_QE | completion_R0 | {'op': 'log_ratio', 'numerator': 2, 'denominator': {'op': 'div', 'left': {'op': 'add', 'left': 1, 'right': {'op': 'sqrt', 'arg': 33}}, 'right': 4}} | 2 | yes | QE-D, D-C2, C-R0 |
| completion_QE | completion_R | {'op': 'log_ratio', 'numerator': 2, 'denominator': {'op': 'div', 'left': {'op': 'add', 'left': 1, 'right': {'op': 'sqrt', 'arg': 33}}, 'right': 4}} | 3 | yes | QE-D, D-R3 |
| completion_QE | completion_C | 2 | 2 | yes | QE-D, D-C2 |
| completion_QE | completion_RC | 2 | 3 | yes | QE-D, D-bs3, partial-bs-RC |
| completion_QE | completion_bs | 2 | 3 | yes | QE-D, D-bs3 |
| completion_QE | completion_s | 3 | 6 | yes | QE-D, D-deg3, deg-s2 |
| completion_QE | completion_lambda | 4 | 6 | yes | QE-D, D-deg3, deg-lambda2 |
| completion_QE | completion_deg | 2 | 3 | yes | QE-D, D-deg3 |
| completion_QE | completion_Q | 2 | 4 | yes | QE-D, D-Q4 |
| completion_QE | completion_adeg | 4 | 4 | yes | QE-D, D-adeg4 |
| completion_deg | completion_D | 1 | 1 | yes | deg-QE, QE-D |
| completion_deg | completion_R0 | {'op': 'log_ratio', 'numerator': 2, 'denominator': {'op': 'div', 'left': {'op': 'add', 'left': 1, 'right': {'op': 'sqrt', 'arg': 33}}, 'right': 4}} | 2 | yes | deg-Q2, Q-R, R-R0 |
| completion_deg | completion_R | {'op': 'log_ratio', 'numerator': 2, 'denominator': {'op': 'div', 'left': {'op': 'add', 'left': 1, 'right': {'op': 'sqrt', 'arg': 33}}, 'right': 4}} | 2 | yes | deg-Q2, Q-R |
| completion_deg | completion_C | 2 | 2 | yes | deg-s2, s-bs, bs-C |
| completion_deg | completion_RC | 2 | 2 | yes | deg-s2, s-bs, partial-bs-RC |
| completion_deg | completion_bs | 2 | 2 | yes | deg-s2, s-bs |
| completion_deg | completion_s | 2 | 2 | yes | deg-s2 |
| completion_deg | completion_lambda | 2 | 2 | yes | deg-lambda2 |
| completion_deg | completion_QE | 1 | 1 | yes | deg-QE |
| completion_deg | completion_Q | 2 | 2 | yes | deg-Q2 |
| completion_deg | completion_adeg | 2 | 2 | yes | deg-adeg2 |
| completion_Q | completion_D | 1 | 1 | yes | Q-R, R-D |
| completion_Q | completion_R0 | 1 | 1 | yes | Q-R, R-R0 |
| completion_Q | completion_R | 1 | 1 | yes | Q-R |
| completion_Q | completion_C | 2 | 2 | yes | Q-C2-upper |
| completion_Q | completion_RC | 2 | 3 | yes | Q-R, R-D, D-bs3, partial-bs-RC |
| completion_Q | completion_bs | 2 | 3 | yes | Q-R, R-D, D-bs3 |
| completion_Q | completion_s | 3 | 6 | yes | Q-R, R-D, D-deg3, deg-s2 |
| completion_Q | completion_lambda | 4 | 6 | yes | Q-R, R-D, D-deg3, deg-lambda2 |
| completion_Q | completion_QE | 1 | 1 | yes | Q-QE |
| completion_Q | completion_deg | 2 | 3 | yes | Q-R, R-D, D-deg3 |
| completion_Q | completion_adeg | 4 | 4 | yes | Q-adeg4-upper |
| completion_adeg | completion_D | 1 | 1 | yes | partial-adeg-R, R-D |
| completion_adeg | completion_R0 | 1 | 1 | yes | partial-adeg-R, R-R0 |
| completion_adeg | completion_R | 1 | 1 | yes | partial-adeg-R |
| completion_adeg | completion_C | 2 | 2 | yes | adeg-Q, Q-C2-upper |
| completion_adeg | completion_RC | 2 | 2 | yes | adeg-deg, deg-s2, s-bs, partial-bs-RC |
| completion_adeg | completion_bs | 2 | 2 | yes | adeg-deg, deg-s2, s-bs |
| completion_adeg | completion_s | 2 | 2 | yes | adeg-deg, deg-s2 |
| completion_adeg | completion_lambda | 2 | 2 | yes | adeg-deg, deg-lambda2 |
| completion_adeg | completion_QE | 1 | 1 | yes | adeg-deg, deg-QE |
| completion_adeg | completion_deg | 1 | 1 | yes | adeg-deg |
| completion_adeg | completion_Q | 1 | 1 | yes | adeg-Q |
