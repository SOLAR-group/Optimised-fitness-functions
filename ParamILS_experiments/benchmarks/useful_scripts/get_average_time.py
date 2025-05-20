import os
import json
import sys
import time
import subprocess
import statistics
from pathlib import Path

TIMEOUT = 40  # seconds
MINIMUM_VALID_TIME = 0.5
N_RUNS = 21

def run_command(command, cwd):
    try:
        start = time.perf_counter()
        subprocess.run(command, shell=True, cwd=cwd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=TIMEOUT)
        elapsed = time.perf_counter() - start
        if elapsed < MINIMUM_VALID_TIME:
            return TIMEOUT  # too fast, consider invalid
        return elapsed
    except subprocess.TimeoutExpired:
        return TIMEOUT

def main():
    if len(sys.argv) < 3:
        print("Usage: python benchmark_json.py <input_json> <failed_prefix>")
        return

    input_path = Path(sys.argv[1])
    failed_prefix = sys.argv[2]

    if not input_path.is_file():
        print(f"File not found: {input_path}")
        return

    with open(input_path) as f:
        data = json.load(f)

    results = {}
    all_failed = {}

    for category_name, entries in data.items():
        category_results = []
        failed_cases = []

        print(f"\n⏱ Benchmarking category: {category_name}")

        for i, entry in enumerate(entries):
            run_dir = entry["run_directory"]
            command = entry["command"]

            print(f"  ▶ Running pair {i + 1} in {run_dir}...")
            # time.sleep(10)  # Sleep for 60 seconds before running the command
            times = []
            for attempt in range(N_RUNS):
                t = run_command(command, run_dir)
                print(f"     Attempt {attempt+1}: {t:.3f}s")
                times.append(t)

                if t == TIMEOUT:
                    print("     ⛔ Timeout — skipping remaining runs for this pair.")
                    failed_cases.append(entry)
                    times = [TIMEOUT]
                    break

            median = statistics.median(times)
            category_results.append(median)
            print(f"     → Median: {median:.3f}s")

        avg_median = round(statistics.mean(category_results), 3) if category_results else None

        results[category_name] = {
            "medians": [round(t, 3) for t in category_results],
            "average_median": avg_median
        }

        if failed_cases:
            failed_path = input_path.parent / f"failed_{failed_prefix}_{category_name}.json"
            with open(failed_path, "w") as f:
                json.dump(failed_cases, f, indent=4)
            print(f"❌ Saved failed cases for {category_name} to {failed_path}")

    results_path = input_path.parent / "results.json"
    with open(results_path, "w") as f:
        json.dump(results, f, indent=4)

    print(f"\n✅ Benchmark results saved to: {results_path}")

if __name__ == "__main__":
    main()
