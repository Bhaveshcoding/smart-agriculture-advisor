import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score


# Load dataset
df = pd.read_csv("data/soil_crop_data.csv")

# Select features and target
X = df[["crop", "soil_type", "temperature", "rainfall", "humidity"]]
y = df["water_needed"]

# Encode categorical columns
crop_encoder = LabelEncoder()
soil_encoder = LabelEncoder()

X["crop"] = crop_encoder.fit_transform(X["crop"])
X["soil_type"] = soil_encoder.fit_transform(X["soil_type"])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
score = r2_score(y_test, y_pred)

print(f"Irrigation Model R² Score: {score:.2f}")

# Save model and encoders
with open("models/irrigation_model.pkl", "wb") as f:
    pickle.dump(
        {
            "model": model,
            "crop_encoder": crop_encoder,
            "soil_encoder": soil_encoder
        },
        f
    )

print("Irrigation model saved successfully.")
