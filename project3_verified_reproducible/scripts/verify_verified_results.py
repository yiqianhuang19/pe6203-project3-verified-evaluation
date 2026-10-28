"""Validate the packaged corrected Project 3 evidence without API calls."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "results" / "verified_analysis"


def read_csv(name: str) -> list[dict[str, str]]:
    with (ANALYSIS / name).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    methods = read_csv("method_comparison_verified.csv")
    heldout = read_csv("heldout_test_results_verified.csv")
    failures = read_csv("failure_mode_analysis/failure_mode_summary.csv")
    audit = json.loads((ANALYSIS / "official_verifier_audit.json").read_text(encoding="utf-8"))

    assert len(methods) == 4, "Expected four compared methods."
    assert all(float(row["verified_validation_pass_at_1"]) == 0.0 for row in methods)
    assert len(heldout) == 2, "Expected two held-out tasks."
    assert all(float(row["official_verifier_pass_at_1"]) == 0.0 for row in heldout)
    assert len(audit) == 23, "Expected 23 audited archived runs."
    assert all(row["old_runner_score"] == 1 for row in audit)
    assert all(row["official_verifier_score"] == 0 for row in audit)
    assert sum(int(row["failure_evidence_rows"]) for row in failures) == 176

    print("Verified package checks passed.")
    print("Methods:", len(methods))
    print("Held-out tasks:", len(heldout))
    print("Audited archived runs:", len(audit))
    print("Failure-evidence rows:", sum(int(row["failure_evidence_rows"]) for row in failures))


if __name__ == "__main__":
    main()
