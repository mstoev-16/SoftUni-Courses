import re

data = input()
word = input()
pattern = f"(^|(?<=\s)){word}($|(?=[\s\.\?\!\,\-]))"

repeated_word = re.finditer(pattern, data, re.IGNORECASE)
repeated_word = [word.group() for word in repeated_word]
print(len(repeated_word))