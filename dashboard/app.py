import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sys
import os
from datetime import datetime, timedelta

# Add src to path
sys.path.append(os.path.abspath("src"))

# Page configuration
st.set_page_config(
    page_title="Financial Inclusion Dashboard - Ethiopia",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .insight-box {
        background-color: #e8f4f8;
        border-left: 4px solid #1f77b4;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header">📊 Financial Inclusion Dashboard - Ethiopia</h1>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Select Dashboard View:",
    ["📈 Overview", "📊 Historical Trends", "🎯 Event Analysis", "🔮 Forecasts", "📋 Insights"]
)

# Data loading functions
@st.cache_data
def load_enriched_data():
    """Load the enriched dataset from Task 3."""
    try:
        df = pd.read_csv("../data/processed/ethiopia_fi_enriched_data.csv")
        df['observation_date'] = pd.to_datetime(df['observation_date'], format='mixed', errors='coerce')
        return df
    except Exception as e:
        st.error(f"Error loading enriched data: {e}")
        return None

@st.cache_data
def load_forecast_data():
    """Load forecast data from Task 4."""
    try:
        forecast_df = pd.read_csv("../data/processed/forecasts_2025_2027.csv")
        forecast_df['date'] = pd.to_datetime(forecast_df['date'])
        return forecast_df
    except Exception as e:
        st.error(f"Error loading forecast data: {e}")
        return None

@st.cache_data
def load_summary_data():
    """Load summary tables from Task 4."""
    try:
        access_summary = pd.read_csv("../data/processed/access_forecast_summary.csv")
        usage_summary = pd.read_csv("../data/processed/usage_forecast_summary.csv")
        return access_summary, usage_summary
    except Exception as e:
        st.error(f"Error loading summary data: {e}")
        return None, None

# Load data
df = load_enriched_data()
forecast_df = load_forecast_data()
access_summary, usage_summary = load_summary_data()

if df is not None:
    # Filter data for dashboard
    obs_df = df[df['record_type'] == 'observation'].copy()
    events_df = df[df['record_type'] == 'event'].copy()
    impacts_df = df[df['record_type'] == 'impact_link'].copy()

    # Key indicators
    ACCESS_INDICATOR = 'ACC_OWNERSHIP'
    USAGE_INDICATOR = 'ACC_MM_ACCOUNT'  # Using mobile money as proxy

    # Overview Page
    if page == "📈 Overview":
        st.header("Financial Inclusion Overview")
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            latest_access = obs_df[obs_df['indicator_code'] == ACCESS_INDICATOR]['value_numeric'].max()
            st.metric("Account Ownership", f"{latest_access:.1f}%", "2024")
        
        with col2:
            latest_usage = obs_df[obs_df['indicator_code'] == USAGE_INDICATOR]['value_numeric'].max()
            st.metric("Digital Payments", f"{latest_usage:.1f}%", "2024")
        
        with col3:
            total_events = len(events_df)
            st.metric("Key Events", total_events)
        
        with col4:
            target_2027 = 60.0  # NFIS-II target
            gap = target_2027 - latest_access
            st.metric("NFIS-II Gap", f"{gap:.1f}pp", "to 60% target")
        
        # Current status chart
        st.subheader("Current Financial Inclusion Status")
        
        # Create gauge charts
        col1, col2 = st.columns(2)
        
        with col1:
            fig_access = go.Figure(go.Indicator(
                mode = "gauge+number+delta",
                value = latest_access,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Account Ownership Rate (%)"},
                delta = {'reference': target_2027},
                gauge = {
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "#1f77b4"},
                    'steps': [
                        {'range': [0, 30], 'color': "lightgray"},
                        {'range': [30, 60], 'color': "yellow"},
                        {'range': [60, 100], 'color': "green"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': target_2027
                    }
                }
            ))
            fig_access.update_layout(height=300)
            st.plotly_chart(fig_access, use_container_width=True)
        
        with col2:
            fig_usage = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = latest_usage,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Digital Payment Usage (%)"},
                gauge = {
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "#ff7f0e"},
                    'steps': [
                        {'range': [0, 20], 'color': "lightgray"},
                        {'range': [20, 50], 'color': "yellow"},
                        {'range': [50, 100], 'color': "green"}
                    ]
                }
            ))
            fig_usage.update_layout(height=300)
            st.plotly_chart(fig_usage, use_container_width=True)
        
        # Recent events
        st.subheader("Recent Key Events")
        if not events_df.empty:
            recent_events = events_df.sort_values('observation_date', ascending=False).head(5)
            for _, event in recent_events.iterrows():
                with st.expander(f"📅 {event['observation_date'].strftime('%Y-%m-%d')}: {event['indicator']}"):
                    st.write(f"**Category**: {event['category']}")
                    st.write(f"**Description**: {event.get('notes', 'No description available')}")

    # Historical Trends Page
    elif page == "📊 Historical Trends":
        st.header("Historical Trends Analysis")
        
        # Time series plot
        st.subheader("Financial Inclusion Trends (2014-2024)")
        
        # Prepare data
        access_trend = obs_df[obs_df['indicator_code'] == ACCESS_INDICATOR].sort_values('observation_date')
        usage_trend = obs_df[obs_df['indicator_code'] == USAGE_INDICATOR].sort_values('observation_date')
        
        # Create interactive plot
        fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=("Account Ownership Rate", "Digital Payment Usage (Mobile Money)"),
            vertical_spacing=0.1
        )
        
        # Account ownership trend
        fig.add_trace(
            go.Scatter(
                x=access_trend['observation_date'],
                y=access_trend['value_numeric'],
                mode='lines+markers',
                name='Account Ownership',
                line=dict(color='#1f77b4', width=3),
                marker=dict(size=8)
            ),
            row=1, col=1
        )
        
        # Digital payment trend
        fig.add_trace(
            go.Scatter(
                x=usage_trend['observation_date'],
                y=usage_trend['value_numeric'],
                mode='lines+markers',
                name='Digital Payments',
                line=dict(color='#ff7f0e', width=3),
                marker=dict(size=8)
            ),
            row=2, col=1
        )
        
        fig.update_layout(
            height=600,
            showlegend=True,
            title_text="Financial Inclusion Historical Trends"
        )
        
        fig.update_xaxes(title_text="Year", row=2, col=1)
        fig.update_yaxes(title_text="Percentage (%)", row=1, col=1)
        fig.update_yaxes(title_text="Percentage (%)", row=2, col=1)
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Growth analysis
        st.subheader("Growth Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if len(access_trend) >= 2:
                first_access = access_trend.iloc[0]['value_numeric']
                last_access = access_trend.iloc[-1]['value_numeric']
                access_growth = ((last_access - first_access) / first_access) * 100
                st.metric("Account Ownership Growth", f"{access_growth:.1f}%", "2014-2024")
        
        with col2:
            if len(usage_trend) >= 2:
                first_usage = usage_trend.iloc[0]['value_numeric']
                last_usage = usage_trend.iloc[-1]['value_numeric']
                usage_growth = ((last_usage - first_usage) / first_usage) * 100 if first_usage > 0 else 0
                st.metric("Digital Payment Growth", f"{usage_growth:.1f}%", "2014-2024")

    # Event Analysis Page
    elif page == "🎯 Event Analysis":
        st.header("Event Impact Analysis")
        
        if not events_df.empty:
            # Event timeline
            st.subheader("Event Timeline")
            
            fig_events = px.timeline(
                events_df,
                x_start="observation_date",
                x_end="observation_date",
                y="indicator",
                color="category",
                title="Financial Inclusion Events Timeline",
                labels={"indicator": "Event", "observation_date": "Date", "category": "Category"}
            )
            fig_events.update_layout(height=400)
            st.plotly_chart(fig_events, use_container_width=True)
            
            # Event impacts
            if not impacts_df.empty:
                st.subheader("Quantified Event Impacts")
                
                # Merge impacts with events
                event_impacts = pd.merge(
                    impacts_df[['parent_id', 'related_indicator', 'impact_magnitude', 'impact_direction']],
                    events_df[['record_id', 'indicator', 'observation_date']],
                    left_on='parent_id',
                    right_on='record_id'
                )
                
                if not event_impacts.empty:
                    # Impact chart
                    fig_impact = px.bar(
                        event_impacts,
                        x='indicator',
                        y='impact_magnitude',
                        color='impact_direction',
                        title="Event Impact Magnitude by Indicator",
                        labels={
                            'indicator': 'Event',
                            'impact_magnitude': 'Impact Magnitude',
                            'impact_direction': 'Direction'
                        }
                    )
                    fig_impact.update_layout(height=400)
                    st.plotly_chart(fig_impact, use_container_width=True)
                    
                    # Impact details table
                    st.subheader("Impact Details")
                    st.dataframe(
                        event_impacts[['indicator', 'related_indicator', 'impact_magnitude', 'impact_direction', 'observation_date']],
                        use_container_width=True
                    )
        else:
            st.info("No event data available.")

    # Forecasts Page
    elif page == "🔮 Forecasts":
        st.header("Financial Inclusion Forecasts (2025-2027)")
        
        if forecast_df is not None:
            # Forecast scenarios
            st.subheader("Forecast Scenarios")
            
            # Scenario selector
            scenario = st.selectbox("Select Scenario:", ["Base", "Optimistic", "Pessimistic"])
            
            # Filter forecast data
            if scenario == "Base":
                forecast_filtered = forecast_df.copy()
            else:
                # For now, show base scenario (would need scenario-specific data)
                forecast_filtered = forecast_df.copy()
            
            # Create forecast plot
            fig_forecast = make_subplots(
                rows=2, cols=1,
                subplot_titles=("Account Ownership Forecast", "Digital Payment Usage Forecast"),
                vertical_spacing=0.1
            )
            
            # Historical data
            access_hist = obs_df[obs_df['indicator_code'] == ACCESS_INDICATOR]
            usage_hist = obs_df[obs_df['indicator_code'] == USAGE_INDICATOR]
            
            # Account ownership forecast
            if not access_hist.empty:
                fig_forecast.add_trace(
                    go.Scatter(
                        x=access_hist['observation_date'],
                        y=access_hist['value_numeric'],
                        mode='lines+markers',
                        name='Historical - Access',
                        line=dict(color='#1f77b4', width=2),
                        marker=dict(size=6)
                    ),
                    row=1, col=1
                )
            
            # Digital payment forecast
            if not usage_hist.empty:
                fig_forecast.add_trace(
                    go.Scatter(
                        x=usage_hist['observation_date'],
                        y=usage_hist['value_numeric'],
                        mode='lines+markers',
                        name='Historical - Usage',
                        line=dict(color='#ff7f0e', width=2),
                        marker=dict(size=6)
                    ),
                    row=2, col=1
                )
            
            fig_forecast.update_layout(
                height=600,
                title_text=f"Financial Inclusion Forecasts - {scenario} Scenario"
            )
            
            fig_forecast.update_xaxes(title_text="Year", row=2, col=1)
            fig_forecast.update_yaxes(title_text="Percentage (%)", row=1, col=1)
            fig_forecast.update_yaxes(title_text="Percentage (%)", row=2, col=1)
            
            st.plotly_chart(fig_forecast, use_container_width=True)
            
            # Forecast summary tables
            if access_summary is not None and usage_summary is not None:
                st.subheader("Forecast Summary")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("**Account Ownership Forecasts**")
                    st.dataframe(access_summary, use_container_width=True)
                
                with col2:
                    st.write("**Digital Payment Forecasts**")
                    st.dataframe(usage_summary, use_container_width=True)
        else:
            st.error("Forecast data not available.")

    # Insights Page
    elif page == "📋 Insights":
        st.header("Key Insights & Recommendations")
        
        # Key insights
        st.markdown("### 🎯 Key Findings")
        
        insights = [
            "Account ownership has grown significantly from 22% (2014) to 49% (2024)",
            "Digital payment adoption remains low at 9.45% but shows potential for growth",
            "Major events like Telebirr launch and M-Pesa entry are driving adoption",
            "NFIS-II 60% target requires accelerated growth of ~3pp by 2027",
            "Mobile money shows strong growth potential, doubling from 2021 to 2024"
        ]
        
        for insight in insights:
            st.markdown(f'<div class="insight-box">💡 {insight}</div>', unsafe_allow_html=True)
        
        # Recommendations
        st.markdown("### 📋 Policy Recommendations")
        
        recommendations = [
            "Accelerate digital infrastructure development in rural areas",
            "Strengthen consumer protection and financial literacy programs",
            "Promote competition among mobile money providers",
            "Support agent network expansion for last-mile access",
            "Integrate informal financial services into formal system"
        ]
        
        for i, rec in enumerate(recommendations, 1):
            st.markdown(f"**{i}.** {rec}")
        
        # Data quality notes
        st.markdown("### ⚠️ Data Limitations")
        
        limitations = [
            "Limited data points (5 Findex surveys over 13 years)",
            "Mobile money usage used as proxy for digital payments",
            "Event impact estimates based on limited validation",
            "External factors (economic shocks, climate events) not fully modeled"
        ]
        
        for limitation in limitations:
            st.markdown(f"- {limitation}")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "Financial Inclusion Dashboard - Ethiopia | Task 5 | "
    f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    "</div>",
    unsafe_allow_html=True
)
