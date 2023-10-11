import re


def get_searched_words(file_path):
    with open(file_path) as file:
        searched_words = file.read().split()
    return searched_words


def get_word_count(file_path, searched_words):
    word_count = {}
    with open(file_path) as file:
        text = file.read()
        for word in searched_words:
            pattern = fr'\b{word}\b'
            count = len(re.findall(pattern, text, re.IGNORECASE))
            word_count[word] = count
    return word_count


def save_result(file_path, word_count):
    with open(file_path, 'w') as file:
        sorted_words = sorted(word_count.items(), key=lambda x: -x[1])

        for word, count in sorted_words:
            file.write(f'{word} - {count}\n')


words = get_searched_words('words.txt')
counted_words = get_word_count('input.txt', words)
save_result('output.txt', counted_words)
