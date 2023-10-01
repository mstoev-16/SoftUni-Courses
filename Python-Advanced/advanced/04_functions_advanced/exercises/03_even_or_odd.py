def even_odd(*args):
    sequence = [int(x) for x in args if isinstance(x, int)]
    command = args[-1]

    if command == 'odd':
        return list(filter(lambda x: x % 2 != 0, sequence))
    elif command == 'even':
        return list(filter(lambda x: x % 2 == 0, sequence))

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))