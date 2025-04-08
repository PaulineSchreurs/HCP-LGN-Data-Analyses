
import os
import nibabel as nib
import numpy as np
from scipy.spatial import distance
import csv
import re  # Import the regular expression module

def find_max_distance(mask_path):
    img = nib.load(mask_path)
    data = img.get_fdata()
    affine = img.affine
    coords = np.array(np.where(data > 0)).T
    world_coords = nib.affines.apply_affine(affine, coords)

    max_distance = 0
    point1 = point2 = None

    for i in range(len(world_coords)):
        distances = distance.cdist([world_coords[i]], world_coords)[0]
        max_dist_index = np.argmax(distances)
        if distances[max_dist_index] > max_distance:
            max_distance = distances[max_dist_index]
            point1 = world_coords[i]
            point2 = world_coords[max_dist_index]

    return max_distance, point1, point2

def process_masks(input_dir, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Subject Number', 'Side', 'Longest Distance', 'Point 1', 'Point 2'])

        # Regex pattern to match the file names
        pattern = re.compile(r"^\d+_LGN_mask_(left|right)_MNI\.nii\.gz$")

        for filename in os.listdir(input_dir):
            match = pattern.match(filename)

            if match:
                mask_path = os.path.join(input_dir, filename)

                subject_number = filename.split('_')[0]  # Extract subject number
                side = match.group(1)  # Extract 'left' or 'right'

                max_distance, point1, point2 = find_max_distance(mask_path)

                writer.writerow([
                    subject_number,
                    side,
                    f"{max_distance:.2f}",
                    f"({point1[0]:.2f}, {point1[1]:.2f}, {point1[2]:.2f})",
                    f"({point2[0]:.2f}, {point2[1]:.2f}, {point2[2]:.2f})"
                ])

if __name__ == "__main__":
    input_directory = "MNI_T1_and_Masks"
    output_csv = "longest_distances.csv"
    process_masks(input_directory, output_csv)
