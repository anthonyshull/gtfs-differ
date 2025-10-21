"""
Configuration constants for GTFS Differ.
"""

from dateutil import parser
from os import environ
from pathlib import Path
from urllib.parse import urlparse

_script_path = Path(__file__).resolve()
_project_root = _script_path.parent.parent
_github_workspace = environ.get("GITHUB_WORKSPACE")

WORKSPACE = Path(_github_workspace) if _github_workspace else _project_root

GTFS_DIR_PATH = WORKSPACE / Path("data/gtfs")
DIFF_GTFS_PATH = GTFS_DIR_PATH / Path("diff")
NEW_GTFS_PATH = GTFS_DIR_PATH / Path("new")
OLD_GTFS_PATH = GTFS_DIR_PATH / Path("old")
ZIP_GTFS_PATH = GTFS_DIR_PATH / Path(urlparse(GTFS_URL).path).name

LAST_MODIFIED = open("LAST_MODIFIED", encoding="utf-8").read().strip()
LAST_MODIFIED_DATETIME = parser.parse(LAST_MODIFIED)

GTFS_URL = environ.get("GTFS_URL")