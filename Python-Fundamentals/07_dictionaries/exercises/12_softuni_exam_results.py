exam_submissions = {}
exam_data = {}

while True:
    data = input()
    if data == 'exam finished':
        break
    data = data.split('-')

    if len(data) == 3:
        user, current_language, points = data[0], data[1], int(data[2])
        if user not in exam_data:
            exam_data[user] = 0
        if points > exam_data[user]:
            exam_data[user] = points
        if current_language not in exam_submissions:
            exam_submissions[current_language] = 0
        exam_submissions[current_language] += 1

    if len(data) == 2:
        user, command = data[0], data[1]
        if command == 'banned' and user in exam_data:
            del exam_data[user]

print('Results:')
for user in exam_data.keys():
    print(user, '|', exam_data[user])
print('Submissions:')
for language in exam_submissions.keys():
    print(language, '-', exam_submissions[language])