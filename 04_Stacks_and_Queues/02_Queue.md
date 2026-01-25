# Queue

## 1. Concept Explanation
A Queue is a linear data structure that follows the principle:

**FIFO — First In, First Out**

This means:
- The first element inserted is the first one removed  
- Insertion happens at the **rear**  
- Deletion happens from the **front**  

Queues are commonly used when:
- Tasks must be processed in order  
- Data flows continuously  
- Scheduling and buffering are required  

---

## 2. Visual / Example

Enqueue → [ 10 ] [ 20 ] [ 30 ] → Dequeue

Front Rear


Operations:
- **Enqueue** → Insert an element at the rear  
- **Dequeue** → Remove an element from the front  
- **Peek**    → View the front element  

---

## 3. Time & Space Complexity

| Operation | Time Complexity |
|-----------|-----------------|
| Enqueue   | O(1)            |
| Dequeue   | O(1)            |
| Peek      | O(1)            |
| Search    | O(n)            |

**Space Complexity:**  
- O(n) for storing `n` elements  

Queues provide efficient ordered processing.

---

## 4. Python Code

```python
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
print("Dequeued:", queue.dequeue())
print("Front after dequeue:", queue.peek())
```

### Output
```python
Front element: 10
Dequeued: 10
Front after dequeue: 20
```
---

##5. Common Interview Problems

Frequently asked queue problems include:

- Implement queue using stacks

- Design a circular queue

- Sliding window maximum

- First non-repeating character in a stream

- Implement deque operations

These problems test understanding of FIFO behavior and real-time processing.

---

##6. ML Connection

Queues are essential in ML systems for:

- Mini-batch scheduling during training

- Data buffering in streaming pipelines

- BFS traversal in graph-based models

- Task scheduling in distributed training

- Managing inference request queues

Understanding queues helps ML engineers build scalable, real-time data pipelines.

---

## 7. Practice Tasks

1. Implement queue using a list

2. Implement circular queue

3. Reverse first K elements of a queue

4. Generate binary numbers using a queue

5. Design a queue with O(1) min operation

---

**Author:**  
Hamna Munir
