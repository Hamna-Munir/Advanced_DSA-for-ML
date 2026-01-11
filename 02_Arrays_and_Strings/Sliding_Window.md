# Sliding Window Technique

## 1. Concept Explanation (Simple English)
The Sliding Window technique is used to **process a subset (window) of elements** in an array or string while moving the window forward step by step.

Instead of recalculating values repeatedly, the window updates efficiently, making this technique ideal for **subarray and substring problems**.

---

## 2. Visual / Example

Consider an array and a window size of 3:

[2, 4, 6, 8, 10]
└───────┘
window


As the window slides:
- One element enters the window
- One element exits the window

This avoids unnecessary recomputation.

---

## 3. Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(k) depending on the problem

Sliding Window optimizes problems that would otherwise take **O(n²)** time.

---

## 4. Python Code

```python
# Maximum sum of a subarray of size k

def max_subarray_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

numbers = [2, 1, 5, 1, 3, 2]
print(max_subarray_sum(numbers, 3))

```
---

## 5. Common Interview Problems

Common Sliding Window problems include:

- Maximum sum subarray of size k

- Longest substring without repeating characters

- Minimum window substring

- Maximum number of vowels in a substring

- Average of subarrays

These problems test optimization and window management skills.

---

## 6. ML Connection

Sliding Window is widely used in Machine Learning:

- Time-series forecasting

- Signal processing

- Text chunking in NLP

- Feature extraction from sequential data

Many ML models rely on window-based data representation.

---

## 7. Practice Tasks

1. Find the average of all subarrays of size k

2. Find the longest substring without repeating characters

3. Compute rolling averages for time-series data

4. Detect anomalies using window-based statistics

5. Convert a brute-force solution into a sliding window solution

---

**Author:**  
Hamna Munir


