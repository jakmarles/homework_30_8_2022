# Read the file
# Parse the JSON to a data structure
# Modify the data structure instead of creating a new one
# Serialise the data structure back to JSON
# Write it to the file

import json


def save(json_lst, DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump(json_lst, f)


def load(DATA_FILE):
    with open(DATA_FILE) as f:
        return json.load(f)
