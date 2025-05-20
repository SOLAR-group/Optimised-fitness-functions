import json

# Initial minimum times for each benchmark
initial_times = {
    "minisat_code": 11.4,
    "minisat_params": 11.3,
    "minisat_hack_code": 4.02,
    "minisat_hack_params": 4.01,
    "sat4j_code": 6.33,
    "sat4j_params": 7.4,
    "weka_code": 7.6,
    "weka_params": 7.6,
    "lpg_params": 9.49,
    "scipy_params": 9.38,
    "zlib_params": 6.3
}

def calculate_improvement_thresholds(initial_time, best_fitness):
    """Calculate 25%, 50%, 75%, and 100% improvement thresholds."""
    best_improvement = initial_time - best_fitness
    return {
        "best_fitness": best_fitness,
        "best_improvement": best_improvement,
        "25_improvement": initial_time - 0.25 * best_improvement,
        "50_improvement": initial_time - 0.50 * best_improvement,
        "75_improvement": initial_time - 0.75 * best_improvement,
        "100_improvement": initial_time - 1 * best_improvement
    }

def find_first_index_below_threshold(fitness_values, threshold):
    """Find the first index where fitness value is below the threshold."""
    for index, value in enumerate(fitness_values):
        if value <=threshold:
            return index
    return None

def process_benchmarks(input_file, output_file):
    # Load the JSON data from the input file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Step 1: Calculate best fitness_min for each benchmark
    best_fitness_per_benchmark = {}
    for item in data:
        benchmark = item["benchmark"]
        fitness_min = item["fitness_min"]
        if benchmark not in best_fitness_per_benchmark:
            best_fitness_per_benchmark[benchmark] = fitness_min
        else:
            best_fitness_per_benchmark[benchmark] = min(best_fitness_per_benchmark[benchmark], fitness_min)
    
    # Step 2: Calculate improvement thresholds for each benchmark
    improvement_thresholds = {}
    for benchmark, initial_time in initial_times.items():
        best_fitness = best_fitness_per_benchmark.get(benchmark, initial_time)
        improvement_thresholds[benchmark] = calculate_improvement_thresholds(initial_time, best_fitness)
    
    # Step 3: Process each item and find the first index for each improvement level
    results = []
    for item in data:
        benchmark = item["benchmark"]
        fitness_values = item["fitness_values"]
        thresholds = improvement_thresholds[benchmark]

        # Find first index below each improvement threshold
        improvement_indices = {
            "25_index": find_first_index_below_threshold(fitness_values, thresholds["25_improvement"]),
            "50_index": find_first_index_below_threshold(fitness_values, thresholds["50_improvement"]),
            "75_index": find_first_index_below_threshold(fitness_values, thresholds["75_improvement"]),
            "100_index": find_first_index_below_threshold(fitness_values, thresholds["100_improvement"])
        }
        
        # Create a result dictionary for this item with calculated values
        result_item = {
            "benchmark": benchmark,
            "crossover": item["crossover"],
            "fitness_min": item["fitness_min"],
            "improvements": thresholds,
            "indices": improvement_indices
        }
        results.append(result_item)
    
    # Step 4: Save the results to the output file
    with open(output_file, 'w') as file:
        json.dump(results, file, indent=4)
    
    print(f"Processed data saved to {output_file}")

# Replace 'input.json' and 'output.json' with your file paths
process_benchmarks('/home/jim/magpie_llm_results/cleaned.json', 'first_indexes.json')
