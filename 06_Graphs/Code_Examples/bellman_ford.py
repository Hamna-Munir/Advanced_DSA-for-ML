def bellman_ford(edges, vertices, start):
    distance = {v: float("inf") for v in vertices}
    distance[start] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if distance[u] != float("inf") and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    for u, v, w in edges:
        if distance[u] != float("inf") and distance[u] + w < distance[v]:
            print("Negative weight cycle detected")
            return None

    return distance


# Example
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


# OUTPUT
# Shortest distances from node 0:
# Node 0: 0
# Node 1: 4
# Node 2: 1
