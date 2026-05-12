import json                                                                        

class Book:                                                                        
    def __init__(self, id, title, author, genre, year, availability=True):      
        self.id = id                                                            
        self.title = title                                                          
        self.author = author                                                        
        self.year = year                                                           
        self.genre = genre                                                          
        self.is_available = availability                                            

    def borrow(self):                                                               #The caller needs to know if a book's state actually changed before deciding to save it.               
        if self.is_available:                                                       
            self.is_available = False                                               
            return True                                                             
        else:                                                                       
            return False                                                            
        
    def return_book(self):                                                          #The caller needs to know if a book's state actually changed before deciding to save it.                                                       
        if not self.is_available:                                                   
            self.is_available = True                                                
            return True                                                             
        else:                                                                      
            return False                                                            

    def to_dict(self):                                                              #to_dict is inside Book because Book handles a book's attributes and is the one responsible for its own serialization.                                                             
        return{"id": self.id,                                                      
               "title": self.title,
               "author": self.author,
               "genre": self.genre,
               "year": self.year,
               "availability": self.is_available}

    @classmethod                                                                    #from_dict is inside Book because Book handles a book's attributes and is the one responsible for its own reconstruction
    def from_dict(cls, data):
        return cls(data["id"], data["title"], data["author"], data["genre"], data["year"], data["availability"])

class Library:                                                                     
    def __init__(self, filepath):                                                   
        self.books = []                                                             
        self.filepath = filepath                                                    
        self.load()                                                                 #Calling load in __init__ ensures that the library is always in a valid state and prevent corrupt additions or changes the moment it's created.                                                 

    def load(self):                                                                 
        try:                                                
            with open (self.filepath, "r") as f:                                    
                data = json.load(f)                                                 
                self.books = [Book.from_dict(item) for item in data]                

        except (FileNotFoundError, json.JSONDecodeError):                           #We use the two conditions: FileNotFound and json.JSONDecodeError with the same outcome of an empty list because both don't have data inside therefore nothing to work with.
            self.books = []                                                         

    def save(self):                                                                 
        data = [book.to_dict() for book in self.books]                              
        with open (self.filepath, "w") as f:                                        
            json.dump(data, f)                                                      

    def _next_id(self):                                                             
        if not self.books:                                                          
            return 1                                                                
        
        else:                                                                       
            result = max(self.books, key=lambda book: book.id)                      #Use max to ensure that even when user's delete books, the new ID of a book will never collide with existing ones.
            next_id = result.id + 1                                                 
            return next_id                                                          
        
    def add_book(self, title, author, genre, year):                                 
        next_id = self._next_id()                                                   
        book = Book(next_id, title, author, genre, year)                            
        self.books.append(book)                                                     
        self.save()                                                                 #Called immediately to not lose data in case of certain events such as a power loss.
        return book                                                                 

    def search_by_title(self, title):                                               #Returns a list instead of a single book for instances when a Book has the same title or author.
        result = [book for book in self.books if book.title == title]               
        return result                                                               
    
    def search_by_author(self, author):                                             
        result = [book for book in self.books if book.author == author]             
        return result                                                               

    def filter_by_genre(self, genre):                                               
        result = [book for book in self.books if book.genre == genre]               
        return result                                                               
    
    def filter_by_availability(self, is_available):                                 
        result = [book for book in self.books if book.is_available == is_available] 
        return result                                                               

    def sort_by_year(self):                                                         
        result = sorted(self.books, key=lambda book: book.year)                     
        return result                                                               

    def borrow_book(self, id):                                                     
        for book in self.books:                                                     
            if book.id == id:                                                       
                result = book.borrow()                                              
                if result:                                                          #Ensure the JSON file matches the self.books immediately after a successful transaction.
                    self.save()                                                     
                return result                                                       
        else:                                                                       
            return False                                                            
        
    def return_book(self, id):                                                      
        for book in self.books:                                                     
            if book.id == id:                                                       
                result = book.return_book()                                         
                if result:                                                          #Ensure the JSON file matches the self.books immediately after a successful transaction.
                    self.save()                                                     
                return result                                                       
        else:                                                                       
            return False                                                            