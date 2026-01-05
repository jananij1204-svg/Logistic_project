import streamlit as st
import pickle
import os

st.title("Movie Interest Prediction App 🎬")

# Path inside the ChatGPT environment
LOCAL_MODEL_PATH = "/mnt/data/logistic (3).pkl"

def load_model():
    if os.path.exists(LOCAL_MODEL_PATH):
        with open(LOCAL_MODEL_PATH, "rb") as f:
            model = pickle.load(f)
        return model
    else:
        st.error("Model file not found! Please upload logistic (3).pkl")
        return None

model = load_model()

# User inputs
age = st.number_input("Enter age", min_value=1, max_value=120, value=25)
gender = st.selectbox("Gender", ["Male", "Female"])
genre = st.selectbox("Favourite Genre", ["Action", "Comedy", "Drama", "Horror", "Romance"])

if st.button("Predict"):
    if model is not None:
        # Simple encoding example (modify according to your training)
        gender_map = {"Male": 0, "Female": 1}
        genre_map = {"Action": 1, "Comedy": 2, "Drama": 3, "Horror": 4, "Romance": 5}

        data = [[age, gender_map[gender], genre_map[genre]]]

        prediction = model.predict(data)

        if prediction[0] == 1:
            st.success("✅ This person is interested in the movie!")
        else:
            st.warning("❌ This person is NOT interested in the movie.")
