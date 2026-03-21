# app.py
import streamlit as st
import pandas as pd
import altair as alt

# ==============================
# 1. LOAD DATASET DIRECTLY
# ==============================
DATA_PATH = r"C:\Users\Admin\OneDrive\Documents\YouTube_Video.csv"  # your CSV path
df = pd.read_csv(DATA_PATH, header=None)

# Add column names based on your data
df.columns = [
    "Category", "Duration", "Views", "Avg_View_Percentage", "Subscribers_Gained",
    "CTR", "Impressions", "Likes", "Comments", "Shares", "Total_Watch_Hours"
]

st.title("YouTube Video Analysis Dashboard")

# ==============================
# 2. SHOW RAW DATA
# ==============================
st.subheader("Raw Data")
st.dataframe(df)

# ==============================
# 3. SUMMARY METRICS
# ==============================
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Average Views", int(df["Views"].mean()))
col2.metric("Average Likes", int(df["Likes"].mean()))
col3.metric("Average Watch Time (hrs)", round(df["Total_Watch_Hours"].mean(), 2))

# ==============================
# 4. VISUALIZATIONS
# ==============================

# Views per Video
st.subheader("Views per Video")
df = df.reset_index()  # add index column
views_chart = alt.Chart(df).mark_bar().encode(
    x=alt.X("index:O", title="Video #"),
    y=alt.Y("Views", title="Views"),
    tooltip=["Category", "Views", "Likes", "Comments", "Shares"]
)
st.altair_chart(views_chart, use_container_width=True)

# CTR vs Subscribers Gained
st.subheader("CTR vs Subscribers Gained")
ctr_chart = alt.Chart(df).mark_circle(size=100, color='orange').encode(
    x="CTR",
    y="Subscribers_Gained",
    tooltip=["Category", "Views", "CTR", "Subscribers_Gained"]
)
st.altair_chart(ctr_chart, use_container_width=True)

# Likes vs Comments
st.subheader("Likes vs Comments")
likes_comments_chart = alt.Chart(df).mark_circle(size=100, color='green').encode(
    x="Likes",
    y="Comments",
    tooltip=["Category", "Views", "Likes", "Comments"]
)
st.altair_chart(likes_comments_chart, use_container_width=True)

# Average Views by Category
st.subheader("Average Views by Category")
category_views = df.groupby("Category")["Views"].mean().reset_index()
bar_chart = alt.Chart(category_views).mark_bar().encode(
    x="Category",
    y="Views",
    tooltip=["Category", "Views"]
)
st.altair_chart(bar_chart, use_container_width=True)
