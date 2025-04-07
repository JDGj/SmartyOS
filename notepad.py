# notepad.py

import tkinter as tk
from tkinter import ttk, filedialog as fd

root = tk.Tk()
root.title("Notepad")
root.geometry("700x500")
root.configure(bg="#1e1e1e")

# Create a notebook (tabbed view) where we will add tabs for text editing
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=10, pady=10)

style = ttk.Style()
style.theme_use("default")
style.configure("TNotebook", background="#2d2d2d", borderwidth=0)
style.configure("TNotebook.Tab", background="#333333", foreground="#ffffff", padding=10)
style.map("TNotebook.Tab", background=[("selected", "#1e1e1e")])

tabs = []

# Function to create a new tab for editing with an optional initial content
def create_tab(content=""):
    frame = tk.Frame(notebook, bg="#1e1e1e")
    text_area = tk.Text(frame, wrap="word", bg="#1e1e1e", fg="white", insertbackground="white", undo=True)
    text_area.insert("1.0", content)
    text_area.pack(expand=True, fill="both")
    notebook.add(frame, text="Untitled")  # Default tab name
    notebook.select(frame)
    tabs.append(text_area)

# Function to save the content of the current tab to a file
def save_file(event=None):
    current_tab = notebook.index(notebook.select())
    text_area = tabs[current_tab]
    file_path = fd.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])  # Save file dialog
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get("1.0", tk.END))
        notebook.tab(current_tab, text=file_path.split("/")[-1])  # Update the tab with the saved file name

# Function to open a file and load its content into a new tab
def open_file(event=None):
    file_path = fd.askopenfilename(filetypes=[("Text Files", "*.txt")])  # Open file dialog
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        create_tab(content)
        notebook.tab("current", text=file_path.split("/")[-1])  # Set the opened file name as tab title

# Function to create a new empty tab
def new_tab(event=None):
    create_tab()

btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="New Tab", command=new_tab, bg="#333", fg="white").pack(side="left", padx=5)
tk.Button(btn_frame, text="Open", command=open_file, bg="#333", fg="white").pack(side="left", padx=5)
tk.Button(btn_frame, text="Save", command=save_file, bg="#333", fg="white").pack(side="left", padx=5)

root.bind("<Control-s>", save_file)  # Bind the save function to Ctrl+S
root.bind("<Control-o>", open_file)  # Bind the open function to Ctrl+O
root.bind("<Control-n>", new_tab)   # Bind the new tab function to Ctrl+N

create_tab()  # Create the first tab when the app starts

root.mainloop()  # Start the Tkinter event loop to run the application
