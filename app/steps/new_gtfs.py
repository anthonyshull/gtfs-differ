from dateutil import parser
from typing import Self

from httpx import Client

from app.config import GTFS_URL, LAST_MODIFIED, LAST_MODIFIED_PATH
from app.step import Step

class NewGTFS(Step):
    """
    Checks the last modified time of a GTFS feed file.
    """
    def process(self) -> Self:
        """Get the Last-Modified header from the GTFS URL and store it."""
        with Client() as client:
            response = client.head(GTFS_URL)
            self.__last_modified = response.headers.get("Last-Modified")

            open(LAST_MODIFIED_PATH, "w").write(self.__last_modified)

        return self

    def success(self) -> bool:
        """Returns True if the remote file has been modified since the last check."""
        if self.__last_modified:
            return parser.parse(self.__last_modified) > parser.parse(LAST_MODIFIED)

if __name__ == "__main__":
    NewGTFS().process().next()
