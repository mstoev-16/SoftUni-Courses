n = int(input())
diagonal_sum = 0

matrix = [[int(x) for x in input().split()] for _ in range(n)]

for i in range(n):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)