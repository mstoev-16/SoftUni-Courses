def even_numbers(function):
    def wrapper(num_list):
        numbers_list = function(num_list)
        result = list(filter(lambda x: x % 2 == 0, numbers_list))
        return result
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
