import pickle
import numpy as np

MAX_YIELD = {
    "rice": 9000,
    "wheat": 8000,
    "maize": 12000,
    "soybean": 3500,
    "cotton": 2500,
    "sugarcane": 120000,
    "millet": 3000,
    "barley": 6000,
    "groundnut": 4000,
    "potato": 45000
}
TEMP_RULES = {
    "maize": {"min": 10, "max": 38},
    "rice": {"min": 12, "max": 40},
    "soybean": {"min": 8, "max": 38},
    "wheat": {"min": 5, "max": 30},
    "millet": {"min": 10, "max": 40},
    "barley": {"min": 5, "max": 28},
}
def calculate_et(temperature, humidity):
    return 0.0023 * (temperature + 17.8) * (100 - humidity)
KC = {
    "rice": 1.2,
    "maize": 1.0,
    "soybean": 0.9,
    "wheat": 0.85,
    "millet": 0.75,
    "barley": 0.8,
}




# Load irrigation model + encoders
with open("models/irrigation_model.pkl", "rb") as f:
    irrigation_data = pickle.load(f)

irrigation_model = irrigation_data["model"]
crop_encoder = irrigation_data["crop_encoder"]
soil_encoder = irrigation_data["soil_encoder"]

# Load yield model
with open("models/yield_model.pkl", "rb") as f:
    yield_model = pickle.load(f)


def advise_farmer(
    crop,
    soil_type,
    temperature,
    rainfall,
    humidity,
    pH,
    N,
    P,
    K
):
    """
    Returns irrigation advice, yield prediction, and reasoning
    """

    reasons = []  # NEW: explanation tracker

    # Encode categorical inputs
    crop_encoded = crop_encoder.transform([crop])[0]
    soil_encoded = soil_encoder.transform([soil_type])[0]

    # ------------------ IRRIGATION (ET-BASED) ------------------

    et = calculate_et(temperature, humidity)
    water_needed = et * KC.get(crop, 1.0)

    if rainfall > 10:
        water_needed = 0
        reasons.append("Sufficient rainfall, irrigation not required")

    # ------------------ YIELD PREDICTION ------------------

    yield_features = np.array([
        pH, N, P, K,
        temperature, rainfall, humidity
    ]).reshape(1, -1)

    predicted_yield = yield_model.predict(yield_features)[0]

    # ------------------ TEMPERATURE RULES ------------------

    rules = TEMP_RULES.get(crop)

    if rules:
        if temperature < rules["min"]:
            predicted_yield = 0
            reasons.append(
                f"Temperature ({temperature}°C) below minimum for {crop}"
            )
        elif temperature > rules["max"]:
            predicted_yield *= 0.4
            reasons.append(
                f"Temperature ({temperature}°C) above optimal range for {crop}"
            )

    # ------------------ BIOLOGICAL CEILING ------------------

    predicted_yield = min(
        predicted_yield,
        MAX_YIELD.get(crop, predicted_yield)
    )

    # ------------------ SOIL CHECK ------------------

    if pH < 5.5 or pH > 7.5:
        reasons.append("Soil pH outside optimal range")

    # ------------------ FINAL DECISION TEXT ------------------

    irrigation_decision = (
        "No irrigation needed"
        if water_needed == 0
        else f"Irrigate with {water_needed:.1f} mm water"
    )

    return {
        "irrigation_decision": irrigation_decision,
        "water_needed_mm": round(float(water_needed), 2),
        "predicted_yield_kg_per_ha": round(float(predicted_yield), 2),
        "reasoning": "; ".join(reasons) if reasons else "Conditions are optimal"
    }



# Test block
if __name__ == "__main__":
    result = advise_farmer(
        crop="rice",
        soil_type="clay",
        temperature=30,
        rainfall=2,
        humidity=70,
        pH=6.5,
        N=90,
        P=40,
        K=40
    )

    print(result)
