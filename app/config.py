"""
Configuration constants for GTFS Differ.
"""

from dateutil import parser
from os import environ
from pathlib import Path
from urllib.parse import urlparse

script_path = Path(__file__).resolve()
project_root = script_path.parent.parent
github_workspace = environ.get("GITHUB_WORKSPACE")

WORKSPACE = Path(github_workspace) if github_workspace else project_root

GTFS_URL = "https://cdn.mbta.com/MBTA_GTFS.zip"
GTFS_DIR_PATH = WORKSPACE / Path("data/gtfs")
DIFF_GTFS_PATH = GTFS_DIR_PATH / Path("diff")
NEW_GTFS_PATH = GTFS_DIR_PATH / Path("new")
OLD_GTFS_PATH = GTFS_DIR_PATH / Path("old")
ZIP_GTFS_PATH = GTFS_DIR_PATH / Path(urlparse(GTFS_URL).path).name

LAST_MODIFIED = open("LAST_MODIFIED", encoding="utf-8").read().strip()
LAST_MODIFIED_DATETIME = parser.parse(LAST_MODIFIED)