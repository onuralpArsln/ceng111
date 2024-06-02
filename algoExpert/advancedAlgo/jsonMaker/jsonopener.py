import json
# Specify the path to your JSON file
json_file_path = 'output.json'

# Read and parse the JSON file
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Print the parsed data
print(data)
print(data["age"])