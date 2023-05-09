
def add_book(library, title, author, isbn):
    if isbn not in library:
        library[isbn]={'title':title, 'author': author, 'isbn': isbn,'available': True}
    else:
        print(f"Book with ISBN {isbn} already exists.")

def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
    else:
        print(f"Book with ISBN {isbn} not found.")

def check_out_book(library, isbn):
    if isbn in library:
        if library[isbn]['available']:
            library[isbn]['available'] = False
        else:
            print(f"Book with ISBN {isbn} not found.")

def return_book(library, isbn):
    if isbn in library:
        library[isbn]['availavle']= True
    else:
        print(f"Book with ISBN {isbn} not found.")

def display_books(library):
    for book in library.values():
        availability= "Available" if book ['available'] else 'checked Out'
        print(f"{book['title']}by{book['author']}(ISBN: {book['isbn']}) - {availability}")
