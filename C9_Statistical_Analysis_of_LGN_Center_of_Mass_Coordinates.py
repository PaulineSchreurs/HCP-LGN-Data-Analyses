import pandas as pd 
import numpy as np

# Read the file
with open('/Volumes/PS1TB/HCP7T/LGN/MNI_T1_and_Masks/LGN_centers_of_mass.txt', 'r') as file: 
lines = file.readlines()

# Remove the header
header = lines.pop(0).strip().split(',')

# Create a list of dictionaries for each row
data = [] 
for line in lines: 
values = line.strip().split(',') 
subject = values[0] 
hemisphere = values[1] 
x, y, z = map(float, values[2].split()) 
data.append({ 
'Subject': subject, 
'Hemisphere': hemisphere, 
'X': x, 
'Y': y, 
'Z': z 
})

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Calculate the statistics
stats = df.groupby('Hemisphere').agg({ 
'X': ['mean', 'std'],
'Y': ['mean', 'std'], 
'Z': ['mean', 'std'] 
})

print(stats)
