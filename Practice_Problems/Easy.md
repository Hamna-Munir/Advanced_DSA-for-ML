# Easy Practice Problems

## Overview
This section contains **beginner-friendly problems** designed to strengthen fundamental understanding of **Data Structures and Algorithms (DSA)**.

These problems focus on basic programming logic, arrays, strings, and simple algorithmic patterns. Each problem includes a **Python implementation and expected output** to help learners understand how solutions work.

---

## 1. Two Sum

### Problem
Given an array of integers and a target value, return the indices of the two numbers that add up to the target.

Example:

Input

nums = [2, 7, 11, 15]
target = 9


Output

[0, 1]


### Python Code

```python
def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))
```
### Output
```python
[0, 1]
```
## 2. Reverse a String
### Problem

Write a function that reverses a string.

Example:

Input

"hello"

Output

"olleh"

### Python Code
```python
def reverse_string(s):
    return s[::-1]


text = "hello"

print(reverse_string(text))
```
### Output
```python
olleh
```
## 3. Find Maximum Element in Array
### Problem

Given an array of numbers, find the largest element.

Example:

Input

[3, 7, 2, 9, 4]

Output

9

### Python Code
```python
def find_max(arr):
    maximum = arr[0]

    for num in arr:
        if num > maximum:
            maximum = num

    return maximum


numbers = [3, 7, 2, 9, 4]

print(find_max(numbers))
```
### Output
```python
9
```
## 4. Palindrome Check
### Problem

Check whether a string is a palindrome.

Example:

Input

"madam"

Output

True

### Python Code
```python
def is_palindrome(text):
    return text == text[::-1]


word = "madam"

print(is_palindrome(word))
```
### Output
```python
True
```
## 5. Count Even Numbers
### Problem

Given an array of integers, count how many numbers are even.

Example:

Input

[1, 2, 3, 4, 5, 6]

Output

3

### Python Code
```python
def count_even(numbers):
    count = 0

    for num in numbers:
        if num % 2 == 0:
            count += 1

    return count


nums = [1, 2, 3, 4, 5, 6]

print(count_even(nums))
```
### Output
```python
3
```
### Goal

These problems help build strong foundational programming skills and introduce basic algorithmic thinking used in more advanced data structure problems.

---

**Author:**  
Hamna Munir
