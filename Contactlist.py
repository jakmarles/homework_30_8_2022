import json
from Contact import Contact

class Contactlist:
    contacts = []

    def __init__(self):
        pass

    def add_contact(self, name="", tell=0):
        self.contacts.append(Contact(name, tell))

    def remove_contact(self, victim):
        self.contacts.remove(victim)

    def search_contact(self, contact_name):
        for contact in self.contacts:
            if type(contact) is Contact:
                if contact.name == contact_name:
                    return contact
        return None

    def get_contacts_as_json_ar(self):
        res = []
        for contact in self.contacts:
            res.append(json.loads(contact.__str__()))
        return res

    def __str__(self) -> str:
        res = ""
        for contact in self.contacts:
            res += contact.__str__()
        return res