import streamlit as st
import numpy as np
import pickle

MODEL_PATH = "logistic (1).pkl"

@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

model = load_model()

st.title("Heart Disease Prediction App")

# Get feature names from model (do NOT display them)
feature_names = list(model.feature_names_in_)

# Custom display names for user-friendly UI
display_names = {
    "male": "Gender (0 = Female, 1 = Male)",
    "age": "Age",
    "currentSmoker": "Current Smoker (1 = Yes, 0 = No)",
    "cigsPerDay": "Cigarettes Per Day",
    "BPMeds": "Using BP Medication (1 = Yes, 0 = No)",
    "prevalentStroke": "History of Stroke (1 = Yes, 0 = No)",
    "prevalentHyp": "Hypertension (1 = Yes, 0 = No)",
    "diabetes": "Diabetes (1 = Yes, 0 = No)",
    "totChol": "Total Cholesterol",
    "sysBP": "Systolic BP",
    "diaBP": "Diastolic BP",
    "BMI": "BMI (Body Mass Index)",
    "heartRate": "Heart Rate",
    "glucose": "Glucose Level"
}

st.subheader("Enter Health Details")

inputs = []

# build inputs using friendly names
for name in feature_names:
    label = display_names.get(name, name)
    val = st.number_input(label, value=0.0)
    inputs.append(val)

features = np.array(inputs).reshape(1, -1)

if st.button("Predict"):
    try:
        pred = model.predict(features)[0]
        prob = model.predict_proba(features)[0][1]

        st.success(f"Prediction: {pred}")
        st.info(f"Risk Probability: {prob:.4f}")

    except Exception as e:
        st.error(f"Prediction Error: {e}")
