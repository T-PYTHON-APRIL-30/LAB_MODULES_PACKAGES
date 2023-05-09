    
nTit = " "
nAu = ""
nIsb = ""
available = True


my_dic = {nTit:"", nAu:"", nIsb:"", available: True}

def add_book(library, title : str, author : str,isbn : str ):
        
    for elemnt in my_dic:
        if check_book(library,isbn):
            print("The book is already registered try with another isbn")
            
        else:
            my_dic.update(nTit = title, nAu = author, nIsb = elemnt)
            library = my_dic
            print("book added successfully")
    return library

def remove_book(library,isbn):
    for isbn in my_dic:
        if check_book(library,isbn):
            del my_dic[isbn]
        else:
            print("isbn not in library")

def check_book(library,isbn):
    library
    for element in my_dic:
        if isbn in my_dic: 
            library = my_dic
            return True
        else:
            print("Book not found")
            return False 

def return_book(library,isbn):
    for element in my_dic:
        if check_book(library,isbn) == False:
            my_dic.update([nIsb, element])
        else:
            print("does not exsist here")

def display(library):
    for element in  library:
        print(library[element])




