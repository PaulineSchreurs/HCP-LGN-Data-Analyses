# LGN Analysis Scripts – Supplementary Material

This repository contains all Python scripts used in the research project titled:

**"Structural Analysis of the Human Lateral Geniculate Nucleus Using MRI-Based Segmentation"**

Each script corresponds to a specific appendix in the supplemental materials section of the research paper. Together, they form a complete pipeline for LGN segmentation, volume and shape analysis, statistical processing, and 3D visualization in MNI space.

---

## Script Overview

|Appendix  | Title                                                                 
|----------|-----------------------------------------------------------------------
| C1       | Thalamic Segmentation Module 
| C2       | Convert Freesurfer output mgz-files to nii-files
| C3       | Volume Analyses
| C4       | Histogram Visualization of LGN Volume Distributions 
| C5       | Scatter Plot of LGN Volume Correlation 
| C6       | Raincloud Plot with Paired t-Test Analysis of LGN Volumes 
| C7       | Transformation T1 to MNI space, apply same transformation to LGN masks   
| C8       | Automated Computation of Center of Mass Coordinates in MNI Space  
| C9       | Statistical Analysis of LGN Center of Mass  
| C10      | Calculation of LGN Dimensions  
| C11      | Measure LGN dimensions along average angle from Trajectory Planning
| C12      | Creation of LGN Probability Maps in MNI Space
| C13      | Visualization of Right LGN Probabilistic Map
| C14      | Registration of LGN Masks Using FLIRT
| C15      | Merging LGN Masks into 4D Volumes Using FSL 
| C16      | Creating and Thresholding LGN Probability Maps to Target Volumes
| C17      | 3D Surface Model Extraction from Right LGN Probability Map

---

## How to Use

Each script is standalone and corresponds to a specific analysis module. Make sure you have the necessary dependencies installed, including:

- `numpy`, `scipy`, `matplotlib`, `pandas`
- `nibabel`, `nilearn`, `fslpy` (for neuroimaging work)
- `seaborn`, `ptitprince` (for visualizations like raincloud plots)

You can run scripts individually via:

```bash
python appendix_b_volume_analyses.py
