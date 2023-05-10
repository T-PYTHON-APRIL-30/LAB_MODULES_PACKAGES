

'''
takes a dictionary (library), a title (string), an author (string), and an ISBN (string) as input,
and adds a new book to the library as a dictionary with the keys 'title', 'author', 'isbn', and 'available'.
The 'available' key should have a boolean value, initially set to True.
If the ISBN already exists in the library, print an appropriate message.'''
def add_book(library:dict, title:str, author:str, isbn:str):
    
    for key in library:
        if isbn in library[key]["isbn"]:
            print(f"The {title} book is already exists in the library")
            return 
    numbers_books=len(library)
    numbers_books+=1
    library[numbers_books]={"title" : title,"author":author,"isbn":isbn,"available":True}
    
    print(f"The book '{title}' has been added successfully")





'''
takes a dictionary (library) and an ISBN (string) as input, and removes the book with the given ISBN from the library.
 If the ISBN does not exist in the library, print an appropriate message.'''
def remove_book(library:dict, isbn:str):
    flag=True
    for key in library:
        if isbn == library[key]["isbn"]:
            flag=False
    if flag:    
        print("The book does not exist in the library")
    else:
        for key1 in library:
            if isbn == library[key1]["isbn"]:
                 del library[key1]
                 break


    

'''takes a dictionary (library) and an ISBN (string) as input, and sets the 'available' key of the book with the given ISBN to False.
 If the ISBN does not exist in the library or the book is not available, print an appropriate message.'''
def check_out_book(library, isbn):
    flag=True
    for key2 in library:
        if isbn == library[key2]["isbn"]:
            if library[key2]["available"] == False:
                print("The book isn't available")
                return
            else: 
                library[key2]["available"] = False
                flag=False
                break
    if flag:
        print("The book does not exist in the library")
       



''' 
takes a dictionary (library) and an ISBN (string) as input, and sets the 'available' key of the book with the given ISBN to True.
If the ISBN does not exist in the library, print an appropriate message.'''
def return_book(library:dict, isbn:str):
    flag=True
    for key3 in library:
        if isbn == library[key3]["isbn"]:
            library[key3]["available"]= True
            flag=False
            break
    if flag:
        print("The book does not exist in the library")




'''takes a dictionary (library) as input and prints all the books in the library in a formatted way.'''
def display_books(library):
    for keys in library:
        for key4 in library[keys]:
            if key4 == "title":
                print(library[keys][key4],end=" by ")
            elif key4 == "author":
                print(library[keys][key4],end=" ")
            elif key4 == "isbn":
                print(f"(ISBN: {library[keys][key4]})",end=" ")
            elif key4 == "available":
                if library[keys][key4] == True:
                    print("- Available")
                else:
                    print("- Checked out")
    print("\n")






'''
Write a script named main.py in your working directory (outside the library folder) that imports and uses the librarian module from the library package to manage a simple library system.

5- use the function from librarian to add books, remove book, checout a book, and display books .
'''


'''A sample output should look like this when you run main.py

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

