import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt

# Data
years = [2011, 2014, 2017, 2021, 2024]
account_ownership = [22.0, 22.0, 35.0, 46.0, 49.0]

# Create plot
plt.figure(figsize=(12, 8))
plt.plot(years, account_ownership, 'o-', linewidth=3, markersize=10, color='#2E86AB')

# Add labels
for year, value in zip(years, account_ownership):
    plt.annotate(f'{value:.1f}%', (year, value), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold')

# Add target line
plt.axhline(y=60, color='red', linestyle='--', linewidth=2, alpha=0.7)
plt.text(2010.5, 62, 'NFIS-II Target (60%)', fontsize=10, color='red')

# Add events
plt.axvline(x=2021, color='orange', linestyle=':', linewidth=2)
plt.text(2021, 55, 'Telebirr Launch', ha='center', fontsize=9)

plt.axvline(x=2023, color='purple', linestyle=':', linewidth=2)
plt.text(2023, 55, 'M-Pesa Entry', ha='center', fontsize=9)

# Formatting
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Percentage of Population (%)', fontsize=12, fontweight='bold')
plt.title('Financial Account Ownership Trajectory (2011-2024)', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.ylim(0, 70)
plt.xlim(2010, 2025)

# Save without showing
plt.tight_layout()
plt.savefig('reports/figures/account_ownership_trajectory.png', dpi=300, bbox_inches='tight')
print("Chart saved successfully to reports/figures/account_ownership_trajectory.png")
