import pytest
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def temp_dir(tmpdir):
    """Provide a temporary directory for file operations"""
    return tmpdir

@pytest.fixture
def sample_files(temp_dir):
    """Create sample files for testing"""
    files = {
        'test1.txt': 'content1',
        'test2.txt': 'content2',
        'test.md': '# Header'
    }
    for name, content in files.items():
        temp_dir.join(name).write(content)
    return temp_dir
