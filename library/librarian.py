

def add_book(library:dict, title:str, author:str, isbn:str):
    new_book={'title':title,"author":author,"isbn":isbn,"available":True}
    number=len(library)

    for i in library:     
        if library[i]["isbn"]==isbn:
            return print("it is already exists!")
            
    else:
        library.update({number:new_book})
        number=number+1 
        print(f"add secsusfuly {number}")
        

        

def remove_book(library:dict,isbn:str):
    for i in library:
        if library[i]["isbn"]==isbn:
             return library.pop(i)
    else:
        print("not found !")

def check_out_book(library:dict, isbn:str):
     for i in library:
        if library[i]["isbn"]==isbn:
          check=library[i]["available"]="not available"
          return check
     else:
         print("not found !")

def return_book(library:dict, isbn:str):
    for i in library:
       if library[i]["isbn"]==isbn:
         check=library[i]["available"]="available"
         return check
    else:
        print("not found !")

def display_books(library):
    
        for i in library:
            print(f"{library[i]['title']} by {library[i]['author']} (ISBN : {library[i]['isbn']}) - {library[i]['available']} ")