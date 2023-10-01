n = int(input())

matrix = [[el for el in input()] for _ in range(n)]
symbol = input()
found = False

for i in range(n):
    if found:
        break
    for j in range(n):
        if matrix[i][j] == symbol:
            coordinates = (i, j)
            found = True
            break

if found:
    print(coordinates)
else:
    print(f"{symbol} does not occur in the matrix")