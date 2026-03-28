class StudentGrades:
    def __init__(self, name):
        self.student_name = name
        self.__marks = 0   # private variable

    def add_marks(self, score):
        if score < 0 or score > 100:
            print("Invalid Score")
        else:
            self.__marks = score

    def get_marks(self):
        return self.__marks


# testing
student = StudentGrades("Ali")

# trying direct access (will not work properly)
# print(student.__marks)   # ❌ error

student.add_marks(85)
print("Marks:", student.get_marks())

student.add_marks(120)   # invalid