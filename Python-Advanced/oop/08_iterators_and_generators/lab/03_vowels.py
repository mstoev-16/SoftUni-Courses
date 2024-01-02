class vowels:
    def __init__(self, string_obj):
        self.string_obj = string_obj
        vowel_list = ['a', 'e', 'o', 'u', 'i', 'y']
        self.found_vowels = [vowel for vowel in self.string_obj if vowel.lower() in vowel_list]
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.found_vowels):
            raise StopIteration
        current_idx = self.idx
        self.idx += 1
        return self.found_vowels[current_idx]
