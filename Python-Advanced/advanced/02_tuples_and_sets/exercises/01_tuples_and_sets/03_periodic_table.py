n = int(input())
compounds = set()

for _ in range(n):
    data = input().split()

    for el in data:
        compounds.add(el)

print(*compounds, sep='\n')
