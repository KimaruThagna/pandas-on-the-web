import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.markdown('''
# **The Streamlit X Pandas Crossover**
 **EDA Web App** 
''')

# Upload CSV data
with st.sidebar.header('1. Upload your CSV file'):
    uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache # make use of web cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    report = ProfileReport(df, explorative=True)
    st.header('** DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Results**')
    st_profile_report(report)