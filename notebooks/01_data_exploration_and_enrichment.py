#!/usr/bin/env python
# coding: utf-8

# # Task 1: Data Exploration and Enrichment
# This notebook focuses on understanding the starter dataset and enriching it with additional data for the forecasting task.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

# Add src to path
sys.path.append(os.path.abspath("../src"))

from utils.data_loader import load_data, preprocess_data
from utils.plotting import set_plot_style

# Set plot style
set_plot_style()


# ## 1. Load the starter dataset

# In[2]:


df = load_data()
df = preprocess_data(df)
df.head()


# ## 2. Explore the Data
# ### 2.1 Count records by record_type, pillar, source_type, and confidence

# In[3]:


cols_to_count = ['record_type', 'pillar', 'source_type', 'confidence']
for col in cols_to_count:
    print(f"--- {col} counts ---")
    print(df[col].value_counts(dropna=False))
    print("\n")


# ### 2.2 Identify the temporal range of observations

# In[4]:


obs_df = df[df['record_type'] == 'observation'].copy()
# observation_date is already converted to datetime by preprocess_data
print(f"Temporal range of observations: {obs_df['observation_date'].min()} to {obs_df['observation_date'].max()}")


# ### 2.3 List all unique indicators and their coverage

# In[5]:


indicators = df[df['record_type'] == 'observation']['indicator_code'].unique()
print(f"Unique indicators: {indicators}")

# Coverage per indicator
df[df['record_type'] == 'observation'].groupby('indicator_code')['observation_date'].count().sort_values(ascending=False)


# ## 3. Data Enrichment & Impact Links
# This section programmatically enriches the dataset with new records and impact links using the `parent_id` field to establish clear causal relationships.

# In[6]:


# Create a list for new records
new_records = []

# 1. Add 2024 mobile money baseline (Usage Pillar)
new_records.append({
    'indicator': 'Total Mobile Money Accounts',
    'indicator_code': 'USG_MM_COUNT',
    'value_numeric': 110000000,
    'observation_date': '2024-06-30',
    'record_type': 'observation',
    'pillar': 'USAGE',
    'source_type': 'regulator',
    'confidence': 'high',
    'note': 'Estimated from National Bank of Ethiopia reports.'
})

# 2. Add IMF Credit Facility Approval (Policy Event)
new_records.append({
    'indicator': 'IMF ECF Approval',
    'indicator_code': 'EVT_IMF_ECF',
    'value_numeric': 1, # Event binary
    'observation_date': '2024-07-29',
    'record_type': 'event',
    'pillar': None,
    'source_type': 'policy',
    'confidence': 'high',
    'note': 'Four-year arrangement approved.'
})

enriched_df = pd.concat([df, pd.DataFrame(new_records)], ignore_index=True)
print("Base enrichment completed.")


# ### 3.1 Explicit Impact Link Example (parent_id based)
# Here we link a specific event (Telebirr Launch) to its observed impact on mobile money account counts using the `parent_id` column. This makes causal relationships explicit in the data.

# In[7]:


# Locate the Telebirr Launch event ID (if it exists) or create it
telebirr_launch = enriched_df[
    (enriched_df['indicator'].str.contains('Telebirr', case=False, na=False)) & 
    (enriched_df['record_type'] == 'event')
].iloc[0] if not enriched_df[
    (enriched_df['indicator'].str.contains('Telebirr', case=False, na=False)) & 
    (enriched_df['record_type'] == 'event')
].empty else None

if telebirr_launch is not None:
    # Add an impact_link record pointing back to this event via parent_id
    impact_link = {
        'indicator': 'Telebirr Impact on MM Growth',
        'indicator_code': 'IMP_TELEBIRR_MM',
        'record_type': 'impact_link',
        'parent_id': 14, # Example explicit ID pointing to Telebirr Launch in raw
        'note': 'Explicit link between launch event and subsequent account growth.',
        'confidence': 'high'
    }

    enriched_df = pd.concat([enriched_df, pd.DataFrame([impact_link])], ignore_index=True)
    print("Explicit impact link added via parent_id.")
else:
    print("Telebirr Launch event not found to link against.")


# ## 4. Save the Enriched Dataset
# We now use the centralized `save_data` utility to persist the enriched dataset for use in subsequent analysis notebooks.

# In[8]:


from utils.data_loader import save_data

# Filter logic (optional: ensure column order or specific filtering)
save_data(enriched_df)
print(f"Enriched dataset saved with {len(enriched_df)} records.")

