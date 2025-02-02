import logging

def initialize_logger():
    """
    Initializes and returns a logger instance with DEBUG level and a console handler.
    
    The logger is set up once per application and prints comprehensive messages
    including timestamps, module names, log levels, and messages.
    """
    logger = logging.getLogger("OmniscientDesktopUI")
    logger.setLevel(logging.DEBUG)
    
    # Avoid adding multiple handlers if the logger is already configured.
    if not logger.handlers:
        # Set up a console handler to output log messages to standard output.
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        
        # Define the format for log messages.
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        console_handler.setFormatter(formatter)
        
        logger.addHandler(console_handler)
    
    return logger