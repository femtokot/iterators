class RangeIterator:
    def __iter__(self):
        return self

    def __init__(self, start, stop, step):
        if step == 0:
            raise ValueError("Step should not be zero")
        self.start = start
        self.stop = stop
        self.step = step
        self.n = self.start

    def __next__(self):
        if self.step < 0:
            while self.n > self.stop:
                a = self.n

                self.n = self.n + self.step
                return a
            raise StopIteration
        else:
            while self.n < self.stop:
                a = self.n
                self.n = self.n + self.step
                return a
            raise StopIteration

for i in RangeIterator(5, 5, -1):
    print(i)

