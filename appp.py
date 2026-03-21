# app.py
import streamlit as st
import pandas as pd
import altair as alt

# ==============================
# 1. LOAD DATASET
# ==============================
# Replace this with your CSV path
DATA_PATH = r"C:\Users\Admin\OneDrive\Documents\YouTube_Video.csv"
df = pd.read_csv(DATA_PATH, header=None)

# Set column names based on your data
df.columns = [
    "Category", "Duration", "Views", "Avg_View_Percentage", "Subscribers_Gained",
    "CTR", "Impressions", "Likes", "Comments", "Shares", "Total_Watch_Hours"
]

st.title("YouTube Video Analysis Dashboard")

# ==============================
# 2. FILTER BY CATEGORY
# ==============================
categories = df["Category"].unique()
selected_category = st.selectbox("Select Category", options=categories)

filtered_df = df[df["Category"] == selected_category]

st.subheader(f"Data for {selected_category} Videos")
st.dataframe(filtered_df)

# ==============================
# 3. SUMMARY METRICS
# ==============================
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Average Views", int(filtered_df["Views"].mean()))
col2.metric("Average Likes", int(filtered_df["Likes"].mean()))
col3.metric("Average Watch Time (hrs)", round(filtered_df["Total_Watch_Hours"].mean(), 2))

# ==============================
# 4. VISUALIZATIONS
# ==============================

# Views by Video
st.subheader("Views per Video")
views_chart = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X("index:O", title="Video #", sort=None),
    y=alt.Y("Views", title="Views"),
    tooltip=["Views", "Likes", "Comments", "Shares"]
).transform_calculate(index="datum.index")
st.altair_chart(views_chart, use_container_width=True)

# CTR vs Subscribers Gained
st.subheader("CTR vs Subscribers Gained")
ctr_chart = alt.Chart(filtered_df).mark_circle(size=100, color='orange').encode(
    x="CTR",
    y="Subscribers_Gained",
    tooltip=["Category", "Views", "CTR", "Subscribers_Gained"]
)
st.altair_chart(ctr_chart, use_container_width=True)

# Likes vs Comments
st.subheader("Likes vs Comments")
likes_comments_chart = alt.Chart(filtered_df).mark_circle(size=100, color='green').encode(
    x="Likes",
    y="Comments",
    tooltip=["Category", "Views", "Likes", "Comments"]
)
st.altair_chart(likes_comments_chart, use_container_width=True)

# ==============================
# 5. CATEGORY COMPARISON
# ==============================
st.subheader("Average Views by Category")
category_views = df.groupby("Category")["Views"].mean().reset_index()
bar_chart = alt.Chart(category_views).mark_bar().encode(
    x="Category",
    y="Views",
    tooltip=["Category", "Views"]
)
st.altair_chart(bar_chart, use_container_width=True)
