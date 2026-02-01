# Depth-First Search (DFS)

## 1. Concept Explanation 
**Depth-First Search (DFS)** is a graph traversal algorithm that explores a graph by going **as deep as possible** along each path before backtracking.

- Starts from a source node  
- Explores one neighbor completely  
- Backtracks when no unvisited neighbors remain  

DFS is implemented using:
- **Recursion**, or  
- An explicit **stack**

DFS is ideal for exploring **structure, connectivity, and dependencies** in graphs.

---

## 2. Visual / Example

Graph:
```python
 0
/ \
1 2
| |
3 4
```

DFS starting from node `0`:

0 → 1 → 3 → 2 → 4


Traversal goes **deep first**, then backtracks.

---

## 3. Time & Space Complexity

| Metric             | Complexity |
|--------------------|------------|
| Time Complexity    | O(V + E)   |
| Space Complexity   | O(V)       |

Space complexity depends on:
- Recursion stack (or explicit stack)
- Visited nodes

---

## 4. Python Code

### Recursive DFS
```python
def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Example graph
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1],
    4: [2]
}

visited = set()

print("DFS Traversal:")
dfs(graph, 0, visited)
```
Output
```python
DFS Traversal:
0 1 3 2 4
```
Iterative DFS (Using Stack)
```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)


print("\nIterative DFS Traversal:")
dfs_iterative(graph, 0)
```
Output
```python
Iterative DFS Traversal:
0 1 3 2 4

```
## 5. Common Interview Problems

- DFS traversal of graph

- Detect cycle in graph

- Topological sorting

- Finding connected components

- Path existence between nodes

These problems test recursion, backtracking, and stack management.

---

## 6. ML Connection

DFS plays an important role in ML-related systems:

- Feature dependency graphs

- Graph-based anomaly detection

- Topological ordering in ML pipelines

- Knowledge graph exploration

- Graph Neural Network preprocessing

DFS is often used when:

- Full exploration is required

- Structure matters more than distance

---


## 7. Practice Tasks

1. Implement DFS for directed graph

2. Detect cycle using DFS

3. Count connected components using DFS

4. Perform topological sort using DFS

5. Convert recursive DFS to iterative DFS
---

**Author:**  
Hamna Munir
