# nums = [int(el) for el in input().split(', ')]
# even_nums_indices = [i for i in range(len(nums)) if nums[i] % 2 == 0]
# print(even_nums_indices)

# nums = list(map(int, input().split(', ')))
# even_nums_indices = list(map())

# numbers = input().split()
#
# nums_to_int = list(map(int, numbers))
# evens = list(filter(lambda x: nums_to_int[x] % 2 == 0, range(len(nums_to_int))))
# print(evens)

# Woah
numbers = input().split(', ')
indices_of_evens = [index for index in range(len(numbers)) if int(numbers[index]) % 2 == 0]
print(indices_of_evens)

# Another Way
numbers = list(map(int, input().split(', ')))
even_indices = list(filter(lambda x: numbers[x] % 2 == 0, range(len(numbers))))
print(even_indices)