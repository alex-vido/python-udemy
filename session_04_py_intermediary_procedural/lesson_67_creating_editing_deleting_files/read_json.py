import json
import os

with open('abc.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)  # Convert to a dict

    for k, v in d1_json.items():
        for k1, v1 in v.items():
            print(k1, v1)

os.remove('abc.json')  # Remove the file
