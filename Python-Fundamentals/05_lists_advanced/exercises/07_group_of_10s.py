# import math
# numbers = [int(num) for num in input().split(', ')]
# max_val = max(numbers)
#
# groups = [[] for i in range(0, (math.ceil(max_val / 10)))]
#
# for i in range(0, (math.ceil(max_val / 10))):
#
#     groups[i] = [num for num in numbers if i * 10 + 1 <= num <= 10 + i * 10]
#     print(f"Group of {i + 1}0's: {groups[i]}")
#


# import math
# numbers = [int(num) for num in input().split(', ')]
# max_10 = math.ceil(max(numbers) / 10)
# groups = [[]] * max_10
#
# for i in range(1, max_10 + 1):
#     groups[i - 1] = [num for num in numbers if 10 * i - 10 < num <= i * 10]
#     print(f"Group of {i}0's: {groups[i-1]}")


# import math
# str_to_num = [int(num) for num in input().split(', ')]
# max_group = math.ceil(max(str_to_num) / 10)
# groups = [[]] * max_group
#
# for i in range(1, max_group + 1):
#     groups[i-1] = [num for num in str_to_num if i - 0.9 <= num / 10 <= i]
#     print(f"Group of {i}0's: {groups[i-1]}")







