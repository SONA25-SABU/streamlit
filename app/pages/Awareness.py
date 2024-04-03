import streamlit as st

# Title and header
st.title("Cancer Awareness")
st.header("Know, Fight, Conquer")

# Introduction
st.write("""
Cancer is a group of diseases involving abnormal cell growth with the potential to invade or spread to other parts of the body. 
Early detection and treatment are crucial for improving the chances of a cure. This page aims to raise awareness about cancer
and provide resources for further information.
""")

# Types of Cancer (brief overview)
st.subheader("Types of Cancer")
st.write("""There are many different types of cancer, each affecting a specific part of the body. 
Some common types include:""")
cancer_types = ["Breast Cancer", "Lung Cancer", "Colon Cancer", "Prostate Cancer"]
for cancer_type in cancer_types:
    st.write(f"- {cancer_type}")

# Risk Factors
st.subheader("Risk Factors")
st.write("""Certain factors can increase your risk of developing cancer. These include:""")
risk_factors = [
    "Tobacco use",
    "Excessive sun exposure",
    "Certain dietary choices",
    "Family history",
    "Obesity",
    "Certain infections"]
for factor in risk_factors:
    st.write(f"- {factor}")

# Early Detection
st.subheader("Early Detection")
st.write("""Early detection is key to successful cancer treatment. Be aware of the signs and symptoms 
associated with different types of cancer and consult a doctor if you experience any concerns.""")
st.write("**Remember, this is not an exhaustive list, and some cancers may not present with any symptoms.**")

# Resources
st.subheader("Resources")
st.write("""Here are some resources for further information about cancer:""")
resources = [
    ("American Cancer Society", "https://www.cancer.org/"),
    ("National Cancer Institute", "https://www.cancer.gov/"),
    ("World Health Organization - Cancer", "https://www.who.int/health-topics/cancer")]
for resource_name, resource_link in resources:
    st.write(f"- {resource_name}: {resource_link}")

# Conclusion
st.subheader("Conclusion")
st.write("""By raising awareness and encouraging early detection, we can fight cancer together. 
Knowledge is power, and this information can empower you to take charge of your health.""")

