# about.py

import streamlit as st

def about_page():
    st.title("About Cancer Predictor App")
    st.write("""
    Welcome to the Cancer Predictor App! This app is designed to help users predict the likelihood of having cancer based on various input parameters.

    **How it works:**
    
    - Users input various medical parameters such as age, gender, family history, and lifestyle habits.
    - The app then utilizes a machine learning model trained on a dataset of cancer cases to predict the probability of cancer for the user.
    - Users can use this information for early detection and to take preventive measures.

    **Creators:**
    
    - This app was developed by [Your Name] and [Co-Developer Name] as a part of [Project/Company Name].
    - For any inquiries or feedback, please contact us at [contact@email.com].

    **Disclaimer:**
    
    - The predictions made by this app are based on statistical models and should not be considered a substitute for professional medical advice.
    - Always consult with a healthcare professional for accurate diagnosis and treatment.

    We hope you find this app useful and informative!
    """)
