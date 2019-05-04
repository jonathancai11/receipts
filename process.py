import json

with open('out.json') as json_file:  
    data = json.load(json_file)
    print(data)
    