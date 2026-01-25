# Priority Queue

## 1. Concept Explanation 
A Priority Queue is a special type of queue where **each element is associated with a priority**, and elements are removed based on their priority rather than their insertion order.

Rules:
- Higher priority elements are processed first  
- If two elements have the same priority, they follow FIFO order  

Priority queues are commonly implemented using **heaps** for efficiency.

---

## 2. Visual / Example

Insert: (A, 3) (B, 1) (C, 2)

Processing Order:

(B, 1) → (C, 2) → (A, 3)


Lower number = higher priority (by convention in many systems)

Operations:
- **Insert** → Add element with priority  
- **Extract-Min / Extract-Max** → Remove highest priority element  
- **Peek** → View highest priority element  

---

## 3. Time & Space Complexity

| Operation        | Time Complexity |
|------------------|-----------------|
| Insert           | O(log n)        |
| Extract-Min/Max  | O(log n)        |
| Peek             | O(1)            |
| Search           | O(n)            |

**Space Complexity:**  
- O(n) for storing `n` elements  

Efficiency comes from maintaining the heap structure.

---

## 4. Python Code

```python
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

print("Top priority:", pq.peek())
print("Removed:", pq.pop())
print("Next priority:", pq.peek())
```
### Output

```python
Top priority: (1, 'Task B')
Removed: (1, 'Task B')
Next priority: (2, 'Task C')
```
---

## 5. Common Interview Problems

Common priority queue problems include:

- Find K largest or smallest elements

- Merge K sorted lists

- Design a task scheduler

- Implement Dijkstra’s algorithm

- Find median from a data stream

These problems test understanding of heap properties and efficient ordering.

---

## 6. ML Connection

Priority queues are heavily used in:

- Dijkstra and A* algorithms for graph-based ML models

- Scheduling training jobs by priority

- Beam search in NLP models

- Event-driven simulation systems

- Resource allocation in distributed ML

Understanding priority queues helps ML engineers design efficient search, scheduling, and optimization systems.

---


## 7. Practice Tasks

1. Implement max-priority queue using heap

2. Find K nearest points using priority queue

3. Implement running median using two heaps

4. Design a task scheduler with priorities

5. Solve Dijkstra’s algorithm using a priority queue

---

**Author:**  
Hamna Munir
