
# doc_checker.py

import os
import re

def check_docs(directory):
    """
    Check documentation files in the given directory for issues.
    """
    issues = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                with open(os.path.join(root, file), 'r') as f:
                    content = f.read()
                    if not re.search(r'#\s+\w+', content):
                        issues.append(f"{file} is missing a title")
                    if not re.search(r'\n##\s+\w+', content):
                        issues.append(f"{file} is missing a section header")
    return issues

if __name__ == "__main__":
    directory = input("Enter the directory to check: ")
    issues = check_docs(directory)
    if issues:
        print("Issues found:")
        for issue in issues:
            print(f" - {issue}")
    else:
        print("No issues found.")