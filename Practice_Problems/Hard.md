# Hard Practice Problems

## Overview
This section contains **advanced-level problems** that require strong understanding of **Data Structures and Algorithms (DSA)**.

These problems often involve complex techniques such as **Dynamic Programming, Graph Algorithms, Backtracking, and Optimization strategies**. Each problem includes a **Python implementation and expected output** to demonstrate the solution.

Hard problems help develop **deep algorithmic thinking and efficient problem-solving skills** required for competitive programming and technical interviews.

---

## 1. Longest Increasing Subsequence

### Problem
Given an integer array, return the length of the **longest strictly increasing subsequence**.

Example:

Input

[10,9,2,5,3,7,101,18]


Output

4


Explanation: The longest increasing subsequence is **[2,3,7,101]**.

### Python Code

```python
def longest_increasing_subsequence(nums):
    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


nums = [10,9,2,5,3,7,101,18]

print(longest_increasing_subsequence(nums))
```
### Output
```python
4
```

## 2. Word Ladder (Shortest Transformation Sequence)

### Problem

Given two words (beginWord and endWord) and a dictionary of words, find the length of the shortest transformation sequence from beginWord to endWord.

Example:

Input

beginWord = "hit"

endWord = "cog"

wordList = ["hot","dot","dog","lot","log","cog"]

Output

5

Explanation:

hit → hot → dot → dog → cog

### Python Code
```python
from collections import deque

def word_ladder(beginWord, endWord, wordList):
    wordSet = set(wordList)
    queue = deque([(beginWord, 1)])

    while queue:
        word, steps = queue.popleft()

        if word == endWord:
            return steps

        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                newWord = word[:i] + c + word[i+1:]

                if newWord in wordSet:
                    queue.append((newWord, steps + 1))
                    wordSet.remove(newWord)

    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(word_ladder(beginWord, endWord, wordList))
```
### Output
```python
5
```

## 3. N-Queens Problem
### Problem

Place N queens on an N×N chessboard so that no two queens attack each other.

Example:

Input

n = 4

Output

2

Explanation: There are 2 valid board configurations.

### Python Code
```python
def solve_n_queens(n):

    def backtrack(row):
        if row == n:
            return 1

        count = 0

        for col in range(n):
            if col in cols or (row-col) in diag1 or (row+col) in diag2:
                continue

            cols.add(col)
            diag1.add(row-col)
            diag2.add(row+col)

            count += backtrack(row + 1)

            cols.remove(col)
            diag1.remove(row-col)
            diag2.remove(row+col)

        return count


    cols = set()
    diag1 = set()
    diag2 = set()

    return backtrack(0)


print(solve_n_queens(4))
```
### Output
```python
2
```

## 4. Minimum Spanning Tree (Kruskal’s Algorithm)

### Problem

Find the minimum spanning tree (MST) of a weighted graph.

### Python Code
```python
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


def kruskal(edges, n):
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(n)
    mst = []

    for u, v, w in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, w))

    return mst


edges = [
    (0,1,4),
    (0,2,3),
    (1,2,1),
    (1,3,2),
    (2,3,4)
]

print(kruskal(edges, 4))
```

### Output
```python
[(1, 2, 1), (1, 3, 2), (0, 2, 3)]
```

## 5. Traveling Salesman Problem (TSP)

### Problem

Given a set of cities and distances between them, find the shortest possible route that visits each city exactly once and returns to the starting city.

### Python Code (Dynamic Programming)
```python
from itertools import permutations

def tsp(graph):

    n = len(graph)
    vertices = list(range(1, n))
    min_path = float('inf')

    for perm in permutations(vertices):

        current_cost = 0
        k = 0

        for j in perm:
            current_cost += graph[k][j]
            k = j

        current_cost += graph[k][0]

        min_path = min(min_path, current_cost)

    return min_path


graph = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]

print(tsp(graph))
```

### Output
```python
80
```
---
## Goal

These problems help develop advanced algorithmic thinking, optimization strategies, and deep understanding of complex data structures.

Solving hard problems prepares learners for technical interviews, competitive programming, and real-world algorithmic challenges.

---

**Author:**  
Hamna Munir


