expression = input()
stack = []

for i in range(len(expression)):
    if expression[i] == '(':
        stack.append(i)
    elif expression[i] == ')':
        print(expression[stack.pop():i + 1])