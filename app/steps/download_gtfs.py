from httpx import Client
from typing import Self

from app.config import GTFS_URL, ZIP_GTFS_PATH
from app.step import Step

class DownloadGTFS(Step):
    """
    Downloads the GTFS feed from the URL and saves it to the file path.
    """
    def process(self) -> Self:
        """Processes the step."""
        with Client() as client:
            response = client.get(GTFS_URL)
            response.raise_for_status()

            with open(ZIP_GTFS_PATH, "wb") as file:
                return file.write(response.content)

        return self

    def success(self) -> bool:
        """Checks that the step was processed successfully."""
        return ZIP_GTFS_PATH.exists() and ZIP_GTFS_PATH.stat().st_size > 0

if __name__ == "__main__":
    DownloadGTFS().process().next()