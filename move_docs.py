import os
import shutil
import subprocess
import sys
from typing import List, Tuple, Optional

def read_requirements() -> List[str]:
    """Read and validate requirements from requirements.txt."""
    try:
        with open('requirements.txt', 'r') as f:
            # Read and clean up each line
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        # Return default packages if requirements.txt not found
        return ['os', 'shutil', 'pathlib', 'typing']

def ensure_docs_folder_exists():
    """Ensure that the 'docs' folder exists, create if it doesn't."""
    if not os.path.exists('docs'):
        os.makedirs('docs')

def get_unique_filename(directory, filename):
    """Generate a unique filename if a file with the same name already exists."""
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    # Increment filename until a unique one is found
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base}_{counter}{extension}"
        counter += 1
    return new_filename

def get_doc_files() -> List[Tuple[str, str]]:
    """Find documentation files and their destinations."""
    doc_files = []
    doc_extensions = ('.md', '.rst', '.txt', '.doc', '.docx', '.pdf')
    for filename in os.listdir('.'):
        if filename == 'README.md' or not filename.endswith(doc_extensions):
            continue
        # Get a unique destination filename
        dest_name = get_unique_filename('docs', filename)
        doc_files.append((filename, dest_name))
    return doc_files

def prompt_user(files: List[Tuple[str, str]]) -> Optional[bool]:
    """Ask user to confirm file moves."""
    if not files:
        print("No documentation files found to move.")
        return None
    # Display files to be moved
    print("\nFiles to be moved to docs/:")
    for src, dest in files:
        print(f"  {src} → {dest}")
    # Prompt user for confirmation
    while True:
        choice = input("\nMove these files? (y/n/exit): ").lower()
        if choice in ('y', 'yes'):
            return True
        if choice in ('n', 'no'):
            return False
        if choice == 'exit':
            sys.exit(0)
        print("Please enter 'y', 'n', or 'exit'")

def move_documentation_files():
    """Move documentation files with user confirmation."""
    while True:
        files = get_doc_files()
        response = prompt_user(files)
        if response is None or response is False:
            break
        for src, dest in files:
            try:
                # Move the file to the docs directory
                shutil.move(src, os.path.join('docs', dest))
                print(f"✓ Moved: {src} → docs/{dest}")
            except Exception as e:
                print(f"✗ Error moving {src}: {e}")

def main():
    """Main execution function."""
    print("Documentation File Mover")
    print("======================")
    try:
        ensure_docs_folder_exists()
        move_documentation_files()
    except KeyboardInterrupt:
        # Handle user interruption gracefully
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        # Handle other exceptions
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Run the main function when the script is executed
    main()