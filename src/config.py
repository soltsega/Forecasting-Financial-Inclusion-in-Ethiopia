import os

# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DATA_PATH = os.path.join(DATA_DIR, "raw", "ethiopia_fi_unified_data - ethiopia_fi_unified_data.csv")
ENRICHED_DATA_PATH = os.path.join(DATA_DIR, "processed", "ethiopia_fi_enriched_data.csv")

# Plot style
PLOT_STYLE = "whitegrid"
FIGURE_SIZE = (12, 6)
