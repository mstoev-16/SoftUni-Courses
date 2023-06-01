# Standard approach
def absolute_values(numbers_list):

    for i in range(len(numbers_list)):
        numbers_list[i] = abs(float(numbers_list[i]))

    return numbers_list


print(absolute_values(input().split()))


# Comprehension
def absolute_values(values):
    str_to_num = [abs(float(num)) for num in values]
    return str_to_num


print(absolute_values(input().split()))


# With mapping
def abs_val(sequence):
    absolute_values = list(map(lambda x: abs(float(x)), sequence))
    return absolute_values


print(abs_val(input().split()))

