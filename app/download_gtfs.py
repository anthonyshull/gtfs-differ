"""
Downloads the GTFS feed from a given URL and saves it to a specified file path.
"""

from httpx import Client

from app.config import GTFS_URL, ZIP_GTFS_PATH
from app.helpers import maybe_continue

def download_gtfs() -> int:
    """Downloads the GTFS feed from the URL and saves it to the file path."""

    with Client() as client:
        response = client.get(GTFS_URL)
        response.raise_for_status()

        with open(ZIP_GTFS_PATH, "wb") as file:
            return file.write(response.content)

if __name__ == "__main__":
    maybe_continue(download_gtfs() > 0)