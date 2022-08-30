import json

def save(json_lst, DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump(json_lst, f)

def load(DATA_FILE):
    with open(DATA_FILE) as f:
        return json.load(f)
