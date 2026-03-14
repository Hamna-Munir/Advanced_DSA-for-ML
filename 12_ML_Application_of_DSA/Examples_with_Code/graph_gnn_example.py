# Graph Example for GNN Concept
# Simple neighbor aggregation

# Node features
features = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4
}

# Graph connections
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}

def aggregate(node):

    neighbors = graph[node]
    total = features[node]

    for n in neighbors:
        total += features[n]

    return total / (len(neighbors) + 1)


for node in graph:
    print(node, "updated feature:", aggregate(node))


# Output
# A updated feature: 2.0
# B updated feature: 2.3333333333333335
# C updated feature: 2.0
# D updated feature: 3.0
