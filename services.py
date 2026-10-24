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