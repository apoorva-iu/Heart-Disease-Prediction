# ❤️ Heart Disease Prediction Dashboard

An interactive **machine learning web app** built with **Streamlit** that predicts the likelihood of heart disease based on patient health metrics.  
It uses a trained **Random Forest Classifier** model and provides **visual reports & downloadable summaries**.

---

## 📊 Features

- **User Input Form** → Enter medical details like age, blood pressure, cholesterol, etc.  
- **Prediction** → Model predicts if the patient is **likely/unlikely** to have heart disease.  
- **Risk Meter Gauge** → A Plotly gauge chart shows heart disease risk percentage:
  - 🟢 0–40% → Low risk  
  - 🟡 40–70% → Moderate risk  
  - 🔴 70–100% → High risk  
- **Input vs Healthy Ranges Chart** → Compares your inputs with medically healthy ranges.  
- **📄 Patient Report** → Downloadable PDF or copyable summary of results.  

---

## 🧠 Model Training

- Dataset: `dataset.csv` (includes patient features & target column `target`)  
- Models compared:  
  - Logistic Regression  
  - Decision Tree  
  - Random Forest ✅ (Best performance)  
  - Support Vector Machine (SVC)  
- Final model: **RandomForestClassifier** (saved as `heart_disease_model.pkl`)

---


## 📂 Project Structure

Heart-Disease-Prediction/
│
├── app.py # Main Streamlit app
├── prediction.py # Prediction page (inputs, charts, risk meter)
├── report.py # Report generation page (PDF + summary)
├── train_models.ipynb # Notebook for training & evaluating models
├── dataset.csv # Heart disease dataset
├── heart_disease_model.pkl # Saved trained model
├── README.md # Project documentation
└── requirements.txt # Python dependencies


---

## ⚙️ Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/apoorva-iu/heart-disease-prediction.git
cd heart-disease-prediction

2. Install Dependencies
pip install -r requirements.txt

3. Run the App
streamlit run app.py

Input Features

The model uses 13 medical features:

age → Age of the patient (years)

sex → Sex (1 = male, 0 = female)

cp → Chest pain type (0–3)

trestbps → Resting blood pressure (mmHg)

chol → Serum cholesterol (mg/dl)

fbs → Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)

restecg → Resting electrocardiographic results (0–2)

thalach → Maximum heart rate achieved

exang → Exercise induced angina (1 = yes, 0 = no)

oldpeak → ST depression induced by exercise

slope → Slope of the peak exercise ST segment (0–2)

ca → Number of major vessels (0–3)

thal → Thalassemia (1 = normal, 2 = fixed defect, 3 = reversible defect)




