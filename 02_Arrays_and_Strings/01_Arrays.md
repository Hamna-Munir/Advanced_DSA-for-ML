# Arrays

## 1. Concept Explanation 
An array is a **collection of elements stored in contiguous memory locations**.  
Each element can be accessed using an index, which makes arrays fast and efficient for reading data.

Arrays are one of the most commonly used data structures and form the backbone of many algorithms and Machine Learning workflows.

---

## 2. Visual / Example

Imagine an array as a row of boxes:

Index:   0   1   2   3  
Values: [4, 7, 1, 9]

- Each box holds one value
- Accessing any element by index takes constant time

Arrays allow structured and predictable data storage.

---

## 3. Time & Space Complexity

| Operation        | Time Complexity |
|------------------|-----------------|
| Access by index  | O(1)            |
| Traversal        | O(n)            |
| Insertion        | O(n)            |
| Deletion         | O(n)            |

**Space Complexity:**  
- O(n), where `n` is the number of elements stored

Understanding these costs is critical when working with large datasets.

---

## 4. Python Code

```python
# Creating an array (list in Python)
arr = [10, 20, 30, 40]

# Accessing elements
print(arr[0])
print(arr[2])

# Traversing the array
for element in arr:
    print(element)

# Updating an element
arr[1] = 25
print(arr)
```
---

## 5. Common Interview Problems

Common array-based interview problems include:

- Find the maximum or minimum element

- Reverse an array

- Rotate an array

- Find duplicates

- Subarray sum problems

Interviewers expect candidates to understand both brute force and optimized solutions.

---

## 6. ML Connection

Arrays are fundamental in Machine Learning:

- Feature vectors are stored as arrays

- Images are represented as multi-dimensional arrays

- NumPy arrays power most ML frameworks

- Batch data is processed as arrays

Efficient array operations directly impact training speed and memory usage.

---

## 7. Practice Tasks

1. Write a function to find the maximum element in an array

2. Reverse an array without using built-in methods

3. Calculate the sum of all elements

4. Count the frequency of elements

5. Find the index of a given element

---

**Author:**  
Hamna Munir
