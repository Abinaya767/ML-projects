import streamlit as st
import pandas as pd
import plotly.express as px

# ===============================
# 1. APP INTRODUCTION
# ===============================
st.set_page_config(page_title="YouTube Video Analytics", layout="wide")

st.markdown("""
# YouTube Video Analytics Dashboard

Visualize your YouTube video performance with **Likes, Comments, and Views**.  
Compare engagement metrics across different **content categories**.  

**Features:**
- Category-wise totals for Likes, Comments, and Views
- Interactive Likes vs Comments bar charts
- Views visualization per category
""")

# ===============================
# 2. RAW DATA
# ===============================
data = {
    "Category": ["Vlog","Education","Reacts","News","Vlog","Comedy","Education","Comedy","Vlog","Education","Comedy","News","Music","Gaming","Music","Vlog","Reacts","Gaming",
                 "Sports","News","Sports","Education","Gaming","Sports","Sports","Comedy","Music","Comedy","Gaming","Gaming","Vlog","Comedy","Tech","Music","Gaming",
                 "Vlog","Comedy","Music","Comedy","Sports","Vlog","Music","Education","Education","Music","Comedy","Vlog","Education","Vlog","Education","Sports","Comedy",
                 "Sports","Education","Education","Tech","Music","News","Gaming","Tech","Vlog","Gaming","Sports","Comedy","Vlog","Vlog"],
    "Likes": [782,949,318,38,493,514,85,1827,1880,914,401,803,1958,1870,506,143,302,2685,944,962,276,83,948,19,153,3402,859,331,29,3151,154,22,760,304,356,528,595,371,1512,501,2176,116,2255,2115,161,651,756,40,192,1596,1966,6,624,2267,99,507,177,179,291,839,682,1379,381,472,2648,925,2493,1173,170,441,1240,1944,2163,2050,41,52,868,1220,300,1708],
    "Comments": [24.12,70.11,53.97,2.36,16.89,17.79,16.71,71.29,94.55,41.02,62.64,26.13,54.72,83.4,20.8,48.15,29.16,78.26,39.1,47.83,71.65,18.18,27.82,14.01,45.29,95.07,57.24,21.65,1.98,89.45,29.43,3.57,35.44,12.16,18.07,16.94,64.6,18.78,98.63,68.72,76.05,32.99,74.72,96.95,37.32,18.51,28.81,22.15,59.48,58.62,75,1.3,20.59,86.72,17.5,20.99,53.83,12.72,8.96,62.2,77.48,47.46,29.98,71.58,92.41,74.73,90.48,69.38,16.83,21.42,71.61,60.19,95.45,72.16,12.52,2.54,75.82,58.26,85.91,59.62],
    "Views": [234459.67,308543.36,61371.08,6441.45,99260.76,283994.57,30611.07,455658.88,446547.52,360631.14,162924.52,216994.24,913204.67,948995.91,115327.8,3245.74,117094.21,1145338.96,180012.93,25481.78,50531.84,23827.11,100772.66,1862.63,54098.34,1744826.26,89869.77,73110.91,885.51,598084.31,46671.62,489.49,221111.87,154180.95,115460.59,208402.77,62178,55480.06,802144.98,9865.39,974038.65,59275.19,39445.59,369243.16,70560.26,14598.49,84450.03,21299.51,21602.67,308598.57,227516.99,939.26,203973.12,924710.56,22312.18,162758.55,71755.8,45832.2,69137.48,158927.58,364161.1,390608.26,177147.64,166111.35,1280521.31,410434.32,1354707.28,1230.35,38612.01,60598.18,119616.94,175926.6,871755.69,541865.11,1416.65,27714.05,25562.84,305038.63,135138.33,216699.65]
}

df = pd.DataFrame(data)

# ===============================
# 3. CATEGORY-WISE TOTALS
# ===============================
st.subheader("Total Likes, Comments, and Views per Category")
category_totals = df.groupby("Category").sum().reset_index()
st.dataframe(category_totals)

# ===============================
# 4. INTERACTIVE BAR CHART: LIKES VS COMMENTS
# ===============================
st.subheader("Likes vs Comments per Video Category")

fig_likes_comments = px.bar(df, 
                            x="Category", 
                            y=["Likes", "Comments"], 
                            barmode="group",
                            title="Likes vs Comments per Video Category",
                            labels={"value":"Count", "Category":"Video Category"},
                            height=500)
st.plotly_chart(fig_likes_comments, use_container_width=True)

# ===============================
# 5. INTERACTIVE BAR CHART: VIEWS PER CATEGORY
# ===============================
st.subheader("Total Views per Category")

fig_views = px.bar(category_totals, 
                   x="Category", 
                   y="Views", 
                   color="Views",
                   title="Total Views by Video Category",
                   labels={"Views":"Total Views", "Category":"Video Category"},
                   height=500)
st.plotly_chart(fig_views, use_container_width=True)
