import json

data = {
    'name': 'Pesho',
    'age': 19,
    'grades': [
        {'subject': 'Math', 'mark': 5.0},
        {'subject': 'Literature', 'mark': 4.5},
    ]
}

json_data = json.dumps(data)
print(repr(json.dumps(data)))
print(repr(json.loads(json_data)))
