# Binary Tree

## 1. Concept Explanation 
A Binary Tree is a hierarchical data structure where:
- Each node has **at most two children**  
- These children are referred to as the **left child** and the **right child**

There is no ordering rule in a basic binary tree.  
Binary trees are mainly used to represent hierarchical data and to support recursive algorithms.

---

## 2. Visual / Example

```python
    1
   / \
  2   3
 / \
4   5
```

Each node:
- Stores a value  
- Has references to its left and right child  

---

## 3. Time & Space Complexity

| Operation        | Time Complexity |
|------------------|-----------------|
| Access / Search  | O(n)            |
| Insertion        | O(n)            |
| Deletion         | O(n)            |
| Traversal        | O(n)            |

**Space Complexity:**  
- O(n) for storing `n` nodes  
- O(h) recursion stack during traversal, where `h` is tree height  

---

## 4. Python Code

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)


def preorder_traversal(root):
    if root:
        print(root.data, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=" ")


# Example tree creation
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder Traversal:")
inorder_traversal(root)

print("\nPreorder Traversal:")
preorder_traversal(root)

print("\nPostorder Traversal:")
postorder_traversal(root)
```
### Output

```python
Inorder Traversal:
4 2 5 1 3

Preorder Traversal:
1 2 4 5 3

Postorder Traversal:
4 5 2 3 1
```
---

## 5. Common Interview Problems

Common binary tree problems include:

- Tree traversals (inorder, preorder, postorder)

- Height and depth of a tree

- Count number of nodes and leaves

- Mirror a binary tree

- Check if a tree is balanced

- Level order traversal

These problems test recursion, traversal logic, and tree understanding.

---

## 6. ML Connection

Binary trees are fundamental in:

- Decision Trees and ensemble models

- Hierarchical clustering

- Feature selection processes

- Expression parsing in symbolic ML systems

- Model interpretability

Understanding binary trees helps ML engineers design interpretable models and efficient hierarchical representations.

---

## 7. Practice Tasks

1. Implement level-order traversal using a queue

2. Find the height of a binary tree

3. Count leaf nodes

4. Check if a tree is symmetric

5. Convert a binary tree into its mirror

---

**Author:**  
Hamna Munir
