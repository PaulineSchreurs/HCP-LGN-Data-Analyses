
import os
import nibabel as nib
import numpy as np
from scipy.ndimage import rotate
import glob
import time
import csv

def find_max_and_min_right_height(mask, t1, mni, lateral_range, anterior_range, csv_file):
    # Load images
    mask_img = nib.load(mask)
    t1_img = nib.load(t1)
    mni_img = nib.load(mni)

    # Get data
    mask_data = mask_img.get_fdata()
    t1_data = t1_img.get_fdata()
    mni_data = mni_img.get_fdata()

    # Convert angle ranges to radians
    lateral_range_rad = np.radians(lateral_range)
    anterior_range_rad = np.radians(anterior_range)

    # List to store all height measurements
    height_measurements = []

    # Open CSV file for writing
    with open(csv_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Lateral', 'Anterior', 'Height'])

        # Iterate through angles
        for lateral in np.arange(lateral_range_rad[0], lateral_range_rad[1], np.radians(1)):
            for anterior in np.arange(anterior_range_rad[0], anterior_range_rad[1], np.radians(1)):
                # Rotate mask
                rotated_mask = rotate(mask_data, np.degrees(lateral), axes=(1,2), reshape=False)
                rotated_mask = rotate(rotated_mask, np.degrees(anterior), axes=(0,2), reshape=False)

                # Find right side (assuming right is negative in x-axis)
                right_side = rotated_mask[:, :mask_data.shape[1]//2, :]

                # Find maximum height
                height = np.sum(right_side, axis=(1,2))
                max_height_angle = np.max(height)

                height_measurements.append((max_height_angle, np.degrees(lateral), np.degrees(anterior)))
                
                # Write to CSV
                csvwriter.writerow([f"{np.degrees(la  teral):.2f}", f"{np.degrees(anterior):.2f}", f"{max_height_angle:.2f}"])

    # Find the maximum and minimum height measurements
    max_height, max_lateral, max_anterior = max(height_measurements, key=lambda x: x[0])
    min_height, min_lateral, min_anterior = min(height_measurements, key=lambda x: x[0])

    # Set maximum height as x-axis
    t1_reoriented = np.rot90(t1_data, k=1, axes=(0,1))
    mni_reoriented = np.rot90(mni_data, k=1, axes=(0,1))

    return max_height, (max_lateral, max_anterior), min_height, (min_lateral, min_anterior), t1_reoriented, mni_reoriented, t1_img.affine, mni_img.affine

# Set paths
base_dir = "/Volumes/PS1TB/HCP7T/LGN/MNI_T1_and_Masks/"
mni_file = "/Users/paulineschreurs/fsl/data/standard/MNI152_T1_1mm.nii.gz"
csv_dir = "/Volumes/PS1TB/HCP7T/LGN/Height_Measurement_csv_files"

# Ensure the CSV directory exists
os.makedirs(csv_dir, exist_ok=True)

# Set angle ranges
lateral_range = (-22, -2)
anterior_range = (21, 41)

# Get all right LGN mask files
mask_files = glob.glob(os.path.join(base_dir, "*_LGN_mask_right_MNI.nii.gz"))

# Process each subject
for mask_file in mask_files:
    # Extract subject ID from the mask file name
    subject_id = os.path.basename(mask_file).split('_')[0]
    
    # Construct T1 file path
    t1_file = os.path.join(base_dir, f"{subject_id}_T1_MNI.nii.gz")
    
    # Construct CSV file path
    csv_file = os.path.join(csv_dir, f"{subject_id}_angle_measurements.csv")
    
    # Check if files exist
    if not os.path.exists(t1_file):
        print(f"T1 file not found for subject {subject_id}. Skipping this subject.")
        continue
    
    print(f"Processing subject {subject_id}...")
    start_time = time.time()
    
    try:
        max_height, max_angle, min_height, min_angle, t1_reoriented, mni_reoriented, t1_affine, mni_affine = find_max_and_min_right_height(mask_file, t1_file, mni_file, lateral_range, anterior_range, csv_file)
        
        # Save reoriented images
        nib.save(nib.Nifti1Image(t1_reoriented, t1_affine), os.path.join(base_dir, f'{subject_id}_T1_reoriented.nii.gz'))
        nib.save(nib.Nifti1Image(mni_reoriented, mni_affine), os.path.join(base_dir, f'{subject_id}_MNI_reoriented.nii.gz'))
        
        end_time = time.time()
        
        print(f"\nSubject {subject_id}:")
        print(f"  Maximum right height: {max_height}")
        print(f"  Angle at maximum height: Lateral {max_angle[0]:.2f}°, Anterior {max_angle[1]:.2f}°")
        print(f"  Minimum right height: {min_height}")
        print(f"  Angle at minimum height: Lateral {min_angle[0]:.2f}°, Anterior {min_angle[1]:.2f}°")
        print(f"  Reoriented T1 and MNI images saved.")
        print(f"  CSV file with all angle measurements saved: {csv_file}")
        print(f"  Processing time: {end_time - start_time:.2f} seconds")
    
    except Exception as e:
        print(f"Error processing subject {subject_id}: {str(e)}")

print("Processing complete for all subjects.")

