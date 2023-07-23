initial_string = input().upper()
unique_symbols = ''
substring = ''
processed_string = ''

for i in range(len(initial_string)):
    if not initial_string[i].isdigit():
        substring += initial_string[i]

    else:
        if i + 1 in range(len(initial_string)) and initial_string[i + 1].isdigit():
            n = int(initial_string[i] + initial_string[i + 1])
            processed_string += substring * n
            substring = ''
            continue
        else:
            n = int(initial_string[i])
            processed_string += substring * n
            substring = ''

print(f"Unique symbols used: {len(set(processed_string))}")
print(processed_string)