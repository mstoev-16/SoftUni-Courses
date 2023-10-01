from collections import deque

main_colors = ['red', 'blue', 'yellow']
required_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}
substrings = deque(el for el in input().split())
temp_colors = []
final_colors = []

while substrings:
    first = substrings.popleft()
    last = substrings.pop() if substrings else ''

    color = first + last
    if color in main_colors or color in required_colors:
        temp_colors.append(color)
        continue

    color = last + first
    if color in main_colors or color in required_colors:
        temp_colors.append(color)
        continue

    first = first[:-1]
    last = last[:-1]

    if first:
        substrings.insert(len(substrings) // 2, first)
    if last:
        substrings.insert(len(substrings) // 2, last)

for color in temp_colors:
    if color in required_colors:
        for main_color in required_colors[color]:
            if main_color not in temp_colors:
                break
        else:
            final_colors.append(color)
    else:
        final_colors.append(color)

print(final_colors)