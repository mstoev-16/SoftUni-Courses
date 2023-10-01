n, m = [int(x) for x in input().split()]
set1 = set()
set2 = set()

for _ in range(n):
    set1.add(int(input()))

for _ in range(m):
    set2.add(int(input()))

set3 = set1.intersection(set2)
print(*set3, sep='\n')
