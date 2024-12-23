# ⚙️ VS Code Settings Manager

> 📝 **Recent Updates**
> - Added workspace settings support
> - Enhanced backup encryption
> - Improved restore validation

## 🔑 Key Features
- 🔒 Encrypted backups
- 💾 Profile management
- 🔄 Auto-sync options
- 📦 Extension settings

## 📋 Commands
```bash
# Backup settings
python src/tools/vscode_backup_restore.py --backup

# Restore settings
python src/tools/vscode_backup_restore.py --restore
```

## 📝 Example
```python
from src.tools.vscode_backup_restore import backup_settings, restore_settings

# Backup VS Code settings
backup_settings()

# Restore VS Code settings
restore_settings()
```
