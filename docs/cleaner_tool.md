# 🧹 Project Cleaner Tool

> 📝 **Recent Updates**
> - Added new cleaning features
> - Updated usage examples
> - Improved configuration options

## ⚡ Features
- 🗑️ Clear log files
- 🧹 Clear cache directories
- 🔄 Clear user data
- 🧮 Clear tool-specific data

## 💻 Usage Examples
```python
from src.utils.cleaner import ProjectCleaner

# Initialize cleaner
cleaner = ProjectCleaner()

# Perform full cleanup
cleaner.full_cleanup()
```

### Specific Operations

```python
# Clear only logs
cleaner.clear_logs()

# Clear only cache
cleaner.clear_cache()

# Clear user data
cleaner.clear_user_data()

# Clear tool data
cleaner.clear_tool_data()
```

### Custom Configuration

You can specify custom log directories:

```python
cleaner.clear_logs(log_dirs=['custom_logs', 'app_logs'])
```

Or custom user data directories:

```python
cleaner.clear_user_data(data_dirs=['custom_data', 'app_data'])
```

## Configuration

The tool automatically detects the project root directory, but you can specify a custom path:

```python
cleaner = ProjectCleaner(project_root="/path/to/your/project")
```

## Default Patterns

- Log files: Searches for directories named 'logs' or 'log'
- Cache: Cleans '__pycache__', '.pytest_cache', '.mypy_cache', '.cache'
- User data: Searches for 'user_data' and 'data' directories
- Tool data: Cleans 'temp', 'tmp', '.tmp' directories

## Safety Features

- The tool prints operations as they are performed
- Errors are caught and reported without stopping the cleanup process
- Read-only files are handled appropriately
