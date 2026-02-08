# Hashing

## 1. Concept Explanation 
**Hashing** is a technique used to store and retrieve data quickly by converting a key into a fixed-size index using a **hash function**.

Instead of searching through data sequentially, hashing allows direct access to storage locations, making operations extremely fast.

A hashing system consists of:

- **Key** → input data  
- **Hash function** → converts key into index  
- **Hash table** → storage structure  

The goal is to distribute keys evenly to minimize collisions and maximize efficiency.

---

## 2. Visual / Example

Keys to insert:

12, 22, 32

Simple hash function:

index = key % 10

Mapping:

12 → 2
22 → 2
32 → 2


This creates a **collision**, where multiple keys map to the same index.

Collision handling strategies:

Index 2 → [12 → 22 → 32]


This chaining ensures all values are stored safely.

---

## 3. Time & Space Complexity

| Operation | Average Case | Worst Case |
|----------|--------------|------------|
| Insert  | O(1)         | O(n)       |
| Search  | O(1)         | O(n)       |
| Delete  | O(1)         | O(n)       |

Space Complexity: **O(n)**

Worst case occurs when many collisions happen.

---

## 4. Python Code

### Simple Hash Table with Chaining

```python
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def search(self, key):
        index = self.hash_function(key)
        return key in self.table[index]

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")


# Example usage
ht = HashTable()

ht.insert(12)
ht.insert(22)
ht.insert(32)

ht.display()

print("Search 22:", ht.search(22))
print("Search 15:", ht.search(15))
```
### Output
```python

Index 0: []
Index 1: []
Index 2: [12, 22, 32]
Index 3: []
...
Search 22: True
Search 15: False
```
## 5. Common Interview Problems

- Implement a hash table from scratch

- First non-repeating character

- Two-sum problem

- Frequency counting

- Detect duplicates

These problems test fast lookup reasoning.

---

## 6. ML Connection

Hashing is heavily used in ML pipelines:

- Feature indexing

- Token hashing in NLP

- Deduplication of datasets

- Fast lookup during preprocessing

- Large-scale data storage

Many ML frameworks rely on hashing for efficient data access.

---

## 7. Practice Tasks

1. Implement open addressing collision handling

2. Build a dynamic resizing hash table

3. Count word frequencies using hashing

4. Detect duplicates in large datasets

5. Compare hashing vs linear search performance
---

**Author:**  
Hamna Munir

