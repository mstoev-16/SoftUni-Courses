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