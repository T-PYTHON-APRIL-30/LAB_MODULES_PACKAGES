#---------- Bonus ----------
#---- Mr.Aqeel solution ----

def add_book(library:dict, title:str, author:str, isbn:str):
    if isbn not in library:
        book = {"title": title, "author":author , "isbn":isbn,"available":True}
        library[isbn] = book
    else:
        print("The book is already in the library !!")

def remove_book(library:dict, isbn:str):
    if isbn in library:
        del library[isbn]
    else:
        print(f"the {isbn} is not found")


def check_out_book(library:dict, isbn:str):
    book = library.get(isbn)
    if book and book["available"]:
        book["available"] = False
        print("Book check out success")
    else:
        print("The book is not available")


def return_book(library:dict, isbn:str):
    
    if isbn not in library:
        print("Book not in the Library")
    else:
        library[isbn]["available"] = True


def display_books(library:dict):
    
    for book in library.values():
        available_phrase = "Available"
        if not book["available"]:
            available_phrase = "Not Available"
        phrase = f"{book['title']} by {book['author']} (ISBN:{book['isbn']}) - {available_phrase} "
        print(phrase)