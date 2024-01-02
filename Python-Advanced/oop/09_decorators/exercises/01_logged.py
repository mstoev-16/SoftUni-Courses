def logged(function):
    def wrapper(*args):
        result = function(*args)
        result_msg = f"you called {function.__name__}{args}\nit returned {result}"
        return result_msg
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(2, 3, 4))

