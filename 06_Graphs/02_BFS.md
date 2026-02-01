# Breadth-First Search (BFS)

## 1. Concept Explanation 
**Breadth-First Search (BFS)** is a graph traversal algorithm that explores a graph **level by level**.

- It starts from a given source node  
- Visits all its immediate neighbors first  
- Then moves to neighbors of neighbors  

BFS guarantees the **shortest path (minimum edges)** in an **unweighted graph**.

It uses a **queue** data structure to manage traversal order.

---

## 2. Visual / Example

Graph:
```python
 0
/ \
1  2
|  |
3  4
```

BFS starting from node `0`:

0 → 1 → 2 → 3 → 4


Traversal expands **horizontally** before going deeper.

---

## 3. Time & Space Complexity

| Metric             | Complexity |
|--------------------|------------|
| Time Complexity    | O(V + E)   |
| Space Complexity   | O(V)       |

Where:
- `V` = number of vertices  
- `E` = number of edges  

Space complexity accounts for the queue and visited nodes.

---

## 4. Python Code

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Example graph (Adjacency List)
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1],
    4: [2]
}

print("BFS Traversal:")
bfs(graph, 0)
```
Output

```python
BFS Traversal:
0 1 2 3 4
```
## 5. Common Interview Problems

- BFS traversal of a graph

- Shortest path in unweighted graph

- Level order traversal in trees

- Finding connected components

- Word ladder problem

These problems test queue usage, visited tracking, and traversal logic.

---

## 6. ML Connection

BFS is widely used in ML-related systems:

- Graph Neural Networks (GNNs) neighborhood expansion

- Recommendation systems (user-to-user distance)

- Social network analysis (degrees of separation)

- Web crawling and indexing

- Knowledge graph traversal

In ML pipelines, BFS helps in:

- Feature expansion

- Neighborhood sampling

- Graph-based exploration

---

## 7. Practice Tasks

1. Implement BFS using adjacency matrix

2. Find shortest path between two nodes using BFS

3. Detect connected components using BFS

4. Implement BFS for a directed graph

5. Modify BFS to return distance array

---

**Author:**  
Hamna Munir
