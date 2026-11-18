class Forward:
    def __init__(self):
        self.forward_stack = []

    def push(self, page):
        self.forward_stack.append(page)

    def pop(self):
        if not self.forward_stack:
            return None
        return self.forward_stack.pop()

    def is_empty(self):
        return len(self.forward_stack) == 0

    def clear(self):
        self.forward_stack.clear()
