try:
    with open('numbers.txt') as file:
        print(sum([int(num) for num in file.readlines()]))
except FileNotFoundError:
    print('File not found.')


# total_sum = 0
# with open('numbers.txt') as file:
#     for line in file.readlines():
#         total_sum += int(line)
#     print(total_sum)


# To avoid additional newline
# with open('numbers.txt') as file:
#     [print(line, end='') for line in file.readlines()]
