import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score


# Load dataset
df = pd.read_csv("data/soil_crop_data.csv")

# Select features and target
X = df[["pH", "N", "P", "K", "temperature", "rainfall", "humidity"]]
y = df["yield"]

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

print(f"Yield Model R² Score: {score:.2f}")

# Save model
with open("models/yield_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Yield model saved successfully.")
