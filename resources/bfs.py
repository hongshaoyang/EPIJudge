# represent graph with adjacency list

graph = {
    "A": set(["B", "C"]),
    "B": set(["A", "D", "E"]),
    "C": set(["A", "F"]),
    "D": set(["B"]),
    "E": set(["B", "F"]),
    "F": set(["C", "E"])
}

# bfs_cc return nodes accesible from `start`
# use a queue
def bfs_cc(graph, start):
    visited, queue = set(), [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node) # visit the node
            visited.add(node)
            # use `-` operator to exclude visited from queue
            queue.extend(graph[node] - visited)
    return visited


print(bfs_cc(graph, "A"))