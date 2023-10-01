initial_list = [el for el in input().split('|')]
new_list = []

while initial_list:
    line = initial_list.pop().split()
    for el in line:
        new_list.append(el)

print(*new_list)