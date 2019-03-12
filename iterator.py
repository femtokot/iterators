class RangeIterator:
    def __iter__(self):
        return self

    def __init__(self, start, stop, step):
        if step == 0:
            raise ValueError("Step should not be zero")
        self.start = start
        self.stop = stop
        self.step = step
        self.current = self.start

    def __next__(self):
        if self.step < 0:
            if self.current > self.stop:
                a = self.n

                self.current = self.current + self.step
                return a
            raise StopIteration
        else:
            while self.current < self.stop:
                a = self.current
                self.current = self.current + self.step
                return a


