import sys

maximum_number = - sys.maxsize

for _ in range(3):
    number = int(input())

    if number > maximum_number:
        maximum_number = number

print(maximum_number)