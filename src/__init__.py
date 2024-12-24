"""
Python Tools Package
------------------
Main package containing all tools and utilities.
"""

import os
import sys

# Ensure the package root is in the Python path
package_root = os.path.dirname(os.path.dirname(__file__))
if package_root not in sys.path:
    sys.path.insert(0, package_root)
