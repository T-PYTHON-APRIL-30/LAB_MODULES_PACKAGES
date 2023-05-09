library_data = [{
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger",
    "isbn": "9780316769174",
    "available": True
},{
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "isbn": "9780446310789",
    "available": True
},{
    "title": "1984",
    "author": "George Orwell",
    "isbn": "9780451524935",
    "available": True
}]

def add_book(library: dict, title: str, author: str, isbn: str):
    library = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True
    }
    for book in library_data:
        if book["isbn"] == isbn:
            print("This book is already exists...")
        else:
            library_data.append(library)


def remove_book(library: dict, isbn: str):
    for book in library_data:
        if isbn not in book["isbn"]:
            print("This book is not exists!!")
        else:
            library_data.remove(book)


def check_out_book(library: dict, isbn: str):
    for book in library_data:
        if book["isbn"] == isbn:
            book["available"] = False
        elif book["isbn"] != isbn or book["available"] == False:
            print("Sorry not found...")


def return_book(library: dict, isbn: str):
    for book in library_data:
        if book["isbn"] == isbn:
            book["available"] = True
        elif book["isbn"] != isbn:
            print("Sorry not found...")


def display_books(library: dict):
    for book in library_data:
        if book["available"] == True:
            print(book["title"], "by", book["author"], "(ISBN: ", book["isbn"], ") - Available")
        else:
            print(book["title"], "by", book["author"], "(ISBN: ", book["isbn"], ") - Checked Out")