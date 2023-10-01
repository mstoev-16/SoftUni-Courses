n = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]
primary = []
secondary = []

for i in range(n):
    primary.append(matrix[i][i])
    secondary.append(matrix[i][n - i - 1])

print(f"Primary diagonal: {', '.join([str(el) for el in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(el) for el in secondary])}. Sum: {sum(secondary)}")