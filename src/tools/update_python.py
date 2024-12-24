import os
import sys
import platform
import subprocess
import requests
from bs4 import BeautifulSoup

def get_latest_python_installer():
    """Fetch the latest Python installer URL for Windows 64-bit"""
    url = "https://www.python.org/downloads/windows/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    release_number = soup.find('span', {'class': 'release-number'})
    
    if release_number:
        version = release_number.text.split()[-1]
        installer_url = f"https://www.python.org/ftp/python/{version}/python-{version}-amd64.exe"
        return installer_url, version
    else:
        raise RuntimeError("Could not find the latest Python version on the website.")

def update_python_windows():
    """Update Python on Windows"""
    print("Updating Python on Windows...")
    try:
        # Get the latest Python installer URL
        installer_url, latest_version = get_latest_python_installer()
        print(f"Latest Python version: {latest_version}")

        # Download the latest Python installer
        installer_path = os.path.join(os.getenv('TEMP'), f'python-{latest_version}-amd64.exe')
        subprocess.run(["curl", "-o", installer_path, installer_url], check=True)
        
        # Run the installer
        subprocess.run([installer_path, "/quiet", "InstallAllUsers=1", "PrependPath=1"], check=True)
        
        # Update pip and setuptools
        subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pip"], check=True)
        subprocess.run(["python", "-m", "pip", "install", "--upgrade", "setuptools"], check=True)
        
        print(f"Python {latest_version} and pip have been updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error updating Python: {e}")
    except RuntimeError as e:
        print(f"Error: {e}")

def update_python_linux():
    """Update Python on Linux"""
    print("Updating Python on Linux...")
    try:
        subprocess.run(["sudo", "apt-get", "update"], check=True)
        subprocess.run(["sudo", "apt-get", "install", "-y", "python3", "python3-pip"], check=True)
        subprocess.run(["python3", "-m", "pip", "install", "--upgrade", "pip"], check=True)
        subprocess.run(["python3", "-m", "pip", "install", "--upgrade", "setuptools"], check=True)
        print("Python and pip have been updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error updating Python: {e}")

def update_python_macos():
    """Update Python on MacOS"""
    print("Updating Python on MacOS...")
    try:
        subprocess.run(["brew", "update"], check=True)
        subprocess.run(["brew", "upgrade", "python"], check=True)
        subprocess.run(["python3", "-m", "pip", "install", "--upgrade", "pip"], check=True)
        subprocess.run(["python3", "-m", "pip", "install", "--upgrade", "setuptools"], check=True)
        print("Python and pip have been updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error updating Python: {e}")

def verify_python_version():
    """Verify the current Python version"""
    try:
        version = subprocess.run(["python", "--version"], capture_output=True, text=True, check=True)
        print(f"Current Python version: {version.stdout.strip()}")
    except subprocess.CalledProcessError as e:
        print(f"Error verifying Python version: {e}")

def main():
    """Main function to update Python based on the platform"""
    current_platform = platform.system()
    if current_platform == "Windows":
        update_python_windows()
    elif current_platform == "Linux":
        update_python_linux()
    elif current_platform == "Darwin":
        update_python_macos()
    else:
        print(f"Unsupported platform: {current_platform}")
    
    # Verify the current Python version after the update
    verify_python_version()

if __name__ == "__main__":
    main()
