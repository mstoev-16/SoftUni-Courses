synonym_dict = {}

for _ in range(int(input())):
    word = input()
    synonym = input()

    if word not in synonym_dict:
        synonym_dict[word] = [synonym]
    else:
        synonym_dict[word].append(synonym)

for key, value in synonym_dict.items():
    print(key, '-', ', '.join(value))