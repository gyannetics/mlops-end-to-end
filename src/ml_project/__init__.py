"""
Logging Configuration Module

This module sets up a centralized logging system for the project, ensuring consistent logging 
practices across various components. It configures a logger with the name 'mlProjectLogger', 
which can be accessed and used from any part of the application for logging purposes.

Features:
- Sets up a `TimedRotatingFileHandler` that rotates log files daily. The rotated log files 
  are named with the date (Year-Month-Day) and stored in a 'logs' directory.
- Configures logging to output both to a file (in 'logs' directory) and to the console (stdout).
- Uses an environment variable 'LOG_LEVEL' to set the logging level, defaulting to 'INFO' 
  if the variable is not set.
- Prevents the addition of duplicate log handlers in case the module is imported multiple times.

The logging format includes the timestamp, log level, module name, and log message.

Example Usage:
To use the logger in other modules, import the logging module and retrieve 
the 'ml_project_logger' logger:

    import logging
    logger = logging.getLogger('ml_project_logger')
    logger.info('Your log message here')

Note:
The 'logger.info("Logging setup complete")' statement at the end of this module is for 
demonstration and can be removed or commented out in production.

"""


import os
import sys
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

# Logging configuration
LOGGING_STR = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
BASE_LOG_DIR = "logs"

# Create log directory based on the current year and month
current_time = datetime.now()
year_month_dir = os.path.join(BASE_LOG_DIR, current_time.strftime("%Y/%m"))
os.makedirs(year_month_dir, exist_ok=True)

log_filepath = os.path.join(year_month_dir, "running_logs.log")

# Create a logger
logger = logging.getLogger("ml_project_logger")
logger.setLevel(os.getenv("LOG_LEVEL", "INFO"))

# Check if handlers already exist to prevent duplicate logs
if not logger.handlers:
    # Create a TimedRotatingFileHandler for daily log rotation
    log_file_handler = TimedRotatingFileHandler(
        log_filepath, when="midnight", interval=1, backupCount=31, encoding='utf-8'
    )
    log_file_handler.suffix = "%Y-%m-%d"
    log_file_handler.setFormatter(logging.Formatter(LOGGING_STR))

    # Create a StreamHandler for console output
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(logging.Formatter(LOGGING_STR))

    # Add handlers to the logger
    logger.addHandler(log_file_handler)
    logger.addHandler(stream_handler)

# Example of logging usage (you can remove or comment out this part in production)
logger.info("Logging setup complete")

