
'''TASK #3
Delivery Route Optimization with Time Windows
● Description: Using the Greedy Best-First Search, optimize delivery routes for a
set of delivery points. Each delivery point has a specific time window for delivery,
and the algorithm must prioritize those with stricter deadlines.
● Challenge: Ensure that the algorithm handles time constraints efficiently while
minimizing total travel distance.'''

# Utility-Based Agent (Greedy BFS)
class DeliveryAgent:
    def __init__(self, goal):
        self.goal = goal

    def greedy_search(self, graph, start, deadlines):
        frontier = [(start, deadlines[start])]
        visited = set()
        path = []
        current = start

        while frontier:
            frontier.sort(key=lambda x: x[1])
            node, _ = frontier.pop(0)

            if node in visited:
                continue

            print(f"Delivering to: {node}")
            visited.add(node)
            path.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    frontier.append((neighbor, deadlines[neighbor]))

        return f"Delivery Order: {path}"

    def act(self, percept, graph, deadlines):
        return self.greedy_search(graph, percept, deadlines)


# Environment
class Environment:
    def __init__(self, graph, deadlines):
        self.graph = graph
        self.deadlines = deadlines

    def get_percept(self, start):
        return start


def run_agent(agent, env, start):
    percept = env.get_percept(start)
    result = agent.act(percept, env.graph, env.deadlines)
    print(result)


graph = {
    'Warehouse': ['A','B'],
    'A': ['C'],
    'B': ['D'],
    'C': [],
    'D': []
}

# Smaller = urgent
deadlines = {
    'Warehouse': 5,
    'A': 2,
    'B': 4,
    'C': 1,
    'D': 3
}

agent = DeliveryAgent(goal=None)
env = Environment(graph, deadlines)

run_agent(agent, env, 'Warehouse')