import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

# Some common function that we used in the project!

# openning a yaml file
@ensure_annotations
def read_yml(path_to_yml: Path) -> ConfigBox:
    """Reads a yaml file and returns
    
    Args:
        pat_to_yaml (str): path ike input yaml file
        
    Raises:
        vlueError: if the yaml file is empty
        e: empty file
        
    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
  
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates a list of directories
    
    Args:
        path_to_directories (list): list of the path of the directories
        ignore_log (bool, optional): ignore the multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """Get size of the file
    
    Args:
        path (Path): path to the file
        
    Returns: 
        str: size of the file in KB
    """
    size_in_kb = os.path.getsize(path) / 1024
    return f"~ {size_in_kb} KB"
