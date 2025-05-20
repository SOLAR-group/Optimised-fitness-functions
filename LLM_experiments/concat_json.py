import os
import json

def find_performance_data_files(directory):
    """Recursively find all performance_data.json files in the given directory."""
    performance_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file == 'performance_data.json':
                performance_files.append(os.path.join(root, file))
    return performance_files

def aggregate_items_from_files(files):
    """Aggregate all items from a list of performance_data.json files."""
    all_items = []
    for file_path in files:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if "items" in data:
                all_items.extend(data["items"])
    return all_items

def save_aggregated_items(all_items, output_file):
    """Save all aggregated items to a new JSON file."""
    with open(output_file, 'w') as file:
        json.dump(all_items, file, indent=4)

def main(directory, output_file='aggregated_performance_data.json'):
    performance_files = find_performance_data_files(directory)
    all_items = aggregate_items_from_files(performance_files)
    save_aggregated_items(all_items, output_file)
    print(f"Aggregated data saved to {output_file}")

# Replace 'your_directory_path' with the path to the directory you want to search
main('./')
