

def add_book(library:dict, title:str, author:str, isbn:str):
    '''takes a dictionary (library), a title (string), an author (string), and an ISBN (string) as input,
    and adds a new book to the library as a dictionary with the keys 'title', 'author', 'isbn', and 'available'.
    The 'available' key should have a boolean value, initially set to True. If the ISBN already exists in the library,
      print an appropriate message.'''
    
    if isbn not in library:
        library[isbn] = {'Title':f'{title}','Author':f'{author}','ISBN':f'{isbn}','Available':True}
        
        print('The book added successfully..')
    else:
        print('The book is already exist..')

    

def remove_book(library, isbn):
    '''takes a dictionary (library) and an ISBN (string) as input, and removes the book with the given ISBN
      from the library. If the ISBN does not exist in the library, print an appropriate message.'''
    
    if isbn in library:
        del library [isbn]
        print('The book is removed..')

    else:
        print('This book is not in the library')


def check_out_book(library, isbn):
    '''takes a dictionary (library) and an ISBN (string) as input, and sets the 'available' key of the book with
      the given ISBN to False. If the ISBN does not exist in the library or the book is not available,
        print an appropriate message.'''
    book = library.get(isbn)
    if book and book['Available']:
        book['Available'] = False
        print('Book checked out success..')
    else:
        print('The book is not available..')

        

def return_book(library, isbn):
    '''takes a dictionary (library) and an ISBN (string) as input, and sets the 'available' key of the book with 
    the given ISBN to True. If the ISBN does not exist in the library, print an appropriate message.'''
    if isbn not in library:
        print('The book is not in the library..')
    
    else:
        library[isbn]['Available'] = True
        print('The book is returned..')
    

def display_books(library:dict):

    for book in library.values():

        available_phrase = "Available"

        if not book["Available"]:
            available_phrase = "Not available"
        
        print(f"{book['Title']} By {book['Author']} (ISBN: {book['ISBN']})")
        print()
    
    
