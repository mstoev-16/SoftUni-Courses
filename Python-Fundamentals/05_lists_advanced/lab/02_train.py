# n_wagons = int(input())
#
# train = [0 for _ in range(n_wagons)]
#
# while True:
#     command = input()
#
#     if command == 'End':
#         break
#
#     command = command.split()
#
#     if command[0] == 'add':
#         train[-1] += int(command[1])
#     elif command[0] == 'insert':
#         train[int(command[1])] += int(command[2])
#     elif command[0] == 'leave':
#         train[int(command[1])] -= int(command[2])
#
# print(train)
