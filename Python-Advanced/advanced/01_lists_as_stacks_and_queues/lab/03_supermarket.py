from collections import deque

client_queue = deque()

while True:
    command = input()
    if command == 'End':
        break
    elif command == 'Paid':
        while client_queue:
            print(client_queue.pop())
    else:
        client_queue.appendleft(command)

print(f"{len(client_queue)} people remaining.")