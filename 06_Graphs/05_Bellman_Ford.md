# Bellman–Ford Algorithm

## 1. Concept Explanation 
The **Bellman–Ford Algorithm** is a shortest path algorithm used to find the minimum distance from a **source node** to all other nodes in a **weighted graph**, even when **negative edge weights** are present.

Key characteristics:
- Works with **negative weights**
- Can **detect negative weight cycles**
- Uses **relaxation of edges repeatedly**

Unlike Dijkstra’s Algorithm, Bellman–Ford does not use a greedy approach.

---

## 2. Visual / Example

Weighted Graph:
```python
  (0)
 |   \
4|    \5
 v     v
(1)--->(2)
    -3
```

Shortest paths from node `0`:
- 0 → 1 = 4  
- 0 → 2 = 1 (0 → 1 → 2)

---

## 3. Time & Space Complexity

| Metric             | Complexity |
|--------------------|------------|
| Time Complexity    | O(V × E)   |
| Space Complexity   | O(V)       |

Because of its higher time complexity, Bellman–Ford is **slower than Dijkstra** but more flexible.

---

## 4. Python Code

```python
def bellman_ford(graph, vertices, start):
    distances = {v: float("inf") for v in vertices}
    distances[start] = 0

    # Relax edges |V| - 1 times
    for _ in range(len(vertices) - 1):
        for u, v, w in graph:
            if distances[u] != float("inf") and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    # Check for negative weight cycle
    for u, v, w in graph:
        if distances[u] != float("inf") and distances[u] + w < distances[v]:
            print("Graph contains a negative weight cycle")
            return None

    return distances


# Example graph (Edge List)
edges = [
    (0, 1, 4),
    (0, 2, 5),
    (1, 2, -3)
]

vertices = [0, 1, 2]

result = bellman_ford(edges, vertices, 0)

if result:
    print("Shortest distances from node 0:")
    for node in result:
        print(f"Node {node}: {result[node]}")
```
### Output
```python
Shortest distances from node 0:
Node 0: 0
Node 1: 4
Node 2: 1

```
## 5. Common Interview Problems

- Implement Bellman–Ford Algorithm

- Detect negative cycle in graph

- Shortest path with negative edges

- Currency exchange arbitrage detection

- Graph optimization problems

These problems test edge relaxation, loop reasoning, and cycle detection.

---

## 6. ML Connection

Bellman–Ford is useful in ML-related scenarios where negative relationships exist:

- Financial modeling (profit/loss graphs)

- Risk propagation analysis

- Knowledge graph reasoning

- Anomaly detection

- Graph-based optimization models

Negative cycle detection is especially important in inconsistent or unstable systems.

---

## 7. Practice Tasks

1. Modify Bellman–Ford to return actual path

2. Implement negative cycle detection separately

3. Compare Bellman–Ford with Dijkstra

4. Apply Bellman–Ford to currency exchange problem

5. Optimize performance for sparse graphs
---

**Author:**  
Hamna Munir
