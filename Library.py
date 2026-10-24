import time
import os
from my-subfolder import services



while True:
    services.print_centered("Library Management System")
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
        services.add_book()

    elif choice.lower() == 'view' or choice == '2':
        services.view_books()

    elif choice.lower() == 'search' or choice == '3':
        services.search_books()

    elif choice.lower() == 'delete' or choice == '4':
        services.delete_books()

    elif choice.lower() == 'add_member' or choice == '5':
        services.add_member()

    elif choice.lower() == 'view_members' or choice == '6':
        services.view_members()

    elif choice.lower() == 'search_members' or choice == '7':
        services.search_members()

    elif choice.lower() == 'delete_members' or choice == '8':
        services.delete_members()

    elif choice.lower() == 'exit' or choice == '9':
        break
    else:
        print("Invalid choice! Please try again.")
    
    services.freeze()