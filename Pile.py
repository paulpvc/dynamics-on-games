class Pile:
    def __init__(self):
        self.stack = []

    def add(self, val):
        self.stack.append(val)

    def empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

    def pop(self):
        if not self.empty():
            return self.stack.pop(self.size()-1)


