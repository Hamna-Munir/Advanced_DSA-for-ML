# Graph Algorithm Example
# Depth First Search (DFS)

def dfs(graph, node, visited):

    if node not in visited:
        print(node)
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}

visited = set()

dfs(graph, "A", visited)


# Output
# A
# B
# D
# C
