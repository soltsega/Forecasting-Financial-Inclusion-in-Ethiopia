import streamlit as st
import sys
import os

# Add src to path
sys.path.append(os.path.abspath("src"))

from utils.data_loader import load_data, preprocess_data
from utils.plotting import set_plot_style

# Set plot style
set_plot_style()

st.title("Forecasting Financial Inclusion in Ethiopia")

# Load data
try:
    df = load_data()
    df = preprocess_data(df)
    st.success("Data loaded and preprocessed successfully.")
    
    st.subheader("Dataset Overview")
    st.write(df.head())
    
except Exception as e:
    st.error(f"Error loading data: {e}")

st.write("Welcome to the Financial Inclusion Forecasting Dashboard.")
