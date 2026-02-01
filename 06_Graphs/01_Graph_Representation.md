# Graph Representation

## 1. Concept Explanation (Simple English)
A **Graph** is a data structure used to represent **relationships** between entities.

A graph consists of:
- **Vertices (Nodes)** → entities
- **Edges** → connections between entities

How a graph is represented in memory has a **direct impact on performance, scalability, and algorithm efficiency**.  
Choosing the right representation is critical in **Machine Learning systems dealing with large networks**.

---

## 2. Types of Graphs

### Directed Graph
Edges have direction.

A → B → C


### Undirected Graph
Edges have no direction.

A — B — C


### Weighted Graph
Edges have weights (cost, distance, similarity).

A --5--> B


### Unweighted Graph
Edges have no weights.

---

## 3. Graph Representation Methods

### 1. Adjacency Matrix
A 2D matrix where:
- Rows = source vertices
- Columns = destination vertices

Example graph:

0 — 1
| |
2 — 3


Adjacency Matrix:

0 0 1 1 0
1 1 0 0 1
2 1 0 0 1
3 0 1 1 0


**Pros**
- Fast edge lookup O(1)

**Cons**
- High memory usage O(V²)

---

### 2. Adjacency List
Each vertex stores a list of connected vertices.

Example:

0 → [1, 2]
1 → [0, 3]
2 → [0, 3]
3 → [1, 2]


**Pros**
- Space efficient O(V + E)
- Preferred for large graphs

**Cons**
- Edge lookup slower than matrix

---

### 3. Edge List
Graph stored as list of edges.

Example:

(0,1), (0,2), (1,3), (2,3)


**Pros**
- Simple structure
- Useful for algorithms like Bellman-Ford

**Cons**
- Slow traversal and lookup

---

## 4. Time & Space Complexity

| Representation      | Space Complexity | Edge Lookup |
|---------------------|------------------|-------------|
| Adjacency Matrix    | O(V²)            | O(1)        |
| Adjacency List      | O(V + E)         | O(deg(V))   |
| Edge List           | O(E)             | O(E)        |

Choosing the wrong representation can **severely impact ML system performance**.

---

## 5. Python Code

### Adjacency List Representation
```python
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)  # Undirected graph

    def display(self):
        for node in self.graph:
            print(node, "->", self.graph[node])


# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

g.display()
```
Output
```python
0 -> [1, 2]
1 -> [0, 3]
2 -> [0, 3]
3 -> [1, 2]
```
---

## 6. ML Connection

Graph representation is fundamental in ML applications:

- Graph Neural Networks (GNNs) use adjacency lists or matrices

- Recommendation systems model users and items as nodes

- Knowledge graphs represent entities and relationships

- Social network analysis relies heavily on graph traversal

Choosing adjacency list vs matrix directly affects:

- Memory usage

- Training speed

- Scalability to millions of nodes

Most large-scale ML systems prefer adjacency lists.

---

## 7. Practice Tasks

1. Implement directed graph using adjacency list

2. Implement weighted graph representation

3. Convert adjacency list to adjacency matrix

4. Implement edge list representation

5. Compare memory usage of different representations

---

**Author:**  
Hamna Munir
