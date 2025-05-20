import json
from collections import defaultdict

def calculate_penalized_average_indices(data, penalty_value):
    # Initialize dictionaries to hold sums and counts for each crossover
    crossover_indices = defaultdict(lambda: {"25_total": 0, "50_total": 0, "75_total": 0, "100_total": 0, "count": 0})
    
    for item in data:
        crossover = item["crossover"]
        indices = item["indices"]
        
        # Add penalized values (penalty_value) for nulls, actual indices otherwise
        crossover_indices[crossover]["25_total"] += indices["25_index"] if indices["25_index"] is not None else penalty_value
        crossover_indices[crossover]["50_total"] += indices["50_index"] if indices["50_index"] is not None else penalty_value
        crossover_indices[crossover]["75_total"] += indices["75_index"] if indices["75_index"] is not None else penalty_value
        crossover_indices[crossover]["100_total"] += indices["100_index"] if indices["100_index"] is not None else penalty_value
        crossover_indices[crossover]["count"] += 1

    # Calculate the penalized average indices for each crossover
    average_indices = {}
    for crossover, values in crossover_indices.items():
        average_indices[crossover] = {
            "average_25_index": values["25_total"] / values["count"],
            "average_50_index": values["50_total"] / values["count"],
            "average_75_index": values["75_total"] / values["count"],
            "average_100_index": values["100_total"] / values["count"]
        }
    
    return average_indices

def main(input_file, output_file, penalty_value):
    # Load the JSON data from the input file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Calculate the penalized average indices for each crossover
    average_indices = calculate_penalized_average_indices(data, penalty_value)
    
    # Save the results to the output file
    with open(output_file, 'w') as file:
        json.dump(average_indices, file, indent=4)
    
    print(f"Penalized average indices saved to {output_file}")

# Usage: Adjust the penalty_value as appropriate
penalty_value = 250  # Choose a high penalty value, e.g., 500 or the length of fitness_values if known
main('/home/jim/magpie_llm_results/first_indexes.json', 'average_first_indexes.json', penalty_value)
