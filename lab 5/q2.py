

'''TASK #2
Implement an A* Search where the edge costs change dynamically at random intervals.
The algorithm should adapt to these changes and always find the optimal path.
Recompute and adjust paths in real time without restarting the algorithm from scratch.'''

import random

# Agent
class AStarAgent:
    def __init__(self, goal):
        self.goal = goal

    def heuristic(self, node):
        return abs(ord(node) - ord(self.goal))  # simple heuristic

    def a_star(self, graph, start):
        frontier = [(start, 0)]
        g_cost = {start: 0}
        came_from = {start: None}
        visited = set()

        while frontier:
            frontier.sort(key=lambda x: x[1])
            node, _ = frontier.pop(0)

            if node in visited:
                continue

            print(f"Visiting: {node}")
            visited.add(node)

            if node == self.goal:
                path = []
                while node:
                    path.append(node)
                    node = came_from[node]
                return path[::-1]

            for neighbor in graph[node]:
                # Dynamic cost change
                dynamic_cost = random.randint(1, 10)

                new_g = g_cost[node] + dynamic_cost
                f = new_g + self.heuristic(neighbor)

                if neighbor not in g_cost or new_g < g_cost[neighbor]:
                    g_cost[neighbor] = new_g
                    came_from[neighbor] = node
                    frontier.append((neighbor, f))

        return "Goal not found"

    def act(self, percept, graph):
        return self.a_star(graph, percept)


# Environment
class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, start):
        return start


def run_agent(agent, env, start):
    percept = env.get_percept(start)
    print(agent.act(percept, env.graph))


graph = {
    'A': ['B','C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

agent = AStarAgent('E')
env = Environment(graph)

run_agent(agent, env, 'A')