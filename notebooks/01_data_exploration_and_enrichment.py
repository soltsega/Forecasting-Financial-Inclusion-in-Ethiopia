#!/usr/bin/env python
# coding: utf-8

# # Task 1: Data Exploration and Enrichment
# This notebook focuses on understanding the starter dataset and enriching it with additional data for the forecasting task.

# In[ ]:


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

# In[ ]:


df = load_data()
df = preprocess_data(df)
df.head()


# ## 2. Explore the Data
# ### 2.1 Count records by record_type, pillar, source_type, and confidence

# In[ ]:


cols_to_count = ['record_type', 'pillar', 'source_type', 'confidence']
for col in cols_to_count:
    print(f"--- {col} counts ---")
    print(df[col].value_counts(dropna=False))
    print("\n")


# ### 2.2 Identify the temporal range of observations

# In[ ]:


obs_df = df[df['record_type'] == 'observation'].copy()
# observation_date is already converted to datetime by preprocess_data
print(f"Temporal range of observations: {obs_df['observation_date'].min()} to {obs_df['observation_date'].max()}")


# ### 2.3 List all unique indicators and their coverage

# In[ ]:


indicators = df[df['record_type'] == 'observation']['indicator_code'].unique()
print(f"Unique indicators: {indicators}")

# Coverage per indicator
df[df['record_type'] == 'observation'].groupby('indicator_code')['observation_date'].count().sort_values(ascending=False)

