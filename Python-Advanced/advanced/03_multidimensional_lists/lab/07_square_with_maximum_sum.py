import sys
m, n = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for _ in range(m)]
max_sum = -sys.maxsize
sub_matrix = []

for i in range(m - 1):
    current_sum = 0
    for j in range(n - 1):
        current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[matrix[i][j], matrix[i][j + 1]], [matrix[i + 1][j], matrix[i + 1][j + 1]]]

for line in sub_matrix:
    print(' '.join([str(el) for el in line]))
print(max_sum)