#!/bin/bash

ruby param_ils_2_3_run.rb -scenariofile example_sat4j/scenario-sat4j.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_sat4j/help_sat4j_time.txt

ruby param_ils_2_3_run.rb -scenariofile example_sat4j/scenario-sat4j-branches.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_sat4j/help_sat4j_branches.txt

ruby param_ils_2_3_run.rb -scenariofile example_sat4j/scenario-sat4j-cache-references.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_sat4j/help_sat4j_cache-references.txt

ruby param_ils_2_3_run.rb -scenariofile example_sat4j/scenario-sat4j-cycles.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_sat4j/help_sat4j_cycles.txt

ruby param_ils_2_3_run.rb -scenariofile example_sat4j/scenario-sat4j-L1.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_sat4j/help_sat4j_L1.txt

ruby param_ils_2_3_run.rb -scenariofile example_sat4j/scenario-sat4j-perf-time.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_sat4j/help_sat4j_perf-time.txt

ruby param_ils_2_3_run.rb -scenariofile example_sat4j/scenario-sat4j-weights.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_sat4j/help_sat4j_weights.txt

ruby param_ils_2_3_run.rb -scenariofile example_sat4j/scenario-sat4j-energy.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_sat4j/help_sat4j_energy.txt