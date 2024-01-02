def reverse_text(string):
    current_idx = len(string) - 1
    end = 0
    while current_idx >= end:
        yield string[current_idx]
        current_idx -= 1

    # Alternatively
    # for i in range(current_idx, -1, -1):
    #     yield string[current_idx]


for char in reverse_text("step"):
    print(char, end='')
