# 🧹 Project Cleaner

> 📝 **Recent Updates**
> - Added smart cleaning
> - Enhanced safety checks
> - Improved reporting

## 🎯 Features
- 🗑️ Intelligent cleanup
- ⚡ Fast scanning
- 🛡️ Safe operations
- 📊 Cleanup reports

## 📝 Example
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
```python
# Specify custom log directories
cleaner.clear_logs(log_dirs=['custom_logs', 'app_logs'])

# Specify custom user data directories
cleaner.clear_user_data(data_dirs=['custom_data', 'app_data'])
```
