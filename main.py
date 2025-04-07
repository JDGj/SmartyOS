# main.py

import tkinter as tk
from clock import Clock
from weather import Weather
from PIL import Image, ImageTk
import os
import subprocess
import fullscreen

root = tk.Tk()
root.title("SmartyOs Dashboard")
root.geometry("700x600")

# Clock widget at the top
clock = Clock(root)
clock.pack(pady=20, anchor="w")

# Frame for the main content at the bottom with distribution (weather, apps, fingerprint)
bottom_frame = tk.Frame(root)
bottom_frame.pack(side="bottom", fill="x", pady=20)

# Left frame for the weather widget
left_frame = tk.Frame(bottom_frame)
left_frame.pack(side="left", anchor="w", padx=20)

# Weather widget
weather = Weather(left_frame, city="<CITY_NAME>", api_key="<API_KEY>")  # Replace <CITY_NAME> with the desired city and <API_KEY> with your actual API key
weather.pack(anchor="w")

# Central frame for app buttons
center_frame = tk.Frame(bottom_frame)
center_frame.pack(side="left", anchor="center", expand=True)

# Load app icons for the buttons
notepad_icon = Image.open("notepad.png").resize((50, 50), Image.Resampling.LANCZOS)
notepad_icon = ImageTk.PhotoImage(notepad_icon)

google_icon = Image.open("google.png").resize((50, 50), Image.Resampling.LANCZOS)
google_icon = ImageTk.PhotoImage(google_icon)

youtube_icon = Image.open("youtube.png").resize((50, 50), Image.Resampling.LANCZOS)
youtube_icon = ImageTk.PhotoImage(youtube_icon)

# Function to open the Notepad app
def open_notepad():
    subprocess.Popen(["python", "notepad.py"])

# Function to open the Google site
def open_google():
    subprocess.Popen(["python", "google.py"])

# Function to open YouTube
def open_youtube():
    subprocess.Popen(["python", "youtube.py"])

# Notepad button (icon only)
btn_notepad = tk.Button(center_frame, image=notepad_icon, command=open_notepad, bd=0)
btn_notepad.pack(side="left", padx=20)

# Google button (icon only)
btn_google = tk.Button(center_frame, image=google_icon, command=open_google, bd=0)
btn_google.pack(side="left", padx=20)

# YouTube button (icon only)
btn_youtube = tk.Button(center_frame, image=youtube_icon, command=open_youtube, bd=0)
btn_youtube.pack(side="left", padx=20)

# Right frame for the fingerprint icon
right_frame = tk.Frame(bottom_frame)
right_frame.pack(side="right", anchor="e", padx=20)

# Load and display fingerprint icon
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "fingerprint.png")
fingerprint_img = Image.open(image_path)
fingerprint_img = fingerprint_img.resize((100, 100), Image.Resampling.LANCZOS)
fingerprint_icon = ImageTk.PhotoImage(fingerprint_img)
fingerprint_label = tk.Label(right_frame, image=fingerprint_icon)
fingerprint_label.pack(anchor="e")

# Load fullscreen icons
fullscreen_icon, exit_fullscreen_icon = fullscreen.load_fullscreen_icons()

# Create the fullscreen button at the top-right
fullscreen.create_fullscreen_button(root, fullscreen_icon, exit_fullscreen_icon)

root.mainloop()
