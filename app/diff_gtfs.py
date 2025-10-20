"""
Creates a diff between the old and new GTFS feed files.
"""

from pathlib import Path

from app.config import NEW_GTFS_PATH, OLD_GTFS_PATH

def diff_gtfs_files(new: Path, old: Path) -> None:
    pass

def diff_gtfs() -> None:
    for new_file in NEW_GTFS_PATH.iterdir():
        old_file = OLD_GTFS_PATH / new_file.name
        if old_file.exists():
            diff_gtfs_files(new_file, old_file)

if __name__ == "__main__":
    diff_gtfs()