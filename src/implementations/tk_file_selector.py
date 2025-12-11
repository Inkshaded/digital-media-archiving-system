from tkinter import filedialog
from typing import Optional
from controller_interface.controller_interface import FileSelector


class TkFileSelector(FileSelector):
    """Selects a file using a Tkinter file dialog."""
    def select_file(self) -> Optional[str]:
        path = filedialog.askopenfilename(
            title="Select a File",
            filetypes=[("All Files", "*.*")]
        )
        return path or None