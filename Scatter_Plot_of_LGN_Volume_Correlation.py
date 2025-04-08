import matplotlib.pyplot as plt 
import numpy as np

# Create the scatter plot
plt.figure(figsize=(8, 8)) plt.scatter(LGN_lh, LGN_rh, color='blue', alpha=0.7, label='Paired Samples')

# Add the diagonal x = y line
min_val = min(min(LGN_lh), min(LGN_rh)) # Minimum value for the diagonal line max_val = max(max(LGN_lh), max(LGN_rh)) # Maximum value for the diagonal line plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', label='x = y')

# Add labels and title
plt.xlabel('LGN volume lh', fontsize=12) plt.ylabel('LGN volume rh', fontsize=12) plt.title('LGN volumes lh vs rh', fontsize=14) plt.legend()

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Show the plot
plt.show()
