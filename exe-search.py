import os
import tkinter as tk
from tkinter import filedialog

def search_files():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    folder_selected = filedialog.askdirectory(initialdir = "/", title = "Select a folder")
    exe_files = []
    for subdir, dirs, files in os.walk(folder_selected):
        for file in files:
            if file.endswith(".exe"):
                exe_files.append(os.path.join(subdir, file))

    result_label = tk.Label(root, text="Results:")
    result_label.pack()
    result_list = tk.Listbox(root)
    result_list.pack()
    for file in exe_files:
        result_list.insert("end", file)
    root.mainloop()

search_files()
