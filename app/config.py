"""
Configuration constants for GTFS Differ.
"""

from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

script_path = Path(__file__).resolve()
project_root = script_path.parent.parent

GTFS_URL = "https://cdn.mbta.com/MBTA_GTFS.zip"
GTFS_DIR_PATH = project_root / Path("data/gtfs")
ZIP_GTFS_PATH = GTFS_DIR_PATH / Path(urlparse(GTFS_URL).path).name
NEW_GTFS_PATH = GTFS_DIR_PATH / Path("new")
OLD_GTFS_PATH = GTFS_DIR_PATH / Path("old")

LAST_MODIFIED = open("LAST_MODIFIED", encoding="utf-8").read().strip()
LAST_MODIFIED_DATETIME = datetime.strptime(LAST_MODIFIED, "%a, %d %b %Y %H:%M:%S %Z")