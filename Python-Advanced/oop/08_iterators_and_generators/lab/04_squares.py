def squares(n):
    num = 1
    while num <= n:
        yield num * num
        num += 1

    # Alternatively
    # for i in range(1, n + 1):
    #     yield num * num
