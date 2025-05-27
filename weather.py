import streamlit as st
import requests
import pandas as pd
import joblib
import os

# Load the enhanced model
model = joblib.load("weather_model.pkl")


import os
API_KEY = os.environ.get("WEATHER_API_KEY")

# Description to category mapping
desc_map = {
    "clear sky": 0,
    "few clouds": 0,
    "scattered clouds": 0,
    "broken clouds": 0,
    "shower rain": 1,
    "rain": 1,
    "thunderstorm": 1,
    "snow": 1,
    "mist": 1,
    "overcast clouds": 1,
    "light rain": 1,
    "moderate rain": 1
}

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if "main" not in data:
        return None, None

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind_speed = data["wind"]["speed"]
    clouds = data["clouds"]["all"]
    description = data["weather"][0]["description"]
    desc_cat = desc_map.get(description.lower(), 0)

    features = [temp, humidity, pressure, wind_speed, clouds, desc_cat]
    return features, data

# Streamlit UI
st.set_page_config(page_title="⛈️ Weather Rain Predictor", layout="centered")
st.title("⛈️ Weather Rain Predictor (Enhanced)")
city = st.text_input("🔍 Enter a city name:")

if city:
    features, raw = get_weather(city)
    if features:
        input_df = pd.DataFrame([features], columns=["Temperature", "Humidity", "Pressure", "Wind Speed", "Clouds", "DescriptionCategory"])
        pred = model.predict(input_df)[0]

        st.markdown("---")
        st.subheader(f"🌍 Weather in **{city.title()}**")
        st.markdown(f"### {'🌧️ Rain Expected' if pred == 1 else '☀️ No Rain Expected'}")

        # Display metrics
        col1, col2 = st.columns(2)
        col1.metric("🌡️ Temperature (°C)", f"{features[0]}°C")
        col2.metric("💧 Humidity (%)", f"{features[1]}%")
        col1.metric("⚡Pressure (hPa)", f"{features[2]}")
        col2.metric("💨 Wind Speed (m/s)", f"{features[3]}")
        col1.metric("☁️ Cloud Cover (%)", f"{features[4]}")
        col2.metric("📝 Description", raw["weather"][0]["description"].title())
        st.markdown("---")
    else:
        st.error("😒😒 Could not fetch weather data for that city.")
