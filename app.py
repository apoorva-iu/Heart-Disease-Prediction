import streamlit as st
from prediction import show_prediction_page
from learn_more import show_learn_more_page
from report import show_report_page

# ---- Sidebar Navigation ----
page = st.sidebar.radio("", ["🏠 Prediction", "📘 Learn More","📄 Report"])  # added "" as label

# ---- Render Pages ----
if page == "🏠 Prediction":
    show_prediction_page()
elif page == "📘 Learn More":
    show_learn_more_page()
elif page == "📄 Report":
    show_report_page()

    # ---- Custom CSS (put here after title) ----
st.markdown("""
    <style>
    /* Background gradient */
    .stApp {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffe6e6 100%);
        font-family: 'Segoe UI', sans-serif;
    }
    /* Title style */
    h1 {
        color: #b22222;
        text-align: center;
        font-size: 2.5em;
        font-weight: 700;
    }
    /* Button style */
    div.stButton > button {
        background-color: #b22222;
        color: white;
        border-radius: 10px;
        padding: 0.6em 1.2em;
        font-size: 1.1em;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #8b0000;
        transform: scale(1.05);
    }
    /* Clean Selectbox style */
    div[data-baseweb="select"] > div {
    border: 1px solid #ccc !important;  /* light gray border */
    border-radius: 8px !important;
    transition: 0.3s;
}

    /* Hover / focus effect */
    div[data-baseweb="select"] > div:hover {
    border-color: #b22222 !important;
    box-shadow: 0 0 5px rgba(178,34,34,0.3);
}

    }
    .stNumberInput > div > div > input:focus,
    .stTextInput > div > div > input:focus {
        border-color: #8b0000 !important;
        box-shadow: 0 0 5px rgba(178,34,34,0.6);
        outline: none;
    }
    .stSlider [role="slider"] {
        background-color: #b22222 !important;
        border-radius: 50%;
    }
    .stSlider [data-baseweb="track"] {
        background: linear-gradient(90deg, #b22222, #ff6666) !important;
    }
    </style>
""", unsafe_allow_html=True)
# ---- End of Custom CSS ----

