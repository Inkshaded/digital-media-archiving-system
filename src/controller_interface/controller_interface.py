from typing import Protocol, Optional, List, Dict

class FileSelector(Protocol):
    """ Interface for selecting file path
    
    Methods:
        select_file: Opens a file selection dialog and returns a path or None.
    """
    def select_file(self) -> Optional[str]: ...