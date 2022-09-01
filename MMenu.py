from helper import *
from Contactlist import *
from Contact import *


contacts = []
DATA_FILE = 'my_contacts.json'

# menu


def mainmenu():
    DATA_FILE = 'my_contacts.json'
    phonebook = Contactlist()
    selection = 1
    chkJson(DATA_FILE)
    while selection != 'x':
        menu()
        selection = input('Your selection: ')
        if selection == 'a':
            phonebook.add_contact(input('enter contact name: '), input(
                'enter contact phone number: '))
        if selection == 'r':
            phonebook.remove_contact(
                input('what name would you like to remove? '), DATA_FILE)
        if selection == 's':
            phonebook.search_contact(
                input('what name would you like to search? '), DATA_FILE)
        if selection == 'p':
            print(phonebook)
        phonebook.send_to_json(DATA_FILE)


# display menu, get user selection
def menu():
    print("a - add a contact")
    print("r - delete a contact")
    print("s - search a contact")
    print("p - print a contact")
    print("x - exit")
