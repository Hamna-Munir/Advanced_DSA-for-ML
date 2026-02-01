import heapq

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        current_dist, node = heapq.heappop(pq)

        if current_dist > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# Example graph
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

# OUTPUT
# Shortest distances from node 0:
# Node 0: 0
# Node 1: 1
# Node 2: 4
# Node 3: 3
