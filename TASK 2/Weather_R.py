import os
import requests  # Import library to request from API
from datetime import datetime  # Import library to get the current date and time

# Generated API Key (make sure to keep this private)

API_KEY = os.getenv(Weather_Api_Key)


# Base URL for the OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

############################################################

# Fetch Data Function
def Get_weather(city):
    
    

    # Parameters for the API request
    params = {
        "q": city,                                                  # City name
        "appid": API_KEY,                                           # API key
        "units": "metric"                                           # Use metric units (Celsius)
    }


#####################################################################################
    try:
        # Send a GET request to the API
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()                                 # Raise an error for bad status codes

        
        weather_data = response.json()                              # Parse the JSON response

        # Extract all Data from the Variable
        temperature = weather_data["main"]["temp"]                  # Extract Temperature Data
        weather = weather_data["weather"][0]["description"]         # Extract Weather Data
        humidity = weather_data["main"]["humidity"]                 # Extract Humidity

        # Get the current date and time
        timefort = datetime.now().strftime("%Y-%m-%d %H:%M:%S")     # Time display format

        # Fetch weather data of city and append it to file

        with open("weather_log.txt", "a") as file:                   # Append Data in file
             file.write(f"At {timefort}, {city}: Temperature is {temperature}°C, Weather is {weather}, Humidity is {humidity}%\n")

        # Display the weather details
        print(f"Time: {timefort}")                                    # Display Time 
        print(f"Location: {city}")
        print(f"Temperature: {temperature}°C")                        
        print(f"weather: {weather.capitalize()}")          
        print(f"Humidity: {humidity}%")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

############################################################

# Main program
while True: 
    city = input("What City are you looking at? ")  # Ask user for the city's name
    Get_weather(city)  # Fetch and display weather data