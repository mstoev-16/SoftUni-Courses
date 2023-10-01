from collections import deque
m, n = [int(x) for x in input().split()]
matrix = []
snake = deque(input())

for i in range(m):
    matrix.append([''] * n)
    for j in range(n):
        if i % 2 == 0:
            matrix[i][j] = snake[0]
        else:
            matrix[i][-1 - j] = snake[0]
        snake.rotate(-1)

for line in matrix:
    print(*line, sep='')