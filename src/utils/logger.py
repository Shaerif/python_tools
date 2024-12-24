import logging
import os
from pathlib import Path
from typing import Optional, Union

def setup_logger(
    name: str, 
    log_file: Optional[str] = None, 
    level: Union[int, str] = logging.INFO
) -> logging.Logger:
    """Configure and return a logger instance with both console and file handlers.

    Args:
        name (str): The name of the logger instance. Used to identify log messages.
        log_file (Optional[str], optional): Path to the log file. If None, only console logging is enabled.
            Defaults to None.
        level (Union[int, str], optional): The logging level. Can be either a string (e.g., 'INFO') 
            or logging constant (e.g., logging.INFO). Defaults to logging.INFO.

    Returns:
        logging.Logger: Configured logger instance with the specified handlers.

    Example:
        >>> logger = setup_logger("app_name", "app.log", "INFO")
        >>> logger.info("Application started")
        >>> logger.error("An error occurred", exc_info=True)

    Note:
        - Creates 'logs' directory if it doesn't exist when file logging is enabled
        - Configures consistent formatting for both console and file outputs
        - Supports all standard Python logging levels
    """
    # Create logger instance
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Add console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Add file handler if log_file is specified
    if log_file:
        log_dir = Path('logs')
        log_dir.mkdir(exist_ok=True)
        file_handler = logging.FileHandler(log_dir / log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

# Example usage in doctest format
if __name__ == "__main__":
    # Setup basic logger
    basic_logger = setup_logger("basic")
    basic_logger.info("This is a basic logger")

    # Setup logger with file output
    full_logger = setup_logger("full", "test.log", "DEBUG")
    full_logger.debug("This is a debug message")
    full_logger.info("This is an info message")
    full_logger.warning("This is a warning message")
