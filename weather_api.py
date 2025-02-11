import requests
import os
import logging
import streamlit as st

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

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.

    Parameters:
    celsius (float): Temperature in Celsius.

    Returns:
    float: Temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32

# Streamlit app
st.title("Weather Dashboard")

city = st.text_input("Enter the city name:")
if city:
    weather_data = get_weather(city)
    if "error" in weather_data:
        st.error(weather_data["error"])
    else:
        temp_celsius = weather_data["main"]["temp"]
        temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
        st.write(f"Temperature in {city}: {temp_celsius}°C / {temp_fahrenheit}°F")
        st.write(weather_data)
