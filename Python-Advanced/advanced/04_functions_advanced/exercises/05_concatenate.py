def concatenate(*args, **kwargs):
    string = ''.join(args)
    for key, value in kwargs.items():
        if key in string:   # not necessary check
            string = string.replace(key, value)
    return string

print(concatenate("I", " ", "Love", " ", "Cythons",
C="P", s="", java='Java'))