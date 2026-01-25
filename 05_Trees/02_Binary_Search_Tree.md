# Binary Search Tree

## 1. Concept Explanation 
A Binary Search Tree (BST) is a special type of binary tree that follows an **ordering rule**:

For every node:
- All values in the **left subtree are smaller**
- All values in the **right subtree are greater**

This ordering allows:
- Fast searching  
- Efficient insertion and deletion  
- Sorted data traversal using inorder traversal  

---

## 2. Visual / Example
```python
    50
   /  \
 30    70
/ \    / \

```

20 40 60 80


BST property:
- Left child < Parent  
- Right child > Parent  

Inorder traversal of a BST always gives **sorted order**.

---

## 3. Time & Space Complexity

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Search    | O(log n)     | O(n)       |
| Insert    | O(log n)     | O(n)       |
| Delete    | O(log n)     | O(n)       |
| Traversal | O(n)         | O(n)       |

Worst case happens when the tree becomes **skewed**.

**Space Complexity:**  
- O(n) for storing nodes  
- O(h) recursion stack, where `h` is tree height  

---

## 4. Python Code

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)


def search(root, key):
    if not root or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)


# Example usage
root = None
values = [50, 30, 70, 20, 40, 60, 80]

for v in values:
    root = insert(root, v)

print("Inorder Traversal (Sorted Order):")
inorder_traversal(root)

found = search(root, 60)
print("\nSearch for 60:", "Found" if found else "Not Found")
```
### Output

```python
Inorder Traversal (Sorted Order):
20 30 40 50 60 70 80

Search for 60: Found
```
---

## 5. Common Interview Problems

Frequently asked BST problems include:

- Validate a binary search tree

- Find lowest common ancestor (LCA)

- Delete a node in BST

- Kth smallest / largest element

- Convert sorted array to BST

- Check if two BSTs are identical

These problems test ordering logic, recursion, and tree restructuring.

---

## 6. ML Connection

 Binary Search Trees are used in:

- Efficient indexing of training data

- Nearest neighbor search structures

- Feature selection and ranking

- Symbolic regression and expression trees

- Accelerating search operations in large datasets

BST concepts are the foundation for balanced trees and ML indexing systems.

---

## 7. Practice Tasks

1. Implement deletion in a BST

2. Find minimum and maximum value

3. Validate if a tree is a BST

4. Find the successor and predecessor

5. Build a balanced BST from a sorted array

---

**Author:**  
Hamna Munir
