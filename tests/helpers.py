from pathlib import Path
from shutil import rmtree


def clean_house():
    """Clean up some shit before we start."""
    if Path("tmp").exists():
        rmtree("tmp")
