"""
Core functionality package for Python Tools
"""

from pathlib import Path
import sys

# Add core package to Python path
core_path = Path(__file__).parent
if str(core_path) not in sys.path:
    sys.path.append(str(core_path))

# Import core modules
try:
    from . import install_requirements
except ImportError:
    pass  # Optional import, will be handled by error handlers
