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
    
        except FileNotFoundError:
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