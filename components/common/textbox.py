import tkinter as tk
from . import utils

class TextBox(tk.LabelFrame):
    def __init__(self, container, label, on_change=lambda self: None, **kwargs):
        super().__init__(master=container, text=label, padx=8, pady=4, **kwargs)
        self.value = tk.StringVar(value="")
        self.value.trace_add("write", lambda name,index,mode: on_change(self))

        def paste_clipboard():
            self.value.set(self.clipboard_get())

        border, _ = utils.setup_border(self, tk.Button, text="\U0001F4CB", command=paste_clipboard)
        border._pack_props.update({"side": "left"})
        border, _ = utils.setup_border(self, tk.Entry, stretch=True, textvariable=self.value)
        border._pack_props.update({"side": "left"})
        utils.pack_children(self)
