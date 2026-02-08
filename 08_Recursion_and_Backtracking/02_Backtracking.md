# Backtracking

## 1. Concept Explanation 
**Backtracking** is an algorithmic technique used to explore all possible solutions to a problem by building candidates step by step and abandoning a candidate (“backtracking”) when it cannot lead to a valid solution.

It is essentially recursion with decision-making and undoing choices.

Backtracking works by:

1. Making a choice  
2. Exploring that choice recursively  
3. Undoing the choice if it fails  

This systematic exploration guarantees that all valid solutions are considered.

Backtracking is commonly used in combinatorial problems, puzzles, and search problems.

---

## 2. Visual / Example

Example: Generate permutations of `[1, 2]`

Decision tree:

Start
├── Choose 1 → [1]

│ └── Choose 2 → [1, 2]

└── Choose 2 → [2]

└── Choose 1 → [2, 1]


The algorithm explores a path, completes it, then backtracks to try another path.

---

## 3. Time & Space Complexity

Backtracking often explores many possibilities.

For permutation generation:

- Time Complexity: **O(n!)**
- Space Complexity: **O(n)** (recursion stack)

Performance depends on the size of the search space.

---

## 4. Python Code

### Generate All Permutations

```python
def permutations(nums, path=[], result=[]):
    if not nums:
        result.append(path)
        return

    for i in range(len(nums)):
        permutations(nums[:i] + nums[i+1:], path + [nums[i]], result)

    return result

print(permutations([1, 2]))
```
### Output
```python

[[1, 2], [2, 1]]
```
### Simple Backtracking — Subsets
```python

def subsets(nums, index=0, path=[], result=[]):
    result.append(path)

    for i in range(index, len(nums)):
        subsets(nums, i + 1, path + [nums[i]], result)

    return result
print(subsets([1, 2]))
```
### Output
```python

[[], [1], [1, 2], [2]]
```
## 5. Common Interview Problems

- Generate permutations/combinations

- N-Queens problem

- Sudoku solver

- Subset generation

- Word search problems

These test exploration, pruning, and recursive reasoning.

---

## 6. ML Connection

Backtracking concepts appear in ML and AI systems:

- Search algorithms in optimization

- Constraint satisfaction problems

- Decision tree exploration

- State-space search

- Pathfinding and reasoning models

Understanding backtracking strengthens algorithm design skills for complex systems.

---

## 7. Practice Tasks

1. Generate all permutations of a list

2. Create all subsets of a set

3. Solve N-Queens for small boards

4. Build a recursive combination generator

5. Trace decision trees manually

Practice builds intuition for exploring solution spaces efficiently.

---

**Author:**  
Hamna Munir


