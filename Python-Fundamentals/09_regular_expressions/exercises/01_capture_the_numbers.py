import re

pattern = r'(?m)\d+'
data = input()
numbers = []

while data:
    current_numbers = re.findall(pattern, data)

    for num in current_numbers:
        numbers.append(num)

    data = input()
print(*numbers, sep=' ')

