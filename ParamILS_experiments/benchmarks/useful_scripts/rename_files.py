import os
import sys

def rename_files_in_directory(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            old_path = os.path.join(root, filename)
            new_filename = filename
            # new_filename = new_filename.replace('help5_', 'help1_')
            # new_filename = new_filename.replace('help4_', 'help2_')
            # new_filename = new_filename.replace('help_', 'help3_')
            new_filename = new_filename.replace('help10_', 'help2_')
            new_filename = new_filename.replace('help11_', 'help3_')
            new_filename = new_filename.replace('help9_', 'help1_')

            # new_filename = new_filename.replace('help_minisat_', 'help3_minisat_')
            # new_filename = new_filename.replace('help_minisat4', 'help2_minisat')
            
            if new_filename != filename:
                new_path = os.path.join(root, new_filename)
                print(f'Renaming: {old_path} -> {new_path}')
                os.rename(old_path, new_path)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python rename_help_files.py <directory_path>")
        sys.exit(1)

    dir_path = sys.argv[1]
    if not os.path.isdir(dir_path):
        print(f"Error: {dir_path} is not a valid directory.")
        sys.exit(1)

    rename_files_in_directory(dir_path)
