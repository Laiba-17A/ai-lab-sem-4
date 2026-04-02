
def best_first(graph, start, goal, h):
    queue = [(h[start], start, [start])]   # (heuristic, node, path)
    visited = []

    while queue:
        queue.sort()   # smallest heuristic first
        heuristic, node, path = queue.pop(0)

        if node == goal:
            return path

        if node not in visited:
            visited.append(node)

            for child, cost in graph.get(node, []):
                queue.append((h[child], child, path + [child]))

    return None


# =========================
# GRAPH
# =========================
graph = {
    "T0": [("T1", 1), ("T2", 1)],
    "T1": [("T3", 1), ("T4", 1)],
    "T2": [("T5", 1)],
    "T3": [("T6", 1)],
    "T4": [("T6", 1)],
    "T5": [("T6", 1)],
    "T6": []
}

# =========================
# HEURISTICS
# =========================
h = {
    "T0": 5,
    "T1": 3,
    "T2": 4,
    "T3": 2,
    "T4": 1,
    "T5": 2,
    "T6": 0
}

# =========================
# RUN
# =========================
path = best_first(graph, "T0", "T6", h)
print("Task execution order:", path)