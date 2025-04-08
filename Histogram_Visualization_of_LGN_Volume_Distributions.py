import matplotlib.pyplot as plt 
import numpy as np

# Calculate mean and standard deviation for both datasets
mean1, std1 = np.mean(LGN_lh), np.std(LGN_lh) mean2, std2 = np.mean(LGN_rh), np.std(LGN_rh)

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot the first histogram
ax1.hist(LGN_lh, bins=50, color='grey', edgecolor='black', alpha=0.7) 
ax1.axvline(mean1, color='red', linestyle='dashed', linewidth=2, label=f'Mean = {mean1:.2f}') 
ax1.axvline(mean1 - std1, color='blue', linestyle='dotted', linewidth=2, label=f'±1 Std Dev = {std1:.2f}') 
ax1.axvline(mean1 + std1, color='blue', linestyle='dotted', linewidth=2) 
ax1.set_title('LGN lh') 
ax1.set_xlabel('LGN volume (mm3)') 
ax1.set_ylabel('Frequency (n=181)') 
ax1.legend()

# Plot the second histogram
ax2.hist(LGN_rh, bins=50, color='grey', edgecolor='black', alpha=0.7) 
ax2.axvline(mean2, color='red', linestyle='dashed', linewidth=2, label=f'Mean = {mean2:.2f}') 
ax2.axvline(mean2 - std2, color='blue', linestyle='dotted', linewidth=2, label=f'±1 Std Dev = {std2:.2f}') 
ax2.axvline(mean2 + std2, color='blue', linestyle='dotted', linewidth=2) 
ax2.set_title('LGN rh') 
ax2.set_xlabel('LGN volume (mm3)') 
ax2.set_ylabel('Frequency (n=181)') 
ax2.legend()

# Adjust layout and display the plot
plt.tight_layout() plt.show()
