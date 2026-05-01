class Movie:                                                    #Defines a BLUEPRINT called Movie.
    def __init__(self, title, director, year, genre):           #Initialized automatically the ATTRIBUTES. (The data attached to that specific object)
        self.title = title                                      #"self.title" permanently stores the value of "title" on the object
        self.director = director                                #"self.director" permanently stores the value of "director" on the object
        self.year = year                                        #"self.year" permanently stores the value of "year" on the object
        self.genre = genre                                      #"self.genre" permanently stores the value of "genre" on the object
    
    def display(self):                                          #Display the movie attributes, it needs self because it is how each object refers to their own specific data.
            print(f"{self.title} ({self.year}) — {self.genre}, Directed by {self.director}")

movies = []                                                     #List where all the movie objects will be placed

def enter_movie():                                              #Defines a function where the user can enter a movie
    title = input("Please enter the Movie Title: ")             #Ask for the movie information
    director = input("Please enter the Movie Director: ")       #Ask for the movie information
    year = input("Please enter the Movie Year: ")               #Ask for the movie information  
    genre = input("Please enter the Movie Genre: ")             #Ask for the movie information
   
    movie = Movie(title, director, year, genre)                 #This line creates a new Movie OBJECT using the collected inputs and assigns it to the variable movie. (A specific thing created from that blueprint)

    movies.append(movie)                                        #Adds the newly listed movies at the end of the movie list
    
def view_movies():                                              #Defines a function where the user can view the movies
    for movie in movies:                                        #Loops through every movie in the movie list
        movie.display()                                         #Calls the display METHOD on each Movie object, which prints its details. (What that object can do)
        
def show_menu():                                                #Defines a function where the user would be shown the menu and asked to choose
    print("1. Enter a Movie") 
    print("2. View Listed Movies") 
    print("3. Exit")
    
while True:                                                     #It keeps asking the user to choose from 1, 2, 3, until they choose, or until they exit the program
    show_menu()                                                 #Shows the menu
    choice = input("Please choose from numbers 1, 2, 3: ")      #Ask the user to choose
    if choice == "1":                                           #if the choice is 1, the program will let the user enter a movie. 
        enter_movie() 
    elif choice == "2":                                         #if they choose 2, the program will let the user to view the movie list. 
        view_movies() 
    elif choice == "3":                                         #if they choose 3, the program will exit.
     exit()
    else: 
        print("Invalid input, please enter a number between 1,2,3: ")