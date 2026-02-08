# Recursion

## 1. Concept Explanation (Simple English)
**Recursion** is a problem-solving technique where a function calls itself to solve smaller instances of the same problem.

A recursive function has two essential parts:

- **Base Case** — stops the recursion
- **Recursive Case** — reduces the problem into a smaller version

The function continues calling itself until the base case is reached.

Recursion is especially useful for problems that naturally divide into subproblems, such as tree traversal, mathematical sequences, and search algorithms.

---

## 2. Visual / Example

Example: Factorial calculation

Factorial of 4:

4! = 4 × 3 × 2 × 1

Recursive breakdown:

factorial(4)

= 4 × factorial(3)

= 4 × 3 × factorial(2)

= 4 × 3 × 2 × factorial(1)

= 4 × 3 × 2 × 1

= 24


Each recursive call waits for the smaller problem to complete.

Call stack visualization:

factorial(4)

└ factorial(3)

└ factorial(2)

└ factorial(1)


---

## 3. Time & Space Complexity

Time complexity depends on how many recursive calls occur.

Factorial example:

- Time Complexity: **O(n)**
- Space Complexity: **O(n)** (due to call stack)

Recursive solutions use stack memory for each function call.

---

## 4. Python Code

### Factorial Using Recursion

```python
def factorial(n):
    if n == 1:   # base case
        return 1
    return n * factorial(n - 1)

print(factorial(4))
```
### Output
```python
24

```
### Fibonacci Using Recursion
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
```
### Output
```python
8

```
## 5. Common Interview Problems

- Factorial and Fibonacci

- Recursive binary search

- Tree traversal

- Tower of Hanoi

- Permutations and combinations

These problems test recursive thinking and stack behavior.

---

## 6. ML Connection

Recursion appears in machine learning and AI workflows:

- Tree-based model traversal

- Divide-and-conquer algorithms

- Hierarchical data processing

- Recursive feature decomposition

- Graph exploration techniques

Understanding recursion improves reasoning about algorithm structure.

---

## 7. Practice Tasks

1. Write recursive sum of an array

2. Implement recursive binary search

3. Reverse a string recursively

4. Compute power using recursion

5. Trace recursive calls manually

Practice strengthens intuition and debugging skills.

---

**Author:**  
Hamna Munir




