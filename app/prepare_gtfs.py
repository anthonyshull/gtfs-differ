"""
Prepares the GTFS file for processing by unzipping its contents.
"""

from shutil import copy2
from zipfile import ZipFile

from app.config import NEW_GTFS_PATH, OLD_GTFS_PATH, ZIP_GTFS_PATH

def move_gtfs() -> None:
    """Moves the contents of the old GTFS file to the old GTFS directory."""
    for item in NEW_GTFS_PATH.iterdir():
        if item.is_file():
            copy2(item, OLD_GTFS_PATH)
    
    for item in NEW_GTFS_PATH.iterdir():
        if item.is_file():
            item.unlink()

def unzip_gtfs() -> None:
    """Unzips the GTFS file into the new GTFS directory."""
    with ZipFile(ZIP_GTFS_PATH, 'r') as zip_ref:
        zip_ref.extractall(NEW_GTFS_PATH)

if __name__ == "__main__":
    move_gtfs()
    unzip_gtfs()