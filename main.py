import dateOP
from library import librarian

print("The current date: ")
dateOP.current_date()

simple_library={}
'''
The Catcher in the Rye by J.D. Salinger (ISBN: 9780316769174) - Available
To Kill a Mockingbird by Harper Lee (ISBN: 9780446310789) - Available
1984 by George Orwell (ISBN: 9780451524935) - Available

The Catcher in the Rye by J.D. Salinger (ISBN: 9780316769174) - Checked Out
To Kill a Mockingbird by Harper Lee (ISBN: 9780446310789) - Available
1984 by George Orwell (ISBN: 9780451524935) - Available

The Catcher in the Rye by J.D. Salinger (ISBN: 9780316769174) - Available
To Kill a Mockingbird by Harper Lee (ISBN: 9780446310789) - Available
1984 by George Orwell (ISBN: 9780451524935) - Available
'''
librarian.add_book(simple_library,"The Catcher in the Rye","J.D. Salinger","9780316769174")
librarian.add_book(simple_library,"To Kill a Mockingbird","Harper Lee","9780446310789")
librarian.add_book(simple_library,"1984","George Orwell","9780451524935")

librarian.display_books(simple_library)

librarian.check_out_book(simple_library,"9780316769174")

librarian.display_books(simple_library)

librarian.return_book(simple_library,"9780316769174")

librarian.display_books(simple_library)

librarian.remove_book(simple_library,"9780451524935")

librarian.display_books(simple_library)