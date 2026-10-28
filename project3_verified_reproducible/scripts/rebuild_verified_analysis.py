"""Rebuild the corrected official-verifier analysis figure without API calls."""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "verified_analysis"
OUT = ROOT / "results" / "rebuilt_verified_analysis"


def read_csv(name: str) -> list[dict[str, str]]:
    with (SOURCE / name).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    methods = read_csv("method_comparison_verified.csv")
    heldout = read_csv("heldout_test_results_verified.csv")

    names = [row["method"] for row in methods]
    costs = [float(row["observed_cumulative_cost_usd"]) for row in methods]
    validation = [float(row["verified_validation_pass_at_1"]) for row in methods]
    tasks = [row["task"] for row in heldout]
    test_scores = [float(row["official_verifier_pass_at_1"]) for row in heldout]

    figure, axes = plt.subplots(1, 3, figsize=(16, 5))
    figure.suptitle("Project 3: Corrected Results Using Official Verifier Evidence")

    bars = axes[0].bar(names, costs, color=["#8ecae6", "#219ebc", "#ffb703", "#fb8500"])
    axes[0].set_title("Observed Cumulative API Cost")
    axes[0].set_ylabel("USD")
    axes[0].tick_params(axis="x", rotation=25)
    for bar, value in zip(bars, costs):
        axes[0].text(bar.get_x() + bar.get_width() / 2, value, f"${value:.3f}", ha="center", va="bottom")

    bars = axes[1].bar(names, validation, color="#e76f51")
    axes[1].set_title("Verified Validation Pass@1")
    axes[1].set_ylabel("Pass@1")
    axes[1].set_ylim(0, 1.1)
    axes[1].tick_params(axis="x", rotation=25)
    for bar, value in zip(bars, validation):
        axes[1].text(bar.get_x() + bar.get_width() / 2, value + 0.03, f"{value:.1f}", ha="center")

    bars = axes[2].bar(tasks, test_scores, color="#2a9d8f")
    axes[2].set_title("Verified Held-out Test Results")
    axes[2].set_ylabel("Pass@1")
    axes[2].set_ylim(0, 1.1)
    axes[2].tick_params(axis="x", rotation=25)
    for bar, value in zip(bars, test_scores):
        axes[2].text(bar.get_x() + bar.get_width() / 2, value + 0.03, f"{value:.0f}", ha="center")

    figure.tight_layout()
    target = OUT / "corrected_experiment_summary.png"
    figure.savefig(target, dpi=200, bbox_inches="tight")
    print(f"Wrote {target}")


if __name__ == "__main__":
    main()
