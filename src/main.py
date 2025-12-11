import tkinter as tk
from app import ArchiveApp
from implementations.tk_file_selector import TkFileSelector
from implementations.local_storage import LocalStorage
from implementations.local_search import LocalSearch
from implementations.csv_record_store import CsvRecordStore
from controller_interface.user_state import ReaderState, ArchivistState

def main():

    root = tk.Tk()

    # Default role is Reader
    role = ReaderState()

    ArchiveApp(root, selector=TkFileSelector(), 
               storage=LocalStorage(),
               search=LocalSearch(),
               records=CsvRecordStore(log_path="archive/records.csv"),
               role=role
               )
    root.mainloop()

if __name__ == "__main__":
    main()