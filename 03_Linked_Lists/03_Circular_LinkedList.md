# Circular Linked List

## 1. Concept Explanation
A Circular Linked List is a variation of a linked list where the **last node points back to the first node**, instead of pointing to `NULL`.

This creates a circular structure where traversal can start at any node and continue indefinitely until the starting node is reached again.

Circular linked lists can be **singly circular** or **doubly circular**, but the core idea remains the same:  
there is **no NULL at the end**.

---

## 2. Visual / Example

  ┌───────────────┐
                  |
  ▼               

[ Data | Next ] → [ Data | Next ] → [ Data | Next ]

▲___________________________________________│


The last node’s `next` pointer links back to the head node.

---

## 3. Time & Space Complexity

| Operation             | Time Complexity |
|-----------------------|-----------------|
| Traversal             | O(n)            |
| Insertion (head)      | O(1)            |
| Insertion (tail)      | O(1)            |
| Deletion              | O(n)            |
| Search                | O(n)            |

**Space Complexity:**  
- O(n) for storing `n` nodes  
- No extra memory besides pointers

---

## 4. Python Code

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def traverse(self):
        if not self.head:
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(Back to Head)")


# Example usage
cll = CircularLinkedList()
cll.insert(1)
cll.insert(2)
cll.insert(3)
cll.traverse()
```
---

### Output
```python
1 -> 2 -> 3 -> (Back to Head)
```
---

## 5. Common Interview Problems

Frequently asked problems include:

- Detect a loop in a linked list

- Split a circular linked list into two halves

- Josephus problem

- Insert and delete nodes in a circular list

- Check if a linked list is circular

These problems test understanding of loop termination and pointer logic.

---

## 6. ML Connection

Circular linked lists are useful in:

- Streaming data processing

- Repetitive training cycles

- Round-robin scheduling of tasks

- Memory-efficient buffering systems

They help ML engineers understand continuous data flow and iterative processing.

---

## 7. Practice Tasks

1. Insert a node at the beginning

2. Delete a specific value

3. Count the number of nodes

4. Split the list into two circular lists

5. Implement the Josephus problem using a circular linked list

---

**Author:**  
Hamna Munir
