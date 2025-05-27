🌦️ Weather Rain Predictor App

A Machine Learning-powered web app that predicts whether it will rain in a given city, using real-time weather data from the OpenWeatherMap API.


🔍 Features

- 🌐 Real-time weather data using city name
- 🤖 Machine Learning model trained on weather features
- ☁️ Uses features like temperature, humidity, pressure, wind speed, cloud cover, and description
- 📊 Interactive Streamlit web interface
- 📦 Model built with `RandomForestClassifier` and deployed on Streamlit Cloud



 Live Demo

👉 [Click here to try the app] https://weather-predictor-boom.streamlit.app/ 


 Tech Stack

 Python
 Streamlit – UI
 Scikit-learn – ML model
 Pandas – Data manipulation
 Requests – API calls
 OpenWeatherMap API – Real-time weather data

File Section:

weather-predictor/
│
├── weather_app.py # Streamlit app
├── train_model.py # Training script for the model
├── weather_model.pkl # Saved ML model
├── requirements.txt # Dependencies
└── README.md # Project description


🪛 How it works
1. User enters a city name
2. App fetches current weather data via OpenWeatherMap API
3. The ML model makes a binary prediction: ☀️ No Rain or 🌧️ Rain
4. Streamlit displays the prediction and weather details

---

## 🙌 Author

Built by Bhavyasri Mudireddy  
Guided by ChatGPT  
Powered by real weather, real data, and ML 🚀

---

## 📬 Feedback

Have suggestions or want to contribute? Open an issue or submit a PR!


