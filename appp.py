import streamlit as st
import pandas as pd

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="YouTube Dashboard", layout="wide")

st.title("📊 YouTube Video Analysis Dashboard (No Graphs)")

# =========================
# FILE UPLOAD
# =========================
uploaded_file = st.file_uploader("📂 Upload Excel File", type=["xlsx"])

if uploaded_file is not None:

    # Read Excel file
    df = pd.read_excel(uploaded_file)
    st.success("✅ File Loaded Successfully")

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
    # COLUMN SELECT
    # =========================
    st.subheader("🎯 Column Selection")
    all_cols = df.columns
    col = st.selectbox("Select Column", all_cols)

    st.write(df[col])

    # =========================
    # STATISTICS
    # =========================
    st.subheader("📊 Statistics")
    st.write(df[col].describe())

    # =========================
    # FILTER
    # =========================
    st.subheader("🔍 Filter Data")

    if pd.api.types.is_numeric_dtype(df[col]):
        min_val = int(df[col].min())
        max_val = int(df[col].max())
        values = st.slider("Select Range", min_val, max_val, (min_val, max_val))
        filtered_df = df[(df[col] >= values[0]) & (df[col] <= values[1])]
        st.write(filtered_df)
    else:
        unique_vals = df[col].unique()
        selected = st.multiselect("Select Values", unique_vals)
        if selected:
            filtered_df = df[df[col].isin(selected)]
            st.write(filtered_df)

    # =========================
    # TOP VALUES
    # =========================
    st.subheader("🏆 Top 10 Values")
    st.write(df[col].value_counts().head(10))

    # =========================
    # DELETE COLUMN
    # =========================
    st.subheader("🗑 Manage Columns")

    del_col = st.selectbox("Select Column to Delete", df.columns)

    if st.button("Delete Column"):
        df = df.drop(columns=[del_col])
        st.success(f"{del_col} deleted ✅")
        st.write(df.head())

    # =========================
    # DOWNLOAD
    # =========================
    st.subheader("⬇ Download Cleaned Data")

    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        "Download CSV",
        csv,
        "cleaned_data.csv",
        "text/csv"
    )

else:
    st.warning("⚠️ Upload Excel file to start analysis")
