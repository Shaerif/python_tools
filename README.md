# Project Bot Tools Documentation

This directory contains documentation for various tools used in the Project Bot.

## Available Tools

- [Code Scanner](docs/code_scanner.md) - Scans and analyzes code repositories
- [Data Processor](docs/data_processor.md) - Processes and transforms data
- [Deployment Helper](docs/deployment_helper.md) - Assists with deployment automation

Each tool has its own dedicated documentation page with detailed information about usage, configuration, and examples.

# Python Development Tools

A collection of utility tools for Python development and system maintenance.

## Features

### VS Code Settings Manager
- Backup and restore VS Code settings
- Support for both stable and insider versions

### File Management
- Duplicate file detection and removal
- Documentation file organization
- Project cleanup utilities

### Development Tools
- Codebase analysis and checking
- Requirements management
- Documentation helpers

## Installation

```bash
git clone https://github.com/yourusername/python_tools.git
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
