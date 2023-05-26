def sorted_nums(numbers):
    numbers = [int(num) for num in numbers]
    sorted_numbers = sorted(numbers)

    return sorted_numbers


print(sorted_nums(input().split()))