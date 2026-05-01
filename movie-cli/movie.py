class Movie:
    def __init__(self, title, director, year, genre):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
    
    def display(self):
            print(f"{self.title} ({self.year}) — {self.genre}, Directed by {self.director}")

