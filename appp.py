import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# 1. TITLE
# =============================
st.title("📊 YouTube Video Data Analysis")

# ==============================
# 2. LOAD DATASET
# ==============================
file_path = r"C:\Users\Admin\OneDrive\Documents\YouTube_Video.csv"

try:
    df = pd.read_csv(file_path)
    st.success("Dataset Loaded Successfully ✅")
except:
    st.error("Error loading file ❌ Check file path")
    st.stop()

# ==============================
# 3. SHOW DATA
# ==============================
st.subheader("🔍 Dataset Preview")
st.write(df.head())

# ==============================
# 4. COLUMN DETAILS
# ==============================
st.subheader("📌 Column Names")
st.write(df.columns)

st.subheader("📊 Dataset Info")
st.write(df.describe())

# ==============================
# 5. SELECT COLUMN
# ==============================
st.subheader("🎯 Select Column")
column = st.selectbox("Choose any column", df.columns)

st.write("Selected Column:", column)
st.write(df[column])

# ==============================
# 6. FILTER DATA
# ==============================
st.subheader("🔎 Filter Data")

if df[column].dtype == 'int64' or df[column].dtype == 'float64':
    min_val = int(df[column].min())
    max_val = int(df[column].max())

    val = st.slider("Select range", min_val, max_val, (min_val, max_val))
    filtered_df = df[(df[column] >= val[0]) & (df[column] <= val[1])]

    st.write(filtered_df)

# ==============================
# 7. PLOT GRAPH
# ==============================
st.subheader("📈 Simple Plot")

if df[column].dtype == 'int64' or df[column].dtype == 'float64':
    fig, ax = plt.subplots()
    ax.hist(df[column])
    st.pyplot(fig)

# ==============================
# 8. DELETE COLUMN OPTION
# ==============================
st.subheader("🗑 Delete Column")

del_col = st.selectbox("Select column to delete", df.columns)

if st.button("Delete Column"):
    df = df.drop(columns=[del_col])
    st.success(f"{del_col} column deleted ✅")
    st.write(df.head())

# ==============================
# 9. DOWNLOAD CLEANED DATA
# ==============================
st.subheader("⬇ Download Data")

csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download CSV",
    data=csv,
    file_name='cleaned_data.csv',
    mime='text/csv',
)
