numbers = [int(x) for x in input().split()]
target = int(input())
used_numbers = set()

for num1 in numbers:
    for num2 in numbers:
        if (num1 != num2) and (num1 not in used_numbers and num2 not in used_numbers) and (num1 + num2) == target:
            print(f"{num1} + {num2} = {target}")
            used_numbers.add(num1),
            used_numbers.add(num2)

