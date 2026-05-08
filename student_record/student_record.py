import json                                                                     #Import JSON Tools in order to use methods like saving and loading list of dictionaries that contains the student's attributes.

class Student:                                                                  #Creates a blueprint called Student.
    def __init__(self, name, number, year, grade):                              #Init exist because Student must be created with valid data from the start, should have a valid name, ID, year, and grade right from the beginning.
        if name.strip() == "":                                                  #Strip removes whitespace from the edges and checks if the strings have nothing but whitespace.
            raise ValueError("Invalid Student Name")                            #It would raise a Value Error if the Condition is True.
        self.student_name = name                                                #"self.student_name" stores the value of "name" on the object.
    
        if number.strip() == "":                                                #Strip removes whitespace from the edges and checks if the strings have nothing but whitespace.
            raise ValueError("Invalid Student Number")                          #It would raise a Value Error if the Condition is True.
        self.student_number = number                                            #"self.student_number" stores the value of "number" on the object.
        
        if year not in [7, 8, 9, 10]:                                           #Condition that if the year inputed by the user is not included in 7, 8, 9, or 10.
            raise ValueError("Invalid Student Year")                            #It would raise a Value Error.
        self.student_year = year                                                #"self.student_year" stores the value of "year" on the object.
        
        if grade < 0 or grade > 100:                                            #Condition that if the grade is less than zero or greater than 100.
            raise ValueError("Invalid Student Grade")                           #It would raise a Value Error.
        self.student_grade = grade                                              #"self.student_grade" stores the value of "grade" on the object.
     
    def to_dict(self):                                                          #Method that returns the attributes and list them as a dictionary.
        return{"name": self.student_name,                               
               "number": self.student_number,
               "year": self.student_year,
               "grade": self.student_grade}
    
    @classmethod                                                                #@classmethod lets you call the method on the class directly before any object exist because from_dict creates the object so there no object to call it on yet.
    def from_dict(cls, data):                                                   #Method that returns the data with their attributes from the dictionary.
        return cls(data["name"], data["number"], data["year"], data["grade"])

class FileManager:                                                              #Creates a blueprint called FileManager.
    def save(self, data):                                                       #Method that automatically saves the changes once it is made by the user.
        with open ("student_list.json", "w") as f:                              #Opens the student_list json file and write on it as a file.
            json.dump(data, f)                                                  #Write every data that is changed in the json file.
            
    def load(self):                                                             #Method that loads all the existing dictionaries in the json file.
        try:                                                                   
            with open("student_list.json", "r") as f:                           #Opens the student_list json file and read on it as a file.
                return json.load(f)                                             #Returns all the list of dictionaries from the json file
    
        except (FileNotFoundError, json.JSONDecodeError):                       #If for instances, the file is not found, or if the json file exist but is empty.
            return []                                                           #Returns an empty list.

class StudentRegistry:                                                          #Creates a blueprint called StudentRegistry.
    def __init__(self):                                                         #Initializes automatically the attributes after being created.
        self.students = []                                                      #Holds Student objects in memory for the session.

    def add(self, name, number, year, grade):                                   #Method that let's the user add a student account through name, number, year, and grade.
        for student in self.students:                                           #Loops through every student in self.students
            if student.student_number == number:                                #If the student number already exists.
                raise ValueError("Inputed ID already exists.")                  #It would raise a ValueError
        else:                                                                   #for/else: only runs if the loop completes without finding a match
            new_student = Student(name, number, year, grade)                    #Stores the student in the new_student object with name, number, year, and grade.
            self.students.append(new_student)                                   #Adds the new_student in the self.students list.
        
    def view_all(self):                                                         #Method that let's the user view all the student accounts.
        return self.students                                                    #Returns the self.students list showing all the accounts.

    def update_grade(self, number, grade):                                      #Method that let's the user update the grade through student number and grade.
        for student in self.students:                                           #Loops through every student in self.students.
            if student.student_number == number:                                #If the number matches the student_number.
                student.student_grade = grade                                   #The student_grade would be replaced by the newly inputed grade.
                return                                                          #Exit the method.
        else:                                                                   #for/else: only runs if the loop completes without finding a match
            raise ValueError("Inputed ID doesn't exists.")                      #It would raise a ValueError
        
    def delete(self, number):                                                   #Method that let's the user remove a student through their ID number.
        for student in self.students:                                           #Loops through every student in self.students list.
            if student.student_number == number:                                #If the student number matches the inputed number.
                self.students.remove(student)                                   #The student would be removed.
                return                                                          #Exit the method.
        else:                                                                   #for/else: only runs if the loop completes without finding a match
            raise ValueError("Inputed ID doesn't exists.")                      #It would raise a ValueError

    def load_students(self, data):                                              #Method that loads all the students in the student_list.    
        for dictionary in data:                                                 #Loops through every dictionary in data.
            student = Student.from_dict(dictionary)                             #Converts raw JSON dictionaries into Student objects so validation and methods are available throughout the program.
            self.students.append(student)                                       #Adds the student in the self.students list.

class Main:                                                                     #Creates a blueprint called Main and is the Main Loop of the Program.
    def __init__(self):                                                         #Initializes automatically the attributes after being created.
        self.file_manager = FileManager()                                       #Creates a FileManager instance.
        self.student_registry = StudentRegistry()                               #Creates a StudentRegistry instance.

        data = self.file_manager.load()                                         #The data will be loaded by the File manager.
        self.student_registry.load_students(data)                               #The list of students will be loaded by the Student Registry.

    def run(self):                                                              #Method that runs the program from start  to finish.
        print("Welcome to Astral High, where learning reach the galaxy.")
    
        while True:                                                             #Keeps asking the user until they choose to exit the program.
            print("1. Add a Student")
            print("2. View Student List")
            print("3. Modify Student Grade")
            print("4. Remove Student")
            print("5. Exit")
            
            choice = input("What would you like to do? Choose a number: ")      #Ask for the choice of the user.
        
            if choice == "1":                                                   #If the user choose 1.
                try:                                                            
                    name = input("Please enter Student's Name: ")               #Ask the user for the student name.
                    number = input("Please enter Student's ID Number: ")        #Ask the user for the student id.
                    year = int(input("Please enter Student's Year Level: "))    #Ask the user for the student year.
                    grade = float(input("Please enter Student's Grade: "))      #Ask the user for the student grade.
                    self.student_registry.add(name, number, year, grade)        #Call the Add Method and Add those inputs in the student_registry.
                    data = [student.to_dict() for student in self.student_registry.view_all()]      #Converts student objects to dictionaries that are stored inside the data object which in then be used by the json.dump to write the data in the json file.
                    self.file_manager.save(data)                                #All data will be saved in the File Manager.
                    print("Student Added Successfully!")
                except ValueError as error:                                     #In any circumstance that the input is invalid.
                    print(error)

            elif choice == "2":                                                 #If the user choose 2.
                students = self.student_registry.view_all()                     #Calls the view_all method from the student_registry and store it in the students object.
                if not students:                                                #If there are no students.
                    print("No students found")                              
                else:                                                           #If there are students.
                    for student in students:                                    #Loop through every student in the students list.
                        print(f"Name: {student.student_name}, ID: {student.student_number}, Year: {student.student_year}, Grade: {student.student_grade}")

            elif choice == "3":                                                 #If the user choose 3.
                try:                                                            
                    number = input("Please enter Student's ID Number: ")        #Ask the user for the student ID number.
                    grade = float(input("Please enter Student's New Grade: "))      #Ask the user for the student new grade.
                    self.student_registry.update_grade(number, grade)           #Call Update_Grade method and update the grade in the student_registry through the number and grade given by the user.
                    data = [student.to_dict() for student in self.student_registry.view_all()]      #Converts student objects to dictionaries that are stored inside the data object which in then be used by the json.dump to write the data in the json file.
                    self.file_manager.save(data)                                #All data will be saved in the File Manager.
                    print("Student Grade Updated Successfully!")            
                except ValueError as error:                                     #In any circumstance that the input is invalid.
                    print(error)

            elif choice == "4":                                                 #If the user choose 4.
                try:                                                            
                    number = input("Please enter the ID of the student you would like to remove: ")     #Ask the user for the ID number of the student they would like to remove.
                    self.student_registry.delete(number)                                                #Calls the delete method in the student_registry and remove student using the number given by the user.
                    data = [student.to_dict() for student in self.student_registry.view_all()]          #Converts student objects to dictionaries that are stored inside the data object which in then be used by the json.dump to write the data in the json file.
                    self.file_manager.save(data)                                                        #All data will be saved in the File Manager.
                    print("Student Removed Successfully!")
                except ValueError as error:                                                             #In any circumstance that the input is invalid.
                    print(error)    

            elif choice == "5":                                                                         #If the user choose 5.
                print("Thank you for using Astral High Student Record System. Goodbye!")
                break                                                                                   #Exit the program
            else:                                                                                       #If the input is invalid
                print("Invalid Input")

if __name__ == "__main__":                                                                              #This ensure that main() will only run when we execute the file directly, and if other file tries to import it it will not run.
    astral = Main()
    astral.run()