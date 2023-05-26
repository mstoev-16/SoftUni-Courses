# Better way
def decide_perfect_number(number):
    numbers = [int(num) for num in range(1, (number // 2) + 1) if number % num == 0]

    if sum(numbers) == number:
        return 'We have a perfect number!'
    return 'It\'s not so perfect'


print(decide_perfect_number(int(input())))


# First time solving
def perfect_number(number):
    divisors_sum = 0

    for divisor in range(1, round(number / 2) + 1):
        if number % divisor == 0:
            divisors_sum += divisor

    if divisors_sum == number:
        return 'We have a perfect number!'
    return "It's not so perfect."


input_number = int(input())
print(perfect_number(input_number))

