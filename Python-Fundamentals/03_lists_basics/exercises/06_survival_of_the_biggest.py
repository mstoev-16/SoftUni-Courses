# First way
numbers_list = input().split()
n_of_removed = int(input())

sorted_numbers = []
for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])

sorted_numbers = sorted(numbers_list.copy())
edited_list = numbers_list.copy()

for i in range(n_of_removed):
    for j in range(len(numbers_list)):

        if numbers_list[j] == sorted_numbers[i] and sorted_numbers[i] in edited_list:
            edited_list.remove(sorted_numbers[i])

for i in range(len(edited_list)):
    edited_list[i] = str(edited_list[i])

print(', '.join(edited_list))


# Alternative - preferable
import sys

numbers = input().split()
to_remove = int(input())
goal_len = len(numbers) - to_remove

while True:
    current_len = len(numbers)
    if current_len == goal_len:
        break

    smallest_num = sys.maxsize
    for number in numbers:
        if int(number) < smallest_num:
            smallest_num = int(number)

    if str(smallest_num) in numbers:
        numbers.remove(str(smallest_num))
    smallest_num = sys.maxsize

print(', '.join(numbers))