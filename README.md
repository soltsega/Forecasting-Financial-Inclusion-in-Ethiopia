# Forecasting Financial Inclusion in Ethiopia

## Project Overview
This project aims to build a forecasting system that tracks Ethiopia's digital financial transformation using time series methods. It focuses on predicting **Access** (Account Ownership Rate) and **Usage** (Digital Payment Adoption Rate) for the years 2025-2027.

## Repository Structure
- `data/`: 
  - `raw/`: Starter datasets including `ethiopia_fi_unified_data.csv` and `reference_codes.csv`.
  - `processed/`: Intermediate data files used for modeling.
- `notebooks/`: 
  - `01_data_exploration_and_enrichment.ipynb`: Task 1 - Data profiling and enrichment.
  - `02_exploratory_data_analysis.ipynb`: Task 2 - Visualizations and insights.
- `src/`: Core logic and modular components.
  - `data_loader.py`: Shared functions for loading data.
- `dashboard/`: Streamlit dashboard for interactive visualization.
- `models/`: Serialized models and configurations.
- `reports/`: Documentation and generated figures.

## Setup Instructions

### 1. Environment Setup
It is recommended to use a virtual environment:
```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Running EDA
Open the Jupyter notebooks in the `notebooks/` directory to follow the analysis.

### 4. Running the Dashboard
To see the interactive insights:
```bash
streamlit run dashboard/app.py
```

## Task 1 & 2 Highlights
- **Enriched Dataset**: Added 2024 mobile money baselines and IMF policy events.
- **Key Insight**: Identified the "Inclusion Slowdown" (2021-2024) where registered users grew faster than actual ownership.
- **Data Quality**: Documented temporal sparsity and supply-side reporting bias.
