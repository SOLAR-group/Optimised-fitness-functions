import os
import json
import re

BASE_DIR = "."  # <-- change this
RUN_DIRECTORY = "/home/jim/LLm_Software_improvement/minisat_necessary/"
SCRIPT_NAME = "bash run_fixed.sh"

output = {}


for file in os.listdir(BASE_DIR):
    file_path = os.path.join(BASE_DIR, file)
    if os.path.isfile(file_path) and (file.startswith("help5_minisat_") or file.startswith("help_minisat4_") or file.startswith("help_minisat_")):
        key = file.replace("help5_minisat_", "").replace("help_minisat4_", "").replace("help_minisat_", "").replace(".txt", "")
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

        cmd_params = ""
        for param in params:
            name, value = param.split("=")
            name = name.strip()
            value = value.strip().strip("'")

            if value.lower() == "true":
                cmd_params += f" -{name}"
            elif value.lower() == "false":
                cmd_params += f" -no-{name}"
            else:
                cmd_params += f" -{name}={value}"

        if key not in output:
            output[key] = []
        output[key].append({
            "run_directory": RUN_DIRECTORY,
            "command": f"{SCRIPT_NAME}{cmd_params}"
        })

# Save to JSON
with open("commands_new.json", "w") as out_file:
    json.dump(output, out_file, indent=4)

print("Done. Output written to minisat_doc_commands.json.")
