import json
from Contact import Contact

class Contactlist: # this is the whole contactlist and functions to perfome
    contacts = []

    def __init__(self):
        pass

    def add_contact(self, name="", tell=0): # function that adds a contact to contact valubale 
        self.contacts.append(Contact(name, tell))

    def remove_contact(self, victim): # removes a contact and let you chose him by name
        self.contacts.remove(victim)

    def search_contact(self, contact_name): # search for a contact by using his name
        for contact in self.contacts:
            if type(contact) is Contact:
                if contact.name == contact_name:
                    return contact
        return None

    def get_contacts_as_json_ar(self): # makes the inputed string putable in json by format
        res = []
        for contact in self.contacts:
            res.append(json.loads(contact.__str__()))
        return res

    def __str__(self) -> str:
        res = ""
        for contact in self.contacts:
            res += contact.__str__()
        return res