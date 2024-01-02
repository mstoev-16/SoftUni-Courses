class dictionary_iter:
    def __init__(self, data):
        self.data = list(data.items())
        self.start = 0
        self.end = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        current_idx = self.start
        self.start += 1
        return self.data[current_idx]


# Alternatively, use a deque and popleft()
