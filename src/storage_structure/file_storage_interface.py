

class FileStorageInterface:
    """Interface for saving a file to a destination.
    
    Methods:
        save: Copies a file from src_path to the archive directory
    """
    def save(self, src_path: str, dest_root: str = "archive") -> str: ...