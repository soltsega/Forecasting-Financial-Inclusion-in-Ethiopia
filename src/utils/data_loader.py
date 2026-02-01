import pandas as pd
import os
import sys

# Add src to path if needed
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import RAW_DATA_PATH, ENRICHED_DATA_PATH

def load_data(file_path=RAW_DATA_PATH):
    """
    Load CSV data with error handling.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found at: {file_path}")
    
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise Exception(f"Error loading data from {file_path}: {e}")

def preprocess_data(df):
    """
    Apply shared cleaning logic.
    """
    df = df.copy()
    
    # Convert dates for observations
    if 'observation_date' in df.columns:
        df['observation_date'] = pd.to_datetime(df['observation_date'], errors='coerce')
    
    return df

def save_data(df, file_path=ENRICHED_DATA_PATH):
    """
    Save DataFrame to CSV with directory creation.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        df.to_csv(file_path, index=False)
        print(f"Data saved successfully to {file_path}")
    except Exception as e:
        raise Exception(f"Error saving data to {file_path}: {e}")
