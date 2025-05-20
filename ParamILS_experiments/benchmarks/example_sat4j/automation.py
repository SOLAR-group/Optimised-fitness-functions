import os
import json
import re

BASE_DIR = "."  # <-- change this
RUN_DIRECTORY = "/home/jim/magpie_llm/examples/sat4j/necessary/"
SCRIPT_NAME = "bash run_fixed.sh"

output = {}

for file in os.listdir(BASE_DIR):
    file_path = os.path.join(BASE_DIR, file)
    if os.path.isfile(file_path) and (file.startswith("help5_sat4j_") or file.startswith("help4_sat4j_") or file.startswith("help_sat4j_")):
        key = file.replace("help5_sat4j_", "").replace("help4_sat4j_", "").replace("help_sat4j_", "").replace(".txt", "")
        print(f"Processing {key}...")

        # Find the result file
        


        # Read and parse the parameters
        with open(file_path, 'r') as f:
            contents = f.read()


        match = re.search(r"Final best parameter configuration:\s*(.*)", contents)
        if not match:
            continue

        param_str = match.group(1)
        params = [param.strip() for param in param_str.split(",")]

        cmd_params = " ".join(param.replace(" ", "") for param in params)

        if key not in output:
            output[key] = []
        output[key].append({
            "run_directory": RUN_DIRECTORY,
            "command": f"{SCRIPT_NAME}{cmd_params}"
        })

# Save to JSON
with open("commands_new.json", "w") as out_file:
    json.dump(output, out_file, indent=4)

print("Done. Output written to sat4j_commands.json.")
