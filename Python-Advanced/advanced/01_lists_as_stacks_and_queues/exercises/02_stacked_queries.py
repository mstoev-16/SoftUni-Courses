query_stack = []
n = int(input())

for _ in range(n):
    command = input()

    if command.startswith('1 '):
        command = command.split()
        number = int(command[1])
        query_stack.append(number)
    elif command == '2' and query_stack:
        query_stack.pop()
    elif command == '3' and query_stack:
        print(max(query_stack))
    elif command == '4' and query_stack:
        print(min(query_stack))

while query_stack:
    number = query_stack.pop()

    if query_stack:
        print(number, end=', ')
    else:
        print(number)