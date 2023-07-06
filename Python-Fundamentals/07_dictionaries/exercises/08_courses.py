courses_data = {}

while True:
    command = input()

    if command == 'end':
        break

    [course_name, student_name] = command.split(' : ')
    if course_name not in courses_data:
        courses_data[course_name] = [student_name]
    else:
        courses_data[course_name].append(student_name)

for course_name in courses_data.keys():
    print(f"{course_name}: {len(courses_data[course_name])}")
    for student_name in courses_data[course_name]:
        print(f"-- {student_name}")