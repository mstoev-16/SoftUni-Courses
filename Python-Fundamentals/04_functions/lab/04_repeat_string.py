# Standard approach
def repeat_string(word, repetitions):
    repeated_string = word * repetitions
    return repeated_string


print(repeat_string(input(), int(input())))


# Using lambda
repeated_string = lambda string, repetitions: string * repetitions

print(repeated_string(input(), int(input())))
