
import pyvista as pv 
import numpy as np 
import nibabel as nib
from skimage import measure

def smooth_and_extract_surface(input_4d_file, target_volume, smoothing_sigma=1.0):
img = nib.load(input_4d_file) 
data = img.get_fdata() 
prob_map = np.mean(data, axis=3)

grid = pv.ImageData()
grid.dimensions = prob_map.shape
grid.origin = (0, 0, 0)
grid.spacing = img.header.get_zooms()[:3]
grid.point_data["values"] = prob_map.flatten(order="F")

smoothed_grid = grid.gaussian_smooth(std_dev=smoothing_sigma)
smoothed_map = smoothed_grid.point_data["values"].reshape(grid.dimensions, order="F")

voxel_volume = np.prod(img.header.get_zooms())
threshold = np.percentile(smoothed_map.flatten(), 100 * (1 - target_volume / (voxel_volume * smoothed_map.size)))

vertices, faces, _, _ = measure.marching_cubes(smoothed_map, level=threshold)
faces = np.insert(faces, 0, 3, axis=1)

mesh = pv.PolyData(vertices, faces)
return mesh
 
right_4d_file = "/Volumes/PS1TB/HCP7T/LGN/4D_and_3D_image/right_LGN_masks_4D.nii.gz" 
right_target_volume = 89.60

right_mesh = smooth_and_extract_surface(right_4d_file, right_target_volume)

plotter = pv.Plotter() 
plotter.add_mesh(right_mesh, color='blue', opacity=0.7) 
plotter.add_axes()

# Add this line to save the model
plotter.export_obj('/Volumes/PS1TB/HCP7T/LGN/4D_and_3D_image/right_LGN_model.obj')

#This line remains at the end
plotter.show()
