import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Event-Indicator Association Data
events = [
    'Telebirr Launch',
    'M-Pesa Entry', 
    '4G Expansion',
    'Agent Network Regulation',
    'Digital ID Initiative',
    'COVID-19 Response'
]

indicators = [
    'Account Ownership',
    'Digital Payments',
    'Mobile Money',
    'Agent Network',
    'Digital Literacy'
]

# Impact scores (-2 to +2 scale)
# Positive impacts: 1 (low), 2 (medium), 3 (high)
# Negative impacts: -1 (low), -2 (medium), -3 (high)
impact_matrix = np.array([
    [3, 2, 3, 1, 2],  # Telebirr Launch
    [2, 3, 3, 2, 1],  # M-Pesa Entry
    [1, 2, 2, 3, 1],  # 4G Expansion
    [2, 1, 1, 3, 2],  # Agent Network Regulation
    [2, 2, 1, 1, 3],  # Digital ID Initiative
    [-1, 2, 1, -2, 1]  # COVID-19 Response
])

# Create DataFrame
df = pd.DataFrame(impact_matrix, index=events, columns=indicators)

# Create the heatmap
plt.figure(figsize=(12, 8))

# Create custom colormap
cmap = sns.diverging_palette(240, 10, as_cmap=True)

# Create heatmap
sns.heatmap(df, 
            annot=True, 
            cmap=cmap, 
            center=0,
            square=True,
            fmt='.0f',
            cbar_kws={'label': 'Impact Score (-3 to +3)'},
            linewidths=0.5)

# Add title and labels
plt.title('Event-Indicator Association Matrix', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Financial Inclusion Indicators', fontsize=12, fontweight='bold')
plt.ylabel('Key Events', fontsize=12, fontweight='bold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

# Add impact legend text
plt.figtext(0.02, 0.02, 
            'Impact Scale: +3 (High Positive) | +2 (Medium Positive) | +1 (Low Positive) | 0 (No Impact) | -1 (Low Negative) | -2 (Medium Negative) | -3 (High Negative)',
            fontsize=9, style='italic', wrap=True)

# Highlight key insights with annotations
plt.annotate('Strongest Impact', xy=(0.5, 0.2), xytext=(0.7, 0.3),
             arrowprops=dict(arrowstyle='->', color='red', lw=2),
             fontsize=10, color='red', fontweight='bold')

plt.annotate('Negative Impact', xy=(3.5, 5.2), xytext=(4.5, 5.5),
             arrowprops=dict(arrowstyle='->', color='blue', lw=2),
             fontsize=10, color='blue', fontweight='bold')

plt.tight_layout()
plt.savefig('reports/figures/event_indicator_matrix.png', dpi=300, bbox_inches='tight')
print("Event-Indicator Association Matrix saved successfully!")
print("Key insights:")
print("- Telebirr Launch has strongest impact on Account Ownership (+3)")
print("- M-Pesa Entry strongly impacts Digital Payments (+3)")
print("- COVID-19 had negative impact on Agent Network (-2)")
