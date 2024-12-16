# Project Bot Tools Documentation

This directory contains documentation for various tools used in the Project Bot.

## Available Tools

- [Code Scanner](code_scanner.md) - Scans and analyzes code repositories
- [Data Processor](data_processor.md) - Processes and transforms data
- [Deployment Helper](deployment_helper.md) - Assists with deployment automation

Each tool has its own dedicated documentation page with detailed information about usage, configuration, and examples.

# Python Tools

Collection of utility scripts for project maintenance.

## Tools Available

### move_docs.py

Automated documentation file organizer that helps maintain project documentation structure.

#### Features
- Automatically moves documentation files to a `docs` folder
- Interactive file movement confirmation
- Prevents README.md from being moved
- Handles file naming conflicts
- Supports multiple document formats (.md, .rst, .txt, .doc, .docx, .pdf)

#### Usage
```bash
python move_docs.py
```

#### Requirements
- Python 3.6+
- Dependencies listed in requirements.txt

# Project Cleaner Tool

A Python-based utility for cleaning up project directories before release by removing unnecessary files and folders.

## Overview

This tool helps developers prepare their projects for release by automatically removing unwanted files and directories such as:
- Temporary files
- Development artifacts
- Local configuration files
- Cache directories

## Installation

```bash
git clone https://github.com/yourusername/python_tools.git
cd python_tools
pip install -r requirements.txt
```

## Usage

1. Basic usage:
```bash
python cleaner.py /path/to/your/project
```

2. With custom configuration:
```bash
python cleaner.py /path/to/your/project --config custom_config.yaml
```

## Configuration

Create a `config.yaml` file to customize which files and directories to clean:

```yaml
exclude_patterns:
  - "*.pyc"
  - "__pycache__"
  - ".env"
  - "node_modules"
  - ".git"

keep_patterns:
  - "*.md"
  - "LICENSE"
  - "*.py"
```

## Examples

### Clean a Python Project
```bash
python cleaner.py /path/to/python/project
```

### Clean a Node.js Project
```bash
python cleaner.py /path/to/node/project --config node_config.yaml
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT License](LICENSE)
