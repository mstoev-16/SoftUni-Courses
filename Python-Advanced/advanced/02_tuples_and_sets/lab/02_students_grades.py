n = int(input())
student_grades = {}

for _ in range(n):
    student, grade = [x for x in input().split()]

    if student not in student_grades:
        student_grades[student] = []
    student_grades[student].append(float(grade))

for student, grades in student_grades.items():
    print(f"{student} -> {' '.join([f'{grade:.2f}' for grade in grades])} (avg: {sum(grades) / len(grades):.2f})")