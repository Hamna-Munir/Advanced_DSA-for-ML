# Matrix Dynamic Programming

## 1. Concept Explanation
**Matrix Dynamic Programming** refers to solving problems on **2D grids or matrices** using dynamic programming techniques.

In these problems, we move through a grid while computing the **optimal value for each cell based on previously solved cells**.

Matrix DP is commonly used in problems involving:

- Grid traversal
- Minimum or maximum path problems
- Counting paths in a grid
- Game boards and map navigation

The idea is to build a **DP table** where each cell stores the best result for reaching that position.

This approach avoids recomputing values and significantly improves efficiency.

---

## 2. Visual / Example

Example problem: **Minimum Path Sum**

Given a grid:

1 3 1

1 5 1

4 2 1


Goal: Move from the **top-left corner to the bottom-right corner** with the **minimum possible sum**.

Allowed moves:

- Right →
- Down ↓

Possible path:

1 → 3 → 1 → 1 → 1

Sum:

1 + 3 + 1 + 1 + 1 = 7

Dynamic Programming table construction:

1 4 5

2 7 6

6 8 7


Final answer = **7**

Each cell stores the **minimum cost to reach that cell**.

---

## 3. Time & Space Complexity

For a matrix with **m rows** and **n columns**:

- Time Complexity: **O(m × n)**
- Space Complexity: **O(m × n)**

Optimized implementations can reduce space complexity to **O(n)**.

---

## 4. Python Code

### Minimum Path Sum Using Dynamic Programming

```python
def min_path_sum(grid):

    rows = len(grid)
    cols = len(grid[0])

    dp = [[0] * cols for _ in range(rows)]

    dp[0][0] = grid[0][0]

    # First row
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # First column
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Fill remaining cells
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[rows-1][cols-1]


grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]

print(min_path_sum(grid))
```
### Output
```python
7
```
---

## 5. Common Interview Problems

- Minimum Path Sum

- Unique Paths in Grid

- Unique Paths with Obstacles

- Maximum Path Sum

- Matrix Chain Multiplication

These problems test understanding of dynamic programming on grids and matrices.

---

## 6. ML Connection

Matrix dynamic programming concepts appear in many machine learning areas:

- Image processing (pixel grid operations)

- Dynamic programming in reinforcement learning

- Path planning algorithms

- Sequence alignment in bioinformatics

- Graph and grid-based optimization

Understanding matrix DP improves the ability to reason about multi-dimensional optimization problems.

---

## 7. Practice Tasks

1. Solve Unique Paths in a Grid

2. Implement Maximum Path Sum

3. Add obstacles to the grid problem

4. Optimize the solution to O(n) space

5. Trace the DP table for small grids manually

These exercises strengthen understanding of dynamic programming on matrices.

---

**Author:**  
Hamna Munir
