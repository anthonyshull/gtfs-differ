"""
Checks the last modified time of a GTFS feed file.
"""

from httpx import Client

from app.config import GTFS_URL, LAST_MODIFIED_DATETIME
from app.helpers import maybe_continue, parse_last_modified

def new_gtfs() -> bool:
    """Returns True if the remote file has been modified since the last check."""
    with Client() as client:
        response = client.head(GTFS_URL)
        last_modified = response.headers.get("Last-Modified")

        if last_modified:
            last_modified_datetime = parse_last_modified(last_modified)

            return last_modified_datetime > LAST_MODIFIED_DATETIME

if __name__ == "__main__":
    maybe_continue(not new_gtfs())
