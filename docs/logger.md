# 📝 Logging Utility

> 📝 **Recent Updates**
> - Added structured logging
> - Enhanced log rotation
> - Improved error tracking

## ⚡ Features
- 🔄 Automatic rotation
- 📊 Log aggregation
- 🎨 Custom formatting
- 🔍 Debug helpers

## 🔧 Configuration
```python
logger = setup_logger(
    name="app",
    log_file="app.log",
    level=logging.INFO
)
```

## 📝 Example
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
````markdown
