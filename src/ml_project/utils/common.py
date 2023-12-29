"""
This module, commons.py, offers utility functions for common tasks in machine learning
projects. It includes functions for reading and saving configurations in YAML and JSON
formats, managing directories, handling binary data with joblib, and calculating file
sizes.

Functions:
- read_yaml(path_to_yaml: Path) -> ConfigBox: Reads a YAML file, returning its contents
  as a ConfigBox object.
- create_directories(path_to_directories: list, verbose=True): Creates directories listed
  in the provided list.
- save_json(path: Path, data: dict): Saves the provided data in JSON format at the
  specified path.
- load_json(path: Path) -> ConfigBox: Loads data from a JSON file, returning it as a
  ConfigBox object.
- save_bin(data: Any, path: Path): Saves data in binary format at the specified path using
  joblib.
- load_bin(path: Path) -> Any: Loads and returns data from a binary file using joblib.
- get_size(path: Path) -> str: Returns the size of the file at the specified path in KB.

Each function is annotated for type checking. Logging is used to track operations.

Note:
- The module uses 'ConfigBox' from the 'box' package for convenient configuration access.
- It relies on a 'logger' from 'ml_project' for logging.
"""


import json
import os
from pathlib import Path
from typing import Any
import joblib
import yaml
from ensure import ensure_annotations
from box import ConfigBox
# Ensure BoxValueError is correctly imported from the 'box' package
from box.exceptions import BoxValueError
from ml_project import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.

    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r', encoding='utf-8') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info("yaml file: %s loaded successfully", path_to_yaml)
            return ConfigBox(content)
    except BoxValueError as exc:
        raise ValueError("yaml file is empty") from exc
    except Exception as exc:
        raise exc

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories from a list of directory paths.

    Args:
        path_to_directories (list): A list of paths to create.
        verbose (bool, optional): If True, logs the creation of each directory.
                                  Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info("created directory at: %s", path)

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves the given data in JSON format at the specified path.

    Args:
        path (Path): The path to save the JSON file.
        data (dict): The data to be saved in JSON format.
    """
    with open(path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    logger.info("json file saved at: %s", path)

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads data from a JSON file and returns it as a ConfigBox object.

    Args:
        path (Path): The path to the JSON file.

    Returns:
        ConfigBox: The contents of the JSON file as a ConfigBox object.
    """
    with open(path, 'r', encoding='utf-8') as f:
        content = json.load(f)
    logger.info("json file loaded successfully from: %s", path)
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data in binary format using joblib.

    Args:
        data (Any): The data to be saved.
        path (Path): The path to save the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info("binary file saved at: %s", path)

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads and returns data from a binary file using joblib.

    Args:
        path (Path): The path to the binary file.

    Returns:
        Any: The data loaded from the binary file.
    """
    data = joblib.load(path)
    logger.info("binary file loaded from: %s", path)
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of the file located at the specified path in kilobytes (KB).

    Args:
        path (Path): The path of the file.

    Returns:
        str: The size of the file in KB, rounded to the nearest kilobyte.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
