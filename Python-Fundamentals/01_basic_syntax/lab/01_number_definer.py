number = float(input())
result = ''

if number == 0:
    result = 'zero'
elif number > 0:
    if abs(number) > 1000000:
        result = 'large positive'
    elif abs(number) < 1:
        result = 'small positive'
    else:
        result = 'positive'
elif number < 0:
    if abs(number) > 1000000:
        result = 'large negative'
    elif abs(number) < 1:
        result = 'small negative'
    else:
        result = 'negative'

print(result)