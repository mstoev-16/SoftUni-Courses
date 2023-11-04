def print_rhombus(size):
    print_upper_rhombus(size)
    print_lower_rhombus(size)


def print_rows(size, stars):
    for j in range(size - stars):
        print(' ', end='')
    for j in range(1, stars):
        print('*', end=' ')
    print('*')


def print_upper_rhombus(size):
    for i in range(1, size + 1):
        print_rows(size, i)


def print_lower_rhombus(size):
    for i in range(size - 1, 0, -1):
        print_rows(size, i)


n = int(input())
print_rhombus(n)
