import pandas as pd
path = r"c:\Users\My Device\Desktop\Forecasting-Financial-Inclusion-in-Ethiopia\data\processed\ethiopia_fi_enriched_data.csv"
df = pd.read_csv(path)

impacts = df[df['record_type'] == 'impact_link']
print("Impact Links keys:")
print(impacts.keys())
print("Impact Links Data:")
print(impacts[['record_type', 'parent_id', 'indicator_code', 'value_numeric', 'confidence']].to_string())

with open("debug_output.txt", "w") as f:
    f.write(impacts[['record_type', 'parent_id', 'indicator_code', 'value_numeric', 'confidence']].to_string())
