import os
import json
import re

BASE_DIR = "."  # <-- change this
RUN_DIRECTORY = "/home/jim/LLm_Software_improvement/lpg_necessary/"
SCRIPT_NAME = "bash run_fixed.sh"

output = {}

for file in os.listdir(BASE_DIR):
    file_path = os.path.join(BASE_DIR, file)
    if os.path.isfile(file_path) and (file.startswith("help5_lpg_") or file.startswith("help6_lpg_") or file.startswith("help_lpg_")):
        key = file.replace("help5_lpg_", "").replace("help6_lpg_", "").replace("help_lpg_", "").replace(".txt", "")
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

        cmd_parts = []
        for param in params:
            name, value = param.split("=")
            name = name.strip()
            value = value.strip().strip("'")

            if value.lower() == "none":
                cmd_parts.append(f"-{name}")
            else:
                cmd_parts.append(f"-{name} {value}")

        command = f"{SCRIPT_NAME} {' '.join(cmd_parts)}"

        if key not in output:
            output[key] = []
        output[key].append({ 
            "run_directory": RUN_DIRECTORY,
            "command": command
        })

# Save to JSON
with open("commands_new.json", "w") as out_file:
    json.dump(output, out_file, indent=4)

print("Done. Output written to lpg_commands.json.")
