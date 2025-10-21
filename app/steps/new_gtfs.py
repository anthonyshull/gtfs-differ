from dateutil import parser

from httpx import Client

from app.config import GTFS_URL, LAST_MODIFIED_DATETIME
from app.step import Step

class NewGTFS(Step):
    """
    Checks the last modified time of a GTFS feed file.
    """
    def process(self) -> None:
        """There is no processing step"""
        pass

    def success(self) -> bool:
        """Returns True if the remote file has been modified since the last check."""
        with Client() as client:
            response = client.head(GTFS_URL)
            last_modified = response.headers.get("Last-Modified")

            if last_modified:
                last_modified_datetime = parser.parse(last_modified)

                print(f"Last-Modified: {last_modified_datetime.isoformat()}")

                return last_modified_datetime > LAST_MODIFIED_DATETIME

if __name__ == "__main__":
    step = NewGTFS()
    step.next()
