test_string = input()

e_list = test_string.split()

for i in range(len(e_list)):
    e_list[i] = int(e_list[i])

    if e_list[i] < 0:
        e_list[i] *= - 1
    elif e_list[i] > 0:
        e_list[i] *= -1

print(e_list)




