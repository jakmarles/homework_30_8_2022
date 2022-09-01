import json
from Contact import Contact

class Contactlist: # this is the whole contactlist and functions to perfome
    contacts = []


    def __init__(self,contacts=[]) -> None:
        self.contacts=contacts


    def __str__(self) -> str:
        res=''
        for contact in self.contacts:
            res+=contact.__str__()
        return res

    def add_contact(self, name, tell): # function that adds a contact to contact valubale 
        self.contacts.append(Contact(name, tell))
    
    

    def send_to_json(self,data):
        res=[]
        for contact in self.contacts:
            res.append( json.loads(contact.__str__()))
        with open(data,'r+')as f:
            tmp=json.load(f)
            for i in res:
                tmp.append(i)
        with open(data,'w')as f:
            json.dump(tmp,f,indent=4)
        self.contacts.clear()   


    def remove_contact(self,name,data):
        with open(data,'r')as f:
            file=json.load(f)
            counter=0
            for i in (file):
                if i['name']==name:
                    del file[counter]
                counter+=1
        with open(data,'w')as f:
            json.dump(file,f,indent=4)

    def search_contact(self,name,data):
        with open(data,'r')as f:
            file=json.load(f)
            for i in file:
                if i['name']==name:
                    print(i)


def print_all():
    with open('my_contacts.json', 'r') as file:
        parsed = json.load(file)
        print(json.dumps(parsed))

    
