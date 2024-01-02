def vowel_filter(function):
    def wrapper():
        letters = function()
        vowels_list = ['a', 'e', 'i', 'o', 'u', 'y']
        returned_vowels = [letter for letter in letters if letter.lower() in vowels_list]
        return returned_vowels
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
