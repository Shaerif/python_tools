# Import and initialize requirements installer
import docs.install_requirements as install_requirements
install_requirements.install_requirements()

import os
import shutil

# Define backup directory relative to the script location
# This ensures consistent backup location regardless of where script is run from
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKUP_DIR = os.path.join(SCRIPT_DIR, 'backups')

# Initialize backup directory
# Create if it doesn't exist to ensure backup operations can proceed
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

def backup_settings():
    """
    Backup both VS Code Stable and Insiders settings
    - Locates settings.json for both versions
    - Creates backup copies in the backup directory
    - Provides feedback about backup status
    """
    # Function to back up VS Code settings
    print("Backing up settings...")

    # Backup settings for VS Code Stable
    stable_settings = os.path.join(os.getenv('APPDATA'), 'Code', 'User', 'settings.json')
    if os.path.exists(stable_settings):
        # Copy the stable settings file to the backup directory
        shutil.copy(stable_settings, os.path.join(BACKUP_DIR, 'settings_stable.json'))
        print(f"Backed up VS Code Stable settings to {os.path.join(BACKUP_DIR, 'settings_stable.json')}")
    else:
        # Inform the user if the settings file doesn't exist
        print("VS Code Stable settings not found.")

    # Backup settings for VS Code Insiders
    insiders_settings = os.path.join(os.getenv('APPDATA'), 'Code - Insiders', 'User', 'settings.json')
    if os.path.exists(insiders_settings):
        # Copy the insiders settings file to the backup directory
        shutil.copy(insiders_settings, os.path.join(BACKUP_DIR, 'settings_insiders.json'))
        print(f"Backed up VS Code Insiders settings to {os.path.join(BACKUP_DIR, 'settings_insiders.json')}")
    else:
        # Inform the user if the settings file doesn't exist
        print("VS Code Insiders settings not found.")

def restore_settings():
    """
    Restore VS Code settings from backup
    - Allows user to choose between Stable and Insiders versions
    - Copies backup file to appropriate VS Code settings location
    - Provides feedback about restore status
    """
    # Function to restore VS Code settings
    print("Choose which version to restore:")
    print("1. VS Code Stable")
    print("2. VS Code Insiders")
    version = input("Enter 1 or 2: ")

    if version == "1":
        # Restore settings for VS Code Stable
        stable_settings = os.path.join(os.getenv('APPDATA'), 'Code', 'User', 'settings.json')
        # Copy the backup settings file to the original location
        shutil.copy(os.path.join(BACKUP_DIR, 'settings_stable.json'), stable_settings)
        print(f"Restored VS Code Stable settings from {os.path.join(BACKUP_DIR, 'settings_stable.json')}")
    elif version == "2":
        # Restore settings for VS Code Insiders
        insiders_settings = os.path.join(os.getenv('APPDATA'), 'Code - Insiders', 'User', 'settings.json')
        # Copy the backup settings file to the original location
        shutil.copy(os.path.join(BACKUP_DIR, 'settings_insiders.json'), insiders_settings)
        print(f"Restored VS Code Insiders settings from {os.path.join(BACKUP_DIR, 'settings_insiders.json')}")
    else:
        # Handle invalid input
        print("Invalid choice.")

def main():
    """
    Main program flow
    - Presents user with backup/restore options
    - Executes chosen operation
    - Handles invalid inputs gracefully
    """
    # Main function to handle user options
    print("Choose an option:")
    print("1. Backup settings")
    print("2. Restore settings")
    option = input("Enter 1 or 2: ")

    if option == "1":
        # Perform backup operation
        backup_settings()
    elif option == "2":
        # Perform restore operation
        restore_settings()
    else:
        # Handle invalid input
        print("Invalid option.")

if __name__ == "__main__":
    # Entry point: Start the backup/restore process
    main()