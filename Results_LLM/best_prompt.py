import json
import sys

def categorize_prompt(name):
    if "simple_with_doc" in name:
        return "simple_with_doc"
    elif "with_hints_and_doc" in name:
        return "with_hints_and_doc"
    elif "with_hints" in name:
        return "with_hints"
    elif "with_cot_and_doc" in name:
        return "with_cot_and_doc"
    elif "with_cot" in name:
        return "with_cot"
    elif "simple" in name:
        return "simple"
    return None

def process_json_file(input_path, output_path):
    with open(input_path, 'r') as file:
        try:
            input_data = json.load(file)
            total_data = input_data.get("total_data", {})
        except json.JSONDecodeError:
            print("Invalid JSON file.")
            return

    prompt_times = {
        "simple": [],
        "with_hints": [],
        "with_hints_and_doc": [],
        "with_cot_and_doc": [],
        "with_cot": [],
        "simple_with_doc": []
    }

    timeout_value = 40000
    for key, value in total_data.items():
        time = value.get("time")
        prompt_type = categorize_prompt(key)

        if prompt_type:
            if not isinstance(time, (int, float)) or time < 1000:
                time = timeout_value
            prompt_times[prompt_type].append(time)

    avg_times = {
        ptype: (sum(times) / len(times) if times else None)
        for ptype, times in prompt_times.items()
    }
    median_times = {
        ptype: (sorted(times)[len(times) // 2] if times else None)
        for ptype, times in prompt_times.items()
    }

    result = {
        "average_times": avg_times,
        "median_times": median_times,
        "all_times": prompt_times
    }

    with open(output_path, 'w') as file:
        json.dump(result, file, indent=4)

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    process_json_file(input_path, output_path)
