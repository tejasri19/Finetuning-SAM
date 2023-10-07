import os
import json

# Directory containing your text files
folder_path = 'dataset/data/new_test'

# Initialize an empty list to store data
data_list = []

# Loop through all files in the folder
for filename in sorted(os.listdir(folder_path)):
    # Check if the file has a '.jpg' extension
    if filename.endswith('.jpg'):
        data_list.append(str(filename))

# Print the filenames to check if they are being collected correctly
print("Collected Filenames:", data_list)

# Create a dictionary with the "train" key containing the list of filenames
data_dict = {'test': data_list}

# Convert the dictionary to JSON format
json_data = json.dumps(data_dict, indent=4)

# Save the JSON data to a file
with open('Train_data.json', 'w') as json_file:
    json_file.write(json_data)
