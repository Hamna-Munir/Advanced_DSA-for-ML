# Singly Linked List

## 1. Concept Explanation 
A Singly Linked List is a **linear data structure** where each element (node) contains:
- Data
- A reference (pointer) to the next node in the list

Unlike arrays, elements are **not stored in contiguous memory locations**. Each node points only to the next node, making traversal one-directional.

---

## 2. Visual / Example

[Data | Next] → [Data | Next] → [Data | Next] → NULL


Each node:
- Stores a value
- Knows where the next node is
- The last node points to `NULL`

This structure allows dynamic memory usage.

---

## 3. Time & Space Complexity

| Operation          | Time Complexity |
|--------------------|-----------------|
| Access (by index)  | O(n)            |
| Insertion (head)   | O(1)            |
| Insertion (tail)   | O(n)            |
| Deletion           | O(n)            |
| Traversal          | O(n)            |

**Space Complexity:**  
- O(n) for storing `n` nodes

Understanding these costs is critical for choosing the right data structure.

---

## 4. Python Code

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("NULL")


# Example usage
ll = SinglyLinkedList()
ll.insert_at_head(3)
ll.insert_at_head(2)
ll.insert_at_head(1)
ll.traverse()

```
---

## 5. Common Interview Problems

Frequently asked problems include:

- Reverse a linked list

- Detect a cycle (Floyd’s algorithm)

- Find the middle of a linked list

- Remove the nth node from the end

- Merge two sorted linked lists

These problems test pointer manipulation and logical precision.

---

## 6. ML Connection

Singly linked lists help build intuition for:

- Pointer-based data traversal

- Dynamic memory handling

- Graph and tree data structures

- Sequential data processing

While not used directly in ML libraries, this understanding strengthens algorithmic and systems-level thinking.

---

## 7. Practice Tasks

1. Insert nodes at the tail of a linked list

2. Delete a node by value

3. Reverse a linked list iteratively

4. Find the length of a linked list

5. Detect a cycle in a linked list

---

**Author:**  
Hamna Munir
