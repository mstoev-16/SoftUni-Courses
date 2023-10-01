initial_text = list(input())
unique_symbols = sorted(set(initial_text))

for el in unique_symbols:
    print(f"{el}: {initial_text.count(el)} time/s")