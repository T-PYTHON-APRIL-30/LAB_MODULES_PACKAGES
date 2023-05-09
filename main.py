import dateOP
from library import librarian 
dateOP.display()

#--------------------------
main_dict={}
librarian.add_book(main_dict,"ai","khalid","23456")
librarian.add_book(main_dict,"software engneer","nawaf","23556")
librarian.add_book(main_dict,"software engneer","nawaf","23556")
librarian.display_books(main_dict)
print("-------")
librarian.remove_book(main_dict,"23556")
librarian.check_out_book(main_dict,'23456')
librarian.display_books(main_dict)
print("-------")
librarian.return_book(main_dict,"23456")
librarian.display_books(main_dict)