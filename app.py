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
