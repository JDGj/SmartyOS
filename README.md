# SmartyOS

A simple OS (with time, weather, a simple notepad, google link and youtube link, fingerprint and fullscreen mode) using python, with comments

## How to Start

# App Setup and Configuration Guide

This app integrates various features such as weather updates, a notepad, and more. Follow the instructions below to set up the app and get it running.

## Prerequisites

Before running the app, ensure you have the following installed:

- Python 3.x
- `pip` (Python package manager)

You will also need the following Python libraries:

- `tkinter` (for the GUI)
- `requests` (for making HTTP requests)
- `Pillow` (for image processing)

You can install the required libraries by running the following command:

```bash
pip install requests Pillow
```

## Setting Up
1. Weather API Key:
To use the weather feature, you need to obtain an API key from WeatherAPI.
Once you have your API key, follow these steps:
	Open the weather.py file.
	Find the following line:
		self.api_key = "YOUR_API_KEY_HERE"
	Replace "YOUR_API_KEY_HERE" with your actual WeatherAPI key (weather.py and also on main.py).

2. City Configuration:
By default, the city is set to "Your City". To change it:
	Open the weather.py file.
	Find the following line:
		self.city = "Your City"
	Replace "Your City" with your desired city (e.g., "New York", "London") (weather.py and also on main.py).

Running the App
After setting up the API keys and configuring the city:
	Open a terminal or command prompt.
	Navigate to the directory where your app files are located.
	Run the app by executing:
		python main.py
This will launch the graphical user interface (GUI), and the weather information, notepad functionality, and other features will be displayed.

## File Descriptions
Here is a brief overview of the files:
	main.py: The main entry point of the app, where the user interface and app widgets are created.
	clock.py: Contains the logic to display the current time in the app.
	fullscreen.py: Provides functionality to toggle between fullscreen and windowed modes.
	google.py: Opens the Google website.
	notepad.py: A simple notepad app that allows the user to create, save, and open text files.
	weather.py: Displays the current weather for a specified city.

## Troubleshooting
	Weather not loading: If the weather data is not loading, check that your API key is correct and ensure the city name is accurate.
	Missing libraries: If you encounter errors related to missing libraries, install them using:
		pip install requests Pillow
	Other issues: If you encounter any other issues, refer to the Python documentation or consult the app's source code.