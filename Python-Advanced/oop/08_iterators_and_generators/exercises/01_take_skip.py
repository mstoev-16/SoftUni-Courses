class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.curr_cnt = 1
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_cnt > self.count:
            raise StopIteration
        current_num = self.start
        self.start += self.step
        self.curr_cnt += 1
        return current_num


# Alternatively
# class take_skip:
#     def __init__(self, step, count):
#         self.step = step
#         self.count = count
#         self.curr_cnt = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.curr_cnt == self.count:
#             raise StopIteration
#         curr_num = self.curr_cnt * self.step
#         self.curr_cnt += 1
#         return curr_num
