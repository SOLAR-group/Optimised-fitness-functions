#!/bin/bash


sudo python3.11 run_examples.py triangle-c scenario_slow "" "./run_triangle" "make run_triangle" triangle.c "" local_search
sudo python3.11 run_examples.py triangle-cpp scenario_slow "" "./build/run_triangle" "bash compile.sh" triangle.cpp.xml "" local_search
sudo python3.11 run_examples.py triangle-py scenario_slow "" "python3.11 run_triangle.py" "" triangle.py "" local_search
sudo python3.11 run_examples.py minisat "" scenario_runtime_config1 "bash run_fixed.sh" "" minisat_simplified.params minisat_simplified.params local_search
sudo python3.11 run_examples.py minisat "" scenario_runtime_config3 "bash run_fixed.sh" "bash compile.sh" core/Solver.cc "" local_search
sudo python3.11 run_examples.py sat4j "" scenario_runtime_config1 "bash run_fixed.sh" "" test.params test.params local_search
sudo python3.11 run_examples.py sat4j "" scenario_runtime_config3 "bash run_fixed.sh" "ant sat" org.sat4j.core/src/main/java/org/sat4j/minisat/core/Solver.java "" genetic_programming
sudo python3.11 run_examples.py minisat_hack "" scenario_runtime_config1 "bash run_fixed.sh" "" minisat_advanced.params minisat_advanced.params genetic_programming
sudo python3.11 run_examples.py minisat_hack "" scenario_runtime_config3 "bash run_fixed.sh" "./build.sh" sources/core/Solver.cc "" genetic_programming
sudo python3.11 run_examples.py weka "" scenario_runtime_config1 "bash run_fixed.sh" "" weka.params weka.params genetic_programming
sudo python3.11 run_examples.py weka "" scenario_runtime_config3 "bash run_fixed.sh" "ant compile" src/main/java/weka/classifiers/trees/RandomForest.java weka.params "" genetic_programming
sudo python3.11 run_examples.py zlib "" scenario_runtime_config1 "bash run_fixed.sh" "" zlib.params zlib.params genetic_programming

sudo python3.11 run_examples.py lpg "" scenario_runtime_config1 "bash run_fixed.sh" "" lpg.params lpg.params local_search
sudo python3.11 run_examples.py scipy "" scenario_runtime_config1 "bash run_fixed.sh" "" scipy.params scipy.params genetic_programming