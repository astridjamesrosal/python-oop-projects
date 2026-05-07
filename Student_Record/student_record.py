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
    def save(self):

    def load(self):
    