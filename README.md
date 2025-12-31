# 🌱 Smart Agriculture Advisor

An AI-powered decision support system that predicts crop yield and irrigation requirements
using weather data, soil parameters, machine learning, and biological constraints.

This project combines agriculture science (biology, chemistry, physics) with explainable AI
to ensure predictions are realistic, interpretable, and practical.

---

## 🚜 Problem Statement

Farmers often rely on experience rather than data for irrigation and fertilization decisions.
This can lead to inefficient water usage, unrealistic yield expectations, and poor adaptation
to changing climate conditions.

This project aims to provide a smart, data-driven agricultural advisory system.

---

## ✨ Key Features

- 📈 Crop Yield Prediction using machine learning
- 💧 Dynamic irrigation advice based on evapotranspiration (ET)
- 🌡️ Crop-specific temperature growth constraints
- 🚫 Biological yield limits to prevent unrealistic predictions
- 🧠 Explainable AI with clear reasoning for each prediction
- 🛰️ Scalable design for future satellite and IoT integration

---

## 🧪 Science Integration (CBSE Aligned)

- **Biology:** Crop growth limits, temperature stress
- **Chemistry:** Soil pH and nutrient (NPK) balance
- **Physics:** Evapotranspiration and heat-driven water loss

---

## 🛠️ Tech Stack

- Python 3
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Open-Meteo Weather API

---

## 📂 Project Structure

smart-agriculture-advisor/
│
├── api/
│ └── weather.py
│
├── data/
│ ├── create_dataset.py
│ └── soil_crop_data.csv
│
├── train/
│ ├── train_irrigation.py
│ └── train_yield.py
│
├── utils/
│ └── advisor.py
│
├── app.py
├── requirements.txt
└── README.md

yaml
Copy code

---

## ▶️ How to Run

1. Install dependencies
pip install -r requirements.txt

markdown
Copy code

2. Generate dataset
python create_dataset.py

markdown
Copy code

3. Train models
python train/train_irrigation.py
python train/train_yield.py

markdown
Copy code

4. Run the app
streamlit run app.py

r
Copy code

Open in browser:
http://localhost:8501

yaml
Copy code

---

## 🧠 Example Output

- **Irrigation Advice:** Irrigate with 6.8 mm water  
- **Predicted Yield:** 4200 kg/hectare  
- **Reasoning:** Temperature optimal; rainfall insufficient; soil pH within range

---

## 🚀 Future Improvements

- Satellite NDVI integration
- Historical yield baselines
- Crop growth stage modeling
- Confidence intervals for predictions
- Cloud deployment

---

## ⚠️ Disclaimer

This project is for educational and research purposes only and should not replace
professional agricultural advice.

---

## 👤 Author

Bhavesh Tushar Bhandari  
Student | AI & Agriculture Enthusiast