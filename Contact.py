import json

class Contact:
    name = ""
    tell = 0

    def __init__(self, name="", tell=0) -> None:
        self.name = name
        self.tell = tell

    def __str__(self):
        return json.dumps({"name": self.name, "tell": self.tell})
