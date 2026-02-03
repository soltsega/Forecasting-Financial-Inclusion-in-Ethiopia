import json

# Load notebook
with open('notebooks/03_event_impact_modeling.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Fix Cell 2: Change from markdown to code
nb['cells'][2]['cell_type'] = 'code'
nb['cells'][2]['execution_count'] = None
nb['cells'][2]['metadata'] = {}
nb['cells'][2]['outputs'] = []
nb['cells'][2]['source'] = [
    "# Load enriched dataset\n",
    "ENRICHED_DATA_PATH = \"../data/processed/ethiopia_fi_enriched_data.csv\"\n",
    "df = pd.read_csv(ENRICHED_DATA_PATH)\n",
    "\n",
    "print(\"Unique Record Types:\", df['record_type'].unique())\n",
    "print(f\"\\nDataset shape: {df.shape}\")"
]

# Delete Cell 4 (the duplicate at index 4)
# Cell indices: 0=title, 1=imports, 2=load, 3=filter, 4=DUPLICATE (delete this)
del nb['cells'][4]

# Add os.makedirs to Cell 9 (the heatmap cell, now at index 8 after deletion)
# Find the heatmap cell
for i, cell in enumerate(nb['cells']):
    if 'association_matrix' in ''.join(cell.get('source', [])) and 'heatmap' in ''.join(cell.get('source', [])):
        # Add mkdir before savefig
        source = cell['source']
        for j, line in enumerate(source):
            if 'plt.tight_layout()' in line:
                # Insert mkdir before tight_layout
                source.insert(j, "    os.makedirs('../reports/figures', exist_ok=True)\n")
                break
        cell['source'] = source
        break

# Save
with open('notebooks/03_event_impact_modeling.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)

print("✅ Fixed all notebook issues:")
print("  - Cell 2: Changed from markdown to code")
print("  - Cell 4: Deleted duplicate cell")
print("  - Added os.makedirs for reports/figures directory")
