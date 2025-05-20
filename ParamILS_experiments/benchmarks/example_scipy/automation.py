import os
import json
import re

BASE_DIR = "."  # <-- change this
RUN_DIRECTORY = "/home/jim/magpie_llm/examples/scipy/necessary/"
SCRIPT_NAME = "bash run_fixed.sh"

output = {}


for file in os.listdir(BASE_DIR):
    file_path = os.path.join(BASE_DIR, file)
    if os.path.isfile(file_path) and (file.startswith("help9_scipy_") or file.startswith("help10_scipy_") or file.startswith("help11_scipy_")):
        key = file.replace("help9_scipy_", "").replace("help10_scipy_", "").replace("help11_scipy_", "").replace(".txt", "")
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

            # Skip boolean False flags
            if value.lower() == "false":
                continue
            # Add all others
            cmd_parts.append(f"--{name}={value}")

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

print("Done. Output written to scipy_commands.json.")
