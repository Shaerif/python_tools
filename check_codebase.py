import install_requirements
install_requirements.install_requirements()

import os
import sys
from pathlib import Path

# Now import the rest of the modules
import magic
from typing import List, Dict

def is_suspicious_file(filename: str) -> bool:
    # Define patterns of suspicious files
    suspicious_patterns = [
        '.tmp', '.bak', '.swp',  # Temporary files
        'thumbs.db', '.ds_store',  # System files
        '~$',  # Temporary Office files
        '.pyc', '__pycache__',  # Python cache
        '.log',  # Log files
        '.idea/', '.vscode/',  # IDE files
        'node_modules/', 'venv/',  # Dependencies
        '.env', '.env.local',  # Environment files
        '.cache', '.sass-cache',  # Cache directories
        'desktop.ini', '.directory',  # System files
        '.git/objects',  # Git objects
    ]
    # Check if filename matches any suspicious pattern
    return any(pattern in filename.lower() for pattern in suspicious_patterns)

def is_empty_file(filepath: str) -> bool:
    # Check if the file size is zero
    return os.path.getsize(filepath) == 0

def is_large_file(filepath: str, size_limit_mb: int = 100) -> bool:
    # Check if file size exceeds the limit
    return os.path.getsize(filepath) > (size_limit_mb * 1024 * 1024)

def is_binary_file(filepath: str) -> bool:
    # Use magic module to determine if file is binary
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(filepath)
    return not file_type.startswith(('text/', 'application/json', 'application/xml'))

def check_codebase(directory: str) -> Dict[str, List[str]]:
    # Initialize results dictionary
    results = {
        'suspicious_files': [],
        'empty_files': [],
        'duplicate_readmes': [],
        'obsolete_docs': [],
        'large_files': [],
        'binary_files': [],
        'git_artifacts': [],
        'env_files': []
    }
    readme_locations = []
    for root, dirs, files in os.walk(directory):
        # Skip version control and virtual environment directories
        dirs[:] = [d for d in dirs if d not in {'.git', 'venv', 'node_modules', '__pycache__'}]
        for file in files:
            filepath = os.path.join(root, file)
            # Perform various checks on the files
            if is_suspicious_file(file):
                results['suspicious_files'].append(filepath)
            if os.path.isfile(filepath) and is_empty_file(filepath):
                results['empty_files'].append(filepath)
            if file.lower() == 'readme.md':
                readme_locations.append(filepath)
            if file.endswith(('.md', '.txt', '.doc', '.docx')) and \
               any(term in file.lower() for term in ['old', 'backup', 'deprecated']):
                results['obsolete_docs'].append(filepath)
            if is_large_file(filepath):
                results['large_files'].append(filepath)
            if 'src' in root.split(os.sep) and is_binary_file(filepath):
                results['binary_files'].append(filepath)
            if '.git' in root and file.endswith('.pack'):
                results['git_artifacts'].append(filepath)
            if file.startswith('.env'):
                results['env_files'].append(filepath)
    # Check for multiple READMEs in the same directory
    seen_dirs = set()
    for readme in readme_locations:
        parent_dir = os.path.dirname(readme)
        if parent_dir in seen_dirs:
            results['duplicate_readmes'].append(readme)
        seen_dirs.add(parent_dir)
    return results

def format_file_size(filepath: str) -> str:
    # Format file size to a readable string
    size_bytes = os.path.getsize(filepath)
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"

def main():
    # Get the current working directory
    project_dir = os.getcwd()
    # Perform the codebase check
    results = check_codebase(project_dir)
    print("📁 Codebase Check Results\n")
    for category, files in results.items():
        if files:
            print(f"\n🔍 {category.replace('_', ' ').title()}:")
            for file in files:
                size = format_file_size(file)
                print(f"- {file} ({size})")
    if not any(results.values()):
        # Inform the user if no issues were found
        print("✅ No issues found in the codebase.")

if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
