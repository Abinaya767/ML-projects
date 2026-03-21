# app.py
import streamlit as st
import pandas as pd

# Path to the CSV in your project folder
DATA_PATH = "YouTube_Video.csv"

# Load CSV
try:
    df = pd.read_csv(DATA_PATH)
    st.success("CSV loaded successfully!")
    st.write("### Data Preview", df.head())

    # Basic analytics
    st.write("### Summary Statistics")
    st.write(df.describe())

    # Example visualizations
    if 'views' in df.columns:
        st.write("### Views Distribution")
        st.bar_chart(df['views'])
    if 'likes' in df.columns:
        st.write("### Likes Distribution")
        st.bar_chart(df['likes'])
except FileNotFoundError:
    st.error(f"File not found: {DATA_PATH}. Please upload it to the project folder.")
