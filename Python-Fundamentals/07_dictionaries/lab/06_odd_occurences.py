lower_names = list(map(lambda x: x.lower(), input().split()))
name_dict = {}
odd_list = []

for el in lower_names:
    if el not in name_dict:
        name_dict[el] = 1
    else:
        name_dict[el] += 1

for key, value in name_dict.items():
    if value % 2 != 0:
        odd_list.append(key)

print(' '.join(odd_list))
