# Better way
def check_palindromes(numbers):
    result = ['True' if num == num[::-1] else 'False' for num in numbers]

    return '\n'.join(result)


print(check_palindromes(input().split(', ')))


# Long way
def is_palindrome(text):
    reversed_text = text[::-1]

    if text == reversed_text:
        return True
    return False


def separate_input(element, separator):
    str_to_num = element.split(separator)

    return str_to_num


input_text = input()

for el in separate_input(input_text, ', '):
    print(is_palindrome(el))
