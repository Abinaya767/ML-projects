# app_manual_data.py
import streamlit as st
import pandas as pd
import altair as alt

st.title("YouTube Video Analysis Dashboard")

# ==============================
# 1. MANUAL DATA (from your raw data)
# ==============================
data = [
    ["Vlog", 54.03, 782, 24.12, 570, 25, 1079354, 1346, 1767, 2744, 234459.67],
    ["Education", 22.56, 949, 70.11, 339, 23.38, 1170449, 10787, 1249, 1998, 308543.36],
    ["Reacts", 9.82, 318, 53.97, 638, 2.94, 694767, 21670, 5403, 322, 61371.08],
    ["News", 26.86, 38, 2.36, 109, 18.86, 610243, 21145, 7984, 1181, 6441.45],
    ["Vlog", 48.66, 493, 16.89, 378, 11.58, 724825, 55342, 5013, 2524, 99260.76],
    ["Comedy", 48.15, 514, 17.79, 548, 14.84, 1989067, 53248, 6019, 2315, 283994.57],
    ["Education", 8.48, 85, 16.71, 255, 1, 1296469, 17508, 1041, 1481, 30611.07],
    ["Comedy", 42.71, 1827, 71.29, 104, 23.46, 897850, 21002, 5620, 1120, 455658.88],
    ["Vlog", 33.14, 1880, 94.55, 378, 18.62, 855091, 10258, 3755, 1836, 446547.52],
    ["Education", 37.14, 914, 41.02, 483, 27.87, 1420429, 92630, 2450, 2207, 360631.14],
    # ... continue adding all your rows here
]

columns = [
    "Category", "Duration", "Views", "Avg_View_Percentage", "Subscribers_Gained",
    "CTR", "Impressions", "Likes", "Comments", "Shares", "Total_Watch_Hours"
]

df = pd.DataFrame(data, columns=columns)

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
