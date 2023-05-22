# Simpler approach
n = int(input())


for num in range(1, n + 1):
    num_as_str = str(num)
    sum_of_digits = 0

    for char in num_as_str:
        sum_of_digits += int(char)

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')


# Interesting approach
# n = int(input())
#
# sum_of_digits = 0
#
# for i in range(1, n + 1):
#
#     digit = i
#     sum_of_digits = 0
#
#     while digit > 0:
#         sum_of_digits += digit % 10
#         digit = int(digit / 10)
#
#     if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
#         print(f'{i} -> True')
#     else:
#         print(f'{i} -> False')
