# app_manual_data_labels.py
import streamlit as st
import pandas as pd
import altair as alt

# ==============================
# APP TITLE & DESCRIPTION
# ==============================
st.title("YouTube Video Analysis Dashboard")

st.markdown("""
Welcome to the **YouTube Video Analysis Dashboard**! 📊  

This interactive dashboard allows you to explore the performance of YouTube videos across different content categories. You can:  
- View **raw data** for each video  
- Analyze **key metrics** like average views, likes, and watch time  
- Visualize trends such as **views per video**, **CTR vs subscribers**, and **likes vs comments**  
- Compare **average views by category**  

Use the charts and tooltips to quickly gain insights into which videos are performing best and how audience engagement varies across categories.
""")

# ==============================
# 1. MANUAL DATA
# ==============================
data = [
    ["Vlog", 54.03, 782, 24.12, 570, 25, 1079354, 1346, 1767, 2744, 234459.67],
    ["Education", 22.56, 949, 70.11, 339, 23.38, 1170449, 10787, 1249, 1998, 308543.36],
    ["Reacts", 9.82, 318, 53.97, 638, 2.94, 694767, 21670, 5403, 322, 61371.08],
    ["News", 26.86, 38, 2.36, 109, 18.86, 610243, 21145, 7984, 1181, 6441.45],
    ["Vlog", 48.66, 493, 16.89, 378, 11.58, 724825, 55342, 5013, 2524, 99260.76],
    # add all remaining rows here
]

columns = [
    "Category", "Duration", "Views", "Avg_View_Percentage", "Subscribers_Gained",
    "CTR", "Impressions", "Likes", "Comments", "Shares", "Total_Watch_Hours"
]

df = pd.DataFrame(data, columns=columns)

# Add a unique label for each video to use in X-axis
df["Video_Label"] = df["Category"] + " #" + (df.index + 1).astype(str)

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

# ---- Views per Video ----
st.subheader("Views per Video")
views_chart = alt.Chart(df).mark_bar(color='skyblue').encode(
    x=alt.X("Video_Label:N", title="Video (Category + #)"),
    y=alt.Y("Views:Q", title="Views"),
    tooltip=["Video_Label", "Views", "Likes", "Comments", "Shares"]
).properties(width=800, height=400)
st.altair_chart(views_chart, use_container_width=True)

# ---- CTR vs Subscribers ----
st.subheader("CTR vs Subscribers Gained")
ctr_chart = alt.Chart(df).mark_circle(size=100, color='orange').encode(
    x=alt.X("CTR:Q", title="Click Through Rate (%)"),
    y=alt.Y("Subscribers_Gained:Q", title="Subscribers Gained"),
    tooltip=["Video_Label", "CTR", "Subscribers_Gained", "Views"]
).properties(width=800, height=400)
st.altair_chart(ctr_chart, use_container_width=True)

# ---- Likes vs Comments ----
st.subheader("Likes vs Comments")
likes_comments_chart = alt.Chart(df).mark_circle(size=100, color='green').encode(
    x=alt.X("Likes:Q", title="Likes"),
    y=alt.Y("Comments:Q", title="Comments"),
    tooltip=["Video_Label", "Likes", "Comments", "Views"]
).properties(width=800, height=400)
st.altair_chart(likes_comments_chart, use_container_width=True)

# ---- Average Views by Category ----
st.subheader("Average Views by Category")
category_views = df.groupby("Category")["Views"].mean().reset_index()
bar_chart = alt.Chart(category_views).mark_bar(color='purple').encode(
    x=alt.X("Category:N", title="Category"),
    y=alt.Y("Views:Q", title="Average Views"),
    tooltip=["Category", "Views"]
).properties(width=600, height=400)
st.altair_chart(bar_chart, use_container_width=True)
