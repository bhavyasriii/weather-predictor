import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample enhanced dataset with extra features
data = [
    # [Temperature, Humidity, Pressure, Wind Speed, Cloud Cover, Description Category, Will Rain?]
    [28.0, 88, 1002, 3.4, 90, 1, 1],  # Rainy
    [26.5, 91, 1003, 2.8, 95, 1, 1],
    [29.0, 85, 1001, 3.9, 85, 1, 1],
    [22.0, 60, 1015, 1.5, 10, 0, 0],  # Clear
    [30.1, 45, 1011, 2.0, 5, 0, 0],
    [25.5, 75, 1013, 2.6, 20, 0, 0],
    [27.3, 68, 1008, 3.0, 30, 0, 0],
]

# Column names
columns = ["Temperature", "Humidity", "Pressure", "Wind Speed", "Clouds", "DescriptionCategory", "WillRain"]

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Features and label
X = df.drop("WillRain", axis=1)
y = df["WillRain"]

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the model
joblib.dump(model, "weather_model.pkl")
print("Enhanced model saved as weather_model.pkl")

