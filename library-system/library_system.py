import json

class Book:
    def __init__(self, number, title, author, genre, year, availability=True):
        self.id = number
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.is_available = availability

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False
        
    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return True
        else:
            return False

    def to_dict(self):
        return{"id": self.id,
               "title": self.title,
               "author": self.author,
               "genre": self.genre,
               "year": self.year,
               "availability": self.is_available}

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["title"], data["author"], data["genre"], data["year"], data["availability"])

class Library:
    def __init__(self, filepath):
        self.books = []
        self.filepath = filepath
        self.load()

    def load(self):
        try:
            with open (self.filepath, "r") as f:
                data = json.load(f)
                self.books = [Book.from_dict(item) for item in data]

        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []  

    def save(self):
        data = [book.to_dict() for book in self.books]
        with open (self.filepath, "w") as f:
            json.dump(data, f)

    def _next_id(self):
        if not self.books:
            return 1
        
        else:
            result = max(self.books, key=lambda book: book.id)
            next_id = result.id + 1
            return next_id
        
    def add_book(self, title, author, genre, year):
        next_id = self._next_id()
        book = Book(next_id, title, author, genre, year)
        self.books.append(book)
        self.save()

    def search_by_title(self, title):
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