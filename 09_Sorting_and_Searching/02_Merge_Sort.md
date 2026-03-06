# Merge Sort

## 1. Concept Explanation 

**Merge Sort** is an efficient sorting algorithm based on the **Divide and Conquer** strategy.

The idea is simple:

1. Divide the array into two halves  
2. Recursively sort each half  
3. Merge the two sorted halves into a single sorted array

This process continues until the array is broken down into single elements. Single elements are already sorted, so they can be merged back together in sorted order.

Merge Sort is widely used because its performance remains consistent even for large datasets.

---

## 2. Visual / Example

### Example array:

[8, 3, 5, 2]


### Step 1 — Divide

[8, 3, 5, 2]

 /        \
[8, 3]  [5, 2]

### Step 2 — Divide again

[8] [3] [5] [2]


### Step 3 — Merge sorted pairs

[3, 8] [2, 5]


### Step 4 — Final merge

[2, 3, 5, 8]


---

## 3. Time & Space Complexity

| Case | Time Complexity |
|-----|----------------|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n log n) |

### Space Complexity:

O(n)


Merge Sort requires additional memory for temporary arrays during merging.

---

## 4. Python Code

```python
def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


data = [8, 3, 5, 2]
sorted_data = merge_sort(data)

print("Sorted Array:", sorted_data)
```
### Output:
```python
Sorted Array: [2, 3, 5, 8]
```
---

## 5. Common Interview Problems

Common questions related to Merge Sort include:

- Implement Merge Sort from scratch

- Merge two sorted arrays

- Count inversions in an array

- Sort a linked list using Merge Sort

- Understand divide and conquer strategy

These problems test understanding of recursion and algorithm design.

---

## 6. ML Connection

Merge Sort concepts appear in many data processing and machine learning systems:

- Efficient dataset sorting

- Large-scale distributed sorting

- External sorting for large files

- Data preprocessing pipelines

- Ranking predictions in ML models

Frameworks handling large datasets often use algorithms similar to Merge Sort.

---

## 7. Practice Tasks

1. Implement Merge Sort without using Python slicing

2. Trace Merge Sort step-by-step on a sample array

3. Modify Merge Sort to sort in descending order

4. Implement Merge Sort for linked lists

5. Compare performance with Quick Sort

Practicing these variations improves understanding of divide and conquer algorithms.

---

**Author:**  
Hamna Munir


