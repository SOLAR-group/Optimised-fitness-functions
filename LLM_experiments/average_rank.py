import json
from collections import defaultdict

def rank_crossovers(input_file, output_file):
    # Load the JSON data from the input file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Step 1: Group items by benchmark
    benchmarks = defaultdict(list)
    for item in data:
        benchmarks[item["benchmark"]].append(item)
    
    # Step 2: Rank crossovers within each benchmark by fitness_min
    crossover_ranks = defaultdict(list)
    for benchmark, items in benchmarks.items():
        # Sort items by fitness_min in ascending order
        ranked_items = sorted(items, key=lambda x: x["fitness_min"])
        
        # Assign ranks (1 for lowest fitness_min, 6 for highest)
        for rank, item in enumerate(ranked_items, start=1):
            crossover = item["crossover"]
            crossover_ranks[crossover].append(rank)
    
    # Step 3: Calculate average rank for each crossover method
    average_ranks = {}
    for crossover, ranks in crossover_ranks.items():
        average_rank = sum(ranks) / len(ranks) if ranks else 0
        average_ranks[crossover] = average_rank
    
    # Step 4: Save the average ranks to the output file
    with open(output_file, 'w') as file:
        json.dump(average_ranks, file, indent=4)
    
    print(f"Average ranks saved to {output_file}")

# Replace 'input.json' and 'output.json' with your file paths
rank_crossovers('/home/jim/magpie_llm_results/cleaned.json', 'average_rank.json')
