from helper import *
from Contactlist import *
from Contact import *


contacts = []
DATA_FILE = 'my_contacts.json'

# menu


def mainmenu():
    DATA_FILE = 'my_contacts.json'
    contactbook = Contactlist()
    user_selection = ''
    file_exist_check(DATA_FILE)
    while user_selection != 'x':
        user_selection = menu()
        if user_selection == 'a':
            contactbook.add_contact(input('enter name: '), input(
                'enter phone number: '))
        if user_selection == 'r':
            contactbook.remove_contact(
                input('what name to remove? '), DATA_FILE)
        if user_selection == 's':
            contactbook.search_contact(
                input('what name to search? '), DATA_FILE)
        if user_selection == 'p': print_all()

        contactbook.send_to_json(DATA_FILE)



# display menu, get user selection
def menu():
    print("a - add a contact")
    print("r - delete a contact")
    print("s - search a contact")
    print("p - print a contact")
    print("x - exit")
    user_selection = input("your selection is: ")
    return (user_selection)

