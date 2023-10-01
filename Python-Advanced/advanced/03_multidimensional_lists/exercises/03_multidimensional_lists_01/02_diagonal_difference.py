n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
primary = []
secondary = []

for i in range(n):
    primary.append(matrix[i][i])
    secondary.append(matrix[i][n - i - 1])

print(abs(sum(primary) - sum(secondary)))
