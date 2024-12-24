# 🔍 Duplicate File Removal Tool

> 📝 **Recent Updates**
> - Added SHA256 hashing
> - Improved detection accuracy
> - Enhanced safety checks

## 🛠️ Features
- 🔐 Secure file hashing
- 👥 Duplicate detection
- ⚡ Fast scanning
- 🗑️ Safe removal

## 💻 Usage
```python
python src/tools/remove_duplicates.py /path/to/scan
```

## 🔧 Configuration
```yaml
# Configuration for duplicate file removal
hash_algorithm: sha256
scan_directories:
  - /path/to/scan
exclude_patterns:
  - "*.tmp"
  - "*.log"
```

## 📝 Example
```python
from src.tools.remove_duplicates import find_duplicates, remove_duplicates

# Find duplicate files
duplicates = find_duplicates(directory="/path/to/scan")

# Remove duplicate files
remove_duplicates(duplicates, keep_first=True)
```
