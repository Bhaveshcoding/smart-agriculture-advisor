import pandas as pd
import random

crops = {
    "rice": (6.0, 7.0, 7.5, 4200),
    "wheat": (6.5, 7.5, 5.0, 3200),
    "maize": (6.0, 7.0, 6.0, 3900),
    "cotton": (5.8, 7.2, 7.0, 2000),
    "sugarcane": (6.0, 7.5, 10.0, 70000),
    "millet": (5.5, 6.8, 4.0, 1800),
    "barley": (6.0, 7.5, 4.5, 2800),
    "soybean": (6.0, 7.0, 5.5, 2500),
    "groundnut": (6.0, 6.8, 5.0, 2300),
    "potato": (5.5, 6.5, 6.5, 30000),
}

soil_types = ["clay", "loamy", "sandy", "silty", "black", "red", "alluvial"]

rows = []

for crop, (ph_min, ph_max, water, base_yield) in crops.items():
    for soil in soil_types:
        for _ in range(5):  # 5 samples per combination
            temperature = random.uniform(18, 35)
            rainfall = random.uniform(40, 250)
            humidity = random.uniform(40, 85)

            pH = random.uniform(ph_min, ph_max)
            N = random.randint(50, 120)
            P = random.randint(20, 60)
            K = random.randint(20, 60)

            water_needed = water + random.uniform(-1.5, 1.5)
            yield_val = base_yield + random.randint(-500, 500)

            rows.append([
                crop, soil, round(pH, 2), N, P, K,
                round(temperature, 1),
                round(rainfall, 1),
                round(humidity, 1),
                round(water_needed, 2),
                yield_val
            ])

columns = [
    "crop", "soil_type", "pH", "N", "P", "K",
    "temperature", "rainfall", "humidity",
    "water_needed", "yield"
]

df = pd.DataFrame(rows, columns=columns)
df.to_csv("data/soil_crop_data.csv", index=False)

print("✅ Expanded dataset created")
print("Rows:", len(df))
