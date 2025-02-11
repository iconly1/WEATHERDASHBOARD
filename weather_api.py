import requests

API_KEY = "your_api_key_here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch weather data for the given city."""
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
        print(f"Error fetching weather data: {e}")
        return {"error": "Could not fetch weather data"}
