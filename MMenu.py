from helper import load , save 
from Contactlist import Contactlist


contacts = []
DATA_FILE = 'my_contacts.json'

# menu
def mainmenu():
    load(DATA_FILE)
    contactlist = Contactlist()
    user_selection = ''
    while user_selection != 'x':
        user_selection = menu()
        if user_selection == 'a':
            contactlist.add_contact(input("name? "), int(input("tell? "))) # add new contact
        if user_selection == 'r':
            contactlist.remove_contact(
            contactlist.search_contact(input("name? ")))   # ask for a name of a contact you want to remove
        if user_selection == 's':
            print(contactlist.search_contact(input("name? "))) # search for contact by name
        if user_selection == 'p': # print all the current contacts
            print(contactlist)
        # x - do nothing

    save(contactlist.get_contacts_as_json_ar(),
         DATA_FILE)  # save data to file


# display menu, get user selection
def menu():
    print("a - add a contact")
    print("r - delete a contact")
    print("s - search a contact")
    print("p - print a contact")
    print("x - exit")
    user_selection = input("your selection:")
    return (user_selection)


