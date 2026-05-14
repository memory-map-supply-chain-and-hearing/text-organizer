import os
import tkinter as tk
from tkinter import ttk, filedialog
from .common import filesystem, textbox

class GetChat(tk.Frame):
    def __init__(self, container, on_change=lambda self: None, **kwargs):
        super().__init__(master=container, padx=8, pady=4, **kwargs)
        list_ais = ["ChatGPT", "Claude"]
        self.is_chat_link = tk.BooleanVar(value=False)
        self.selected_ai = tk.StringVar(value=list_ais[0])
        track_values = {option: {False: "", True: ""} for option in list_ais}

        def on_change_combobox(name, index, mode):
            current_ai = track_values[self.selected_ai.get()]
            if self.is_chat_link.get():
                text_chat_link.value.set(current_ai[True])
            else:
                folder_picker.path.set(current_ai[False])

        self.selected_ai.trace_add("write", on_change_combobox)
        checkbox_frame = tk.Frame(self)

        gap = 4
        for column in range(4):
            self.columnconfigure(column, pad=gap)
        # Allow last column to grow or shrink. All other columns remain as they are.
        self.columnconfigure(3, weight=1)
        for row in range(2):
            self.rowconfigure(row, pad=gap)

        def on_change_is_chat_link():
            if len(checkbox_frame.winfo_children()) != 0:
                for child in checkbox_frame.winfo_children():
                    child.pack_forget()
            # Require checkbox_frame sticky=ew
            if self.is_chat_link.get():
                text_chat_link.pack(fill="x")
            else:
                folder_picker.pack(fill="x")
            on_change_combobox("", 0, None)

        tk.Checkbutton(
            self,
            text="Link Chat",
            variable=self.is_chat_link,
            command=on_change_is_chat_link,
        ).grid(row=0, column=0, sticky="w")
        ttk.Separator(self, orient="vertical").grid(row=0, column=1, sticky="ns")
        tk.Label(self, text="Select AI:").grid(row=0, column=2, sticky="w")
        combobox = ttk.Combobox(
            self,
            textvariable=self.selected_ai,
            values=list_ais,
            state="readonly",
        )
        combobox.grid(row=0, column=3, sticky="w")

        checkbox_frame.grid(row=1, column=0, columnspan=4, sticky="ew")

        def on_change_folder_picker(picker):
            track_values[self.selected_ai.get()][self.is_chat_link.get()] = picker.path.get()

        folder_picker = filesystem.Picker(
            container=checkbox_frame,
            label="Upload",
            mode="folder",
            on_change=on_change_folder_picker,
        )
        # Update default values for picker, which is "No selection" whenever path is empty.
        for option in list_ais:
            track_values[option][False] = folder_picker.path.get()

        def on_change_chat_link(textbox_widget):
            track_values[self.selected_ai.get()][self.is_chat_link.get()] = textbox_widget.value.get()

        text_chat_link = textbox.TextBox(
            container=checkbox_frame,
            label="Enter Chat Link:",
            on_change=on_change_chat_link,
        )

        on_change_is_chat_link()
