def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ''
    for name, qty in sorted_cheeses:
        result += name + '\n'
        qty = sorted(qty, reverse=True)
        result += '\n'.join(str(el) for el in qty) + '\n'
    result = result.strip()
    return result