import os
import tkinter as tk
from tkinter import filedialog
from . import utils

class Picker(tk.LabelFrame):
    def __init__(self, container, label, mode, accept=[], on_change=lambda self: None, **kwargs):
        super().__init__(master=container, text=label, padx=8, pady=4, **kwargs)
        if mode == "file":
            options = ["File"]
        elif mode == "folder":
            options = ["Folder"]
        elif mode == "both":
            options = ["File", "Folder"]
        else:
            raise Exception("Invalid mode!")
        self.current_option = tk.StringVar(value=options[0])
        self.path = tk.StringVar(value="")

        def on_change_path(name, index, mode):
            if not self.path.get():
                self.path.set("No selection")

        self.path.trace_add("write", on_change_path)
        on_change_path("", 0, None)

        for option in options:
            tk.Radiobutton(
                self,
                text=option,
                variable=self.current_option,
                value=option
            ).pack(side="left")

        def browse():
            if self.current_option.get() == "File":
                path = filedialog.askopenfilename(filetypes=accept)
            elif self.current_option.get() == "Folder":
                path = filedialog.askdirectory()
            if path:
                self.path.set(path)
            on_change(self)

        def copy_path():
            self.clipboard_clear()
            self.clipboard_append(self.path.get())

        border, _ = utils.setup_border(self, tk.Button, text="Browse", command=browse)
        border.pack(side="left")
        border, _ = utils.setup_border(self, tk.Button, text="\U00002750", command=copy_path)
        border.pack(side="left")
        tk.Label(self, textvariable=self.path, anchor="w").pack(side="left")
        utils.pack_children(self)
