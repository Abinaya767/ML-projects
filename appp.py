# app.py
import streamlit as st
import pandas as pd

# ==============================
# 1. App Introduction
# ==============================
st.title("YouTube Channel Analytics Dashboard")
st.write("""
This app provides a quick analytics overview of a YouTube channel dataset. 
You can explore content statistics, subscriber counts, average video duration, 
and overall engagement metrics like likes, comments, shares, and total watch hours.

**Note:** The dataset must be a CSV file.
""")

# ==============================
# 2. Predefined CSV Path
# ==============================
DATA_PATH = r"C:\Users\Admin\OneDrive\Desktop\YouTube_Video.csv"  # <- CSV file path

try:
    # Load CSV
    df = pd.read_csv(DATA_PATH)

    # ==============================
    # 3. Show Data Preview
    # ==============================
    st.write("### Data Preview")
    st.dataframe(df.head())

    # ==============================
    # 4. Bar chart: Content vs Subscribers
    # ==============================
    if 'content' in df.columns and 'subscribers' in df.columns:
        content_subs = df.groupby('content')['subscribers'].sum().reset_index()
        st.write("### Content Count vs Subscribers")
        st.bar_chart(data=content_subs.set_index('content'))

    # ==============================
    # 5. Table: Video Duration & Avg Views
    # ==============================
    if 'content' in df.columns and 'video_duration' in df.columns and 'views' in df.columns:
        table_data = df.groupby('content').agg({
            'video_duration': 'mean',
            'views': 'mean'
        }).reset_index()
        table_data.rename(columns={'video_duration': 'Avg Video Duration (min)', 
                                   'views': 'Avg Views'}, inplace=True)
        st.write("### Average Video Duration & Views per Content")
        st.dataframe(table_data)

    # ==============================
    # 6. Total Engagement Metrics
    # ==============================
    engagement_columns = ['likes', 'comments', 'shares', 'watch_hours']
    st.write("### Total Engagement Metrics Across All Content")
    total_engagement = df[engagement_columns].sum().to_frame().reset_index()
    total_engagement.columns = ['Metric', 'Total']
    st.dataframe(total_engagement)

except FileNotFoundError:
    st.error(f"File not found: {DATA_PATH}. Please make sure this file exists on your system.")
