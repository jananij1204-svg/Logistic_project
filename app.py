import streamlit as st
import pickle
import os
import numpy as np

st.set_page_config(page_title="Heart Disease Prediction", layout="centered")
st.title("❤️ Heart Disease Prediction App")

# ---- MODEL PATH ----
MODEL_PATH = "/mnt/data/logistic (3).pkl"

# ---- LOAD MODEL ----
@st.cache_resource
def load_model():
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "rb") as f:
            return pickle.load(f)
    else:
        st.error("❌ Model file not found. Please upload logistic (3).pkl.")
        return None

model = load_model()


# ---- USER INPUT FORM ----
st.header("🧍 Patient Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 120, 45)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type (CP)", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)
    chol = st.number_input("Cholesterol", 100, 600, 200)

with col2:
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
    thalach = st.number_input("Max Heart Rate Achieved", 60, 220, 140)
    exang = st.selectbox("Exercise-Induced Angina", [0, 1])
    oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 10.0, 1.0)

# Your model likely uses these 11 standard features
input_data = np.array([[age,
                        0 if sex == "Male" else 1,
                        cp,
                        trestbps,
                        chol,
                        fbs,
                        restecg,
                        thalach,
                        exang,
                        oldpeak
                       ]])

# ---- PREDICT ----
st.write("")

if st.button("🔍 Predict"):
    if model is None:
        st.error("Model not loaded.")
    else:
        prediction = model.predict(input_data)[0]

        if prediction == 1:
            st.error("⚠️ High Chance of Heart Disease")
        else:
            st.success("✅ No Significant Heart Disease Detected")
