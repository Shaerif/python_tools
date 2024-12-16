# 🐍 Python Tools Documentation

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
[![Made with Python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

This directory contains documentation for various tools used in the Project Bot.

## 🛠️ Available Tools

- [🔍 Code Scanner](docs/code_scanner.md) - Scans and analyzes code repositories for quality and security issues
- [⚡ Data Processor](docs/data_processor.md) - Processes and transforms data with support for multiple formats
- [🚀 Deployment Helper](docs/deployment_helper.md) - Assists with deployment automation and configuration
- [⚙️ VS Code Manager](docs/vscode_manager.md) - Manages VS Code settings and extensions
- [📁 File Organizer](docs/file_organizer.md) - Handles file organization and duplicate detection
- [📚 Doc Generator](docs/doc_generator.md) - Automates documentation generation and maintenance
- [📦 Package Manager](docs/package_manager.md) - Manages Python package dependencies
- [✨ Code Formatter](docs/code_formatter.md) - Enforces consistent code style and formatting
- [🧪 Test Runner](docs/test_runner.md) - Automated test execution and reporting

Each tool can be accessed individually or through the central menu system (menu.py).
See individual documentation pages for detailed usage instructions and configuration options.

# Python Development Tools

A collection of utility tools for Python development and system maintenance.

## Features

### 🔧 VS Code Settings Manager
- Backup and restore VS Code settings
- Support for both stable and insider versions

### 📂 File Management
- Duplicate file detection and removal
- Documentation file organization
- Project cleanup utilities

### 🛠️ Development Tools
- Codebase analysis and checking
- Requirements management
- Documentation helpers

## Installation

```bash
git clone https://github.com/Shaerif/python_tools.git
cd python_tools
pip install -r requirements.txt
```

## Usage

Each tool can be run independently:

```bash
python vscode_backup_restore.py  # Backup/restore VS Code settings
python remove_duplicates.py      # Find and remove duplicate files
python cleaner.py               # Clean project directories
python doc_checker.py           # Analyze documentation files
```

## Documentation
All documentation can be found in the [`docs/`](docs/) directory.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Roadmap

See [ROADMAP.md](ROADMAP.md) for future development plans.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

## License

MIT License - See LICENSE file for details

# Python Tools

A comprehensive collection of Python development and maintenance utilities.

## Technologies & Requirements

### 🔧 Core Technologies
- 🐍 Python 3.8+
- 📦 pip (latest version)

### 📚 Key Dependencies
- 🔨 setuptools >= 65.5.1
- 🖱️ click >= 8.0.0
- 🌐 requests >= 2.28.0
- 📁 pathlib (for Python < 3.4)
- ✨ python-magic (platform-specific)

### 🔧 Development Tools
- 💻 Visual Studio Code (recommended)
- 🔄 Git for version control
- 🐍 Python virtual environment

## Features

### Package Management
- Automatic dependency installation
- Cross-platform compatibility
- Requirements verification

### Development Tools
- Code analysis and linting
- Documentation helpers
- Project cleanup utilities

## Quick Start

```bash
# Clone the repository
git clone https://github.com/Shaerif/python_tools.git

# Navigate to project directory
cd python_tools

# Install requirements
python install_requirements.py

# Run the tools menu
python menu.py
```

## Using the Tools Menu

The `menu.py` script provides a centralized interface to access all available tools:

```bash
python menu.py [--help]
```

### Menu Options

1. ⚙️ VS Code Settings Manager
   - Backup settings
   - Restore settings
   - Compare configurations

2. 📂 File Management
   - Scan for duplicates
   - Clean project directories
   - Organize documentation

3. Development Tools
   - Code analysis
   - Documentation check
   - Requirements update

4. System Maintenance
   - Cache cleanup
   - Temporary file removal
   - Log rotation

### Command Line Arguments

```bash
python menu.py --tool <tool_name>    # Run a specific tool directly
python menu.py --list                # List all available tools
python menu.py --config <file>       # Use custom configuration
```

## Documentation

Detailed documentation is available in the [`docs/`](docs/) directory:

- 📥 [Installation Guide](docs/installation.md)
- 📖 [Usage Guide](docs/usage.md)
- 👥 [Contributing Guidelines](docs/CONTRIBUTING.md)
- 📝 [Change Log](docs/CHANGELOG.md)
- 🗺️ [Roadmap](docs/ROADMAP.md)

## License

MIT License - See [LICENSE](docs/LICENSE) file for details

## 🤝 Community

[![GitHub Stars](https://img.shields.io/github/stars/Shaerif/python_tools.svg)](https://github.com/Shaerif/python_tools/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/Shaerif/python_tools.svg)](https://github.com/Shaerif/python_tools/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/Shaerif/python_tools.svg)](https://github.com/Shaerif/python_tools/pulls)
