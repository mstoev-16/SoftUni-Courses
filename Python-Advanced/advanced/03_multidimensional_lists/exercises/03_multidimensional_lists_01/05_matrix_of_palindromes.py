m, n = [int(x) for x in input().split()]

for i in range(m):
    for j in range(n):
        print(f"{chr(97 + i)}{chr(97 + i + j)}{chr(97 + i)}", end=' ')
    print()