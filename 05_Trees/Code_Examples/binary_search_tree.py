# Binary Search Tree Implementation

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


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


def search(root, key):
    if not root or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)


# Example Usage
values = [50, 30, 70, 20, 40, 60, 80]
root = None

for v in values:
    root = insert(root, v)

print("Inorder Traversal (Sorted Order):")
inorder(root)

print("\nSearch 60:", "Found" if search(root, 60) else "Not Found")
print("Search 25:", "Found" if search(root, 25) else "Not Found")

# Output
# Inorder Traversal (Sorted Order):
# 20 30 40 50 60 70 80
# Search 60: Found
# Search 25: Not Found
