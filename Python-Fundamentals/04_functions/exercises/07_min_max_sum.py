def nums(numbers):
    numbers = [int(num) for num in numbers]
    min_n = min(numbers)
    max_n = max(numbers)
    sum_n = sum(numbers)

    return f'The minimum number is {min_n}\n' \
           f'The maximum number is {max_n}\n' \
           f'The sum number is: {sum_n}'


print(nums(input().split()))