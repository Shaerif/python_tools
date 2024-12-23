# 📂 Documentation File Manager

> 📝 **Recent Updates**
> - Added automatic file organization
> - Enhanced error handling
> - Updated validation checks

## Overview
Script to organize documentation files by moving them to a dedicated 'docs' directory.

## 🛠️ Functions

### 📥 read_requirements()
- Reads package requirements from requirements.txt
- Falls back to default requirements if file not found

### ✅ check_requirements()
- Verifies all required packages are installed
- Automatically installs missing packages

### 🔍 get_doc_files()
- Find documentation files

### 🔄 move_documentation_files()
- Safe file movement

### prompt_user()
- Interactive confirmation for file moves
- Options: yes/no/exit
- Shows preview of planned moves
