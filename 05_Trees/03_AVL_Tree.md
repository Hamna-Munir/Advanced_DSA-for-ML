# AVL Tree

## 1. Concept Explanation 
An **AVL Tree** is a **self-balancing Binary Search Tree** (BST).  
- Each node stores a key and maintains a **height** value.  
- For every node, the **balance factor** (height of left subtree − height of right subtree) must be **-1, 0, or +1**.  

If the tree becomes unbalanced after an insertion or deletion, **rotations** are applied to restore balance.  
This guarantees **O(log n)** search, insert, and delete operations in the worst case.

AVL Trees are widely used in **databases, indexing, and ML pipelines** where balanced search trees are required.

---

## 2. Visual / Example

Unbalanced tree after insertion:

```python


30
/
20
/
10
```

Balanced tree after right rotation:
```python

20

/
10 30
```

Rotation types used to maintain balance:
- **Left Rotation** (RR Case)  
- **Right Rotation** (LL Case)  
- **Left-Right Rotation** (LR Case)  
- **Right-Left Rotation** (RL Case)  

---

## 3. Time & Space Complexity

| Operation | Time Complexity |
|-----------|-----------------|
| Search    | O(log n)        |
| Insert    | O(log n)        |
| Delete    | O(log n)        |
| Traversal | O(n)            |

**Space Complexity:**  
- O(n) for storing nodes  
- O(log n) recursion stack for balanced operations  

AVL trees guarantee **worst-case logarithmic height**, unlike standard BSTs.

---

## 4. Python Code

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# Helper functions
def height(node):
    return node.height if node else 0

def get_balance(node):
    return height(node.left) - height(node.right) if node else 0

# Rotations
def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = max(height(y.left), height(y.right)) + 1
    x.height = max(height(x.left), height(x.right)) + 1
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = max(height(x.left), height(x.right)) + 1
    y.height = max(height(y.left), height(y.right)) + 1
    return y

# Insert function with balancing
def insert(root, key):
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    # Update height
    root.height = 1 + max(height(root.left), height(root.right))
    balance = get_balance(root)

    # LL Case
    if balance > 1 and key < root.left.key:
        return right_rotate(root)
    # RR Case
    if balance < -1 and key > root.right.key:
        return left_rotate(root)
    # LR Case
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    # RL Case
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

# Inorder traversal
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)

# Example usage
root = None
values = [10, 20, 30, 40, 50, 25]

for v in values:
    root = insert(root, v)

print("Inorder Traversal (Balanced AVL Tree):")
inorder_traversal(root)
```

### Output
```python

Inorder Traversal (Balanced AVL Tree):
10 20 25 30 40 50
```
---

## 5. Common Interview Problems

- Implement insertion in an AVL tree with rotations

- Delete a node in AVL and rebalance

- Find balance factor of each node

- Check if a tree is height balanced

- Convert an unbalanced BST into an AVL tree

These problems test recursion, rotation logic, and balancing principles.

---

## 6. ML Connection

AVL trees are critical in ML for:

- Indexing large datasets efficiently

- Nearest neighbor search optimization

- Maintaining balanced search structures in real-time pipelines

- Database operations for training data

- Symbolic ML and decision tree preprocessing

Balanced trees ensure consistent, high-performance data access in large-scale ML systems.

---

## 7. Practice Tasks

1. Implement deletion in an AVL tree

2. Print balance factor for every node

3. Convert a given BST to AVL

4. Count rotations performed during insertions

5. Implement iterative inorder traversal

---

**Author:**  
Hamna Munir


