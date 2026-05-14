import tkinter as tk
from tkinter import ttk, filedialog, messagebox, font
import importlib
from components.common import radiogroup, textbox, filesystem
from components import ai

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text Organizer")
        self.resizable(False, False)
        self._build_styles()
        self._build_ui()

    def _build_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure(
            "TCombobox",
            fieldbackground="black",
            background="black",
            foreground="white"
        )
        style.map(
            "TCombobox",
            fieldbackground=[("readonly", "black")],
            foreground=[("readonly", "white")],
            background=[("readonly", "white")],
            selectbackground=[("readonly", "black")],
            selectforeground=[("readonly", "white")],
        )
        self.option_add("*Button.cursor", "hand2")
        self.option_add("*Background", "black")
        self.option_add("*Foreground", "white")
        self.option_add("*Radiobutton.activeBackground", "black")
        self.option_add("*Radiobutton.activeForeground", "white")
        self.option_add("*Checkbutton.activeBackground", "black")
        self.option_add("*Checkbutton.activeForeground", "white")
        self.default_font = font.Font(family="Segoe UI", weight="bold")
        self.option_add("*Font", self.default_font)

    def _build_ui(self):
        def unfocus(event):
            try:
                cls = self.tk.call("winfo", "class", event.widget)
                if cls in ("Entry", "TEntry", "TCombobox", "Listbox"):
                    return
            except:
                pass
            outer.focus_set()

        outer = tk.Frame(self, width=600, height=600, padx=32, pady=28)
        outer.bind_all("<Button-1>", unfocus)
        outer.pack_propagate(False)
        outer.pack()

        tk.Label(outer, text="Text Organizer").pack(pady=(0, 20))

        def on_change_import_mode(group):
            if len(mode_container.winfo_children()) != 0:
                for child in mode_container.winfo_children():
                    child.pack_forget()
            if group.current_option.get() == "Google Doc":
                text_doc_id.pack(fill="x")
            elif group.current_option.get() == "File System":
                file_system_upload.pack(fill="x")
            elif group.current_option.get() == "AI":
                ai_chats.pack(fill="x")

        import_mode = radiogroup.RadioGroup(
            container=outer,
            label="Import",
            options=["Google Doc", "File System", "AI"],
            on_change=on_change_import_mode,
        )
        import_mode.pack(pady=(0, 12))

        mode_container = tk.Frame(outer)
        mode_container.pack(fill="x")

        def on_change_doc_id(textbox_widget):
            pass

        text_doc_id = textbox.TextBox(
            container=mode_container,
            label="Enter Doc ID",
            on_change=on_change_doc_id,
        )

        def on_change_file_system_upload(picker):
            pass

        file_system_upload = filesystem.Picker(
            container=mode_container,
            label="Upload",
            mode="both",
            accept=[
                ("Text", "*.txt"),
                ("Markdown", "*.md"),
                ("HTML", "*.html"),
                ("JSON", "*.json"),
            ],
            on_change=on_change_file_system_upload,
        )

        def on_change_ai_chats(chats):
            pass

        ai_chats = ai.GetChat(
            container=mode_container,
            on_change=on_change_ai_chats,
        )

        on_change_import_mode(import_mode)

        def go():
            if import_mode.current_option.get() == "Google Doc":
                pass
            elif import_mode.current_option.get() == "File System":
                pass
            elif import_mode.current_option.get() == "AI":
                pass

        tk.Button(
            master=outer,
            text="Go",
            bg="green",
            fg="black",
            command=go,
       ).pack(fill="x", pady=20)

if __name__ == "__main__":
    App().mainloop()

