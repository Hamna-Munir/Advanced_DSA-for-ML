# AVL Tree Implementation

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    return node.height if node else 0


def balance(node):
    return height(node.left) - height(node.right) if node else 0


def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x


def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


def insert(root, key):
    if not root:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.height = 1 + max(height(root.left), height(root.right))
    bf = balance(root)

    # Rotations
    if bf > 1 and key < root.left.key:
        return right_rotate(root)

    if bf < -1 and key > root.right.key:
        return left_rotate(root)

    if bf > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    if bf < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


# Example
values = [10, 20, 30, 40, 50, 25]
root = None

for v in values:
    root = insert(root, v)

print("Inorder Traversal of Balanced AVL Tree:")
inorder(root)

# Output
# Inorder Traversal of Balanced AVL Tree:
# 10 20 25 30 40 50
