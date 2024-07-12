
# File Uploader: Create an app that lets users upload and process files (e.g., CSV, Excel).

import streamlit as st
import pandas as pd

st.title("File Uploader")

# File upload
uploaded_file = st.file_uploader("Upload a file (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Process the uploaded file
    df = pd.read_csv(uploaded_file)  # For Excel, use pd.read_excel(uploaded_file)
    st.write("Uploaded Data:")
    st.write(df)
