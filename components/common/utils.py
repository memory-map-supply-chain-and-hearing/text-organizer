import tkinter as tk

def pack_children(container, padx=(6,0)):
    for widget in container.winfo_children():
        pack_info = {} if widget.winfo_manager() == "" else widget.pack_info()
        pack_info["padx"] = padx
        pack_info.update(getattr(widget, "_pack_props", {}))
        widget.pack(**pack_info)

def setup_border(container, widget_class, bg="white", thickness=1, stretch=False, **widget_kwargs):
    border = tk.Frame(container, bg=bg)
    border._pack_props = {}
    if stretch:
        border._pack_props.update({"fill": "x", "expand": True})
    widget = widget_class(border, **widget_kwargs)
    widget.pack(padx=thickness, pady=thickness, fill="x")
    return border, widget
