"""
Requirements Installation Manager

This module handles the installation of all project dependencies.
It ensures that setuptools is installed first as a bootstrap package,
then processes the requirements.txt file for all other dependencies.

Functions:
    install_bootstrap_packages(): Installs basic setup requirements
    install_requirements(): Installs all packages from requirements.txt
"""

# Import required system modules
import subprocess
import sys
import os

def install_bootstrap_packages():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'setuptools'])
    except subprocess.CalledProcessError:
        print("Failed to install setuptools. Please install it manually.")
        sys.exit(1)

def install_requirements():
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if not os.path.exists(requirements_path):
        print("requirements.txt not found!")
        return False
    
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_path])
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == '__main__':
    install_bootstrap_packages()
    if install_requirements():
        print("Requirements installed successfully!")
    else:
        print("Failed to install requirements!")
