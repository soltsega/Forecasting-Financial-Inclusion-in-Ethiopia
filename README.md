# Forecasting Financial Inclusion in Ethiopia

## Project Overview
This project aims to build a forecasting system that tracks Ethiopia's digital financial transformation using time series methods. It focuses on predicting Access (Account Ownership Rate) and Usage (Digital Payment Adoption Rate) for the years 2025-2027.

## Folder Structure
- `data/`: Contains raw and processed datasets.
- `notebooks/`: Jupyter notebooks for data exploration and modeling.
- `src/`: Source code for the project.
- `dashboard/`: Streamlit dashboard for interactive visualization.
- `models/`: Saved models.
- `reports/`: Project reports and figures.
- `tests/`: Unit tests.

## Setup Instructions
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Place the starter datasets in `data/raw/`:
   - `ethiopia_fi_unified_data.csv`
   - `reference_codes.csv`
3. Run the dashboard:
   ```bash
   streamlit run dashboard/app.py
   ```
