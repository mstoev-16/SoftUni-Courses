string = list(input())
explosion_strength = 0
explosions = 0
n_explosions = string.count('>')


for i in range(len(string)):
    if i + 1 in range(len(string)):
        if string[i] == '>' and string[i + 1].isdigit():
            explosion_strength += int(string[i + 1]) - explosions
            explosions = 0

            for j in range(explosion_strength):
                if i + 1 in range(len(string)):
                    if string[i + 1] != '>':
                        string.pop(i + 1)
                        explosions += 1

                    else:
                        break
print(''.join(string))

