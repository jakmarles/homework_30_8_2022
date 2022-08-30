import json

class Contact: # this class is meant for the contact itself
    name = ""
    tell = 0

    def __init__(self, name="", tell=0) -> None:
        self.name = name
        self.tell = tell

    def __str__(self):
        return json.dumps({"name": self.name, "tell": self.tell}) # add a new contact to contacts list
