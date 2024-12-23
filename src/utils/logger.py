import logging
import os
from pathlib import Path

def setup_logger(name: str, log_file: str = None, level=logging.INFO):
    """Configure logging for the application"""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler
    if log_file:
        log_dir = Path('logs')
        log_dir.mkdir(exist_ok=True)
        file_handler = logging.FileHandler(log_dir / log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
