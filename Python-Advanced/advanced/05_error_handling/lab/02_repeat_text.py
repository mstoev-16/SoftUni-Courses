while True:
    try:
        name = str(input())
        times = int(input())
        print(name * times)
    except ValueError:
        print('Variable times must be an integer')
