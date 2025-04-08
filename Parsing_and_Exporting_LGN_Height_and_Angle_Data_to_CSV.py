
import re
import csv

def parse_subject_data(file_path):
    subjects = []
    current_subject = {}

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("Subject"):
                if current_subject:
                    subjects.append(current_subject)
                subject_match = re.search(r'Subject (\d+):', line)
                current_subject = {'Subject': subject_match.group(1)}
            elif "Maximum right height:" in line:
                height_match = re.search(r'Maximum right height: ([\d.]+)', line)
                current_subject['Max Height'] = float(height_match.group(1))
            elif "Angle at maximum height:" in line:
                angle_match = re.search(r'Lateral ([-\d.]+)°, Anterior ([\d.]+)°', line)
                current_subject['Max Lateral Angle'] = float(angle_match.group(1))
                current_subject['Max Anterior Angle'] = float(angle_match.group(2))
            elif "Minimum right height:" in line:
                height_match = re.search(r'Minimum right height: ([\d.]+)', line)
                current_subject['Min Height'] = float(height_match.group(1))
            elif "Angle at minimum height:" in line:
                angle_match = re.search(r'Lateral ([-\d.]+)°, Anterior ([\d.]+)°', line)
                current_subject['Min Lateral Angle'] = float(angle_match.group(1))
                current_subject['Min Anterior Angle'] = float(angle_match.group(2))

    if current_subject:
        subjects.append(current_subject)

    return subjects

def write_csv(subjects, output_file):
    fieldnames = ['Subject', 'Max Height', 'Max Lateral Angle', 'Max Anterior Angle',
                  'Min Height', 'Min Lateral Angle', 'Min Anterior Angle']

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for subject in subjects:
            writer.writerow(subject)

# Usage
input_file = 'Height_and_Angles_right.txt' #change for left
output_file = 'Height_and_Angles_right.csv' #change for left

subjects = parse_subject_data(input_file)
write_csv(subjects, output_file)

print(f"CSV file has been created at {output_file}")
