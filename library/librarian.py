def add_book(library: dict, title: str, author: str, isbn: str):
    isbn_value = library.values()

    if isbn not in isbn_value:

        library[isbn] = {"title": title, "author": author,
                         "isbn": isbn, "avalable": True}

        return library
    else:
        print(f"Book with this ISBN: {isbn} aleady exsist")


def remove_book(library: dict, isbn: str):

    if isbn in library:
        del library[isbn]
        print(f"Book with ISBN {isbn} has been deleted from the library.")
    else:
        print(f"Book with ISBN nomber: {isbn} dosn't exsist")


def check_out_book(library: dict, isbn: str):
    if isbn in library:
        library.update(avalable="False")
        # print(library)
    else:
        print("book is not available")


def return_book(library: dict, isbn: str):
    if isbn in library:
        library.update(avalable="True")


def display_books(library: dict):
    if len(library) == 0:
        print("The library is empty.")
    else:

        for i, details in library.items():
            print(
                f'{details["title"]} by {details["author"]} ({details["isbn"]}) - {details["avalable"]}')
