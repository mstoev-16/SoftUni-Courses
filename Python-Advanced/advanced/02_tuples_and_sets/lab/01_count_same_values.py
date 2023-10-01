numbers = (float(num) for num in input().split())
number_occurences = {}

for num in numbers:
    if num not in number_occurences:
        number_occurences[num] = 0
    number_occurences[num] += 1

for num, count in number_occurences.items():
    print(f"{num:.1f} - {count} times")