import json

class Student:
    def __init__(self, name, number, year, grade):
        if name.strip() == "":
            raise ValueError("Invalid Student Name")
        self.student_name = name
    
        if number.strip() == "":
            raise ValueError("Invalid Student Number")
        self.student_number = number
        
        if year not in [7, 8, 9, 10]:
            raise ValueError("Invalid Student Year")
        self.student_year = year
        
        if grade < 0 or grade > 100:
            raise ValueError("Invalid Student Grade")
        self.student_grade = grade
     
    def to_dict(self):
        return{"name": self.student_name,
               "number": self.student_number,
               "year": self.student_year,
               "grade": self.student_grade}
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["number"], data["year"], data["grade"])

class FileManager:
    def save(self, data):
        with open ("student_list.json", "w") as f:
            json.dump(data, f)
            
    def load(self):
        try:
            with open("student_list.json", "r") as f:
                return json.load(f)
    
        except (FileNotFoundError, json.JSONDecodeError):
            return []

class StudentRegistry:
    def __init__(self):
        self.students = []

    def add(self, name, number, year, grade):
        for student in self.students:
            if student.student_number == number:
                raise ValueError("Inputed ID already exists.")
        else:
            new_student = Student(name, number, year, grade)
            self.students.append(new_student)   
        
    def view_all(self):
        return self.students

    def update_grade(self, number, grade):
        for student in self.students:
            if student.student_number == number:
                student.student_grade = grade
                return
        else:
            raise ValueError("Inputed ID doesn't exists.")
        
    def delete(self, number):
        for student in self.students:
            if student.student_number == number:
                self.students.remove(student)
                return
        else:
            raise ValueError("Inputed ID doesn't exists.")

    def load_students(self, data):
        for dictionary in data:
            student = Student.from_dict(dictionary)
            self.students.append(student)

class Main:
    def __init__(self):
        self.file_manager = FileManager()
        self.student_registry = StudentRegistry()

        data = self.file_manager.load()
        self.student_registry.load_students(data)

    def run(self):
        print("Welcome to Astral High, where learning reach the galaxy.")
    
        while True:
            print("1. Add a Student")
            print("2. View Student List")
            print("3. Modify Student Grade")
            print("4. Remove Student")
            print("5. Exit")
            
            choice = input("What would you like to do? Choose a number: ")
        
            if choice == "1":
                try:
                    name = input("Please enter Student's Name: ")
                    number = input("Please enter Student's ID Number: ")
                    year = int(input("Please enter Student's Year Level: "))
                    grade = float(input("Please enter Student's Grade: "))
                    self.student_registry.add(name, number, year, grade)
                    data = [student.to_dict() for student in self.student_registry.view_all()]
                    self.file_manager.save(data)
                    print("Student Added Successfully!")
                except ValueError as error:
                    print(error)

            elif choice == "2":
                students = self.student_registry.view_all()
                if not students:
                    print("No students found")
                else: 
                    for student in students:
                        print(f"Name: {student.student_name}, ID: {student.student_number}, Year: {student.student_year}, Grade: {student.student_grade}")

            elif choice == "3":
                try: 
                    number = input("Please enter Student's ID Number: ")
                    grade = float(input("Please enter Student's New Grade: "))
                    self.student_registry.update_grade(number, grade)
                    data = [student.to_dict() for student in self.student_registry.view_all()]
                    self.file_manager.save(data)
                    print("Student Grade Updated Successfully!")
                except ValueError as error:
                    print(error)

            elif choice == "4":
                try:
                    number = input("Please enter the ID of the student you would like to remove: ")
                    self.student_registry.delete(number)
                    data = [student.to_dict() for student in self.student_registry.view_all()]
                    self.file_manager.save(data)
                    print("Student Removed Successfully!")
                except ValueError as error:
                    print(error)

            elif choice == "5":
                print("Thank you for using Astral High Student Record System. Goodbye!")
                break
            else:
                print("Invalid Input")

if __name__ == "__main__":
    astral = Main()
    astral.run()