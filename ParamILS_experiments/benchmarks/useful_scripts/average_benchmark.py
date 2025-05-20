import json
import sys
from pathlib import Path
from statistics import mean

def load_json_files(directory):
    return [f for f in Path(directory).glob("*.json") if f.is_file()]

def rank_metrics(metrics_dict):
    sorted_items = sorted(metrics_dict.items(), key=lambda x: x[1]["average_median"])
    return {name: rank + 1 for rank, (name, _) in enumerate(sorted_items)}

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_metrics.py <directory>")
        return

    directory = Path(sys.argv[1])
    if not directory.is_dir():
        print(f"Not a directory: {directory}")
        return

    all_files = load_json_files(directory)
    if not all_files:
        print("No JSON files found.")
        return

    aggregated_medians = {}
    aggregated_ranks = {}

    for file_path in all_files:
        with open(file_path) as f:
            data = json.load(f)

        metric_ranks = rank_metrics(data)

        for metric, values in data.items():
            avg_median = values["average_median"]
            rank = metric_ranks[metric]

            aggregated_medians.setdefault(metric, []).append(avg_median)
            aggregated_ranks.setdefault(metric, []).append(rank)

    summary = {}
    for metric in aggregated_medians:
        summary[metric] = {
            "average_of_average_medians": round(mean(aggregated_medians[metric]), 3),
            "average_rank": round(mean(aggregated_ranks[metric]), 3)
        }

    print("\n📊 Summary Across All Files:")
    for metric, stats in sorted(summary.items(), key=lambda x: x[1]["average_of_average_medians"]):
        print(f"{metric}: median={stats['average_of_average_medians']} | rank={stats['average_rank']}")

if __name__ == "__main__":
    main()
