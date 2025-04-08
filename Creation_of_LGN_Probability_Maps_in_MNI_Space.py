import os 
import glob 
import nibabel as nib
import numpy as np

# Configuration
input_dir = "/Volumes/PS1TB/HCP7T/LGN/MNI_T1_and_Masks" 
output_dir = "/Volumes/PS1TB/HCP7T/LGN/Probability_Maps_MNI"

#Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

def create_probability_map(hemisphere): 
# Get all mask files for the given hemisphere mask_files = glob.glob(os.path.join(input_dir, f"*LGN_mask{hemisphere}_MNI.nii.gz"))

if not mask_files:
    print(f"No {hemisphere} LGN masks found.")
    return

# Load the first mask to get dimensions and affine
first_mask = nib.load(mask_files[0])
shape = first_mask.shape
affine = first_mask.affine

# Initialize sum array
sum_array = np.zeros(shape)

# Sum all masks
for mask_file in mask_files:
    mask = nib.load(mask_file).get_fdata()
    sum_array += mask

# Calculate probability
prob_map = sum_array / len(mask_files)

# Create and save the probability map
prob_img = nib.Nifti1Image(prob_map, affine)
output_file = os.path.join(output_dir, f"{hemisphere}_LGN_probability_map_MNI.nii.gz")
nib.save(prob_img, output_file)
print(f"Probability map created: {output_file}")
 
Create probability maps for left and right LGN
for hemisphere in ["left", "right"]: create_probability_map(hemisphere)
print("Probability maps creation completed.")
