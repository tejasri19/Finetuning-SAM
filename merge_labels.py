import os
import json

# Directory containing your image files
image_folder = 'dataset/data/new_test/image'
label_folder = 'dataset/data/new_test/labels'

# List all image files in the folder
image_files = [f for f in os.listdir(image_folder) if f.endswith(".jpg")]

# List all label files in the folder
label_files = [f for f in os.listdir(label_folder) if f.endswith(".txt")]

image_files.sort()
label_files.sort()

# Initialize an empty dictionary to store data
data_dict = {}

for img, label in zip(image_files, label_files):
    # Create an entry in data_dict for the image file
    data_dict[img] = {}

    # Loop through label files to extract point coordinates and update data_dict
    label_file_path = os.path.join(label_folder, label)

    # Read the coordinates from the label file
    with open(label_file_path, 'r') as label_file:
        coordinates = [list(map(float, line.strip().split())) for line in label_file]

    # Update the "Points" key in data_dict with the extracted coordinates
    data_dict[img]["Points"] = coordinates

# Specify the output JSON file path
output_json_file = 'output_data.json'

# Write the dictionary to the JSON file
with open(output_json_file, 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)
