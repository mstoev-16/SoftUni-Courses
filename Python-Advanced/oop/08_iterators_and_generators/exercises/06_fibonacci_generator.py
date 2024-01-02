def fibonacci():
    current = 0
    following = 1

    while True:
        yield current
        prev = current
        current = following
        following = current + prev


generator = fibonacci()
for i in range(5):
    print(next(generator))