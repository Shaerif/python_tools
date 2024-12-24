"""
Python Tools Menu Interface
--------------------------
Provides a command-line interface for accessing various Python tools.
Features:
- Categorized tool organization
- Dynamic tool loading
- Error handling and recovery
- Safe requirements installation
"""

import os
import sys
from pathlib import Path
from typing import List, Tuple, Optional, Dict, Any
import importlib.util
import glob

# Add src directory to Python path
src_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(src_dir)
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

class ToolError(Exception):
    """Custom exception for tool-related errors."""
    pass

def safe_install_requirements():
    """Safely attempt to install requirements with interrupt handling"""
    try:
        from core import install_requirements
        install_requirements.install_requirements()
    except KeyboardInterrupt:
        print("\nInstallation interrupted by user. Continuing with available packages...")
        return False
    except ImportError as e:
        print(f"Error: Could not import install_requirements: {e}")
        print("Please ensure install_requirements.py is in the core directory.")
        sys.exit(1)
    return True

# Attempt to install requirements
safe_install_requirements()

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
        "Move Docs": "tools/move_docs.py",
        "Update Python": "tools/update_python.py"  # Added new tool
    }
}

def get_tool_description(tool_path: str) -> str:
    """Get the description of a tool from its docstring.
    
    Args:
        tool_path (str): Path to the tool file
        
    Returns:
        str: Tool description or default message if not found
    """
    try:
        spec = importlib.util.spec_from_file_location("module", tool_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.__doc__.split('\n')[0] if module.__doc__ else "No description available"
    except Exception:
        return "Description unavailable"

def display_menu(categories: dict) -> Tuple[str, Dict[str, Tuple[str, str]]]:
    """Display categorized menu options with tool descriptions.
    
    Args:
        categories (dict): Dictionary of tool categories and their tools
        
    Returns:
        Tuple[str, Dict[str, Tuple[str, str]]]: Selected option and option mapping
    """
    print("\n🛠️  Python Tools Menu")
    print("=" * 50)
    
    option_map = {}
    option_number = 1
    
    for category, tools in categories.items():
        print(f"\n📁 {category}:")
        for tool_name, tool_path in tools.items():
            full_path = os.path.join(os.path.dirname(__file__), tool_path)
            description = get_tool_description(full_path)
            print(f"{option_number}. {tool_name}")
            print(f"   └─ {description}")
            option_map[str(option_number)] = (tool_name, tool_path)
            option_number += 1
    
    print("\n0. Exit")
    return input("\n👉 Select an option (0-{}): ".format(len(option_map))), option_map

def run_tool(tool_path: str) -> None:
    """Run the selected Python tool with error handling.
    
    Args:
        tool_path (str): Path to the tool to run
        
    Raises:
        ToolError: If the tool cannot be run
    """
    try:
        full_path = os.path.join(os.path.dirname(__file__), tool_path)
        if not os.path.exists(full_path):
            raise ToolError(f"Tool not found: {tool_path}")

        print(f"\n🚀 Running {os.path.basename(tool_path)}...")
        
        spec = importlib.util.spec_from_file_location("module", full_path)
        if not spec or not spec.loader:
            raise ToolError(f"Could not load tool: {tool_path}")
            
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        if hasattr(module, 'main'):
            module.main()
            print(f"\n✅ Successfully completed: {os.path.basename(tool_path)}")
        else:
            raise ToolError(f"Tool has no main() function: {tool_path}")
            
    except Exception as e:
        error_msg = f"❌ Error running {tool_path}: {str(e)}"
        print(error_msg)
        raise ToolError(error_msg) from e

def main():
    """Main program loop"""
    try:
        while True:
            choice, option_map = display_menu(TOOL_CATEGORIES)
            
            if choice == "0":
                print("\n👋 Goodbye!")
                sys.exit(0)
            
            if choice in option_map:
                _, tool_path = option_map[choice]
                try:
                    run_tool(tool_path)
                except ToolError:
                    print("\n❌ Failed to run the tool. Please check the error message above.")
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
