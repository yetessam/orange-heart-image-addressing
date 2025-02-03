from loguru import logger
import sys

def setup_logger(debug_mode=True):
    """Initialize the logger with a simple format and temp_dir stripping."""
    logger.remove()  # Remove default logger

   
    # Add stdout logger with the default format: "- {message}"
    logger.add(
        sys.stdout,
        level="DEBUG" if debug_mode else "INFO",
        format="     - {message}",
        colorize=True  #  color coding
    )
    
    # Overload logger.info and logger.debug
    logger.original_info = logger.info
    logger.original_debug = logger.debug

    def custom_log(original_func):
        """Wrapper function to handle temp_dir removal."""
        def wrapper(message, *args, **kwargs):
            if hasattr(logger, "temp_dir") and logger.temp_dir:
                message = message.replace(logger.temp_dir, "")  # Remove temp_dir
            return original_func(message, *args, **kwargs)
        return wrapper

    logger.info = custom_log(logger.original_info)
    logger.debug = custom_log(logger.original_debug)
    return logger

def set_log_temp(temp_dir):
    logger.temp_dir = temp_dir
    
    
# Example usage (commented out for reference)
"""
if __name__ == "__main__":
    # Initialize the logger once
    setup_logger(debug_mode=True)

    # Set the temporary directory
    set_log_temp("/tmp/my_temp_dir")

    # Log messages (temp_dir will be stripped automatically)
    logger.info("This is a log message. Temp dir: /tmp/my_temp_dir")
    logger.debug("This is a debug message. Temp dir: /tmp/my_temp_dir")
"""