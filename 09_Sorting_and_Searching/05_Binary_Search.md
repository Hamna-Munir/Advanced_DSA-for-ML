# Binary Search

## 1. Concept Explanation 

**Binary Search** is an efficient searching algorithm used to find a target value in a **sorted array**.

Instead of checking each element one by one, Binary Search repeatedly divides the search space in half. It compares the target value with the **middle element** of the array.

The algorithm works as follows:

1. Find the middle element of the array.
2. If the middle element equals the target, the search is complete.
3. If the target is smaller than the middle element, search the **left half**.
4. If the target is greater than the middle element, search the **right half**.
5. Repeat this process until the element is found or the search space becomes empty.

Binary Search is much faster than linear search for large sorted datasets.

---

## 2. Visual / Example

Example array:

[1, 3, 5, 7, 9, 11, 13]


Target = **7**

Step 1:

Middle element = 7


Since the middle element equals the target, the search stops.

Another example: Target = **11**

Step 1:

Middle = 7
11 > 7 → search right half

Step 2:

[9, 11, 13]
Middle = 11 → Found


---

## 3. Time & Space Complexity

| Case | Time Complexity |
|-----|----------------|
| Best Case | O(1) |
| Average Case | O(log n) |
| Worst Case | O(log n) |

### Space Complexity (Iterative):

O(1)

### Space Complexity (Recursive):

O(log n)


Binary Search is extremely efficient for large sorted datasets.

---

## 4. Python Code

### Iterative Binary Search

```python
def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


data = [1, 3, 5, 7, 9, 11, 13]
target = 11

result = binary_search(data, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

```
### Output:

```python
Element found at index: 5

```
---

## 5. Common Interview Problems

Common interview questions related to Binary Search include:

- Implement Binary Search (iterative and recursive)

- Find the first or last occurrence of an element

- Search in a rotated sorted array

- Find the square root using Binary Search

- Find peak elements in an array

These problems test understanding of divide-and-conquer search techniques.

---

## 6. ML Connection

Binary Search concepts appear in many machine learning and data systems:

- Efficient lookup in sorted datasets

- Hyperparameter tuning ranges

- Searching thresholds in classification problems

- Optimizing search spaces in algorithms

- Efficient indexing and retrieval

Many optimization techniques in ML rely on logarithmic search strategies similar to Binary Search.

---

## 7. Practice Tasks

1. Implement Binary Search recursively

2. Modify the algorithm to return the first occurrence of a target

3. Search an element in a rotated sorted array

4. Use Binary Search to find the square root of a number

5. Compare Binary Search with Linear Search on large datasets

Practicing these variations improves understanding of efficient searching techniques.

---

**Author:**  
Hamna Munir
