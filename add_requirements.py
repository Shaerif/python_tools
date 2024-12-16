"""
Requirements Management Tool

This module provides functionality to:
1. Add new requirements to requirements.txt
2. Modify Python files to include requirement checks
3. Process entire directories of Python files

Functions:
    add_requirement(package_name, version=None): Adds a new package requirement
    modify_python_file(file_path): Updates Python files with requirement checks
    process_directory(directory): Processes all Python files in a directory
"""

# Purpose: Add requirement installation code to all Python files in the directory

# Fix import path
import install_requirements
install_requirements.install_requirements()

import os
import pkg_resources
import subprocess
import sys

def add_requirement(package_name, version=None):
    try:
        pkg_resources.require(package_name)
    except (pkg_resources.DistributionNotFound, pkg_resources.VersionConflict):
        package_spec = f"{package_name}=={version}" if version else package_name
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_spec])
        with open('requirements.txt', 'a') as f:
            f.write(f"{package_spec}\n")

def modify_python_file(file_path):
    """
    Modify a Python file to include requirement installation code.
    Steps:
    1. Read the file content
    2. Check if import is needed
    3. Add import and function call if not present
    4. Write back the modified content
    """
    # Step 1: Read the current file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Step 2: Check if modification is needed
    if 'import install_requirements' not in content:
        # Step 3: Prepare the new content with requirement installation
        new_content = (
            'import install_requirements\n'
            'install_requirements.install_requirements()\n\n'
            f'{content}'
        )

        # Step 4: Write the modified content back to file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Modified: {file_path}")

def process_directory(directory):
    """
    Process all Python files in the given directory and subdirectories.
    Steps:
    1. Walk through all files recursively
    2. Filter for Python files
    3. Modify each Python file
    """
    # Walk through directory tree
    for root, _, files in os.walk(directory):
        for file in files:
            # Process only Python files, excluding this script
            if file.endswith('.py') and file != 'add_requirements.py':
                file_path = os.path.join(root, file)
                modify_python_file(file_path)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        add_requirement(sys.argv[1])
    else:
        # Get the script's directory location
        directory = os.path.dirname(os.path.abspath(__file__))
        # Process all Python files in the directory
        process_directory(directory)
        print("Completed processing all Python files.")
