
# src/add_requirements.py

import os
import sys
import subprocess

def process_directory(directory):
    requirements = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r') as f:
                    for line in f:
                        if line.startswith('import ') or line.startswith('from '):
                            requirements.add(line.strip())
    return requirements

def write_requirements(requirements, output_file):
    with open(output_file, 'w') as f:
        for requirement in sorted(requirements):
            f.write(requirement + '\n')

def main():
    if len(sys.argv) != 3:
        print("Usage: python add_requirements.py <directory> <output_file>")
        sys.exit(1)

    directory = sys.argv[1]
    output_file = sys.argv[2]

    requirements = process_directory(directory)
    write_requirements(requirements, output_file)

    print(f"Requirements written to {output_file}")

if __name__ == "__main__":
    main()