repeating_chars = input()
processed_chars = repeating_chars[0]

for i in range(1, len(repeating_chars)):
    if repeating_chars[i] != processed_chars[-1]:
        processed_chars += repeating_chars[i]

print(processed_chars)