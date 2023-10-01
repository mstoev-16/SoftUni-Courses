def grocery_store(**kwargs):
    sorted_groceries = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = []
    for name, qty in sorted_groceries:
        result.append(f"{name}: {qty}")
    return '\n'.join(result)
