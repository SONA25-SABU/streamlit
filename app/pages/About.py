import streamlit as st

def about_page():
    st.title("Breast Cancer Diagnosis Model - About")

    st.header("Project Overview:")
    st.write("""
    The aim of this project is to develop a machine learning model capable of predicting whether a breast tumor is malignant (M) or benign (B) 
    based on various features extracted from diagnostic images. The script employs logistic regression, a widely used classification algorithm, 
    to accomplish this objective.
    """)

    st.header("Technologies Utilized:")
    st.write("""
    - **Python**: The chosen programming language for scripting purposes.
    - **Pandas**: A Python library utilized for data manipulation and analysis.
    - **scikit-learn (sklearn)**: A prevalent Python machine learning library.
    - **pickle**: A Python module employed for serializing and deserializing Python objects.
    """)

    st.header("Workflow Overview:")
    st.subheader("Data Cleaning and Preprocessing (get_clean_data function):")
    st.write("""
    - Reads the dataset from a CSV file named "data.csv".
    - Removes unnecessary columns ('Unnamed: 32' and 'id').
    - Converts 'diagnosis' column values from 'M' (malignant) and 'B' (benign) to numeric values (1 and 0) respectively.
    """)

    st.subheader("Model Training (create_model function):")
    st.write("""
    - Prepares the data for training purposes.
    - Standardizes the features using StandardScaler.
    - Divides the dataset into training and testing sets.
    - Trains a logistic regression model using the training data.
    - Evaluates the trained model's performance on the testing data.
    """)

    st.subheader("Model Saving (main function):")
    st.write("""
    - Manages the entire process.
    - Invokes get_clean_data to load and preprocess the dataset.
    - Utilizes create_model to train the model and assess its performance.
    - Saves the trained model and scaler objects using pickle for future usage.
    """)

if __name__ == "__main__":
    about_page()
