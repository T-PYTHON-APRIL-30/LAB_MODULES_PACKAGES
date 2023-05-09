

def add_book(library:dict, title:str, author:str, isbn:str):
    '''takes a dictionary (library), a title (string), an author (string), and an ISBN (string) as input,
    and adds a new book to the library as a dictionary with the keys 'title', 'author', 'isbn', and 'available'.
    The 'available' key should have a boolean value, initially set to True. If the ISBN already exists in the library,
      print an appropriate message.'''
    counter = 1
    library[counter] = {'Title':f'{title}','Author':f'{author}','ISBN':f'{isbn}','Available':True}
    counter +=1
    print('The book added successfully..')

def remove_book(library, isbn):
    '''takes a dictionary (library) and an ISBN (string) as input, and removes the book with the given ISBN
      from the library. If the ISBN does not exist in the library, print an appropriate message.'''
    counter = 1
    for key in library:
        if library[counter]['ISBN'] == isbn:
            del library[counter]
            print('The book is deleted successfully..')
        else:
            print('The ISBN dosn\'nt exist!')

        counter +=1


def check_out_book(library, isbn):
    '''takes a dictionary (library) and an ISBN (string) as input, and sets the 'available' key of the book with
      the given ISBN to False. If the ISBN does not exist in the library or the book is not available,
        print an appropriate message.'''
    counter = 1
    for key in library:
        if library[counter]['ISBN'] != isbn:
            print('The book is not available!')
            library[counter]['Available'] = False

        else:
            print(f'The book is available..\n {library[counter]}')

        

def return_book(library, isbn):
    '''takes a dictionary (library) and an ISBN (string) as input, and sets the 'available' key of the book with 
    the given ISBN to True. If the ISBN does not exist in the library, print an appropriate message.'''
    counter = 1
    for key in library:
        if library[counter]['ISBN'] == isbn:
            library[counter]['Available'] = True
            print('The book is available..')

        else:
            print(f'The ISBN {isbn} is does\'nt exist in the library!')
    

def display_books(library):
    
    for b_id, b_info in library.items():
      print("\nBook information:", b_id)
    
      for key in b_info:
          print(key + ':', b_info[key])

    print()
