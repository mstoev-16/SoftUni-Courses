class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.number:
            raise StopIteration
        current_symbol = self.sequence[self.count % len(self.sequence)]
        self.count += 1
        return current_symbol


seq = sequence_repeat('abc', 5)
for x in seq:
    print(x)