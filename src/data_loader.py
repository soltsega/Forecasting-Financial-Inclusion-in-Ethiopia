import pandas as pd
import os

def load_unified_dataset(base_path="data/raw"):
    """
    Loads the primary unified financial inclusion dataset for Ethiopia.
    """
    filename = "ethiopia_fi_unified_data - ethiopia_fi_unified_data.csv"
    path = os.path.join(base_path, filename)
    if not os.path.exists(path):
        # Try relative to notebook
        path = os.path.join("..", base_path, filename)
        
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        raise FileNotFoundError(f"Could not find dataset at {path}")

def load_reference_codes(base_path="data/raw"):
    """
    Loads the reference codes mapping.
    """
    filename = "reference_codes - reference_codes.csv"
    path = os.path.join(base_path, filename)
    if not os.path.exists(path):
        # Try relative to notebook
        path = os.path.join("..", base_path, filename)
        
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        raise FileNotFoundError(f"Could not find reference codes at {path}")

def get_data_summary(df):
    """
    Returns a dictionary with counts of record types, pillars, and sources.
    """
    summary = {
        "record_types": df['record_type'].value_counts().to_dict(),
        "pillars": df['pillar'].value_counts(dropna=False).to_dict(),
        "sources": df['source_type'].value_counts().to_dict()
    }
    return summary
