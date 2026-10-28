# Corrected Experiment Summary

## Important scoring correction
The initial harness interpreted verifier script exit code 0 as task success.
A post-hoc audit of each official verifier log found that the verifier scripts
can exit normally even when their internal tests fail. Therefore, all reported
success values were recomputed from official verifier output rather than shell
exit codes.

## Corrected validation result
All four search methods obtained verified validation pass@1 = 0.0 on the
two-task validation set.

## Cost result
Observed cumulative costs differed substantially:
- Default: $0.062066
- Random Search: $0.225147
- Bayesian Optimization: $0.242667
- Custom Cost-Aware Search: $0.320940

## Held-out result
The frozen configuration final_c0_off_default obtained verified pass@1 = 0/2
on the held-out tasks court-form-filling and offer-letter-generator.

## Interpretation
Under this small budget and the selected PI Agent + gpt-4o-mini setup,
hyperparameter search increased experimentation cost but did not yield a
verified task success. This is a valid negative result. It also shows why
harnesses must parse official verifier outcomes rather than relying only on a
process exit code.

## Limitation
The validation set has two tasks and the held-out set has two tasks, so the
result is exploratory rather than a broad benchmark claim.
