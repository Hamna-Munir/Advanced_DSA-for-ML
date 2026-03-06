# Heap Sort

## 1. Concept Explanation 

**Heap Sort** is a comparison-based sorting algorithm that uses a **Heap data structure** to sort elements efficiently.

A **Heap** is a special type of binary tree that satisfies the **heap property**. In a **Max Heap**, the parent node is always greater than or equal to its children.

Heap Sort works in two main steps:

1. Build a **Max Heap** from the input array.
2. Repeatedly extract the **maximum element** from the heap and place it at the end of the array.

After each extraction, the heap size is reduced and the heap property is restored. This process continues until all elements are sorted.

Heap Sort is efficient and guarantees good performance even in the worst case.

---

## 2. Visual / Example

Example array:

[4, 10, 3, 5, 1]

### Step 1 — Build Max Heap

```python
    10
   /  \
  5    3
 / \
4   1
```
### Step 2 — Extract Maximum (10)

[10, 5, 4, 3, 1]

### Step 3 — Repeat until sorted

Final sorted array:

[1, 3, 4, 5, 10]


---

## 3. Time & Space Complexity

| Case | Time Complexity |
|-----|----------------|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n log n) |

Space Complexity:

O(1)


Heap Sort is an **in-place sorting algorithm**, meaning it does not require additional memory.

---

## 4. Python Code

```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


data = [4, 10, 3, 5, 1]
sorted_data = heap_sort(data)

print("Sorted Array:", sorted_data)
```
### Output:
```python
Sorted Array: [1, 3, 4, 5, 10]
```
---

## 5. Common Interview Problems

Typical questions related to Heap Sort include:

- Implement Heap Sort from scratch

- Build a Max Heap

- Convert an array into a heap

- Find the k-th largest element using a heap

- Implement a priority queue using heaps

These problems help evaluate understanding of tree-based data structures.

---

## 6. ML Connection

Heap-based algorithms appear in several machine learning and data engineering tasks:

- Priority queues in search algorithms

- Efficient ranking of predictions

- Top-K selection in recommendation systems

- Data stream processing

- Task scheduling in ML pipelines

Heaps are widely used when efficient retrieval of minimum or maximum elements is required.

---

## 7. Practice Tasks

1. Implement Heap Sort without using helper functions

2. Visualize heap construction step-by-step

3. Modify Heap Sort to build a Min Heap

4. Find the k-th largest element using a heap

5. Compare Heap Sort performance with Quick Sort and Merge Sort

Practicing these exercises improves understanding of heap-based algorithms.

---

**Author:**  
Hamna Munir
