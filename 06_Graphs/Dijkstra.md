# Dijkstra’s Algorithm

## 1. Concept Explanation (Simple English)
**Dijkstra’s Algorithm** is a **shortest path algorithm** used to find the minimum distance from a **source node** to all other nodes in a **weighted graph**.

Key points:
- Works only when **edge weights are non-negative**
- Uses a **greedy approach**
- Always expands the node with the **currently smallest known distance**

It is widely used in routing, recommendation systems, and optimization problems.

---

## 2. Visual / Example

Weighted Graph:
```python

       1
  (0) ----> (1)
  |          |
4 |          | 2
  v          v
 (2) ----> (3)
       1
```

Starting from node `0`, shortest paths:
- 0 → 1 = 1
- 0 → 2 = 4
- 0 → 3 = 3 (0 → 1 → 3)

---

## 3. Time & Space Complexity

| Implementation            | Time Complexity |
|---------------------------|-----------------|
| Using Priority Queue      | O((V + E) log V) |
| Using Adjacency Matrix    | O(V²)           |

| Metric             | Complexity |
|--------------------|------------|
| Space Complexity   | O(V)       |

---

## 4. Python Code

```python
import heapq

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example graph (Adjacency List with weights)
graph = {
    0: [(1, 1), (2, 4)],
    1: [(3, 2)],
    2: [(3, 1)],
    3: []
}

result = dijkstra(graph, 0)

print("Shortest distances from node 0:")
for node in result:
    print(f"Node {node}: {result[node]}")
```
### Output
```python
Shortest distances from node 0:
Node 0: 0
Node 1: 1
Node 2: 4
Node 3: 3
```
## 5. Common Interview Problems

- Implement Dijkstra’s Algorithm

- Shortest path between two nodes

- Network delay time

- Minimum cost path

- Graph routing problems

These problems test priority queues, greedy logic, and graph traversal.

---

## 6. ML Connection

Dijkstra’s Algorithm is highly relevant in ML systems:

- Recommendation systems (user-item distance)

- Routing and navigation models

- Graph-based similarity scoring

- Cost optimization in ML pipelines

- Knowledge graph inference

In large-scale ML:

- Used during preprocessing

- Used in graph feature engineering

- Often combined with embeddings

---

## 7. Practice Tasks

1. Modify Dijkstra to return actual shortest path

2. Implement Dijkstra using adjacency matrix

3. Compare BFS vs Dijkstra on weighted graphs

4. Handle disconnected graphs

5. Optimize Dijkstra for large graphs
---

**Author:**  
Hamna Munir
