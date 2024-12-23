import yaml
from pathlib import Path
from typing import Dict, Any

class Settings:
    def __init__(self):
        self.config_path = Path(__file__).parent / 'config.yaml'
        self.config: Dict[str, Any] = {}
        self.load_config()

    def load_config(self):
        """Load configuration from YAML file"""
        if self.config_path.exists():
            with open(self.config_path) as f:
                self.config = yaml.safe_load(f)
        else:
            self.config = self.default_config()
            self.save_config()

    def save_config(self):
        """Save current configuration to YAML file"""
        with open(self.config_path, 'w') as f:
            yaml.dump(self.config, f)

    @staticmethod
    def default_config() -> Dict[str, Any]:
        """Return default configuration settings"""
        return {
            'backup_dir': 'backups',
            'log_level': 'INFO',
            'max_file_size': 100,  # MB
            'excluded_dirs': [
                '__pycache__',
                '.git',
                'venv',
                'node_modules'
            ]
        }
