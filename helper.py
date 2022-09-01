
import json
from genericpath import exists

def save(json_lst, DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump(json_lst, f)


def load(DATA_FILE):
    with open(DATA_FILE) as f:
        return json.load(f)
        
def chkJson(data):
    if exists(data):
        pass
    else:
        with open(data,'w')as f:
            x=[]
            json.dump(x,f)