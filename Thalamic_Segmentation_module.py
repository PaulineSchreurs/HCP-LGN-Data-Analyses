
# run thalamic segmentation === 
# https://freesurfer.net/fswiki/ThalamicNuclei 
# do this is parallel to speed it up 
from multiprocessing import Pool 
import subprocess 
  
base_command = "segmentThalamicNuclei.sh" 
def run_command(s): 
    cmd = f"{base_command} {s}" 
    result = subprocess.run(cmd, shell=True, capture_output=False, text=True) 
    #print(cmd) 
  
# Create a pool of workers 
with Pool(processes=10) as pool:   
    results = pool.map(run_command, subjects)

substring = " ".join(subjects)
print(substring)

# group output stats
!asegstats2table --statsfile=thalamic-nuclei.lh.v13.T1.stats --tablefile=thalamic-nuclei.lh.v13.T1.dat --subjects {substring} 
!asegstats2table --statsfile=thalamic-nuclei.rh.v13.T1.stats --tablefile=thalamic-nuclei.rh.v13.T1.dat --subjects {substring}

HCP7T_LGN_path = '/media/DATA1/HCP7T/LGN' os.makedirs(os.path.join(HCP7T_LGN_path,'subjects'),exist_ok=True) 
for s in subjects: 
src = os.path.join(folder_path,s,'T1w',s) 
dest = os.path.join(HCP7T_LGN_path,'subjects',s) 
shutil.copytree(src,dest)

src = '/home/chris/Documents/MRI_ANALYSIS/HCP7T/HCP7T_Process-LGN.ipynb' shutil.copy2(src,os.path.join(HCP7T_LGN_path,'HCP7T_Process-LGN.ipynb'))

src = '/home/chris/Documents/MRI_ANALYSIS/HCP7T/thalamic-nuclei.lh.v13.T1.dat' shutil.copy2(src,os.path.join(HCP7T_LGN_path,'thalamic-nuclei.lh.v13.T1.dat')) 

src = '/home/chris/Documents/MRI_ANALYSIS/HCP7T/thalamic-nuclei.rh.v13.T1.dat' shutil.copy2(src,os.path.join(HCP7T_LGN_path,'thalamic-nuclei.rh.v13.T1.dat'))

'/media/DATA1/HCP7T/LGN/thalamic-nuclei.rh.v13.T1.dat'
