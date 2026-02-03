import pandas as pd

# Load data
df = pd.read_csv('data/processed/ethiopia_fi_enriched_data.csv')

with open('task3_data_inspection.txt', 'w', encoding='utf-8') as f:
    f.write("="*80 + "\n")
    f.write("IMPACT_LINKS DATA\n")
    f.write("="*80 + "\n")
    impact_links = df[df['record_type'] == 'impact_link'].copy()
    f.write(f"\nTotal Impact Links: {len(impact_links)}\n")
    f.write(f"\nColumns: {impact_links.columns.tolist()}\n")

    # Check key fields
    key_fields = ['record_id', 'parent_id', 'pillar', 'related_indicator', 
                  'impact_direction', 'impact_magnitude', 'lag_months', 
                  'confidence', 'evidence_basis']

    f.write("\n" + "="*80 + "\n")
    f.write("IMPACT LINKS DETAILS\n")
    f.write("="*80 + "\n")
    for col in key_fields:
        if col in impact_links.columns:
            f.write(f"\n{col}:\n")
            f.write(str(impact_links[col].value_counts(dropna=False).head()) + "\n")
        else:
            f.write(f"\n{col}: COLUMN NOT FOUND\n")

    f.write("\n" + "="*80 + "\n")
    f.write("SAMPLE IMPACT LINKS\n")
    f.write("="*80 + "\n")
    cols_to_show = [c for c in key_fields if c in impact_links.columns]
    f.write(impact_links[cols_to_show].to_string(index=False) + "\n")

    f.write("\n" + "="*80 + "\n")
    f.write("EVENTS DATA\n")
    f.write("="*80 + "\n")
    events = df[df['record_type'] == 'event'].copy()
    f.write(f"\nTotal Events: {len(events)}\n")
    f.write("\nEvent Details:\n")
    event_cols = ['record_id', 'indicator', 'observation_date', 'category', 'notes']
    cols_to_show_events = [c for c in event_cols if c in events.columns]
    f.write(events[cols_to_show_events].to_string(index=False) + "\n")

print("Data inspection saved to task3_data_inspection.txt")
