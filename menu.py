"""
Main Menu Interface
Provides a command-line menu for accessing various Python tools
"""

import os
import sys
from pathlib import Path

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

def get_python_tools():
    """Get all Python files in the current directory excluding menu.py"""
    tools = []
    excluded_files = ["menu.py", "__init__.py", "install_requirements.py"]
    
    current_dir = Path(__file__).parent
    for file in current_dir.glob("*.py"):
        if file.name not in excluded_files:
            name = file.stem
            title = " ".join(name.split("_")).title()
            tools.append((title, name, str(file)))
    
    if not tools:
        print("No Python tools found in directory!")
        tools.append(("Exit", "exit", None))
    
    return sorted(tools)

def display_menu(tools):
    """Display the main menu options"""
    print("\n=== Python Tools Menu ===")
    for idx, (title, _, _) in enumerate(tools, 1):
        print(f"{idx}. {title}")
    max_option = len(tools)
    return input(f"\nSelect an option (1-{max_option}): ")

def run_tool(tool_path):
    """Run the selected Python tool"""
    try:
        tool_path = Path(tool_path)
        spec = importlib.util.spec_from_file_location("module", str(tool_path))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        if hasattr(module, 'main'):
            module.main()
        print(f"\nCompleted running {tool_path}")
    except Exception as e:
        print(f"Error running {tool_path}: {str(e)}")

def main():
    try:
        tools = get_python_tools()
        while True:
            try:
                choice = display_menu(tools)
                try:
                    choice_idx = int(choice) - 1
                    if choice_idx == len(tools):
                        print("Exiting...")
                        sys.exit(0)
                    elif 0 <= choice_idx < len(tools):
                        _, _, tool_file = tools[choice_idx]
                        tool_path = os.path.join(current_dir, tool_file)
                        print(f"\nRunning {tool_file}...")
                        run_tool(tool_path)
                    else:
                        print("Invalid option. Please try again.")
                except ValueError:
                    print("Please enter a valid number.")
            except KeyboardInterrupt:
                print("\nOperation cancelled. Return to menu...")
                continue
    except KeyboardInterrupt:
        print("\nExiting program...")
        sys.exit(0)

if __name__ == "__main__":
    main()
