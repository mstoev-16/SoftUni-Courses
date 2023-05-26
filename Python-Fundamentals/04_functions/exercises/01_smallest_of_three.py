import sys


def smallest_int():
    min_number = sys.maxsize
    for _ in range(3):
        number = int(input())

        if number < min_number:
            min_number = number

    return min_number


print(smallest_int())