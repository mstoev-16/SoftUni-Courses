nums = [int(num) for num in input().split(', ')]

positives = ', '.join([str(posit) for posit in nums if posit >= 0])
negatives = ', '.join([str(neg) for neg in nums if neg < 0])
evens = ', '.join([str(even) for even in nums if even % 2 == 0])
odds = ', '.join([str(odd) for odd in nums if odd % 2 != 0])

print(f'Positive: {positives}')
print(f'Negative: {negatives}')
print(f'Even: {evens}')
print(f'Odd: {odds}')


# numbers = input().split(', ')
#
# positives = [num for num in numbers if int(num) > 0]
# negatives = [num for num in numbers if int(num) < 0]
# evens = [num for num in numbers if int(num) % 2 == 0]
# odds = [num for num in numbers if int(num) % 2 != 0]
#
# print(f"Positive: {', '.join(positives)}")
# print(f"Negative: {', '.join(negatives)}")
# print(f"Even: {', '.join(evens)}")
# print(f"Odd: {', '.join(odds)}")
