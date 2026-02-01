import json
import os

nb_path = "notebooks/02_exploratory_data_analysis.ipynb"
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Cell 5: Load enriched data instead of raw
nb['cells'][4]['source'] = [
    "from config import ENRICHED_DATA_PATH\n",
    "df = load_data(ENRICHED_DATA_PATH)\n",
    "df = preprocess_data(df)\n",
    "obs_df = df[df['record_type'] == 'observation'].copy()\n",
    "# Derive 'year' column to avoid KeyError\n",
    "obs_df['year'] = obs_df['observation_date'].dt.year\n",
    "\n",
    "print(\"--- Summary by Record Type ---\")\n",
    "print(df['record_type'].value_counts())\n",
    "\n",
    "print(\"\\n--- Summary by Pillar ---\")\n",
    "print(df['pillar'].value_counts(dropna=False))\n",
    "\n",
    "print(\"\\n--- Summary by Source Type ---\")\n",
    "print(df['source_type'].value_counts())"
]

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
    f.write('\n')

print("Notebook 02 updated to use enriched data and derivation of 'year' column fixed.")
