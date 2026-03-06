# Bubble Sort

## 1. Concept Explanation 

**Bubble Sort** is one of the simplest sorting algorithms. It works by repeatedly comparing **adjacent elements** in a list and swapping them if they are in the wrong order.

During each pass through the list, the largest unsorted element "bubbles up" to its correct position at the end of the array. This process continues until the entire list becomes sorted.

Although Bubble Sort is easy to understand and implement, it is **not efficient for large datasets** and is mainly used for educational purposes.

---

## 2. Visual / Example

Example array:

[5, 1, 4, 2, 8]


Pass 1:

5 > 1 → swap → [1,5,4,2,8]

5 > 4 → swap → [1,4,5,2,8]

5 > 2 → swap → [1,4,2,5,8]

5 < 8 → no swap


Pass 2:

[1,4,2,5,8]

4 > 2 → swap → [1,2,4,5,8]


Final sorted array:

[1,2,4,5,8]


---

## 3. Time & Space Complexity

| Case | Time Complexity |
|-----|----------------|
| Best Case | O(n) |
| Average Case | O(n²) |
| Worst Case | O(n²) |

Space Complexity:

O(1)


Bubble Sort is an **in-place sorting algorithm**, meaning it does not require additional memory.

---

## 4. Python Code

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


data = [5, 1, 4, 2, 8]
sorted_data = bubble_sort(data)

print("Sorted Array:", sorted_data)
```
### Output:

```python
Sorted Array: [1, 2, 4, 5, 8]

```

## 5. Common Interview Problems

Typical questions related to Bubble Sort include:

- Implement Bubble Sort

- Optimize Bubble Sort using a swap flag

- Compare Bubble Sort with other sorting algorithms

- Analyze Bubble Sort time complexity

These questions test understanding of basic sorting mechanics.

---

## 6. ML Connection

While Bubble Sort itself is rarely used in production ML systems, the concept of sorting is fundamental in machine learning workflows:

- Sorting datasets before preprocessing

- Ranking predictions or probabilities

- Organizing features during data transformation

- Understanding algorithm efficiency

More efficient sorting algorithms such as Quick Sort and Merge Sort are commonly used in data processing pipelines.

---

## 7. Practice Tasks

1. Implement Bubble Sort from scratch

2. Modify Bubble Sort to detect already sorted arrays

3. Count the number of swaps performed during sorting

4. Compare Bubble Sort with Python's built-in sorted() function

5. Test Bubble Sort on different dataset sizes

Practicing these tasks helps strengthen algorithmic thinking and performance analysis.

---

**Author:**  
Hamna Munir
