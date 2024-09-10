#!/bin/bash
###############################################################################
# This script is to tune the ACOTSP software.
#
# PARAMETERS:
# $1 is the ID of the candidate to be evaluated
# $2 is the instance ID
# $3 is the seed
# $4 is the instance name
# The rest ($* after `shift 4') are parameters for running ACOTSP
#
# RETURN VALUE:
# This script should print a single numerical value (the value to be minimized).
###############################################################################
error() {
    echo "`TZ=UTC date`: $0: error: $@" >&2
    exit 1
}


# Path to the ACOTSP executable (this path is relative to the execution directory `execDir` specified in the scenario).
# EXE="~/bin/acotsp"
EXE="./run_fixed.sh"

# Fixed parameters that should be always passed to ACOTSP.
# The time to be used is always 10 seconds, and we want only one run:
FIXED_PARAMS=""

CONFIG_ID="$1"
INSTANCE_ID="$2"
SEED="$3"
INSTANCE="$4"
# All other parameters are the candidate parameters to be passed to program
shift 4 || error "Not enough parameters"
CONFIG_PARAMS=$*



read -r -a params_array <<< "$CONFIG_PARAMS"

# Initialize an empty string to hold the formatted command-line parameters
formatted_params=""

# Loop through each parameter in the array
for param in "${params_array[@]}"; do
    #if the param does not start with - then it is a value and should be ignored
    if [[ ! "$param" == -* ]]; then
        continue
    fi
    if [[ "$param" == *'=True' ]]; then
        # Strip out '=True' and add the flag name only
        flag=${param%=True}
        formatted_params+="$flag "
    elif [[ "$param" == *'=False' ]]; then
        # If 'False', skip adding this parameter
        continue
    else
        # Add non-boolean parameters as is
        formatted_params+="$param "
    fi
done

# Trim trailing whitespace from formatted_params
CONFIG_PARAMS=$(echo "$formatted_params" | xargs)



STDOUT=c${CONFIG_ID}-${INSTANCE_ID}-${SEED}.stdout
STDERR=c${CONFIG_ID}-${INSTANCE_ID}-${SEED}.stderr

if [ ! -x "${EXE}" ]; then
    error "${EXE}: not found or not executable (pwd: $(pwd))"
fi
# echo $INSTANCE
# echo $CONFIG_PARAMS
# Now we can call ACOTSP by building a command line with all parameters for it
start_time=$(date +%s.%N)

# Execute the command 20 times
for i in {1..20}
do
    $EXE ${CONFIG_PARAMS} 1> $STDOUT 2> $STDERR
done

# End the performance measurement
end_time=$(date +%s.%N)

# Calculate total time and mean time
total_time=$(echo "$end_time - $start_time" | bc)
mean_time=$(echo "$total_time / 20" | bc -l)

# Output the total and mean time
echo "Total Execution Time: $total_time seconds"
echo "Average Execution Time per Command: $mean_time seconds"

# The output of the candidate $CONFIG_ID should be written in the file 
# c${CONFIG_ID}.stdout (see target runner for ACOTSP).
# Does this file exist?
if [ ! -s "${STDOUT}" ]; then
    # In this case, the file does not exist. Let's exit with a value 
    # different from 0. In this case irace will stop with an error.
    error "${STDOUT}: No such file or directory"
fi

# Ok, the file exist. It contains the whole output written by ACOTSP.
# This script should return a single numerical value, the best objective 
# value found by this run of ACOTSP. The following line is to extract
# this value from the file containing ACOTSP output.
# COST=$(cat ${STDOUT} | grep -o -E 'Best [-+0-9.e]+' | cut -d ' ' -f2)
# if ! [[ "$COST" =~ ^[-+0-9.e]+$ ]] ; then
#     error "${STDOUT}: Output is not a number"
# fi

# Assuming the output is stored in a variable or file $STDOUT
# Extract the number of cycles


# rm -f best.* stat.* cmp.*
exit 0

# data/uf50-01.cnf
# -luby -gc-frac=0.2 -rinc=2.0 -var-decay=0.95 -cla-decay=0.999 -rnd-freq=0.0 -rnd-seed=91648253 -phase-saving=2 -ccmin-mode=2 -rfirst=100 -pre -verb=1 -elim -simp-gc-frac=0.5 -sub-lim=1000 -cl-lim=20 -grow=0