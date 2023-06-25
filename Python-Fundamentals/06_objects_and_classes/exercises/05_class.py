class Class:
    __student_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, student_name, student_grade):
        if len(self.students) < Class.__student_count:
            self.students.append(student_name)
            self.grades.append(student_grade)

    def get_average_grade(self):
        average_grade = sum(self.grades) / len(self.grades)
        return average_grade

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. " \
               f"Average grade: {self.get_average_grade():.2f}"