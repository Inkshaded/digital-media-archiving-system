import tkinter as tk
from tkinter import messagebox

class ArchiveUI:
    def __init__(self, root, app_logic):
        self.root = root
        self.app_logic = app_logic

        self.root.title("Digital Media Archiving System")
        self.root.geometry("900x700")

        # ~~~ Widgets ~~~
        # -- Title --
        self.title_label = tk.Label(
            root, 
            text="Digital Media Archiving System", 
            font=("Arial", 18, "bold")
            )
        self.title_label.pack(pady=10)

        # -- Upload Button --
        self.upload_button = tk.Button(
            root, 
            text="Upload Files", 
            command=self.app_logic.upload_file
            )
        self.upload_button.pack()

        # -- View Log Button --
        self.view_log_button = tk.Button(
            root,
            text="View Log",
            command=lambda: self.app_logic.view_log(entries=20)
        )
        self.view_log_button.pack(pady=8)

        # -- Upload Listbox --
        self.file_listbox = tk.Listbox(
            root,
            width=50,
            height=1,
            selectmode=tk.SINGLE
        )
        self.file_listbox.pack(pady=12, padx=10, fill="x")

    # --- Helpers for controller ---
    def update_selected_file(self, file_path: str):
        """Replace the list contents with a single selected file path."""
        self.file_listbox.delete(0, tk.END)
        self.file_listbox.insert(tk.END, file_path)

    def show_log_window(self, rows, entries: int):
        """Render a read-only window showing the last N archive records."""
        win = tk.Toplevel(self.root)
        win.title(f"Archive Log (last {entries})")
        win.geometry("800x400")

        header = tk.Label(win, text=f"Last {entries} archive entries", font=("Arial", 12, "bold"))
        header.pack(pady=8)

        text = tk.Text(win, wrap="none", height=20)
        text.pack(fill="both", expand=True, padx=10, pady=10)

        # Scrollbars
        xscroll = tk.Scrollbar(win, orient="horizontal", command=text.xview)
        xscroll.pack(fill="x", side="bottom")
        text.configure(xscrollcommand=xscroll.set)

        yscroll = tk.Scrollbar(win, orient="vertical", command=text.yview)
        yscroll.pack(fill="y", side="right")
        text.configure(yscrollcommand=yscroll.set)

        # Populate
        if not rows:
            text.insert("1.0", "No records found.\n")
        else:
            cols = ["timestamp_iso", "src_path", "dest_path", "size_bytes"]
            line_header = " | ".join(cols)
            sep = "-" * len(line_header)
            text.insert("end", line_header + "\n")
            text.insert("end", sep + "\n")
            for r in rows:
                line = f"{r.get('timestamp_iso','')} | {r.get('src_path','')} | {r.get('dest_path','')} | {r.get('size_bytes','')}"
                text.insert("end", line + "\n")

        text.configure(state="disabled")
