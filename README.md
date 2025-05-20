


# Optimised Fitness Functions for runtime improvement , an application on MAGPIE


## Introduction

We are integrating 13 measures and the retry parameter into MAGPIE and performing experiments on 7 benchmarks.
We also performed consistency and correlation to rutnime experiments for the 13 measures + linus time.

Magpie is a tool for automated software improvement.
It implements [MAGPIE](#citation), using the genetic improvement methodology to traverse the search space of different software variants to find improved software.

Magpie provides support for improvement of both functional (automated bug fixing) and non-functional (e.g., execution time) properties of software.  
Two types of language-agnostic source code representations are supported: line-by-line, and XML trees.
For the latter we recommend the [srcML](https://www.srcml.org/) tool with out-of-the-box support for C/C++/C# and Java.  
Finally, Magpie also enables parameter tuning and algorithm configuration, both independently and concurrently of the source code search process.

##
## Requirements

- Unix (Linux/macOS/etc; untested on Windows)
- Python 3.8+


## Try it now!

    git clone https://github.com/bloa/magpie.git
    cd magpie
    python3 magpie local_search --scenario examples/triangle-c/_magpie/scenario_slow.txt


## Documentation

Everything you need to know about Magpie and the new Optimised Fitness Function and retry parameter.

**Results**
- [Results for local search approach for 14 measure,  retry combos on 11 scenarios](./local_search_results/)
- [Results for genetic programming approach for 14 measure, 5 retry combos on 11 scenarios](./genetic_programming_results/)

**Optimised Fitness Functions**

- [Consistency - corellation experiments](./docs/results/initial_experiments.md)
- [Guide to running a new benchmark](./docs/results/running_new_benchmark.md)
- [Guide to create a scenario file](./docs/results/scenario_file_guide.md)
- [Analysis Methodology](./docs/results/analysis_methodology.md)
- [Understanding the Results](./docs/results/understanding_results.md)
- [Test on Irace](./irace/)
**Tutorials**

- [Quick start](./docs/tutorials/quick_start.md) **(start here!)**
- [Search for improved variants](./docs/tutorials/search.md)

**How-to guides**

- [Write a custom fitness function](./docs/howto/custom_fitness_function.md)

**Explanations**

- [Project structure](./docs/explanations/project_structure.md)

**Reference guides**

- [Entry points](./docs/reference/entry_points.md)
- [Fitness functions](./docs/reference/fitness_functions.md)
- [Scenario files](./docs/reference/scenario_file.md)
- [Algorithm configuration model](./docs/params_model.md)


**For ParamILS experiments**
- [Go to this folder](./ParamILS_experiments)


**For LLM based experiments**
- [Go to this folder](./LLM_experiments)

