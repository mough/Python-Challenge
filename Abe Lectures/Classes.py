from functools import lru_cache

class Building:
    def __init__(self, n, s, e, w, h = 10):
        self.n = n
        self.s = s
        self.e = e
        self.w = w
        self.h = h
        self.width = abs(e - w)
        self.len = abs(n - s)

    def get_width(self):
        return self.width

    def get_len(self):
        return self.len

    @property  # turns area to a read-only attribute
    @lru_cache()  # will return value that's cached instead of re-calculating it
    def area(self):
        return self.len * self.width

b = Building(2, 4, 8, 10)
print(b.area)
