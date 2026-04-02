def bfs(graph, start, goal):
    queue = [(start, [start])]   # store node and path
    visited = []

    while queue:
        node, path = queue.pop(0)   # remove first element

        if node == goal:            # if goal found
            return path

        if node not in visited:
            visited.append(node)

            # add children with updated path
            for child in graph[node]:
                queue.append((child, path + [child]))

    return None

def dfs(graph, start, goal):
    stack = [(start, [start])]   # node, path
    visited = []

    while stack:
        node, path = stack.pop()

        if node == goal:
            return path

        if node not in visited:
            visited.append(node)

            # reverse so left child comes first
            for child in reversed(graph[node]):
                stack.append((child, path + [child]))

    return None


def dls(graph, start, goal, limit):
    stack = [(start, [start], 0)]
    visited = []

    while stack:
        node, path, depth = stack.pop()

        if node == goal:
            return path

        if node not in visited and depth < limit:
            visited.append(node)

            # reverse for correct DFS order
            for child in reversed(graph[node]):
                stack.append((child, path + [child], depth + 1))

    return None

def ids(graph, start, goal, max_depth):
    for limit in range(max_depth + 1):   # try 0 to max_depth
        result = dls(graph, start, goal, limit)

        if result:
            return result

    return None

def ucs(graph, start, goal):
    queue = [(0, start, [start])]   # cost, node, path
    visited = []

    while queue:
        queue.sort()                # smallest cost first
        cost, node, path = queue.pop(0)

        if node == goal:
            return path, cost

        if node not in visited:
            visited.append(node)

            # add children with total cost
            for child, edge_cost in graph[node]:
                queue.append((cost + edge_cost, child, path + [child]))

    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

print(bfs(graph, 'A', 'G'))
print(dfs(graph, 'A', 'G'))
print(dls(graph, 'A', 'G', 3))
print(ids(graph, 'A', 'G', 5))

graph_cost = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('G', 1)],
    'F': [],
    'G': []
}

print(ucs(graph_cost, 'A', 'G'))