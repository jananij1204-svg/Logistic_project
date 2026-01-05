import streamlit as st
import pickle
import os
import numpy as np

st.set_page_config(page_title="Heart Disease Prediction", layout="centered")
st.title("❤️ Heart Disease Prediction App")

# ---- MODEL PATH ----
MODEL_PATH = "logistic (3).pkl"

# ---- LOAD MODEL ----
@st.cache_resourceimport streamlit as st
import numpy as np
import pickle
import os

st.set_page_config(page_title="Heart Disease Prediction", layout="centered")
st.title("❤️ Heart Disease Prediction (Framingham Dataset)")

MODEL_PATH = "logistic (3).pkl"   # Must be in same folder as app.py

# Load modelimport streamlit as st
import numpy as np
import pickle
import os

st.set_page_config(page_title="Heart Disease Prediction", layout="centered")
st.title("❤️ Heart Disease Prediction (Framingham Dataset)")

MODEL_PATH = "logistic (3).pkl"   # Must be in same folder as app.py

# Load model
@st.cache_resource
def load_model():
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "rb") as f:
            return pickle.load(f)
    else:
        st.error(f"❌ Model file not found. Place '{MODEL_PATH}' in the same folder.")
        return None

model = load_model()

# --------------------------------------
# INPUT FIELDS (15 FEATURES)
# --------------------------------------
st.header("📌 Patient Information")

col1, col2 = st.columns(2)

with col1:
    male = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", 1, 120, 45)
    currentSmoker = st.selectbox("Current Smoker?", [0, 1])
    cigsPerDay = st.number_input("Cigarettes Per Day", 0, 70, 0)
    BPMeds = st.selectbox("On BP Medication?", [0, 1])
    prevalentStroke = st.selectbox("Prevalent Stroke?", [0, 1])
    prevalentHyp = st.selectbox("Hypertension?", [0, 1])

with col2:
    diabetes = st.selectbox("Diabetes?", [0, 1])
    totChol = st.number_input("Total Cholesterol", 100, 700, 200)
    sysBP = st.number_input("Systolic BP", 80, 240, 120)
    diaBP = st.number_input("Diastolic BP", 50, 150, 80)
    BMI = st.number_input("BMI", 10.0, 60.0, 25.0)
    heartRate = st.number_input("Heart Rate", 30, 220, 70)
    glucose = st.number_input("Glucose", 40, 500, 80)

# Prepare input array
input_data = np.array([[
    1 if male == "Male" else 0,
    age,
    currentSmoker,
    cigsPerDay,
    BPMeds,
    prevalentStroke,
    prevalentHyp,
    diabetes,
    totChol,
    sysBP,
    diaBP,
    BMI,
    heartRate,
    glucose
]])

# --------------------------------------
# PREDICTION
# --------------------------------------
st.write("")

if st.button("🔍 Predict"):
    if model is None:
        st.error("Model not loaded.")
    else:
        pred = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0][1]

        if pred == 1:
            st.error(f"⚠️ High Risk of Heart Disease\nProbability: {prob:.2f}")
        else:
            st.success(f"✅ Low Risk of Heart Disease\nProbability: {prob:.2f}")

@st.cache_resource
def load_model():
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "rb") as f:
            return pickle.load(f)
    else:
        st.error(f"❌ Model file not found. Place '{MODEL_PATH}' in the same folder.")
        return None

model = load_model()

# --------------------------------------
# INPUT FIELDS (15 FEATURES)
# --------------------------------------
st.header("📌 Patient Information")

col1, col2 = st.columns(2)

with col1:
    male = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", 1, 120, 45)
    currentSmoker = st.selectbox("Current Smoker?", [0, 1])
    cigsPerDay = st.number_input("Cigarettes Per Day", 0, 70, 0)
    BPMeds = st.selectbox("On BP Medication?", [0, 1])
    prevalentStroke = st.selectbox("Prevalent Stroke?", [0, 1])
    prevalentHyp = st.selectbox("Hypertension?", [0, 1])

with col2:
    diabetes = st.selectbox("Diabetes?", [0, 1])
    totChol = st.number_input("Total Cholesterol", 100, 700, 200)
    sysBP = st.number_input("Systolic BP", 80, 240, 120)
    diaBP = st.number_input("Diastolic BP", 50, 150, 80)
    BMI = st.number_input("BMI", 10.0, 60.0, 25.0)
    heartRate = st.number_input("Heart Rate", 30, 220, 70)
    glucose = st.number_input("Glucose", 40, 500, 80)

# Prepare input array
input_data = np.array([[
    1 if male == "Male" else 0,
    age,
    currentSmoker,
    cigsPerDay,
    BPMeds,
    prevalentStroke,
    prevalentHyp,
    diabetes,
    totChol,
    sysBP,
    diaBP,
    BMI,
    heartRate,
    glucose
]])

# --------------------------------------
# PREDICTION
# --------------------------------------
st.write("")

if st.button("🔍 Predict"):
    if model is None:
        st.error("Model not loaded.")
    else:
        pred = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0][1]

        if pred == 1:
            st.error(f"⚠️ High Risk of Heart Disease\nProbability: {prob:.2f}")
        else:
            st.success(f"✅ Low Risk of Heart Disease\nProbability: {prob:.2f}")

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
