# Task 2: EDA Insights & Data Quality Assessment

## 5 Key Insights for Ethiopia (2025)

### 1. The "Inclusion Slowdown" (2021-2024)
Despite the massive entry of Telebirr and M-Pesa, national account ownership only increased by **3 percentage points** (46% to 49%). This indicates that mobile money is largely being adopted by those who **already have bank accounts**, rather than bringing the unbanked into the formal system.

### 2. High Infrastructure-Inclusion Decoupling
4G population coverage has doubled from ~37% to over 70%, yet account ownership has not responded with the same velocity. This suggests that **connectivity is no longer the primary bottleneck**; Trust, Literacy, or Product Relevance may be the limiting factors.

### 3. Persistent Gender Parity Gap
The gender gap remains significant at approximately **20 percentage points** (56% male vs 36% female). Women's mobile money account share is particularly low at 14%, highlighting a critical policy focus area for NFIS-II.

### 4. The Registered vs. Active Paradox
Telebirr registrations (~54M) and mobile money account counts (~110M) vastly exceed the Findex-reported account ownership (~37M adults). This points to **passive usage or multiple account holdings** (sim-card stacking), suggesting that "Registered Users" is a leading but often misleading indicator for actual inclusion.

### 5. P2P Dominance as Digital Rail
Digital transactions are surging, but they occur primarily on **P2P rails** rather than merchant POS. This confirms the market nuance that small-scale commerce in Ethiopia happens via direct person-to-person transfers, bypassing traditional payment gateways.

---

## Data Quality Assessment & Limitations

### 1. Temporal Sparsity
Findex data only arrives every 3 years (2011, 2014, 2017, 2021, 2024), creating significant gaps that make traditional time-series forecasting (like ARIMA) difficult without event-augmentation.

### 2. Confidence Distribution
While "Observation" records from Findex are high-confidence, manyinfrastructure and event-impact records are categorized as **Medium** due to reporting lags or operator-provided (supply-side) bias vs. demand-side surveys.

### 3. Urban/Rural Blindspot
The current unified dataset lacks granular urban vs. rural disaggregation for most indicators, limiting our ability to model regional disparities.

### 4. Registered User Over-reporting
Supply-side data (NBE, Ethio Telecom) often lists "registered accounts," which overcounts usage compared to demand-side surveys. We must use a **deflator** or discount factor when using these as proxies for Findex outcomes.
