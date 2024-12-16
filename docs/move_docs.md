# move_docs.py Documentation

## Overview
Script to organize documentation files by moving them to a dedicated 'docs' directory.

## Functions

### read_requirements()
- Reads package requirements from requirements.txt
- Falls back to default requirements if file not found

### check_requirements()
- Verifies all required packages are installed
- Automatically installs missing packages

### get_doc_files()
- Scans current directory for documentation files
- Excludes README.md
- Supports: .md, .rst, .txt, .doc, .docx, .pdf

### prompt_user()
- Interactive confirmation for file moves
- Options: yes/no/exit
- Shows preview of planned moves

### move_documentation_files()
- Handles the file movement process
- Includes error handling
- Provides movement status feedback
