import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys
import os

# Add src to path if needed
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import PLOT_STYLE, FIGURE_SIZE

def set_plot_style():
    """Set centralized plot style."""
    sns.set_theme(style=PLOT_STYLE)
    plt.rcParams['figure.figsize'] = FIGURE_SIZE

def plot_temporal_coverage(df, title="Temporal Coverage Heatmap"):
    """Plot heatmap of indicator counts per year."""
    obs_df = df[df['record_type'] == 'observation'].copy()
    if 'observation_date' not in obs_df.columns:
         return
    
    obs_df['year'] = obs_df['observation_date'].dt.year
    
    coverage = obs_df.pivot_table(
        index='indicator_code', 
        columns='year', 
        values='value_numeric', 
        aggfunc='count'
    ).fillna(0)
    
    sns.heatmap(coverage, annot=True, cmap="YlGnBu", cbar=False)
    plt.title(title)
    plt.tight_layout()

def plot_confidence_distribution(df, title="Distribution of Confidence Levels"):
    """Plot distribution of confidence levels."""
    sns.countplot(data=df, x='confidence', palette='viridis', hue='confidence', legend=False)
    plt.title(title)
    plt.tight_layout()
