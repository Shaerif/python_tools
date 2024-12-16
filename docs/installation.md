# Installation Guide

## System Requirements

- Python 3.8 or higher
- pip (package installer)
- Git (for version control)

## Platform-Specific Requirements

### Windows
```bash
python -m pip install --upgrade pip setuptools
python -m pip install python-magic-bin
```

### Linux/MacOS
```bash
pip3 install --upgrade pip setuptools
pip3 install python-magic
```

## Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/yourusername/python_tools.git
```

2. Navigate to project directory:
```bash
cd python_tools
```

3. Install requirements:
```bash
python install_requirements.py
```

## Verification

Run the test suite:
```bash
python menu.py
```
