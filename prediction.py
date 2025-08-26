import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Load model
model = pickle.load(open("heart_disease_model.pkl", "rb"))

# ---------------- Gauge Chart ----------------
def show_risk_gauge(probability):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability * 100,  # convert to %
        title={'text': "Heart Disease Risk (%)"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "darkred"},
            'steps': [
                {'range': [0, 40], 'color': "lightgreen"},
                {'range': [40, 70], 'color': "yellow"},
                {'range': [70, 100], 'color': "red"},
            ],
        }
    ))
    return fig

# ---------------- Main Prediction Page ----------------
def show_prediction_page():
    st.title("❤️ Heart Disease Prediction")
    st.write("An interactive medical dashboard to assess heart disease risk.")

    col1, col2 = st.columns(2)

    # ---------------- Left Column ----------------
    with col1:
        age = st.number_input("Age", 20, 100, 52, help="Older age increases risk")
        sex = st.selectbox("Sex", [0, 1], help="0=Female, 1=Male")
        cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3], help="Type of chest pain")
        trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120, help="Normal ~120 mmHg")
        chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 600, 240, help="Normal <200 mg/dl")
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1], help="1=True, 0=False")

    # ---------------- Right Column ----------------
    with col2:
        restecg = st.selectbox("Resting ECG (0-2)", [0, 1, 2], help="0=Normal, 1=Abnormal, 2=LVH")
        thalach = st.number_input("Max Heart Rate Achieved", 70, 220, 150, help="Higher is better")
        exang = st.selectbox("Exercise Induced Angina", [0, 1], help="1=Yes, 0=No")
        oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 6.0, 1.0, help="ST drop during exercise")
        slope = st.selectbox("Slope of ST (0-2)", [0, 1, 2], help="0=Upsloping, 1=Flat, 2=Downsloping")
        ca = st.selectbox("Major Vessels (0-3)", [0, 1, 2, 3], help="Number of blocked vessels")
        thal = st.selectbox("Thalassemia (1-3)", [1, 2, 3], help="1=Normal, 2=Fixed, 3=Reversible")

    # ---------------- Predict Button ----------------
    if st.button("Predict"):
        input_dict = {
            "age": [age], "sex": [sex], "cp": [cp], "trestbps": [trestbps],
            "chol": [chol], "fbs": [fbs], "restecg": [restecg], "thalach": [thalach],
            "exang": [exang], "oldpeak": [oldpeak], "slope": [slope], "ca": [ca], "thal": [thal]
        }
        input_df = pd.DataFrame(input_dict)

        # --- Prediction ---
        prediction = model.predict(input_df)[0]
        proba = model.predict_proba(input_df)[0][1]

        # Store values for report
        st.session_state["input_dict"] = input_dict
        st.session_state["prediction"] = prediction
        st.session_state["proba"] = proba

        # --- Results ---
        st.subheader("Results")
        if prediction == 1:
            st.warning(f"⚠️ Likely to have heart disease\n\nProbability: {proba:.2f}")
        else:
            st.success(f"✅ Unlikely to have heart disease\n\nProbability: {proba:.2f}")

        # --- Risk Gauge Chart ---
        st.subheader("📊 Risk Meter")
        st.plotly_chart(show_risk_gauge(proba), use_container_width=True)

        # --- Chart: Input vs Healthy Range ---
        st.subheader("Your Input vs. Healthy Ranges")
        friendly_labels = {
            "age": "Age",
            "trestbps": "BP ",
            "chol": "Cholesterol",
            "thalach": "Heart Rate",
            "oldpeak": "Depression"
        }
        ranges = {
            "age": (20, 60),
            "trestbps": (90, 120),
            "chol": (150, 240),
            "thalach": (120, 190),
            "oldpeak": (0.0, 2.0)
        }

        fig, ax = plt.subplots(figsize=(8, 4))
        for col in ranges.keys():
            value = input_df[col][0]
            ax.bar(friendly_labels[col], value, color="skyblue")
            ax.axhspan(ranges[col][0], ranges[col][1], color="lightgreen", alpha=0.3)

        ax.set_ylabel("Value")
        ax.set_title("Inputs vs. Healthy Ranges")
        st.pyplot(fig)
        st.caption("✅ Green shaded areas indicate healthy ranges.")
