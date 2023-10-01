m, n = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split()] for _ in range(m)]

for col in range(n):
    column_sum = 0
    for row in range(m):
        column_sum += matrix[row][col]
    print(column_sum)