values = input().split()
even_values = []

for i in range(len(values)):
    values[i] = int(values[i])


def filtering(value):
    if value % 2 == 0:
        return True
    else:
        return False


even = filter(filtering, values)

for i in even:
    even_values.append(i)

print(even_values)


# Another filter approach
def return_evens(numbers):
    num_to_int = [int(num) for num in numbers]
    evens = list(filter(lambda x: x % 2 == 0, num_to_int))

    return evens


print(return_evens(input().split()))