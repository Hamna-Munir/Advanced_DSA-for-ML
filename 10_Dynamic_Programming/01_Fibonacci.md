# Fibonacci

## 1. Concept Explanation
The **Fibonacci sequence** is a well-known mathematical sequence where each number is the **sum of the two previous numbers**.

The sequence begins as:

0, 1, 1, 2, 3, 5, 8, 13, 21 ...

Mathematically:

F(0) = 0  
F(1) = 1  
F(n) = F(n − 1) + F(n − 2)

The Fibonacci problem is often used to demonstrate **Dynamic Programming** because the recursive solution repeatedly calculates the same values.

Dynamic Programming improves efficiency by **storing previously computed results** and reusing them instead of recalculating them.

---

## 2. Visual / Example

Example: Fibonacci of 6

F(6)

= F(5) + F(4)

= (F(4) + F(3)) + (F(3) + F(2))

= ((F(3) + F(2)) + (F(2) + F(1))) + ((F(2) + F(1)) + F(0))

Result:

F(6) = 8

Recursive tree visualization:

F(6)

├ F(5)

│ ├ F(4)

│ │ ├ F(3)

│ │ └ F(2)

│ └ F(3)

└ F(4)

Notice that **F(3)** and **F(2)** are calculated multiple times.  
Dynamic Programming eliminates these repeated calculations.

---

## 3. Time & Space Complexity

Recursive Fibonacci is inefficient because it recomputes the same subproblems.

- Recursive Time Complexity: **O(2ⁿ)**
- Recursive Space Complexity: **O(n)**

Using Dynamic Programming:

- DP Time Complexity: **O(n)**
- DP Space Complexity: **O(n)**

Dynamic Programming significantly improves performance.

---

## 4. Python Code

### Fibonacci Using Recursion

```python
def fibonacci(n):
    if n <= 1:   # base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
```
### Output
```python
8
```

### Fibonacci Using Dynamic Programming (Memoization)
```python
def fibonacci_dp(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci_dp(n-1, memo) + fibonacci_dp(n-2, memo)

    return memo[n]


print(fibonacci_dp(6))
```
### Output
```python
8
```
### Fibonacci Using Tabulation (Bottom-Up)
```python
def fibonacci_tab(n):

    if n <= 1:
        return n

    dp = [0] * (n + 1)

    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print(fibonacci_tab(6))
```
### Output
```python
8
```
---

## 5. Common Interview Problems

- Fibonacci sequence variations

- Climbing stairs problem

- Dynamic programming optimization

- Minimum cost climbing stairs

- Tribonacci sequence

These problems test understanding of recursion and dynamic programming.

---

## 6. ML Connection

Fibonacci-style recurrence relations appear in many computing and ML systems:

- Reinforcement learning value updates

- Dynamic programming optimization

- Sequence modeling

- Algorithm efficiency analysis

- Recursive problem decomposition

 These concepts strengthen the understanding of state transitions and iterative optimization.

 ---

## 7. Practice Tasks

1. Print Fibonacci series up to n

2. Implement Fibonacci using iteration

3. Optimize Fibonacci using constant space

4. Compare recursion vs dynamic programming runtime

5. Trace recursive calls manually

Practicing these problems builds intuition for dynamic programming.

---

**Author:**  
Hamna Munir
