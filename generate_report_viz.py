import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

# Add src to path
sys.path.append(os.path.abspath("src"))

from utils.data_loader import load_data, preprocess_data
from utils.plotting import set_plot_style, plot_temporal_coverage
from config import ENRICHED_DATA_PATH

# Set plot style
set_plot_style()

# Ensure reports directory exists
os.makedirs("reports/figures", exist_ok=True)

# Load data
df = load_data(ENRICHED_DATA_PATH)
df = preprocess_data(df)

# 1. Dataset Temporal Coverage
plt.figure(figsize=(12, 6))
plot_temporal_coverage(df)
plt.title("Ethiopia FI Forecasting: Dataset Temporal Coverage")
plt.savefig("reports/figures/temporal_coverage.png", bbox_inches='tight')
plt.close()

# 2. Access Analysis: Account Ownership Trajectory
acc_df = df[(df['indicator_code'] == 'ACC_FIN_ACC') & (df['record_type'] == 'observation')].dropna(subset=['observation_date']).sort_values('observation_date')
plt.figure(figsize=(10, 6))
plt.plot(acc_df['observation_date'], acc_df['value_numeric'] * 100, marker='o', linewidth=2, color='#1f77b4')
plt.fill_between(acc_df['observation_date'], acc_df['value_numeric'] * 100, alpha=0.1)
plt.title("Financial Account Ownership Trajectory (2011-2024)")
plt.ylabel("Percentage of Population (%)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig("reports/figures/account_ownership_trajectory.png")
plt.close()

# 3. Usage Analysis: Mobile Money & Digital Payments
usage_indicators = ['USG_MM_ACC', 'USG_DIG_PAY']
plt.figure(figsize=(10, 6))
for ind in usage_indicators:
    sub_df = df[(df['indicator_code'] == ind) & (df['record_type'] == 'observation')].dropna(subset=['observation_date']).sort_values('observation_date')
    plt.plot(sub_df['observation_date'], sub_df['value_numeric'] * 100, marker='s', label=ind.replace('_', ' '))

plt.title("Mobile Money and Digital Payment Usage (2014-2024)")
plt.ylabel("Percentage of Population (%)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig("reports/figures/usage_trends.png")
plt.close()

# 4. Event Timeline Overlay
# Focus on Mobile Money growth with event overlays
mm_df = df[(df['indicator_code'] == 'USG_MM_COUNT') & (df['record_type'] == 'observation')].dropna(subset=['observation_date']).sort_values('observation_date')
events = df[df['record_type'] == 'event'].dropna(subset=['observation_date']).sort_values('observation_date')

plt.figure(figsize=(12, 7))
plt.plot(mm_df['observation_date'], mm_df['value_numeric'] / 1e6, marker='o', color='green', label='Total MM Accounts (Millions)')

# Overlay events
for _, event in events.iterrows():
    plt.axvline(x=event['observation_date'], color='red', linestyle='--', alpha=0.4)
    plt.text(event['observation_date'], plt.ylim()[1]*0.9, event['indicator'], rotation=90, verticalalignment='top', fontsize=8)

plt.title("Mobile Money Growth with Key Event Overlays")
plt.ylabel("Accounts (Millions)")
plt.legend()
plt.savefig("reports/figures/event_impact_timeline.png")
plt.close()

print("Interim report visualizations generated in reports/figures/")
