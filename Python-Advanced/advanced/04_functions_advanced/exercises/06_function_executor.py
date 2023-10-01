def func_executor(*args):
    result = []
    for func, params in args:
        result.append(f'{func.__name__} - {func(*params)}')
    return '\n'.join(result)

# try to do it on a single line
