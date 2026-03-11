# Greedy Algorithms

## 1. Concept Explanation
A **Greedy Algorithm** is a problem-solving strategy that makes the **best possible choice at each step** with the hope of finding the global optimal solution.

Instead of considering all possible solutions, greedy algorithms select the **locally optimal choice** and move forward without revisiting previous decisions.

Greedy algorithms are efficient and simple, but they only work correctly for problems that have:

- **Greedy Choice Property** — a local optimal choice leads to a global optimal solution  
- **Optimal Substructure** — the optimal solution can be built from optimal subsolutions  

When these conditions are satisfied, greedy algorithms can produce optimal results with very good performance.

---

## 2. Visual / Example

Example: **Coin Change Problem**

Coins available:

1, 5, 10, 25

Target amount:

30


Greedy approach:

Step 1 → Choose largest coin ≤ 30 → **25**  
Remaining → 30 − 25 = **5**

Step 2 → Choose largest coin ≤ 5 → **5**

Solution:

25 + 5 = 30

Number of coins used:

2 coins


The greedy strategy chooses the **largest possible coin at each step**.

---

## 3. Time & Space Complexity

Greedy algorithms are typically very efficient.

For many greedy problems:

- Time Complexity: **O(n log n)** (if sorting is required)
- Space Complexity: **O(1)** or **O(n)**

Efficiency depends on the specific problem and implementation.

---

## 4. Python Code

### Activity Selection Problem (Greedy)

```python
def activity_selection(start, finish):

    n = len(start)
    activities = []

    i = 0
    activities.append(i)

    for j in range(1, n):

        if start[j] >= finish[i]:
            activities.append(j)
            i = j

    return activities


start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

selected = activity_selection(start, finish)

print("Selected activity indices:", selected)
```

### Output
```python
Selected activity indices: [0, 1, 3, 4]
```
### Coin Change (Greedy)
```python
def coin_change(coins, amount):

    coins.sort(reverse=True)
    result = []

    for coin in coins:

        while amount >= coin:
            amount -= coin
            result.append(coin)

    return result


coins = [1, 5, 10, 25]
amount = 30

print("Coins used:", coin_change(coins, amount))
Output
Coins used: [25, 5]
```
---

## 5. Common Interview Problems

- Activity Selection Problem

- Fractional Knapsack

- Coin Change (Greedy version)

- Minimum Number of Platforms

- Huffman Coding

These problems test understanding of local optimization strategies.

---

## 6. ML Connection

Greedy strategies appear in several machine learning and AI algorithms:

- Decision tree splitting (greedy feature selection)

- Feature selection techniques

- Heuristic search algorithms

- Scheduling tasks in distributed ML systems

- Optimization in reinforcement learning

Greedy thinking helps design fast approximation algorithms for large datasets.

---

## 7. Practice Tasks

1. Implement Fractional Knapsack using Greedy

2. Solve Minimum Number of Platforms Problem

3. Implement Huffman Coding

4. Compare Greedy vs Dynamic Programming solutions

5. Trace greedy decisions step-by-step

---

**Author:**  
Hamna Munir
