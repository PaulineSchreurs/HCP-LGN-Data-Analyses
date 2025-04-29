
import os 
import glob
import nibabel as nib from nilearn 
import plotting 
import numpy as np 
import matplotlib.pyplot as plt

# Directory containing the mask files
mask_dir = '/Volumes/PS1TB/HCP7T/LGN/MNI_T1_and_Masks/'

# Function to get right mask files for a specific subject
def get_right_mask_files(directory, subject_number): 
pattern = os.path.join(directory, f"{subject_number}_LGN_mask_right_MNI.nii.gz") 
return glob.glob(pattern)

# Get all subject numbers
subject_numbers = set(os.path.basename(f).split('_')[0] for f in os.listdir(mask_dir) if f.endswith('_MNI.nii.gz'))

# Initialize an empty list to store right masks
right_masks = []

# Process masks for each subject to get right masks only
for subject in subject_numbers: 
right_masks.extend([nib.load(f) for f in get_right_mask_files(mask_dir, subject)])

# Check if any right masks were found
if not right_masks: print("No right LGN masks found.") 
else: 
# Sum all right masks 
sum_mask = np.sum([m.get_fdata() for m in right_masks], axis=0)

# Create probabilistic map
prob_map = sum_mask / len(right_masks)
prob_nii = nib.Nifti1Image(prob_map, right_masks[0].affine)

# Plot the probabilistic map
plt.figure(figsize=(10, 5))
plotting.plot_stat_map(
    prob_nii,
    title="Right LGN Probabilistic Map",
    display_mode="ortho",
    colorbar=True,
    threshold=0.1
)

# Show the plot
plt.show()

# Save the probabilistic map
output_file = os.path.join(mask_dir, 'LGN_probabilistic_map_right.nii.gz')
nib.save(prob_nii, output_file)
print(f"Right probabilistic map saved as: {output_file}")

