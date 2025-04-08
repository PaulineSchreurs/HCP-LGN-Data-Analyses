
import os 
import subprocess

# Configuration
masks_dir = "/Volumes/PS1TB/HCP7T/LGN/LGN_mask_MNI_registered" 
output_dir = "/Volumes/PS1TB/HCP7T/LGN/4D_image" # Directory to save the 4D images

# Script
def merge_masks(masks_dir, output_dir): 
""" Merges NIfTI masks into 4D volumes.
Args:
    masks_dir (str): Path to the directory containing the masks.
    output_dir (str): Path to the directory where the 4D images will be saved.
"""

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Change directory to where the masks are located
os.chdir(masks_dir)

# Merge left LGN masks
left_masks = [f for f in os.listdir(".") if "_left_aligned_MNI.nii.gz" in f]
if left_masks:
    subprocess.run(["fslmerge", "-t", os.path.join(output_dir, "left_LGN_masks_4D.nii.gz")] + left_masks, check=True)
    print(f"Left LGN masks merged. Output: {os.path.join(output_dir, 'left_LGN_masks_4D.nii.gz')}")
else:
    print("No left LGN masks found.")

# Merge right LGN masks
right_masks = [f for f in os.listdir(".") if "_right_aligned_MNI.nii.gz" in f]
if right_masks:
    subprocess.run(["fslmerge", "-t", os.path.join(output_dir, "right_LGN_masks_4D.nii.gz")] + right_masks, check=True)
    print(f"Right LGN masks merged. Output: {os.path.join(output_dir, 'right_LGN_masks_4D.nii.gz')}")
else:
    print("No right LGN masks found.")

print(f"Done! 4D images created in: {output_dir}")
 
# Run the script
if name == "main": 
merge_masks(masks_dir, output_dir)
