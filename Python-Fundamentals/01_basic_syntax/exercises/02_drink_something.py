age = int(input())

if age <= 14:
    result = 'drink toddy'
elif age <= 18:
    result = 'drink coke'
elif age <= 21:
    result = 'drink beer'
else:
    result = 'drink whisky'

print(result)
