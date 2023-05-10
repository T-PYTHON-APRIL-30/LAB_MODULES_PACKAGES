#add_book(library, title, author, isbn) - takes a dictionary (library), a title (string), an author (string), and an ISBN (string) as
# input, and adds a new book to the library as a dictionary with the keys
# 'title', 'author', 'isbn', and 'available'. The 'available' key should have a boolean value, initially set to True. 
#If the ISBN already exists in the library, print an appropriate message
 #remove_book(library, isbn) - 
# takes a dictionary (library) and an ISBN (string) as input, and removes the book with the given ISBN from the library. 
# If the ISBN does not exist in the library, print an appropriate message.
#check_out_book(library, isbn) - 
# takes a dictionary (library) and an ISBN (string) as input,
#  and sets the 'available' key of the book with the given ISBN to False. 
# If the ISBN does not exist in the library or the book is not available, print an appropriate message
#return_book(library, isbn) - takes a dictionary (library) and an ISBN (string) as input, 
# and sets the 'available' key of the book with the given ISBN to True. 
# If the ISBN does not exist in the library, print an appropriate message.
#display_books(library) - takes a dictionary (library)
#  as input and prints all the books in the library in a formatted way.


def add_book(library:dict, title:str, author:str, isbn:str):
    if isbn not in library:
        book = {"title" : title, "author" : author, "isbn" : isbn, "available" : True}
        library[isbn] = book
    else:
        print("The book is already in the Library")

def remove_book(library:dict, isbn:str):
    if isbn in library:
        del library[isbn]
    else:
        print(f"The book with this ISBN: {isbn} is not found")


def check_out_book(library:dict, isbn:str):
    book = library.get(isbn)
    if book and book["available"]:
        book["available"] = False
        print("Book check out success")
    else:
        print("The book is not available")


def return_book(library:dict, isbn:str):
    
    if isbn not in library:
        print("Book not in Library")
    else:
        library[isbn]["available"] = True


def display_book(library:dict):
    
    for book in library.values():
        availabe_phrase = "Available"
        if not book["available"]:
            availabe_phrase = "Not Available"
            
        phrase = f"{book['title']} by {book['author']} (ISBN:{book['isbn']}) - {availabe_phrase} "
        print(phrase)


