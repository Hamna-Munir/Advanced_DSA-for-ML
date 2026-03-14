# Medium Practice Problems

## Overview
This section contains **intermediate-level problems** that require a deeper understanding of **Data Structures and Algorithms (DSA)**.

These problems often involve combining multiple concepts such as arrays, hash maps, binary search, trees, and graph traversal. Each problem includes a **Python implementation and expected output** to demonstrate how the solution works.

---

## 1. Longest Substring Without Repeating Characters

### Problem
Given a string, find the length of the **longest substring without repeating characters**.

Example:

Input

"abcabcbb"


Output

3


Explanation: The longest substring without repeating characters is **"abc"**.

### Python Code

```python
def longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


text = "abcabcbb"

print(longest_substring(text))
```
### Output
```python
3
```

## 2. Binary Search
### Problem

Given a sorted array, find the index of a target value using binary search.

Example:

Input

nums = [1,3,5,7,9]
target = 7

Output

3

### Python Code
```python
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


nums = [1,3,5,7,9]
target = 7

print(binary_search(nums, target))
```
### Output

```python
3
```
## 3. Level Order Traversal of Binary Tree
### Problem

Given a binary tree, return its level order traversal (breadth-first traversal).

Example Tree

      3
     / \
    9  20
       / \
      15  7

Output

[[3],[9,20],[15,7]]

### Python Code
```python
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.value)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(level_order(root))
```
### Output
```python
[[3], [9, 20], [15, 7]]
```

## 4. Detect Cycle in Linked List
### Problem

Determine if a linked list contains a cycle.

### Python Code
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Create linked list
head = Node(1)
second = Node(2)
third = Node(3)

head.next = second
second.next = third
third.next = second  # cycle

print(has_cycle(head))
```
### Output
```python
True
```
## 5. Top K Frequent Elements
### Problem

Given an integer array, return the k most frequent elements.

Example:

Input

nums = [1,1,1,2,2,3]
k = 2

Output

[1,2]

### Python Code
```python
from collections import Counter

def top_k_frequent(nums, k):
    freq = Counter(nums)
    return [num for num, _ in freq.most_common(k)]


nums = [1,1,1,2,2,3]
k = 2

print(top_k_frequent(nums, k))
```
### Output
```python
[1, 2]
```
### Goal

These problems strengthen understanding of efficient algorithms, data structures, and problem-solving strategies required for technical interviews and real-world software development.

---

**Author:**  
Hamna Munir
