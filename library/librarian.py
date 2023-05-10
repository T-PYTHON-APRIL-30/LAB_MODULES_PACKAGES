# 3. Create a new file named `librarian.py` inside the `library` folder. In this file,
#  define the following functions:

'''`add_book(library, title, author, isbn)` - takes a dictionary (library), a title (string),
 an author (string), and an ISBN (string) as input, and adds a new book to the library 
 as a dictionary with the keys 'title', 'author', 'isbn', and 'available'.
 The 'available' key should have a boolean value, initially set to True.
 If the ISBN already exists in the library, print an appropriate message.
'''
# library = {}
# book_keys = ['title','author','isbn','available'] # Initialize keys

# def add_book(library, title:str, author:str, isbn:str):
#     for keys in book_keys:
#         library[keys] = "black hat python"
#     library = {}
#     title = "black hat python"
#     library["title"] = title
#     author = "Justin Seitz"
#     library["Author"] = author
#     isbn = "9781457189807"
#     library["isbn"] = isbn
#     library["availability"]=True
#     book_list.append(library)
# book_list = []
library={}
def add_book(library, title, author, isbn):
    if isbn not in library:
        print("the book is already exist in the library")
    else:
        library[isbn]={'title':title,'author':author,'isbn':isbn,'available':True}

    

        

'''- `remove_book(library, isbn)` - takes a dictionary (library) and an ISBN (string) as input,
 and removes the book with the given ISBN from the library.
 If the ISBN does not exist in the library, print an appropriate message.'''

def remove_book(library, isbn:str):
    if isbn in library:
        

    


 




'''- `check_out_book(library, isbn)` - takes a dictionary (library) and an ISBN (string) as input,
 and sets the 'available' key of the book with the given ISBN to False. 
If the ISBN does not exist in the library or the book is not available, print an appropriate message.'''

'''- `return_book(library, isbn)` - takes a dictionary (library) and an ISBN (string) as input, 
and sets the 'available' key of the book with the given ISBN to True.
 If the ISBN does not exist in the library, print an appropriate message.'''

'''- `display_books(library)` - takes a dictionary (library) as input and prints all the books in
 the library in a formatted way.'''

# 4. Write a script named `main.py` in your working directory (outside the `library` folder) that imports and uses the `librarian` module from the `library` package to manage a simple library system.

# 5- use the function from librarian to add books, remove book, checout a book, and display books .

# ### A sample output should look like this when you run main.py
# ```
# The Catcher in the Rye by J.D. Salinger (ISBN: 9780316769174) - Available
# To Kill a Mockingbird by Harper Lee (ISBN: 9780446310789) - Available
# 1984 by George Orwell (ISBN: 9780451524935) - Available

# The Catcher in the Rye by J.D. Salinger (ISBN: 9780316769174) - Checked Out
# To Kill a Mockingbird by Harper Lee (ISBN: 9780446310789) - Available
# 1984 by George Orwell (ISBN: 9780451524935) - Available

# The Catcher in the Rye by J.D. Salinger (ISBN: 9780316769174) - Available
# To Kill a Mockingbird by Harper Lee (ISBN: 9780446310789) - Available
# 1984 by George Orwell (ISBN: 9780451524935) - Available

# ```
