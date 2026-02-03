import json

# Load notebook
with open('notebooks/03_event_impact_modeling.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Cell 2 should be: Load data
nb['cells'][2]['source'] = [
    "# Load enriched dataset\n",
    "ENRICHED_DATA_PATH = \"../data/processed/ethiopia_fi_enriched_data.csv\"\n",
    "df = pd.read_csv(ENRICHED_DATA_PATH)\n",
    "\n",
    "print(\"Unique Record Types:\", df['record_type'].unique())\n",
    "print(f\"\\nDataset shape: {df.shape}\")"
]

# Cell 3 should be: Filter events and impacts
nb['cells'][3]['source'] = [
    "# Filter Events and Impact Links\n",
    "events_df = df[df['record_type'] == 'event'].copy()\n",
    "events_df['observation_date'] = pd.to_datetime(events_df['observation_date'], format='mixed', errors='coerce')\n",
    "\n",
    "impacts_df = df[df['record_type'] == 'impact_link'].copy()\n",
    "\n",
    "print(f\"Found {len(events_df)} Events and {len(impacts_df)} Impact Links.\")\n",
    "print(\"\\nEvents:\")\n",
    "display(events_df[['record_id', 'indicator', 'observation_date', 'category']].dropna(subset=['record_id']))\n",
    "\n",
    "print(\"\\nImpact Links:\")\n",
    "display(impacts_df[['record_id', 'parent_id', 'pillar', 'related_indicator', \n",
    "                    'impact_direction', 'impact_magnitude', 'lag_months']].dropna(subset=['record_id']))"
]

# Fix observation date parsing in later cells
for i, cell in enumerate(nb['cells']):
    source_text = ''.join(cell.get('source', []))
    if 'obs_df' in source_text and 'observation_date' in source_text:
        # Find and fix the line
        new_source = []
        for line in cell['source']:
            if "pd.to_datetime(obs_df['observation_date'])" in line and 'format=' not in line:
                line = line.replace(
                    "pd.to_datetime(obs_df['observation_date'])",
                    "pd.to_datetime(obs_df['observation_date'], format='mixed', errors='coerce')"
                )
            new_source.append(line)
        cell['source'] = new_source

# Save
with open('notebooks/03_event_impact_modeling.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)

print("✅ Fixed notebook cells properly")
