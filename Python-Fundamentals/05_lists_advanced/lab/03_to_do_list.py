to_do_list = []

while True:
    command = input()

    if command == 'End':
        break

    command = command.split('-')
    importance = int(command[0])
    task = command[1]

    to_do_list.insert(importance - 1, task)

print(to_do_list)


# Noice
# ordered = [0] * 10
# while True:
#     data = input()
#
#     if data == 'End':
#         break
#
#     temp = data.split('-')
#     index = int(temp[0]) - 1
#     value = temp[1]
#     ordered.pop(index)
#     ordered.insert(index, value)
#
# new = [data for data in ordered if data != 0]
# print(new)


