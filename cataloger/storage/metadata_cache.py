import json
from dataclasses import asdict
from pathlib import Path

from cataloger.metadata.metadata_record import MetadataRecord


class MetadataCache:
    """
    Stores MetadataRecord objects as JSON files.
    """

    def __init__(self):
        self.cache_dir = Path("cataloger/storage/cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _cache_file(self, isbn: str) -> Path:
        return self.cache_dir / f"{isbn}.json"

    def get(self, isbn: str):
        path = self._cache_file(isbn)

        if not path.exists():
            return None

        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return MetadataRecord(**data)

    def save(self, metadata: MetadataRecord):
        if not metadata.isbn:
            return

        path = self._cache_file(metadata.isbn)

        with path.open("w", encoding="utf-8") as file:
            json.dump(asdict(metadata), file, indent=2)