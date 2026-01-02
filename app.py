import streamlit as st
import pickle
import pandas as pd
import os

st.set_page_config(page_title="ML Prediction App", layout="centered")

st.title("📊 Machine Learning Prediction App")

# ---------------- Load Model ---------------- #
@st.cache_resource
def load_model():
    model_path = "model.pkl"   # rename your file to model.pkl

    if not os.path.exists(model_path):
        st.error("❌ Model file 'model.pkl' not found. Please place it in the app folder.")
        st.stop()

    with open(model_path, "rb") as f:
        return pickle.load(f)

model = load_model()

st.success("✅ Model loaded successfully!")

# ---------------- CSV Upload ---------------- #
uploaded_file = st.file_uploader(
    "📥 Upload CSV file for prediction",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### 🧾 Uploaded Data")
    st.dataframe(df)

    # Validate number of features
    try:
        required_features = model.n_features_in_
    except:
        required_features = df.shape[1]  # fallback for custom models

    if df.shape[1] != required_features:
        st.error(f"""
        ❌ Incorrect number of columns.

        Your model expects **{required_features} features**,  
        but CSV contains **{df.shape[1]} columns**.
        """)
    else:
        if st.button("🔮 Predict"):
            predictions = model.predict(df)

            result = df.copy()
            result["Prediction"] = predictions

            st.success("✅ Prediction completed!")
            st.write("### 📄 Prediction Results")
            st.dataframe(result)

            # Download result
            csv = result.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇ Download Prediction CSV",
                data=csv,
                file_name="predictions.csv",
                mime="text/csv"
            )
