# app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set page config
st.set_page_config(
    page_title="Multi-Language Business Dashboard",
    page_icon="📊",
    layout="wide"
)

# ... [KODE UTAMA YANG SUDAH DIPERBAIKI SEBELUMNYA MASUK DI SINI] ...

# Add custom CSS
st.markdown("""
<style>
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #4e8cff;
    }
    .stDownloadButton > button {
        width: 100%;
    }
    .css-1d391kg {padding-top: 2rem;}
</style>
""", unsafe_allow_html=True)