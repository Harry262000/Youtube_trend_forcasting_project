import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

def create_project_structure(list_of_files, project_name):
    for filepath in list_of_files:
        filepath = Path(filepath)

        if filepath.parent != "":
            os.makedirs(filepath.parent, exist_ok=True)
            logging.info(f"Creating directory: {filepath.parent} for the file {filepath.name}")

        if not filepath.exists():
            with open(filepath, 'w') as f:
                pass
            logging.info(f"Created empty file: {filepath}")
        else:
            logging.info(f"File already exists: {filepath}")

project_name = "textSummarizer"

list_of_files = [
    ".github.com/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "README.md",
    "LICENSE",
    "setup.py",
    "research/trails.py",
    "research/trails.ipynb",
    "tests/test_trails.py",
    "tests/test_trails.ipynb",
    "requirements.txt",
    "environment.yml",
]

create_project_structure(list_of_files, project_name)
