#!/bin/bash

# python3 get_average_time.py /home/jim/paramils2.3.8-source/example_minisat_hack/commands_new.json minisat_hack
# python3 get_average_time.py /home/jim/paramils2.3.8-source/example_minisat/commands_new.json minisat

# python3 get_average_time.py /home/jim/paramils2.3.8-source/example_lpg/commands_new.json lpg

# python3 get_average_time.py /home/jim/paramils2.3.8-source/example_sat4j/commands_new.json sat4j

# python3 get_average_time.py /home/jim/paramils2.3.8-source/example_scipy/commands_new2.json scipy

# python3 get_average_time.py /home/jim/paramils2.3.8-source/example_weka/commands_new.json weka

# python3 get_average_time.py /home/jim/paramils2.3.8-source/example_zlib/commands_new.json zlib

# ./run_all_zlib.sh
# ./run_all_scipy.sh

python3 get_average_time.py /home/jim/paramils2.3.8-source/example_scipy/commands_new.json scipy_new
python3 get_average_time.py /home/jim/paramils2.3.8-source/example_zlib/commands_new.json zlib_new