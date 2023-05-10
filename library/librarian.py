"""
`add_book(library, title, author, isbn)` - takes a dictionary (library), a title (string), an author (string), 
and an ISBN (string) as input, and adds a new book to the library as a dictionary with the keys 'title', 'author', 'isbn', and 'available'. 
The 'available' key should have a boolean value, initially set to True. If the ISBN already exists in the library, print an appropriate message.
`remove_book(library, isbn)` - takes a dictionary (library) and an ISBN (string) as input, and removes 
the book with the given ISBN from the library. If the ISBN does not exist in the library, print an appropriate message.

check_out_book(library, isbn)` - takes a dictionary (library) and an ISBN (string) as input, and sets the 'available' key of
 the book with the given ISBN to False. If the ISBN does not exist in the library or the book is not available,
   print an appropriate message.
   - `return_book(library, isbn)` - takes a dictionary (library) and an ISBN (string) as input, and sets the 'available' key of the 
   book with the given ISBN to True. If the ISBN does not exist in the library, print an appropriate message.
   - `display_books(library)` - takes a dictionary (library) as input and prints all the books in the library in a formatted way.
"""

def add_book(library:dict, title:str, author:str, isbn:str):
    if isbn in library:
        print(f"Book with ISBN {isbn} already exists in the library.")
    else:
        library[isbn] = {'title': title, 'author': author, 'isbn': isbn, 'available': True}


def remove_book(library, isbn):
    if  isbn not in library:
        print(f"Book with ISBN: {isbn} does not exist in the library.")
    else:
        del library[isbn]
        
def check_out_book(library, isbn):
    if isbn not in library:
        print(f"Book with ISBN: {isbn} does not exist in the library.")
    elif not library[isbn]['available']:    
        print("Book is not available for checkout.")
    else:
        library[isbn]['available'] = False

def return_book(library, isbn):
    if isbn not in library:
        print(f"Book with ISBN: {isbn} does not exist in the library.")
    else:
        library[isbn]['available']=True
"""
def display_books(library):
    for book in library.values():
        print(f"Title: {book['title']}\nAuthor: {book['author']}\nISBN: {book['isbn']}\nAvailable: {book['available']}\n")   
"""
def display_books(library):
    for book in library.values():
        availability = "Available" if book['available'] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {availability}")
