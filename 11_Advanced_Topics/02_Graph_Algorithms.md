# Graph Algorithms

## 1. Concept Explanation
A **Graph** is a data structure used to represent relationships between objects.

It consists of:

- **Vertices (Nodes)** — represent entities  
- **Edges** — represent connections between nodes  

Graphs are widely used to model real-world systems such as:

- Social networks
- Road maps
- Computer networks
- Recommendation systems

**Graph Algorithms** are used to traverse, analyze, and extract information from graph structures.

Common graph operations include:

- Traversing nodes
- Finding shortest paths
- Detecting cycles
- Searching relationships
- Finding optimal connections

Graphs can be represented in two common ways:

- **Adjacency List**
- **Adjacency Matrix**

---

## 2. Visual / Example

Example Graph:

A ----- B
|       |
|       |
C ----- D

Adjacency List Representation:


A → B, C
B → A, D
C → A, D
D → B, C


Adjacency Matrix Representation:

A B C D

A [ 0 1 1 0 ]
B [ 1 0 0 1 ]
C [ 1 0 0 1 ]
D [ 0 1 1 0 ]


Graphs can be:

- **Directed** (edges have direction)
- **Undirected** (edges are bidirectional)
- **Weighted** (edges have costs)

---

## 3. Time & Space Complexity

Complexity depends on graph representation.

For a graph with **V vertices** and **E edges**:

Adjacency List:

- Space Complexity: **O(V + E)**

Adjacency Matrix:

- Space Complexity: **O(V²)**

Traversal algorithms such as **DFS** and **BFS**:

- Time Complexity: **O(V + E)**

---

## 4. Python Code

### Graph Representation (Adjacency List)

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

print(graph)
```
### Output
```python
{'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C']}
```
### Depth First Search (DFS)
```python
def dfs(graph, node, visited):

    if node not in visited:
        print(node)
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}

visited = set()

dfs(graph, "A", visited)
```
### Output
```python
A
B
D
C
```
### Breadth First Search (BFS)
```python
from collections import deque

def bfs(graph, start):

    visited = set()
    queue = deque([start])

    while queue:

        node = queue.popleft()

        if node not in visited:
            print(node)
            visited.add(node)

            for neighbor in graph[node]:
                queue.append(neighbor)


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}

bfs(graph, "A")
```
### Output
```python
A
B
C
D
```
---

## 5. Common Interview Problems

- Depth First Search (DFS)

- Breadth First Search (BFS)

- Shortest Path (Dijkstra Algorithm)

- Minimum Spanning Tree (Kruskal / Prim)

- Cycle Detection in Graph

- Topological Sorting

These problems test understanding of graph traversal and connectivity.

---

## 6. ML Connection

Graphs are extremely important in modern machine learning.

Applications include:

- Graph Neural Networks (GNNs)

- Knowledge graphs

- Recommendation systems

- Social network analysis

- Fraud detection

Graph algorithms help analyze relationships between entities in complex datasets.

---

## 7. Practice Tasks

1. Implement DFS using stack

2. Implement BFS using queue

3. Detect a cycle in a graph

4. Find shortest path using Dijkstra

5. Implement topological sort

Practicing graph problems builds strong algorithmic thinking.

---

**Author:**  
Hamna Munir
