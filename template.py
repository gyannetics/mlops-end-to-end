"""
This script sets up a basic project structure for a machine learning project named 
'ml_project'. It includes creating necessary directories and empty files for the 
project.

Features:
- A context manager `setup_logging` is defined to set up logging with a specified 
  level and format. It ensures that logging is properly initialized and shut down.
- The project structure includes directories and files such as Python modules, 
  configuration files, Dockerfile, requirements.txt, and more, necessary for a typical 
  ML project.
- The script uses the context manager to log the creation of directories and files. 
  It ensures that directories are created if they do not exist and creates empty files 
  if they are not present or are empty.

Usage:
- Run this script to initialize a new project structure for 'ml_project'.
- The logging output will indicate the creation of directories and files, which helps 
  in tracking the setup process.

Note:
- The script assumes a specific project layout and can be modified to fit the structure 
  of different projects.
- It is advisable to review and update the list of files and directories 
  (`list_of_files`) as per the specific needs of your project.
"""

import os
from pathlib import Path
import logging
from contextlib import contextmanager

# Context manager for logging setup
@contextmanager
def setup_logging(level=logging.INFO, log_format='[%(asctime)s]: %(message)s:'):
    """
    A context manager for setting up logging across the application. This manager
    configures logging with a specified level and format, ensuring initialization
    at the start and proper closure at the end of a block, even if errors occur.

    Parameters:
    - level (int, optional): Logging level (e.g., logging.INFO, logging.DEBUG).
      Defaults to logging.INFO.
    - format (str, optional): Format string for log messages. Defaults to
      '[%(asctime)s]: %(message)s:'.

    Yields:
    - None: This context manager does not yield any value.

    """
    logging.basicConfig(level=level, format=log_format)
    try:
        yield
    finally:
        logging.shutdown()

PROJECT_NAME = "ml_project"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/utils/common.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/entity/config_entity.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
    ]

# Using the context manager for logging
with setup_logging():
    for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)

        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info("Creating directory; %s for the file: %s", filedir, filename)

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, "w", encoding="utf-8") as f:
                logging.info("Creating empty file: %s", filepath)

        else:
            logging.info("%s exists", filename)
            