# Results provenance

Only official-verifier evidence is included in this package.

- `verified_analysis/method_comparison_verified.csv`: corrected validation Pass@1 and observed API cost for the four methods.
- `verified_analysis/heldout_test_results_verified.csv`: corrected held-out outcomes for the frozen configuration.
- `verified_analysis/official_verifier_audit.json`: audit of 23 archived runs, showing the original wrapper-based score versus internal official-verifier score.
- `verified_analysis/failure_mode_analysis/`: saved failure-event extraction, category summary, chart, and manual audit checklist.

Raw run folders are deliberately not included: they are bulky and carry the original wrapper-based success metadata. The audit file preserves the run-level corrected scoring needed for review.
