import pandas as pd

def prepare_weather_data(raw_data):
    """Convert raw API data into a pandas DataFrame for easier processing."""
    data = {
        "City": raw_data["name"],
        "Temperature (°C)": raw_data["main"]["temp"],
        "Feels Like (°C)": raw_data["main"]["feels_like"],
        "Min Temp (°C)": raw_data["main"]["temp_min"],
        "Max Temp (°C)": raw_data["main"]["temp_max"],
        "Humidity (%)": raw_data["main"]["humidity"],
        "Weather": raw_data["weather"][0]["description"],
        "Wind Speed (m/s)": raw_data["wind"]["speed"],
    }
    return pd.DataFrame([data])
