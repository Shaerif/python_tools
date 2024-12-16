# Import required system modules
import subprocess
import sys
import pkg_resources
import os

def get_required_packages():
    """Read requirements.txt and return list of required packages."""
    # Get the path to requirements.txt in the same directory as this script
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    # Read and parse requirements.txt, skipping empty lines and comments
    with open(requirements_path) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

def check_and_install_requirements():
    """Check for missing packages and install them."""
    # Get list of required packages
    required = get_required_packages()
    # Get set of installed packages
    installed = {pkg.key for pkg in pkg_resources.working_set}

    # Find missing packages
    missing = []
    for package in required:
        package_name = package.split('>=')[0] if '>=' in package else package
        if package_name.lower() not in installed and package_name not in sys.modules:
            missing.append(package)

    # Install missing packages if any
    if missing:
        print("Installing missing requirements...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing)
            print("Requirements installed successfully!")
        except subprocess.CalledProcessError:
            print("Error: Failed to install requirements.")
            sys.exit(1)

def install_requirements(requirements_file='requirements.txt'):
    """Main function to handle requirement installation."""
    try:
        # Read requirements from file
        with open(requirements_file) as f:
            requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

        # Check installed packages
        installed = {pkg.key for pkg in pkg_resources.working_set}
        missing = []

        # Find missing packages
        for requirement in requirements:
            package_name = requirement.split('==')[0].split('>=')[0].split('<=')[0].strip()
            if package_name.lower() not in installed:
                missing.append(requirement)

        # Install missing packages
        if missing:
            print(f"Installing missing packages: {', '.join(missing)}")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing)
            print("All required packages have been installed.")
        else:
            print("All required packages are already installed.")

    except FileNotFoundError:
        # Handle missing requirements.txt file
        print(f"Warning: {requirements_file} not found.")
    except Exception as e:
        # Handle other exceptions
        print(f"Error installing requirements: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # Run the install_requirements function when the script is executed
    install_requirements()
