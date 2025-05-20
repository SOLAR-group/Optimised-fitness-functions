import json
import statistics

def process_items(input_file, output_file):
    # Load the JSON data from the input file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Process each item in the JSON
    processed_items = []
    for item in data:
        fitness_values = item.get("fitness_values", [])
        
        # Calculate the required metrics
        fitness_count = len(fitness_values)
        fitness_avg = statistics.mean(fitness_values) if fitness_values else 0
        fitness_min = min(fitness_values) if fitness_values else 0
        
        # Store the processed data for this item
        processed_item = {
            "benchmark": item.get("benchmark"),
            "fitness_values": fitness_values,
            "crossover": item.get("crossover"),
            "fitness_count": fitness_count,
            "fitness_avg": fitness_avg,
            "fitness_min": fitness_min
        }
        processed_items.append(processed_item)
    
    # Save the processed data to the output file
    with open(output_file, 'w') as file:
        json.dump(processed_items, file, indent=4)
    print(f"Processed data saved to {output_file}")

# Replace 'input.json' with the path to your input JSON file
# Replace 'output.json' with the desired path for the output JSON file
process_items('/home/jim/magpie_llm_results/aggregated_performance_data.json', 'cleaned.json')
