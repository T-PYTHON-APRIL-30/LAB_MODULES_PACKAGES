# this file should include functions for managing books and patrons in a library system without using classes.

# adds a new book
def add_book(library, title, author, isbn):
    if isbn in library:
        print(isbn, "book is exist in the library")
    else:
        library[isbn] = {'title': title, 'author': author, 'isbn': isbn, 'available': True}

# remove an exist book 
def remove_book(library, isbn):
    if isbn not in library:
        print(isbn, "does not exist in the library.")
    else:
        del library[isbn]

# checkout a book 
def check_out_book(library, isbn):
    if isbn not in library:
        print(isbn, " not exist")
    elif not library[isbn]['available']:
        print(isbn, "not available.")
    else:
        library[isbn]['available'] = False

# return a book 
def return_book(library, isbn):
    if isbn not in library:
        print(isbn, "not exist")
    else:
        library[isbn]['available'] = True

# display all books
def display_books(library):
    for book in library.values():
        print(book['title'], "by", book['author'], f"(ISBN: {book['isbn']})", " - ", book['available'])

'''
The Catcher in the Rye by J.D. Salinger (ISBN: 9780316769174) - Available
To Kill a Mockingbird by Harper Lee (ISBN: 9780446310789) - Available
1984 by George Orwell (ISBN: 9780451524935) - Available
'''