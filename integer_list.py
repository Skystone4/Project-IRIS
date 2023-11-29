class IntegerList:
    def __init__(self):
        self.integers = []

    def add_integer(self, num):
        self.integers.append(num)

    def remove_integer(self, num):
        if num in self.integers:
            self.integers.remove(num)
    def get_average(self):
        if not self.integers:
            return None
        return sum(self.integers) / len(self.integers)

    def get_max(self):
        if not self.integers:
            return None
        return max(self.integers)

    def get_min(self):
        if not self.integers:
            return None
        return min(self.integers)
