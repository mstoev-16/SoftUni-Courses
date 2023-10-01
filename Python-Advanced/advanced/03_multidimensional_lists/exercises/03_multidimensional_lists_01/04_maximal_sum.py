import sys
m, n = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(m)]
max_sum = -sys.maxsize
sub_matrix = []

for i in range(m - 2):
    current_sum = 0
    for j in range(n - 2):
        current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] \
                      + matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2] \
                      + matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
                          [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
                          [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]]

print(f"Sum = {max_sum}")
for line in sub_matrix:
    print(' '.join([str(el) for el in line]))
