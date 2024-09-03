class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.queue[0]

    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(6)
q.enqueue(7)
q.enqueue(2)

print(q.dequeue())
print(q.peek())
print(q.size())


