import requests
import os
import logging

API_KEY = os.getenv("OPENWEATHER_API_KEY", "your_default_api_key_here")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

logging.basicConfig(level=logging.INFO)

def get_weather(city):
    """
    Fetch weather data for the given city.

    Parameters:
    city (str): The name of the city to fetch weather data for.

    Returns:
    dict: A dictionary containing weather data or an error message.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching weather data: {e}")
        return {"error": "Could not fetch weather data"}
