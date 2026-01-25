# Segment Tree

## 1. Concept Explanation 
A **Segment Tree** is a **binary tree data structure** used to efficiently perform **range queries and updates** on an array.

- Each node represents a **segment (interval) of the array**  
- Internal nodes combine information from their children (sum, min, max, etc.)  
- Leaf nodes represent **single elements**  

Segment Trees are very useful when:
- You need **frequent queries on ranges**  
- You need **frequent updates** to array elements  
- Operations must be faster than O(n) per query  

---

## 2. Visual / Example

Array: `[1, 3, 5, 7, 9, 11]`  

```python

     [0-5]
    /     \
 [0-2]    [3-5]
 /   \    /   \
[0-1] [2] [3-4] [5]
/
[0] [1]
```


- Leaf nodes store individual elements  
- Parent nodes store the **sum (or other function)** of their children  

Query example: Sum from index 1 to 4 → use relevant nodes without traversing entire array.

---

## 3. Time & Space Complexity

| Operation       | Complexity |
|-----------------|------------|
| Build Tree       | O(n)       |
| Range Query      | O(log n)   |
| Update Element   | O(log n)   |
| Space Complexity | O(2n)      |

Segment Trees provide **logarithmic query and update** on static or dynamic arrays.

---

## 4. Python Code

```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        # Build the segment tree
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        # Update element
        pos = index + self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def query(self, left, right):
        # Query sum in interval [left, right]
        result = 0
        left += self.n
        right += self.n
        while left <= right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 0:
                result += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return result

# Example usage
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)

print("Sum of range 1-4:", seg_tree.query(1, 4))
seg_tree.update(3, 10)
print("Sum of range 1-4 after update:", seg_tree.query(1, 4))
```
### Output

```python
Sum of range 1-4: 24
Sum of range 1-4 after update: 27
```
---

## 5. Common Interview Problems

- Range sum / min / max queries

- Range update with lazy propagation

- Count of numbers in a range satisfying conditions

- Maximum subarray sum using segment tree

- 2D Segment Trees for matrices

These problems test divide-and-conquer, tree construction, and query optimization.

---

## 6. ML Connection

Segment Trees are useful in ML for:

- Range aggregation in time series data

- Preprocessing features efficiently

- Calculating cumulative statistics for large datasets

- Implementing RL environments with efficient interval queries

- Handling dynamic feature updates in real-time pipelines

Segment Trees allow ML engineers to perform fast data queries without recomputing the entire dataset.

---

## 7. Practice Tasks

1. Implement range minimum query using segment tree

2. Implement range maximum query

3. Implement range sum query with lazy propagation

4. Implement segment tree for 2D array

5. Update multiple elements efficiently using segment tree

---

**Author:**  
Hamna Munir


