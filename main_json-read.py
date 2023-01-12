import json


with open('data/cats_json.json') as cat_file:
    data = json.load(cat_file)

print(data)

for key, value in data.items():
    if type(value) == list:
        print(f'{key}: {", ".join(value)}')
    else:
        print(f'{key}: {value}')