grades_data = {}

for _ in range(int(input())):
    student = input()
    grade = float(input())

    if student not in grades_data:
        grades_data[student] = [grade]
    else:
        grades_data[student].append(grade)

for student, grades in grades_data.items():
    average_grade = sum(grades) / len(grades)
    grades_data[student] = average_grade

for student, grades in grades_data.items():
    if grades >= 4.50:
        print(student, '->', f"{grades:.2f}")