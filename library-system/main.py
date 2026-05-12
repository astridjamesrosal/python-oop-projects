from library_system import Library

print("Welcome to Astral, where imaginations shine")

library = Library("library.json")                                   #Initialize once outside the loop to prevent repeated storage access and memory overhead.

while True:

    print("1. Add a Book")
    print("2. Search a Book by Title")
    print("3. Search a Book by Author")
    print("4. Filter Library by Genre")
    print("5. Filter Library by Availability")
    print("6. Sort Books by Year")
    print("7. Borrow a Book")
    print("8. Return a Book")
    print("9. Exit Library")

    choice = input("Please choose what you would like to do: ")
    try:
        choice = int(choice)                                        #Attempt to convert input is inside a try/except to avoid crashing which leads to bad user experience.             
    except ValueError:
        print("Invalid Input, Please enter a valid number")
        continue
    if choice < 1 or choice > 9:                                                
        print("Invalid Input")
        continue
    
    if choice == 1:
        title = input("What is the title of the book?: ")
        author = input("Who is the author of the book?: ")
        genre = input("What is the genre of the book?: ")
        year = int(input("When was the book published?: "))         #Ensure the year is stored as an integer for proper sorting later.
        book = library.add_book(title, author, genre, year)                    
        print(f"{book.title} added into the library successfully!")

    elif choice == 2:
        title = input("What is the title of the book?: ")
        results = library.search_by_title(title)                              
        if not results:
            print("Book Not Found")
        else:
            for result in results:
                print(f"{result.id}, {result.title}, {result.author}, {result.genre}, {result.year}")

    elif choice == 3:
        author = input("Who is the author of the book?: ")
        results = library.search_by_author(author)                  
        if not results:
            print("Book Not Found")
        else:
            for result in results:
                print(f"{result.id}, {result.title}, {result.author}, {result.genre}, {result.year}")

    elif choice == 4:
        genre = input("What genre would you like to filter?: ")
        results = library.filter_by_genre(genre)                    
        if not results:
            print("Book Not Found")
        else:
            for result in results:
                print(f"{result.id}, {result.title}, {result.author}, {result.genre}, {result.year}")

    elif choice == 5:
        answer = input("Would you like to see which books are available?(yes/no): ")
        if answer == "yes":
            is_available = True
        elif answer == "no":
            is_available = False
        else:
            print("Invalid Input")
            continue
        results = library.filter_by_availability(is_available)
        if not results:
            print("Book Not Found")
        else:
            for result in results:
                print(f"{result.id}, {result.title}, {result.author}, {result.genre}, {result.year}")
    
    elif choice == 6:
        results = library.sort_by_year()
        if not results:
            print("Book Not Found")
        else:
            for result in results:
                print(f"{result.id}, {result.title}, {result.author}, {result.genre}, {result.year}")

    elif choice == 7:
        book_id = int(input("Please enter the ID of the book you would like to borrow: "))
        borrowed = library.borrow_book(book_id)
        if borrowed: 
            print("Book borrowed successfully!")
        else: 
            print("Sorry book is unavailable for borrowing.")


    elif choice == 8:
        book_id = int(input("Please enter the ID of the book you would like to return: "))
        returned = library.return_book(book_id)
        if returned:
            print("Thanks for returning the book. Have a nice day!")
        else:
            print("Book is not currently borrowed.")

    elif choice == 9:
        print("Thank you for visiting Astral")
        break