"""
Prepares the GTFS file for processing by unzipping its contents.
"""

from shutil import copy2
from zipfile import ZipFile

from app.config import NEW_GTFS_PATH, OLD_GTFS_PATH, ZIP_GTFS_PATH

def _move_gtfs() -> None:
    """Moves the contents of the old GTFS file to the old GTFS directory."""
    for item in NEW_GTFS_PATH.iterdir():
        if item.is_file():
            copy2(item, OLD_GTFS_PATH)
    
    for item in NEW_GTFS_PATH.iterdir():
        if item.is_file():
            item.unlink()

def _unzip_gtfs() -> None:
    """Unzips the GTFS file into the new GTFS directory."""
    with ZipFile(ZIP_GTFS_PATH, 'r') as zip_ref:
        zip_ref.extractall(NEW_GTFS_PATH)

def prepare_gtfs() -> None:
    """Prepares the GTFS file by moving old files and unzipping the new file."""
    _move_gtfs()
    _unzip_gtfs()

if __name__ == "__main__":
    prepare_gtfs()