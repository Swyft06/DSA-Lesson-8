#queue: first in first out | last in last out
#enqueue: add items
#dequeue: remove items

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,n):
        self.queue.append(n)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        print("Number of elements: ",len(self.queue))


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print("Before removing an element: ")
q.display()
q.size()

q.dequeue()
q.dequeue()

print("After removing elements")
q.display()
