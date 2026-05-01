class Movie:
    def __init__(self, title, director, year, genre):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
    
    def display(self):
            print(f"{self.title} ({self.year}) — {self.genre}, Directed by {self.director}")

movies = [] 

def enter_movie(): 
    title = input("Please enter the Movie Title: ") 
    director = input("Please enter the Movie Director: ") 
    year = input("Please enter the Movie Year: ") 
    genre = input("Please enter the Movie Genre: ") 
    movie = Movie(title, director, year, genre) 

    movies.append(movie) 
    
def view_movies(): 
    for movie in movies: 
        movie.display() 
        
def show_menu(): 
    print("1. Enter a Movie") 
    print("2. View Listed Movies") 
    
while True: 
    show_menu() 
    choice = input("Please choose between 1 and 2: ") 
    if choice == "1": 
        enter_movie() 
    elif choice == "2": 
        view_movies() 
    else:
     exit()