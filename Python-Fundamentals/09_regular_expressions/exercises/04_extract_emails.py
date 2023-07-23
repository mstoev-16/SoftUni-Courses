import re

data = input()
pattern = r'(^|(?<=\s))[a-z0-9]+[._-]?[a-z0-9]+@' \
          r'([a-z]+(-)?[a-z])+\.([a-z]+(-)?[a-z])+((\.[a-z]+(-)?[a-z])*)?($|(?=[.\s\!\?\,\-]))'

valid_emails = re.finditer(pattern, data)

for email in valid_emails:
    print(email.group())