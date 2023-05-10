from dateOP import current_date
from library import librarian


today = current_date()
print(f"today date is : {today}")


library = {}

#add book
librarian.add_book(library, "Think Slow and Fast", "Sam Altman", "4567")
librarian.add_book(library, "Harry Potter", "Chrisitina", "32423")

#check out book
librarian.check_out_book(library, "4567")

#return book
librarian.return_book(library, "4567")


librarian.display_book(library)