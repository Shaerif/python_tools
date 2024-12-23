"""
Main Menu Interface
Provides a command-line menu for accessing various Python tools
"""

import os
import sys
from pathlib import Path
from typing import List, Tuple, Optional

# Add the current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

def safe_install_requirements():
    """Safely attempt to install requirements with interrupt handling"""
    try:
        from install_requirements import install_requirements
        install_requirements()
    except KeyboardInterrupt:
        print("\nInstallation interrupted by user. Continuing with available packages...")
        return False
    except ImportError as e:
        print("Error: Could not import install_requirements.")
        print("Please ensure install_requirements.py is in the same directory.")
        sys.exit(1)
    return True

# Attempt to install requirements
safe_install_requirements()

import glob
import importlib.util

TOOL_CATEGORIES = {
    "Core Tools": {
        "Requirements Manager": "core/install_requirements.py",
        "Add Requirements": "core/add_requirements.py"
    },
    "Development Tools": {
        "VS Code Backup": "tools/vscode_backup_restore.py",
        "Remove Duplicates": "tools/remove_duplicates.py",
        "Check Codebase": "tools/check_codebase.py",
        "Doc Checker": "tools/doc_checker.py"
    },
    "Utility Tools": {
        "Project Cleaner": "utils/cleaner.py",
        "Move Docs": "tools/move_docs.py"
    }
}

def display_menu(categories: dict) -> str:
    """Display categorized menu options"""
    print("\n🛠️  Python Tools Menu")
    print("=" * 50)
    
    option_number = 1
    option_map = {}
    
    for category, tools in categories.items():
        print(f"\n📁 {category}:")
        for tool_name in tools:
            print(f"{option_number}. {tool_name}")
            option_map[str(option_number)] = (tool_name, tools[tool_name])
            option_number += 1
    
    print("\n0. Exit")
    return input("\n👉 Select an option (0-{}): ".format(len(option_map))), option_map

def run_tool(tool_path: str) -> None:
    """Run the selected Python tool"""
    try:
        full_path = os.path.join(os.path.dirname(__file__), tool_path)
        if not os.path.exists(full_path):
            print(f"❌ Tool not found: {tool_path}")
            return

        print(f"\n🚀 Running {os.path.basename(tool_path)}...")
        
        # Import and run the tool
        spec = importlib.util.spec_from_file_location("module", full_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        if hasattr(module, 'main'):
            module.main()
        print(f"\n✅ Completed running {os.path.basename(tool_path)}")
    except Exception as e:
        print(f"❌ Error running {tool_path}: {str(e)}")

def main():
    """Main program loop"""
    try:
        while True:
            choice, option_map = display_menu(TOOL_CATEGORIES)
            
            if choice == "0":
                print("\n👋 Goodbye!")
                sys.exit(0)
            
            if choice in option_map:
                tool_name, tool_path = option_map[choice]
                run_tool(tool_path)
            else:
                print("\n❌ Invalid option. Please try again.")
            
            input("\n⏎ Press Enter to continue...")
            
    except KeyboardInterrupt:
        print("\n\n👋 Exiting program...")
        sys.exit(0)

if __name__ == "__main__":
    # Ensure we're in the correct directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
