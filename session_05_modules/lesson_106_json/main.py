"""
JavaScript Object Notation - JSON
JSON is a changer format of data between systems and light apps and easy utilization.
Too much used for APIs
"""
from textwrap import indent
from data import dict_clients, json_clients
import json

data_json = json.dumps(dict_clients, indent=4)
# print(type(data_json), data_json)

dic = json.loads(json_clients)
# for key, value in dic.items():
#   print(key)
#   print(value)

with open('clients.json', 'w') as file:
    json.dump(dict_clients, file, indent=4)

with open('clients.json', 'r') as file:
    da = json.load(file)

for key, value in da.items():
    print(key)
    print(value)
