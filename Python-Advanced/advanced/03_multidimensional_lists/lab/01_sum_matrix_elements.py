m, n = [int(x) for x in input().split(', ')]
matrix = []
matrix_sum = 0

for _ in range(m):
    row = [int(x) for x in input().split(', ')]
    matrix_sum += sum(row)
    matrix.append(row)

print(matrix_sum)
print(matrix)