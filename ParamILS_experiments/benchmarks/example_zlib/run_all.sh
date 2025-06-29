#!/bin/bash

ruby param_ils_2_3_run.rb -scenariofile example_zlib/scenario-zlib.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_zlib/help_zlib_time.txt

ruby param_ils_2_3_run.rb -scenariofile example_zlib/scenario-zlib-branches.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_zlib/help_zlib_branches.txt

ruby param_ils_2_3_run.rb -scenariofile example_zlib/scenario-zlib-cache-references.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_zlib/help_zlib_cache-references.txt

ruby param_ils_2_3_run.rb -scenariofile example_zlib/scenario-zlib-cycles.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_zlib/help_zlib_cycles.txt

ruby param_ils_2_3_run.rb -scenariofile example_zlib/scenario-zlib-L1.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_zlib/help_zlib_L1.txt

ruby param_ils_2_3_run.rb -scenariofile example_zlib/scenario-zlib-perf-time.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_zlib/help_zlib_perf-time.txt

ruby param_ils_2_3_run.rb -scenariofile example_zlib/scenario-zlib-weights.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_zlib/help_zlib_weights.txt

ruby param_ils_2_3_run.rb -scenariofile example_zlib/scenario-zlib-energy.txt  -numRun 1  -maxEvals 100000 -maxIts 10000 -approach basic -validN 30 > example_zlib/help_zlib_energy.txt