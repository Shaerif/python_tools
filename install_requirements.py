"""
Requirements Installation Manager - Cross Platform
"""

import subprocess
import sys
import os
import platform

def get_pip_command():
    """Get the appropriate pip command for the current platform"""
    if platform.system() == "Windows":
        return [sys.executable, '-m', 'pip']
    return ['pip3'] if os.system('pip3 --version') == 0 else ['pip']

def install_bootstrap_packages():
    try:
        pip_cmd = get_pip_command()
        subprocess.check_call([*pip_cmd, 'install', 'setuptools'])
        return True
    except subprocess.CalledProcessError:
        print("Failed to install setuptools. Please install it manually.")
        return False

def install_requirements():
    try:
        if not install_bootstrap_packages():
            return False

        requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
        if not os.path.exists(requirements_path):
            print("requirements.txt not found!")
            return False
        
        print("Installing requirements... (Press Ctrl+C/Cmd+C to skip)")
        try:
            pip_cmd = get_pip_command()
            # Install platform-specific requirements
            subprocess.check_call([*pip_cmd, 'install', '--upgrade', 'setuptools'])
            subprocess.check_call([*pip_cmd, 'install', '-r', requirements_path])
            return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to install requirements: {e}")
            return False
    except KeyboardInterrupt:
        print("\nInstallation interrupted. Some packages may not be installed.")
        return False

if __name__ == '__main__':
    if install_requirements():
        print("Requirements installed successfully!")
    else:
        print("Failed to install requirements!")
