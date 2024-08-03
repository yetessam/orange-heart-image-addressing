from loguru import logger
import sys

def setup_logger(debug_mode=True):
    # Remove the default logger
    logger.remove()

    # Add a new logger that outputs to stdout
    logger.add(sys.stdout, level="DEBUG" if debug_mode else "INFO", format="{level}: {name}  {message}")
    
    # Add another logger that outputs errors to stderr
    logger.add(sys.stderr, level="ERROR", format="{level}: {name}  {message}")

    return logger

# Automatically set up the logger when this module is imported
logger = setup_logger(debug_mode=False)
