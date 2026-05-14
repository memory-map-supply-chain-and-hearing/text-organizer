import tkinter as tk

class RadioGroup(tk.LabelFrame):
    def __init__(self, container, label, options, on_change=lambda self: None, **kwargs):
        super().__init__(master=container, text=label, padx=8, pady=4, **kwargs)
        self.columnconfigure(0, weight=1)
        self.current_option = tk.StringVar(value=options[0])
        for option in options:
            tk.Radiobutton(
                self,
                text=option,
                variable=self.current_option,
                value=option,
                command=lambda: on_change(self),
                # Keep text left-aligned
                anchor="w",
            ).pack(fill="x")
            # Expand clickable area to full width of radio group

