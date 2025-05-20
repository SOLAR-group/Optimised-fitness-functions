import os
import json
import re

BASE_DIR = "."  # <- change this
RUN_DIRECTORY = "/home/jim/magpie_llm/examples/weka/necessary/"
SCRIPT_NAME = "bash run_fixed.sh"

output = {}
for file in os.listdir(BASE_DIR):
    file_path = os.path.join(BASE_DIR, file)
    if os.path.isfile(file_path) and (file.startswith("help4_weka_") or file.startswith("help5_weka_") or file.startswith("help_weka_")):
        key = file.replace("help5_weka_", "").replace("help4_weka_", "").replace("help_weka_", "").replace(".txt", "")
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

        # Build the command-line string
        cmd_params = ""
        for param in params:
            name, value = param.split("=")
            cmd_params += f" -{name.strip()} {value.strip()}"
        if key not in output:
            output[key] = []
        output[key].append({
            "run_directory": RUN_DIRECTORY,
            "command": f"{SCRIPT_NAME}{cmd_params}"
        })

# Save to JSON
with open("commands_new.json", "w") as out_file:
    json.dump(output, out_file, indent=4)

print("Done. Output written to commands.json.")
