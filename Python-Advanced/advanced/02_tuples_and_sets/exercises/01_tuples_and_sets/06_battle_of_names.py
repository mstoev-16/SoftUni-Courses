n = int(input())
evens = set()
odds = set()

for row in range(1, n + 1):
    current_sum = 0
    name = list(input())

    for i in range(len(name)):
        current_sum += ord(name[i])
    current_sum //= row

    if current_sum % 2 == 0:
        evens.add(current_sum)
    else:
        odds.add(current_sum)

evens_sum = sum(evens)
odds_sum = sum(odds)

if evens_sum == odds_sum:
    result = odds.union(evens)
elif evens_sum > odds_sum:
    result = odds.symmetric_difference(evens)
elif evens_sum < odds_sum:
    result = odds.difference(evens)

print(*result, sep=', ')