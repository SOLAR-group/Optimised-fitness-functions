#!/bin/bash



ruby param_ils_2_3_run.rb -scenariofile example_minisat/scenario-minisat-L1.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_minisat/help_minisat4_L1.txt


ruby param_ils_2_3_run.rb -scenariofile example_minisat/scenario-minisat-weights.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_minisat/help_minisat4_weights.txt


ruby param_ils_2_3_run.rb -scenariofile example_minisat/scenario-minisat-L1.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_minisat/help5_minisat_L1.txt


ruby param_ils_2_3_run.rb -scenariofile example_minisat/scenario-minisat-weights.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_minisat/help5_minisat_weights.txt


ruby param_ils_2_3_run.rb -scenariofile example_minisat/scenario-minisat-L1.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_minisat/help_minisat_L1.txt


ruby param_ils_2_3_run.rb -scenariofile example_minisat/scenario-minisat-weights.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_minisat/help_minisat_weights.txt

