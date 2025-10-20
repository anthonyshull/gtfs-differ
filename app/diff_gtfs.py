"""
Creates a diff between the old and new GTFS feed files.
"""

from hashlib import sha256
from pathlib import Path

from app.config import DIFF_GTFS_PATH, NEW_GTFS_PATH, OLD_GTFS_PATH

def diff_gtfs_files(new: Path, old: Path) -> None:
    new_lines = hash_lines(new)
    old_lines = hash_lines(old)

    added = {h: new_lines[h] for h in new_lines if h not in old_lines}
    if added:
        added_path = DIFF_GTFS_PATH / Path(new.stem)
        added_path.mkdir(parents=True, exist_ok=True)
        write(added, added_path / Path(f"added.{new.suffix}"))
    
    removed = {h: old_lines[h] for h in old_lines if h not in new_lines}
    if removed:
        removed_path = DIFF_GTFS_PATH / Path(old.stem)
        removed_path.mkdir(parents=True, exist_ok=True)
        write(removed, DIFF_GTFS_PATH / Path(old.stem) / Path(f"removed.{old.suffix}"))

def diff_gtfs() -> None:
    for new_file in NEW_GTFS_PATH.iterdir():
        old_file = OLD_GTFS_PATH / new_file.name
        if old_file.exists():
            diff_gtfs_files(new_file, old_file)

def hash_line(line: str) -> str:
    return sha256(line.encode("utf-8")).hexdigest()

def hash_lines(path: Path) -> dict[str, str]:
    with path.open("r", encoding="utf-8") as f:
        lines = f.readlines()[1:]

        return {hash_line(line.strip()): line.strip() for line in lines if line.strip()}

def write(lines: dict[str, str], path: Path) -> None:
    with path.open("w", encoding="utf-8") as f:
        for line in lines.values():
            f.write(f"{line}\n")

if __name__ == "__main__":
    diff_gtfs()