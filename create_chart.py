import matplotlib.pyplot as plt
import pandas as pd

# Data from your analysis
years = [2011, 2014, 2017, 2021, 2024]
account_ownership = [22.0, 22.0, 35.0, 46.0, 49.0]

# Create the plot
plt.figure(figsize=(12, 8))
plt.plot(years, account_ownership, 'o-', linewidth=3, markersize=10, color='#2E86AB', label='Account Ownership Rate')

# Add data point labels
for year, value in zip(years, account_ownership):
    plt.annotate(f'{value:.1f}%', (year, value), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold')

# Add NFIS-II target line
plt.axhline(y=60, color='red', linestyle='--', linewidth=2, alpha=0.7, label='NFIS-II Target (60%)')
plt.fill_between(years, 60, 70, alpha=0.1, color='red')

# Add event markers
plt.axvline(x=2021, color='orange', linestyle=':', linewidth=2, alpha=0.7)
plt.text(2021, 58, 'Telebirr\nLaunch', ha='center', fontsize=9, color='orange')

plt.axvline(x=2023, color='purple', linestyle=':', linewidth=2, alpha=0.7)
plt.text(2023, 58, 'M-Pesa\nEntry', ha='center', fontsize=9, color='purple')

# Formatting
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Percentage of Population (%)', fontsize=12, fontweight='bold')
plt.title('Financial Account Ownership Trajectory (2011-2024)', fontsize=14, fontweight='bold')
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)
plt.ylim(0, 70)
plt.xlim(2010, 2025)

# Add growth annotations
growth_rates = []
for i in range(1, len(years)):
    growth = ((account_ownership[i] - account_ownership[i-1]) / account_ownership[i-1]) * 100
    growth_rates.append(growth)
    mid_year = (years[i] + years[i-1]) / 2
    mid_value = (account_ownership[i] + account_ownership[i-1]) / 2
    if growth > 0:
        plt.annotate(f'+{growth:.0f}%', (mid_year, mid_value), textcoords="offset points", xytext=(0,-20), ha='center', fontsize=9, color='green')

plt.tight_layout()
plt.savefig('reports/figures/account_ownership_trajectory.png', dpi=300, bbox_inches='tight')
print("Chart generated successfully!")
plt.show()
