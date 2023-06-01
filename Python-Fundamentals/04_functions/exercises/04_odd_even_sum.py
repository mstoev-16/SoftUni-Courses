# Second attempt (with filter)
def odd_and_even_sum(number):
    str_to_num = list(map(int, number))
    odd_sum = sum(list(filter(lambda x: x % 2 != 0, str_to_num)))
    even_sum = sum(list(filter(lambda x: x % 2 == 0, str_to_num)))

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


print(odd_and_even_sum(list(input())))


# First attempt
def sum_of_odd_and_even():
    number = input()
    even_sum = 0
    odd_sum = 0
    for i in range(len(number)):
        if int(number[i]) % 2 == 0:
            even_sum += int(number[i])
        else:
            odd_sum += int(number[i])

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


print(sum_of_odd_and_even())
