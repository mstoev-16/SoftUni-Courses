def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return f"Enter valid values!"

    def area():
        return length * width

    def periemter():
        return 2 * (length + width)

    return f"Rectangle area: {area()}\n" \
           f"Rectangle perimeter: {periemter()}"
