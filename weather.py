# weather.py

import tkinter as tk
import requests
from PIL import Image, ImageTk
import io

class Weather(tk.Label):
    def __init__(self, parent, city="Your City", api_key="Your_API_Key"):
        super().__init__(parent)
        self.city = city  # Replace with your desired city
        self.api_key = api_key  # Replace with your actual API key
        self.temp = tk.StringVar(value="Loading...")
        self.icon = None
        # Set label properties such as font, color, and link the temperature text variable
        self.config(font=("Arial", 50, "bold"), fg="white", compound="top", textvariable=self.temp)
        self.update_weather()

    # Function to update the weather data every 10 minutes
    def update_weather(self):
        try:
            # Make a request to the weather API
            url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={self.city}"
            data = requests.get(url).json()
            temp = data["current"]["temp_c"]
            self.temp.set(f"{temp}°C")  # Update the temperature on the label
            icon_url = f"http:{data['current']['condition']['icon']}"  # Fetch the weather icon
            icon_data = requests.get(icon_url).content
            image = Image.open(io.BytesIO(icon_data))
            image = image.resize((50, 50), Image.Resampling.LANCZOS)  # Resize the icon
            self.icon = ImageTk.PhotoImage(image)  # Create a PhotoImage object
            self.config(image=self.icon)  # Set the icon on the label
        except:
            self.temp.set("Error")  # If an error occurs, display "Error"
        # Set the function to run every 10 minutes (600000 ms)
        self.after(600000, self.update_weather)

#root.mainloop()
