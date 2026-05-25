import json
import glob
import os
from datetime import datetime


BONUS_DIRS = {
    "claude-sonnet":     "Claude Sonnet 4.5",
    "llama-8b":          "Llama 3.1 8B",
    "deepseek-v3":       "DeepSeek V3.1",
    "gpt-4o-mini":       "GPT-4o-mini",
}

BASELINE_PATH = "results/comparison_baseline.json"
IMPROVED_PATH = "results/comparison_improved.json"


def latest_comparison(subdir):
    files = sorted(glob.glob(f"results/{subdir}/comparison_*.json"))
    return files[-1] if files else None


def main():
    rows = []
    if os.path.exists(BASELINE_PATH):
        with open(BASELINE_PATH) as f:
            rows.append(("Baseline (placeholder prompt)", json.load(f)))
    if os.path.exists(IMPROVED_PATH):
        with open(IMPROVED_PATH) as f:
            rows.append(("Gemini 2.5 Flash (improved prompts)", json.load(f)))

    for subdir, label in BONUS_DIRS.items():
        path = latest_comparison(subdir)
        if not path:
            print(f"[skip] no results in results/{subdir}/")
            continue
        with open(path) as f:
            rows.append((label, json.load(f)))

    print()
    print("=" * 118)
    print(f"  {'Model':<42}  {'A succ':>8} {'A F1':>7} {'A tok':>8} {'A lat':>7}  |  "
          f"{'B succ':>8} {'B F1':>7} {'B tok':>8} {'B lat':>7}  Winner")
    print("=" * 118)
    for label, d in rows:
        a, b = d["config_a"], d["config_b"]
        if a["success_rate"] > b["success_rate"]:
            winner = "A"
        elif b["success_rate"] > a["success_rate"]:
            winner = "B"
        else:
            winner = "Tie"
        print(f"  {label:<42}  "
              f"{a['success_rate']:>8.2f} {a['avg_f1']:>7.2f} {a['avg_tokens']:>8.0f} {a['avg_latency']:>6.2f}s  |  "
              f"{b['success_rate']:>8.2f} {b['avg_f1']:>7.2f} {b['avg_tokens']:>8.0f} {b['avg_latency']:>6.2f}s   {winner}")

    print()
    print("PER-CATEGORY SUCCESS RATES (A / B)")
    print("=" * 118)
    cats = ["simple_lookup", "tag_search", "temporal", "content_search", "multi_faceted", "graph_based"]
    print(f"  {'Model':<42}  " + "  ".join(f"{c:>13}" for c in cats))
    print("-" * 118)
    for label, d in rows:
        cells = []
        for c in cats:
            sa = d["config_a"]["by_category"].get(c, {}).get("success_rate", 0)
            sb = d["config_b"]["by_category"].get(c, {}).get("success_rate", 0)
            cells.append(f"{sa:.2f}/{sb:.2f}")
        print(f"  {label:<42}  " + "  ".join(f"{x:>13}" for x in cells))

    summary = {
        "generated_at": datetime.now().isoformat(),
        "runs": [{"label": label, "data": data} for label, data in rows],
    }
    with open("results/final_summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print("\nSaved results/final_summary.json")


if __name__ == "__main__":
    main()
