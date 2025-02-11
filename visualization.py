import matplotlib.pyplot as plt
import streamlit as st

def plot_temperature(df):
    """Plot a simple temperature trend using matplotlib."""
    fig, ax = plt.subplots()
    ax.bar(df.index, df["Temperature (°C)"], color='skyblue')
    ax.set_title("Temperature")
    ax.set_ylabel("Temperature (°C)")
    ax.set_xlabel("Time")
    st.pyplot(fig)
