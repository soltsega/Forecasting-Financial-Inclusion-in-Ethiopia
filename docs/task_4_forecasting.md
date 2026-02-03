# Task 4: Financial Inclusion Forecasting (2025-2027)

## Overview

This task generates comprehensive forecasts for Ethiopia's financial inclusion indicators with uncertainty quantification, combining historical trend analysis with event impact modeling.

## Objectives

1. **Baseline Models**: Develop trend regression models using historical Findex data
2. **Event-Augmented Forecasts**: Incorporate quantified impacts from key financial inclusion events
3. **Scenario Analysis**: Generate optimistic, base, and pessimistic scenarios
4. **Uncertainty Quantification**: Provide confidence intervals and scenario ranges
5. **Visualization**: Create comprehensive plots and summary tables

## Target Indicators

- **Access**: Account Ownership Rate (ACC_OWNERSHIP) - % of adults with financial accounts
- **Usage**: Digital Payment Usage (USG_DIGITAL_PAYMENT) - % of adults using digital payments
  - *Note: Uses Mobile Money Account Rate (ACC_MM_ACCOUNT) as proxy due to data limitations*

## Methodology

### 1. Data Preparation
- Load enriched dataset from Task 3
- Filter observations for target indicators
- Handle missing data and validate data quality

### 2. Baseline Trend Modeling
- Fit linear regression models to historical data points
- Calculate R² and RMSE for model validation
- Generate baseline projections for 2025-2027

### 3. Event Impact Integration
- Load quantified event impacts from Task 3
- Apply lag periods for delayed effects
- Create cumulative impact scenarios:
  - **Optimistic**: 120% of estimated event impacts
  - **Base**: 100% of estimated event impacts
  - **Pessimistic**: 80% of estimated event impacts

### 4. Forecast Generation
- Combine baseline trends with event impacts
- Calculate 95% confidence intervals using historical RMSE
- Generate bi-annual forecasts (January and July) for 2025-2027

### 5. Analysis & Visualization
- Time series plots with confidence bands
- Scenario comparison charts
- Summary tables with key metrics
- Target achievement analysis (NFIS-II 60% goal)

## Key Events Modeled

1. **Telebirr Launch** (2021): +7pp impact on account ownership
2. **M-Pesa Entry** (2023): +4pp impact on digital payment usage

## Forecast Results

### Account Ownership Rate
- **Current (2024)**: 49.0%
- **Projected (2027)**: 56-59% (base scenario: ~57%)
- **Annual Growth**: ~2.7pp/year
- **NFIS-II Target**: 60% by 2027 (gap: ~3pp)

### Digital Payment Usage (Mobile Money Proxy)
- **Current (2024)**: 9.45%
- **Projected (2027)**: 15-18% (base scenario: ~16%)
- **Annual Growth**: ~2.2pp/year

## Files Generated

### Data Outputs
- `../data/processed/forecasts_2025_2027.csv` - Complete forecast dataset
- `../data/processed/access_forecast_summary.csv` - Account ownership summary
- `../data/processed/usage_forecast_summary.csv` - Digital payment summary

### Visualizations
- `../reports/figures/account_ownership_rate_forecast.png` - Access forecasts
- `../reports/figures/digital_payment_usage_(mm_proxy)_forecast.png` - Usage forecasts

## Assumptions

1. **Political Stability**: No major disruptions through 2027
2. **Infrastructure Growth**: Continued 4G expansion and smartphone penetration
3. **Economic Conditions**: Stable GDP growth and income levels
4. **Regulatory Environment**: Supportive policies for financial inclusion
5. **Event Independence**: Impacts are additive without saturation effects
6. **Trend Continuation**: Historical relationships persist into future

## Limitations

1. **Data Sparsity**: Only 5 Findex surveys over 13 years
2. **Event Impact Uncertainty**: Limited validation of impact estimates
3. **Usage Proxy**: Mobile money accounts ≠ actual digital payment usage
4. **Competition Effects**: Model doesn't capture market saturation
5. **External Shocks**: No modeling of drought, conflict, or economic crises
6. **Survey Methodology**: Potential comparability issues over time

## Technical Implementation

### Key Functions
- `fit_trend_model()`: Linear regression with uncertainty quantification
- `generate_forecast()`: Baseline + event impacts with scenario multipliers
- `create_forecast_summary()`: Year-end forecast summaries
- `plot_forecast()`: Comprehensive visualization with confidence intervals

### Error Handling
- Null value validation in model fitting
- Empty DataFrame protection in summary generation
- Safe dictionary access for forecast data
- Robust data access with proper None checking

## Dependencies

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **scikit-learn**: Linear regression modeling
- **matplotlib/seaborn**: Data visualization
- **datetime**: Date handling and calculations

## Next Steps

1. **Dashboard Integration**: Use forecasts in Task 5 dashboard
2. **Model Enhancement**: Incorporate macroeconomic variables
3. **Validation**: Compare forecasts against actual data as available
4. **Scenario Expansion**: Add more granular event impact scenarios

## Usage

```python
# Run the forecasting notebook
jupyter notebook notebooks/04_forecasting.ipynb

# Key outputs will be saved to:
# - ../data/processed/forecasts_2025_2027.csv
# - ../reports/figures/
```

## Quality Assurance

- Comprehensive error handling and data validation
- Multiple scenario analysis for robustness
- Clear documentation of assumptions and limitations
- Reproducible code with version-controlled outputs

---

**Task Status**: ✅ Complete  
**Next Task**: Task 5 - Dashboard Development
