import pandas as pd
path = r"c:\Users\My Device\Desktop\Forecasting-Financial-Inclusion-in-Ethiopia\data\processed\ethiopia_fi_enriched_data.csv"
df = pd.read_csv(path)
print("Columns:", df.columns.tolist())
print("\nUnique Record Types:", df['record_type'].unique())
print("\nSample Events:")
print(df[df['record_type'] == 'event'].head())
print("\nSample Impact Links:")
print(df[df['record_type'] == 'impact_link'].head())
