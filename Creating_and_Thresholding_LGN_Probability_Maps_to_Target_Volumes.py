
import nibabel as nib 
import numpy as np 
import os

def create_probability_map(input_4d_file, output_file): 
img = nib.load(input_4d_file) 
data = img.get_fdata()
prob_map = np.mean(data, axis=3) 
prob_img = nib.Nifti1Image(prob_map, img.affine, img.header) 
nib.save(prob_img, output_file) 
return output_file

def threshold_to_target_volume(prob_map_file, target_volume, tolerance=0.01): 
img = nib.load(prob_map_file) 

data = img.get_fdata() voxel_volume = np.prod(img.header.get_zooms())

low, high = 0, 1
while high - low > tolerance:
    threshold = (low + high) / 2
    binary_mask = (data > threshold).astype(np.int16)
    current_volume = np.sum(binary_mask) * voxel_volume
    
    if current_volume > target_volume:
        low = threshold
    else:
        high = threshold

return threshold, binary_mask, img.affine, img.header
 
# File paths
left_4d_file = "/Volumes/PS1TB/HCP7T/LGN/4D_image/left_LGN_masks_4D.nii.gz" 
right_4d_file = "/Volumes/PS1TB/HCP7T/LGN/4D_image/right_LGN_masks_4D.nii.gz" 
output_dir = "/Volumes/PS1TB/HCP7T/LGN/4D_image"

# Create probability maps
left_prob_map = create_probability_map(left_4d_file, os.path.join(output_dir, "left_LGN_prob_map.nii.gz")) 
right_prob_map = create_probability_map(right_4d_file, os.path.join(output_dir, "right_LGN_prob_map.nii.gz"))

# Set your target volumes here (in mm³)
left_target_volume = 95.02 # Replace with actual average left LGN volume right_target_volume = 89.60 # Replace with your actual average right LGN volume

# Threshold probability maps to target volumes
left_threshold, left_mask, left_affine, left_header = threshold_to_target_volume(left_prob_map, left_target_volume) 
right_threshold, right_mask, right_affine, right_header = threshold_to_target_volume(right_prob_map, right_target_volume)

#Save thresholded masks
nib.save(nib.Nifti1Image(left_mask, left_affine, left_header), os.path.join(output_dir, "left_LGN_thresholded.nii.gz")) 
nib.save(nib.Nifti1Image(right_mask, right_affine, right_header), os.path.join(output_dir, "right_LGN_thresholded.nii.gz"))

print(f"Left LGN optimal threshold: {left_threshold}") 
print(f"Right LGN optimal threshold: {right_threshold}") 
print(f"Thresholded masks saved in: {output_dir}")

