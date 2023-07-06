string = list(input())
string_data = {}

for el in string:
    if el != ' ':
        if el not in string_data:
            string_data[el] = 1
        else:
            string_data[el] += 1

for key, value in string_data.items():
    print(key, '->', value)