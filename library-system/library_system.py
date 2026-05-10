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

