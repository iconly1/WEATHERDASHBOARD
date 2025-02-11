import pandas as pd

def prepare_weather_data(raw_data):
    """Convert raw API data into a pandas DataFrame for easier processing."""
    data = {
        "Temperature (°C)": raw_data['main']['temp'],
        "Feels Like (°C)": raw_data['main']['feels_like'],
        "Humidity (%)": raw_data['main']['humidity'],
        "Weather": raw_data['weather'][0]['description'],
    }
    return pd.DataFrame([data])
