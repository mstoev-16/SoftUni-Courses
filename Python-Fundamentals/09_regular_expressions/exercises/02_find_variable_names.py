import re

data = input()
pattern = r'(?<=\b\_)[a-zA-Z]+($|(?=\s))'

variable_names = re.finditer(pattern, data)
valid_variables = [var.group() for var in variable_names]
print(*valid_variables, sep=',')
