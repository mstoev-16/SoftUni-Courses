parentheses = list(input())
stack = []
opening = '([{'
closing = ')]}'
pairs = '{}[]()'
balanced = True

for el in parentheses:
    if el in opening:
        stack.append(el)
    elif el in closing and stack:
        opening_el = stack.pop()
        if opening_el + el not in pairs:
            balanced = False
            break
    else:
        balanced = False
        break

if balanced:
    print('YES')
else:
    print('NO')