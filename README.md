# LGN Analysis Scripts – Supplementary Material

This repository contains all Python scripts used in the research project titled:

**"Structural Analysis of the Human Lateral Geniculate Nucleus (LGN) Using MRI-Based Segmentation"**

Each script corresponds to a specific appendix in the supplemental materials section of the research paper. Together, they form a complete pipeline for LGN segmentation, volume and shape analysis, statistical processing, and 3D visualization in MNI space.

---

## Script Overview

|Appendix  | Title                                                                 
|----------|-----------------------------------------------------------------------
| A        | Thalamic Segmentation Module 
| B        | Volume Analyses 
| C        | Histogram Visualization of LGN Volume Distributions 
| D        | Scatter Plot of LGN Volume Correlation
| E        | Raincloud Plot with Paired t-Test Analysis of LGN Volumes
| F        | Center of Mass Coordinates in MNI Space
| G        | Statistical Analysis of LGN Center of Mass
| H        | Calculation of LGN Dimensions
| I        | Right LGN Height Across Rotational Angles
| J        | Aggregation of LGN Height with Angle Extraction
| K        | Export LGN Height & Angle Data to CSV
| L        | Longest Distance Between LGN Mask Points
| M        | Creation of LGN Probability Maps in MNI Space
| N        | Visualization of Right LGN Probabilistic Map
| O        | Registration of LGN Masks Using FLIRT
| P        | Merging LGN Masks into 4D Volumes Using FSL 
| Q        | Thresholding LGN Probability Maps to Target Volumes
| R        | 3D Surface Model Extraction from Right LGN Probability Map

---

## How to Use

Each script is standalone and corresponds to a specific analysis module. Make sure you have the necessary dependencies installed, including:

- `numpy`, `scipy`, `matplotlib`, `pandas`
- `nibabel`, `nilearn`, `fslpy` (for neuroimaging work)
- `seaborn`, `ptitprince` (for visualizations like raincloud plots)

You can run scripts individually via:

```bash
python appendix_b_volume_analyses.py
