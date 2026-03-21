import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="YouTube Dashboard", layout="wide")

st.title("📊 YouTube Video Analysis Dashboard")

# =========================
# LOAD EXCEL FILE
# =========================
uploaded_file = st.file_uploader("📂 Upload Excel File", type=["xlsx"])

if uploaded_file is not None:

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

    numeric_cols = df.select_dtypes(include=['int64','float64']).columns
    all_cols = df.columns

    col = st.selectbox("Select Column", all_cols)

    # =========================
    # STATISTICS
    # =========================
    st.subheader("📊 Statistics")
    st.write(df[col].describe())

    # =========================
    # FILTER
    # =========================
    st.subheader("🔍 Filter Data")

    if col in numeric_cols:
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
    # GRAPH SECTION
    # =========================
    st.subheader("📈 Data Visualization")

    chart_type = st.selectbox("Choose Chart", ["Histogram", "Bar Chart", "Line Chart"])

    if col in numeric_cols:
        fig, ax = plt.subplots()

        if chart_type == "Histogram":
            ax.hist(df[col])
        elif chart_type == "Line Chart":
            ax.plot(df[col])
        elif chart_type == "Bar Chart":
            df[col].value_counts().head(10).plot(kind='bar', ax=ax)

        st.pyplot(fig)
    else:
        st.warning("⚠️ Select numeric column for better visualization")

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
