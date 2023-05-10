from library import librarian

'''
- Write a script named main.py in your working directory (outside the library folder) that imports and uses the librarian module from the library package to manage a simple library system.
- use the function from librarian to add books, remove book, checout a book, and display books .
'''

# empty library dictionary
library = {}

# add books to the dictionary
librarian.add_book(library, 'The Catcher in the Rye', 'J.D. Salinger', '9780316769174')
librarian.add_book(library, 'To Kill a Mockingbird', 'Harper Lee', '9780446310789')
librarian.add_book(library, '1984', 'George Orwell', '9780451524935')

# display books
librarian.display_books(library)
print()

# checout a book
librarian.check_out_book(library, '9780316769174')
librarian.display_books(library)
print()

# return book
librarian.return_book(library, '9780316769174')
librarian.display_books(library)
print()

# remove book
librarian.remove_book(library, '9780446310789')
librarian.display_books(library)