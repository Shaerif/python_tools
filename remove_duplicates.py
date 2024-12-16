# Import required libraries
import os
import hashlib
from pathlib import Path
from collections import defaultdict
import subprocess
import sys
import install_requirements

def check_requirements():
    """Check and install required packages."""
    required_packages = ['os', 'shutil', 'hashlib', 'pathlib', 'collections', 'subprocess', 'sys']
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            # Install missing package
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

def calculate_file_hash(filepath):
    """Calculate SHA256 hash of a file.
    
    Args:
        filepath: Path to the file to be hashed
    Returns:
        str: Hexadecimal string of the file's SHA256 hash
    """
    hasher = hashlib.sha256()
    # Read file in chunks to handle large files efficiently
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicates(directory):
    """Find duplicate files in the given directory.
    
    Args:
        directory: Root directory to search for duplicates
    Returns:
        dict: Dictionary with hash values as keys and lists of duplicate file paths as values
    """
    # Use defaultdict to automatically create lists for new hash values
    hash_map = defaultdict(list)
    
    # Recursively walk through all subdirectories
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            # Calculate hash for each file and store in hash_map
            file_hash = calculate_file_hash(filepath)
            hash_map[file_hash].append(filepath)
    
    # Return only entries with more than one file (duplicates)
    return {k: v for k, v in hash_map.items() if len(v) > 1}

def remove_duplicates(duplicates, keep_first=True):
    """Remove duplicate files from the system.
    
    Args:
        duplicates: Dictionary of duplicate files (hash -> list of file paths)
        keep_first: Boolean flag to keep the first occurrence of duplicate files
    """
    for hash_value, file_list in duplicates.items():
        # Display all files with the same hash
        print(f"\nDuplicate files with hash {hash_value}:")
        for i, filepath in enumerate(file_list):
            print(f"{i + 1}. {filepath}")
        
        if keep_first:
            # Remove all duplicates except the first occurrence
            for filepath in file_list[1:]:
                print(f"Removing: {filepath}")
                os.remove(filepath)
        else:
            # Remove all duplicates including the first occurrence
            for filepath in file_list:
                print(f"Removing: {filepath}")
                os.remove(filepath)

# Main execution block
if __name__ == "__main__":
    # Check and install requirements
    check_requirements()
    install_requirements.install_requirements()
    # Start search from current directory
    directory = "."  
    
    # Find all duplicate files
    duplicates = find_duplicates(directory)
    
    if not duplicates:
        print("No duplicate files found.")
    else:
        # Display all found duplicates
        print("\nFound the following duplicate files:")
        for hash_value, file_list in duplicates.items():
            print(f"\nFiles with hash {hash_value}:")
            for filepath in file_list:
                print(filepath)
        
        # Prompt user for confirmation before removing files
        user_input = input("\nWould you like to remove the duplicates? (y/n): ")
        if user_input.lower() == 'y':
            remove_duplicates(duplicates)
            print("\nDuplicate files have been removed.")
