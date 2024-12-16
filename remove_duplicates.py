# Import required libraries for file operations and hashing
import os
import hashlib
from pathlib import Path
from collections import defaultdict
import subprocess
import sys
import install_requirements

def calculate_file_hash(filepath):
    """
    Generate SHA256 hash of file contents
    - Reads file in chunks to handle large files efficiently
    - Returns hexadecimal hash string
    """
    hasher = hashlib.sha256()
    # Read file in chunks to handle large files efficiently
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicates(directory):
    """
    Scan directory tree for duplicate files
    - Uses SHA256 hashing to identify identical files
    - Creates hash map of file paths grouped by hash
    - Returns only groups containing duplicates
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
    """
    Remove identified duplicate files
    - Shows list of duplicate files with same hash
    - Optionally keeps first occurrence of each file
    - Removes duplicate files from filesystem
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

# Main execution block with user interaction
if __name__ == "__main__":
    # Initialize requirements
    install_requirements.install_requirements()
    
    # Set starting directory for duplicate search
    directory = "."  
    
    # Execute duplicate detection
    duplicates = find_duplicates(directory)
    
    # Handle results and user interaction for file removal
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
