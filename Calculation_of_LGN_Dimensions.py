
import nibabel as nib
import numpy as np

def calculate_dimensions(mask_path):
    # Load the NIfTI file
    img = nib.load(mask_path)
    data = img.get_fdata()
    affine = img.affine

    # Define the voxel dimensions
    voxel_size = np.abs(np.diag(affine)[:3])

    # Find the non-zero voxels (mask)
    mask_coords = np.where(data > 0)

    # Convert voxel coordinates to mm
    x_mm = mask_coords[0] * voxel_size[0]
    y_mm = mask_coords[1] * voxel_size[1]
    z_mm = mask_coords[2] * voxel_size[2]

    # Define the angle of the height axis
    # Assuming -8 degrees lateral and -33 degrees anterior relative to y-axis
    # Convert angles to radians
    lateral_angle_rad = np.deg2rad(-8)
    anterior_angle_rad = np.deg2rad(-33)

    # Define the height axis vector (assuming y-axis is anterior-posterior)
    height_axis = np.array([
        np.sin(lateral_angle_rad) * np.cos(anterior_angle_rad),
        np.cos(lateral_angle_rad) * np.cos(anterior_angle_rad),
        np.sin(anterior_angle_rad)
    ])

    # Normalize the height axis vector
    height_axis = height_axis / np.linalg.norm(height_axis)

    # Project the mask coordinates onto the height axis
    height_projections = np.dot(np.array([x_mm, y_mm, z_mm]).T, height_axis)

    # Calculate the height
    height_mm = np.max(height_projections) - np.min(height_projections)

    # Calculate the length and width perpendicular to the height axis
    # First, find the plane perpendicular to the height axis
    # We can use the cross product to find two orthogonal vectors in this plane
    # For simplicity, let's use the standard x and z axes as references
    # to find vectors orthogonal to the height axis
    x_axis = np.array([1, 0, 0])
    z_axis = np.array([0, 0, 1])

    # Find a vector orthogonal to both height_axis and x_axis
    if np.linalg.norm(np.cross(height_axis, x_axis)) > 0:
        length_axis = np.cross(height_axis, x_axis)
    else:
        length_axis = np.cross(height_axis, z_axis)

    # Normalize the length axis vector
    length_axis = length_axis / np.linalg.norm(length_axis)

    # Find a vector orthogonal to both height_axis and length_axis
    width_axis = np.cross(height_axis, length_axis)
    width_axis = width_axis / np.linalg.norm(width_axis)

    # Project the mask coordinates onto the length and width axes
    length_projections = np.dot(np.array([x_mm, y_mm, z_mm]).T, length_axis)
    width_projections = np.dot(np.array([x_mm, y_mm, z_mm]).T, width_axis)

    # Calculate the length and width
    length_mm = np.max(length_projections) - np.min(length_projections)
    width_mm = np.max(width_projections) - np.min(width_projections)

    return height_mm, length_mm, width_mm

# Example usage
mask_path = 'path/to/your_lgn_mask.nii.gz'
height_mm, length_mm, width_mm = calculate_dimensions(mask_path)

print(f"Height: {height_mm} mm, Length: {length_mm} mm, Width: {width_mm} mm")

