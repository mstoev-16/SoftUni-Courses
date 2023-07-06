students = {}
idx = 0

while True:
    student_data = input()

    if ':' not in student_data:
        break

    [name, student_id, course] = student_data.split(':')
    course = '_'.join(course.split())
    single_student = {
        'name': name,
        'student_id': student_id,
        'course': course
    }
    students[f"{idx}"] = single_student
    idx += 1

for i in range(len(students)):
    if student_data == students[f"{i}"]['course']:
        print(students[f"{i}"]['name'], "-", students[f"{i}"]['student_id'])