# Graphs in Graph Neural Networks (GNN)

## 1. Concept Explanation
A **Graph** is a data structure used to represent relationships between objects. It consists of:

- **Nodes (Vertices)** — represent entities  
- **Edges** — represent connections or relationships between nodes  

In many real-world datasets, information is naturally structured as **relationships**, not just rows and columns. This is where **Graph Neural Networks (GNNs)** become powerful.

A **Graph Neural Network** is a type of machine learning model designed to learn from **graph-structured data**.

Instead of treating data points independently, GNNs learn by **propagating information between connected nodes**.

Each node updates its representation by combining information from its neighbors. This process is often called **message passing** or **neighbor aggregation**.

GNNs are especially useful for problems where relationships between data points matter.

---

## 2. Visual / Example

Example: Social Network Graph
```python
    Alice
    /   \
 Bob     Carol
   \     /
    David
```

Explanation:

- Each **person is a node**
- Each **friendship is an edge**
- Information can flow between connected nodes

In a GNN:

- Alice's representation depends on **Bob and Carol**
- Bob's representation depends on **Alice and David**

The model learns by aggregating neighbor information across the graph.

---

## 3. Time & Space Complexity

The complexity of graph neural networks depends on:

- Number of **nodes (V)**
- Number of **edges (E)**
- Number of **layers**

Typical complexity for one GNN layer:

- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V + E)

For large graphs, specialized frameworks and sampling techniques are often used.

---

## 4. Python Code

### Graph Representation Example

```python
# Graph represented as adjacency list

graph = {
    "Alice": ["Bob", "Carol"],
    "Bob": ["Alice", "David"],
    "Carol": ["Alice"],
    "David": ["Bob"]
}

print(graph)
```
### Output

```python
{
 'Alice': ['Bob', 'Carol'],
 'Bob': ['Alice', 'David'],
 'Carol': ['Alice'],
 'David': ['Bob']
}

```
### Simple Neighbor Aggregation (GNN Idea)

```python
# Node features
features = {
    "Alice": 1,
    "Bob": 2,
    "Carol": 3,
    "David": 4
}

# Graph connections
graph = {
    "Alice": ["Bob", "Carol"],
    "Bob": ["Alice", "David"],
    "Carol": ["Alice"],
    "David": ["Bob"]
}

def aggregate(node):
    neighbors = graph[node]
    total = features[node]

    for n in neighbors:
        total += features[n]

    return total / (len(neighbors) + 1)


for node in graph:
    print(node, "new feature:", aggregate(node))

```

### Output

```python
Alice new feature: 2.0
Bob new feature: 2.3333333333333335
Carol new feature: 2.0
David new feature: 3.0

```
Explanation:

- Each node updates its value using information from its neighbors, similar to how GNN layers work.

---

## 5. Common Interview Problems

- Graph traversal using BFS

- Graph traversal using DFS

- Shortest path algorithms

- Cycle detection in graphs

- Topological sorting

Understanding graph algorithms helps when working with graph-based ML models.

---

## 6. ML Connection

Graphs are extremely important in modern machine learning.

Applications include:

- Social network analysis

- Recommendation systems

- Fraud detection

- Knowledge graphs

- Molecular structure prediction

- Traffic and transportation networks

Popular graph ML models include:

- Graph Neural Networks (GNN)

- Graph Convolutional Networks (GCN)

- Graph Attention Networks (GAT)

These models learn patterns not only from node features but also from relationships between nodes.

---

## 7. Practice Tasks

1. Represent a graph using an adjacency list

2. Implement BFS traversal

3. Implement DFS traversal

4. Simulate a simple neighbor aggregation step

5. Explore graph datasets used in machine learning

Practicing graph algorithms builds a strong foundation for graph-based machine learning models

---

**Author:**  
Hamna Munir
