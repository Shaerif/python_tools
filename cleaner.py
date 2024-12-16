import install_requirements
install_requirements.install_requirements()

import os
import shutil
from pathlib import Path
from typing import List, Optional

class ProjectCleaner:
    def __init__(self, project_root: str = None):
        # Set the project root directory
        self.project_root = project_root or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def clear_logs(self, log_dirs: List[str] = None) -> None:
        """Clear log files from specified directories."""
        default_log_dirs = ['logs', 'log']
        log_dirs = log_dirs or default_log_dirs
        for log_dir in log_dirs:
            # Clear log files in the specified directories
            self._clear_directory(log_dir, ['.log', '.txt'])

    def clear_cache(self) -> None:
        """Clear cache directories and files."""
        cache_patterns = [
            '__pycache__',
            '.pytest_cache',
            '.mypy_cache',
            '.cache'
        ]
        for pattern in cache_patterns:
            # Clear cache directories matching the patterns
            self._clear_directory(pattern)

    def clear_user_data(self, data_dirs: List[str] = None) -> None:
        """Clear user data directories."""
        default_data_dirs = ['user_data', 'data']
        data_dirs = data_dirs or default_data_dirs
        for data_dir in data_dirs:
            # Clear user data directories
            self._clear_directory(data_dir)

    def clear_tool_data(self) -> None:
        """Clear tool-specific temporary data."""
        tool_patterns = [
            'temp',
            'tmp',
            '.tmp'
        ]
        for pattern in tool_patterns:
            # Clear tool-specific temporary directories
            self._clear_directory(pattern)

    def full_cleanup(self) -> None:
        """Perform all cleanup operations."""
        self.clear_logs()
        self.clear_cache()
        self.clear_user_data()
        self.clear_tool_data()

    def _clear_directory(self, pattern: str, extensions: Optional[List[str]] = None) -> None:
        """Helper method to clear directories/files matching pattern."""
        for path in Path(self.project_root).rglob('*'):
            if pattern in str(path):
                if path.is_dir():
                    try:
                        # Remove the directory and its contents
                        shutil.rmtree(path)
                        print(f"Cleared directory: {path}")
                    except Exception as e:
                        print(f"Error clearing {path}: {e}")
                elif path.is_file() and extensions:
                    if any(str(path).endswith(ext) for ext in extensions):
                        try:
                            # Delete the file
                            path.unlink()
                            print(f"Cleared file: {path}")
                        except Exception as e:
                            print(f"Error clearing {path}: {e}")

if __name__ == "__main__":
    # Create an instance of ProjectCleaner and perform cleanup
    cleaner = ProjectCleaner()
    cleaner.full_cleanup()
