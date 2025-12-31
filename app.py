import streamlit as st
import pandas as pd
from api.weather import get_weather
from utils.advisor import advise_farmer

df = pd.read_csv("data/soil_crop_data.csv")

crop_list = sorted(df["crop"].unique().tolist())
soil_list = sorted(df["soil_type"].unique().tolist())


st.set_page_config(page_title="Smart Agriculture Advisor", layout="centered")

st.title("🌱 Smart Agriculture Advisor")
st.write("AI-based irrigation and crop yield prediction system")



### User Inputs

st.header("📍 Location & Crop Details")

latitude = st.number_input("Latitude", value=12.9716)
longitude = st.number_input("Longitude", value=77.5946)

crop = st.selectbox("Crop Type", crop_list)
soil_type = st.selectbox("Soil Type", soil_list)

st.header("🌱 Soil Parameters")

pH = st.slider("Soil pH", 4.5, 8.5, 6.5)
N = st.number_input("Nitrogen (N)", value=80)
P = st.number_input("Phosphorus (P)", value=35)
K = st.number_input("Potassium (K)", value=30)



if st.button("Predict & Advise"):
    weather = get_weather(latitude, longitude)

    result = advise_farmer(
        crop=crop,
        soil_type=soil_type,
        temperature=weather["temperature"],
        rainfall=weather["rainfall"],
        humidity=weather["humidity"],
        pH=pH,
        N=N,
        P=P,
        K=K
    )

    st.success("✅ Prediction Complete")

    st.subheader("🌦 Weather Conditions")
    st.write(weather)

    st.subheader("💧 Irrigation Advice")
    st.write(result["irrigation_decision"])

    st.subheader("🌾 Expected Crop Yield")
    st.write(f"{result['predicted_yield_kg_per_ha']} kg/hectare")
    
    st.subheader("🧠 Reasoning")
    st.write(result["reasoning"])

    
    
    #run statement
    #streamlit run app.py

