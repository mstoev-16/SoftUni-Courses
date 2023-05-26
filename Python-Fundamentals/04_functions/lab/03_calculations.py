def calculate(operator, num1, num2):
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