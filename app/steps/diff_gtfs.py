from hashlib import sha256
from pathlib import Path
from typing import Self

from app.config import DIFF_GTFS_PATH, NEW_GTFS_PATH, OLD_GTFS_PATH
from app.step import Step

class DiffGTFS(Step):
    """
    Creates a diff between the old and new GTFS feed files.
    """
    def process(self) -> Self:
        """Processes the step."""
        DIFF_GTFS_PATH.mkdir(parents=True, exist_ok=True)
        (DIFF_GTFS_PATH / Path(".gitkeep")).touch()

        for item in DIFF_GTFS_PATH.iterdir():
            if item.is_file():
                item.unlink()

        for new_file in NEW_GTFS_PATH.iterdir():
            old_file = OLD_GTFS_PATH / new_file.name
            if old_file.exists():
                self.__diff_gtfs_files(new_file, old_file)

        return self

    def success(self) -> bool:
        """Checks that the diff files have been created."""
        # return any(DIFF_GTFS_PATH.iterdir())
        return True

    def __diff_gtfs_files(self, new: Path, old: Path) -> None:
        new_lines = self.__hash_lines(new)
        old_lines = self.__hash_lines(old)

        added = {h: new_lines[h] for h in new_lines if h not in old_lines}
        if added:
            added_path = DIFF_GTFS_PATH / Path(new.stem)
            added_path.mkdir(parents=True, exist_ok=True)
            self.__write(added, added_path / Path(f"added{new.suffix}"))
        
        removed = {h: old_lines[h] for h in old_lines if h not in new_lines}
        if removed:
            removed_path = DIFF_GTFS_PATH / Path(old.stem)
            removed_path.mkdir(parents=True, exist_ok=True)
            self.__write(removed, DIFF_GTFS_PATH / Path(old.stem) / Path(f"removed{old.suffix}"))

    def __hash_line(self, line: str) -> str:
        return sha256(line.encode("utf-8")).hexdigest()

    def __hash_lines(self, path: Path) -> dict[str, str]:
        with path.open("r", encoding="utf-8") as f:
            lines = f.readlines()[1:]

            return {self.__hash_line(line.strip()): line.strip() for line in lines if line.strip()}

    def __write(self, lines: dict[str, str], path: Path) -> None:
        with path.open("w", encoding="utf-8") as f:
            for line in lines.values():
                f.write(f"{line}\n")

if __name__ == "__main__":
    DiffGTFS().process().next()
