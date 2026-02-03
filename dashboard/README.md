# Financial Inclusion Dashboard - Ethiopia

## Overview

Interactive Streamlit dashboard for visualizing and analyzing financial inclusion trends, events, and forecasts in Ethiopia. This dashboard integrates data from all previous tasks to provide comprehensive insights for policymakers, financial analysts, and researchers.

## Features

### 📈 Overview Page
- **Key Metrics**: Current account ownership and digital payment rates
- **NFIS-II Target Tracking**: Progress towards 60% account ownership goal
- **Interactive Gauges**: Visual representation of current status
- **Recent Events**: Timeline of key financial inclusion events

### 📊 Historical Trends Page
- **Time Series Analysis**: Interactive plots of account ownership and digital payment usage (2014-2024)
- **Growth Metrics**: Percentage growth calculations and trends
- **Multi-indicator Views**: Side-by-side comparison of access and usage metrics

### 🎯 Event Analysis Page
- **Event Timeline**: Visual timeline of financial inclusion events
- **Impact Quantification**: Bar charts showing event impact magnitudes
- **Event Details**: Detailed information about each event and its effects

### 🔮 Forecasts Page
- **Scenario Analysis**: Base, optimistic, and pessimistic forecast scenarios
- **Historical + Forecast**: Combined view of historical data and future projections
- **Summary Tables**: Year-by-year forecast summaries with confidence intervals

### 📋 Insights Page
- **Key Findings**: Automated insights from the analysis
- **Policy Recommendations**: Actionable recommendations for stakeholders
- **Data Limitations**: Transparent documentation of constraints

## Technology Stack

- **Frontend**: Streamlit
- **Visualization**: Plotly (interactive charts, gauges, timelines)
- **Data Processing**: Pandas, NumPy
- **Styling**: Custom CSS for enhanced UI

## Data Sources

The dashboard integrates data from multiple sources:

1. **Enriched Dataset** (`../data/processed/ethiopia_fi_enriched_data.csv`)
   - Historical observations (2014-2024)
   - Event catalog with impact quantification
   - Impact links and relationships

2. **Forecast Data** (`../data/processed/forecasts_2025_2027.csv`)
   - Baseline and scenario-based forecasts
   - Confidence intervals
   - Year-end projections

3. **Summary Tables** (`../data/processed/*_forecast_summary.csv`)
   - Consolidated forecast summaries
   - Target achievement analysis

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Dependencies
```bash
pip install streamlit pandas numpy plotly
```

### Running the Dashboard

1. **Navigate to dashboard directory**:
   ```bash
   cd dashboard
   ```

2. **Run Streamlit app**:
   ```bash
   streamlit run app.py
   ```

3. **Open browser**: The dashboard will open at `http://localhost:8501`

## Dashboard Structure

```
dashboard/
├── app.py              # Main Streamlit application
├── README.md           # This file
└── assets/            # Static assets (if needed)
```

## Key Features Explained

### Interactive Visualizations
- **Gauge Charts**: Real-time status indicators with target tracking
- **Time Series**: Historical trend analysis with zoom and pan capabilities
- **Timeline Charts**: Event visualization with color-coded categories
- **Bar Charts**: Impact magnitude comparisons
- **Data Tables**: Sortable, filterable data displays

### Data Integration
- **Cached Loading**: Efficient data loading with Streamlit caching
- **Error Handling**: Robust error handling for missing or corrupted data
- **Real-time Updates**: Dynamic data refresh capabilities

### User Experience
- **Responsive Design**: Works on desktop and mobile devices
- **Intuitive Navigation**: Sidebar-based page navigation
- **Custom Styling**: Professional appearance with custom CSS
- **Export Capabilities**: Data export functionality (planned)

## Configuration

### Page Configuration
```python
st.set_page_config(
    page_title="Financial Inclusion Dashboard - Ethiopia",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)
```

### Data Paths
- Enriched data: `../data/processed/ethiopia_fi_enriched_data.csv`
- Forecast data: `../data/processed/forecasts_2025_2027.csv`
- Summary data: `../data/processed/*_forecast_summary.csv`

## Usage Guide

### For Policymakers
1. **Start with Overview**: Get current status and target progress
2. **Review Forecasts**: Understand future projections and scenarios
3. **Check Insights**: Review policy recommendations

### For Financial Analysts
1. **Historical Trends**: Analyze growth patterns and rates
2. **Event Analysis**: Understand impact of key events
3. **Forecast Details**: Review confidence intervals and assumptions

### For Researchers
1. **Data Exploration**: Use interactive charts to explore trends
2. **Event Impact**: Study quantified event effects
3. **Limitations**: Review data constraints and methodology

## Customization

### Adding New Pages
1. Add page option to sidebar selectbox
2. Create new elif block for page logic
3. Implement page-specific visualizations

### Modifying Visualizations
- Edit Plotly chart configurations
- Update color schemes and styling
- Add new chart types as needed

### Data Updates
- Update data file paths in loading functions
- Modify data processing logic as needed
- Update indicator codes and mappings

## Performance Considerations

- **Data Caching**: Uses `@st.cache_data` for efficient loading
- **Lazy Loading**: Data loaded only when needed
- **Optimized Charts**: Efficient Plotly configurations
- **Memory Management**: Proper data cleanup and filtering

## Future Enhancements

### Planned Features
- [ ] Export functionality for charts and data
- [ ] User authentication and access control
- [ ] Real-time data integration
- [ ] Advanced filtering and search
- [ ] Custom report generation
- [ ] Mobile app version

### Technical Improvements
- [ ] Database integration for larger datasets
- [ ] API endpoints for external access
- [ ] Automated data refresh
- [ ] Performance optimization
- [ ] Enhanced error handling

## Troubleshooting

### Common Issues

1. **Data Loading Errors**
   - Check file paths and permissions
   - Verify data file formats
   - Review error messages in console

2. **Visualization Issues**
   - Clear browser cache
   - Check Plotly version compatibility
   - Verify data types and formats

3. **Performance Issues**
   - Reduce data size for testing
   - Check memory usage
   - Optimize chart configurations

### Getting Help
- Review Streamlit documentation
- Check Plotly chart reference
- Review data processing logic
- Contact development team

## Contributing

### Development Setup
1. Clone repository
2. Install dependencies
3. Run dashboard locally
4. Make changes and test

### Code Standards
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test all changes thoroughly
- Update documentation

## License

This dashboard is part of the Financial Inclusion Forecasting project for Ethiopia.

---

**Project Status**: ✅ Task 5 Complete  
**Last Updated**: 2025-02-03  
**Version**: 1.0.0
