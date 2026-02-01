import pytest
import pandas as pd
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

from utils.data_loader import load_data, preprocess_data

def test_load_data_invalid_path():
    with pytest.raises(FileNotFoundError):
        load_data("invalid/path.csv")

def test_preprocess_data():
    df = pd.DataFrame({
        'observation_date': ['2020-01-01', '2021-01-01'],
        'value_numeric': [10, 20]
    })
    processed_df = preprocess_data(df)
    assert pd.api.types.is_datetime64_any_dtype(processed_df['observation_date'])
