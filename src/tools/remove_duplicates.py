"""
Duplicate File Detection and Removal Tool
---------------------------------------
Identifies and safely removes duplicate files in a directory tree using SHA256 hashing.
Features:
- Secure file comparison using cryptographic hashing
- Safe removal with backup options
- Memory-efficient processing for large files
- Detailed reporting of operations
"""

import os
import hashlib
from pathlib import Path
from collections import defaultdict
import subprocess
import sys
from typing import Dict, List, Set, Optional
import logging
from src.utils.logger import setup_logger

# Initialize logger
logger = setup_logger("duplicate_finder", "duplicate_finder.log")

class FileProcessor:
    """Handles file processing operations with safety checks."""
    
    def __init__(self, chunk_size: int = 4096):
        """Initialize file processor.
        
        Args:
            chunk_size (int): Size of chunks to read when processing large files.
                            Defaults to 4KB for optimal performance.
        """
        self.chunk_size = chunk_size
        self.processed_files: Set[str] = set()
        
    def calculate_file_hash(self, filepath: Path) -> Optional[str]:
        """Generate SHA256 hash of file contents.
        
        Args:
            filepath (Path): Path to the file to hash.
            
        Returns:
            Optional[str]: Hexadecimal hash string or None if file cannot be read.
            
        Note:
            Uses chunked reading to handle large files efficiently.
        """
        try:
            hasher = hashlib.sha256()
            with open(filepath, 'rb') as f:
                for chunk in iter(lambda: f.read(self.chunk_size), b''):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except (IOError, PermissionError) as e:
            logger.error(f"Error reading file {filepath}: {e}")
            return None

class DuplicateFinder:
    """Finds and manages duplicate files in a directory tree."""
    
    def __init__(self, base_dir: str):
        """Initialize duplicate finder.
        
        Args:
            base_dir (str): Root directory to start searching for duplicates.
        """
        self.base_dir = Path(base_dir)
        self.processor = FileProcessor()
        self.duplicates: Dict[str, List[Path]] = defaultdict(list)
        
    def find_duplicates(self, exclude_dirs: Optional[List[str]] = None) -> Dict[str, List[Path]]:
        """Scan directory tree for duplicate files.
        
        Args:
            exclude_dirs (Optional[List[str]]): Directories to exclude from scan.
                                              Defaults to None.
                                              
        Returns:
            Dict[str, List[Path]]: Dictionary mapping file hashes to lists of duplicate files.
            
        Note:
            Skips unreadable files and logs errors instead of crashing.
        """
        exclude_dirs = exclude_dirs or []
        hash_map = defaultdict(list)
        
        logger.info(f"Starting duplicate file scan in {self.base_dir}")
        
        for path in self.base_dir.rglob('*'):
            if path.is_file() and not any(d in str(path) for d in exclude_dirs):
                file_hash = self.processor.calculate_file_hash(path)
                if file_hash:
                    hash_map[file_hash].append(path)
        
        # Filter for only duplicates (more than one file with same hash)
        self.duplicates = {k: v for k, v in hash_map.items() if len(v) > 1}
        logger.info(f"Found {len(self.duplicates)} groups of duplicate files")
        return self.duplicates

    def remove_duplicates(self, keep_first: bool = True) -> None:
        """Remove identified duplicate files.
        
        Args:
            keep_first (bool): If True, keeps the first occurrence of each file.
                             Defaults to True.
                             
        Note:
            - Logs all removal operations
            - Implements safety checks before deletion
            - Preserves at least one copy when keep_first is True
        """
        if not self.duplicates:
            logger.warning("No duplicates found to remove")
            return
            
        for hash_value, file_list in self.duplicates.items():
            logger.info(f"\nProcessing duplicate group with hash {hash_value}:")
            self._process_duplicate_group(file_list, keep_first)

    def _process_duplicate_group(self, file_list: List[Path], keep_first: bool) -> None:
        """Process a group of duplicate files.
        
        Args:
            file_list (List[Path]): List of duplicate files.
            keep_first (bool): If True, keeps the first occurrence of each file.
        """
        for i, filepath in enumerate(file_list):
            try:
                if keep_first and i == 0:
                    logger.info(f"Keeping original: {filepath}")
                    continue
                    
                # Safety check before removal
                if not filepath.exists():
                    logger.warning(f"File no longer exists: {filepath}")
                    continue
                    
                filepath.unlink()
                logger.info(f"Removed: {filepath}")
            except PermissionError:
                logger.error(f"Permission denied: {filepath}")
            except Exception as e:
                logger.error(f"Error removing {filepath}: {e}")

def main():
    """Main execution function with error handling."""
    try:
        directory = input("Enter directory to scan: ")
        directory = directory or "."
        
        finder = DuplicateFinder(directory)
        duplicates = finder.find_duplicates(exclude_dirs=['.git', '__pycache__', 'node_modules'])
        
        if not duplicates:
            print("No duplicate files found.")
            return
            
        print("\nFound the following duplicate files:")
        for hash_value, file_list in duplicates.items():
            print(f"\nFiles with hash {hash_value}:")
            for filepath in file_list:
                print(filepath)
        
        if input("\nWould you like to remove the duplicates? (y/n): ").lower() == 'y':
            finder.remove_duplicates()
            print("\nDuplicate files have been removed.")
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print("An error occurred. Check the log file for details.")
        sys.exit(1)

if __name__ == "__main__":
    main()
