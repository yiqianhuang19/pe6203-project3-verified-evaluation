# PE6203 Project 3 — Verified Harness Hyperparameter Optimization

This is the clean, corrected submission package for the Project 3 experiment. It contains only results scored from the **internal outcomes of the official SkillsBench verifier tests**. It deliberately excludes the earlier false-success interpretation that treated the verifier wrapper process exit code as task success.

## What was evaluated

- **Harness / agent:** PI Agent 0.73.1 in Docker on WSL2.
- **Model endpoint:** OpenRouter, using `openai/gpt-4o-mini`.
- **Benchmark:** SkillsBench v1.1.
- **Formal validation tasks:** `paper-anonymizer` and `edit-pdf`.
- **Held-out tasks:** `offer-letter-generator` and `court-form-filling`.
- **Pilot only (excluded from formal metrics):** `dialogue-parser`.

Four search methods were compared: Default, Random Search, Bayesian Optimization, and a custom two-stage cost-aware search. Their observed cumulative API costs were respectively $0.062066, $0.225147, $0.242667, and $0.320940.

## Corrected result

All four methods received verified validation Pass@1 = **0.0**. The frozen configuration `final_c0_off_default` received verified held-out Pass@1 = **0/2**. This is a valid negative experimental result, not a claim that the tasks succeeded.

The audit found that all 23 archived runs had an agent/verifier-wrapper exit status that the original harness read as success, while the official verifier's internal tests failed. Therefore, wrapper process status alone is not a valid evaluation signal for this benchmark.

## Failure analysis

The package includes 176 verifier failure-evidence rows from 23 logs. This is evidence-level frequency, not 176 independent model runs.

| Preliminary category | Evidence rows |
| --- | ---: |
| Content missing / requirement not met | 154 |
| File format / structure | 22 |

## Contents

- `notebooks/project3_verified_analysis.ipynb` — clean, read-only notebook for reviewing the corrected evidence; it does not call an API.
- `configs/official_verifier_scoring_protocol.json` — the corrected scoring rule.
- `results/verified_analysis/` — official audit, method and held-out CSVs, corrected figure, and failure-mode evidence.
- `scripts/verify_verified_results.py` — local consistency check; costs $0.
- `scripts/rebuild_verified_analysis.py` — rebuilds the corrected chart from CSV files; costs $0.

## Reproduce the packaged analysis

```bash
pip install -r requirements.txt
python scripts/verify_verified_results.py
python scripts/rebuild_verified_analysis.py
```

The scripts reproduce the analysis of the stored evidence. They do not rerun paid model calls or download SkillsBench.

## Limitations

The formal validation and held-out sets each contain two tasks, so conclusions are exploratory rather than broad estimates of model capability. Failure categories are rule-based preliminary classifications that should be interpreted alongside the saved verifier logs and audit table.
