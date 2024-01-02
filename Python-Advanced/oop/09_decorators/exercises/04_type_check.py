def type_check(received_type):
    def decorator(func):
        def wrapper(param):
            if not isinstance(param, received_type):
                return "Bad Type"
            result = func(param)
            return result
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2
