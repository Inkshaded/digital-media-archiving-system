import os
import shutil
from storage_structure.file_storage_interface import FileStorageInterface


class LocalStorage(FileStorageInterface):
    """Saves files locally in the archive/ directory."""
    def save(self, src_path: str, dest_root: str = "archive") -> str:
        if not os.path.isfile(src_path):
            raise FileNotFoundError(src_path)
        os.makedirs(dest_root, exist_ok=True)
        dst_path = os.path.join(dest_root, os.path.basename(src_path))
        shutil.copyfile(src_path, dst_path)
        return dst_path