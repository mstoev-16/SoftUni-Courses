# First approach
gifts = input().split()

while True:
    command = input()
    if command == 'No Money':
        break

    for i in range(len(gifts)):
        if 'OutOfStock' in command and gifts[i] in command:
            gifts[i] = 'None'
        elif 'Required' in command:
            temp_list = command.split()
            if int(temp_list[-1]) < len(gifts):
                gifts[int(temp_list[-1])] = temp_list[1]
        elif 'JustInCase' in command:
            temp_list = command.split()
            gifts[-1] = temp_list[1]

final_gifts = gifts.copy()

for i in range(len(gifts)):
    if 'None' in final_gifts:
        final_gifts.remove('None')

print(' '.join(final_gifts))


#  Almost the same
gifts = input().split()
new_gifts = []

while True:
    command = input()

    if command == 'No Money':
        break

    temp_list = command.split()

    for i in range(len(gifts)):
        if 'OutOfStock' == temp_list[0] and temp_list[1] == gifts[i]:
            gifts[i] = 'None'
    if 'Required' == temp_list[0] and int(temp_list[2]) < len(gifts):
        gifts[int(temp_list[2])] = temp_list[1]
    elif 'JustInCase' == temp_list[0]:
        gifts[-1] = temp_list[1]

    new_gifts = gifts.copy()

for i in range(len(gifts)):
    if 'None' in new_gifts and new_gifts[i] == 'None':
        new_gifts.pop(i)

print(' '.join(new_gifts))




