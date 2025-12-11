import tkinter as tk
from tkinter import messagebox, filedialog
from ui.ui_start import ArchiveUI
from search.search_interface import SearchInterface
from storage_structure.file_storage_interface import FileStorageInterface
from storage_structure.record_storage_interface import RecordStorageInterface
from controller_interface import FileSelector

class ArchiveApp:
    """ Controller to connect GUI to file operations """
    def __init__(self, root: tk.Tk, selector: FileSelector, storage: FileStorageInterface, search: SearchInterface, records: RecordStorageInterface):
        self.root = root
        self.selector = selector
        self.storage = storage
        self.search = search
        self.records = records
        self.gui = ArchiveUI(root, app_logic=self)

    def upload_file(self):
        file_path = self.selector.select_file()
        if not file_path:
            messagebox.showinfo("No Selection", "No file was selected.")
            return
        
        #Update view
        self.gui.update_selected_file(file_path)

        try:
            saved_path = self.storage.save(file_path, dest_root="archive")
            # Log the archive operation
            self.records.append(src_path=file_path, dest_path=saved_path)
            messagebox.showinfo("Success", f"Archived file to:\n{saved_path}")
        except RuntimeError as e:
            messagebox.showerror("Error", str(e))

    
    def view_log(self, entries: int = 20):
        """Fetch the last N records and ask the UI to display them."""
        try:
            rows = self.records.read_tail(entries)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read log: {e}")
            return

        self.gui.show_log_window(rows, entries)

    def search_files(self, query: str):
        """Search for files in the archive folder matching a query."""
        if not query.strip():
            messagebox.showinfo("Search", "Please enter a search term.")
            return []

        results = self.search.search_files("archive", query)
        self.gui.display_search_results(results)
        return results