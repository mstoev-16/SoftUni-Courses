class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.start_idx = 0
        self.curr_idx = len(iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_idx < self.start_idx:
            raise StopIteration
        idx = self.curr_idx
        self.curr_idx -= 1
        return self.iterable[idx]
