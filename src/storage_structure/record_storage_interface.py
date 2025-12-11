from typing import Protocol, List, Dict

class RecordStorageInterface(Protocol):
    """Interface for recording archive operations.
    
    Methods:
        append: Appends a record to the archive record
        read_tail: Read a certain number of archival records detailing what has been most recnetly archived
    """
    def append(self, src_path: str, dest_path: str) -> None: ...
    def read_tail(self, n: int = 20) -> List[Dict[str, str]]: ...