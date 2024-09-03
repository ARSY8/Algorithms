class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Ваш стэк пуст")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Ваш стэк пуст")
        return self.stack[-1]

    def size(self):
        return len(self.stack)

s = Stack()

s.push(6)
s.push(2)
s.push(5)
s.push(3)

print(s.pop())
print(s.peek())
print(s.size())
