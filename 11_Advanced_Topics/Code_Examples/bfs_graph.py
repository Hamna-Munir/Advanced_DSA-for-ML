# Graph Algorithm Example
# Breadth First Search (BFS)

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


# Output
# A
# B
# C
# D
