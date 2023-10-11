excluded_symbols = ["-", ",", ".", "!", "?"]

with open('text.txt') as file:
    for count, line in enumerate(file):
        if count % 2 == 0:
            current_line = ' '.join(reversed(line.split()))
            for symbol in excluded_symbols:
                current_line = current_line.replace(symbol, '@')
            print(current_line)


# A bit too long but still works
# with open('text.txt') as file:
#     lines = file.readlines()
#     even_lines = [lines[i] for i in range(len(lines)) if i % 2 == 0]
#
#     for i in range(len(even_lines)):
#         for symbol in excluded_symbols:
#             even_lines[i] = even_lines[i].replace(symbol, '@')
#
#     reversed_lines = []
#     for line in even_lines:
#         current_line = []
#         line = line.split()
#         while line:
#             current_line.append(line.pop())
#         reversed_lines.append(' '.join(current_line))
#
# print('\n'.join(reversed_lines))
#
