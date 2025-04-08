# read in the tables
import pandas as pd

# Read the .dat file
file = 'thalamic-nuclei.lh.v13.T1.dat' thal_lh = pd.read_csv(file, sep='\t')
file = 'thalamic-nuclei.rh.v13.T1.dat' thal_rh = pd.read_csv(file, sep='\t')

LGN_lh = thal_lh['LGN'](0.7**3) # correct for voxel size meta data 
LGN_rh = thal_rh['LGN'](0.7**3)
