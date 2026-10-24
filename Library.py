import time
import os
import services

# menu options

def add_book():
    pass

def view_books():
    pass

def search_books():
    pass

def delete_books():
    pass

def add_member():
    pass

def view_members():
    pass

def search_members():
    pass

def delete_members():
    pass

# utility functions

def get_width():
    return os.get_terminal_size().columns

def print_centered(text):
    width = get_width()
    print(text.center(width,"*"))

def freeze():
    time.sleep(2)
    
while True:
    print_centered("Library Management System")
    print("\n\t1. Add Book [ADD]")
    print("\t2. View Books [VIEW]")
    print("\t3. Search Books [SEARCH]")
    print("\t4. Delete Books [DELETE]")
    print("\t5. Add Member [ADD_MEMBER]")
    print("\t6. View Members [VIEW_MEMBERS]")
    print("\t7. Search Members [SEARCH_MEMBERS]")
    print("\t8. Delete Members [DELETE_MEMBERS]")
    print("\t9. Exit [EXIT]")

    choice = input("Enter your choice: ")

    if choice.lower() == 'add' or choice == '1':
        add_book()

    elif choice.lower() == 'view' or choice == '2':
        view_books()

    elif choice.lower() == 'search' or choice == '3':
        search_books()

    elif choice.lower() == 'delete' or choice == '4':
        delete_books()

    elif choice.lower() == 'add_member' or choice == '5':
        add_member()

    elif choice.lower() == 'view_members' or choice == '6':
        view_members()

    elif choice.lower() == 'search_members' or choice == '7':
        search_members()

    elif choice.lower() == 'delete_members' or choice == '8':
        delete_members()

    elif choice.lower() == 'exit' or choice == '9':
        break
    else:
        print("Invalid choice! Please try again.")
    
    freeze()