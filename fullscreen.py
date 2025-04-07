# fullscreen.py

import tkinter as tk
from PIL import Image, ImageTk

# Function to toggle fullscreen mode
def toggle_fullscreen(root, fullscreen_icon, exit_fullscreen_icon, fullscreen_button):
    current_state = root.attributes("-fullscreen")
    root.attributes("-fullscreen", not current_state)

    # Switch the icon when fullscreen is toggled on or off
    if not current_state:
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        fullscreen_button.config(image=exit_fullscreen_icon)  # Changes icon to fullscreen-out
    else:
        root.geometry("700x600")
        fullscreen_button.config(image=fullscreen_icon)  # Changes icon to fullscreen-in

# Function to create the fullscreen button and keep it always on the top-right
def create_fullscreen_button(root, fullscreen_icon, exit_fullscreen_icon):
    fullscreen_button = tk.Button(root, image=fullscreen_icon, command=lambda: toggle_fullscreen(root, fullscreen_icon, exit_fullscreen_icon, fullscreen_button), bd=0, highlightthickness=0)
    fullscreen_button.place(relx=1.0, rely=0.0, x=-10, y=10, anchor="ne")  # Positions it at the top-right

# Load fullscreen icons
def load_fullscreen_icons():
    # Replace sensitive paths with placeholders
    fullscreen_icon = Image.open("fullscreen.png").resize((30, 30), Image.Resampling.LANCZOS)
    exit_fullscreen_icon = Image.open("fullscreen-out.png").resize((30, 30), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(fullscreen_icon), ImageTk.PhotoImage(exit_fullscreen_icon)
