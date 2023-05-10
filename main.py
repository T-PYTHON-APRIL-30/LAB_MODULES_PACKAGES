import dateOP
from Library import librarian

#---------- Lab ----------
dateOP.presentDate()

#---------- Bonus ----------
#---- Mr.Aqeel solution ----

library = {}


librarian.add_book(library, "Think Slow and Fast", "Sam Altman", "4567")

librarian.check_out_book(library, "4567")

librarian.return_book(library, "4567")

librarian.display_books(library)