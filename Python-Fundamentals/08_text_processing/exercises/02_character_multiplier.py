total_sum = 0
strings = input().split()
string_1 = strings[0]
string_2 = strings[1]
remaining = ''
len_difference = abs(len(string_2) - len(string_1))

if len(string_1) > len(string_2):
    working_len = len(string_2)
    remaining = string_1[-len_difference:]

elif len(string_1) < len(string_2):
    working_len = len(string_1)
    remaining = string_2[-len_difference:]
else:
    working_len = len(string_1)

for i in range(working_len):
    total_sum += (ord(string_1[i]) * ord(string_2[i]))

if remaining:
    for i in range(len(remaining)):
        total_sum += ord(remaining[i])

print(total_sum)