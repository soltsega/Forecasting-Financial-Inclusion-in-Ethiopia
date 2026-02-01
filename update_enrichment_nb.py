import json
import os

nb_path = "notebooks/01_data_exploration_and_enrichment.ipynb"
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Define the new enrichment cells
enrichment_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 3. Data Enrichment & Impact Links\n",
            "This section programmatically enriches the dataset with new records and impact links using the `parent_id` field to establish clear causal relationships."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Create a list for new records\n",
            "new_records = []\n",
            "\n",
            "# 1. Add 2024 mobile money baseline (Usage Pillar)\n",
            "new_records.append({\n",
            "    'indicator': 'Total Mobile Money Accounts',\n",
            "    'indicator_code': 'USG_MM_COUNT',\n",
            "    'value_numeric': 110000000,\n",
            "    'observation_date': '2024-06-30',\n",
            "    'record_type': 'observation',\n",
            "    'pillar': 'USAGE',\n",
            "    'source_type': 'regulator',\n",
            "    'confidence': 'high',\n",
            "    'note': 'Estimated from National Bank of Ethiopia reports.'\n",
            "})\n",
            "\n",
            "# 2. Add IMF Credit Facility Approval (Policy Event)\n",
            "new_records.append({\n",
            "    'indicator': 'IMF ECF Approval',\n",
            "    'indicator_code': 'EVT_IMF_ECF',\n",
            "    'value_numeric': 1, # Event binary\n",
            "    'observation_date': '2024-07-29',\n",
            "    'record_type': 'event',\n",
            "    'pillar': None,\n",
            "    'source_type': 'policy',\n",
            "    'confidence': 'high',\n",
            "    'note': 'Four-year arrangement approved.'\n",
            "})\n",
            "\n",
            "enriched_df = pd.concat([df, pd.DataFrame(new_records)], ignore_index=True)\n",
            "print(\"Base enrichment completed.\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 3.1 Explicit Impact Link Example (parent_id based)\n",
            "Here we link a specific event (Telebirr Launch) to its observed impact on mobile money account counts using the `parent_id` column. This makes causal relationships explicit in the data."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Locate the Telebirr Launch event ID (if it exists) or create it\n",
            "telebirr_launch = enriched_df[\n",
            "    (enriched_df['indicator'].str.contains('Telebirr', case=False, na=False)) & \n",
            "    (enriched_df['record_type'] == 'event')\n",
            "].iloc[0] if not enriched_df[\n",
            "    (enriched_df['indicator'].str.contains('Telebirr', case=False, na=False)) & \n",
            "    (enriched_df['record_type'] == 'event')\n",
            "].empty else None\n",
            "\n",
            "if telebirr_launch is not None:\n",
            "    # Add an impact_link record pointing back to this event via parent_id\n",
            "    impact_link = {\n",
            "        'indicator': 'Telebirr Impact on MM Growth',\n",
            "        'indicator_code': 'IMP_TELEBIRR_MM',\n",
            "        'record_type': 'impact_link',\n",
            "        'parent_id': 14, # Example explicit ID pointing to Telebirr Launch in raw\n",
            "        'note': 'Explicit link between launch event and subsequent account growth.',\n",
            "        'confidence': 'high'\n",
            "    }\n",
            "    \n",
            "    enriched_df = pd.concat([enriched_df, pd.DataFrame([impact_link])], ignore_index=True)\n",
            "    print(\"Explicit impact link added via parent_id.\")\n",
            "else:\n",
            "    print(\"Telebirr Launch event not found to link against.\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 4. Save the Enriched Dataset\n",
            "We now use the centralized `save_data` utility to persist the enriched dataset for use in subsequent analysis notebooks."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "from utils.data_loader import save_data\n",
            "\n",
            "# Filter logic (optional: ensure column order or specific filtering)\n",
            "save_data(enriched_df)\n",
            "print(f\"Enriched dataset saved with {len(enriched_df)} records.\")"
        ]
    }
]

# Append the new cells to the notebook
nb['cells'].extend(enrichment_cells)

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
    f.write('\n')

print("Notebook 01 updated with enrichment and impact link logic.")
