# 🔌 API Documentation

> 📝 **Recent Updates**
> - Reorganized API structure
> - Added menu system integration
> - Updated tool interfaces

## 🛠️ Core API

### 📦 Menu System
```python
from src.menu import run_tool

# Run specific tool
run_tool('tools/vscode_backup_restore.py')
```

### 📦 Requirements Manager
```python
from src.core.install_requirements import install_requirements

# Install project dependencies
success = install_requirements()
```

### ⚙️ Settings Manager
```python
from src.config.settings import Settings

# Initialize settings
settings = Settings()

# Access configuration
backup_dir = settings.config['backup_dir']

# Update and save settings
settings.config['log_level'] = 'DEBUG'
settings.save_config()
```

## 🔧 Tools API

### 💾 VS Code Backup
```python
from src.tools.vscode_backup_restore import backup_settings, restore_settings

# Backup VS Code settings
backup_settings()

# Restore VS Code settings
restore_settings()
```

### 🔍 Duplicate File Scanner
```python
from src.tools.remove_duplicates import find_duplicates, remove_duplicates

# Find duplicate files
duplicates = find_duplicates(directory="./")

# Remove duplicate files
remove_duplicates(duplicates, keep_first=True)
```

### 📄 Documentation Checker
```python
from src.tools.doc_checker import check_docs

# Check documentation files
issues = check_docs(directory="./docs")
```

## ⚙️ Utils API

### 📝 Logger
```python
from src.utils.logger import setup_logger

# Setup application logger
logger = setup_logger(
    name="app_name",
    log_file="app.log",
    level="INFO"
)

# Usage
logger.info("Operation completed")
logger.error("Error occurred")
```

### 🧹 Cleaner
```python
from src.utils.cleaner import ProjectCleaner

# Initialize cleaner
cleaner = ProjectCleaner()

# Clean specific items
cleaner.clear_logs()
cleaner.clear_cache()
cleaner.clear_user_data()

# Full cleanup
cleaner.full_cleanup()
```

## 🔄 Error Handling

### Exception Types
```python
class SecurityError(Exception):
    """Raised for security-related issues"""
    pass

class ConfigurationError(Exception):
    """Raised for configuration-related issues"""
    pass
```

### Error Handling Example
```python
try:
    settings = Settings()
    settings.load_config()
except FileNotFoundError:
    print("Configuration file not found")
except yaml.YAMLError:
    print("Invalid configuration format")
```

## 🎯 Response Types

### Success Response
```python
{
    "status": "success",
    "data": {...},
    "message": "Operation completed successfully"
}
```

### Error Response
```python
{
    "status": "error",
    "error": "ErrorType",
    "message": "Error description"
}
```

## 📚 Type Definitions

### Common Types
```python
from typing import Dict, List, Optional, Union

PathLike = Union[str, Path]
ConfigDict = Dict[str, Any]
FileList = List[PathLike]
```

## 🔒 Security Considerations

### Safe File Operations
```python
from pathlib import Path

def safe_file_operation(file_path: PathLike) -> bool:
    """Safely handle file operations with path validation"""
    path = Path(file_path).resolve()
    if not path.is_relative_to(base_dir):
        raise SecurityError("Invalid path")
    return True
```

## 📋 Configuration

### Default Configuration
```yaml
backup_dir: backups
log_level: INFO
max_file_size: 100  # MB
excluded_dirs:
  - __pycache__
  - .git
  - venv
  - node_modules
```

## 🚀 Usage Examples

### Complete Workflow
```python
# Initialize components
settings = Settings()
logger = setup_logger("app")
cleaner = ProjectCleaner()

# Perform operations
try:
    backup_settings()
    cleaner.clear_cache()
    logger.info("Backup and cleanup completed")
except Exception as e:
    logger.error(f"Operation failed: {e}")
```

---

> 📌 **Note**: All API methods include proper type hints and docstrings. Refer to the source code for detailed documentation.
