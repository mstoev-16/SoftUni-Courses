def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def add_and_subtract(a, b, c):
    summation = add(a, b)
    difference = subtract(summation, c)

    return difference


print(add_and_subtract(int(input()), int(input()), int(input())))





