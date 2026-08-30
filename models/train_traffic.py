import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load traffic data
data = pd.read_csv("data/traffic_data.csv")

# Convert day to number
day_map = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

data["day_of_week"] = data["day_of_week"].map(day_map)

# Features
X = data[
    [
        "hour",
        "day_of_week",
        "vehicles",
        "avg_speed",
        "rain",
        "accidents"
    ]
]

# Target
y = data["traffic_level"]

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Save model
joblib.dump(model, "models/traffic_model.pkl")

print("Traffic model trained successfully!")
print("Saved as: models/traffic_model.pkl")
