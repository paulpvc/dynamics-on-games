class Pile:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def is_empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

    def pull(self):
        if not self.empty():
            return self.stack.pop(self.size()-1)


