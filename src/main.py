import tkinter as tk
from app import ArchiveApp
from implementations.tk_file_selector import TkFileSelector
from implementations.local_storage import LocalStorage
from implementations.csv_record_store import CsvRecordStore

def main():

    root = tk.Tk()
    ArchiveApp(root, selector=TkFileSelector(), 
               storage=LocalStorage(),
               records=CsvRecordStore(log_path="archive/records.csv"),)
    root.mainloop()

if __name__ == "__main__":
    main()