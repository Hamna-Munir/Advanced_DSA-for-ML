# Quick Sort

## 1. Concept Explanation 

**Quick Sort** is one of the most efficient and widely used sorting algorithms. It also follows the **Divide and Conquer** strategy.

The algorithm works by selecting a **pivot element** from the array and partitioning the remaining elements into two groups:

- Elements **smaller than the pivot**
- Elements **greater than the pivot**

After partitioning, the same process is applied recursively to the left and right subarrays until the entire array becomes sorted.

Quick Sort is very fast in practice and is commonly used in many real-world systems.

---

## 2. Visual / Example

### Example array:

[10, 7, 8, 9, 1, 5]


Choose pivot = **5**

### Partition step:

[1] 5 [10, 7, 8, 9]

### Recursive sorting:

Left: [1]
Right: [10, 7, 8, 9]

### After sorting:

[1, 5, 7, 8, 9, 10]


---

## 3. Time & Space Complexity

| Case | Time Complexity |
|-----|----------------|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n²) |

Worst case occurs when the pivot is always the smallest or largest element.

### Space Complexity:

O(log n)


This comes from the recursion stack.

Quick Sort is an **in-place sorting algorithm**, meaning it does not require extra memory for another array.

---

## 4. Python Code

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []

    for num in arr[:-1]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    return quick_sort(left) + [pivot] + quick_sort(right)


data = [10, 7, 8, 9, 1, 5]
sorted_data = quick_sort(data)

print("Sorted Array:", sorted_data)
```
### Output:
```python
Sorted Array: [1, 5, 7, 8, 9, 10]
```
## 5. Common Interview Problems

Typical interview questions include:

- Implement Quick Sort

- Explain pivot selection strategies

- Partition an array around a pivot

- Find the k-th smallest element using Quick Select

- Compare Quick Sort with Merge Sort

These questions evaluate algorithm design and understanding of divide-and-conquer techniques.

---

## 6. ML Connection

Sorting algorithms like Quick Sort are important in machine learning and data engineering:

- Ranking predictions or probabilities

- Sorting datasets during preprocessing

- Efficient data indexing

- Nearest neighbor search algorithms

- Feature selection and ranking

Many ML libraries rely on optimized sorting operations internally.

---

## 7. Practice Tasks

1. Implement Quick Sort using different pivot strategies

2. Trace Quick Sort step-by-step on an example array

3. Modify the algorithm to sort in descending order

4. Implement Quick Select to find the k-th smallest element

5. Compare runtime with Merge Sort and Bubble Sort

These exercises help strengthen understanding of recursive sorting algorithms.

---

**Author:**  
Hamna Munir
