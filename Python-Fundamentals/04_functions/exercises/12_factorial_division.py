# Newest attempt at solving
def divide_2_factorials(number1, number2):
    factorial_1 = 1
    factorial_2 = 1

    for num in range(number1, 0, -1):
        factorial_1 *= num

    for num in range(number2, 0, -1):
        factorial_2 *= num

    return f'{factorial_1 / factorial_2:.2f}'


print(divide_2_factorials(int(input()), int(input())))


# First attempt
def factorial(num1, num2):
    factorial1 = 1
    factorial2 = 1

    for number1 in range(1, num1 + 1):
        factorial1 *= number1

    for number2 in range(1, num2 + 1):
        factorial2 *= number2

    return f'{factorial1 / factorial2:.2f}'


input_n1 = int(input())
input_n2 = int(input())
print(factorial(input_n1, input_n2))