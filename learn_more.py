import streamlit as st

def show_learn_more_page():
    st.title("📘 Learn More")
    st.write("Understand the medical meaning of each feature used in the model.")

    st.markdown("""
    ### 🧑‍⚕️ Features Explained

    **Age**  
    Risk increases as you get older (more common after 50).  

    **Sex**  
    Males have higher early risk; women catch up after menopause.  

    **Chest Pain Type (cp)**  
    - 0 = Typical Angina (classic chest pain)  
    - 1 = Atypical Angina  
    - 2 = Non-anginal Pain  
    - 3 = Asymptomatic (silent disease, higher risk)  

    **Resting Blood Pressure (trestbps)**  
    Pressure in arteries while resting.  
    Normal ≈ 120 mmHg. Hypertension damages arteries.  

    **Serum Cholesterol (chol)**  
    High cholesterol → plaque buildup in arteries.  
    Normal < 200 mg/dl.  

    **Fasting Blood Sugar (fbs)**  
    >120 mg/dl → possible diabetes, raises heart risk.  

    **Resting ECG (restecg)**  
    - 0 = Normal  
    - 1 = ST-T abnormality  
    - 2 = Left ventricular hypertrophy  

    **Max Heart Rate (thalach)**  
    Lower maximum rate may indicate reduced heart function.  

    **Exercise Induced Angina (exang)**  
    - 1 = Yes (pain during exercise)  
    - 0 = No  

    **ST Depression (oldpeak)**  
    Drop in ST during exercise. Larger drop = worse blood flow.  

    **Slope of ST Segment (slope)**  
    - 0 = Upsloping (good)  
    - 1 = Flat (intermediate)  
    - 2 = Downsloping (bad prognosis)  

    **Major Vessels (ca)**  
    Number of vessels (0–3) blocked. More blocked = higher risk.  

    **Thalassemia (thal)**  
    - 1 = Normal  
    - 2 = Fixed defect  
    - 3 = Reversible defect  
    """)
