def read_next(*args):
    for arg in args:
        for el in arg:
            yield el


a = read_next('aloha', [1, 2, 3, 4, "hello"], {1: 'b', 2: 'c'})
for el in a:
    print(el)