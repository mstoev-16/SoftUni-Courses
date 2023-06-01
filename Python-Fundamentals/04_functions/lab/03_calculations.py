# Beginner approach
def calculate(operator, num1, num2):
    result = None
    if operator == 'add':
        result = num1 + num2
    elif operator == 'subtract':
        result = num1 - num2
    elif operator == 'multiply':
        result = num1 * num2
    elif operator == 'divide':
        result = num1 // num2

    print(result)


operator_input = input()
num1_input = int(input())
num2_input = int(input())

calculate(operator_input, num1_input, num2_input)


# Advanced way
def calculate(operation, num1, num2):
    return {
        'add': num1 + num2,
        'subtract': num1 - num2,
        'multiply': num1 * num2,
        'divide': int(num1 / num2)
    }.get(operation, 'Invalid operation')


print(calculate(input(), int(input()), int(input())))