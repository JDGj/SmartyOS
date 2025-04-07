# clock.py

import tkinter as tk
import time

# Creating a Clock class that inherits from tkinter Label
class Clock(tk.Label):
    def __init__(self, parent, *args, **kwargs):
        # Initializing the Label with the provided arguments
        super().__init__(parent, *args, **kwargs)
        # Setting initial text, font, and color for the label
        self.config(text="00:00:00", font=("Arial", 50, "bold"), fg="white")
        # self.config(text="00:00", font=("Arial", 50, "bold"), fg="white") # Alternative format
        self.pack(pady=50)
        # Starting the clock update method
        self.update_clock()

    # Method to update the time every second
    def update_clock(self):
        # Getting the current time in the format HH:MM:SS
        current_time = time.strftime("%H:%M:%S")
        # current_time = time.strftime("%H:%M") # Alternative format
        # Updating the label with the current time
        self.config(text=current_time)
        # Calling the update_clock method every 1000 milliseconds (1 second)
        self.after(1000, self.update_clock)

# root.mainloop()  # Uncomment this to start the Tkinter event loop
