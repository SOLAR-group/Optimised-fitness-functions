
# Experimental Results for LLM-Assisted Genetic Programming

This repository contains the results and configuration files for all experiments conducted using LLM-assisted genetic programming. Results are located in the `results_gp_llm` directory.

## Overview

The `results_gp_llm` folder includes:
- **Scenario files**: Each scenario file provides the configuration necessary to replicate individual experiments.
- **Post-processing scripts**: These scripts are used to analyze and summarize experiment data, as detailed below.
  
> **Note**: Some input data files (such as those used for zlib compression experiments) are not included due to size constraints and could not be uploaded to GitHub.

## Environment Setup

To use the LLM-assisted components, environment variables must be set for API access, depending on the LLM service you choose.

For OpenAI models:
```bash
export OPENAI_API_KEY="your-openai-api-key"
```

The experiments currently use the GPT-4 mini model.

### Configuration for LLM-Assisted Crossover

In the provided scenario files, you will find configurations for the LLM-assisted crossover algorithm. Key settings include:
- `algorithm = GeneticProgrammingLLM` 
- For documentation references in API calls:
  ```python
  llm_documentation_path = /path/to/documentation
  ```

## Post-Processing Data

After running experiments, several post-processing steps were applied to analyze the data, with all scripts available in the `results_gp_llm` folder.

1. **Combine Results**: All results were merged into a single file:
   ```plaintext
   total_results.json
   ```
   
2. **Clean Data**: We cleaned the combined results using the `clean_json.py` script:
   ```plaintext
   cleaned_total_results.json
   ```
   
3. **Initial Analysis**: We extracted initial metrics like average optimal fitness per crossover using:
   ```plaintext
   initial_postprocess.py
   ```

4. **Ranking and Variant Analysis**: 
   - Average rank of each crossover method was calculated with:
     ```plaintext
     average_rank.py
     ```
   - Average variant count for each crossover method to reach critical performance milestones was determined with:
     ```plaintext
     average_indexes.py
     ```

---

This README provides the necessary instructions to set up, run, and analyze LLM-assisted genetic programming experiments. For any additional questions, refer to the documentation or reach out for support.