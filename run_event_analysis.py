import pandas as pd
import numpy as np
import os
import sys

# Define path directly for this script execution
ENRICHED_DATA_PATH = r"c:\Users\My Device\Desktop\Forecasting-Financial-Inclusion-in-Ethiopia\data\processed\ethiopia_fi_enriched_data.csv"

def run_analysis():
    print(f"Loading data from {ENRICHED_DATA_PATH}...")
    try:
        df = pd.read_csv(ENRICHED_DATA_PATH)
    except FileNotFoundError:
        print("Error: File not found.")
        return

    # Filter Events
    events_df = df[df['record_type'] == 'event'].copy()
    
    # Filter Impact Links (checking for 'impact_link' or 'impact')
    impacts_df = df[df['record_type'] == 'impact_link'].copy()
    
    print(f"Found {len(events_df)} Events and {len(impacts_df)} Impact Links.")

    if len(impacts_df) == 0:
        print("WARNING: No impact links found. Checking unique record types...")
        print(df['record_type'].unique())
        return

    # Join tables
    merged_df = pd.merge(
        impacts_df,
        events_df[['record_id', 'indicator', 'observation_date', 'notes']],
        left_on='parent_id',
        right_on='record_id',
        suffixes=('_impact', '_event')
    )
    
    if len(merged_df) == 0:
        print("WARNING: Merge resulted in 0 records. Checking parent_id match...")
        print("Sample Impact parent_ids:", impacts_df['parent_id'].unique()[:5])
        print("Sample Event record_ids:", events_df['record_id'].unique()[:5])
        return

    # Create Matrix
    matrix_data = merged_df[['indicator_event', 'indicator_code', 'value_numeric']]
    
    association_matrix = matrix_data.pivot_table(
        index='indicator_event',
        columns='indicator_code',
        values='value_numeric',
        fill_value=0
    )
    
    print("\n--- Event-Indicator Association Matrix ---")
    print(association_matrix)
    
    # Validation Statistics
    print("\n--- Validation: Telebirr Impact ---")
    telebirr_impact = merged_df[merged_df['indicator_event'].str.contains('Telebirr', case=False)]
    if not telebirr_impact.empty:
        print(telebirr_impact[['indicator_event', 'indicator_code', 'value_numeric']])
    else:
        print("No specific Telebirr impact record found in linked data.")

if __name__ == "__main__":
    run_analysis()
