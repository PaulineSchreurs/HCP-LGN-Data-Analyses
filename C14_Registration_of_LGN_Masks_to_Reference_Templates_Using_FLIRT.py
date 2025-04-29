
import os 
import subprocess

# Directory and documents
INPUT_DIR = "/mnt/e/HCP7T/LGN/MNI_T1_and_Masks" 
LEFT_REF = "/mnt/e/HCP7T/LGN/MNI_T1_and_Masks/100206_LGN_mask_left_MNI.nii.gz" RIGHT_REF = "/mnt/e/HCP7T/LGN/MNI_T1_and_Masks/100206_LGN_mask_right_MNI.nii.gz" OUTPUT_DIR = "/mnt/e/HCP7T/LGN/MNI_T1_and_Masks/output"

# Make output directory if not yet excisting
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Loop through all documents in output directory
files = [f for f in os.listdir(INPUT_DIR) if 
f.endswith("_LGN_mask_MNI.nii.gz")]

if not files: 
print("Geen bestanden gevonden die voldoen aan het patroon.") 
exit(1)

for filename in files: 
# Check if the file is not the reference(100206) 
if filename.startswith("100206"): 
continue
filepath = os.path.join(INPUT_DIR, filename)


if "_left_" in filename:
    ref = LEFT_REF
    side = "left"
elif "_right_" in filename:
    ref = RIGHT_REF
    side = "right"
else:
    print(f"Onbekend masker type: {filename}")
    continue

# Genergate output file name
output_filename = f"{os.path.splitext(filename)[0]}_registered.nii.gz"
output_filepath = os.path.join(OUTPUT_DIR, output_filename)

# Perform FLIRT
try:
    subprocess.run(
        ["flirt", "-in", filepath, "-ref", ref, "-out", output_filepath],
        check=True
    )
    print(f"Geregistreerd: {filename} ({side})")
except subprocess.CalledProcessError as e:
    print(f"Fout bij registratie van {filename}: {e}")
 
print("Registratie voltooid.")
