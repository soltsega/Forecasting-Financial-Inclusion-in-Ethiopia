import pandas as pd
import matplotlib.pyplot as plt

# Data
account_data = {
    'year': [2011, 2014, 2017, 2021, 2024],
    'account_ownership': [22.0, 22.0, 35.0, 46.0, 49.0]
}

df = pd.DataFrame(account_data)

# Create plot
plt.figure(figsize=(12, 8))
plt.plot(df['year'], df['account_ownership'], 'o-', linewidth=3, markersize=8, color='#2E86AB')

# Add labels
for i, row in df.iterrows():
    plt.annotate(f'{row["account_ownership"]:.1f}%', 
                (row['year'], row['account_ownership']),
                textcoords="offset points", xytext=(0,10), ha='center')

# Add target line
plt.axhline(y=60, color='red', linestyle='--', alpha=0.7, label='NFIS-II Target (60%)')

# Add event markers
plt.axvline(x=2021, color='orange', linestyle=':', alpha=0.7, label='Telebirr Launch')
plt.axvline(x=2023, color='purple', linestyle=':', alpha=0.7, label='M-Pesa Entry')

plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Percentage of Population (%)', fontsize=12, fontweight='bold')
plt.title('Financial Account Ownership Trajectory (2011-2024)', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.ylim(0, 70)
plt.tight_layout()

# Save
plt.savefig('reports/figures/account_ownership_trajectory.png', dpi=300, bbox_inches='tight')
plt.show()
print("Chart saved to reports/figures/account_ownership_trajectory.png")
