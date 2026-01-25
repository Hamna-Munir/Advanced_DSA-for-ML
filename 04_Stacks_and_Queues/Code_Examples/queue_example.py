# Queue Example Implementation

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0


# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front element:", queue.peek())
print("Dequeued element:", queue.dequeue())
print("Front after dequeue:", queue.peek())

# Output:
# Front element: 10
# Dequeued element: 10
# Front after dequeue: 20
