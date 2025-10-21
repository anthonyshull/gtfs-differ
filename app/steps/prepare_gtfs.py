from shutil import copy2
from typing import Self
from zipfile import ZipFile

from app.config import NEW_GTFS_PATH, OLD_GTFS_PATH, ZIP_GTFS_PATH
from app.step import Step

class PrepareGTFS(Step):
    """
    Prepares the GTFS file by moving old files and unzipping the new file.
    """
    def process(self) -> Self:
        """Moves the old GTFS files and unzips the new GTFS file."""
        self.__move_gtfs()
        self.__unzip_gtfs()

        return self

    def success(self) -> bool:
        """Checks that new files have been placed in the new GTFS directory."""
        return any(NEW_GTFS_PATH.iterdir())

    def __move_gtfs(self) -> None:
        """Moves the contents of the old GTFS file to the old GTFS directory."""
        for item in NEW_GTFS_PATH.iterdir():
            if item.is_file():
                copy2(item, OLD_GTFS_PATH)
        
        for item in NEW_GTFS_PATH.iterdir():
            if item.is_file():
                item.unlink()

    def __unzip_gtfs(self) -> None:
        """Unzips the GTFS file into the new GTFS directory."""
        with ZipFile(ZIP_GTFS_PATH, 'r') as zip_ref:
            zip_ref.extractall(NEW_GTFS_PATH)

if __name__ == "__main__":
    PrepareGTFS().process().next()
