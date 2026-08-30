import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

data = pd.read_csv("data/accident_data.csv")

# Convert text columns to numbers
for column in ["location", "road_condition", "vehicle_type"]:
    encoder = LabelEncoder()
    data[column] = encoder.fit_transform(data[column])
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

data = pd.read_csv("data/accident_data.csv")

# Convert text columns to numbers
text_columns = [
    "location",
    "road_condition",
    "visibility",
    "vehicle_type",
    "severity"
]

for column in text_columns:
    encoder = LabelEncoder()
    data[column] = encoder.fit_transform(data[column])

X = data[
    [
        "hour",
        "vehicles_nearby",
        "avg_speed",
        "rain",
        "traffic_level",
        "location",
        "road_condition",
        "visibility",
        "vehicle_type",
        "severity",
        "nearby_help"
    ]
]

y = data["accident_detected"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

joblib.dump(model, "models/accident_model.pkl")

print("Accident model trained successfully!")
print("Saved: models/accident_model.pkl")
print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))
X = data[
    [
        "hour",
        "vehicles_nearby",
        "avg_speed",
        "rain",
        "traffic_level",
        "location",
        "road_condition",
        "visibility",
        "vehicle_type",
        "nearby_help"
    ]
]

y = data["accident_detected"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

joblib.dump(model, "models/accident_model.pkl")

print("Accident model trained successfully!")
print("Saved: models/accident_model.pkl")
print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))
