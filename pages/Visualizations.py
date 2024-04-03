import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Breast Cancer Data Visualization")

    # Load data
    df = pd.read_csv("data.csv")

    # Display the first few rows of the dataset
    st.subheader("Dataset Preview")
    st.write(df.head())

    st.header("Data Visualizations")

    # Scatter plot
    st.subheader("Scatter Plot")
    scatter_plot = px.scatter(df, x="radius_mean", y="texture_mean", color="diagnosis",
                              title="Scatter Plot of Radius Mean vs Texture Mean")
    st.plotly_chart(scatter_plot)

    # Histogram
    st.subheader("Histogram of Area Mean")
    hist_plot = px.histogram(df, x="area_mean", color="diagnosis",
                             title="Histogram of Area Mean")
    st.plotly_chart(hist_plot)

    # Box plot
    st.subheader("Box Plot of Perimeter Mean")
    box_plot = px.box(df, x="diagnosis", y="perimeter_mean",
                      title="Box Plot of Perimeter Mean by Diagnosis")
    st.plotly_chart(box_plot)

if __name__ == "__main__":
    main()
