
import os 
import glob 
import subprocess

# Set the directory
MASK_DIR = "/Volumes/PS1TB/HCP7T/LGN/MNI_T1_and_Masks"

# Output file
OUTPUT_FILE = os.path.join(MASK_DIR, "LGN_centers_of_mass.txt")
Initialize the output file
with open(OUTPUT_FILE, 'w') as f: f.write("Subject,Hemisphere,X,Y,Z\n")

3 Loop through all subjects
for T1_FILE in glob.glob(os.path.join(MASK_DIR, "*_T1_MNI.nii.gz")): if os.path.isfile(T1_FILE): # Extract subject ID SUBJECT_ID = os.path.basename(T1_FILE).replace("_T1_MNI.nii.gz", "")
  
 # Left LGN mask
    LEFT_MASK = os.path.join(MASK_DIR, f"{SUBJECT_ID}_LGN_mask_left_MNI.nii.gz")
    if os.path.isfile(LEFT_MASK):

        # Calculate center of mass for left LGN
        LEFT_COM = subprocess.check_output(["fslstats", LEFT_MASK, "-c"]).decode().strip()
        with open(OUTPUT_FILE, 'a') as f:
            f.write(f"{SUBJECT_ID},Left,{LEFT_COM}\n")
    else:
        print(f"Warning: Left mask not found for subject {SUBJECT_ID}")
    
    # Right LGN mask
    RIGHT_MASK = os.path.join(MASK_DIR, f"{SUBJECT_ID}_LGN_mask_right_MNI.nii.gz")
    if os.path.isfile(RIGHT_MASK):

        # Calculate center of mass for right LGN
        RIGHT_COM = subprocess.check_output(["fslstats", RIGHT_MASK, " c"]).decode().strip()
        with open(OUTPUT_FILE, 'a') as f:
            f.write(f"{SUBJECT_ID},Right,{RIGHT_COM}\n")
    else:
        print(f"Warning: Right mask not found for subject {SUBJECT_ID}")
 
print(f"Center of mass calculations complete. Results saved in {OUTPUT_FILE}")
