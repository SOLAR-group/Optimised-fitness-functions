import json
import re
import sys
import os
from collections import defaultdict

EXPECTED_NAMES = [
    "time", "cycles", "cache_references", "L1",
    "perf_time", "energy", "weights", "branches"
]
EXPECTED_COUNT = 3  # how many inputs should exist per name

def clean_key_name(key):
    # Special case: preserve L1
    if re.match(r"^[\d\-]*L1$", key):
        return "L1"
    # Remove all leading digits and dashes (e.g. "1-time", "-time", "--time" → "time")
    return re.sub(r"^[\d\-]+", "", key)


def main():
    if len(sys.argv) < 2:
        print("Usage: python merge_json.py <input_json_path>")
        return

    input_path = sys.argv[1]

    if not os.path.isfile(input_path):
        print(f"Error: File '{input_path}' not found.")
        return

    with open(input_path) as f:
        data = json.load(f)

    merged_output = defaultdict(list)

    for key, value in data.items():
        clean_key = clean_key_name(key)

        # Skip if clean_key is empty
        if not clean_key:
            continue

        entry = {
            "run_directory": value["run_directory"],
            "command": value["command"]
        }

        merged_output[clean_key].append(entry)

    # Write merged output
    with open(input_path, "w") as f:
        json.dump(merged_output, f, indent=4)

    print(f"\n✅ Original file overwritten with merged data: {input_path}\n")

    # print(f"\n✅ Merged output written to: {output_path}\n")

    # Report missing entries for expected names
    print("🔎 Missing inputs per expected name (expecting 3 each):\n")
    for name in EXPECTED_NAMES:
        count = len(merged_output.get(name, []))
        missing = EXPECTED_COUNT - count
        if missing > 0:
            print(f"  - {name}: {missing} missing")
        else:
            print(f"  - {name}: ✅ complete")

if __name__ == "__main__":
    main()
