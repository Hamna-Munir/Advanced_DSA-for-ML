# Knapsack Problem

## 1. Concept Explanation
The **Knapsack Problem** is a classic **optimization problem** in computer science and dynamic programming.

The goal is to determine the **maximum value of items** that can be placed inside a knapsack without exceeding its weight capacity.

Each item has:
- a **weight**
- a **value**

The objective is to **maximize the total value while keeping the total weight within the capacity limit**.

In the **0/1 Knapsack Problem**, each item can either be:
- **included (1)**
- **excluded (0)**

We cannot take fractions of items.

Dynamic Programming is used because the problem contains:
- **Overlapping subproblems**
- **Optimal substructure**

---

## 2. Visual / Example

Example:

Knapsack capacity = **5**

Items:

| Item | Weight | Value |
|-----|--------|-------|
| A | 2 | 3 |
| B | 3 | 4 |
| C | 4 | 5 |
| D | 5 | 6 |

Possible choices:

- A + B → Weight = 5, Value = **7**
- C → Weight = 4, Value = **5**
- D → Weight = 5, Value = **6**

Best choice:

A + B

Maximum value = **7**

Dynamic programming builds a **table of optimal values** for smaller capacities and items.

---

## 3. Time & Space Complexity

For **n items** and capacity **W**:

- Time Complexity: **O(n × W)**
- Space Complexity: **O(n × W)**

Optimized versions can reduce space complexity to **O(W)**.

---

## 4. Python Code

### 0/1 Knapsack Using Dynamic Programming

```python
def knapsack(values, weights, capacity):

    n = len(values)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):

        for w in range(1, capacity + 1):

            if weights[i-1] <= w:

                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],
                    dp[i-1][w]
                )

            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]


values = [3, 4, 5, 6]
weights = [2, 3, 4, 5]
capacity = 5

print(knapsack(values, weights, capacity))
```
### Output
```python
7
```
---

## 5. Common Interview Problems

- 0/1 Knapsack

- Fractional Knapsack

- Subset Sum Problem

- Partition Equal Subset Sum

- Target Sum Problem

These problems test dynamic programming optimization strategies.

---

## 6. ML Connection

Knapsack-style optimization appears in several machine learning and AI scenarios:

- Resource allocation in distributed systems

- Feature selection under constraints

- Budget optimization in model training

- Reinforcement learning reward maximization

- Scheduling and planning algorithms

Understanding the knapsack problem improves reasoning about constraint-based optimization.

---

## 7. Practice Tasks

1. Implement Knapsack using recursion

2. Optimize the DP solution to O(W) space

3. Solve Subset Sum Problem

4. Implement Fractional Knapsack using Greedy approach

5. Trace the DP table manually for small inputs

These exercises strengthen dynamic programming problem-solving skills.

---

**Author:**  
Hamna Munir
