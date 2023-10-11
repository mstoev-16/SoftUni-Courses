import re

line_numbers = []
with open('text.txt') as input_file, open('output.txt', 'w') as output_file:
    for count, line in enumerate(input_file):
        stripped_line = line.strip()
        letter_pattern = fr'[a-zA-Z]'
        punctuation_pattern = fr'[\,\.\!\?\'\"\:\-]'
        letter_count = len(re.findall(letter_pattern, stripped_line))
        punctuation_count = len(re.findall(punctuation_pattern, stripped_line))

        output_file.writelines(f"Line {count + 1}: {stripped_line} ({letter_count}) ({punctuation_count})\n")
