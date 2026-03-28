'''Q1 Iran vs. USA (The Diplomatic Drone)
Tensions are high , War is imminent between Iran and the USA! You are the lead AI engineer for
the United Nations. Your task is to guide a high-speed "Diplomatic Drone" from 'Tehran' to
'Washington' to deliver a last-minute peace treaty. The airspace is a network of cities, but some
routes are faster than others. You must find the shortest path (fewest stops) to prevent total
destruction. Graph:
● 'Tehran' connects to ['Baghdad', 'Istanbul']
● 'Baghdad' connects to ['Cairo']
● 'Istanbul' connects to ['Berlin']
● 'Cairo' connects to ['Washington'] (The Goal!)
● 'Berlin' connects to ['Washington']

Task: Write a Python program using BFS that starts at 'Tehran', explores the neighboring
cities level-by-level, and stops immediately when it reaches 'Washington'. Print the path the
drone takes to save the world!'''

class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def bfs(self, graph, start):
        queue = [[start]]
        visited = []

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node not in visited:
                print(f"Visiting: {node}")
                visited.append(node)

                if node == self.goal:
                    return f"Path found: {path}"

                for neighbor in graph[node]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

        return "Goal not found"

    def act(self, percept, graph):
        return self.bfs(graph, percept)


class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node


def run_agent(agent, env, start):
    percept = env.get_percept(start)
    print(agent.act(percept, env.graph))


graph = {
    'Tehran': ['Baghdad', 'Istanbul'],
    'Baghdad': ['Cairo'],
    'Istanbul': ['Berlin'],
    'Cairo': ['Washington'],
    'Berlin': ['Washington']
}

agent = GoalBasedAgent('Washington')
env = Environment(graph)

run_agent(agent, env, 'Tehran')