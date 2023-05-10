# imports and uses the librarian module from the library package to manage a simple library system

from library import librarian

print('Welcome to our library...')
library = {}
title = ''
author = ''
ISBN = ''

print()




while True:
    print("Please select from the menu: \n 1- enter 1 to add a book \n 2- enter 2 to remove a book."
                    + "\n 3- enter 3 to check out a book. \n 4- enter 4 to return a book. \n 5- enter 5 to display all the books\n" +
                    "6- enter 6 for Exit")
    print()
    choise = input('Your choise: ')
    print()
    
    if choise == '1':
        print('To add a book please enter the following info: \n')
        title = input('Please enter the book\'s title: ')
        author = input('Please enter the book\'s author: ')
        ISBN = input('Please enter the ISBN for the book: ')
        print()
        librarian.add_book(library,title,author,ISBN)
        print()
        

    elif choise == '2':
        print('To remove a book please enter the following info: \n')
        ISBN = input('Please enter the book\'s ISBN: ')
        print()
        librarian.remove_book(library,ISBN)
        print()
        
    elif choise == '3':
        print('To check out a book please enter the following info: \n')
        ISBN = input('Please enter the book\'s ISBN: ')
        print()
        librarian.check_out_book(library,ISBN)
        print()


    elif choise == '4':
        print('To return a book please enter the following info: \n')
        ISBN = input('Please enter the book\'s ISBN: ')
        print()
        librarian.return_book(library,ISBN)
        print()

    elif choise == '5':
        print('Displays all the books in the library...')
        print()
        librarian.display_books(library)

    elif choise == '6':
        print('Thank you for using our library...')
        break

    else:
        print('wrong entry please enter a valid choise!!')
        print()
    