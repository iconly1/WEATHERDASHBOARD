import streamlit as st
from weather_api import get_weather
from data_processing import prepare_weather_data
from visualization import plot_temperature

st.set_page_config(page_title="Weather Dashboard", layout="wide")

st.title("🌦️ Python Weather Dashboard")

# Input for City
city = st.text_input("Enter a city name:", "New York")

if st.button("Get Weather"):
    # Fetch weather data from the API
    weather_data = get_weather(city)
    
    if "error" in weather_data:
        st.error("Could not fetch weather data. Please try again.")
    else:
        # Process and display data
        st.subheader(f"Weather in {city}")
        weather_df = prepare_weather_data(weather_data)
        st.dataframe(weather_df)
        
        # Plot temperature trend (dummy data for now)
        st.subheader("Temperature Trend")
        plot_temperature(weather_df)  # Replace with real trend data later

        st.success("Weather data loaded successfully!")
