class Node():
    def __init__(self, value):
        self.visited = False
        self.value = value
        self.adjacent = []   

# represent graph with adjacency list

graph = {
    "A": set(["B", "C"]),
    "B": set(["A", "D", "E"]),
    "C": set(["A", "F"]),
    "D": set(["B"]),
    "E": set(["B", "F"]),
    "F": set(["C", "E"])
}

# dfs_cc return vertices accesible from `start`
# use a stack
def dfs_cc(graph, start):
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node) # visit the node
            visited.add(node)
            # use `-` operator to exclude visited from stack
            stack.extend(graph[node] - visited)
    return visited


# let's figure this out later
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for n in graph[vertex] - set(path):
            if n == goal:
                yield path + [n]
            else:
                stack.append((n, path + [n]))

print(dfs_cc(graph, "A"))
# print(list(dfs_paths(graph, 'A', 'F')))