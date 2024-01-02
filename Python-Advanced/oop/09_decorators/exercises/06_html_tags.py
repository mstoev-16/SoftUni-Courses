def tags(el):
    def decorator(func_ref):
        def wrapper(*args):
            result = func_ref(*args)
            return f"<{el}>{result}</{el}>"
        return wrapper
    return decorator



@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
