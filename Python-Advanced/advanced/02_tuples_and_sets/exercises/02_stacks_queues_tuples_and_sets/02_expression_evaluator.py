from collections import deque
expression = deque(input().split())
operators = '+-*/'
current_operation = deque()

for current_el in expression:

    if current_el not in operators:
        current_operation.append(int(current_el))
    else:
        while len(current_operation) > 1:
            num1 = current_operation.popleft()
            num2 = current_operation.popleft()
            if current_el == '+':
                result = num1 + num2
            elif current_el == '-':
                result = num1 - num2
            elif current_el == '*':
                result = num1 * num2
            elif current_el == '/':
                result = num1 // num2
            current_operation.appendleft(result)

print(result)