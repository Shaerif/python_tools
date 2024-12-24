import yaml
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class ValidationError:
    """Represents a configuration validation error"""
    field: str
    message: str
    value: Any

class Settings:
    """Configuration manager for Python Tools.
    
    Handles loading, validating, and saving application settings.
    Provides type-safe access to configuration values with validation.
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize Settings manager.
        
        Args:
            config_path (Optional[str]): Path to config file. Defaults to config.yaml in same directory.
        """
        self.config_path = Path(config_path) if config_path else Path(__file__).parent / 'config.yaml'
        self.config: Dict[str, Any] = {}
        self.load_config()

    def validate_config(self) -> list[ValidationError]:
        """Validate configuration values against expected types and ranges.
        
        Returns:
            list[ValidationError]: List of validation errors found, empty if valid.
        """
        errors = []
        
        # Validate backup_dir
        if 'backup_dir' not in self.config:
            errors.append(ValidationError('backup_dir', 'Missing required field', None))
        elif not isinstance(self.config['backup_dir'], str):
            errors.append(ValidationError('backup_dir', 'Must be a string', self.config['backup_dir']))
            
        # Validate log_level
        valid_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        if 'log_level' not in self.config:
            errors.append(ValidationError('log_level', 'Missing required field', None))
        elif self.config['log_level'] not in valid_levels:
            errors.append(ValidationError('log_level', f'Must be one of: {", ".join(valid_levels)}', 
                                       self.config['log_level']))
            
        # Validate max_file_size
        if 'max_file_size' not in self.config:
            errors.append(ValidationError('max_file_size', 'Missing required field', None))
        elif not isinstance(self.config['max_file_size'], (int, float)) or self.config['max_file_size'] <= 0:
            errors.append(ValidationError('max_file_size', 'Must be a positive number', 
                                       self.config['max_file_size']))
        
        return errors

    def load_config(self) -> None:
        """Load configuration from YAML file with validation.
        
        Raises:
            ValueError: If configuration validation fails.
        """
        try:
            if self.config_path.exists():
                with open(self.config_path) as f:
                    self.config = yaml.safe_load(f)
                
                # Validate configuration
                errors = self.validate_config()
                if errors:
                    error_msgs = [f"{e.field}: {e.message}" for e in errors]
                    raise ValueError(f"Invalid configuration:\n" + "\n".join(error_msgs))
            else:
                self.config = self.default_config()
                self.save_config()
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing config file: {e}")

    def save_config(self) -> None:
        """Save current configuration to YAML file.
        
        Raises:
            IOError: If unable to write to config file.
        """
        try:
            with open(self.config_path, 'w') as f:
                yaml.dump(self.config, f, default_flow_style=False)
        except IOError as e:
            raise IOError(f"Unable to save configuration: {e}")

    @staticmethod
    def default_config() -> Dict[str, Any]:
        """Return default configuration settings.
        
        Returns:
            Dict[str, Any]: Default configuration values.
        """
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
