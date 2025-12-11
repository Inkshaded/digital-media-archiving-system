import csv
import os
from datetime import datetime
from pathlib import Path
from typing import List, Dict
from storage_structure.record_storage_interface import RecordStorageInterface

class CsvRecordStore(RecordStorageInterface):
    """
    Appends archive records to a CSV file and can read the last N entries.
    Columns: timestamp_iso, src_path, dest_path, size_bytes
    """
    def __init__(self, log_path: str = "archive/records.csv"):
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.log_path.exists():
            with self.log_path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp_iso", "src_path", "dest_path", "size_bytes"])

    def append(self, src_path: str, dest_path: str) -> None:
        try:
            size_bytes = os.path.getsize(dest_path) if os.path.exists(dest_path) else 0
            ts = datetime.now().isoformat(timespec="seconds")
            with self.log_path.open("a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([ts, os.path.abspath(src_path), os.path.abspath(dest_path), size_bytes])
        except Exception as e:
            raise RuntimeError(f"Failed to append archive record: {e}") from e

    def read_tail(self, n: int = 20) -> List[Dict[str, str]]:
        """Return the last n rows as a list of dicts (newest last)."""
        if not self.log_path.exists():
            return []
        try:
            with self.log_path.open("r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                return rows[-n:] if n > 0 else rows
        except Exception as e:
            raise RuntimeError(f"Failed to read archive records: {e}") from e
