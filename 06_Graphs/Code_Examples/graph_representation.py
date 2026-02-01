# Graph Representation using Adjacency List

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
            print(f"{node} -> {self.graph[node]}")


# Example
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

g.display()


# OUTPUT
# 0 -> [1, 2]
# 1 -> [0, 3]
# 2 -> [0, 3]
# 3 -> [1, 2]
