import streamlit as st
import pandas as pd

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="YouTube Video Analysis Dashboard", layout="wide")

st.title("📊 YouTube Video Analysis Dashboard (No Graphs, Auto Load)")

# =========================
# LOAD DATASET DIRECTLY
# =========================
DATA_PATH = r"C:\Users\Admin\OneDrive\Documents\YouTube_Video.csv"

df = pd.read_csv(DATA_PATH)

st.success("✅ Dataset Loaded Automatically")

# =========================
# BASIC INFO
# =========================
st.subheader("📌 Dataset Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Missing Values", df.isnull().sum().sum())

st.write(df.head())

# =========================
# COLUMN SELECTION & DISPLAY
# =========================
st.subheader("🎯 Column Data")

for col_name in df.columns:
    st.write(f"**Column:** {col_name}")
    st.write(df[col_name].head(10))  # show first 10 values
    st.write(df[col_name].describe() if pd.api.types.is_numeric_dtype(df[col_name]) else df[col_name].value_counts().head(10))

# =========================
# DOWNLOAD
# =========================
st.subheader("⬇ Download Dataset")
csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    "Download CSV",
    csv,
    "youtube_trending_data.csv",
    "text/csv"
)
