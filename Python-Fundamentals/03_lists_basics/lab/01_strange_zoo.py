tail = input()
body = input()
head = input()

# simple variant
meerkat = [head, body, tail]
print(meerkat)

# another variant
meerkat = [tail, body, head]
meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

print(meerkat)


