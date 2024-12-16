import install_requirements
install_requirements.install_requirements()

import os
import magic
from datetime import datetime
from pathlib import Path
import argparse

def is_document(file_path):
    """Check if file is a document based on mime type."""
    # Create a Magic object to get the MIME type
    mime = magic.Magic(mime=True)
    # Get the MIME type of the file
    file_type = mime.from_file(str(file_path))
    # Define a list of document MIME types
    doc_types = [
        'application/pdf',
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'text/plain'
    ]
    # Check if the file's MIME type is in the list of document types
    return file_type in doc_types

def scan_documents(directory):
    """Scan directory for document files."""
    # Initialize a list to store results
    results = []
    # Recursively iterate over all files in the directory
    for path in Path(directory).rglob('*'):
        # Check if the path is a file and a document
        if path.is_file() and is_document(path):
            # Get file statistics
            stats = path.stat()
            # Add file information to the results list
            results.append({
                'path': str(path),
                'size': stats.st_size,
                'modified': datetime.fromtimestamp(stats.st_mtime)
            })
    # Return the list of documents
    return results

def main():
    # Set up command-line argument parser
    parser = argparse.ArgumentParser(description='Check document files in codebase')
    # Add '--path' argument with default value '.'
    parser.add_argument('--path', default='.', help='Directory path to scan')
    # Parse the arguments
    args = parser.parse_args()

    # Print the directory being scanned
    print(f"Scanning documents in: {args.path}")
    # Scan for documents in the specified path
    documents = scan_documents(args.path)

    if not documents:
        # Inform user if no documents are found
        print("No document files found.")
        return

    # Print the details of the documents found
    print("\nFound documents:")
    for doc in documents:
        # Print document path and details
        print(f"\nPath: {doc['path']}")
        print(f"Size: {doc['size']} bytes")
        print(f"Last modified: {doc['modified']}")

if __name__ == '__main__':
    # Execute the main function when the script is run
    main()
