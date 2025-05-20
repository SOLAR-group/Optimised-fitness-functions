import json
from collections import defaultdict

def process_data(input_file, output_file):
    # Load the JSON data from the input file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Initialize dictionaries to store sums and counts for each crossover type
    crossover_data = defaultdict(lambda: {
        "total_fitness_avg": 0,
        "total_fitness_min": 0,
        "total_fitness_count": 0,
        "total_fitness_count_code": 0,
        "count": 0,
        "count_code": 0
    })
    
    # Process each item and accumulate values based on crossover type
    for item in data:
        crossover = item["crossover"]
        crossover_data[crossover]["total_fitness_avg"] += item["fitness_avg"]
        crossover_data[crossover]["total_fitness_min"] += item["fitness_min"]
        crossover_data[crossover]["total_fitness_count"] += item["fitness_count"]
        crossover_data[crossover]["count"] += 1
        
        # Check if 'code' is in the benchmark name and accumulate separately
        if "code" in item["benchmark"]:
            crossover_data[crossover]["total_fitness_count_code"] += item["fitness_count"]
            crossover_data[crossover]["count_code"] += 1
    
    # Calculate averages for each crossover type
    result = {}
    for crossover, values in crossover_data.items():
        result[crossover] = {
            "average_fitness_avg": values["total_fitness_avg"] / values["count"],
            "average_fitness_min": values["total_fitness_min"] / values["count"],
            "average_fitness_count": values["total_fitness_count"] / values["count"],
            "average_fitness_count_code": (
                values["total_fitness_count_code"] / values["count_code"]
                if values["count_code"] > 0 else 0
            )
        }
    
    # Save the results to the output file
    with open(output_file, 'w') as file:
        json.dump(result, file, indent=4)
    print(f"Processed data saved to {output_file}")

# Replace 'input.json' and 'output.json' with the paths to your input and output files
process_data('/home/jim/magpie_llm_results/cleaned.json', 'initial_res.json')
