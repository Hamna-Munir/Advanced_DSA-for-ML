# Priority Queue Example Implementation

import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, value, priority):
        heapq.heappush(self.heap, (priority, value))

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def peek(self):
        if self.heap:
            return self.heap[0]
        return None


# Example usage
pq = PriorityQueue()
pq.push("Task A", 3)
pq.push("Task B", 1)
pq.push("Task C", 2)

print("Top priority element:", pq.peek())
print("Removed element:", pq.pop())
print("Next priority element:", pq.peek())

# Output:
# Top priority element: (1, 'Task B')
# Removed element: (1, 'Task B')
# Next priority element: (2, 'Task C')
